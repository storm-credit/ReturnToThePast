# Session State

## Current Objective
- Status: `active`
- Request: setting library is locked; reopen drafting only on request using the launch packet
- Scope: lore_bible / outline / Guidelines / orchestra with draft launch readiness

## Canonical Sources
- `Start_Here.md`
- `outline/Series_Roadmap.md`
- Additional files:

## Active Work Packet
- Mode: `draft-ready-after-setting-lock`
- Target volume/chapter: `Vol.1 Chapter 1 launch readiness`
- Impacted files: `lore_bible/**`, `outline/**`, `Guidelines/**`, `orchestra/**`

## Open Risks
- `.obsidian/**` and `orchestra/runs/**` must stay outside the default commit scope
- local user-side docs in `lore_bible/monsters/Creatures_of_the_Glitch.md` and `lore_bible/psych_logs/pre_death_final_log.md` remain outside the default commit scope
- launch should follow the locked packet rather than ad-libbing a new opening frame

## Decisions
- integration branch remains `codex/orchestra-setting-sync`
- `.obsidian` and `orchestra/runs` stay outside the default commit scope
- drafting lanes remain closed until the exit gate defined in the execution plan
- engine JSON keys stay stable; Korean-facing explanation lives in companion docs
- 2026-04-07 21:05 KST smoke audit passed after the optional-polish pass
- pre-draft packet assembly may complete while `SETTING_FIRST_MODE.md` stays active
- 2026-04-07 21:09 KST smoke audit passed after the Vol. 1 packet bundle was added
- 2026-04-07 user chose to finish the setting library before any new prose pass
- magic and monster layers are part of required completion, not optional garnish
- 2026-04-08 final setting sweep passed and the setting library is treated as locked for launch
- drafting should reopen via `DRAFTING_REOPEN_GATE_2026-04-08.md` and `Vol_1_Chapter_1_Launch_Packet.md`

## Next Step
- if the user requests prose, open the draft lane with the Vol.1 Chapter 1 launch packet and run chapter audit after drafting.
