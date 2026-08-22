# -*- coding: utf-8 -*-
"""
Episode Packet Builder v1
=========================

Materializes the 22-field contract that every Deep Context Master declares but
does not fill in. Given an episode id it slices the design corpus down to the
minimum coherent bundle and emits a Craft Manifest draft plus a writer prompt.

Implements:
  docs/10_story_architecture/minimum-context-resolver-v1.md   (paths, 3-way load split)
  docs/10_story_architecture/craft-context-resolver-v1.md     (signals -> craft route)
  docs/10_story_architecture/deep-context-pack-production-standard-v1.md (22 fields)

Usage:
  python .agent/tools/build_episode_packet.py E002
  python .agent/tools/build_episode_packet.py E002 --out packets/
  python .agent/tools/build_episode_packet.py E002 --check     # preflight only

Refuses to build when a blocking condition is present. That refusal is the
point: a packet that quietly omits a required field is worse than no packet.
"""

import io
import os
import re
import sys
import json
import argparse

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def rd(rel):
    p = os.path.join(ROOT, rel)
    if not os.path.exists(p):
        return None
    return io.open(p, encoding="utf-8", errors="replace").read()


# --------------------------------------------------------------------------
# 1. Deterministic routing  (minimum-context-resolver v1 section 1 and 2)
# --------------------------------------------------------------------------

SUBACT_TABLE = []
for _vol in range(1, 16):
    _base = (_vol - 1) * 25 + 1
    _letters = ["A", "B", "C", "D"]
    _spans = [(0, 5), (6, 11), (12, 17), (18, 24)]
    for _i, (_s, _e) in enumerate(_spans):
        SUBACT_TABLE.append(
            ("V%02d-%d%s" % (_vol, _vol, _letters[_i]), _base + _s, _base + _e)
        )

GA_REGISTRY = [
    (1, 75, "ga01-episode-registry-e001-e075.md"),
    (76, 150, "ga02-episode-registry-e076-e150.md"),
    (151, 225, "ga03-episode-registry-e151-e225.md"),
    (226, 300, "ga04-episode-registry-e226-e300.md"),
    (301, 375, "ga05-episode-registry-e301-e375.md"),
]

GA_ROMAN = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V"}


def route(n):
    if not 1 <= n <= 375:
        raise ValueError("episode out of range: %d" % n)
    ga = (n - 1) // 75 + 1
    vol = (n - 1) // 25 + 1
    subact = None
    for name, s, e in SUBACT_TABLE:
        if s <= n <= e:
            subact = name
            break
    reg = next(f for s, e, f in GA_REGISTRY if s <= n <= e)
    return {
        "episode": "E%03d" % n,
        "n": n,
        "ga": ga,
        "ga_roman": GA_ROMAN[ga],
        "volume": "V%02d" % vol,
        "vol_n": vol,
        "subact": subact,
        "hub": "docs/10_story_architecture/subacts/%s.md" % subact,
        "scene_ready": "docs/10_story_architecture/detail/v%02d-scene-ready-design-v1.md" % vol,
        "registry": "docs/10_story_architecture/detail/%s" % reg,
        "deep_master": ".agent/context-packs/deep/%s-deep-context-master.md" % subact,
    }


# --------------------------------------------------------------------------
# 2. Row slicing  (never load a whole index file)
# --------------------------------------------------------------------------

def d6_row(r):
    t = rd(r["registry"])
    if not t:
        return None
    m = re.search(r"^\|\s*%s\s*\|(.+)$" % r["episode"], t, re.M)
    if not m:
        return None
    cells = [c.strip() for c in m.group(1).split("|")]
    return {
        "beat": cells[0] if len(cells) > 0 else "",
        "goal": cells[1] if len(cells) > 1 else "",
        "choice": cells[2] if len(cells) > 2 else "",
        "hook": cells[3] if len(cells) > 3 else "",
    }


def density_row(r):
    t = rd("docs/10_story_architecture/scene-density-map-v1.md")
    if not t:
        return None
    m = re.search(r"^\|\s*%s\s*\|(.+)$" % r["episode"], t, re.M)
    if not m:
        return None
    cells = [c.strip() for c in m.group(1).split("|")]
    dens = cells[0] if cells else ""
    letter = dens.split("\u00b7")[0].strip() if dens else ""
    return {
        "type": letter,
        "label": dens,
        "fixed": "\uace0\uc815" in (cells[1] if len(cells) > 1 else ""),
        "reason": cells[2] if len(cells) > 2 else "",
        "scenes": {"Q": 2, "S": 3, "E": 4, "X": 6}.get(letter, 0),
    }


def ga_block(r):
    t = rd("docs/10_story_architecture/grand-acts-v1.md")
    if not t:
        return None
    blocks = re.split(r"^## ", t, flags=re.M)
    for b in blocks:
        if b.startswith("Grand Act %s " % r["ga_roman"]):
            out = {}
            for k in ["Promise", "Goal", "Opposition", "Choice", "Cost",
                      "Revelation", "Reward", "Loss", "State Change",
                      "Next Cause", "Anti-Repeat"]:
                m = re.search(r"\*\*%s:\*\*\s*(.+)" % re.escape(k), b)
                out[k] = m.group(1).strip() if m else ""
            out["title"] = b.split("\n")[0].strip()
            return out
    return None


# --------------------------------------------------------------------------
# 3. POV  (ALWAYS-load: hubs alone cannot tell you whether an assignment exists)
# --------------------------------------------------------------------------

def pov(r):
    res = {"type": "AIDEN_CLOSE_THIRD", "who": "\uc5d0\uc774\ub4e0 \ub85c\uc5d4",
           "function": "", "ceiling": "", "rejoin": "", "source": "default",
           "supplement": ""}
    t = rd("docs/10_story_architecture/secondary-pov-and-offscreen-action-allocation-v1.md")
    if t:
        for m in re.finditer(r"^\|\s*(V\d+)\s*\|\s*(E\d{3})\s*\|(.+)$", t, re.M):
            if m.group(2) == r["episode"]:
                c = [x.strip() for x in m.group(3).split("|")]
                res.update({
                    "type": "SECONDARY",
                    "who": c[0] if len(c) > 0 else "",
                    "function": c[1] if len(c) > 1 else "",
                    "ceiling": c[2] if len(c) > 2 else "",
                    "rejoin": c[3] if len(c) > 3 else "",
                    "source": "secondary-pov-and-offscreen-action-allocation-v1.md",
                })
                break
    # D15 supplement overrides the older global table
    s = rd("docs/10_story_architecture/d15-pov-allocation-supplement-v1.md")
    if s:
        blocks = re.split(r"^## ", s, flags=re.M)
        for b in blocks:
            if b.startswith(r["episode"]):
                lock = re.search(r"\*\*(.+?)\*\*", b)
                res["supplement"] = lock.group(1).strip() if lock else b.split("\n")[0]
                res["source"] = "d15-pov-allocation-supplement-v1.md (OVERRIDE)"
                break
    return res


# --------------------------------------------------------------------------
# 4. Mystery ceiling  (the part that most needs to be automatic)
# --------------------------------------------------------------------------

def mysteries(r):
    """Active rungs at this episode, and answers that must stay shut.

    A mystery whose reader-inference episode is later than this one may appear
    as a clue but its answer must not be stated. Computing this by hand for 375
    episodes is where leaks come from.
    """
    t = rd("docs/11_mystery/mystery-semantic-crosswalk-e001-e375-v2.md")
    if not t:
        return {"active": [], "sealed": [], "opens_here": [], "retired": [],
                "hub_only": []}
    n = r["n"]
    active, sealed, opens = [], [], []

    # Section 4 retires rungs that older sources still list. Crosswalk v2 wins:
    # "회차·rung은 이 v2 Crosswalk를 사용한다" (section 5).
    retired = []
    for m in re.finditer(r"^- (M\d{2}) ((?:E\d{3}/?)+):\s*(.+)$", t, re.M):
        for e in re.findall(r"E(\d{3})", m.group(2)):
            retired.append({"id": m.group(1), "episode": "E%03d" % int(e),
                            "reason": m.group(3).strip()})

    for m in re.finditer(r"^\|\s*\*\*(M\d{2})\*\*\s*([^|]*)\|([^|]*)\|([^|]*)\|", t, re.M):
        mid, question, route_s, infer_s = (m.group(1), m.group(2).strip(),
                                          m.group(3), m.group(4).strip())
        rungs = [int(x) for x in re.findall(r"E(\d{3})", route_s)]
        # The inference cell also names episodes it is REJECTING as precursors
        # ("기존 E045/E125/E226은 precursor이지 이 질문의 Plant가 아님").
        # Counting those as inference points makes min() too early, which
        # under-seals the mystery. Drop anything inside such a clause.
        infer_clean = re.sub(r"기존[^.。]*?(?:precursor|아님|아니라)[^.。]*[.。]?", " ", infer_s)
        infer_eps = [int(x) for x in re.findall(r"E(\d{3})", infer_clean)]
        if not infer_eps:  # the whole cell was a rejection clause
            infer_eps = [int(x) for x in re.findall(r"E(\d{3})", infer_s)]
        rec = {"id": mid, "question": question,
               "rungs": ["E%03d" % x for x in rungs],
               "inference": ["E%03d" % x for x in infer_eps],
               "note": re.sub(r"\s+", " ", infer_s)[:400]}
        rec["sealed"] = bool(infer_eps) and n < min(infer_eps)
        if n in rungs:
            active.append(rec)
        if infer_eps and n in infer_eps:
            opens.append(rec)
        elif rec["sealed"]:
            sealed.append(rec)

    # validation-echo continuation rows carry post-resolution applications
    for m in re.finditer(r"^\|\s*\|\s*Post-resolution validation:\s*([^|]*)\|", t, re.M):
        if "E%03d" % n in m.group(1):
            active.append({"id": "ECHO", "question": re.sub(r"\s+", " ", m.group(1)),
                           "rungs": [], "inference": [], "sealed": False,
                           "note": "post-resolution validation, not a new rung"})

    # What the subact hub claims, that crosswalk v2 does not carry.
    hub = rd(r["hub"]) or ""
    hub_ids = set()
    for line in hub.split("\n"):
        if r["episode"] in line:
            hub_ids.update(re.findall(r"\bM\d{2}\b", line))
    cw_ids = {x["id"] for x in active} | {x["id"] for x in opens}
    hub_only = sorted(hub_ids - cw_ids)

    return {"active": active, "sealed": sealed, "opens_here": opens,
            "retired": [x for x in retired if x["episode"] == r["episode"]],
            "hub_only": hub_only}


# --------------------------------------------------------------------------
# 5. Anti-repeat  (craft-context-resolver v1 section 11 layer 3)
# --------------------------------------------------------------------------

LEDGER = "docs/10_story_architecture/technique-ledger.json"


def load_ledger():
    t = rd(LEDGER)
    return json.loads(t) if t else {}


def anti_repeat(r):
    led = load_ledger()
    prev = []
    for k in range(r["n"] - 3, r["n"]):
        e = "E%03d" % k
        if e in led:
            prev.append(dict(led[e], episode=e))
    forbid_hook, forbid_dens, forbid_craft = set(), set(), set()
    # Forbid any value already used twice in the previous three episodes.
    #
    # The earlier rule only blocked a repeat of the immediately preceding
    # episode, which let V01-1A alternate H2 H1 H2 H1 H2 H1 for six episodes
    # straight. No rule was broken and the result was still a pattern; a
    # two-beat cycle reads as monotony just as a three-in-a-row does.
    for field, bucket in (("hook", forbid_hook), ("density", forbid_dens),
                          ("primary_craft", forbid_craft)):
        vals = [p.get(field) for p in prev if p.get(field)]
        for v in set(vals):
            if v and vals.count(v) >= 2:
                bucket.add(v)
        if vals and vals[-1]:
            bucket.add(vals[-1])

    # Hook types never used yet, so the packet can point somewhere fresh
    # instead of only saying what is closed off.
    used = {v.get("hook") for v in led.values() if v.get("hook")}
    unused = [h for h in ("H1", "H2", "H3", "H4", "H5", "H6", "H7") if h not in used]

    return {"previous": prev, "forbid_hook": sorted(forbid_hook),
            "forbid_density": sorted(forbid_dens),
            "forbid_primary_craft": sorted(forbid_craft),
            "hooks_never_used": unused}


# --------------------------------------------------------------------------
# 6. Craft diagnosis  (craft-context-resolver v1 section 2)
# --------------------------------------------------------------------------

DIAGNOSIS = [
    ("\uc815\uce58\u00b7\ubc95\u00b7\ud589\uc815", ["\uc2b9\uc778", "\uc815\uc871\uc218", "\uccad\ubb38", "\ubc95", "\uc2dc\ubbfc\uad8c", "\uc18c\uc720\uad8c", "\uc5f4\ub78c", "\uc11c\uba85", "\uc81c\ub3c4", "\uacf5\uac1c\uc808\ucc28"]),
    ("\ud611\uc0c1\u00b7\uac70\ubd80\uad8c", ["\ud611\uc0c1", "\uac70\ubd80\uad8c", "\uc591\ubcf4", "\uc870\uac74", "\uc694\uad6c"]),
    ("\uc870\uc0ac\u00b7\ucd94\ub9ac", ["\ub300\uc870", "\uac80\uc99d", "\uc7a5\ubd80", "\uae30\ub85d", "\ubd88\uc77c\uce58", "\uc218\uc0ac", "\ud574\ub3c5"]),
    ("\uc2dc\uac04\uc120 \uc774\uc0c1", ["\uc624\ucc29", "\uadc0\ud658\ucc3d", "\uc88c\ud45c", "\uc2dc\uac04\uc120", "\ub3c4\uc57d"]),
    ("\uc804\ud22c\u00b7\ucd94\uaca9\u00b7\uacf5\uc131", ["\ud3ec\uc704", "\uacf5\uc131", "\ucd94\uaca9", "\ubc29\uc5b4", "\uad70\uc0ac", "\uc804\ud22c"]),
    ("\uc7ac\ub09c\u00b7\ub300\ud53c\u00b7\ubcf4\uae09", ["\ub300\ud53c", "\ubc30\uae09", "\ubd95\uad34", "\ud658\uc790", "\uad6c\ud638", "\uae30\uadfc"]),
    ("\uad00\uacc4 \ubcc0\ud654\u00b7\uc0c1\uc2e4", ["\uc0ac\ub9dd", "\uc774\ubcc4", "\uc2e0\ub8b0", "\uae30\uc5b5 \uc190\uc0c1", "\uc0c1\uc2e4", "\uc7a5\ub840"]),
    ("\uc720\uc0b0\u00b7\uc2e0\uc218\u00b7\uc18c\uc720\uad8c", ["\uc720\ubb3c", "\uc2e0\uc218", "\uc0c1\uc18d", "\uc778\uc7a5", "\uc720\uc0b0"]),
    ("\ubbf8\ub798 \ubcc0\ud615\u00b7\uadc0\ud658", ["\uadc0\ud658", "\ubcc0\ud615", "\uba85\ub2e8 \ubcc0\ud654", "\uc0ac\ub77c\uc9c4"]),
    ("\uc0dd\uc874 \uc555\ubc15", ["\uac80\ubb38", "\uc7a0\uc785", "\ubd80\uc0c1", "\uc2dc\ud55c", "\ud0c8\ucd9c", "\uc2e0\ubd84"]),
    ("\ubb38\ud654\ucda9\ub3cc\u00b7\ubc88\uc5ed", ["\uc5b8\uc5b4", "\ud638\uce6d", "\ud1b5\uc5ed", "\uc2dc\ub300\ucc28"]),
    ("\uc560\ub3c4\u00b7\ud68c\ubcf5\u00b7\uc0dd\ud65c \ud6c4\uacfc", ["\uc560\ub3c4", "\ud68c\ubcf5", "\ud6c4\uacfc", "\uc0dd\ud65c", "\ubcf4\uc874"]),
    ("\uacb0\ub9d0 \uae30\ub2a5 \uc900\ube44", ["\ud68c\uc218", "\ucd5c\uc885 \uc870\ud56d", "\ud5cc\ubc95", "\ubd84\ub9ac", "\uc7a0\uae08"]),
]

CRAFT_COMBOS = {
    "\uc870\uc0ac\u00b7\ucd94\ub9ac": ("\uacf5\uc815 \ub2e8\uc11c", ["\uc624\ub2f5", "\uc815\ubcf4 \uac04\uadf9"]),
    "\uc815\uce58\u00b7\ubc95\u00b7\ud589\uc815": ("\uc774\ud574\uad00\uacc4 \ud611\uc0c1", ["\uad8c\ud55c \uc808\ucc28", "\ub300\ub9bd\uc790 \uc131\uacfc"]),
    "\ud611\uc0c1\u00b7\uac70\ubd80\uad8c": ("\uc774\ud574\uad00\uacc4 \ud611\uc0c1", ["\uad8c\ud55c \uc808\ucc28", "\uac00\uce58 \ubcc0\ud654"]),
    "\uc7ac\ub09c\u00b7\ub300\ud53c\u00b7\ubcf4\uae09": ("\uc81c\ud55c\uc790\uc6d0 \uc120\ud0dd", ["\uacf5\uac04 \uba85\ub8cc\uc131", "\uc0dd\ud65c \ud6c4\uacfc"]),
    "\uc804\ud22c\u00b7\ucd94\uaca9\u00b7\uacf5\uc131": ("\uacf5\uac04 \ubaa9\ud45c", ["\uc804\uc220 \ubcc0\ud654", "\ubd80\uc0c1/\uc790\uc6d0 \ube44\uc6a9"]),
    "\uad00\uacc4 \ubcc0\ud654\u00b7\uc0c1\uc2e4": ("\uad00\uacc4 \uc0c1\ud0dc \ubcc0\ud654", ["\uc7a5\uba74\u2013\ubc18\uc751", "\ubd80\uc7ac \ubcf5\uc120"]),
    "\uc720\uc0b0\u00b7\uc2e0\uc218\u00b7\uc18c\uc720\uad8c": ("\uc18c\uc720\uad8c\u00b7\uac70\ubd80\uad8c", ["\uc624\ud574\ub41c \uae30\ub2a5", "\ubc18\ud658/\ubd84\ud574"]),
    "\uc2dc\uac04\uc120 \uc774\uc0c1": ("\uad6c\uccb4\uc801 \ud604\uc2e4 \ubd88\uc77c\uce58", ["\uae30\uc5b5 \uc2e0\ub8b0\ub3c4", "\ud604\uc7ac\uc778\uc758 \uad8c\ub9ac"]),
    "\ubbf8\ub798 \ubcc0\ud615\u00b7\uadc0\ud658": ("\uad6c\uccb4\uc801 \ud604\uc2e4 \ubd88\uc77c\uce58", ["\uae30\uc5b5 \uc2e0\ub8b0\ub3c4", "\ud604\uc7ac\uc778\uc758 \uad8c\ub9ac"]),
    "\uc0dd\uc874 \uc555\ubc15": ("\uc81c\ud55c\uc790\uc6d0 \uc120\ud0dd", ["\uc2dc\ub3c4\u2013\uc2e4\ud328\u2013\ud559\uc2b5", "\uacf5\uac04 \uba85\ub8cc\uc131"]),
    "\ubb38\ud654\ucda9\ub3cc\u00b7\ubc88\uc5ed": ("\uc2dc\ub300\ubcc4 \uc5b8\uc5b4 \ucc28\uc774", ["\ub2e8\uc5ed \ud654\ubc95 \ubd84\ud654", "\uc81c\ub3c4 \uc608\uc678"]),
    "\uc560\ub3c4\u00b7\ud68c\ubcf5\u00b7\uc0dd\ud65c \ud6c4\uacfc": ("\uc7a5\uba74\u2013\ubc18\uc751", ["\uac00\uce58 \ubcc0\ud654", "\uc0dd\ud65c \ud6c4\uacfc"]),
    "\uacb0\ub9d0 \uae30\ub2a5 \uc900\ube44": ("\uacb0\ub9d0 \uc5ed\uc0b0", ["\uc2dd\ubb3c\u2013\ud68c\uc218\u2013\uc7ac\ub9e5\ub77d\ud654", "\uc57d\uc18d\u2013\uc9c4\ud589\u2013\ud68c\uc218"]),
}

HOOK_TYPES = [
    ("H1", "\ubb3c\ub9ac\uc801 \uc704\ud5d8", ["\ucd94\uaca9", "\ubd95\uad34", "\ubd80\uc0c1", "\ubd09\uc1c4", "\uc624\ucc28", "\ud3ec\uc704", "\uc218\uba85", "\uc9e7", "\uc904\uc5b4", "\ube44\uc5b4"]),
    ("H2", "\uc815\ubcf4 \uc5ed\uc804", ["\ub2e4\ub974", "\ubd88\uc77c\uce58", "\uc99d\uc5b8", "\uae30\ub85d", "\ubc1c\uacac", "\uc228\uaca8", "\uc228\uaca8\uc838"]),
    ("H3", "\uad00\uacc4 \uc120\ud0dd", ["\uac70\ubd80", "\ubc30\uc2e0", "\uc774\ubcc4", "\uacbd\uace0", "\uac10\uc2dc"]),
    ("H4", "\uc81c\ub3c4 \ubcc0\ud654", ["\uc2b9\uc778", "\uad8c\ub9ac", "\ubc30\uae09", "\uc2dc\ubbfc\uad8c", "\uc18c\uc720\uad8c", "\uac00\ub3d9"]),
    ("H5", "\ubbf8\ub798 \ubcc0\ud615", ["\uadc0\ud658 \ub4a4", "\uc0ac\ub77c\uc84c", "\ubcc0\ud588", "\uba85\ub2e8\uc774 \ubc14", "\ub2e4\ub978 \ubbf8\ub798"]),
    ("H6", "\uc724\ub9ac\uc801 \uc9c8\ubb38", ["\ube44\uc6a9", "\ub204\uad6c", "\uc120\ud0dd"]),
    ("H7", "\uc5ec\uc6b4\ud615", ["\uc774\ub984", "\ub0a8\uae30", "\uc870\uc6a9"]),
]


def diagnose(d6, dens):
    """Weighted so that what the episode DOES outranks how it ends.

    The hook is the last beat, not the episode's central problem. Scoring it
    equally sent E001 - an approval-and-access-rights episode - to
    investigation, because its hook mentions mismatched records.
    """
    fields = [
        (d6.get("goal", ""), 3),
        (d6.get("choice", ""), 3),
        (dens.get("reason", "") if dens else "", 2),
        (d6.get("beat", ""), 1),
        (d6.get("hook", ""), 1),
    ]
    scores = {}
    for name, keys in DIAGNOSIS:
        s = 0
        for text, w in fields:
            s += w * sum(1 for k in keys if k in text)
        if s:
            scores[name] = s
    if not scores:
        return "\uc815\uce58\u00b7\ubc95\u00b7\ud589\uc815", 0
    best = max(scores, key=lambda k: scores[k])
    ranked = sorted(scores.values(), reverse=True)
    margin = ranked[0] - (ranked[1] if len(ranked) > 1 else 0)
    return best, margin


def hook_type(d6):
    h = d6.get("hook", "")
    for hid, label, keys in HOOK_TYPES:
        if any(k in h for k in keys):
            return hid, label
    return "H6", "\uc724\ub9ac\uc801 \uc9c8\ubb38"


# --------------------------------------------------------------------------
# 7. Read-aloud alerts fed back from prior audits
# --------------------------------------------------------------------------

ALERTS_PATH = "docs/99_quality_control/read-aloud-alerts.json"

DEFAULT_ALERTS = [
    "\ub9c8\uc9c0\ub9c9 \ubb38\uc7a5\uc744 `~\uac83\uc744 \ubcf4\uc558\ub2e4` / `~\uace0 \uc788\uc5c8\ub2e4` \ub85c \ub05d\ub0b4\uc9c0 \uc54a\ub294\ub2e4. \ud6c5\uc740 \ub2e8\ub2e8\ud558\uac8c \ucc29\uc9c0\ud574\uc57c \ud55c\ub2e4.",
    "\uaca9\uc5b8\ud615 \ub9c8\uac10 \uae08\uc9c0 \u2014 \uc7a5\uba74 \ub05d\uc5d0 \uc11c\uc220\uc790\uac00 \uc758\ubbf8\ub97c \ud655\uc815\ud574 \uc8fc\uc9c0 \uc54a\ub294\ub2e4.",
    "\ub300\uce6d \ub300\uc870\uad6c\ubb38(`~\ud558\uae30\uc5d0\ub294 \ub108\ubb34 A, ~\ud558\uae30\uc5d0\ub294 B`) \uae08\uc9c0.",
    "\uba85\uc0ac\ud615 \uad00\ud615 \uc885\uacb0(`~\ud558\ub294 \ub208\uc774\uc5c8\ub2e4`, `~\uc5c6\ub2e4\ub294 \uc190\ub180\ub9bc\uc774\uc5c8\ub2e4`) \ud55c \uc7a5\uba74 2\ud68c \uc774\uc0c1 \uae08\uc9c0.",
    "\uc11c\ub85c \ub2e4\ub978 \uae30\ub2a5\uc778\ubb3c\uc774 \uac19\uc740 \uc885\uacb0\uc5b4\ubbf8\ub97c \uacf5\uc720\ud558\uba74 \ub0ad\ub3c5\uc790\uac00 \uac19\uc740 \ubaa9\uc18c\ub9ac\ub85c \uc77d\ub294\ub2e4. \uc9c1\uc5c5\u00b7\uc2e0\ubd84\uc73c\ub85c \uac08\ub77c\uc57c \ud55c\ub2e4.",
    "\ub300\uba85\uc0ac `\uadf8\uac00`\uac00 \uc55e \ubb38\uc7a5\uc758 \uc8fc\uc5b4\uc640 \ub2e4\ub978 \uc0ac\ub78c\uc744 \uac00\ub9ac\ud0a4\uba74 \uc774\ub984\uc73c\ub85c \uad50\uccb4\ud55c\ub2e4.",
    "**\uc6d0\uace0 \ubcf8\ubb38\uc5d0 \ud68c\ucc28 \ubc88\ud638(`E001`, `E002`\u2026)\ub97c \uc4f0\uc9c0 \uc54a\ub294\ub2e4.** \uc55e \ud68c\ucc28\ub97c \uac00\ub9ac\ud0ac \ub54c\ub294 \uc7a5\uba74\u00b7\uc778\ubb3c\u00b7\uc0ac\ubb3c\ub85c \ubd80\ub978\ub2e4. \uc81c\ubaa9 \uc904\ub9cc \uc608\uc678\ub2e4. (E002 \ucd08\uace0\uc5d0\uc11c `E001\uc758 \uae30\ub85d \uc811\uadfc\uc2e4 \ub2f4\ub2f9\uc790`\uac00 \uac80\ucd9c\ub428)",
    "**\uc7a5\ubd80\u00b7\ud45c\u00b7\uba85\ub2e8\uc758 \ud56d\ubaa9\uc744 \uc9e7\uc740 \uc870\uac01 \ubb38\uc7a5\uc73c\ub85c \uae38\uac8c \ub098\uc5f4\ud558\uc9c0 \uc54a\ub294\ub2e4.** \uc774 \uc791\ud488\uc740 \ubb38\uc11c\ub97c \uc790\uc8fc \uc77d\uc9c0\ub9cc, \ud56d\ubaa9\uc744 8\uc904\uc529 \ub04a\uc5b4 \uc4f0\uba74 \uc11c\uc220 \ub9ac\ub4ec\uc774 \ubd81\uc18c\ub9ac\uac00 \ub41c\ub2e4. \uc138 \ud56d\ubaa9\uae4c\uc9c0\ub294 \uc870\uac01\uc73c\ub85c, \uadf8 \uc774\uc0c1\uc740 \ud55c \ubb38\uc7a5 \uc548\uc5d0 \ubb36\uac70\ub098 \uc778\ubb3c\uc774 \uc77d\ub294 \ud589\ub3d9\uc5d0 \uc2e4\uc5b4 \ubcf4\ub0b8\ub2e4. (E042 \ucd08\uace0\uc5d0\uc11c \ubc30\ubd84\ud45c \ud56d\ubaa9\uc774 8\uc5f0\uc18d \ub2e8\ubb38\uc73c\ub85c \uac80\ucd9c\ub428)",
]


def alerts():
    t = rd(ALERTS_PATH)
    if t:
        try:
            return json.loads(t)
        except ValueError:
            pass
    return DEFAULT_ALERTS


# --------------------------------------------------------------------------
# 8. Preflight  (minimum-context-resolver v1 section 7)
# --------------------------------------------------------------------------

def preflight(r, d6, dens, prv):
    checks = []

    def add(name, ok, detail=""):
        checks.append({"check": name, "ok": bool(ok), "detail": detail})

    add("1 routing unique", bool(r["subact"]), r["subact"])
    add("1b hub exists", rd(r["hub"]) is not None, r["hub"])
    add("1c registry row", d6 is not None, r["registry"])
    add("1d density row", dens is not None, "")
    add("5 GAP-B triage", True, "hub warnings must be triaged by hand; see section 6")
    if r["n"] == 1:
        add("7 previous exit", True, "SERIES ORIGIN STATE")
    else:
        add("7 previous exit", prv is not None,
            prv if prv else
            "missing: manuscript/state/E%03d-state-mutation.md" % (r["n"] - 1))
    return checks


def prev_state(r):
    if r["n"] == 1:
        return "SERIES ORIGIN STATE"
    p = "manuscript/state/E%03d-state-mutation.md" % (r["n"] - 1)
    return p if rd(p) else None


# --------------------------------------------------------------------------
# 9. Emit
# --------------------------------------------------------------------------

def build(n, check_only=False):
    r = route(n)
    d6 = d6_row(r)
    dens = density_row(r)
    ga = ga_block(r)
    pv = pov(r)
    my = mysteries(r)
    ar = anti_repeat(r)
    prv = prev_state(r)
    checks = preflight(r, d6, dens, prv)
    diag, conf = diagnose(d6 or {}, dens or {})
    hid, hlabel = hook_type(d6 or {})
    primary, secondary = CRAFT_COMBOS.get(diag, ("\uc774\ud574\uad00\uacc4 \ud611\uc0c1", ["\uad8c\ud55c \uc808\ucc28"]))

    ok = all(c["ok"] for c in checks)
    packet = {
        "route": r, "d6": d6, "density": dens, "ga": ga, "pov": pv,
        "mystery": my, "anti_repeat": ar, "previous_exit": prv,
        "diagnosis": diag, "diagnosis_confidence": conf,
        "primary_craft": primary, "secondary_craft": secondary,
        "hook_type": hid, "hook_label": hlabel,
        "alerts": alerts(), "preflight": checks, "preflight_pass": ok,
    }
    return packet


def render(p):
    r, d6, dens, ga, pv = p["route"], p["d6"], p["density"], p["ga"], p["pov"]
    L = []
    A = L.append
    A("# %s Craft Manifest (auto-built)" % r["episode"])
    A("")
    A("Generated by `.agent/tools/build_episode_packet.py`.")
    A("Format: `craft-context-resolver-v1.md` section 12. Values are sliced from source, not restated.")
    A("")
    A("## 0. Routing")
    A("")
    A("| | |")
    A("|---|---|")
    A("| Episode | **%s** |" % r["episode"])
    A("| Grand Act | GA %s |" % r["ga_roman"])
    A("| Volume | %s |" % r["volume"])
    A("| Subact | **%s** |" % r["subact"])
    A("| Subact Beat | %s |" % (d6["beat"] if d6 else "?"))
    A("| Hub | `%s` |" % r["hub"])
    A("| D6 | `%s` |" % r["registry"])
    A("| Previous Exit | %s |" % (p["previous_exit"] or "**MISSING**"))
    A("")
    A("## 1. S1 density")
    A("")
    if dens:
        A("**%s**%s" % (dens["label"], " (fixed)" if dens["fixed"] else ""))
        A("")
        A("> %s" % dens["reason"])
        A("")
        A("Scene count: **%d**" % dens["scenes"])
    A("")
    A("## 2. S2 function")
    A("")
    if d6:
        A("| | |")
        A("|---|---|")
        A("| Goal | %s |" % d6["goal"])
        A("| Choice / State change | %s |" % d6["choice"])
        A("| Hook | %s |" % d6["hook"])
    A("")
    A("Diagnosis: **%s** (keyword confidence %d)" % (p["diagnosis"], p["diagnosis_confidence"]))
    if p["diagnosis_confidence"] <= 3:
        A("")
        A("> **Thin margin (%d).** Two categories scored close. Confirm against the hub before writing; the craft combo below follows the winner only." % p["diagnosis_confidence"])
        A("")
    A("")
    A("## 3. S3 POV")
    A("")
    if pv["type"] == "SECONDARY":
        A("**%s — secondary POV**" % pv["who"])
        A("")
        A("- Function: %s" % pv["function"])
        A("- **Knowledge ceiling: %s**" % pv["ceiling"])
        A("- Rejoin: %s" % pv["rejoin"])
    else:
        A("**Aiden Roen, close third. No secondary POV assigned to this episode.**")
    if pv["supplement"]:
        A("")
        A("> D15 supplement override: **%s**" % pv["supplement"])
    A("")
    A("Source: `%s`" % pv["source"])
    A("")
    A("## 4. S4 Grand Act")
    A("")
    if ga:
        A("- Promise: %s" % ga["Promise"])
        A("- Revelation: %s" % ga["Revelation"])
        A("- **Anti-Repeat: %s**" % ga["Anti-Repeat"])
    A("")
    A("## 5. Craft route")
    A("")
    A("- Primary: **%s**" % p["primary_craft"])
    A("- Secondary: %s" % ", ".join(p["secondary_craft"]))
    A("- Hook type: **%s %s**" % (p["hook_type"], p["hook_label"]))
    A("")
    A("## 6. Anti-repeat (previous 3 episodes)")
    A("")
    if p["anti_repeat"]["previous"]:
        A("| Episode | Density | Hook | Primary craft |")
        A("|---|---|---|---|")
        for q in p["anti_repeat"]["previous"]:
            A("| %s | %s | %s | %s |" % (q["episode"], q.get("density", ""),
                                          q.get("hook", ""), q.get("primary_craft", "")))
        A("")
    else:
        A("No prior episodes recorded.")
        A("")
    for k, label in (("forbid_hook", "Hook"), ("forbid_density", "Density"),
                     ("forbid_primary_craft", "Primary craft")):
        v = p["anti_repeat"][k]
        if v:
            A("- **%s forbidden this episode: %s**" % (label, ", ".join(v)))
    nu = p["anti_repeat"].get("hooks_never_used")
    if nu:
        A("- Hook types not used anywhere yet: **%s**. Prefer one of these if the D6 hook text supports it." % ", ".join(nu))
    A("")
    A("## 7. Mystery — active rungs")
    A("")
    if p["mystery"]["active"]:
        for m in p["mystery"]["active"]:
            tag = "  **clue only — answer still sealed**" if m.get("sealed") else ""
            A("- **%s** %s%s" % (m["id"], m["question"], tag))
    else:
        A("None active at this episode.")
    A("")
    if p["mystery"]["retired"]:
        A("### Retired rungs — do NOT reinstate")
        A("")
        A("Crosswalk v2 section 4 removed these from this episode. Older sources may still list them.")
        A("")
        for m in p["mystery"]["retired"]:
            A("- **%s** at %s — %s" % (m["id"], m["episode"], m["reason"]))
        A("")
    if p["mystery"]["hub_only"]:
        A("### Hub mentions, crosswalk v2 does not carry")
        A("")
        A("`%s` names these near %s while crosswalk v2 assigns no rung here. "
          "Crosswalk v2 is the routing authority (its section 5). Treat as background, not a rung to play."
          % (r["hub"], r["episode"]))
        A("")
        A("- " + ", ".join(p["mystery"]["hub_only"]))
        A("")
    if p["mystery"]["opens_here"]:
        A("### Reader inference OPENS here")
        A("")
        for m in p["mystery"]["opens_here"]:
            A("- **%s** %s" % (m["id"], m["note"]))
        A("")
    A("## 8. DO NOT REVEAL — answers still sealed")
    A("")
    A("Reader inference for these is later than %s. A clue may appear; the answer may not be stated by narration or dialogue." % r["episode"])
    A("")
    for m in p["mystery"]["sealed"]:
        A("- **%s** %s — inference opens at %s" % (m["id"], m["question"], ", ".join(m["inference"])))
    A("")
    A("## 9. Read-aloud alerts (fed back from prior audits)")
    A("")
    for a in p["alerts"]:
        A("- %s" % a)
    A("")
    A("## 10. Preflight")
    A("")
    A("| Check | Result | Detail |")
    A("|---|---|---|")
    for c in p["preflight"]:
        A("| %s | %s | %s |" % (c["check"], "PASS" if c["ok"] else "**FAIL**", c["detail"]))
    A("")
    A("**%s**" % ("PREFLIGHT PASS" if p["preflight_pass"] else "PREFLIGHT FAIL - DO NOT WRITE"))
    A("")
    A("## 11. Length")
    A("")
    A("Minimum 7,000 characters including spaces, no upper limit. If short, return to the scene functions above; never lengthen sentences.")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("episode")
    ap.add_argument("--out", default="docs/10_story_architecture/craft-manifests")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    n = int(re.sub(r"\D", "", a.episode))
    p = build(n)

    if a.json:
        sys.stdout.write(json.dumps(p, ensure_ascii=False, indent=1))
        return 0

    if a.check:
        for c in p["preflight"]:
            print("%-24s %s  %s" % (c["check"], "PASS" if c["ok"] else "FAIL", c["detail"]))
        print("PREFLIGHT: %s" % ("PASS" if p["preflight_pass"] else "FAIL"))
        return 0 if p["preflight_pass"] else 1

    if not p["preflight_pass"]:
        for c in p["preflight"]:
            if not c["ok"]:
                sys.stderr.write("FAIL %s  %s\n" % (c["check"], c["detail"]))
        sys.stderr.write("Refusing to build a packet that is missing a required field.\n")
        return 1

    out = os.path.join(ROOT, a.out, "E%03d-craft-manifest-auto.md" % n)
    d = os.path.dirname(out)
    if not os.path.isdir(d):
        os.makedirs(d)
    io.open(out, "w", encoding="utf-8").write(render(p))
    print("wrote %s" % os.path.relpath(out, ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
