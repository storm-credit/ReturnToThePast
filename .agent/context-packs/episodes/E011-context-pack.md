# Episode Context Pack — E011

Status: D10 READY  
Episode: E011  
Title: 한 번 늦어진 임무  
Compiled By: A21 Context Pack Compiler  
Reference: `agent/1b-subact-context-packs`

> 이 CP는 정본이 아니다. 충돌 시 원본 정본과 권한계층을 따른다.

## 1. Authority / Architecture

Required sources:

- [`/AI_PROJECT.md`](../../../AI_PROJECT.md)
- [`docs/00_project/canon-constitution-v1.md`](../../../docs/00_project/canon-constitution-v1.md)
- [`docs/00_project/canon-naming-pack-v1.md`](../../../docs/00_project/canon-naming-pack-v1.md)
- [`docs/00_project/terminology-and-addressing-clarification-v1.md`](../../../docs/00_project/terminology-and-addressing-clarification-v1.md)
- [`docs/00_project/decision-log.md`](../../../docs/00_project/decision-log.md) — DEC-016·017·018·020·021
- [`docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md`](../../../docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md) — E011 행
- [`docs/10_story_architecture/detail/v01-scene-ready-design-v1.md`](../../../docs/10_story_architecture/detail/v01-scene-ready-design-v1.md) — Subact 1B / E011 절
- [`docs/10_story_architecture/detail/v01-d9-correction-overlay.md`](../../../docs/10_story_architecture/detail/v01-d9-correction-overlay.md) — §6
- [`docs/10_story_architecture/subact-causal-matrix-v1.md`](../../../docs/10_story_architecture/subact-causal-matrix-v1.md) — 1B 행
- [`docs/10_story_architecture/location-world-crosswalk-v1.md`](../../../docs/10_story_architecture/location-world-crosswalk-v1.md) — V01 1B, 이동·장면 감사
- [`docs/10_story_architecture/scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) — V1 E011 행
- [`docs/05_characters/cast-canon-index-v2.md`](../../../docs/05_characters/cast-canon-index-v2.md) — C01 · C03
- [`docs/05_characters/voice-relationship-state-bible-v1.md`](../../../docs/05_characters/voice-relationship-state-bible-v1.md) — §2 · §3 에이든↔아이리스 · §5
- [`docs/03_systems/causal-propagation-and-memory-protocol-v1.md`](../../../docs/03_systems/causal-propagation-and-memory-protocol-v1.md) — 살아 있는 현지 앵커 · 귀환 판정
- [`docs/02_world/military-foreign-powers-v1.md`](../../../docs/02_world/military-foreign-powers-v1.md) — 미래 장비 한계
- [`docs/11_mystery/mystery-reinforcement-ladder-v1.md`](../../../docs/11_mystery/mystery-reinforcement-ladder-v1.md) — M02 · M14 · M15
- [`docs/12_losses/permanent-loss-lock-v1.md`](../../../docs/12_losses/permanent-loss-lock-v1.md)
- [`.agent/context-packs/episodes/E010-context-pack.md`](E010-context-pack.md)

Episode function:

- Grand Act: GA I — 잘못된 치료
- Volume: V1 — 회색 종이 울리는 날
- Subact: 1B — 격리촌의 통행증
- Beat: 선택
- Goal: 현지 주민을 임무의 수단으로 삼을 것인지 실제 상황에서 판단하게 한다
- Opposition: 본부의 잔여시간 신호, 붕괴한 다리, 갈라지는 두 경로
- Choice: 임무 시간을 희생해 붕괴 수레와 환자를 구하며, 사람 → 기록상자 순서로 구조
- Cost: 표적 접촉 가능 시간이 반나절 줄고 미래 장비 일부가 물에 노출돼 은폐가 약해짐
- State Change: 에이든의 현지 행동이 ‘임무 유지용 위장’에서 ‘실제로 임무를 깎는 선택’으로 이동
- Hook: 구조한 기록상자 안에 에이든의 출발일보다 뒤에 작성된 문서가 있음 — 현지 앵커 후보가 그를 감시한다
- Next Cause: E012에서 이 구조행위가 통행권의 근거가 되지만 동시에 아이리스의 조건부 거래를 부른다

## 2. E010 Carryover

원본: `E010-context-pack.md` §11 · `v01-scene-ready-design-v1.md` E010

### 에이든

- 성당 구휼기사단 명부에 외지 치료보조자로 등재돼 위치·일정이 추적 가능하다
- 별도 수레 목적지 확인권을 얻었으나 절차 바깥에서 벌어진 일에는 닿지 않는다
- 치료 수송 참여로 표적 접근 가능 시간이 이미 줄어든 상태다
- 미래 장비는 여전히 은폐 상태이며 노출은 미발생

### 아이리스

- 에이든의 협상을 관찰했고 의심의 내용이 갱신됐다
- 여전히 에이든의 임무 목적을 모르며 협조 의무가 없다
- 귀환표식 연결·차단에 동의권을 가진다

### 현장

- 표적 조직의 문양이 격리촌 인근에서 관측된 상태로 미해석 유지
- 환자 가족들의 요구는 미해결로 남아 있다
- 회색 종은 E010에서 울리지 않았다

E011은 E010의 협상 구조를 반복하지 않는다. 이번 회차에는 협상 상대가 없고, 선택할 시간만 있다.

## 3. Time / Location

원본: `master-chronology-and-aging-ledger-v1.md` §1–§2 · `location-world-crosswalk-v1.md` 이동·장면 감사

- Era: N
- 기준연도: 건국력(CY) 640
- 에이든: 41세
- Main locations:
  1. 다리 입구 — 환자 호송로와 표적 추적로가 갈라지는 분기점
  2. 붕괴한 다리와 강 — 수레가 기울고 사람과 상자가 떨어지는 현장
  3. 강가 — 건져 올린 것들을 늘어놓는 자리
- 이동: 격리촌에서 도시 관문 방향 육로 호송 중이며 우회로는 실시간으로 계산된다
- 두 경로는 물리적으로 갈라지므로 하나를 택하면 다른 하나는 그 시간만큼 늦어진다

## 4. Rescue Logistics and Time Cost

원본: `v01-scene-ready-design-v1.md` E011 · `causal-propagation-and-memory-protocol-v1.md` · `military-foreign-powers-v1.md`

### 시간 구조

- 본부의 잔여시간 신호가 표적 쪽으로 즉시 이동하라고 재촉한다
- 신호는 명령이자 계산이며, 본부는 현지 사망·이동·정치 변화를 실시간으로 보지 못한다
- 구조에 쓰는 시간은 그대로 표적 접촉 가능 시간에서 빠진다 — 이 회차의 확정 비용은 **반나절**

### 물리 조건

- 붕괴는 수리 대상이 아니라 진행 중인 사고다. E008의 수레 축 수리와 같은 문제로 다루지 않는다
- 사람과 기록상자가 동시에 물로 향하며 둘 다 건질 시간은 없다
- 구조 순서는 사람 → 기록상자다

### 미래 장비 한계

- 미래 장비는 수리재료와 동반등록 한계 때문에 과거에서 무한 우위를 주지 않는다
- 이 회차에서 장비는 문제를 해결하는 도구가 아니라 **노출되는 물건**이다
- 물에 잠긴 장비 일부가 드러나 은폐가 약해진다
- 금지: 장비 사용으로 구조를 성공시키기, 장비 손상을 즉석 수리로 되돌리기

### 귀환 조건

- 살아 있는 현지 앵커는 여전히 미확보다
- 아이리스가 귀환표식을 거부하면 자동 강제귀환이 불가능하다는 조건이 배경으로 유지된다

## 5. Character State

원본: `cast-canon-index-v2.md` · `voice-relationship-state-bible-v1.md` · `v01-d9-correction-overlay.md` §6

### 에이든 로엔

- 목표: 표적 접근과 호송 유지 중 하나를 택해야 함을 인정
- 내적 압박: 본부 신호는 숫자를 말하고 눈앞의 강은 사람을 말한다
- 습관: 목표 → 출구 → 비용 순서. 이 회차에서는 그 순서를 끝까지 세우지 못하고 움직인다
- 죄책감 표식: 상대를 이름이 아니라 ‘환자·표적·요원’ 같은 역할명으로 부른다 — 이 회차에서 특히 두드러진다
- 오류 가능성: 사람을 먼저 구한 행동을 스스로 임무 실패의 증거로 셈함
- 금지: 영웅적 결단으로 미화, 구조 성공으로 신뢰를 자동 획득

### 아이리스 네르 (C03)

- 역할: 이 회차의 관찰자이자 독립 행위자. 에이든의 구조 순서를 직접 본다
- 독립 행동: 도움을 받았다고 충성하지 않고 장비의 정체를 묻는다
- 말투: 사람·장소·오늘 필요한 물자를 구체적으로 언급하며, 누가 언제 무엇을 잃는지 묻는다
- 모르는 것: F0/F1의 전체 생존상태, 국가장치의 기술적 연쇄, 에이든의 임무 목적
- 금지: 감화에 의한 협력 전환, 운명적 안내자화, 로맨스 축 진입

### 환자와 호송 인원

- 각자 자기 가족·짐·순번을 우선하며 주인공의 지시를 기다리지 않는다
- 구조된 사람은 감사 표현보다 자기 사람을 먼저 찾는다

### 본부 (신호로만 등장)

- 잔여시간 계산은 실제 근거를 가진다. 악의적 재촉이 아니다
- 현지 상황을 볼 수 없으므로 판단이 틀릴 수 있다
- 금지: 신호를 악역 목소리로 연출, 통신 대사 낭독으로 장면 채우기

## 6. Mystery / Information Ceiling

원본: `mystery-reinforcement-ladder-v1.md` M02 · M14 · M15

Active mysteries:

- M02 세렌 바일은 왜 창시자로 기록됐는가
- M14 원래 시간선은 진짜인가 — 출발일보다 뒤에 작성된 문서가 시간 순서 자체를 흔든다
- M15 최초 연대기는 어디 있는가 — 기록상자가 왜 사람과 함께 호송되는가

Reader may know:

- 임무 시간과 사람 목숨이 같은 시계를 쓴다
- 구조는 신뢰로 자동 환전되지 않는다
- 호송 대열이 사람만이 아니라 기록도 함께 옮기고 있다
- 건져 올린 문서 한 장의 작성일이 에이든의 출발일보다 뒤다

Reader must not know yet:

- 그 문서를 누가 왜 작성했는가
- 세렌의 전체 기능과 책임 전가의 주체
- 삭제된 증언자의 정체
- 19만 계산의 최종 오류구조
- F0가 원본 시간선이 아닐 가능성의 확정 (독자 추론 가능 시점 E220)
- 기록상자의 내용 전체와 소유 주체

Final hook:

- 구조한 기록상자 안에 에이든의 출발일보다 뒤에 작성된 문서가 있다
- 동시에 아이리스가 그를 감시한다 — 구조 자체가 그를 더 잘 보이게 만들었다
- 의미: 시간 순서가 한 장에서 어긋났고, 그것을 본 사람이 에이든뿐이 아니다
- 금지: 문서를 미래 개입의 증거로 확정, 작성자 특정, 아이리스가 문서의 뜻을 이미 아는 것으로 처리

## 7. POV / Storycraft

원본: `scene-density-map-v1.md` V1 E011 행 · `secondary-pov-and-offscreen-action-allocation-v1.md` §4–§6

- POV: 에이든 단일 근접 3인칭 (E011에는 P1·P2·P3 배치 없음)
- **Scene Density: S형 3장면**
- 배정 사유: 다리 입구·붕괴·구조로 표적 추적과 환자 구조가 갈리는 현장 3장면이다
- S형 규칙: 단일 현장 문제를 추적·해결하는 표준 3단 진행. 기관 순회나 다층 교차를 넣지 않는다
- Primary craft: 순서가 곧 인격인 구조 선택
- Secondary A: 감사받는 선행
- Secondary B: 노출로 지불하는 비용
- Hook: H2 정보 역전 + H1 물리적 귀환위험
- Reader reward: 주인공이 옳은 일을 했는데 임무와 은폐가 동시에 나빠지는 정직한 대가

## 8. Scene Values

밀도표 S형 3장면과 일치한다.

### Scene 1 — 다리 입구

- Entry: 호송을 따라가면서도 표적 경로를 잃지 않을 수 있다
- Evidence: 본부의 잔여시간 신호, 두 경로가 물리적으로 갈라지는 지형
- Exit: 두 목표가 동시에 성립하지 않음이 확정

### Scene 2 — 붕괴

- Entry: 조금 늦더라도 둘 다 건질 수 있다
- Evidence: 기우는 수레, 물로 향하는 사람과 기록상자, 사용할 수 없는 미래 장비
- Exit: 선택이 아니라 순서만 남음. 아이리스가 그 순서를 지켜본다

### Scene 3 — 강가

- Entry: 사람을 먼저 구했으니 최소한 관계는 얻었다
- Evidence: 아이리스는 감사 대신 장비의 정체를 묻고, 젖은 상자에서 작성일이 어긋난 문서가 나온다
- Choice/Exit: 에이든은 표적 추적을 반나절 포기한 대가를 확정하고, 은폐가 약해진 채 감시 아래 놓인다

## 9. Anti-Repeat

- E008의 파손 수레 수리를 반복하지 않는다. 이번 수레는 고칠 대상이 아니라 이미 무너지는 중이다
- E010의 조건 협상 구조를 반복하지 않는다. 이 회차에는 협상 상대가 없다
- E003·E009처럼 두 기록을 나란히 놓고 대조하지 않는다. 문서 한 장의 날짜가 순서를 깨는 방식으로만 처리한다
- E001의 삭제된 글자, E007의 종소리를 훅 형식으로 재사용하지 않는다
- 카운트다운 숫자를 장면마다 반복 표시하지 않는다. 시간 압박은 신호 한 번과 갈라지는 길로만 제시한다
- 구조 성공으로 아이리스의 태도가 호의로 바뀌지 않는다
- 미래 장비를 꺼내 구조를 해결하지 않는다
- 에이든이 구조를 후회하거나 정당화하는 내적 독백으로 장면을 마감하지 않는다

## 10. Active State / Props

- 본부 잔여시간 신호 — 이 회차의 유일한 본부 접촉면
- 붕괴한 다리와 환자 수레
- 기록상자 — 신규 활성 물건. 내용 전체는 미공개
- 작성일이 어긋난 문서 한 장
- 물에 노출된 미래 장비 — 은폐 등급 하락 상태로 이월
- 기사단 치료보조자 명부 등재 — 배경상태로 유지
- 귀환석 — 배경상태. 귀환표식은 아이리스 동의 전까지 불안정

기록상자가 E012 이후 재등장할 경우 A10이 prop/relic 승격 여부를 판정한다.

## 11. State Mutation Plan

E011 종료 시 기록:

- 표적 접촉 가능 시간 반나절 감소 확정
- 미래 장비 은폐 등급 하락과 노출된 품목 범위
- 구조된 인원과 구조하지 못한 대상의 구분
- 기록상자의 확보 상태와 접근 권한
- 작성일 모순 문서의 보관 위치와 열람자
- 아이리스의 감시 개시와 질문 내용
- 본부 신호에 대한 에이든의 미응답·지연 사실

## 12. Ready Verdict

- Authority: RESOLVED
- Domain Readiness: READY
- Storycraft companion: REQUIRED / prepared separately
- POV: READY
- Scene density conformance: S형 3장면 = 설계 3장면 · PASS
- S0: 0
- S1: 0

E011 Storycraft Manifest와 E010 상태기록 확인 뒤 A18 호출 가능.
