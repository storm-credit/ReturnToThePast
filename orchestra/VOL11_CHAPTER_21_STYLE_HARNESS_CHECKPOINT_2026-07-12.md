# Vol.11 Chapter 21 Style-Harness Checkpoint

- Date: `2026-07-12 KST`
- Mode: `rttp style-harness recast`
- Skill: `rttp-lock-cycle`
- Automation: `rttp-style-harness-completion-loop`
- Unit processed: `Vol.11 Chapter 21`
- Draft path: `Drafts/Vol_11/Vol_11_Chapter_21.md`
- Final status: `style-locked complete`
- Next unit: `Vol.11 Chapter 22`

## Required Packet Read

- Queue state: `orchestra/SESSION_STATE.md`, `orchestra/NEXT_DIALOGUE_HANDOFF.md`, `orchestra/EXECUTION_PROGRESS_LEDGER.md`
- Target and edges: `Drafts/Vol_11/Vol_11_Chapter_20.md`, `Drafts/Vol_11/Vol_11_Chapter_21.md`, `Drafts/Vol_11/Vol_11_Chapter_22.md`, `Drafts/Vol_11/Vol_11_Chapter_23.md`, `Drafts/Vol_11/Vol_11_Chapter_24.md`
- Additional lookahead metric check: `Drafts/Vol_11/Vol_11_Chapter_25.md`
- Continuity and harness packet: `outline/Vol_11_Outline.md`, `outline/Vol_11_Timeline.md`, `outline/Vol_10_Outline.md`, `outline/Vol_10_Timeline.md`, `orchestra/RTTP_ENGINE.md`, `Guidelines/Chapter_Audit_Checklist.md`, `Guidelines/Prompt_Quick_Reference.md`, `Guidelines/Writing_Prompt_Template.md`, `Guidelines/Banned_Surface_Ledger.md`, `Guidelines/Time_Travel_Frame.md`, `lore_bible/style/Tone_Manner_Guide.md`, `lore_bible/style/Naming_Style_Guide.md`, `00_CANON.md`, `lore_bible/characters/Protagonist.md`, `lore_bible/characters/Iris.md`, `lore_bible/Time_Travel_Laws.md`, `lore_bible/rules/Forced_Return_Residual_Syntax.md`
- Prior checkpoints: `orchestra/VOL11_CHAPTER_20_STYLE_HARNESS_CHECKPOINT_2026-07-12.md`, `orchestra/VOL9_CHAPTER_21_25_STYLE_HARNESS_AGGREGATE_CHECKPOINT_2026-07-07.md`

## Initial Target Metrics

- Raw title: `271화 조사실 밖의 규칙`
- Raw body no-space: `2,715`
- Raw total no-space: `2,726`
- Raw lines: `271` by current live counter
- Raw chars: `3,738`
- Raw backticks: `10`
- Raw strict hits: `이번엔=1; 이번=1; 이미=4; 순간=4`
- Raw own-title hits: `조사실 밖의 규칙=1`
- Raw Latin residue: `0`
- Raw numeric residue: `4`
- Raw hash: `862301ACEB9837BEB124815E9254E57220CC97E48192442603934E7A57F7BF35`

## Specialist FAIL Ledger

- Hook / first-screen FAIL: the numeric episode header, artifact backticks, raw administrative labels, and short abstract opening left the chapter in packet mode instead of immediate outside-room procedural pressure.
- Length / format FAIL: body no-space `2,715` was below the active `4,800` floor and could not be locked without expansion.
- Time-scent / regression-route FAIL: strict residues `이번엔`, `이번`, `이미`, and `순간` created route/replay scent in a chapter that needed current routine pressure.
- Boundary hygiene FAIL: Ch21 had to own only `조사실 밖의 규칙` as title, preserve Ch20's staying-three strategy, and reserve Ch22 `하나의 사건을 남기는 법`, Ch23 `길어진 문장 아래에서`, and Ch24 `임시 조치의 무게`.
- Continuity FAIL: the chapter needed concrete continuation from Ch20's locked strategy that the three do not share a single signal but each refuses the same prepared administrative slot.
- Mid-pressure FAIL: the outside-room rules needed proof through meal line, cups, door labels, movement permissions, washroom/sleeping routine, staff hesitation, and distinct Aiden/Iris/Rena correction lanes.
- Ending-click FAIL: the ending needed to hand into Ch22's record-preservation pressure without naming or solving Ch22's exact title lane.
- Motif / style FAIL: "rules" language needed to become functional procedure rather than abstract explanation.
- Clarity / canon FAIL: Aiden needed the lead-judgment/body-lag lane, Iris the relation/reaction lane, and Rena the outside-observer/position lane while all three remained tied to one day of administrative pressure.

## Repairs Applied

- Recast the header to title-only `조사실 밖의 규칙`.
- Removed numeric title residue, Arabic digits, backticks, Latin residue, strict route-scent residue, and exact-title body repeats.
- Expanded the chapter above the length floor through procedural outside-room scenes: separated breakfast, cup placement, food-line recording, door labels, corridor crossing, washroom/surface routines, bedding assignment, and night patrol speech.
- Carried Ch20 continuity through `잠정 운영문`, `탑 출구 관련 세 사람`, `분리 배식`, `선행선`, `선행 판단 확인선`, `교차 관찰선`, `시선 교차 금지 구간`, `교차 구간`, `단독 확인 후`, and `공동 반응군`.
- Differentiated Aiden, Iris, and Rena by correction lane: Aiden separates order from judgment and body lag from intent, Iris prevents cups/looks/gestures from becoming relation proof, and Rena refuses to become an outside measuring tool.
- Preserved Ch22 through Ch25 as boundaries and handed only into the next chapter's split-record pressure.
- Reread the full chapter after the edit before final verification.

## Final Target Metrics

- Final title: `조사실 밖의 규칙`
- Body no-space: `6,619`
- Total no-space: `6,626`
- Lines: `1,154`
- Chars: `9,307`
- Backticks: `0`
- Strict hits: `0`
- Own-title hits: `1`
- Own-title body hits: `0`
- Reserved adjacent-title hits: `0`
- Required misses: `0`
- Duplicate non-empty five-line windows: `0`
- Latin residue: `0`
- Numeric residue: `0`
- BOM: `false`
- EOF missing: `false`
- Hash: `32E3BCB925883619F2FE29E0A130680F37BB9B826320A978F62DE3B8FD460124`

## Required Continuity Hits

- `잠정 운영문=3`
- `탑 출구 관련 세 사람=1`
- `분리 배식=2`
- `선행선=1`
- `선행 판단 확인선=1`
- `교차 관찰선=1`
- `시선 교차 금지 구간=2`
- `교차 구간=2`
- `단독 확인 후=1`
- `공동 반응군=2`
- `에이든=24`
- `아이리스=20`
- `레나=25`

## Final No-Edit Five-Cycle Verification

| Cycle | Result | Body no-space | Strict | Required misses | Hash |
|---|---:|---:|---:|---:|---|
| 1 | PASS | 6,619 | 0 | 0 | `32E3BCB925883619F2FE29E0A130680F37BB9B826320A978F62DE3B8FD460124` |
| 2 | PASS | 6,619 | 0 | 0 | `32E3BCB925883619F2FE29E0A130680F37BB9B826320A978F62DE3B8FD460124` |
| 3 | PASS | 6,619 | 0 | 0 | `32E3BCB925883619F2FE29E0A130680F37BB9B826320A978F62DE3B8FD460124` |
| 4 | PASS | 6,619 | 0 | 0 | `32E3BCB925883619F2FE29E0A130680F37BB9B826320A978F62DE3B8FD460124` |
| 5 | PASS | 6,619 | 0 | 0 | `32E3BCB925883619F2FE29E0A130680F37BB9B826320A978F62DE3B8FD460124` |

No edits occurred during or after the five-cycle verification.

## Edge Metrics For Next Handoff

- Ch21 final: title `조사실 밖의 규칙`; body no-space `6,619`; total no-space `6,626`; lines `1,154`; chars `9,307`; backticks `0`; strict hits `0`; own title hits `1`; Latin `0`; digits `0`; hash `32E3BCB925883619F2FE29E0A130680F37BB9B826320A978F62DE3B8FD460124`.
- Ch22 raw: title `272화 하나의 사건을 남기는 법`; body no-space `2,643`; total no-space `2,657`; lines `256`; chars `3,627`; backticks `32`; strict hits `이번엔=1; 이번에는=2; 이번=3; 시간=1; 순간=1`; own title hits `1`; Latin `0`; digits `3`; hash `6E6B2D364105B265DD8D1234315A1416EBF65BD277494CE8737FADB2ACBF3224`.
- Ch23 raw: title `273화 길어진 문장 아래에서`; body no-space `2,651`; total no-space `2,664`; lines `283`; chars `3,625`; backticks `36`; strict hits `이미=1; 순간=1`; own title hits `1`; Latin `0`; digits `8`; hash `7162CE2DD8A933E806305EE6B458044130D9AED483E31D38819AEE9D41031D06`.
- Ch24 raw: title `274화 임시 조치의 무게`; body no-space `2,679`; total no-space `2,690`; lines `268`; chars `3,707`; backticks `12`; strict hits `이번엔=2; 이번=2; 이미=1; 시간=5; 원래=3; 순간=2`; own title hits `1`; Latin `0`; digits `7`; hash `1FAC4232AC9F99652F67BFA5441CA640ED36AD57F00C53E88816DF7CE2C673C0`.
- Ch25 raw lookahead: title `275화 먼저 찢어질 자리`; body no-space `2,991`; total no-space `3,002`; lines `279`; chars `4,089`; backticks `24`; strict hits `이미=6; 시간=3; 순간=1`; own title hits `1`; Latin `0`; digits `7`; hash `7AB723311DD2823FE1FFE218057AABFC384A0E7358C7F33E1B1F1DEFAF906D3A`.

## Handoff To Chapter 22

- `Vol.11 Chapter 22` is now the active incomplete style-harness unit.
- Ch22 should preserve Ch21's locked outside-room routine pressure: food lines, cups, doors, movement permissions, washroom surfaces, bedding, patrol speech, and split small reasons that prevent a single shared signal.
- Ch22 owns `하나의 사건을 남기는 법`: the pressure should turn those split outside-room traces into the problem of preserving the same day as one account without collapsing Aiden, Iris, and Rena into one prepared slot.
- Reserve Ch23 `길어진 문장 아래에서`, Ch24 `임시 조치의 무게`, and Ch25 `먼저 찢어질 자리`.
- Continue to enforce title-only header, no backticks, no strict route-scent residue, no Latin/numeric residue, no exact adjacent-title leakage, length floor `4,800`, full reread after edits, and final no-edit five-cycle verification.
