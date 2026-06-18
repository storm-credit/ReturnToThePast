# Vol.6 Chapter 17 Style-Harness Checkpoint

- Date: `2026-06-18 KST`
- Mode: `rttp style-harness recast`
- Skill: `rttp-lock-cycle`
- Unit: `Vol.6 Chapter 17`
- Target file: `Drafts/Vol_6/Vol_6_Chapter_17.md`
- Prior edge: `Drafts/Vol_6/Vol_6_Chapter_16.md`
- Right edge: `Drafts/Vol_6/Vol_6_Chapter_18.md`

## Required Packet Read

- `orchestra/SESSION_STATE.md`
- `orchestra/NEXT_DIALOGUE_HANDOFF.md`
- `orchestra/EXECUTION_PROGRESS_LEDGER.md`
- `Drafts/Vol_6/Vol_6_Chapter_16.md`
- `Drafts/Vol_6/Vol_6_Chapter_17.md`
- `Drafts/Vol_6/Vol_6_Chapter_18.md`
- `outline/Vol_6_Outline.md`
- `outline/Vol_6_Timeline.md`
- `orchestra/RTTP_ENGINE.md`
- `Guidelines/Chapter_Audit_Checklist.md`
- `Guidelines/Prompt_Quick_Reference.md`
- `Guidelines/Writing_Prompt_Template.md`
- `Guidelines/Banned_Surface_Ledger.md`
- `Guidelines/Time_Travel_Frame.md`
- `lore_bible/style/Tone_Manner_Guide.md`
- `orchestra/VOL6_CHAPTER_16_STYLE_HARNESS_CHECKPOINT_2026-06-18.md`
- `orchestra/VOL6_CHAPTER_11_15_STYLE_HARNESS_AGGREGATE_CHECKPOINT_2026-06-18.md`
- `00_CANON.md`
- `lore_bible/Time_Travel_Laws.md`
- `lore_bible/rules/Equivalent_Exchange.md`
- `lore_bible/characters/Protagonist.md`
- `lore_bible/characters/Iris.md`
- `lore_bible/characters/Ria.md`
- `lore_bible/characters/Baltazar.md`
- `lore_bible/characters/Mirel.md`

## Continuity Check

- Ch16 ends with the dawn report payload `야간 교전 다수`, `개입자 확인 불가`, and the first unofficial `유령` naming.
- Ch17 spends the required broader packet: repeated-night reports, Ria and Barkan's record struggle, enemy adaptation, the `유령의 전쟁` frame, and the move from rumor to tactical response.
- Ch18 remains protected as the `이름 없는 검` / enemy-base destruction packet. Ch17 no longer uses `이름 없는 검` or the enemy-base destruction payload.
- `Drafts/Vol_6/Vol_6_Chapter_18.md` was dirty on entry and was read as the right edge only.

## Specialist FAIL Ledger

- 가장 치명적인 FAIL: title/format and length. The live target was already dirty on entry, opened without the clean title `유령의 전쟁`, and held only `body_nospace=4,492`, below the active `4,800` floor.
- 반복 압력 FAIL: the chapter's report ladder, `유령`, invisible combat, and missing-name motifs were functional, but the final block repeated Ch18's `이름 없는 검` payload instead of closing Ch17's records/war escalation.
- 오류 검 FAIL: right-edge payload intrusion. The live ending pulled in Ch18's short-sword/nameless-blade setup, weakening the Chapter 18 boundary.
- 결말 압력 FAIL: the pre-repair ending pointed into Ch18's object packet too early. It needed to end on the ongoing report/war pressure instead.
- 문체/명료도 FAIL: title and body-floor repair were required. One new line briefly introduced `이미`; it was removed during reread as a time-scent risk.
- Hook / first-screen: PASS after repair. The chapter now opens with the clean title and immediately turns Ch16's first `유령` report into institutional uncertainty.
- Mid-pressure / scene-causality: PASS after repair. Reports escalate into repeated nights, enemy adaptation, deliberate fear propagation, and the trap at the dry reservoir.
- Ending click: PASS after repair. The ending now lands on records, empty subject positions, Barkan/Ria pressure, and Aiden's continuing movement rather than Ch18's blade.
- Time-scent / regression-route: PASS after repair. No game/route framing or regression-coded wording remains in the final gate.
- Motif overuse / style: PASS. `유령`, reports, empty names, and invisible combat recur with changed function: rumor, record, tactical adaptation, and war frame.
- Clarity / canon-continuity: PASS. Vol.6 D+20 isolation, forbidden memory erasure cost, Ria/Barkan record roles, Baltazar's witness position, and Ch18 boundary all hold.
- Style-harness fit: PASS after repair. The chapter stays dry, report-driven, reaction-proven, violence-controlled, and mobile-readable.
- Length / format: PASS after repair. Final body no-space count is `5,147`; total no-space count is `5,152`.

## Narrow Repair

- Added the clean title `유령의 전쟁`.
- Removed the Ch18-intrusive `이름 없는 검` ending block from Ch17.
- Replaced that ending position with Ch17-specific report/war pressure: Ria's fear of result-only records, Barkan's map/ledger hesitation, enemy-side tactical reading, and Aiden's need to remain a pressure rather than a voice.
- Removed one residual `이미` in the new block during post-repair reread.
- No prior edge, right edge, Ch18 `이름 없는 검`, Ch18 enemy-base destruction, Ch19 `발타자르의 기억`, or later Vol.6 payload was rewritten.

## Full Reread After Repair

- Full Ch17 reread completed after title, ending-boundary, body-floor, and `이미` cleanup.
- The repaired chapter still spends only Ch17's repeated-night records, enemy adaptation, `유령의 전쟁` naming, and record/outside-war pressure.
- Ch18 remains a right edge only and keeps the object/base-destruction payload for the next unit.

## Final No-Edit 5-Cycle Verification

| Cycle | Body no-space | Total no-space | BOM | Backticks | EOF extra blank | Latin hits | Title | Duplicate exact 5-line windows | Banned/meta hits | Required Ch17 hits | Ch18 payload intrusion | Hash | Result |
| --- | ---: | ---: | --- | ---: | --- | ---: | --- | ---: | ---: | --- | ---: | --- | --- |
| 1 | 5,147 | 5,152 | false | 0 | false | 0 | `유령의 전쟁` | 0 | 0 | `유령의 전쟁=3; 기록 밖 전투 지속=1; 야간 전장 비가시 개입 지속=1; 유령=8` | 0 | `E9475F19511F4BB18F61786E65BA39C2D71F26C5E2FB52C272D9CBDCF1DE0AF7` | PASS |
| 2 | 5,147 | 5,152 | false | 0 | false | 0 | `유령의 전쟁` | 0 | 0 | `유령의 전쟁=3; 기록 밖 전투 지속=1; 야간 전장 비가시 개입 지속=1; 유령=8` | 0 | `E9475F19511F4BB18F61786E65BA39C2D71F26C5E2FB52C272D9CBDCF1DE0AF7` | PASS |
| 3 | 5,147 | 5,152 | false | 0 | false | 0 | `유령의 전쟁` | 0 | 0 | `유령의 전쟁=3; 기록 밖 전투 지속=1; 야간 전장 비가시 개입 지속=1; 유령=8` | 0 | `E9475F19511F4BB18F61786E65BA39C2D71F26C5E2FB52C272D9CBDCF1DE0AF7` | PASS |
| 4 | 5,147 | 5,152 | false | 0 | false | 0 | `유령의 전쟁` | 0 | 0 | `유령의 전쟁=3; 기록 밖 전투 지속=1; 야간 전장 비가시 개입 지속=1; 유령=8` | 0 | `E9475F19511F4BB18F61786E65BA39C2D71F26C5E2FB52C272D9CBDCF1DE0AF7` | PASS |
| 5 | 5,147 | 5,152 | false | 0 | false | 0 | `유령의 전쟁` | 0 | 0 | `유령의 전쟁=3; 기록 밖 전투 지속=1; 야간 전장 비가시 개입 지속=1; 유령=8` | 0 | `E9475F19511F4BB18F61786E65BA39C2D71F26C5E2FB52C272D9CBDCF1DE0AF7` | PASS |

## Result

- `Vol.6 Chapter 17` is style-harness locked complete under the current style harness.
- Current style-harness verified range advances to `Vol.1 Chapters 1~25; Vol.2 Chapters 1~25; Vol.3 Chapters 1~25; Vol.4 Chapters 1~25; Vol.5 Chapters 1~25; Vol.6 Chapters 1~17`.
- Current aggregate style-harness verified range remains `Vol.1 Chapters 1~25; Vol.2 Chapters 1~25; Vol.3 Chapters 1~25; Vol.4 Chapters 1~25; Vol.5 Chapters 1~25; Vol.6 Chapters 1~15`.
- Next one-unit target is `Vol.6 Chapter 18`.

## Aggregate Surface Repair Addendum - 2026-06-18 KST

- During aggregate `Vol.6 Chapters 16~20`, one aggregate-level surface repair was made in this chapter: `밤마다 같은 패턴으로 사람이 사라지면` -> `밤마다 같은 순서로 사람이 사라지면`.
- Full Ch17 reread completed after the repair; the repeated-night report ladder, enemy adaptation, `유령의 전쟁`, Ch18 boundary, and style-harness result still hold.
- Revised final metrics after aggregate repair: `body_nospace=5,146`, `total_no_space=5,151`, hash `315205286FC70E5BD910F84AEC57AD869D251E2746AFFBD09CC3924B88AED9AB`.
- The aggregate checkpoint `orchestra/VOL6_CHAPTER_16_20_STYLE_HARNESS_AGGREGATE_CHECKPOINT_2026-06-18.md` supersedes the older hash for packet-level verification.
