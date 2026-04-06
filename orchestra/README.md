# Orchestra Overview

This folder contains the operating system for the repo-local novel orchestra.

## What lives here

- `SOURCE_OF_TRUTH.md`: canonical priority order
- `WORKFLOW.md`: lane order and merge discipline
- `LORE_AUDIT_HARNESS.md`: setting-library audit flow
- `FORESHADOW_HARNESS.md`: clue and payoff flow
- `STORYCRAFT_HARNESS.md`: structure, arc, reveal, and cadence flow
- `SMOKE_AUDIT_HARNESS.md`: fast automated consistency checks
- `../lore_bible/Relationship_Map.md`: core relationship damage grammar
- `../lore_bible/Supporting_Cast_Witness_Map.md`: side-character witness grammar
- `../lore_bible/Front_Half_Foreshadow_Map.md`: front-half clue obligations
- `../lore_bible/Ending_Convergence_Map.md`: late-series ending convergence map
- `SESSION_STATE.md`: live project snapshot
- `templates/`: reusable packet and reporting formats
- `scripts/`: helper tooling and packet builders
- `runs/`: generated output packets created on demand

Active helper tooling should live under `orchestra/scripts` or `backend/`. Root-level one-off utilities should be moved out of the repo root so the canon entry points stay clean.

## Usage

Use the conductor first. The conductor decides which specialists are necessary, creates the packet, and merges outputs back into canon files. Do not route every task through every lane.

Use the smoke audit when you need a fast pass before or after heavy edits. It is a structural gate, not a replacement for novelist judgment.

If the task touches human cost, reveal fairness, or the late ending spine, pull the relevant map first instead of reconstructing those rules from scattered lore files.

## Three major harnesses

### Lore audit

Use when the problem is world, character, faction, location, or timeline integrity.

### Foreshadow audit

Use when the problem is clue fairness, red herrings, or payoff debt.

### Storycraft

Use when the problem is novelist-side design: structure, reveal order, emotional arcs, or serial retention.
