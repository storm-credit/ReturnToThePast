---
node_type: deep_context_master
node_id: DCP-V02-2B
parent_act: GA-I
parent_volume: V02
parent_subact: V02-2B
episode_start: E032
episode_end: E037
status: STATIC DEEP CONTEXT / SOURCE-BOUND COMPLETE
runtime_state: JIT_ONLY
---
# V02-2B — Static Deep Context Master
> Static Deep Context. Runtime exact state는 JIT-only.
## 1. Deep source bundle
- `docs/10_story_architecture/subacts/V02-2B.md`
- `docs/10_story_architecture/detail/v02-scene-ready-design-v1.md`
- `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md`
- active chronology / character / POV / mystery / assets-loss / visual / deep-context standard.
## 2. Shared locks
- Ownership: `GA-I → V02 → V02-2B → E032–E037`.
- D6 causality, Subact agenda, multi-source evidence limits, custody and legal traceability를 보존한다.
- 하나의 유산·보고서·신수·감사관을 최종 truth judge로 승격하지 않는다.
- 증거 생존성 증가와 에이든 개인 통제 감소를 구분한다.
## 3. Routing
| EP | D6 | Prev | Next | Override |
|---|---|---|---|---|
| E032 | `ga01-episode-registry-e001-e075.md#E032` | E031 JIT | E033 | — |
| E033 | `ga01-episode-registry-e001-e075.md#E033` | E032 JIT | E034 | E003 사망일 단서를 첫 공개처럼 반복 금지; current function은 F0 임무보고서 metadata/다렌 작성자 hook |
| E034 | `ga01-episode-registry-e001-e075.md#E034` | E033 JIT | E035 | — |
| E035 | `ga01-episode-registry-e001-e075.md#E035` | E034 JIT | E036 | — |
| E036 | `ga01-episode-registry-e001-e075.md#E036` | E035 JIT | E037 | — |
| E037 | `ga01-episode-registry-e001-e075.md#E037` | E036 JIT | E038 | — |
## 4. 22-field materialization
각 row는 active source에서 Identity/Authority/D6/Entry/Timeline/Logistics/POV/Agency/Relationship/Institution/System/Mystery/Assets/Loss/Clocks/Craft/Visual/Planned State/Next Cause/Mutation/Graph/Override를 materialize한다. 큰 Bible 복제 금지.
## 5. Runtime-only
Previous actual Exit, exact custody/permissions/clocks/evidence copies는 drafting 직전에만.
## 6. Gate
Coverage **E032–E037 / 6**, G1–G12 required.
