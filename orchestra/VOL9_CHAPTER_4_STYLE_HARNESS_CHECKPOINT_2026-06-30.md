# Vol.9 Chapter 4 Style-Harness Checkpoint

Date: `2026-06-30 KST`
Status: `잠금 완료`

## Scope

- Target: `Drafts/Vol_9/Vol_9_Chapter_4.md`
- Prior edge: `Drafts/Vol_9/Vol_9_Chapter_3.md`
- Right edge: `Drafts/Vol_9/Vol_9_Chapter_5.md`
- Queue: RTTP Style-Harness Recast
- Skill: `rttp-lock-cycle`

## Required Packet Read

Read fully for this pass:

- `orchestra/SESSION_STATE.md`
- `orchestra/NEXT_DIALOGUE_HANDOFF.md`
- `orchestra/EXECUTION_PROGRESS_LEDGER.md`
- `Drafts/Vol_9/Vol_9_Chapter_3.md`
- `Drafts/Vol_9/Vol_9_Chapter_4.md`
- `Drafts/Vol_9/Vol_9_Chapter_5.md`
- `outline/Vol_9_Outline.md`
- `outline/Vol_9_Timeline.md`
- `orchestra/RTTP_ENGINE.md`
- `Guidelines/Chapter_Audit_Checklist.md`
- `Guidelines/Prompt_Quick_Reference.md`
- `Guidelines/Writing_Prompt_Template.md`
- `Guidelines/Banned_Surface_Ledger.md`
- `Guidelines/Time_Travel_Frame.md`
- `lore_bible/style/Tone_Manner_Guide.md`
- `orchestra/VOL9_CHAPTER_3_STYLE_HARNESS_CHECKPOINT_2026-06-30.md`
- `orchestra/VOL8_CHAPTER_21_25_STYLE_HARNESS_AGGREGATE_CHECKPOINT_2026-06-30.md`
- `00_CANON.md`
- `lore_bible/characters/Protagonist.md`
- `lore_bible/characters/Iris.md`
- `lore_bible/Time_Travel_Laws.md`
- `lore_bible/rules/Forced_Return_Residual_Syntax.md`

## Specialist FAIL Ledger

- Hook/first-screen: FAIL. Raw title used numeric episode prefix `204화 빈자리의 얼굴`, and the opening lingered in explanation before the rumor/face pressure cut in.
- Mid-pressure/scene-causality: FAIL. Raw draft owned the correct face/upper-observer lane, but it needed a cleaner bridge from Ch3's `관측` and hand/intermediary proof into the old observer and rhythm-reading mechanism.
- Ending click: FAIL. Raw ending pointed at the next action broadly, but it did not sharply force the Ch5 threshold-corruption lane while preserving Ch5's concrete mechanics.
- Time-scent/regression-route: FAIL. Raw surface contained 46 backticks and strict route-scent residues including `이번엔`, `이번`, and `이미`.
- Motif overuse/style: FAIL. `빈자리`, `관측`, and reading devices repeated from Ch3 without enough new function until the chapter made the new fact explicit: the seat reads the rhythm between people, not just a person.
- Clarity/canon-continuity: FAIL. The chapter needed to keep Iris's memory damage as body-first response, keep 후영 as delayed cost rather than answer-key, and show why Aiden is tempted by the seat.
- Style-harness fit: FAIL. Raw text was clear in lane but too artifact-marked and undercut by explanatory packaging.
- Length/format: FAIL. Raw body no-space count was `3,616`, below the 4,800 floor, and contained a numeric title plus 46 backticks.

## Narrow Repair

- Changed title from `204화 빈자리의 얼굴` to `빈자리의 얼굴`.
- Rebuilt Ch4 as the face/upper-observer reveal:
  - Ch3's `외벽 3-1`, `관측`, `둘이 아니었군. 셋이었어.`, and the hand/intermediary proof become the pressure that sends rumor and confirmation lines down into 북빈가.
  - 레나's rumor gives `결손 확인선이 셋으로 갈렸다` and `빈자리 얼굴 본 놈은 오래 못 산다`, making the face pressure immediate.
  - The 폐종탑 vantage, 젊은 여자, 늙은 남자, and 유리판 own Ch4's upper-reader lane.
  - `이탈`, `재검`, `활용 보류`, and the 빈 패 prove the old observer is weighing the unresolved `결손 1 자리`.
  - `칼로 읽지 마` / `박자로` establishes the new function: the seat reads Aiden and Iris's shared rhythm, not only Aiden's body.
  - 후영 shows Aiden in the seat as a dangerous attraction, not a clean future answer.
  - Ending lands on the need to delay the confirmation path and learn to be wrong together, setting up Ch5 without using Ch5's threshold/in장함/전이복도 mechanics.
- Removed raw backticks, numeric-title prefix, strict route-scent terms, and Ch5 reserved mechanics.

## Final Metrics

| File | Title | Body no-space | Total no-space | Lines | Chars | SHA-256 |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| `Drafts/Vol_9/Vol_9_Chapter_4.md` | `빈자리의 얼굴` | `5,493` | `5,499` | `812` | `7,797` | `23E9E49A9217EF54DE6E15232B7D066855F92BB26F18180D15D8990E8BB17197` |

Detector results:

- Numeric title prefix: `0`
- Backticks: `0`
- Strict route-scent terms checked: `루프`, `회귀`, `루트`, `공략`, `시스템`, `세이브`, `로드`, `리셋`, `게임처럼`, `상태창`, `정답`, `이번엔`, `이번`, `이미` -> `0`
- Ch5 reserved-lane terms checked: `결손의 문턱`, `문턱`, `바로 쓰지 못하게`, `후보가 망가졌다`, `후보가 둘이 아니라 넷`, `문턱 자체가 오염`, `전이 복도`, `인장함`, `박자 확인`, `이관 보류`, `격리 우선` -> `0`
- Required Ch4 markers present: `빈자리의 얼굴`, `외벽 3-1`, `관측`, `동벽 결손 1`, `둘이 아니었군`, `셋이었어`, `빈자리 얼굴 본 놈`, `오래 못 산다`, `폐종탑`, `늙은 남자`, `유리판`, `이탈`, `재검`, `활용 보류`, `빈 패`, `결손 1 자리`, `칼로 읽지 마`, `박자로`, `둘이 맞으면`, `셋째가 열린다`, `같이 틀리는 법`
- Duplicate contiguous nonempty 5-line windows: `0`
- BOM: `0`
- EOF newline: present

## Final No-Edit 5-Cycle Verification

All cycles ran after the final full reread with no edits between or after cycles. A prior detector run had a boolean precedence bug in the BOM check; the corrected no-edit gate below is the valid final run.

| Cycle | Result | Body no-space | Hash |
| --- | --- | ---: | --- |
| 1 | PASS | `5,493` | `23E9E49A9217EF54DE6E15232B7D066855F92BB26F18180D15D8990E8BB17197` |
| 2 | PASS | `5,493` | `23E9E49A9217EF54DE6E15232B7D066855F92BB26F18180D15D8990E8BB17197` |
| 3 | PASS | `5,493` | `23E9E49A9217EF54DE6E15232B7D066855F92BB26F18180D15D8990E8BB17197` |
| 4 | PASS | `5,493` | `23E9E49A9217EF54DE6E15232B7D066855F92BB26F18180D15D8990E8BB17197` |
| 5 | PASS | `5,493` | `23E9E49A9217EF54DE6E15232B7D066855F92BB26F18180D15D8990E8BB17197` |

Cycle checks held:

- First 20 lines hook: PASS
- Mid-pressure/scene-causality: PASS
- Ending click: PASS
- Time-scent guard: PASS
- Motif/style function: PASS
- Clarity/canon-continuity: PASS
- Style-harness fit: PASS
- Length/format: PASS
- Right-edge reservation: PASS

## Queue Update

- Individual style-harness verified range advances through `Vol.9 Chapters 1~4`.
- Aggregate style-harness verified range remains contiguous through `Vol.8 Chapters 1~25`.
- Next single-chapter target: `Vol.9 Chapter 5`.
- Ch5 watch: raw title `205화 결손의 문턱`; it may own threshold corruption, delayed use, false candidate status, transition corridor, seal-box, and `박자 확인` evidence. Ch4 has already used only the face/old-observer/glass-plate and rhythm-reading reveal, preserving Ch5's concrete sabotage lane and Ch6's `박자 절단` continuation.
