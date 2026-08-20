---
node_type: deep_context_master
node_id: DCP-V01-1D
parent_act: GA-I
parent_volume: V01
parent_subact: V01-1D
episode_start: E019
episode_end: E025
status: STATIC DEEP CONTEXT / SOURCE-BOUND COMPLETE
runtime_state: JIT_ONLY
---

# V01-1D — Static Deep Context Master

> 이미 확정된 Act/Volume/Subact/D6를 집필 입력으로 깊게 컴파일한다. 실제 직전 화 결과는 JIT Runtime Overlay에서만 채운다.

## 1. Deep source bundle
- Subact Hub: `docs/10_story_architecture/subacts/V01-1D.md`
- Volume Scene-Ready: `docs/10_story_architecture/detail/v01-scene-ready-design-v1.md`
- D6 Registry: `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md`
- Active chronology / character checkpoints / POV / mystery / asset-state / permanent-loss / visual resolver / production standard.

## 2. Shared static deep context
- Ownership: `GA-I → V01 → V01-1D → E019–E025`.
- Subact Hub의 Entry/Exit/active agendas와 D6 row의 episode causality를 상속한다.
- 세렌 바일 E023 영구사망을 후속 상태에서 되돌리지 않는다. R03은 전리품/강화무기가 아니라 증거·부채·소유권 분쟁 상태를 유지한다.
- F1 귀환 이후 관계/기억 변화는 actual state/ledger를 통해서만 확정하며, 미래 손실을 앞당기지 않는다.
- 제도·왕실·성당의 실제 기능을 평면악역화하지 않고, 아이리스 독립성과 귀환거부/현지생존 선택을 주인공 보조행동으로 축소하지 않는다.

## 3. Episode ownership / causal routing
| EP | Exact D6 source | Previous Exit input | Next boundary | Override |
|---|---|---|---|---|
| E019 | `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md#E019` | E018 actual Exit/JIT | E020 | — |
| E020 | `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md#E020` | E019 actual Exit/JIT | E021 | — |
| E021 | `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md#E021` | E020 actual Exit/JIT | E022 | — |
| E022 | `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md#E022` | E021 actual Exit/JIT | E023 | — |
| E023 | `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md#E023` | E022 actual Exit/JIT | E024 | C06 세렌 바일 permanent death lock |
| E024 | `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md#E024` | E023 actual Exit/JIT | E025 | — |
| E025 | `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md#E025` | E024 actual Exit/JIT | E026 | F1 귀환/관계소거는 actual state source와 합성 |

## 4. Episode Deep Entry contract
각 row는 22개 필드(ID/title hierarchy, authority, D6 G/O/C/C/state/hook, entry, timeline/logistics, POV/knowledge, character/relationship, institution/system, mystery, assets/loss, clocks, density/craft, visual, planned state target, next cause, mutation plan, Obsidian, override)를 source-bound로 가진다. Draft 전 resolver materialization 필수.

## 5. Runtime-only
Previous Exit의 exact state, wounds, custody, relationship delta, exact clocks/permissions, evidence survival은 집필 직전에만 채운다.

## 6. Completion gate
- Coverage: **E019–E025 / 7 episodes**
- G1–G12 required. HUMAN PROSE PASS는 별도다.
