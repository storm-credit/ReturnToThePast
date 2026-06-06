# Vol.4 Chapter 6 Style-Harness Checkpoint - 2026-06-06 KST

- Target chapter: `Drafts/Vol_4/Vol_4_Chapter_6.md`
- Status: `style-harness locked complete`
- Queue: `rttp-style-harness-completion-loop`
- Conductor: `Codex`
- Skill: `rttp-lock-cycle`
- Unit type: single chapter

## Context Read

- `orchestra/SESSION_STATE.md`
- `orchestra/NEXT_DIALOGUE_HANDOFF.md`
- `Drafts/Vol_4/Vol_4_Chapter_5.md` as prior edge
- `Drafts/Vol_4/Vol_4_Chapter_6.md`
- `Drafts/Vol_4/Vol_4_Chapter_7.md` as right edge
- `outline/Vol_4_Outline.md`
- `outline/Vol_4_Timeline.md`
- `orchestra/RTTP_ENGINE.md`
- `Guidelines/Chapter_Audit_Checklist.md`
- `Guidelines/Prompt_Quick_Reference.md`
- `Guidelines/Writing_Prompt_Template.md`
- `Guidelines/Banned_Surface_Ledger.md`
- `Guidelines/Time_Travel_Frame.md`
- `lore_bible/style/Tone_Manner_Guide.md`
- `00_CANON.md`
- `lore_bible/Time_Travel_Laws.md`
- `lore_bible/Temporal_Facts_Guide.md`
- `lore_bible/rules/Equivalent_Exchange.md`
- `lore_bible/history/Fixed_Points_and_Branches.md`
- `lore_bible/history/Fixed_Point_Pressure_Map.md`
- `lore_bible/characters/Protagonist.md`
- `lore_bible/characters/Iris.md`
- `lore_bible/characters/Ria.md`
- `lore_bible/characters/Baltazar.md`
- `lore_bible/characters/Mirel.md`
- `lore_bible/locations/Seraphim_Transit_Map.md`
- `orchestra/VOL4_CHAPTER_1_5_STYLE_HARNESS_AGGREGATE_CHECKPOINT_2026-06-06.md`

No dedicated Vol.4 pressure grid was found; this pass used the Vol.4 outline/timeline, adjacent edge chapters, latest aggregate checkpoint, and canon/style guidance as the active pressure map.

## Chapter Function

Vol.4 Chapter 6 receives Chapter 5's north-east outer-front order and proves that the crisis is not a normal battlefield problem. The chapter's pressure chain is:

`Ch5 city-maintenance order -> northeast outer-front inspection -> weak-line diagnosis -> rear/transport/message-line collapse -> "one day" survival limit -> conventional weapons cannot finish it -> unlit-room handoff into Ch7's taboo-door discussion`.

The ending now lands directly into Chapter 7's opening condition: Aiden asks for a room where the lights can be put out, while Balthazar's unopened box becomes the silent next-episode object.

## Specialist FAIL Ledger

- Hook / first-screen: PASS. The first screen opens on the outer front as an accident field rather than a heroic battle, then immediately makes sound/order failure the governing problem.
- Mid-pressure / scene-causality: PASS. The chapter escalates through weak lines, failed purification, transport collapse, crossed commands, the knight commander's `one day` limit, and Aiden's decision that the front cannot be ended there.
- Ending click / next-episode force: initial FAIL, then PASS after repair. The earlier ending cooled into explanation about meetings and city maintenance. The repaired ending converts the decision into a concrete handoff: `회의보다 먼저 방 하나가 필요합니다` / `불을 끌 수 있는 방`, matching Ch7's dark-room opening.
- Time-scent / regression-route guard: PASS. `후영`, late sound, bodily refusal, and future-adjacent dread remain body-first and asymmetric; no loop/game route scent remains.
- Motif overuse / style guard: initial FAIL, then PASS after repair. The back third previously stacked `문 / 문법 / 금기 / 장부` too heavily. Repairs cut the explanation drift, returned pressure to transport lines, bandages, delayed orders, and the physical room.
- Clarity / canon-continuity guard: PASS. Ch5 sends Aiden to the outer front; Ch6 proves conventional methods cannot win; Ch7 can now disclose Balthazar's taboo option without a continuity gap.
- Style-harness fit: PASS after repair. The chapter stays dry, civic, object-led, and pressure-forward: front lines, transport carts, command delay, ledgers, bells, and sealed-room preparation carry the decision.
- Length / format gate: initial FAIL, then PASS. Initial blockers were bare title, UTF-8 BOM, backticks, extra EOF blank, and `게임` surface. Final title, BOM, backticks, EOF, banned surfaces, and length all pass.

## Narrow Repairs

- Normalized title from a bare `전선` to `제4권 제6화. 전선`.
- Removed hidden UTF-8 BOM and normalized EOF to a single final newline.
- Removed all in-world backticks.
- Replaced the modern/game-surface phrase `버티는 게임` with `버티는 싸움`.
- Reworked the back-third abstraction cluster so the chapter lands on concrete battlefield cost and the Ch7 dark-room handoff.
- Preserved the chapter's core plot, causal order, character positions, and Ch5/Ch7 continuity.

## Full Reread Verdict

The repaired full reread held. Ch6 now opens with visible disorder at the outer front, diagnoses the actual failure as broken lines rather than stronger enemies, lets the knight commander validate the field truth from below, and ends with Aiden requesting the kind of sealed, dark room Ch7 immediately uses. The chapter no longer explains its final thesis after earning it.

## Final No-Edit 5-Cycle Verification

| Cycle | PASS | Body no-space | No-space | SHA-256 | Hard hits | Backticks | BOM | Extra EOF blank |
| --- | --- | ---: | ---: | --- | ---: | ---: | --- | --- |
| 1 | YES | 4,882 | 4,891 | `A7066D1330EE136967FA832789CB7C953955B691A187BDC002DB5773734E08E4` | 0 | 0 | false | false |
| 2 | YES | 4,882 | 4,891 | `A7066D1330EE136967FA832789CB7C953955B691A187BDC002DB5773734E08E4` | 0 | 0 | false | false |
| 3 | YES | 4,882 | 4,891 | `A7066D1330EE136967FA832789CB7C953955B691A187BDC002DB5773734E08E4` | 0 | 0 | false | false |
| 4 | YES | 4,882 | 4,891 | `A7066D1330EE136967FA832789CB7C953955B691A187BDC002DB5773734E08E4` | 0 | 0 | false | false |
| 5 | YES | 4,882 | 4,891 | `A7066D1330EE136967FA832789CB7C953955B691A187BDC002DB5773734E08E4` | 0 | 0 | false | false |

Context watch terms reviewed as non-blocking scene-native usage: `후영=2`, `시간=5`, `이제=2`, `그때=1`, `처음=2`, `늦=14`, `흔적=1`, `장부=3`, `문턱=1`, `검은=4`, `종=7`, `봉쇄=1`, `전쟁=3`, `전선=19`, `금기=1`, `문법=2`, `문=13`.

## Result

- Vol.4 Chapter 6 is style-harness verified complete.
- Style-harness verified range advances to `Vol.1 Chapters 1~25; Vol.2 Chapters 1~25; Vol.3 Chapters 1~25; Vol.4 Chapters 1~6`.
- Aggregate style-harness verified range remains `Vol.1 Chapters 1~25; Vol.2 Chapters 1~25; Vol.3 Chapters 1~25; Vol.4 Chapters 1~5`.
- Next one-unit run: `Vol.4 Chapter 7`.
- Next aggregate due: `Vol.4 Chapters 6~10` after Chapter 10 passes.
