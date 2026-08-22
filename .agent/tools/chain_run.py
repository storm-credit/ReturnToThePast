# -*- coding: utf-8 -*-
"""
Chain Runner
============

Runs episodes back to back and stops the moment one fails.

  python .agent/tools/chain_run.py E007 E012      # run a range
  python .agent/tools/chain_run.py E007 E375      # run to the end

The chain is strictly sequential: episode N needs N-1's state mutation, so
there is nothing to parallelise. Each episode goes through the same loop as
run_episode.py, then gets its ledger row written so the next packet can see
what to avoid.

Stops on the first gate failure rather than pressing on. A drift that gets
past the gate is cheaper to fix at one episode than at twenty, and the
rubric's rewrite limit only means something if the chain actually halts.
"""

import io
import os
import re
import sys
import json
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import importlib.util
_s = importlib.util.spec_from_file_location(
    "runner", os.path.join(ROOT, ".agent", "tools", "run_episode.py"))
runner = importlib.util.module_from_spec(_s)
_s.loader.exec_module(runner)
bep = runner.bep

LEDGER = os.path.join(ROOT, "docs/10_story_architecture/technique-ledger.json")
LOG = os.path.join(ROOT, "chain-progress.md")


def load_ledger():
    return json.load(io.open(LEDGER, encoding="utf-8")) if os.path.exists(LEDGER) else {}


def save_ledger(d):
    io.open(LEDGER, "w", encoding="utf-8").write(
        json.dumps(d, ensure_ascii=False, indent=1))


def note(line):
    with io.open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    sys.stdout.write(line + "\n")
    sys.stdout.flush()


def run_one(n):
    ep = "E%03d" % n
    p = bep.build(n)

    if not p["preflight_pass"]:
        bad = [c for c in p["preflight"] if not c["ok"]]
        note("| %s | PREFLIGHT FAIL | %s |" % (ep, "; ".join(c["check"] for c in bad)))
        return False

    rc = subprocess.call([sys.executable,
                          os.path.join(ROOT, ".agent", "tools", "run_episode.py"), ep])
    ms = runner.find_manuscript(n)
    if not ms:
        note("| %s | NO OUTPUT | codex produced no manuscript |" % ep)
        return False

    checks, stats = runner.gate(ms, p["density"]["scenes"] if p["density"] else 3)
    hard = [c for c in checks if not c[0].startswith("WARN") and not c[1]]
    warns = [c for c in checks if c[0].startswith("WARN") and not c[1]]

    if hard:
        note("| %s | GATE FAIL | %s |" % (ep, "; ".join("%s=%s" % (c[0], c[2]) for c in hard)))
        return False

    d = load_ledger()
    d[ep] = {
        "density": p["density"]["type"] if p["density"] else "?",
        "hook": p["hook_type"],
        "primary_craft": p["primary_craft"],
        "secondary_craft": p["secondary_craft"],
        "diagnosis": p["diagnosis"],
        "pov": p["pov"]["type"],
        "chars": stats["chars"],
        "scenes": stats["scenes"],
        "status": "FIRST DRAFT / GATE PASS / AWAITING QUALITY SCORE",
    }
    save_ledger(d)

    note("| %s | PASS | %d chars, %d scenes, run %d, long %.1f%%%s |" % (
        ep, stats["chars"], stats["scenes"], stats["max_run"], stats["long_pct"],
        ", WARN: " + warns[0][0] if warns else ""))
    return True


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    a = int(re.sub(r"\D", "", sys.argv[1]))
    b = int(re.sub(r"\D", "", sys.argv[2]))

    note("\n## chain %s -> %s\n" % ("E%03d" % a, "E%03d" % b))
    note("| Episode | Result | Detail |")
    note("|---|---|---|")

    for n in range(a, b + 1):
        if not run_one(n):
            note("\n**STOPPED at E%03d.** Fix before continuing; the chain does not skip.\n" % n)
            return 1
    note("\n**Chain complete: E%03d - E%03d.**\n" % (a, b))
    return 0


if __name__ == "__main__":
    sys.exit(main())
