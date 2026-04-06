---
name: novel-orchestra-conductor
description: Orchestrate repo-local novel production for ReturnToThePast. Use when a request spans lore-bible additions, plausibility repairs, outline or chapter continuity, storycraft planning, draft creation, hook strengthening, or final chapter audit and Codex needs to coordinate specialist skills instead of handling everything in one pass.
---

# Novel Orchestra Conductor

- Treat this skill as the workflow owner. Specialists propose deltas; the conductor decides order, merges outputs, and writes canonical files.
- Read `orchestra/SOURCE_OF_TRUTH.md` and `orchestra/WORKFLOW.md` before routing work.
- Start from repository truth in this order:
  1. `00_CANON.md`
  2. `Start_Here.md`
  3. `orchestra/WORKFLOW.md`
  4. `outline/Series_Roadmap.md`
  5. relevant `outline/Vol_*_Outline.md` and `outline/Vol_*_Timeline.md`
  6. relevant `lore_bible/**`
  7. relevant `Guidelines/**`
  8. relevant `Drafts/Vol_*/*.md`
- Build a work packet before dispatching specialists. Use `scripts/build_work_packet.py` whenever the task targets a volume, chapter, or lore entity.
- Read `references/packet-contract.md` before routing work.
- Use `references/role-map.md` to choose the lane.
- For setting-library audits, also read `references/lore-audit-role-map.md` and `references/model-routing.md`.
- For storycraft planning, reveal strategy, chapter-retention work, or character-arc mapping, read `orchestra/STORYCRAFT_HARNESS.md`, `references/craft-role-map.md`, and `references/craft-algorithms.md`.
- When Python is unavailable, use `orchestra/scripts/Build-LoreAuditPackets.ps1` to create lore-audit packets.
- When twist setup or payoff tracking is the issue, read `orchestra/FORESHADOW_HARNESS.md` and route through `foreshadow-bookkeeper`.

## Default lane order

1. `lore-forgemaster` when canon is missing, contradictory, or too thin to support the request.
2. `plausibility-warden` to test causality, timeline, motivation, recovery time, and payment logic.
3. `scene-smith` to draft or rewrite prose only after canon blockers are resolved.
4. `hook-doctor` to sharpen the opening, ending, or chapter-turn rhythm without altering canon.
5. `chapter-inspector` for final audit and precise fix instructions.

Skip lanes that do not add value. Never draft before canon blockers are resolved.

## Lore audit order

For setting-library audits, split work by domain:

1. `character-architect`
2. `faction-strategist`
3. `location-cartographer`
4. `world-rule-keeper`
5. `timeline-historian`
6. `chrono-weaver`
7. `lore-forgemaster` if repair patches are needed
8. `plausibility-warden` for merge-level stress testing

## Storycraft lane

Use this lane when the issue is not raw canon but novelist-side strategy, structure, reveal control, or reader-retention design:

1. `structure-architect`
2. `arc-psychologist`
3. `reveal-choreographer`
4. `foreshadow-bookkeeper` if long-tail payoff bookkeeping matters
5. `serial-tension-engineer`
6. `plausibility-warden`
7. `scene-smith` only if the user also wants prose
8. `chapter-inspector` for final validation

## Foreshadow lane

Use this lane when the issue is not raw canon but clue path and payoff control:

1. `foreshadow-bookkeeper`
2. `timeline-historian`
3. `world-rule-keeper` if the reveal changes world-law meaning
4. `plausibility-warden`

## Dynamic split authority

If the setting task is too broad for one domain owner, split further without asking again.

- Add `relic-curator` for items, weapons, cursed artifacts, or possession continuity.
- Add `monster-ecologist` for monsters, outbreaks, mutation ecology, or infection pressure.
- Add `systems-chancellor` for economy, guilds, nobility, cartel structure, or survival institutions.
- Add `structure-architect` for series design, ending backsolve, act turns, and volume promises.
- Add `arc-psychologist` for wound, desire, fear, relationship pressure, and identity-shift design.
- Add `reveal-choreographer` for secret ladders, misdirection fairness, and staged truth delivery.
- Add `serial-tension-engineer` for chapter-end carry, scene pressure, and retention cadence.
- Keep final merge authority in `novel-orchestra-conductor`.

## Separation rules

- `lore-forgemaster` does not write chapter prose.
- `plausibility-warden` does not invent hidden canon without flagging it as a lore delta.
- `scene-smith` does not silently change roadmap or timeline facts.
- `hook-doctor` does not repair deep continuity failures.
- `chapter-inspector` does not rewrite an entire chapter unless the user explicitly asks.
- `structure-architect` does not silently rewrite canon or volume outcomes.
- `arc-psychologist` does not flatten conflict into clean therapy language.
- `reveal-choreographer` does not rely on unfair hidden information.
- `serial-tension-engineer` does not use hollow cliffhangers or gore spectacle as pressure.

## Merge protocol

- Consolidate specialist outputs into one change list before editing files.
- Apply only compatible deltas.
- State assumptions explicitly.
- Resolve conflicts with this truth order:
  1. roadmap
  2. timeline
  3. chapter-to-chapter continuity
  4. stylistic flourish

## Utilities

- Use `../chrono-weaver/scripts/` and `../../backend/` as low-level helpers only.
- Keep the conductor responsible for file selection, lane ordering, and final merge decisions.
- Use `scripts/validate_repo_contract.py` after changing orchestration docs or skill references when Python is available.

## Finish

- Run the lightest relevant verification available after merging.
- Summarize remaining risks, especially unresolved canon ambiguity, reveal fairness risk, or chapter continuity exposure.
