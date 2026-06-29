# Vol.8 Chapter 21 Style-Harness Checkpoint

Date: 2026-06-30 KST

## Unit

- Target: `Drafts/Vol_8/Vol_8_Chapter_21.md`
- Prior edge read: `Drafts/Vol_8/Vol_8_Chapter_20.md`
- Right edge read: `Drafts/Vol_8/Vol_8_Chapter_22.md`
- Status: style-locked complete after full packet read, specialist FAIL ledger, narrow repair, full reread after edits, and final no-edit 5-cycle verification.

## Required Packet Read

- `orchestra/SESSION_STATE.md`
- `orchestra/NEXT_DIALOGUE_HANDOFF.md`
- `orchestra/EXECUTION_PROGRESS_LEDGER.md`
- `Drafts/Vol_8/Vol_8_Chapter_20.md`
- `Drafts/Vol_8/Vol_8_Chapter_21.md`
- `Drafts/Vol_8/Vol_8_Chapter_22.md`
- `outline/Vol_8_Outline.md`
- `outline/Vol_8_Timeline.md`
- `orchestra/RTTP_ENGINE.md`
- `Guidelines/Chapter_Audit_Checklist.md`
- `Guidelines/Prompt_Quick_Reference.md`
- `Guidelines/Writing_Prompt_Template.md`
- `Guidelines/Banned_Surface_Ledger.md`
- `Guidelines/Time_Travel_Frame.md`
- `lore_bible/style/Tone_Manner_Guide.md`
- `lore_bible/style/Aiden_Voice.md`
- `lore_bible/style/Naming_Style_Guide.md`
- `00_CANON.md`
- `lore_bible/characters/Protagonist.md`
- `lore_bible/characters/Iris.md`
- `lore_bible/Time_Travel_Laws.md`
- `lore_bible/rules/Equivalent_Exchange.md`
- `lore_bible/rules/Forced_Return_Residual_Syntax.md`
- `lore_bible/locations/The_Grey_City_Map.md`
- `orchestra/VOL8_CHAPTER_20_STYLE_HARNESS_CHECKPOINT_2026-06-29.md`
- `orchestra/VOL8_CHAPTER_1_5_STYLE_HARNESS_AGGREGATE_CHECKPOINT_2026-06-26.md`

## Specialist FAIL Ledger

- Hook/first-screen FAIL with repair: the live chapter opened on the correct ledger-reading pressure, but the numeric title prefix and artifact backticks broke the clean first-screen surface. The repair leaves the title as `북구획 유입분` and removes all backticks while preserving the immediate ledger hook.
- Mid-pressure/scene-causality FAIL with repair: the ledger logic was clear, but Ch21's outline-owned survivor-consolidation lane was too thin. The repair adds 북빈가's practical response: silent signals, route tokens, local witnesses, and people sharing paths without restoring personal memory.
- Ending click FAIL with repair: the live ending pointed to the hand that wrote `위임자 확인`, but needed a stronger bridge proving the fight is no longer only Aiden and Iris reading a ledger. The repair lands on `장부 안에 없는 사람들이었다`, then returns to `위임자 확인` as the next actionable pressure.
- Time-scent/regression-route FAIL with repair: strict route-scent hits on `이번엔` and `정답` were replaced with current-scene wording. 후영 remains a costly contamination of letters, not an answer key.
- Motif overuse/style FAIL with repair: removed all 64 artifact backticks and kept ledger entries as in-world text rather than code-like surfaces.
- Clarity/canon-continuity PASS with repair: Ch21 now owns deeper `북구획 유입분` reading, `공백 관측반` linkage, `남수문 외곽` / `동벽 하층` / `위임자 확인`, and 북빈가 survivor route-network consolidation. Ch22 remains reserved for the live `남수문` operation and the outline/live `무장` alignment question.
- Style-harness fit PASS with repair: Aiden stays body-delayed and cost-first; Iris chooses by practical reading; north-bin people prove trust through signals and route fragments rather than sentimental recognition.
- Length/format FAIL with repair: live chapter was `3,196` body no-space with numeric title, 64 backticks, and strict hits. Final body no-space is `4,887` with clean title and zero detector failures.

## Narrow Repairs Applied

- Removed numeric episode prefix, leaving title as `북구획 유입분`.
- Removed all 64 artifact backticks.
- Replaced route-scent surfaces:
  - `"이번엔 길이 아니라 글자."` -> `"길이 아니라 글자 쪽이야."`
  - `정답을 얻어서가 아니라,` -> `완전한 답을 얻어서가 아니라,`
  - nearby `이번`-coded phrasing was softened to current-scene wording.
- Expanded only Ch21-local material:
  - north-bin silent signal and shelter movement after Iris names Aiden as currently on their side,
  - small route/help tokens that prove traces remain even when memory does not,
  - 레나's practical refusal to empty the settlement,
  - anonymous survivor fragments for 남수문 route pressure,
  - ending bridge that frames the opposition as ledgered people versus people outside the ledger.

## Metrics

Initial live boundary risks before repair:

- title: `196화 북구획 유입분`
- body no-space: `3,196`
- total no-space: `3,206`
- line records: `316`
- content lines: `222`
- episode numeric prefix: `1`
- backticks: `64`
- strict route-scent hits: `2` (`이번엔`, `정답`)
- banned/surface hits: `0`
- sha256: `8D5C061C65B6ED0D18BFB316FCC6070E7E643A2A549595B68EA4260A25914204`

Final metrics after full reread and final no-edit gate:

- title: `북구획 유입분`
- body no-space: `4,887`
- total no-space: `4,893`
- line records: `481`
- content lines: `351`
- episode numeric prefix: `0`
- under-floor failure: `0`
- backticks: `0`
- Latin hits: `0`
- Arabic/Devanagari/Bengali stray-script hits: `0`
- strict route-scent hits: `0`
- banned/surface hits: `0`
- required marker misses: `0`
- reserved Ch22-lane hits: `0`
- duplicate contiguous nonempty 5-line windows: `0`
- BOM: `0`
- EOF missing: `0`
- sha256: `CC36F451116217914453868D1821286B093C492CE3932FF6A37745BBA69601CA`

## Final No-Edit 5-Cycle Verification

| Cycle | Result | Body no-space | Total no-space | Hash | Title fail | Under floor | Backticks | Latin | Stray script | Strict route | Banned | Required misses | Reserved Ch22 | Dup 5-line | BOM | EOF missing |
| --- | --- | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | PASS | 4,887 | 4,893 | `CC36F451116217914453868D1821286B093C492CE3932FF6A37745BBA69601CA` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | PASS | 4,887 | 4,893 | `CC36F451116217914453868D1821286B093C492CE3932FF6A37745BBA69601CA` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | PASS | 4,887 | 4,893 | `CC36F451116217914453868D1821286B093C492CE3932FF6A37745BBA69601CA` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 4 | PASS | 4,887 | 4,893 | `CC36F451116217914453868D1821286B093C492CE3932FF6A37745BBA69601CA` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 5 | PASS | 4,887 | 4,893 | `CC36F451116217914453868D1821286B093C492CE3932FF6A37745BBA69601CA` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

All five cycles held with zero numeric-prefix title fail, zero under-floor failure, zero backticks, zero Latin hits, zero stray-script hits, zero strict route-scent hits, zero banned/surface hits, zero required marker misses, zero Ch22 reserved-lane hits, zero duplicate contiguous nonempty 5-line windows, zero byte-level BOM, and zero EOF missing.

## Result

- Vol.8 Chapter 21 is style-locked complete.
- Current style-harness verified range advances through `Vol.8 Chapters 1~21`.
- Current aggregate style-harness verified range remains through `Vol.8 Chapters 1~5`.
- Next required unit is `Vol.8 Chapter 22`.
