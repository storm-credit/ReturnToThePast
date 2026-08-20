# Episode Context / State Pipeline v1

Status: **D16.6 PRODUCTION STANDARD — ACTIVE AFTER MERGE**  
Applies: E089–E375 신규 생산 + E001–E088 재검수 시 JIT overlay  
Authority: production routing only; Canon/Architecture/Manuscript가 상위

## 1. Single Production Loop

```text
PREVIOUS EXIT
  ↓
ACT / VOLUME / SUBACT
  ↓
D6 EPISODE CARD
  ↓
JIT CONTEXT PACK
  ↓
VISUAL + CHARACTER + INSTITUTION CURRENT STATE
  ↓
CRAFT / POV / INFORMATION CEILING
  ↓
MANUSCRIPT
  ↓
QA / AUTHOR REVIEW
  ↓
STATE MUTATION
  ↓
NEXT ENTRY
```

새 회차가 이 순서를 건너뛰면 production FAIL이다.

## 2. Input Resolution

Episode ID를 받으면 먼저 D16.5 Wiring Registry에서 유일한 계층을 찾는다.

필수:

- Grand Act
- Volume
- Subact
- D6 Registry row
- Scene-Ready Design
- active amendment/overlay
- previous Exit source

그 후에만 Character/Relic/Beast/Landmark/Faction state를 호출한다.

## 3. Previous Exit Source

우선순위:

1. 직전 회차의 current State Mutation
2. current grouped State Mutation의 해당 episode row/exit
3. actual manuscript exit + next CP carryover
4. State Ledger / active checkpoint

과거 회차에 독립 State Mutation 파일이 없다고 새 사건을 추론하지 않는다.

Backfill은 반드시 3번 이상의 실제 source를 가리킨다.

## 4. JIT Context Pack Schema

```text
EPISODE_ID
TITLE
GRAND_ACT
VOLUME
SUBACT
ARCHITECTURE_HUB
D6_CARD
PREVIOUS_EXIT_SOURCE
ENTRY_STATE
POV
INFORMATION_CEILING
GOAL
OPPOSITION
CHOICE
COST
STATE_CHANGE_TARGET
HOOK
SCENE_ASSETS
PRIMARY_VISUAL_ASSET
CURRENT_VISUAL_STATE
SECONDARY_ECHO
DO_NOT_REEXPLAIN
DO_NOT_ADVANCE
ACTIVE_CLOCKS
MYSTERY_CEILING
LOSS_LOCKS
CRAFT_ROUTE
NEXT_CAUSE_BOUNDARY
```

### JIT Context Minimality

현재 회차에 필요 없는 세계관 설명은 넣지 않는다.

- 장면에 없는 Character를 넣지 않는다.
- 미래 Variant를 넣지 않는다.
- 이미 확정된 설정을 설명용으로 중복 복사하지 않는다.
- 큰 Bible 전체를 CP에 붙이지 않는다.
- CP는 ‘현재 장면에 필요한 정본 포인터 + 현재 상태’만 보유한다.

## 5. Context Pack Granularity

### Future default

E089 이후는 **회차별 JIT Context**를 기본으로 한다.

단, 같은 Subact에서 2–6화가 매우 강하게 결속되어 있고 공통 배경이 큰 경우 묶음 master CP를 만들 수 있다. 그 경우에도 실제 집필 직전 회차별 JIT header/overlay가 다음을 분리해야 한다.

- Episode ID
- Previous Exit
- exact POV
- exact clocks
- exact current asset state
- exact Do Not Advance

### Historical compatibility

E001–E088의 기존 individual/group CP는 provenance로 유지한다. 포맷 통일만을 위해 재작성하지 않는다.

## 6. State Mutation Schema

```text
EPISODE
SOURCE_MANUSCRIPT
STATUS
TIMELINE_STATE
CHARACTER_MUTATIONS
RELATIONSHIP_MUTATIONS
INSTITUTION_FACTION_MUTATIONS
ASSET_MUTATIONS
LOCATION_MUTATIONS
MYSTERY_INFORMATION_MUTATIONS
PERMANENT_LOSS_OR_IRREVERSIBLE_CHOICE
CLOCK_MOVEMENT
UNCHANGED_CRITICAL_LOCKS
NEXT_ENTRY_HANDOFF
HUMAN_PROSE_STATUS
```

### Only Mutations

State Mutation은 ‘현재 세계 전체 상태’를 복제하는 문서가 아니다.

- 바뀐 것만 기록
- 중요한 불변 lock은 필요한 경우에만 `UNCHANGED_CRITICAL_LOCKS`에 짧게 기록
- 다음 CP가 필요하면 상위 ledger와 합성

## 7. Handoff Invariant

Episode N의 Exit와 Episode N+1의 Entry는 다음 관계여야 한다.

```text
Entry(N+1) = Exit(N) + allowed offscreen transition + explicitly locked time/location movement
```

FAIL:

- 설명 없는 관계 복구
- 소유권 순간 복귀
- 손상/사망/영구손실 리셋
- 이전 화에서 없던 정보가 POV 지식으로 자동 진입
- 현재/과거 법적 상태가 이유 없이 뒤집힘
- Graph link만으로 등장 허가

## 8. Boundary Rule

한 Context/State group이 Subact 경계를 가로지를 수는 있지만, current router는 Episode 단위 소속을 우선한다.

현재 historical exceptions:

- `E063-E069`: E063–E068 = 3C, E069 = 3D
- `E082-E088`: E082–E087 = 4B, E088 = 4C

향후 신규 묶음 CP는 가능하면 Subact 경계를 넘지 않는다.

## 9. Visual Binding

JIT CP는 `visual-cp-resolver-rules-v1.md`를 통해 다음을 확정한다.

- Primary Asset 1
- Secondary Echo 0–2
- Current State
- 3-Second Anchor
- Do Not Re-explain
- Do Not Advance
- Collision target
- Production Prompt Route if actual art is needed

비주얼 자산이 서사 자산보다 먼저 선택되면 FAIL.

## 10. Obsidian Node/Edge

권장 edge:

```text
Episode → Subact
Episode → Previous State
Episode → JIT Context
Episode → Primary Asset
JIT Context → Visual Resolver
State Mutation → Next Episode
```

Backlinks로 역탐색한다. 의미 없는 양방향 중복링크를 넣지 않는다.

## 11. Existing E001–E088 Policy

기존 88화는 다음 조건이면 GREEN 유지한다.

- 원고 존재
- CP coverage 존재
- state/next-entry handoff 기능
- current Subact와 해석 가능
- blocking Canon conflict 없음

D16.5 새 필드가 과거 CP 본문에 직접 없다는 이유만으로 YELLOW/RED로 만들지 않는다. **재사용·재검수 시 JIT overlay로 최신 필드를 주입**한다.

## 12. Future Empty-File Ban

다음은 금지한다.

- E090–E375 empty Context Pack batch creation
- E090–E375 empty State Mutation batch creation
- 빈 파일을 `READY`로 표시
- 아직 집필되지 않은 사건의 Exit State 선결정

Architecture는 미리 설계하고, Context/State는 실제 생산 직전에 컴파일한다.

## 13. Human Prose

Pipeline PASS ≠ HUMAN PROSE PASS.

원고가 main에 있어도 최종 문체 승인이 아님. AI는 `FIRST DRAFT / AUTHOR REVIEW / AUTHOR REVIEW READY`까지만 기록한다.

**D16.6 Episode Context / State Pipeline: READY FOR JIT USE.**
