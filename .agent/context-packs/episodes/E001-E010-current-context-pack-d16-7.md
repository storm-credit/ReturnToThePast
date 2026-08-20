---
node_type: context_pack
node_id: CP-E001-E010-D16.7
scope: E001-E010
status: CURRENT CONTEXT MASTER / PACK-FIRST
base_main: da538974f8cfb200f359c0de797259f7885a9a03
parent_act: GA-I
parent_volume: V01
visual_router: docs/10_story_architecture/visual-cp-resolver-rules-v1.md
state_pipeline: docs/10_story_architecture/episode-context-state-pipeline-v1.md
---

# E001–E010 Current Context Pack — D16.7

Status: **CURRENT CONTEXT MASTER / PACK-FIRST COMPLETE**  
Purpose: E001–E010을 최신 정본·Act/Subact·POV·Chronology·Visual/State 규칙으로 다시 읽기 위한 현재형 Context Pack.  
Historical provenance: 기존 `.agent/context-packs/episodes/E001-context-pack.md` ~ `E010-context-pack.md`는 삭제·대체하지 않는다.  
Authority: 이 파일은 production routing overlay이며 Canon/Architecture/Decision/actual State보다 위가 아니다.

## 0. Pack-first rule

이 배치의 작업순서는 아래로 고정한다.

```text
CURRENT CANON / ACTIVE AMENDMENT
  → GA I / V01 / SUBACT 1A·1B
  → HISTORICAL CP + CURRENT STATE
  → THIS CURRENT CONTEXT PACK
  → MANUSCRIPT REVALIDATION
  → REPAIR ONLY IF REQUIRED
  → STATE / NEXT ENTRY RECHECK
```

따라서 과거 원고를 먼저 PASS/FAIL하고 나중에 Context를 맞추지 않는다.

이 파일은 D16.6 JIT schema의 회차별 필드를 10개 회차에 소급 적용한다. 큰 Bible 내용을 복제하지 않고 **현재 회차가 필요로 하는 정본 포인터와 상태만** 보유한다.

## 1. Shared authority stack

1. `docs/00_project/canon-constitution-v1.md`
2. active Decision / Amendment / Errata
3. `docs/01_timeline/master-chronology-and-aging-ledger-v1.md`
4. `docs/05_characters/cast-canon-index-v2.md`
5. `docs/05_characters/character-state-checkpoints-v1.md`
6. `docs/10_story_architecture/acts/GA-I.md`
7. `docs/10_story_architecture/detail/v01-scene-ready-design-v1.md`
8. current POV allocation + `d15-pov-allocation-supplement-v1.md`
9. `docs/11_mystery/mystery-reinforcement-ladder-v1.md` with active D16.7 routing correction
10. D16.4/D16.5 Visual Matrix / Resolver
11. actual previous State Mutation
12. historical episode CP / Craft Manifest
13. actual manuscript
14. current State Mutation / next-entry CP

Conflict rule: 1–10이 12의 옛 문구와 충돌하면 historical CP는 provenance로만 남고 현재 routing은 상위층을 따른다.

## 2. Shared V01 locks

- Grand Act: **GA I — 잘못된 치료**
- Volume: **V01 — 회색 종이 울리는 날**
- Arc 01: E001–E012 `살아남기 위해 믿어야 하는 거짓말`
- E001–E006: **Subact 1A — 출발표에 서명하는 사람**
- E007–E010: **Subact 1B — 격리촌의 통행증**
- C01 에이든 로엔 current visual state: **F0 FIELD**
- C02 리아 세른 where scene-present: **PRIVATE+OFFICIAL MIX**
- C03 아이리스 네르 where scene-present: **WESTERN FIELD**
- C10 메이라 솔: **FIELD MEDICAL**
- C26 아벨 네르: **PATIENT WITNESS**
- R01 회색 종: 공동체/증거 오브젝트. 예언도구·에이든 개인장비화 금지.
- 미래 F1/F2/F3 지식, ADDRESS-LOSS, Final Loss, 최종 마나열병/회색 종 정답을 앞당기지 않는다.

---

# E001 — 마지막 도시의 다른 날짜

## Routing
- EPISODE_ID: `E001`
- GRAND_ACT: `GA I`
- VOLUME: `V01`
- SUBACT: `1A`
- ARCHITECTURE_HUB: `docs/10_story_architecture/subacts/V01-1A.md`
- D6_CARD: `docs/10_story_architecture/detail/v01-scene-ready-design-v1.md#E001`
- HISTORICAL_CP: `.agent/context-packs/episodes/E001-context-pack.md`
- PREVIOUS_EXIT_SOURCE: series entry / GA I·V01·1A Entry State

## Current episode context
- ENTRY_STATE: F0 외곽 방벽 붕괴와 생존한계. 에이든은 아직 시간 파견에 동의하지 않았다.
- POV: **에이든 로엔 근접 3인칭**
- INFORMATION_CEILING: 동일 사건의 날짜 불일치·삭제된 증언자 흔적까지만. 조작 주체/세렌 실제 기능/F1 결과 금지.
- GOAL: 임무 정보와 원자료 열람 요구.
- OPPOSITION: 방벽 붕괴, 생존시한, 분산 승인권, 제한 기록.
- CHOICE: 불완전 브리핑 수령은 인정하지만 임무 동의는 보류.
- COST: 제7방벽 구조 가능 인원 감소 + 리아 비인가 열람 흔적.
- STATE_CHANGE_TARGET: 일반 구조 임무의 현장요원 → 시간 파견 후보.
- HOOK: 세 날짜·빈 증언자 자리·삭제된 이름 첫 글자.
- SCENE_ASSETS: C01, C02, F0 생존시설/승인기관, 세렌 기록 이미지.
- PRIMARY_VISUAL_ASSET: C01 `F0 FIELD`
- SECONDARY_ECHO: C02 `PRIVATE+OFFICIAL MIX`
- DO_NOT_REEXPLAIN: 시간장치 전체 원리, 기관 전체 역사.
- DO_NOT_ADVANCE: F1, 세렌 무죄/유죄 최종판정, 리아 최종 기억원리.
- ACTIVE_CLOCKS: formal series clock 별도 할당 없음; F0 생존시한과 방벽 구조 가능 인원 감소만 local deadline으로 사용.
- MYSTERY_CEILING: 기록이 틀릴 수 있다는 의심까지.
- LOSS_LOCKS: 영구손실 없음. 현장 인명/구조기회 감소는 실제 비용.
- CRAFT_ROUTE: E형 4장면; Goal–Opposition–Choice–Cost.
- NEXT_CAUSE_BOUNDARY: 미완전 기록과 압박이 E002의 6개 승인·귀환석 검사로 이동.

---

# E002 — 여섯 개의 승인

## Routing
- EPISODE_ID: `E002`
- GRAND_ACT: `GA I`
- VOLUME: `V01`
- SUBACT: `1A`
- ARCHITECTURE_HUB: `docs/10_story_architecture/subacts/V01-1A.md`
- D6_CARD: `docs/10_story_architecture/detail/v01-scene-ready-design-v1.md#E002`
- HISTORICAL_CP: `.agent/context-packs/episodes/E002-context-pack.md`
- PREVIOUS_EXIT_SOURCE: `manuscript/state/E001-state-mutation.md` + E001 manuscript exit

## Current episode context
- ENTRY_STATE: 브리핑 수령/동의 보류. 구조 가능 인원은 계속 감소하고 기록 검증은 미완료.
- POV: **에이든 로엔 근접 3인칭**
- INFORMATION_CEILING: 승인체계·귀환석 위험은 공개 가능. 장치 반복개입/배신자 확정 금지.
- GOAL: 기록 검증을 기다리면서 6개 분산 승인조건 통과.
- OPPOSITION: 구조 가능 인원 감소, 귀환석 균열, 승인순서 의존성.
- CHOICE: 즉시 출발보다 기록검증 서명을 기다림.
- COST: 기다린 만큼 현지 체류/귀환창 감소.
- STATE_CHANGE_TARGET: 임무 찬반 → 제한 조건 아래 출발 가능성으로 구체화.
- HOOK: 귀환석 내부의 출발지와 다른 시대 흙.
- SCENE_ASSETS: C01, C02 scene-present 범위, 6 승인 기능선, 귀환석.
- PRIMARY_VISUAL_ASSET: C01 `F0 FIELD`
- SECONDARY_ECHO: 기관별 다른 실무재료/표식. 특정 신규 인물 디자인 금지.
- DO_NOT_REEXPLAIN: E001 방벽붕괴를 새 장면처럼 반복하지 않음.
- DO_NOT_ADVANCE: 귀환석=완전복원키, 승인기관 개인흑막, 자유 시간선 선택.
- ACTIVE_CLOCKS: 승인 지연이 직접 줄이는 현지 체류/귀환창.
- MYSTERY_CEILING: 흙의 정확 연대·지역 미확정.
- LOSS_LOCKS: 귀환창 회복/균열 리셋 금지.
- CRAFT_ROUTE: S형 3장면; 제한자원 선택 + 절차 긴장.
- NEXT_CAUSE_BOUNDARY: 승인만으로 부족한 표적 증거 검토가 E003으로 연결.

---

# E003 — 창시자의 증거

## Routing
- EPISODE_ID: `E003`
- GRAND_ACT: `GA I`
- VOLUME: `V01`
- SUBACT: `1A`
- ARCHITECTURE_HUB: `docs/10_story_architecture/subacts/V01-1A.md`
- D6_CARD: `docs/10_story_architecture/detail/v01-scene-ready-design-v1.md#E003`
- HISTORICAL_CP: `.agent/context-packs/episodes/E003-context-pack.md`
- PREVIOUS_EXIT_SOURCE: `manuscript/state/E002-state-mutation.md`

## Current episode context
- ENTRY_STATE: 공식기록은 세렌 바일이 재앙 직전 금지의식을 시행했다고 주장. 귀환조건은 제한적.
- POV: **에이든 로엔 근접 3인칭**
- INFORMATION_CEILING: 공식 혐의와 기록 삭제 흔적은 공개. 책임전가 주체/세렌 전체 기능 금지.
- GOAL: 표적 제거를 정당화하는 증거의 강도를 확인.
- OPPOSITION: 압수도구·희생자수·왕실명령서는 혐의를 강화하지만 증언자 기록이 비정상.
- CHOICE: 의심을 품되 미래 전체를 걸 만큼 강한 반증은 아니라고 판단.
- COST: 수치의 규모가 출처검증보다 판단에 더 큰 무게를 갖기 시작.
- STATE_CHANGE_TARGET: `공식기록 수용` → `공식기록에 의심을 남긴 채 임무 지속`.
- HOOK: 삭제된 증언자의 사망일이 세렌에게 귀속된 범행일보다 앞섬.
- SCENE_ASSETS: C01, C02, C06는 기록/증거로만.
- PRIMARY_VISUAL_ASSET: C01 `F0 FIELD`
- SECONDARY_ECHO: C02 `PRIVATE+OFFICIAL MIX`, 물리적으로 도려낸 기록흔적.
- DO_NOT_REEXPLAIN: 세 날짜 단서를 E001처럼 다시 강의하지 않음.
- DO_NOT_ADVANCE: 세렌 무죄 확정, 기록조작 주체 확정.
- ACTIVE_CLOCKS: F0 생존시한/검증시간 충돌이 다음 화로 증폭.
- MYSTERY_CEILING: **이 사망일 역전 단서는 E003에서 이미 소비됨.** 현 `mystery-reinforcement-ladder-v1.md`의 E033 동일 단서 행은 production상 stale로 취급; E033에서 첫 단서처럼 재연 금지.
- LOSS_LOCKS: 없음.
- CRAFT_ROUTE: S형 3장면; 합리적 오답에 균열 삽입.
- NEXT_CAUSE_BOUNDARY: 더 검증하려면 시간이 필요하지만 E004에서 지연 자체가 실제 사망비용으로 돌아옴.

---

# E004 — 지연의 사망자

## Routing
- EPISODE_ID: `E004`
- GRAND_ACT: `GA I`
- VOLUME: `V01`
- SUBACT: `1A`
- ARCHITECTURE_HUB: `docs/10_story_architecture/subacts/V01-1A.md`
- D6_CARD: `docs/10_story_architecture/detail/v01-scene-ready-design-v1.md#E004`
- HISTORICAL_CP: `.agent/context-packs/episodes/E004-context-pack.md`
- PREVIOUS_EXIT_SOURCE: `manuscript/state/E003-state-mutation.md`

## Current episode context
- ENTRY_STATE: 증거는 모순되지만 F0 생존/약품·구조 자원은 계속 감소.
- POV: **에이든 로엔 근접 3인칭**
- INFORMATION_CEILING: 현지 앵커 정보가 비어 있다는 위험까지만.
- GOAL: 추가 검증시간을 확보할지 출발 리스크를 감수할지 결정.
- OPPOSITION: 하루 지연의 환자·약품·구조 비용, 미확정 현지 앵커.
- CHOICE: 누락 위험을 인지했다는 책임서에 서명하고 현지 앵커 없는 출발을 허용.
- COST: 지연 피해를 막는 대신 오착/귀환 위험을 자기 선택으로 인수.
- STATE_CHANGE_TARGET: 검증 보류 상태 → 불완전 정보 하 책임수용.
- HOOK: 목표 시대 귀환점 목록이 한 칸씩 사라짐.
- SCENE_ASSETS: C01, C02 where present, 선별/배급 기능선.
- PRIMARY_VISUAL_ASSET: C01 `F0 FIELD`
- SECONDARY_ECHO: C02는 기록노동자로만; 감정적 양심역할 금지.
- DO_NOT_REEXPLAIN: 선별파=악이라는 단순화 금지.
- DO_NOT_ADVANCE: 앵커 실패의 전체 시간법칙.
- ACTIVE_CLOCKS: F0 생존일 vs 검증시간.
- MYSTERY_CEILING: 귀환점 소실 원인 미확정.
- LOSS_LOCKS: 책임서 선택을 다음 화에서 무효화하지 않음.
- CRAFT_ROUTE: Q형 2장면으로 압축 해석; 기능비트 3개를 실제 장면수로 오해하지 않음.
- NEXT_CAUSE_BOUNDARY: 책임수용이 E005의 목표축소와 최종 출발서명으로 연결.

---

# E005 — 제거와 차단

## Routing
- EPISODE_ID: `E005`
- GRAND_ACT: `GA I`
- VOLUME: `V01`
- SUBACT: `1A`
- ARCHITECTURE_HUB: `docs/10_story_architecture/subacts/V01-1A.md`
- D6_CARD: `docs/10_story_architecture/detail/v01-scene-ready-design-v1.md#E005`
- HISTORICAL_CP: `.agent/context-packs/episodes/E005-context-pack.md`
- PREVIOUS_EXIT_SOURCE: `manuscript/state/E004-state-mutation.md`

## Current episode context
- ENTRY_STATE: 위험을 알고도 출발경로를 유지하기로 한 상태. 귀환 가능성을 위해 목표축소 필요.
- POV: **에이든 로엔 근접 3인칭**
- INFORMATION_CEILING: 리아의 경고는 경고일 뿐 진실판정이 아님.
- GOAL: 제한된 귀환창 안에 수행할 임무범위를 확정.
- OPPOSITION: 조사/구조 범위를 넓히면 귀환확률과 표적접근이 악화.
- CHOICE: `개혁가 제거 + 연대기 접근 차단`으로 목표를 좁히고 임무 거부는 하지 않음.
- COST: 현지에서 더 넓은 검증/구조를 할 기회를 스스로 버림.
- STATE_CHANGE_TARGET: 조건부 출발 후보 → 좁은 임무에 서명한 요원.
- HOOK: 출발 인장에 표적 진명이 아닌 다른 이름이 잠깐 비침.
- SCENE_ASSETS: C01, C02, 출발 인장/임무문서.
- PRIMARY_VISUAL_ASSET: C01 `F0 FIELD`
- SECONDARY_ECHO: C02 `PRIVATE+OFFICIAL MIX`.
- DO_NOT_REEXPLAIN: E003 증거대조 재연 금지.
- DO_NOT_ADVANCE: 리아 경고를 정답화, 세렌 완전 면죄.
- ACTIVE_CLOCKS: 귀환창 / 임무범위 교환.
- MYSTERY_CEILING: 다른 이름의 의미 미확정.
- LOSS_LOCKS: 포기한 조사범위를 다음 화에서 무료 복구하지 않음.
- CRAFT_ROUTE: S형 3장면.
- NEXT_CAUSE_BOUNDARY: 최소 정족수와 서명 완료 → E006 실제 도약.

---

# E006 — 빗나간 도착

## Routing
- EPISODE_ID: `E006`
- GRAND_ACT: `GA I`
- VOLUME: `V01`
- SUBACT: `1A`
- ARCHITECTURE_HUB: `docs/10_story_architecture/subacts/V01-1A.md`
- D6_CARD: `docs/10_story_architecture/detail/v01-scene-ready-design-v1.md#E006`
- HISTORICAL_CP: `.agent/context-packs/episodes/E006-context-pack.md`
- PREVIOUS_EXIT_SOURCE: `manuscript/state/E005-state-mutation.md`

## Current episode context
- ENTRY_STATE: 6개 권한의 최소 정족수 성립. 현지 앵커 없음. 제한된 강제귀환 1회 조건.
- POV: **에이든 로엔 근접 3인칭**
- INFORMATION_CEILING: 도약 실패조건·오착 결과까지만. 장치 전체 기전 금지.
- GOAL: 제한조건 안에서 Era N 목표지점으로 진입.
- OPPOSITION: 좌표오차, 몸 부담, 미등록 개인물품, 현지 앵커 부재.
- CHOICE: 조건을 수용하고 도약.
- COST: 예정 도시 내부가 아닌 서부 수로로 오착; 일부 장비 잠김; 현지 신분문서 무효.
- STATE_CHANGE_TARGET: F0 요원 → Era N의 신분 없는 외지인.
- HOOK: 멀리 회색 종과 귀환석의 같은 박자 진동.
- CURRENT_CHRONOLOGY: **출발 F0/CY 664/장야월 21일 → 도착 N0/CY 640/안개월 4일**.
- SCENE_ASSETS: C01, F0 출발장비, 귀환석, R01은 원거리 관측 echo만.
- PRIMARY_VISUAL_ASSET: C01 `F0 FIELD`
- SECONDARY_ECHO: F0 실무장비; R01 반응은 설명 없는 소리/진동.
- DO_NOT_REEXPLAIN: E001~E005 승인과정 전체 재설명 금지.
- DO_NOT_ADVANCE: 아이리스 직접등장, 회색 종 원리, 주소불일치 정답.
- ACTIVE_CLOCKS: 귀환 가능시간/현지 체류창.
- MYSTERY_CEILING: 회색 종과 귀환석의 동조는 관측만.
- LOSS_LOCKS: 오착/장비잠금/신분실패를 즉시 복구하지 않음.
- CRAFT_ROUTE: X형 5~6장면.
- NEXT_CAUSE_BOUNDARY: 오착·신분부재·숨겨야 할 장비가 E007 현지 관찰/통행문제로 연결.

Historical note: 과거 CP/frontmatter의 `정확한 날짜 미확정` 계열 문구는 현재 J01보다 낮은 provenance다.

---

# E007 — 회색 종 곁의 외지인

## Routing
- EPISODE_ID: `E007`
- GRAND_ACT: `GA I`
- VOLUME: `V01`
- SUBACT: `1B`
- ARCHITECTURE_HUB: `docs/10_story_architecture/subacts/V01-1B.md`
- D6_CARD: `docs/10_story_architecture/detail/v01-scene-ready-design-v1.md#E007`
- HISTORICAL_CP: `.agent/context-packs/episodes/E007-context-pack.md`
- PREVIOUS_EXIT_SOURCE: `manuscript/state/E006-state-mutation.md`

## Current episode context
- ENTRY_STATE: 에이든은 N0 서부 격리촌 외곽 오착. 현지 신분 없음, 일부 장비 잠김, 귀환자원 제한.
- POV: **C03 아이리스 네르 — P1**
- INFORMATION_CEILING: 아이리스는 에이든의 임무 목적/F0 전체 사정/장비 내부 계산을 모른다.
- GOAL: 아이리스가 환자 호송·현지 질서·거부권을 지키면서 정체불명 외지인을 독립적으로 관찰하고 경로 위험을 판단.
- OPPOSITION: 신분 없는 외지인, 환자 호송의 실제 부족자원, 회색 종의 설명되지 않는 반응, 현지 규칙을 모르는 행동.
- CHOICE: 아이리스는 에이든에게 협력자가 되지 않고, 호송/순번/경로를 주민 필요에 맞게 조정하면서 추적을 지속.
- COST: 에이든은 본인이 모르는 현지 결정의 결과를 E008에서 떠안음; 아이리스도 호송 책임과 관찰 부담을 같이 짊어짐.
- STATE_CHANGE_TARGET: `관측되지 않은 오착자` → `현지인이 독립적으로 기억하고 추적하는 외지인`.
- HOOK: 회색 종/외지인 장비의 비정상 반응과, 그 장면을 아이리스가 자기 기준으로 기억함.
- SCENE_ASSETS: **C03 primary**, C01 external-only, R01 echo, 환자 호송/서부 생활흔적.
- PRIMARY_VISUAL_ASSET: C03 `WESTERN FIELD`
- SECONDARY_ECHO: C01 `F0 FIELD` external silhouette, R01 현장 오브젝트.
- DO_NOT_REEXPLAIN: 에이든 내부 장비수치/귀환마력 계산을 아이리스가 아는 것처럼 쓰지 않음.
- DO_NOT_ADVANCE: 아이리스=운명적 안내자, 에이든 임무목적 인지, 협력 확정, 로맨스 신호.
- ACTIVE_CLOCKS: 호송 일정 / 에이든 귀환창은 아이리스에게 수치로 공개되지 않음.
- MYSTERY_CEILING: 회색 종은 반응만; 무엇을 감지하는지 미확정.
- LOSS_LOCKS: E006 장비잠금/신분실패 유지.
- CRAFT_ROUTE: S형 3장면; **관측당하는 주인공을 현지인 P1에서 구현**.
- NEXT_CAUSE_BOUNDARY: 아이리스의 독립 경로/순번 결정이 E008에서 에이든이 만나는 현실로 나타남.

Current conflict note: historical E007 CP/Manifest/manuscript의 에이든 POV는 현재 active POV allocation과 충돌한다. 이 Current Pack이 먼저 기준을 고정하며, 원고 수리는 다음 단계다.

---

# E008 — 이름 없는 검문

## Routing
- EPISODE_ID: `E008`
- GRAND_ACT: `GA I`
- VOLUME: `V01`
- SUBACT: `1B`
- ARCHITECTURE_HUB: `docs/10_story_architecture/subacts/V01-1B.md`
- D6_CARD: `docs/10_story_architecture/detail/v01-scene-ready-design-v1.md#E008`
- HISTORICAL_CP: `.agent/context-packs/episodes/E008-context-pack.md`
- PREVIOUS_EXIT_SOURCE: current E007 target exit + `manuscript/state/E007-state-mutation.md` event-state salvage

## Current episode context
- ENTRY_STATE: 에이든은 환자 행렬에 섞였지만 무등록. 아이리스는 이미 독립 관찰/추적 중.
- POV: **에이든 로엔 근접 3인칭 + 메이라 솔 P3 제한 관찰 1회**
- INFORMATION_CEILING: 마나열병 최종원리/아벨 발언 의미/아이리스 협력여부 미확정.
- GOAL: 격리촌 검문과 언어·화폐/책임귀속 차이를 통과.
- OPPOSITION: 존재하지 않는 왕조 형식의 문서, 책임회피 검문실무, 파손 수레, 현지 관찰.
- CHOICE: 환자 호송을 돕는 조건으로 임시 통행권/노역표를 얻음.
- COST: 임무시간과 이동자유가 호송 일정에 묶이고 얼굴·발음·손기술이 기록됨.
- STATE_CHANGE_TARGET: 숨어서 통과하는 외지인 → 조건을 지고 등록된 노동자.
- HOOK: C26 아벨 네르가 처음 본 에이든에게 `두 번째로 늦게 왔다`고 말함.
- SCENE_ASSETS: C01, C03, C10, C26, 관문/수레/임시대기막.
- PRIMARY_VISUAL_ASSET: C01 `F0 FIELD`
- SECONDARY_ECHO: C03 `WESTERN FIELD`, C10 `FIELD MEDICAL`, C26 `PATIENT WITNESS` 중 scene function에 따라 최대 2.
- DO_NOT_REEXPLAIN: E007 회색 종 반응을 재타종해 설명하지 않음.
- DO_NOT_ADVANCE: 아벨 예언자화, 마나열병 정답, 아이리스 자동동료화.
- ACTIVE_CLOCKS: 환자 호송 일정 + 에이든 귀환/표적 접근시간.
- MYSTERY_CEILING: 가족 단위 증상과 존재하지 않는 가족/집 기억까지.
- LOSS_LOCKS: 임시 등록으로 추적 가능해진 상태 유지.
- CRAFT_ROUTE: E형 4장면 + 메이라 P3는 별도 장면 수 증가 없이 제한 창.
- NEXT_CAUSE_BOUNDARY: 호송의무·아벨의 모순기억이 E009 이중 출생증명 검증으로 연결.

---

# E009 — 두 개의 출생증명

## Routing
- EPISODE_ID: `E009`
- GRAND_ACT: `GA I`
- VOLUME: `V01`
- SUBACT: `1B`
- ARCHITECTURE_HUB: `docs/10_story_architecture/subacts/V01-1B.md`
- D6_CARD: `docs/10_story_architecture/detail/v01-scene-ready-design-v1.md#E009`
- HISTORICAL_CP: `.agent/context-packs/episodes/E009-context-pack.md`
- PREVIOUS_EXIT_SOURCE: `manuscript/state/E008-state-mutation.md`

## Current episode context
- ENTRY_STATE: 에이든은 기한부 등록/호송의무. 아벨 가족의 유사증상과 모순기억이 확인됨.
- POV: **에이든 로엔 근접 3인칭**
- INFORMATION_CEILING: 두 출생증명은 진품-compatible. 어느 쪽도 가짜로 확정하지 않음. 최종 병인 금지.
- GOAL: 마나열병을 접촉전염으로 보는 가설을 실제 관측으로 시험.
- OPPOSITION: 두 장 모두 오래된 진품 인장/재료, 가족접촉 안정, 기록 낭독과 증상 악화의 상관.
- CHOICE: 관측이 가설과 어긋나면 가설을 방어하지 않고 조건을 다시 나눔.
- COST: 미래지식으로 내린 첫 판단의 신뢰가 약해지고 현지인 불신 증가.
- STATE_CHANGE_TARGET: `아는 사람의 개입` → `모른다는 상태를 인정한 관찰`.
- HOOK: 아벨의 두 번째 고향이 공식 지도에 존재하지 않음.
- SCENE_ASSETS: C01, C03, C10, C26, 출생증명 2장, 임시진료/서류대.
- PRIMARY_VISUAL_ASSET: C26 `PATIENT WITNESS` 또는 현재 장면 중심 C01. 실제 장면기능을 먼저 정하고 선택.
- SECONDARY_ECHO: C03/C10 current states, R01 if scene-present only.
- DO_NOT_REEXPLAIN: E008 검문·등록 협상 반복 금지.
- DO_NOT_ADVANCE: 한 문서를 위조로 확정, 비감염성 정답, 회색 종 주소감지 정답.
- ACTIVE_CLOCKS: 호송/재심 일정과 귀환창.
- MYSTERY_CEILING: 기록낭독-증상 상관까지만.
- LOSS_LOCKS: 에이든의 오판을 즉석 정답 획득으로 상쇄하지 않음.
- CRAFT_ROUTE: S형 3장면; 합리적 오답의 실패 실연.
- NEXT_CAUSE_BOUNDARY: 사람을 어떻게 분류할 것인가가 E010의 구휼기사단 절차 충돌로 확대.

---

# E010 — 구휼과 분류

## Routing
- EPISODE_ID: `E010`
- GRAND_ACT: `GA I`
- VOLUME: `V01`
- SUBACT: `1B`
- ARCHITECTURE_HUB: `docs/10_story_architecture/subacts/V01-1B.md`
- D6_CARD: `docs/10_story_architecture/detail/v01-scene-ready-design-v1.md#E010`
- HISTORICAL_CP: `.agent/context-packs/episodes/E010-context-pack.md`
- PREVIOUS_EXIT_SOURCE: `manuscript/state/E009-state-mutation.md`

## Current episode context
- ENTRY_STATE: 감염 정답은 미확정. 기록 불일치 환자 분류문제가 실제 구호체계의 수용력과 충돌.
- POV: **에이든 로엔 근접 3인칭**
- INFORMATION_CEILING: 분류기준이 최종 병인을 증명하지 않음. 세렌 조직의 환자 이동 목적 미확정.
- GOAL: 구휼기사단이 실제 생명을 구하면서도 강제분류한다는 양면을 동시에 성립.
- OPPOSITION: 제한 침상/물/약/수레, 분류권한, 에이든의 신분·접근권 부족.
- CHOICE: 기사단과 무력충돌하지 않고 치료수송에 참여하면서 목적지 확인권을 요구.
- COST: 에이든이 기사단 명부에 외지 치료보조자로 등재돼 위치/일정이 추적 가능.
- STATE_CHANGE_TARGET: 무등록/기한부 노동자 → 등록되어 관측되는 치료 협력자.
- HOOK: 정규 경로 밖 수레/굄목 흔적과 표적 조직 관련 문양의 유사성. 의미 확정 금지.
- SCENE_ASSETS: C01, C03, C10, C26, 성당 구휼기사단, 치료선/분류대/수레 마당.
- PRIMARY_VISUAL_ASSET: C10 `FIELD MEDICAL` 또는 scene function상 C01. 구호 실효가 보이는 생활자산 우선.
- SECONDARY_ECHO: C03 `WESTERN FIELD`, C26 `PATIENT WITNESS`.
- DO_NOT_REEXPLAIN: E009 서류 2장 대조를 다시 핵심구조로 쓰지 않음.
- DO_NOT_ADVANCE: 구휼기사단 평면 악역화, 세렌 조직 목적 확정, 마나열병 최종정답.
- ACTIVE_CLOCKS: 수용가능 침상/신규 유입수 + 에이든 표적접근/귀환시간.
- MYSTERY_CEILING: `기록 불일치가 분류에 쓰인다`까지; 원인 확정 금지.
- LOSS_LOCKS: 등록으로 생긴 추적가능성을 E011에서 지우지 않음.
- CRAFT_ROUTE: E형 4장면; 반대편 효용을 실제로 성립시킨 제도갈등.
- NEXT_CAUSE_BOUNDARY: 등록된 치료수송 역할 + 줄어든 임무시간 + 미해결 수레 흔적이 E011 다리 구조/추적 선택으로 직결.

---

## 3. Batch handoff checksum

```text
E001 incomplete evidence
→ E002 distributed approval / return risk
→ E003 evidence contradiction
→ E004 delay has human cost
→ E005 mission narrowed and accepted
→ E006 jump / miss / identity failure
→ E007 Iris P1 independent local observation and route action
→ E008 checkpoint / temporary registration / Abel anomaly
→ E009 rational infection hypothesis fails under evidence
→ E010 relief utility + coercive classification / traceable registration
→ E011 bridge rescue vs mission-time choice
```

Required invariant:
- 어떤 화도 다음 화의 선택을 무료로 만든 상태로 끝나지 않는다.
- E007 수리 전에도 **목표 Exit State**는 이 팩에 먼저 고정되어 있어야 한다.
- 원고 수리 후 E006→E007→E008 handoff를 다시 검증한다.

## 4. Obsidian graph contract

권장 edge:

```text
[[E001]] → [[V01-1A]] → [[CP-E001-E010-D16.7]]
[[E002]] → [[V01-1A]] → [[CP-E001-E010-D16.7]]
...
[[E006]] → [[V01-1A]] → [[CP-E001-E010-D16.7]]
[[E007]] → [[V01-1B]] → [[CP-E001-E010-D16.7]] → [[C03-아이리스-네르]]
[[E008]] → [[V01-1B]] → [[CP-E001-E010-D16.7]]
[[E009]] → [[V01-1B]] → [[CP-E001-E010-D16.7]]
[[E010]] → [[V01-1B]] → [[CP-E001-E010-D16.7]]
```

- Historical CP는 provenance edge.
- Current Pack은 current-production edge.
- 실제 manuscript/state 파일과의 연결은 Episode node가 담당.
- backlinks를 사용하므로 무의미한 양방향 링크 복제 금지.

## 5. Pack gate

### PASS
- E001–E010 10/10에 current routing header 존재.
- 10/10 previous-state source 또는 series entry 존재.
- 10/10 POV current lock 명시.
- 10/10 information ceiling / Do Not Advance 명시.
- 10/10 next-cause boundary 명시.
- D16.4/D16.5 visual state를 현재 시점으로 제한.
- historical CP는 보존.
- 기존 원고 변경 0.

### Known current-production repairs exposed by pack
- E003: Mystery Ladder의 옛 E033 중복 단서 routing debt.
- E006: 옛 CP/frontmatter의 chronology metadata debt.
- E007: historical CP/manuscript Aiden POV vs current Iris P1 architecture conflict.

이 3개는 **팩이 먼저 발견/고정한 수리대상**이며, 팩을 원고에 맞춰 왜곡하지 않는다.

**E001–E010 CURRENT CONTEXT PACK: COMPLETE / READY FOR MANUSCRIPT REVALIDATION.**
