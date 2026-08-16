# Episode Context Pack — E018

Status: D10 READY  
Episode: E018  
Title: 하루가 줄어든 증거  
Compiled By: A21 Context Pack Compiler  
Reference: `agent/1c-evidence-subact`

> 이 CP는 정본이 아니다. 충돌 시 원본 정본과 권한계층을 따른다.

## 1. Authority / Architecture

Required sources:

- [`/AI_PROJECT.md`](../../../AI_PROJECT.md)
- [`docs/00_project/canon-constitution-v1.md`](../../../docs/00_project/canon-constitution-v1.md)
- [`docs/00_project/canon-naming-pack-v1.md`](../../../docs/00_project/canon-naming-pack-v1.md)
- [`docs/00_project/terminology-and-addressing-clarification-v1.md`](../../../docs/00_project/terminology-and-addressing-clarification-v1.md)
- [`docs/00_project/decision-log.md`](../../../docs/00_project/decision-log.md) — DEC-016·017·018·020·021
- [`docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md`](../../../docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md) — E018 행
- [`docs/10_story_architecture/detail/v01-scene-ready-design-v1.md`](../../../docs/10_story_architecture/detail/v01-scene-ready-design-v1.md) — Subact 1C, E018 절
- [`docs/10_story_architecture/subact-causal-matrix-v1.md`](../../../docs/10_story_architecture/subact-causal-matrix-v1.md) — 1C 행 Resolution·Cost
- [`docs/10_story_architecture/scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) — V1 E018 배정
- [`docs/10_story_architecture/location-world-crosswalk-v1.md`](../../../docs/10_story_architecture/location-world-crosswalk-v1.md) — V01 1C
- [`docs/05_characters/cast-canon-index-v2.md`](../../../docs/05_characters/cast-canon-index-v2.md) — C01·C03·C06·C10·C12·C26
- [`docs/05_characters/voice-relationship-state-bible-v1.md`](../../../docs/05_characters/voice-relationship-state-bible-v1.md)
- [`docs/03_systems/time-travel-ontology-v1.md`](../../../docs/03_systems/time-travel-ontology-v1.md) — Return, Timeline Model, Temporal Debt
- [`docs/02_world/atlas-region-dossiers-v1.md`](../../../docs/02_world/atlas-region-dossiers-v1.md) — R05 생활·정치
- [`docs/11_mystery/mystery-reinforcement-ladder-v1.md`](../../../docs/11_mystery/mystery-reinforcement-ladder-v1.md) — M01·M02
- [`docs/12_losses/permanent-loss-lock-v1.md`](../../../docs/12_losses/permanent-loss-lock-v1.md)
- [`.agent/context-packs/episodes/E017-context-pack.md`](E017-context-pack.md)

Episode function:

- Grand Act: GA I — 잘못된 치료
- Volume: V1 — 회색 종이 울리는 날
- Subact: 1C — 증거가 맞고 진실이 틀릴 때
- Beat: 국소 해결
- Goal: 왕실 기록상 혐의는 성립하지만 환자 기억과 날짜가 모순됨을 확정한다
- Opposition: 검증 요청 자체가 본부에서 오염 신호로 처리된다
- Choice: 본부와 현지 어느 쪽도 완전히 믿지 않는다
- Cost: 추가 조사와 안전 귀환 중 하나만 가능해진다
- State Change: 1C가 ‘증거 확보’에서 ‘양방향 불신’으로 닫힌다
- Hook: 귀환창이 하루 줄어들고, 그 직후 왕실군이 은신처 외곽 환자 수레에 불을 놓는다

## 2. E017 Carryover

### 에이든

- 세렌을 제압했으나 죽이지 않았고 제거 준비는 유지 중
- 명령의 원문을 제시하지 못했다
- 세렌의 기억채취 자백과 그 축소분을 알고 있다
- 세렌이 요구한 기록 계보 항목이 검증 목록이 된다

### 세렌 바일

- 생존. 자기 방식의 피해를 축소한 상태로 남아 있다
- 조직의 남은 기록과 주민 대피 계획을 계속 붙잡고 있다

### 아이리스 네르

- E012 조건 유지 — 환자를 표적 접근 수단으로 쓰면 귀환표식을 끊는다
- 환자 수레와 대피 일정이 그의 직접 책임 영역이다

### 본부

- E012에서 제거 시한을 앞당김
- E018에서 처음으로 에이든의 요청을 거부가 아닌 ‘신호 분류’로 처리한다

### 물질 상태

- 사건 발생 전 날짜로 작성된 왕실 보고서와 덧씌운 피해 수치 (E014)
- 삭제예정지 주민·족보 목록 (E015)
- 세렌의 암호 조각 — 미해독 (E016)
- 귀환용 응급자원 감소분 (E014)

## 3. Time / Location

- Era: N — 건국력 640년대, 서부 잿빛 변경
- 시점: E017 대화 직후. 왕실 포위와 귀환창이 동시에 좁아지는 구간
- Main locations:
  1. 기록 비교대 — 혐의 항목 대조
  2. 환자 구역 — 발생일과 몸의 시간 확인
  3. 통신 지점 — 본부 응답 수신
- 이동은 은신처 내부와 외곽 사이로 제한된다
- 1C 주무대는 crosswalk V01 기준 `두 역사의 라베른·절검의 언덕`이며 세부 장소명은 SOFT LOCK
- 절검의 언덕은 1D 구간 배정 장소이므로 여기서 소모하지 않는다

## 4. Verification Package

Sources:

- V1 scene-ready design E018 절
- [`docs/11_mystery/mystery-reinforcement-ladder-v1.md`](../../../docs/11_mystery/mystery-reinforcement-ladder-v1.md)
- [`docs/03_systems/time-travel-ontology-v1.md`](../../../docs/03_systems/time-travel-ontology-v1.md)

### 성립하는 혐의 — 행위 축

- 금지된 시간·주소 의식 시행
- 동의 없는 기억채취
- 명령 불복종

이 세 항목은 사실로 확정된다. 왕실 기록이 이 부분에서 날조가 아니라는 점이 회차 전반부의 결론이다.

### 성립하지 않는 인과 — 결과 축

- 환자 발생일
- 보고서 작성일
- 마을 소거일

세 날짜가 공식 설명과 맞지 않는다. 어긋남의 방향이 하나가 아니라 서로 다르다는 점이 핵심이다. 하나의 날짜가 다른 하나보다 앞선다는 단일 모순으로 축약하지 않는다.

### 확정하지 않는 것

- 누가 날짜층을 위조했는가 — M02 사다리의 E061 항목이다
- 마나열병이 감염이 아니라는 결론 — M01 사다리의 E176 항목이다
- 세렌이 무엇을 늦추고 있는가 — E072 항목이다

### 본부 통신의 제도 반응

- 에이든의 검증 요청은 거절되지 않는다. 분류가 바뀐다
- 시간오염 신호로 처리되며 그 결과 귀환창이 하루 단축된다
- 이것은 악의적 방해가 아니라 절차의 자동 반응으로 제시한다. 기관을 평면 악역으로 만들지 않는다
- 귀환 관련 정본: 출발 당시의 미래로 돌아간다는 보장이 없고, 귀환은 현재 존재하는 고정석으로 연결된다

## 5. Character State

### 에이든 로엔

- 목표: 실행 전에 인과를 확인한다
- 방법: 혐의와 인과를 같은 저울에 올리지 않고 따로 판정한다
- 압박: 검증 요청이 자신의 신뢰도를 깎는 신호로 되돌아온다
- 오류 가능성: 양쪽을 다 못 믿게 되자 결국 시한에 판단을 맡긴다
- 금지: 본부 전체를 적으로 규정, 세렌 무죄 확정, 현지 편입 선언

### 아이리스 네르

- 독립 목표: 환자 수레와 대피 일정. 미래의 숫자와 중앙의 수동태를 공격한다
- 기능: 문서의 시간이 아니라 사람의 시간을 대는 유일한 화자
- 금지: 에이든의 양심 역할로만 배치, 감정적 호소로 국면 전환

### 환자 증인

- 발생일·증상 순서·기억의 모순을 몸으로 증언한다
- 이름 없는 숫자로만 등장시키지 않는다
- 마나열병 여부를 확정 진단하는 대사를 만들지 않는다
- C26 아벨 네르가 V1 첫 핵심권 환자 증인 인물이나 E018 배치는 정본 미지정이므로 A08 확인 필요

### 본부 통신 담당

- 새 핵심 이름을 즉석 확정하지 않는다
- 규정을 읽는 사람이지 음모의 실행자가 아니다

## 6. Mystery / Information Ceiling

Active mysteries:

- M02 세렌은 왜 창시자로 기록됐는가 — 혐의는 성립, 인과는 불성립으로 갈라진다. 위조 주체 확정 금지
- M01 마나열병은 전염병인가 — 환자 발생일이 문서와 어긋난다는 사실만 남긴다. 사다리 확정 시점은 E176
- M05 빈 세금장부 — 마을 소거일 항목으로 배경 강화
- M12 최종 흑막 — 사다리 첫 단은 E070. 개인 흑막 암시 금지

Reader may know:

- 세렌의 불법행위 세 항목은 실제다
- 그런데 결과의 날짜들이 서로 다른 방향으로 어긋난다
- 검증을 요청하는 행위 자체가 본부에서 위험 신호로 분류된다
- 에이든은 이제 양쪽 어디에도 완전한 근거를 두지 못한다

Reader must not know yet:

- 세렌이 지방 소거를 늦췄다는 전체 기능
- 날짜층을 위조한 주체
- 삭제된 증언자의 정체
- 19만 생존모델의 최종 오류구조
- 세렌의 생체인장과 서부 봉쇄의 관계 — E019 소관

Final hook:

- 귀환창이 하루 줄어들고, 그 직후 왕실군이 은신처 외곽 환자 수레에 불을 놓는다
- 의미: 남은 시간이 줄어든 바로 그 순간에 그 시간을 써야 할 이유가 하나 더 생긴다
- 금지: 방화를 세렌의 자작극으로 처리, 방화범 정체를 이 회차에서 반전으로 쓰기

## 7. POV / Storycraft

- POV: 에이든 단일 근접 3인칭
- Scene Density: **S형 3장면** — [`scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) V1 E018
- 배정 사유: 기록 비교·인과 비교·본부 통신으로 검증 결과와 귀환창 단축을 정리하는 회차다
- Primary craft: 혐의와 인과의 분리 검증
- Secondary A: 몸의 시간과 종이의 시간
- Secondary B: 검증 요청이 처벌로 되돌아오는 제도 반응
- Hook: H4 제도변화 + H1 물리적 위협
- Reader reward: 표적이 유죄이면서 동시에 원인이 아닐 수 있다는 구조를 독자가 직접 조립하는 경험

## 8. Scene Values

### Scene 1 — 기록 비교대

- Entry: 대화 뒤에도 혐의는 흔들릴 것이다
- Evidence: 금지의식·기억채취·명령불복종 세 항목이 모두 사실로 확인된다
- Exit: 왕실 기록은 이 부분에서 날조가 아니다

### Scene 2 — 환자 구역

- Entry: 혐의가 사실이면 재앙의 원인도 그다
- Evidence: 환자 발생일·보고서 작성일·마을 소거일이 서로 다른 방향으로 어긋난다. 문서가 아니라 환자의 몸과 증상 순서가 첫 번째 시계다
- Exit: 행위는 유죄인데 결과의 인과가 서지 않는다

### Scene 3 — 통신 지점

- Entry: 본부에 검증을 요청하면 시간을 얻을 수 있다
- Evidence: 요청이 시간오염 신호로 분류되고 귀환창이 하루 단축된다
- Exit: 어느 쪽도 믿지 못하는데 결정을 미룰 시간도 사라진다. 외곽에서 불이 오른다

## 9. Anti-Repeat

- E003·E013·E014의 ‘두 문서를 나란히 놓고 대조’ 이미지 반복 금지 — 이번 비교의 첫 축은 종이가 아니라 환자의 몸이다
- E003 훅 구조 반복 금지 — 날짜 하나가 다른 하나보다 앞선다는 단일 모순으로 축약하지 않는다
- E001의 삭제된 글자 훅 금지
- E002의 기관 순회, E016의 세력 교차 구조 재사용 금지
- E017의 단일 공간 대화 구조를 반복하지 않는다
- 본부를 순수 악역으로 처리해 갈등을 단순화하지 않는다
- 환자를 이름 없는 숫자로만 제시하지 않는다
- ‘사실 모든 기록이 가짜였다’ 반전 금지

## 10. Active State / Props

- 왕실 혐의 세 항목의 검증 결과
- 사건 발생 전 날짜로 작성된 보고서 (E014)
- 삭제예정지 주민·족보 목록 (E015)
- 환자 발생일 기록과 증상 관찰 순서
- 본부 통신의 신호 분류 응답
- 귀환창 잔여 — 하루 단축 확정
- 불타는 환자 수레 — 회차 종료 이미지
- 세렌의 암호 조각 — 미해독 배경 상태

혐의 검증 결과표가 V3 재검토에서 재등장하므로 A13이 상태 보존을 확인한다.

## 11. State Mutation Plan

E018 종료 시 기록:

- 성립한 혐의 세 항목과 그 근거
- 성립하지 않는 인과 세 날짜와 어긋난 방향
- 본부 검증 요청 상태와 신호 분류 결과
- 귀환창 잔여 — 하루 단축 반영
- 추가 조사와 안전 귀환의 배타 관계 확정
- 에이든의 본부·현지 양방향 불신 수준
- 환자 수레 피해와 아이리스의 대응 개시
- Subact 1C 종료 상태 — 공식 증거 확보, 인과 해석 불확실

## 12. Ready Verdict

- Authority: RESOLVED
- Domain Readiness: READY
- Storycraft companion: REQUIRED / prepared separately
- POV: READY
- Scene Density: S형 3장면 확정 · 설계 3비트와 1:1 대응
- Subact exit alignment: 1C Resolution·Cost와 일치
- S0: 0
- S1: 0

E018 Storycraft Manifest와 E017 상태기록 확인 뒤 A18 호출 가능. 1D 진입 전 Subact 1C 종료 감사를 병행한다.
