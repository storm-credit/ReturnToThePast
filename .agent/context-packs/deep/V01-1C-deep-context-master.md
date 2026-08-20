---
node_type: deep_context_master
node_id: DCP-V01-1C
parent_act: GA-I
parent_volume: V01
parent_subact: V01-1C
episode_start: E013
episode_end: E018
status: STATIC DEEP CONTEXT / SOURCE-BOUND COMPLETE
runtime_state: JIT_ONLY
---

# V01-1C — Static Deep Context Master

> 이미 확정된 Act/Volume/Subact/D6를 집필 입력으로 깊게 컴파일한다. 실제 직전 화 결과는 JIT Runtime Overlay에서만 채운다.

## 1. Deep source bundle
- Subact Hub: `docs/10_story_architecture/subacts/V01-1C.md`
- Volume Scene-Ready: `docs/10_story_architecture/detail/v01-scene-ready-design-v1.md`
- D6 Registry: `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md`
- Chronology / Character / POV / Mystery / Assets-Loss / Visual / Production Standard: active master sources.

## 2. Shared static deep context
- Ownership: `GA-I → V01 → V01-1C → E013–E018`.
- Subact Hub의 Goal/Entry/Exit/Active Agendas/Mystery/Locations/Cast/Institutions/Assets와 각 D6 row의 Goal/Opposition/Choice/Cost/Planned State Change/Hook/Next Cause를 상속한다.
- Chronology·POV·Mystery·asset custody·permanent loss·visual current state의 후대 active source가 historical CP보다 우선한다.
- supporting cast agency / institution benefit / system reveal ceiling / anti-repeat를 보존한다.
- Planned State Change는 완료사실이 아니며 actual state는 draft QA 후 State Mutation으로만 승격한다.

## 3. Episode ownership / causal routing
| EP | Exact D6 source | Previous Exit input | Next boundary | Override |
|---|---|---|---|---|
| E013 | `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md#E013` | E012 actual Exit/JIT | E014 | — |
| E014 | `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md#E014` | E013 actual Exit/JIT | E015 | — |
| E015 | `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md#E015` | E014 actual Exit/JIT | E016 | — |
| E016 | `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md#E016` | E015 actual Exit/JIT | E017 | active POV allocation을 materialize하고 historical Aiden-only metadata를 자동신뢰하지 않는다 |
| E017 | `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md#E017` | E016 actual Exit/JIT | E018 | — |
| E018 | `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md#E018` | E017 actual Exit/JIT | E019 | — |

## 4. Episode Deep Entry contract
각 row는 22개 필드(ID/title hierarchy, authority, D6 G/O/C/C/state/hook, entry, timeline/logistics, POV/knowledge, character/relationship, institution/system, mystery, assets/loss, clocks, density/craft, visual, planned state target, next cause, mutation plan, Obsidian, override)를 source-bound로 가진다. Draft 전 resolver가 값을 materialize하지 못하면 FAIL.

## 5. Runtime-only
Previous Exit의 exact state, wounds, custody, relationship delta, exact clocks/permissions, evidence survival은 집필 직전에만 채운다.

## 6. Completion gate
- Coverage: **E013–E018 / 6 episodes**
- G1–G12 required. HUMAN PROSE PASS는 별도다.
