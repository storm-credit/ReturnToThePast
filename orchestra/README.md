# Orchestra Overview

This folder contains the operating system for the repo-local novel orchestra.

## What lives here

- `SOURCE_OF_TRUTH.md`: canonical priority order
- `WORKFLOW.md`: lane order and merge discipline
- `HANDOFF_PACKET_PLAYBOOK.md`: common mission packets for faster conductor dispatch
- `LORE_AUDIT_HARNESS.md`: setting-library audit flow
- `FORESHADOW_HARNESS.md`: clue and payoff flow
- `STORYCRAFT_HARNESS.md`: structure, arc, reveal, and cadence flow
- `SMOKE_AUDIT_HARNESS.md`: fast automated consistency checks
- `../lore_bible/Relationship_Map.md`: core relationship damage grammar
- `../lore_bible/Supporting_Cast_Witness_Map.md`: side-character witness grammar
- `../lore_bible/Front_Half_Foreshadow_Map.md`: front-half clue obligations
- `../lore_bible/Ending_Convergence_Map.md`: late-series ending convergence map
- `SESSION_STATE.md`: live project snapshot
- `ORCHESTRA_PORTABILITY_AUDIT_2026-04-07.md`: reusable-core boundary and separation guidance
- `CORE_LAYER_MAP.md`: reusable core / project config / canon layer split
- `modules/novel-orchestra-core/README.md`: named reusable-core module overview
- `templates/`: reusable packet, handoff, and reporting formats
- `templates/NOVEL_ORCHESTRA_BOOTSTRAP_CHECKLIST.md`: bootstrap checklist for reusing this system on another novel
- `templates/PROJECT_PROFILE_TEMPLATE.md`: per-project config template for a new novel
- `templates/SOURCE_OF_TRUTH_TEMPLATE.md`: source-of-truth template for a new novel
- `templates/SETTING_AUDIT_RULES_TEMPLATE.json`: smoke-rule skeleton for a new novel
- `scripts/`: helper tooling and packet builders
- `runs/`: generated output packets created on demand

Active helper tooling should live under `orchestra/scripts` or `backend/`. Root-level one-off utilities should be moved out of the repo root so the canon entry points stay clean.

## Usage

Use the conductor first. The conductor decides which specialists are necessary, creates the packet, and merges outputs back into canon files. Do not route every task through every lane.

For repeatable work such as chapter drafting, lore repair, or bridge reinforcement, start from `HANDOFF_PACKET_PLAYBOOK.md` and the matching template instead of improvising a new packet every time.

Use the smoke audit when you need a fast pass before or after heavy edits. It is a structural gate, not a replacement for novelist judgment.

If the task touches human cost, reveal fairness, or the late ending spine, pull the relevant map first instead of reconstructing those rules from scattered lore files.

If you plan to reuse this system on another novel, read `ORCHESTRA_PORTABILITY_AUDIT_2026-04-07.md` first, then `CORE_LAYER_MAP.md`, then clone the templates in `templates/`.
If you want a named extraction target, treat `modules/novel-orchestra-core/` as the current reusable-core module boundary.

## Three major harnesses

### Lore audit

Use when the problem is world, character, faction, location, or timeline integrity.

### Foreshadow audit

Use when the problem is clue fairness, red herrings, or payoff debt.

### Storycraft

Use when the problem is novelist-side design: structure, reveal order, emotional arcs, or serial retention.
