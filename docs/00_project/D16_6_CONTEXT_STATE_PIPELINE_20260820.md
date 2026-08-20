# D16.6 Production Context & State Pipeline — 2026-08-20

Status: **D16.6 ACTIVE / BACKFILL + JIT PRODUCTION STANDARD**  
Base: `main@e44be6d11cc5f802fdc42df2af29eba3ce22def4`  
Scope: E001–E088 existing-production backfill audit + E089–E375 future JIT Context/State production  
Non-Scope: 사건·설정·결말·인물의도 변경, E001–E088 원고 전면 재작성, E090–E375 빈 Context 파일 선생성

## 1. 결정

이 프로젝트의 회차 생산은 다음 원칙으로 고정한다.

> **전체 375화 설계/연결은 미리 완성하되, 전체 375화의 빈 Context Pack을 미리 만들지 않는다. 실제 Context와 상태는 집필 직전에 JIT로 만들고, 회차가 끝날 때 실제로 변한 상태만 기록해 다음 회차 Entry State로 넘긴다.**

현재 저장소는 이미:

- 5 Grand Acts = 5/5
- 15 Volumes = 15/15
- 60 Subacts = 60/60
- E001–E375 D6 cards = 375/375
- D16.5 Act/Volume/Subact/Obsidian wiring = COMPLETE
- main manuscript = E001–E088

상태이므로, E001부터 다시 설계하거나 E090–E375 빈 CP를 생성하지 않는다.

## 2. Canon / Production Authority

Context Pack과 State Mutation은 정본을 대신하지 않는다.

충돌 시 우선순위:

1. Author decision
2. Canon Constitution
3. active Amendment / Errata
4. Decision Log
5. State Ledger
6. Domain Bible
7. Story Architecture / D6 card / active overlay
8. actual accepted manuscript
9. Context Pack / Craft Manifest / production state artifact
10. Graph / Prompt metadata

Backfill 문서는 과거 사건을 새로 정의하는 문서가 아니다. **이미 main에 존재하는 원고와 다음 회차가 실제로 승계한 사실을 구조화**하는 문서다.

## 3. Standard Production Chain

E089 이후 신규 회차는 아래 순서를 강제한다.

`Previous Episode Exit State`
→ `Grand Act`
→ `Volume`
→ `Subact`
→ `D6 Episode Card`
→ `JIT Context Pack`
→ `Visual CP Resolver / current asset state`
→ `Craft / POV / Information Ceiling`
→ `Manuscript Draft`
→ `Canon / Continuity / Reader / Human-Prose Audit`
→ `State Mutation`
→ `Next Episode Entry State`

### Hard Stop

다음 중 하나라도 불명확하면 원고 생산을 멈춘다.

- Episode가 어느 Subact에 속하는지 불명확
- 직전 회차 Exit와 현재 Entry가 충돌
- 현재 시점 Character/Relic/Beast/Institution 상태가 서로 다른 문서에서 충돌
- 미래 Variant가 현재 상태로 선행 노출
- permanent loss / death / ownership state가 역행
- POV / information ceiling이 active lock과 충돌

## 4. Context Pack JIT Rule

### 만들 때

- 실제 다음 회차를 집필하거나 재검수하기 직전
- 최신 main freshness를 확인한 뒤
- 필요한 범위만 컴파일

### 만들지 않을 때

- E090–E375를 빈 템플릿 파일로 미리 생성하지 않는다.
- ‘나중에 필요할 수 있다’는 이유만으로 수백 개 CP를 만들지 않는다.
- 이미 기능하는 과거 CP를 포맷 통일만 위해 재작성하지 않는다.

### Mandatory JIT CP Fields

- Episode ID / title
- Grand Act / Volume / Subact
- Architecture Hub / D6 card source
- Previous Exit State source
- Entry State
- POV / information ceiling
- Goal / Opposition / Choice / Cost / State Change / Hook
- Scene assets actually present
- Primary Visual Asset
- Current Visual State
- Secondary Echo 0–2
- Do Not Re-explain
- Do Not Advance
- Mystery / Loss / Institution / Clock state if active
- Craft Manifest route if required
- Next-cause boundary

## 5. State Mutation Rule

State Mutation에는 **실제로 바뀐 것만** 기록한다.

기본 범주:

- Timeline / Era / address state
- Character state / relationship / knowledge
- Institution / faction / legal state
- Relic ownership / damage / availability
- Beast contract / location / trace if changed
- Location / landmark state
- Mystery reveal ceiling
- Permanent loss / irreversible choice
- Clock progress
- Next Episode Entry handoff

변하지 않은 설정을 매 화 복사하지 않는다. 필요하면 상위 State Ledger를 참조한다.

## 6. Historical Backfill Rule — E001–E088

E001–E088은 이미 main 원고가 있으므로 재집필이 아니라 **production-chain backfill audit** 대상이다.

각 회차는 다음 7개를 검사한다.

1. actual manuscript exists
2. Context Pack coverage exists
3. current Grand Act / Volume / Subact mapping
4. State Mutation 또는 동등한 Exit-state source
5. 다음 회차 Entry / Carryover 연결
6. D16.5 current routing compatibility
7. current Canon/Architecture와 blocking conflict 여부

### Verdict

- **GREEN** — 현재 생산선에서 그대로 사용 가능
- **YELLOW** — 내용은 기능하지만 형식/라우팅/독립 state artifact가 최신 표준과 다름. overlay/backfill로 해결
- **RED** — 실제 원고/상태가 current Canon/Architecture와 충돌. 원고 수정 검토 필요

GREEN을 새 포맷으로 다시 쓰지 않는다.

## 7. E001–E088 Audit Summary

현재 전수 구조검사 결과:

- Manuscript coverage: **88/88**
- Context Pack coverage: **88/88**
- Context Pack gap: **0**
- State handoff functional coverage: **88/88**
- independent historical State Mutation artifact missing before backfill: **E001 / E003 / E024 = 3**
- verified broken handoff: **0**
- verified RED content conflict: **0 at D16.6 structural audit stage**

E001 / E003 / E024는 다음 CP가 이전 회차 Carryover를 명시적으로 보존하고 있어 인과가 끊긴 상태가 아니다. D16.6에서 derived backfill state file을 추가해 구조를 닫는다.

## 8. Historical Group-Pack Boundary Exceptions

과거 지원팩 중 2개는 Subact 경계를 가로지른다.

### E063–E069

- E063–E068 = V03 / 3C
- E069 = V03 / 3D
- 기존 `E063-E069-context-pack.md`와 동일 범위 state mutation은 역사적 지원팩으로 유지
- current routing은 D16.5를 우선해 E069를 3D로 해석

### E082–E088

- E082–E087 = V04 / 4B
- E088 = V04 / 4C
- 기존 파일 자체가 `4B + 4C 진입 E088`을 명시
- current routing은 E088을 4C로 해석

파일을 억지로 분할해 provenance를 깨지 않는다. D16.6 Boundary Overlay가 정확한 소속을 고정한다.

## 9. E088 → E089 Gate

E089은 빈 상태에서 시작하지 않는다.

직전 상태:

- `manuscript/quality/E082-E088-state-mutation.md`
- actual E088 manuscript

현재 CP:

- `.agent/context-packs/episodes/E089-E093-context-pack-d12.md`
- D12 Craft Manifest
- D12 Preflight
- D16.5 wiring / resolver

E089–E093 D12 CP의 오래된 header `MANUSCRIPT BLOCKED`는 당시 컴파일 시점 상태다. 이후 Craft/Continuity gate가 완료되었으므로 현재 operational authority는 최신 `GATE_STATUS.md`, `D15_PRODUCTION_GATE_OVERRIDE_20260820.md`, `manuscript/PROGRESS.md`를 따른다.

따라서 E089은 **AUTHOR-REVIEW DRAFT 생산 가능**, HUMAN PROSE 최종승인은 아님.

## 10. Obsidian Graph Contract

향후 graph edge는 생산 순서를 반영한다.

`E088 → E088 Exit State → V04-4C → E089 JIT CP → E089 → E089 State Mutation → E090`

권장 property:

```yaml
node_type: episode|context|state
node_id: E089|CP-E089|STATE-E089
parent_act: GA-II
parent_volume: V04
parent_subact: V04-4C
previous_state: STATE-E088
next_episode: E090
```

미집필 Episode node 375개를 미리 만들지 않는다.

## 11. Human Prose Separation

이 파이프라인의 GREEN/PASS는 **구조·연속성·생산 가능성 판정**이다.

다음을 의미하지 않는다.

- 원고 문장이 완벽함
- 낭독감이 최종임
- HUMAN PROSE PASS 부여됨

최종 HUMAN PROSE PASS는 작가만 승인한다.

## 12. Final Operational Rule

앞으로 신규 회차는 항상:

> **직전 실제 상태를 읽고 → 현재 회차 Context를 JIT로 만들고 → 원고를 쓰고 → 실제 변화만 State Mutation에 기록하고 → 그 상태를 다음 회차에 넘긴다.**

D16.6은 이 흐름을 E001–E088의 기존 생산유산과 E089–E375의 미래 생산선 사이에서 하나의 규칙으로 통합한다.
