---
node_type: deep_context_master
node_id: DCP-V01-1B
parent_act: GA-I
parent_volume: V01
parent_subact: V01-1B
episode_start: E007
episode_end: E012
status: STATIC DEEP CONTEXT / SOURCE-BOUND COMPLETE
runtime_state: JIT_ONLY
---

# V01-1B — Static Deep Context Master

> 이미 확정된 Act/Volume/Subact/D6를 집필 입력으로 깊게 컴파일한다. 이 Pack은 Canon이 아니며, 아직 쓰이지 않은 회차의 실제 Exit·부상·소유권·정확한 Clock 값을 선결정하지 않는다.

## 1. Deep source bundle
- Subact Hub: `docs/10_story_architecture/subacts/V01-1B.md`
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
- Ownership: `GA-I → V01 → V01-1B → E007–E012`.
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
| E007 | `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md#E007` | E006 actual Exit/JIT | E008 | POV=C03 아이리스 P1; Aiden interior 금지 |
| E008 | `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md#E008` | E007 actual Exit/JIT | E009 | — |
| E009 | `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md#E009` | E008 actual Exit/JIT | E010 | — |
| E010 | `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md#E010` | E009 actual Exit/JIT | E011 | — |
| E011 | `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md#E011` | E010 actual Exit/JIT | E012 | — |
| E012 | `docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md#E012` | E011 actual Exit/JIT | E013 | — |

## 4. Episode Deep Entry materialization contract
위 표의 **각 Episode row는 아래 22필드를 모두 가진다.** 값은 Deep Source Bundle에서 resolve한다: ID/title/GA/V/Subact/Arc; Authority; D6 G/O/C/C/State/Hook; Entry assumptions; timeline; logistics; POV/knowledge; character agency; relationship; institution benefit; system ceiling; mystery rung/false interpretation; asset custody; permanent loss; clocks; density/craft/anti-repeat; visual anchors/current state/do-not-advance; planned state target; next cause; mutation checklist; Obsidian edges; stale override/gap.

Drafting agent must materialize these fields before prose. Source pointer를 읽지 않은 상태로 빈칸을 추측하면 FAIL.

## 5. JIT Runtime Overlay — deliberately unfrozen
PREVIOUS_EXIT_SOURCE / exact Entry State / wounds / missing persons / possession-custody / relationship delta / exact permissions / exact clocks / evidence survival / allowed offscreen transition은 집필 직전에만 채운다.

## 6. Completion gate
- Coverage: **E007–E012 / 6 episodes**
- G1–G12 required. HUMAN PROSE PASS는 별도다.
