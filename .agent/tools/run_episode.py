# -*- coding: utf-8 -*-
"""
Episode Runner
==============

One command per episode. Builds the packet, refuses to proceed if preflight
fails, invokes Codex from the repository root, then runs the quantitative gate.

  python .agent/tools/run_episode.py E003
  python .agent/tools/run_episode.py E003 --gate-only    # re-run the gate
  python .agent/tools/run_episode.py E003 --dry          # print the prompt

Codex must run with the repository as its working root. Going through the
companion put the writable root somewhere else and cost a full drafting pass
that could not be saved, so this calls `codex exec -C <repo>` directly.
"""

import io
import os
import re
import sys
import json
import argparse
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, ".agent", "tools"))

import importlib.util
_spec = importlib.util.spec_from_file_location(
    "bep", os.path.join(ROOT, ".agent", "tools", "build_episode_packet.py"))
bep = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bep)


# --------------------------------------------------------------------------
# Title lookup
# --------------------------------------------------------------------------

def title_for(n):
    """Working title from the subact hub's episode-breakdown table.

    The hub holds several tables keyed by episode id. Take the first cell that
    actually looks like a title: not a density code, not a movement path, not a
    prohibition list. E003 first matched the movement table and shipped as
    '증거실 → 피해 계산실 → 폐기기록 보관대'.
    """
    r = bep.route(n)
    hub = bep.rd(r["hub"]) or ""
    for line in hub.split("\n"):
        cells = [c.strip() for c in line.split("|")]
        if len(cells) < 3 or cells[1] != "E%03d" % n:
            continue
        # The episode-breakdown table is the wide one: id, title, density,
        # hook, links. Movement (3 cells) and prohibitions (2) are narrower.
        if len(cells) < 6:
            continue
        t = cells[2]
        if t and "→" not in t and "장면" not in t:
            return t
    t2 = bep.rd("docs/10_story_architecture/v1-episode-titles-v1.md") or ""
    m2 = re.search(r"^\|\s*E%03d\s*\|\s*([^|]+?)\s*\|" % n, t2, re.M)
    return m2.group(1).strip() if m2 else "제목-미정"


def slug(t):
    return re.sub(r"[^\w가-힣]+", "-", t).strip("-")


# --------------------------------------------------------------------------
# Prompt
# --------------------------------------------------------------------------

PROMPT = """Write episode {ep} of the Korean web novel 《왕국은 과거를 먹고 산다》 as new prose in Korean.

Output file: {out}

You are the prose writer. The design is fixed; your job is sentences, not story decisions.

READ FIRST, IN THIS ORDER:
1. {manifest} — YOUR PACKET. If it has a "Hand triage" section, that section OVERRIDES the auto-generated sections above it. Follow its scene table exactly.
2. {prev_state} — the previous episode's exit. This is your entry state. Its JIT_RESOLVED_VALUES are fixed surface details that must stay consistent.
3. {prev_ms} — the immediately preceding episode, for voice continuity and to avoid repeating its structure. This is the ONLY manuscript file you may read.
4. {hub} — subact hub: cast, institutions, assets, active mysteries, prohibitions. Read its 금지 row for this episode and obey it.
5. .agent/skills/sentence-narrator/SKILL.md — sections 2, 5, 6, 7, 8, 9, 10, 11, 12, 16.
6. .agent/skills/human-prose-audit/SKILL.md — section 3.
7. docs/13_writing_harness/anti-padding-policy-v1.md
8. docs/05_characters/hubs/C01-에이든-로엔.md — sections 말투, 사상·거짓 믿음, 이 인물이 모르는 것. Plus the hub of any other named character the packet lists.

DO NOT READ: Drafts/, lore_bible/, outline/, Guidelines/, .agent/context-packs/episodes/, any manuscript file other than {prev_ms}, and any craft manifest other than the one named above.

The legacy manuscript has been removed from the working tree. manuscript/ now holds only this run's episodes. Do not attempt to recover legacy text from git history.

HARD CONSTRAINTS:
- Korean prose. Close third on the POV character named in the packet. No head-hopping.
- Minimum 7000 characters including spaces. If short, add a missing scene function from the packet — never longer sentences or repeated description.
- Exactly {scenes} scenes, separated by a line containing only ***
- Obey the packet's "DO NOT REVEAL" list. A clue may appear; its answer may not be stated by narration or dialogue.
- Obey the packet's forbidden hook/density/craft carried from previous episodes.
- 에이든 refers to 세렌 바일 only as 표적, never by name, until the design says otherwise.
- No surname-alone address. 세른 기록관 / 로엔 요원 / 네르 대표 are correct; the bare surname is not.
- Sentence breath: at most 8 short sentences (20 chars or fewer) consecutively in NARRATION; at least 5 percent of narration sentences over 40 chars. Dialogue is not counted.
- Do not invent events, settings, characters, institutions, time-laws, foreshadowing or reveals. Surface detail only where the design is silent, and only where it cannot change a choice, causality, an information ceiling, or a permanent loss.
- No institution or functionary is a villain, saboteur, or traitor. Opposition has real reasons and real casualties.
- Do not end a scene with an aphorism, a thematic summary, or a symmetrical contrast construction. Do not name an emotion then re-illustrate it with an action.
- Read-aloud rules from prior audits:
{alerts}

FILE FORMAT: H1 line '# {ep} — {title}', then prose. Scenes split by ***. Prose only. No commentary, no scene labels, no design notes.

SECOND OUTPUT — also write {state_out}:
A state mutation recording ONLY what changed, using the same section headings as {prev_state}. Include a JIT_RESOLVED_VALUES table listing every surface detail you invented, so later episodes stay consistent. End with NEXT_ENTRY_HANDOFF describing the entry state for the following episode. Do not claim HUMAN PROSE PASS.

AFTER WRITING report: character count including spaces; longest run of consecutive short narration sentences; percentage of narration sentences over 40 chars.
"""


def build_prompt(n, p):
    r = p["route"]
    t = title_for(n)
    return PROMPT.format(
        ep=r["episode"], title=t,
        out="manuscript/volume-%02d/%s-%s.md" % (r["vol_n"], r["episode"], slug(t)),
        state_out="manuscript/state/%s-state-mutation.md" % r["episode"],
        manifest="docs/10_story_architecture/craft-manifests/%s-craft-manifest-auto.md" % r["episode"],
        prev_state=p["previous_exit"],
        prev_ms=prev_manuscript(n) or "(none - series entry)",
        hub=r["hub"],
        scenes=p["density"]["scenes"] if p["density"] else 3,
        alerts="\n".join("  - " + a for a in p["alerts"]),
    )


def prev_manuscript(n):
    if n <= 1:
        return None
    d = os.path.join(ROOT, "manuscript", "volume-%02d" % ((n - 2) // 25 + 1))
    if not os.path.isdir(d):
        return None
    for f in os.listdir(d):
        if f.startswith("E%03d-" % (n - 1)):
            return "manuscript/volume-%02d/%s" % ((n - 2) // 25 + 1, f)
    return None


# --------------------------------------------------------------------------
# Quantitative gate
# --------------------------------------------------------------------------

def narration_text(narr):
    """Narration with inline quotes stripped, so dialogue register is not
    judged by narration rules."""
    return "\n".join(re.sub(r"[“\"][^”\"]*[”\"]", "", p) for p in narr)


def gate(path, expected_scenes, prev_hook=None):
    t = io.open(os.path.join(ROOT, path), encoding="utf-8").read()
    body = t.split("\n", 1)[1] if "\n" in t else ""
    lines = [l for l in body.split("\n") if l.strip() and l.strip() != "***"]
    dial = [l for l in lines if l.strip()[:1] in '"“―—「']
    narr = [l for l in lines if l not in dial]

    sents = []
    for pg in narr:
        s = re.sub(r"[“\"][^”\"]*[”\"]", "", pg)
        # Split on sentence-ending punctuation only.
        #
        # The old pattern also split after a bare 다 followed by space, which
        # cuts inside 다시, 다음, 한 번에 다, and so on. That inflated the
        # short-sentence count in every episode measured so far and finally
        # halted the chain at E042 on a run of 9 that is really 8.
        for x in re.split(r"(?<=[.!?…])\s+", s):
            if len(x.strip()) >= 2:
                sents.append(x.strip())

    runs, c = [], 0
    for x in sents:
        if len(x) <= 20:
            c += 1
        else:
            if c:
                runs.append(c)
            c = 0
    if c:
        runs.append(c)

    chars = len(body.replace("***", ""))
    long_pct = sum(1 for x in sents if len(x) > 40) / max(len(sents), 1) * 100
    scenes = t.count("***") + 1

    checks = [
        ("chars >= 7000", chars >= 7000, chars),
        ("scene count", scenes == expected_scenes, "%d (want %d)" % (scenes, expected_scenes)),
        ("short run <= 8", (max(runs) if runs else 0) <= 8, max(runs) if runs else 0),
        ("long >= 5%", long_pct >= 5, round(long_pct, 1)),
        # Only the two that are translationese wherever they appear.
        #
        # sentence-narrator 5.3 calls these 번역체 표지 - signals, not banned
        # words - and the same section says dialogue is not counted, because
        # each character needs their own register. Treating a single 에 대한
        # as a hard failure halted the chain at E021 over one line of a
        # records-keeper's ordinary administrative speech: "장부가 없어지면
        # 표적에 대한 판정도 사라집니다."
        ("no translationese", not re.search(r"되어졌", t)
         and not re.search(r"에 의해", narration_text(narr)), ""),
        # Bare surname only. A full name (리아 세른) and a trailing title
        # (세른 기록관) are both correct; the retroactive run on E001 flagged
        # "참관 기록관 리아 세른" until the given-name lookbehind was added.
        # Wrong target, not wrong threshold.
        ("no bare surname", not re.search(
            r"(?<![가-힣])(?<!에이든 )(?<!리아 )(?<!아이리스 )(?<!마르칸 )(?<!오르바드 )"
            r"(?<!세렌 )(?<!다렌 )(?<!엘사 )(?<!아벨 )(?<!하렌 )"
            r"(로엔|세른|네르)(?![ ]?(?:요원|기록관|대표|가문))(?![가-힣])", t), ""),
        ("no episode id in prose", len(re.findall(r"E\d{3}", body)) == 0,
         re.findall(r"E\d{3}", body)[:3]),
    ]
    nt = narration_text(narr)
    per10k = lambda p: len(re.findall(p, nt)) / max(len(nt), 1) * 10000
    warns = [
        ("scene ends on weak landing", any(
            re.search(r"(고 있었다|고 있다|것을 보았다)[.”\"]?\s*$", s.strip())
            for s in t.split("***")),
         "훅 착지가 늘어진다. 작가 판단"),
        ("에 대한 density", per10k(r"에 대한") > 4,
         "서술 1만자당 %.1f회" % per10k(r"에 대한")),
        ("할 수 있었다 chain", len(re.findall(
            r"할 수 있었다[^.]*\.[^.]*할 수 있었다", nt)) > 0, "연쇄 사용"),
    ]
    return checks + [("WARN " + n, not v, d) for n, v, d in warns], \
           {"chars": chars, "scenes": scenes,
                    "max_run": max(runs) if runs else 0,
                    "long_pct": round(long_pct, 1),
                    "narration_sentences": len(sents)}


def find_manuscript(n):
    d = os.path.join(ROOT, "manuscript", "volume-%02d" % ((n - 1) // 25 + 1))
    if not os.path.isdir(d):
        return None
    for f in os.listdir(d):
        if f.startswith("E%03d-" % n):
            return "manuscript/volume-%02d/%s" % ((n - 1) // 25 + 1, f)
    return None


# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("episode")
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--gate-only", action="store_true")
    a = ap.parse_args()
    n = int(re.sub(r"\D", "", a.episode))

    p = bep.build(n)

    if a.gate_only:
        ms = find_manuscript(n)
        if not ms:
            print("no manuscript for E%03d" % n)
            return 1
        checks, stats = gate(ms, p["density"]["scenes"] if p["density"] else 3)
        for name, ok, detail in checks:
            print("%-26s %s  %s" % (name, "PASS" if ok else "FAIL", detail))
        print(json.dumps(stats))
        return 0 if all(c[1] for c in checks if not c[0].startswith("WARN")) else 1

    if not p["preflight_pass"]:
        for c in p["preflight"]:
            if not c["ok"]:
                print("PREFLIGHT FAIL  %s  %s" % (c["check"], c["detail"]))
        return 1

    # write the packet
    mp = os.path.join(ROOT, "docs/10_story_architecture/craft-manifests",
                      "E%03d-craft-manifest-auto.md" % n)
    if not os.path.exists(mp):
        io.open(mp, "w", encoding="utf-8").write(bep.render(p))
        print("packet: %s" % os.path.relpath(mp, ROOT))
    else:
        print("packet exists (kept, may carry hand triage): %s" % os.path.relpath(mp, ROOT))

    prompt = build_prompt(n, p)
    if a.dry:
        io.open(os.path.join(ROOT, "prompt-preview.txt"), "w", encoding="utf-8").write(prompt)
        print("wrote prompt-preview.txt")
        return 0

    vol = os.path.join(ROOT, "manuscript", "volume-%02d" % ((n - 1) // 25 + 1))
    if not os.path.isdir(vol):
        os.makedirs(vol)

    cmd = ["codex", "exec", "-C", ROOT,
           "--dangerously-bypass-approvals-and-sandbox",
           "-o", os.path.join(ROOT, "codex-last-report.txt"), prompt]
    print("running codex for E%03d ..." % n)
    subprocess.call(cmd)

    ms = find_manuscript(n)
    if not ms:
        print("codex produced no manuscript file")
        return 1
    checks, stats = gate(ms, p["density"]["scenes"] if p["density"] else 3)
    print("\n=== GATE E%03d ===" % n)
    for name, ok, detail in checks:
        print("%-26s %s  %s" % (name, "PASS" if ok else "FAIL", detail))
    print(json.dumps(stats))
    return 0 if all(c[1] for c in checks if not c[0].startswith("WARN")) else 1


if __name__ == "__main__":
    sys.exit(main())
