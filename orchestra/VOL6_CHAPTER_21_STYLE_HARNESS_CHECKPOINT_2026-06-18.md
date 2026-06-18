# Vol.6 Chapter 21 Style-Harness Checkpoint

- Date: `2026-06-18 KST`
- Mode: `rttp style-harness recast`
- Skill: `rttp-lock-cycle`
- Unit: `Vol.6 Chapter 21`
- Target file: `Drafts/Vol_6/Vol_6_Chapter_21.md`
- Prior edge: `Drafts/Vol_6/Vol_6_Chapter_20.md`
- Right edge: `Drafts/Vol_6/Vol_6_Chapter_22.md`

## Required Packet Read

- Orchestra state: `orchestra/SESSION_STATE.md`, `orchestra/NEXT_DIALOGUE_HANDOFF.md`, `orchestra/EXECUTION_PROGRESS_LEDGER.md`.
- Target packet: `Drafts/Vol_6/Vol_6_Chapter_20.md`, `Drafts/Vol_6/Vol_6_Chapter_21.md`, `Drafts/Vol_6/Vol_6_Chapter_22.md`.
- Right-edge existence check: `Drafts/Vol_6/Vol_6_Chapter_23.md` exists and begins with `후영의 포효`.
- Vol.6 guides: `outline/Vol_6_Outline.md`, `outline/Vol_6_Timeline.md`, `orchestra/RTTP_ENGINE.md`.
- Harness guides: `Guidelines/Chapter_Audit_Checklist.md`, `Guidelines/Prompt_Quick_Reference.md`, `Guidelines/Writing_Prompt_Template.md`, `Guidelines/Banned_Surface_Ledger.md`, `Guidelines/Time_Travel_Frame.md`, `lore_bible/style/Tone_Manner_Guide.md`.
- Canon and character context: `00_CANON.md`, `lore_bible/Time_Travel_Laws.md`, `lore_bible/rules/Equivalent_Exchange.md`, `lore_bible/characters/Protagonist.md`, `lore_bible/characters/Iris.md`, `lore_bible/characters/Ria.md`, `lore_bible/characters/Baltazar.md`, `lore_bible/characters/Mirel.md`.
- Previous checkpoints: `orchestra/VOL6_CHAPTER_20_STYLE_HARNESS_CHECKPOINT_2026-06-18.md`, `orchestra/VOL6_CHAPTER_16_20_STYLE_HARNESS_AGGREGATE_CHECKPOINT_2026-06-18.md`.

## Continuity Check

- Ch20 ends on enemy trap/capture-reading pressure and a shadow moving ahead of Aiden.
- Ch21 spends that edge into repeated `그림자 사냥`: uniform traces, black powder, fixed sickle pressure, role-divided hunters, observer/record tools, white powder and ink lines, fixation, and repeated measurement.
- Ch21 cost holds: Aiden survives and damages hunters, but accepts that night is also a hunting ground; intervention and retreat both become measured choices.
- Ch21 preserves Ch22: it only bridges with Baltazar drawing a small tower shape and does not explain `시간의 탑` or the proposal payload.
- Ch22 was read as right edge only; Ch23 exists with `후영의 포효` for the next right-edge handoff.
- `Drafts/Vol_6/Vol_6_Chapter_21.md` was dirty on entry and was treated as the live target.

## Specialist FAIL Ledger

- 가장 치명적인 FAIL: title/format and surface. The target entered without a clean title and carried non-required modern surface (`패턴` x5, `함수` x1) plus technical register (`반응 곡선`, `임계점`, `자료`, `전술조`).
- Hook/first-screen: PASS after adding the title. The first movement opens from Ch20's trap into a repeated-hunt frame.
- Mid-pressure/scene-causality: PASS. Pursuit pressure escalates by trace, measurement, fixation, powder/ink, and role division rather than by explanation.
- Ending click: PASS. `밤 안에서만 버티면 진다` turns survival into a strategic loss condition, then hands Ch22 the tower sketch.
- Time-scent/regression-route: PASS. Cost and route-reading stay tactile and behavioral, not systemized.
- Motif overuse/style: PASS after repairs. Required hunt/fixation terms remain, while non-required modern surfaces are removed.
- Clarity/canon-continuity: PASS. Ch20 enemy-trap handoff is spent; Ch22 tower-proposal payload remains reserved.
- Style-harness fit: PASS after surface replacements.
- Length/format: PASS. Title present, no backticks, no Latin hits, no BOM, no extra EOF blank.

## Narrow Repair

- Added clean title `그림자 사냥`.
- Replaced non-required `패턴` surfaces with older-register equivalents: `결`, `움직임의 결`, `도망길`, `소리 결`.
- Replaced `반응 함수처럼` with `반응 순서처럼`.
- Replaced `자료` with `기록`.
- Replaced `반응 곡선` with `반응의 굽이`.
- Replaced `임계점` language with `선`.
- Replaced `전술조` with `사냥조`.
- No plot boundary, Ch22 proposal payload, or right-edge chapter content was rewritten.

## Full Reread After Repair

- Full Ch21 reread completed after the final cleanup edit.
- The chapter still spends only Ch21's `그림자 사냥` hunt/measurement pressure and leaves Ch22's `발타자르의 제안` / `시간의 탑` explanation for the next unit.

## Final No-Edit 5-Cycle Verification

| Cycle | Body no-space | Total no-space | Title | Backticks | Latin hits | Duplicate 5-line windows | Banned/surface hits | Ch22+ reserved hits | BOM | EOF extra blank | Hash | Result |
| --- | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| 1 | 5,494 | 5,499 | `그림자 사냥` | 0 | 0 | 0 | 0 | 0 | false | false | `A0FDDFE7B6A7413E9BC5D42A946A76E8A021CEC5B230B814394B723FACFC33B4` | PASS |
| 2 | 5,494 | 5,499 | `그림자 사냥` | 0 | 0 | 0 | 0 | 0 | false | false | `A0FDDFE7B6A7413E9BC5D42A946A76E8A021CEC5B230B814394B723FACFC33B4` | PASS |
| 3 | 5,494 | 5,499 | `그림자 사냥` | 0 | 0 | 0 | 0 | 0 | false | false | `A0FDDFE7B6A7413E9BC5D42A946A76E8A021CEC5B230B814394B723FACFC33B4` | PASS |
| 4 | 5,494 | 5,499 | `그림자 사냥` | 0 | 0 | 0 | 0 | 0 | false | false | `A0FDDFE7B6A7413E9BC5D42A946A76E8A021CEC5B230B814394B723FACFC33B4` | PASS |
| 5 | 5,494 | 5,499 | `그림자 사냥` | 0 | 0 | 0 | 0 | 0 | false | false | `A0FDDFE7B6A7413E9BC5D42A946A76E8A021CEC5B230B814394B723FACFC33B4` | PASS |

Required target hits held across all cycles: `그림자 사냥=2; 함정은 한 번으로 끝나지 않았다=1; 폐수정장=3; 고정낫=1; 사냥=33; 고정됐다=1; 고정용=1; 하얀 가루=4; 밤 안에서만 버티면 진다=1; 탑 모양=1`.

## Result

- `Vol.6 Chapter 21` style-harness locked complete.
- Style verified range advances through `Vol.6 Chapter 21`.
- Aggregate style verified range remains through `Vol.6 Chapter 20`.
- Next target: `Vol.6 Chapter 22`.
