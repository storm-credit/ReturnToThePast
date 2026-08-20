---
node_type: deep_context_master
node_id: DCP-V03-3A
parent_act: GA-I
parent_volume: V03
parent_subact: V03-3A
episode_start: E051
episode_end: E056
status: STATIC DEEP CONTEXT / SOURCE-BOUND COMPLETE
runtime_state: JIT_ONLY
---
# V03-3A — Static Deep Context Master
## Sources
`docs/10_story_architecture/subacts/V03-3A.md`; `v03-scene-ready-design-v1.md`; GA I D6 registry; active chronology/character/POV/mystery/assets/loss/visual.
## Locks
- Ownership `GA-I → V03 → V03-3A → E051–E056`.
- Subact causal state and D6 row are authoritative for planned beat; actual achieved state is not pre-frozen.
- Character agency, institution benefit, evidence ceiling, asset custody/loss and anti-repeat preserved.
## Routing
E051←E050→E052; E052→E053; E053→E054; E054→E055; E055→E056; E056→E057. Each uses exact `ga01-episode-registry-e001-e075.md#E###` row.
## 22-field contract
Identity, authority, D6, entry, timeline/logistics, POV/knowledge, character/relationship, institution/system, mystery, assets/loss, clocks, craft/visual, planned state, next cause, mutation, Obsidian, override are resolved before prose. Runtime exact values stay JIT-only.
## Gate
Coverage **E051–E056 / 6**, G1–G12.
