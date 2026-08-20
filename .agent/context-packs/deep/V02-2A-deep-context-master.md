---
node_type: deep_context_master
node_id: DCP-V02-2A
parent_act: GA-I
parent_volume: V02
parent_subact: V02-2A
episode_start: E026
episode_end: E031
status: STATIC DEEP CONTEXT / SOURCE-BOUND COMPLETE
runtime_state: JIT_ONLY
---
# V02-2A — Static Deep Context Master
> 이미 확정된 Architecture를 집필 입력으로 컴파일한다. Canon이 아니며 실제 직전 화 결과는 JIT Runtime Overlay에서만 채운다.
## 1. Deep source bundle
- Subact Hub: `docs/10_story_architecture/subacts/V02-2A.md`
- Volume Scene-Ready: `docs/10_story_architecture/detail/v02-scene-ready-design-v1.md`
- D6 Registry: `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md`
- Active chronology / character checkpoints / POV / mystery / asset-state / permanent-loss / visual resolver / production standard.
## 2. Shared static deep context
- Ownership: `GA-I → V02 → V02-2A → E026–E031`.
- Subact Hub의 Goal/Entry/Exit/Agendas/Mystery/Locations/Cast/Institutions/Assets와 각 D6 row의 Goal/Opposition/Choice/Cost/Planned State Change/Hook/Next Cause를 상속한다.
- Timeline·POV·Mystery·asset custody·loss·visual current state는 active source가 historical CP보다 우선한다.
- F1의 실제 관계·기억·영웅기록 상태는 previous actual State와 합성하며 자동 복구/리셋 금지.
## 3. Episode ownership / causal routing
| EP | Exact D6 source | Previous Exit | Next | Override |
|---|---|---|---|---|
| E026 | `ga01-episode-registry-e001-e075.md#E026` | E025 actual Exit/JIT | E027 | — |
| E027 | `ga01-episode-registry-e001-e075.md#E027` | E026 actual Exit/JIT | E028 | — |
| E028 | `ga01-episode-registry-e001-e075.md#E028` | E027 actual Exit/JIT | E029 | — |
| E029 | `ga01-episode-registry-e001-e075.md#E029` | E028 actual Exit/JIT | E030 | — |
| E030 | `ga01-episode-registry-e001-e075.md#E030` | E029 actual Exit/JIT | E031 | — |
| E031 | `ga01-episode-registry-e001-e075.md#E031` | E030 actual Exit/JIT | E032 | — |
## 4. Episode Deep Entry contract
각 row는 22개 필드(Identity/Authority/D6/Entry/Timeline/Logistics/POV/Character/Relationship/Institution/System/Mystery/Assets/Loss/Clocks/Craft/Visual/Planned State/Next Cause/Mutation/Obsidian/Override)를 source-bound로 가진다. Draft 전 materialize 필수.
## 5. Runtime-only
Exact Entry, wounds, custody, relationship delta, exact permissions/clocks/evidence survival은 집필 직전에만 채운다.
## 6. Completion gate
- Coverage: **E026–E031 / 6 episodes**
- G1–G12 required. HUMAN PROSE PASS 별도.
