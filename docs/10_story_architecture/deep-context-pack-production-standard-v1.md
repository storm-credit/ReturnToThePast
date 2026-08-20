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

1. Episode ID / Title / GA / Volume / Subact / Arc
2. Authority pointers
3. D6 Goal / Opposition / Choice / Cost / State Change / Hook
4. Entry assumptions — architecture-level only
5. Timeline / age / calendar ceiling
6. Location / movement / logistics constraints
7. POV / P1·P2·P3 allocation / knowledge ceiling
8. Character current design-state and independent agenda
9. Relationship state and prohibited automatic reconciliation
10. Institution / faction active functions and opposition benefit
11. Active systems — allowed facts / forbidden reveals
12. Mystery / MacGuffin active rung / false interpretation / reveal ceiling
13. Relic / beast / landmark / faction assets and ownership/contract state
14. Permanent loss / irreversible choice locks
15. Active clocks and which may move in this episode
16. Scene density / craft route / anti-repeat
17. Primary visual anchor / secondary echoes / Do-Not-Advance
18. Required state-change target
19. Next Cause Boundary
20. State Mutation plan — what categories must be checked after drafting
21. Obsidian node/edge pointers
22. Known stale-source overrides / unresolved gaps

## 3. JIT Runtime Overlay 필드

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

## 4. Pack grouping

파일 단위는 Subact Master를 기본으로 한다.

- 60 Subacts = 60 Deep Context Masters
- 각 Master 내부에 해당 Episode의 독립 Deep Entry를 둔다.
- Episode별 실제 집필 시 JIT Runtime Overlay는 별도 episode file 또는 header로 생성한다.

이 방식은 375개의 중복 Bible 복사를 피하면서도 375 Episode Entry를 모두 사전 컴파일한다.

## 5. Authority rule

Deep Pack은 Canon이 아니다.

충돌 우선순위:
Author → Canon Constitution → Amendment/Errata → Decision Log → State Ledger → Domain Bible → Story Architecture → Active Deep Context → Historical Context → Manuscript provenance.

Deep Pack이 상위 정본과 충돌하면 Pack을 고친다. 사건을 Pack에 맞춰 바꾸지 않는다.

## 6. Pack completeness gate

각 Episode Entry는 다음 12 Gate를 모두 통과해야 COMPLETE다.

- G1 Architecture ownership unique
- G2 Previous/Next causal boundaries identifiable
- G3 POV/knowledge ceiling explicit
- G4 Character agency explicit
- G5 Institution opposition benefit explicit where relevant
- G6 Mystery reveal ceiling explicit
- G7 Asset ownership/contract state explicit where relevant
- G8 Loss/irreversibility lock explicit
- G9 Visual current-state ceiling explicit
- G10 Anti-repeat/craft route explicit
- G11 Runtime-only fields not prematurely frozen
- G12 Obsidian routing valid

## 7. Production order

```text
375 Static Deep Entries complete
→ Hostile Blindspot QA
→ fix S0/S1
→ main merge
→ actual episode JIT Runtime Overlay
→ draft/review
→ State Mutation
```

HUMAN PROSE PASS는 이 표준의 범위 밖이며 작가 승인 전 부여하지 않는다.
