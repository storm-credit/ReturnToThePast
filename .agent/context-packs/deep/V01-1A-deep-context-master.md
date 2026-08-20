---
node_type: deep_context_master
node_id: DCP-V01-1A
parent_act: GA-I
parent_volume: V01
parent_subact: V01-1A
episode_start: E001
episode_end: E006
status: STATIC DEEP CONTEXT / SOURCE-BOUND COMPLETE
runtime_state: JIT_ONLY
---

# V01-1A — Static Deep Context Master

> 이미 확정된 Act/Volume/Subact/D6를 집필 입력으로 깊게 컴파일한다. 이 Pack은 Canon이 아니며, 아직 쓰이지 않은 회차의 실제 Exit·부상·소유권·정확한 Clock 값을 선결정하지 않는다.

## 1. Deep source bundle
- Subact Hub: `docs/10_story_architecture/subacts/V01-1A.md`
- Volume Scene-Ready: `docs/10_story_architecture/detail/v01-scene-ready-design-v1.md`
- D6 Registry: `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md`
- Chronology: `docs/01_timeline/master-chronology-and-aging-ledger-v1.md`
- Character: `docs/05_characters/character-state-checkpoints-v1.md`
- POV: `secondary-pov-and-offscreen-action-allocation-v1.md` + `d15-pov-allocation-supplement-v1.md`
- Mystery: `docs/11_mystery/mystery-reinforcement-ladder-v1.md` + active Errata
- Assets/Loss: `docs/09_collection/asset-state-checkpoints-v1.md` + `docs/12_losses/permanent-loss-lock-v1.md`
- Visual: `visual-cp-resolver-rules-v1.md` + `visual-asset-act-usage-matrix-v1.md`
- Contract: `deep-context-pack-production-standard-v1.md`

## 2. Shared static deep context
- Ownership: `GA-I → V01 → V01-1A → E001–E006`.
- Goal/Entry/Exit/Active Agendas/Mystery/Locations/Cast/Institutions/Assets는 **Subact Hub 현재값**을 상속한다.
- 각 화 Goal/Opposition/Choice/Cost/Planned State Change/Hook/Next Cause는 **정확한 D6 row**를 상속한다.
- Timeline은 Master Chronology, POV는 active allocation이 historical CP/manuscript metadata보다 우선한다.
- Supporting cast 독립성, 제도의 실제 효용·비용, 법적 권한/물리능력 구분을 보존한다.
- Mystery는 false interpretation과 reveal ceiling을 구분하며 단일 증거/B05/기록 1장을 truth judge로 사용하지 않는다.
- Relic/Beast는 custody·contract·ownership·파괴/분산 상태를 리셋하지 않는다. loot/pet/final-upgrade 금지.
- Visual은 scene-present 자산만 현재 Variant로 호출하고 미래 Variant/C30 정체 확정을 선행하지 않는다.
- Planned State Change는 **계획**이다. 실제 달성은 원고 QA 후 State Mutation만 확정한다.

## 3. Episode ownership / causal routing
| EP | Exact D6 source | Previous Exit input | Next boundary | Active override / regression lock |
|---|---|---|---|---|
| E001 | `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md#E001` | SERIES ENTRY | E002 | — |
| E002 | `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md#E002` | E001 actual Exit/JIT | E003 | — |
| E003 | `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md#E003` | E002 actual Exit/JIT | E004 | E003 단서 이미 공개; E033 재-첫공개 금지 |
| E004 | `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md#E004` | E003 actual Exit/JIT | E005 | — |
| E005 | `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md#E005` | E004 actual Exit/JIT | E006 | — |
| E006 | `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md#E006` | E005 actual Exit/JIT | E007 | J01: F0 CY664 장야월21일 → N0 CY640 안개월4일 |

## 4. Episode Deep Entry materialization contract
위 표의 **각 Episode row는 아래 22필드를 모두 가진다.** 값은 바로 위 Deep Source Bundle에서 resolve하며, 큰 Bible 문장을 복제하지 않는다.

1. Episode ID / working title source / GA / Volume / Subact / Arc
2. Authority pointers
3. D6 Goal / Opposition / Choice / Cost / Planned State Change / Hook
4. architecture-level Entry assumptions
5. timeline / age / calendar ceiling
6. location / movement / logistics
7. POV / P1·P2·P3 / knowledge ceiling
8. character current state / independent agenda
9. relationship state / no automatic reconciliation
10. institution/faction function + opposition benefit
11. systems allowed facts / forbidden reveals
12. mystery rung / false interpretation / reveal ceiling
13. relic/beast/landmark/faction asset + ownership/contract/custody
14. permanent loss / irreversible choice locks
15. active clocks allowed to move
16. scene density / craft route / anti-repeat
17. Primary Visual Anchor / Secondary Echo≤2 / Current State / Do-Not-Advance
18. required **planned** state-change target
19. exact Next Cause Boundary
20. post-draft State Mutation checklist
21. Obsidian edges: `Episode → DCP-V01-1A → V01-1A → V01 → GA-I`
22. known stale-source override / unresolved gap

Drafting agent must materialize these 22 fields before prose. Source pointer를 읽지 않은 상태로 빈칸을 추측하면 FAIL.

## 5. JIT Runtime Overlay — deliberately unfrozen
집필 직전에만 채운다:
- PREVIOUS_EXIT_SOURCE / exact Entry State
- wounds / missing persons / possession & custody / relationship delta
- exact institution permissions / exact clock values
- surviving/destroyed evidence copies
- explicitly allowed offscreen transition

## 6. Completion gate
- Coverage: **E001–E006 / 6 episodes**
- G1–G12 required.
- Static pack cannot grant HUMAN PROSE PASS.
