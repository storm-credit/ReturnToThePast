# Episode Context Pack — E005

Status: D10 READY  
Episode: E005  
Title: 제거와 차단  
Compiled By: A21 Context Pack Compiler  
Reference: `agent/e004-finalize-status`

> 이 CP는 정본이 아니다. 충돌 시 원본 정본과 권한계층을 따른다.

## 1. Authority / Architecture

Required sources:

- [`/AI_PROJECT.md`](../../../AI_PROJECT.md)
- [`docs/00_project/canon-constitution-v1.md`](../../../docs/00_project/canon-constitution-v1.md)
- [`docs/00_project/canon-naming-pack-v1.md`](../../../docs/00_project/canon-naming-pack-v1.md)
- [`docs/00_project/terminology-and-addressing-clarification-v1.md`](../../../docs/00_project/terminology-and-addressing-clarification-v1.md)
- [`docs/00_project/decision-log.md`](../../../docs/00_project/decision-log.md) — DEC-016·017·018·020·021
- [`docs/00_project/GATE_STATUS.md`](../../../docs/00_project/GATE_STATUS.md)
- [`docs/10_story_architecture/detail/v01-scene-ready-design-v1.md`](../../../docs/10_story_architecture/detail/v01-scene-ready-design-v1.md) — E005 절
- [`docs/10_story_architecture/detail/v01-d9-correction-overlay.md`](../../../docs/10_story_architecture/detail/v01-d9-correction-overlay.md) — §4 E005 보강
- [`docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md`](../../../docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md) — E005 행
- [`docs/10_story_architecture/subact-causal-matrix-v1.md`](../../../docs/10_story_architecture/subact-causal-matrix-v1.md) — 1A
- [`docs/10_story_architecture/location-world-crosswalk-v1.md`](../../../docs/10_story_architecture/location-world-crosswalk-v1.md) — V01 1A
- [`docs/10_story_architecture/scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) — V1 E005 = S · 3장면
- [`docs/05_characters/voice-relationship-state-bible-v1.md`](../../../docs/05_characters/voice-relationship-state-bible-v1.md)
- [`docs/11_mystery/mystery-reinforcement-ladder-v1.md`](../../../docs/11_mystery/mystery-reinforcement-ladder-v1.md)
- [`.agent/context-packs/episodes/E004-context-pack.md`](E004-context-pack.md)

Episode function (registry E005 행 + v01 설계 E005 절):

- Grand Act: GA I — 잘못된 치료
- Volume: V1 — 회색 종이 울리는 날
- Subact: 1A — 출발표에 서명하는 사람
- Beat: 선택
- Goal: 귀환 가능성을 높이기 위해 임무 목표를 좁히고 최종 수락한다
- Opposition: 피해 없는 정답이 없음 / 목표를 좁힐수록 현지에서 할 수 있는 일이 사라짐 / 리아의 사적 경고
- Choice: 세렌 바일 제거와 연대기 접근 차단 두 목표로 확정하고 대규모 구조·조사는 제외
- Cost: 현지에서 사람을 구할 권한을 스스로 삭제하고, 검증되지 않은 경고를 보고하지도 버리지도 못한 채 소지
- State Change: 조건부 서명자가 목표가 확정된 실행자로 바뀜
- Hook: 출발 인장에 표적의 진명이 아닌 다른 이름이 잠깐 비침

## 2. E004 Carryover

출처: [`E004-context-pack.md`](E004-context-pack.md) §11

- 에이든: 누락 위험 인지 책임서에 서명 완료. 살아 있는 현지 앵커 없는 고위험 출발 수용
- 리아: 앵커 공백을 근거로 연기를 요구했으나 기각. 의견은 기록에만 남음. 감사표식 유지
- 명단: 하루 지연 시 약품 중단 대상 명단이 확정 보관됨
- 좌표: 목표 시대의 귀환점 목록이 한 칸씩 줄어드는 것이 관측됨
- 귀환석: 3갈래 균열 / 체류 5시간 17분 / 최대 오착 18km / 강제복귀 1회
- 현재 피해: 제칠 방벽 구조 가능 인원과 서부 구조대 31명 상태는 배경으로만 환기

E005는 E004의 명단을 다시 읽지 않는다. 명단은 이미 지불된 값이며, 이 화의 문제는 남은 시간으로 무엇을 할지다.

## 3. Time / Location

- Date: 건국력 664년 장야월 18일 또는 그 직후, E004 직후
- Era: F0
- 에이든: 41세 / 주관적 누적일 0
- Main locations:
  1. 전술실
  2. 리아의 기록대
  3. 출발실 앞 복도
- 이동은 중앙 복합시설 내부
- E005 안에서 실제 출발은 일어나지 않는다. 출발실 문 앞까지만 간다

## 4. 목표 확정과 귀환 가능성

Sources:

- v01 설계 E005 절
- [`docs/03_systems/time-travel-ontology-v1.md`](../../../docs/03_systems/time-travel-ontology-v1.md)
- [`.agent/context-packs/episodes/E002-context-pack.md`](E002-context-pack.md) §5 귀환석 규칙
- [`docs/10_story_architecture/detail/v01-d9-correction-overlay.md`](../../../docs/10_story_architecture/detail/v01-d9-correction-overlay.md) §4

### 확정 목표 두 개

1. **세렌 바일 제거**
2. **연대기 접근 차단** — 표적이 접근·보존하려는 기록계보로의 접근을 끊는 것

제외되는 것:

- 대규모 구조
- 광범위 현지 조사
- 환자 증언 확보 (E002에서 부목표였던 항목이 이 화에서 임무 밖으로 내려감)

### 교환 규칙 (E002 확정 사항의 적용)

- 목표 축소는 체류시간과 귀환확률을 높이지만 조사·구조 범위를 줄인다
- 강제복귀는 사실상 1회이며 오착 수정에 쓰면 귀환불능 위험
- 목표 축소 권고는 겁쟁이 행동이 아니라 실제 귀환확률 관리다

### 금지

- ‘연대기’의 최종 정체·소재·권수를 이 화에서 확정 (M15는 E016·E165·E230·E332로 진행)
- 차단 방법을 구체적 시술·주문으로 신설
- 목표 축소를 본부의 음모로 단정

## 5. Character State

### 에이든 로엔

- 목표: 돌아올 수 있는 임무로 범위를 줄이되, 줄인 만큼 무엇을 버리는지 스스로 말한다
- 감정 전환 (설계 Emotional Turn): 용감해서가 아니라 남겨질 사람들의 눈을 피하지 못해 서명했음을 인정
- 습관: “목표·출구·비용” 순서 / 결론은 짧게
- 오류 가능성: 목표를 좁히면 책임도 좁아진다고 느낌
- 금지: 목표 축소에 반발해 임무를 거부, 리아의 경고로 즉시 태도 반전

### 리아 세른

- 역할: 공식 보고서가 아닌 개인 경고를 암호로 남긴다
- 정본 경고 문장(설계 확정): `기록이 틀렸다는 뜻이 아니라 기록이 살아남은 이유를 보라.`
- 이 경고는 증거가 아니라 판단 기준의 재배치다. 새 사실을 주지 않는다
- 제한: 감사표식·원본층 접근 불가 / “기억한다”와 “증명할 수 있다”를 구분
- 금지: 예언자 말투, 조작 주체 인지, 에이든 대신 결정, 경고를 애정 고백으로 전환

### 전술·귀환 담당

- 새 핵심 이름을 즉석 확정하지 않음
- 수치·균열·오차범위를 명확히 말하되 정답을 아는 예언자가 아님
- 목표 축소를 권고하되 임무 자체의 정당성은 판정하지 않음

### 세렌 바일

- 여전히 기록·인장·목표명으로만 등장
- 유죄·무죄 확정 금지 / 영구 사망은 E024 부근에서 잠긴다 (permanent-loss-lock L001)

## 6. Mystery / Information Ceiling

Active mysteries:

- M02 세렌은 왜 재앙 창시자로 기록됐는가
- M12 조작을 한 한 명의 흑막이 있는가 — 개인 흑막 지목 금지
- M15 최초 연대기는 어디 있는가 — 목표 문장으로만 접촉, 사다리 진입은 E016

Reader may know:

- 임무 목표가 두 개로 좁혀졌고 그 대가로 구조·조사가 버려졌다
- 리아는 반증을 갖고 있지 않으며, 대신 기록을 읽는 방향을 바꾸라고 말한다
- 출발 인장이 표적의 진명과 다른 이름을 한 번 내보인다

Reader must not know yet:

- 다른 이름이 누구인지, 어느 시간층에서 왔는지
- 세렌이 지방 소거를 늦췄다는 전체 기능
- 조작 주체와 삭제된 증언자의 정체
- 19만 모델의 최종 오류구조
- ‘연대기’가 한 권이 아니라는 사실

Final hook:

- 출발 인장에 표적의 진명이 아닌 다른 이름이 잠깐 비침
- 정본 해석 (overlay §4): 새 예언이 아니라 **세렌의 개인주소와 사건주소가 일치하지 않는다는 전조**
- 독자가 품게 되는 의심: 표적을 죽이면 사건기능도 함께 사라지는가
- 금지: 다른 이름을 인물로 확정, 리아가 그 이름을 알아봄, 새 시간법칙 추가

## 7. POV / Storycraft

- POV: 에이든 단일 근접 3인칭
- Scene Density: **S형 3장면** — [`scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) V1 표
- Primary craft: 목표 축소의 교환 — 버리는 것을 이름으로 말하기
- Secondary A: 증거가 아닌 경고의 보관
- Secondary B: 동기의 자기 폭로
- Hook: H2 정보 역전 — 단, E001의 ‘지워진 흔적이 되살아난다’가 아니라 **지금 작동 중인 장치가 다른 판독을 내놓는다**
- Reader reward: 임무가 좁아질수록 주인공이 더 위험해진다는 역설

## 8. Scene Values

S형 3장면.

### Scene 1 — 전술실

- Entry: 목표를 넓게 유지해야 현지에서 더 많이 확인할 수 있다
- Evidence: 균열 귀환석, 체류 5시간 17분, 오착 18km, 강제복귀 1회
- Turn: 에이든이 목표를 줄이는 대신 무엇이 임무에서 삭제되는지 항목으로 확인
- Exit: 두 목표만 남고 구조·조사·환자 증언이 임무 밖으로 내려감

### Scene 2 — 리아의 기록대

- Entry: 리아가 공식 반증을 낼 것이라는 기대
- Evidence: 감사표식 아래에서 공식 경로가 막혀 있음 / 리아는 확정할 수 없는 것을 확정하지 않음
- Turn: 리아가 보고서 대신 암호화된 개인 경고를 남김
- Exit: 새 사실 없이 판단 기준만 바뀜. 에이든은 반박도 채택도 못 함

### Scene 3 — 출발실 앞

- Entry: 경고를 받았으니 임무를 미룰 근거가 생겼다
- Evidence: E004에서 이미 서명한 지연비용 / 경고는 기록이 아니라 문장일 뿐
- Choice: 경고를 지우지도 제출하지도 않고 장갑 안쪽에 숨긴 채 임무를 거부하지 않음
- Exit: 출발 인장에 다른 이름이 잠깐 비침

## 9. Anti-Repeat

- E001처럼 삭제된 글자가 회색으로 되살아나는 훅을 반복하지 않음. E005의 이름은 삭제 흔적이 아니라 **현재 판독 결과**다
- E002처럼 여섯 기관을 순회하며 조건을 듣는 구성 금지. 이 화의 협상 상대는 목표 범위 하나다
- E002의 귀환석 토양·균열 검사를 다시 장면화하지 않음. 수치는 인용만 한다
- E003처럼 압수품·문서를 나란히 대조하지 않음
- E004처럼 명단을 다시 낭독하지 않음. 명단은 이미 지불된 값이다
- 리아의 경고를 결정적 반증으로 만들지 않음
- 리아의 경고를 로맨스 고백으로 전환하지 않음
- 에이든이 경고를 즉시 상부에 보고하거나 즉시 파기하는 이분법 금지
- ‘사실 목표 축소는 본부의 함정이었다’ 반전 금지

## 10. Active State / Props

- 출발 인장
- 리아의 암호화된 개인 경고 (장갑 안쪽)
- 목표 확정서 — 제거·차단 2항목
- 균열 귀환석 상태표
- E004의 책임서와 명단은 배경 상태로만 유지

장갑 안쪽 경고는 E006 통과·E007 이후 현지 소지품 판정과 직접 연결되므로 A10 prop 등재 대상이다.

## 11. State Mutation Plan

E005 종료 시 기록:

- 확정 목표 2항목과 임무에서 삭제된 항목 목록
- 목표 축소 후 갱신된 체류창·귀환확률
- 리아 경고의 물리적 형태·소지 위치·해독 여부
- 에이든의 자기 동기 인정 상태
- 출발 인장에서 관측된 다른 이름의 기록 여부와 보고 여부
- 성당 재검사 및 최종 정족수 진행상태

## 12. Ready Verdict

- Authority: RESOLVED
- Domain Readiness: READY
- Storycraft companion: REQUIRED / prepared separately
- POV: READY
- Scene density: S · 3장면 — 설계 장면 수와 일치
- S0: 0
- S1: 0

E005 Storycraft Manifest와 E004 상태기록 확인 뒤 A18 호출 가능.
