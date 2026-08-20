# Deep Context Pack Production Standard v1

Status: ACTIVE WORKING STANDARD — FULL SERIES STATIC PACK + JIT RUNTIME OVERLAY
Date: 2026-08-20
Scope: E001–E375

## 1. 목적

Grand Act / Volume / Subact / D6 Episode Card가 이미 완성된 상태에서, 각 회차를 실제 집필 가능한 입력으로 깊게 컴파일한다.

핵심은 Context를 2층으로 분리하는 것이다.

```text
STATIC DEEP CONTEXT PACK
  = 미리 확정 가능한 서사·인물·제도·미스터리·자산·금지·다음 인과

JIT RUNTIME STATE OVERLAY
  = 직전 실제 원고 Exit에서만 확정 가능한 현재값
```

따라서 E090–E375도 '빈 파일'로 만들지 않고, 이미 설계된 Architecture를 근거로 Static Deep Context는 미리 만들 수 있다. 다만 실제 이전 화 결과를 선결정하지 않는다.

## 2. Static Deep Context 필수 필드

각 Episode Entry는 최소 다음을 가진다.

1. Episode ID / Title source / GA / Volume / Subact / Arc
2. Authority pointers
3. D6 Goal / Opposition / Choice / Cost / Planned State Change / Hook
4. Entry assumptions — architecture-level only
5. Timeline / age / calendar ceiling
6. Location / movement / logistics constraints
7. POV / P1·P2·P3 allocation / knowledge ceiling
8. Character current design-state and independent agenda
9. Relationship state and prohibited automatic reconciliation
10. Institution / faction active functions and opposition benefit
11. Active systems — allowed facts / forbidden reveals
12. Mystery / MacGuffin active rung / false interpretation / reveal ceiling
13. Relic / beast / landmark / faction assets and ownership/contract/custody state
14. Permanent loss / irreversible choice locks
15. Active clocks and which may move in this episode
16. Scene density / craft route / anti-repeat
17. Primary visual anchor / secondary echoes / Do-Not-Advance
18. Required planned state-change target
19. Next Cause Boundary
20. State Mutation plan — what categories must be checked after drafting
21. Obsidian node/edge pointers
22. Known stale-source overrides / unresolved gaps

## 3. Deepness model — source-bound, not Bible-copy

Deep Pack의 깊이는 파일 글자수로 판정하지 않는다.

`SOURCE-BOUND DEEP`가 되려면 해당 Episode가 다음을 **유일하게 resolve**할 수 있어야 한다.

```text
Subact Hub
+ Volume Scene-Ready Design
+ exact D6 Episode row
+ active POV allocation
+ Chronology
+ Character/Relationship state
+ Institution/Faction rules
+ Mystery ladder/Errata
+ Asset/Loss state
+ Visual resolver
```

규칙:
- 위 소스의 긴 내용을 Deep Pack에 다시 복사해 drift를 만드는 것은 금지한다.
- 대신 draft 직전 resolver가 22개 필드를 실제 값으로 materialize해야 한다.
- source pointer만 있고 소스가 없거나, 어느 값을 읽어야 할지 모호하면 COMPLETE가 아니다.
- D12 E089–E093처럼 이미 충분히 컴파일된 Historical/Current CP가 있으면 Deep Master는 그것을 provenance/active support로 함께 읽을 수 있다.

## 4. Unresolved source gap rule

상위 Hub/Scene-Ready/Domain Bible에 `[설계 미정]`이 있으면 Deep Pack이 임의로 채우지 않는다.

분류:
- `GAP-NB` non-blocking: 정확한 지명·분 단위 거리·부차 이름처럼 현재 Episode의 선택/인과/정보상한을 바꾸지 않는 값. Pack에 gap으로 남기고 JIT에서 필요할 때만 ruling.
- `GAP-B` blocking: POV 주체, 핵심 선택, 인물 정체, 필수 이동 가능성, 법적 권한, Mystery reveal 시점처럼 실제 장면을 쓰려면 확정이 필요한 값. 해당 Episode JIT Preflight에서 STOP.

중요:
- Static Pack coverage는 gap 존재와 별개로 만들 수 있다.
- `STATIC COMPLETE`는 빈칸을 숨겼다는 뜻이 아니라 **빈칸의 위치와 권한을 안전하게 보존했다**는 뜻이다.
- Manuscript READY는 GAP-B가 0일 때만 가능하다.

## 5. JIT Runtime Overlay 필드

실제 집필 직전에만 채운다.

- PREVIOUS_EXIT_SOURCE
- exact Entry State after prior manuscript
- current wounds / missing persons / possession / custody
- exact clock values if manuscript-dependent
- exact institution permissions in force
- current relationship deltas
- current evidence copies / destroyed originals
- unresolved offscreen transition explicitly allowed by architecture

금지:
- 직전 화가 아직 쓰이지 않았는데 실제 Exit를 확정
- 미래 손실을 현재 상태처럼 기록
- Static Pack의 목표를 실제 사건 완료 상태로 오인

## 6. Pack grouping

파일 단위는 Subact Master를 기본으로 한다.

- 60 Subacts = 60 Deep Context Masters
- 각 Master 내부에 해당 Episode의 독립 routing entry를 둔다.
- 각 entry는 공통 22-field materialization contract를 상속한다.
- Episode별 실제 집필 시 JIT Runtime Overlay는 별도 episode file 또는 header로 생성한다.

이 방식은 375개의 중복 Bible 복사를 피하면서도 E001–E375 전체를 사전 컴파일한다.

## 7. Authority rule

Deep Pack은 Canon이 아니다.

충돌 우선순위:
Author → Canon Constitution → Amendment/Errata → Decision Log → State Ledger → Domain Bible → Story Architecture → Active Deep Context → Historical Context → Manuscript provenance.

Deep Pack이 상위 정본과 충돌하면 Pack을 고친다. 사건을 Pack에 맞춰 바꾸지 않는다.

과거 Subact Hub의 `Context Pack 없음` 문구는 새 Full-Series Deep Master 생성 이후 **routing/index staleness**로 취급한다. 사건/정본 부재를 뜻하지 않는다.

## 8. Pack completeness gate

각 Episode Entry는 다음 Gate를 모두 통과해야 STATIC COMPLETE다.

- G1 Architecture ownership unique
- G2 Previous/Next causal boundaries identifiable
- G3 POV/knowledge ceiling resolvable
- G4 Character agency resolvable
- G5 Institution opposition benefit resolvable where relevant
- G6 Mystery reveal ceiling resolvable
- G7 Asset ownership/contract/custody state resolvable where relevant
- G8 Loss/irreversibility lock resolvable
- G9 Visual current-state ceiling resolvable
- G10 Anti-repeat/craft route resolvable
- G11 Runtime-only fields not prematurely frozen
- G12 Obsidian routing valid
- G13 Deep source bundle exists and is unambiguous
- G14 `[설계 미정]` is surfaced as GAP-NB/GAP-B rather than invented

## 9. Production order

```text
375 Static Deep Entries complete
→ Hostile Blindspot QA
→ fix S0/S1
→ main merge
→ actual episode JIT Runtime Overlay
→ resolve GAP-B if any
→ draft/review
→ State Mutation
```

HUMAN PROSE PASS는 이 표준의 범위 밖이며 작가 승인 전 부여하지 않는다.
