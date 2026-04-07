# Orchestra Workflow

This document explains how the repo-local novel orchestra should operate.

## Goal

- Keep canon repair, storycraft planning, later drafting, and audit work separated.
- Let specialists own narrow problems while the conductor owns merge order and final decisions.
- Use only the lanes that remove the current bottleneck.
- While `SETTING_FIRST_MODE.md` is active, treat drafting lanes as suspended by default.

## Core files

- `SESSION_STATE.md`: active working context and current targets
- `WORKFLOW.md`: operating rules and lane order
- `SETTING_FIRST_MODE.md`: declares that the project is still finishing the setting library before prose
- `SOURCE_OF_TRUTH.md`: canonical priority order and no-touch references
- `Guidelines/Setting_Audit_Scope.md`: audit surface map for full setting-library work
- `HANDOFF_PACKET_PLAYBOOK.md`: fast packet choices for common orchestra missions
- `LORE_AUDIT_HARNESS.md`: full-domain lore audit flow
- `FORESHADOW_HARNESS.md`: clue and payoff audit flow
- `STORYCRAFT_HARNESS.md`: structure, reveal, arc, and cadence planning flow
- `lore_bible/Mid_War_Emotional_Continuity.md`: Vol. 4~8 emotional continuity canon
- `lore_bible/history/Fixed_Point_Pressure_Map.md`: fixed-point, branch, and pressure grammar
- `templates/WORK_PACKET.md`: conductor dispatch format
- `templates/AGENT_REPORT.md`: specialist report format
- `templates/REVISION_LEDGER.md`: merge log for accepted deltas
- `scripts/Build-LoreAuditPackets.ps1`: PowerShell lore-audit packet builder

## Operating rules

1. Update `SESSION_STATE.md` when a long-running task changes target or scope.
2. The conductor reads the truth sources first and creates a work packet.
3. For repeatable task shapes, prefer a handoff template or preset before writing a freeform packet.
4. Specialists work only from the packet and their required reads.
5. Specialists return structured findings before file edits happen.
6. The conductor merges only compatible deltas into canonical files.

## Lane patterns

### Canon build or repair

1. `novel-orchestra-conductor`
2. `lore-forgemaster`
3. `chrono-weaver`
4. `plausibility-warden`
5. `chapter-inspector` if the result will immediately touch prose

### Lore library audit

1. `novel-orchestra-conductor`
2. domain specialists as needed
3. `chrono-weaver`
4. `arc-psychologist` when emotional continuity is the bottleneck
5. `lore-forgemaster` if repair patches are needed
6. `plausibility-warden`

For fixed-point or branch-pressure work, prefer:

1. `novel-orchestra-conductor`
2. `chrono-weaver`
3. `world-rule-keeper`
4. `plausibility-warden`

Optional detail lanes:

- `relic-curator`
- `monster-ecologist`
- `systems-chancellor`

### Storycraft planning

1. `novel-orchestra-conductor`
2. `structure-architect` when skeleton or ending-backsolve is unstable
3. `arc-psychologist` when the emotional path is thin
4. `reveal-choreographer` when truth delivery is weak
5. `foreshadow-bookkeeper` when clue bookkeeping is missing
6. `serial-tension-engineer` when chapters drag or exits feel soft
7. `plausibility-warden`
8. `scene-smith` only after setting-first mode is lifted
9. `chapter-inspector` only after setting-first mode is lifted

### Foreshadow and payoff audit

1. `novel-orchestra-conductor`
2. `foreshadow-bookkeeper`
3. `timeline-historian`
4. `world-rule-keeper` if the reveal depends on rules
5. `plausibility-warden`

Conductor note:

- Lock both the ledger and the front-half clue map when a reveal changes whole-series meaning.
- If a payoff relies on a clue that first appears in the same volume, treat it as under-seeded until proven otherwise.

### Post-setting drafting or rewrite

This lane is inactive until the conductor explicitly lifts `setting-first mode`.

## Packet rules

Every packet should lock:

- `Mission`
- `Lane`
- `Target`
- `State Snapshot`
- `Required Reads`
- `Locked Facts`
- `Editable Targets`
- `No-Touch Files`
- `Deliverable`
- `Blocking Decisions`
- `Stop Conditions`

## Anti-patterns

- Drafting before canon blockers are resolved
- Drafting while setting-first mode is still active
- Mixing lore invention and prose revision in one undifferentiated pass
- Running many lanes against the same file when a narrower route is enough
- Treating setting work as outline/timeline-only maintenance
- Using twist energy or gore spectacle to cover for weak structure
- Skipping the merge step and letting specialist suggestions overwrite canon directly
