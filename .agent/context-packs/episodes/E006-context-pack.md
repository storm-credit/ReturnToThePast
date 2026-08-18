# Episode Context Pack — E006

Status: D10 READY  
Episode: E006  
Title: 빗나간 도착  
Compiled By: A21 Context Pack Compiler  
Reference: `agent/e005-finalize-status`

> 이 CP는 정본이 아니다. 충돌 시 원본 정본과 권한계층을 따른다.

## 1. Authority / Architecture

Required sources:

- [`/AI_PROJECT.md`](../../../AI_PROJECT.md)
- [`docs/00_project/canon-constitution-v1.md`](../../../docs/00_project/canon-constitution-v1.md)
- [`docs/00_project/canon-naming-pack-v1.md`](../../../docs/00_project/canon-naming-pack-v1.md)
- [`docs/00_project/terminology-and-addressing-clarification-v1.md`](../../../docs/00_project/terminology-and-addressing-clarification-v1.md)
- [`docs/00_project/decision-log.md`](../../../docs/00_project/decision-log.md) — DEC-016·017·018·020·021
- [`docs/00_project/GATE_STATUS.md`](../../../docs/00_project/GATE_STATUS.md)
- [`docs/10_story_architecture/detail/v01-scene-ready-design-v1.md`](../../../docs/10_story_architecture/detail/v01-scene-ready-design-v1.md) — E006 절, Subact 1A Exit State
- [`docs/10_story_architecture/detail/v01-d9-correction-overlay.md`](../../../docs/10_story_architecture/detail/v01-d9-correction-overlay.md) — §5 E006 보강, §6 아이리스 역할, §8 금지
- [`docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md`](../../../docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md) — E006 행
- [`docs/10_story_architecture/subact-causal-matrix-v1.md`](../../../docs/10_story_architecture/subact-causal-matrix-v1.md) — 1A→1B
- [`docs/10_story_architecture/location-world-crosswalk-v1.md`](../../../docs/10_story_architecture/location-world-crosswalk-v1.md) — V01 1A·1B, 이동·장면 감사
- [`docs/10_story_architecture/scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) — V1 E006 = X · 5~6장면 **고정**
- [`docs/11_mystery/mystery-reinforcement-ladder-v1.md`](../../../docs/11_mystery/mystery-reinforcement-ladder-v1.md) — M16
- [`docs/12_losses/permanent-loss-lock-v1.md`](../../../docs/12_losses/permanent-loss-lock-v1.md)
- [`.agent/context-packs/episodes/E005-context-pack.md`](E005-context-pack.md)

Episode function (registry E006 행 + v01 설계 E006 절):

- Grand Act: GA I — 잘못된 치료
- Volume: V1 — 회색 종이 울리는 날
- Subact: 1A — 출발표에 서명하는 사람 / **Subact 종료 회차**
- Beat: 국소 해결
- Goal: 여섯 기관의 최소 정족수로 출발해 Era N 서부에 도달한다
- Opposition: 낮은 좌표정확도, 낮은 귀환안정도, 살아 있는 현지 앵커 부재, 등록 불가 물품
- Choice: 불완전 기록과 짧은 귀환창을 받아들이고 통과한다
- Cost: 약 18km 오착, 장비 일부 시간 오차로 잠김, 신분문서가 현지 법과 불일치, 강제복귀 1회를 오착 수정에 쓰면 귀환불능
- State Change: ‘출발 승인 문제’였던 임무가 ‘현지 생존 문제’로 바뀐다
- Exit State: Era N 도착 성공, 계획된 현지 앵커 없음
- Hook: 멀리서 울린 회색 종이 에이든의 귀환석과 같은 박자로 진동

## 2. E005 Carryover

출처: [`E005-context-pack.md`](E005-context-pack.md) §11

- 목표: 세렌 바일 제거 / 연대기 접근 차단 2항목 확정. 구조·조사·환자 증언은 임무에서 삭제
- 소지: 리아의 암호화된 개인 경고가 장갑 안쪽에 있음. 미보고 상태
- 관측: 출발 인장에서 표적의 진명이 아닌 다른 이름이 한 번 비쳤고 보고되지 않음
- 서명: E004의 누락 위험 인지 책임서 유효
- 앵커: 역사주소 앵커 성립 / 살아 있는 현지 앵커 없음
- 귀환석: 3갈래 균열 / 체류 5시간 17분 / 최대 오착 18km / 강제복귀 1회
- 좌표: 목표 시대의 귀환점 목록이 줄어드는 중

## 3. Time / Location

- 출발 시점: 건국력 664년 장야월 18일 또는 그 직후, F0
- 에이든: 41세 / 주관적 누적일 0 → 도약 직후에도 주관적 하루 미만
- 도착 시대: Era N, 잿빛 변경 서부. **정확한 도착 연·월·일은 정본에 없다.** 원고에서 확정하지 말고 A13 연대 정본 판정을 받는다
- Main locations:
  1. 동기화실
  2. 출발대 등록구역
  3. 통과 구간
  4. 오차 구간
  5. 서부 격리촌 외곽 진흙 수로
  6. 수로 위 들판 — 종소리 도달 지점
- 이동 규칙 (location crosswalk 이동·장면 감사):
  - 시간도약을 공간이동과 동일하게 처리하지 않는다
  - 도착 뒤 격리촌까지의 현지 이동을 생략하지 않는다. E006은 **격리촌 안에 들어가지 않고 외곽에서 끝난다**
  - 18km는 지도상 거리이며 수로·진흙·부상 상태가 실제 이동시간을 늘린다

## 4. 도약 판정과 실현되는 위험

Sources:

- [`docs/10_story_architecture/detail/v01-d9-correction-overlay.md`](../../../docs/10_story_architecture/detail/v01-d9-correction-overlay.md) §3·§5·§8
- [`docs/03_systems/time-travel-ontology-v1.md`](../../../docs/03_systems/time-travel-ontology-v1.md)
- [`.agent/context-packs/episodes/E002-context-pack.md`](E002-context-pack.md) §4·§5

### 판정표 (overlay §5)

| 항목 | 판정 |
|---|---|
| 역사주소 앵커 | 성립 |
| 살아 있는 현지 앵커 | 없음 |
| 법적 승인 | 긴급 최소정족수 |
| 좌표정확도 | 낮음 |
| 귀환안정도 | 낮음 |

### 역사주소의 구성 (overlay §1)

세렌 바일 사건기록 + 회색 종 잔향 + 서부 세무층. 인물 하나가 아니라 사건기록·물질층·공공기록이 서로 가리키는 범위다.

### 결과

- 도약 자체는 성공한다
- 공간오차·장비잠김·신분실패가 발생한다
- 이것은 시간법칙 위반도 작가편의도 아니라 **E004에서 받아들인 위험의 직접 결과**다 (overlay §8 금지)

### 여섯 승인의 기능 (E002 확정)

1. 왕좌 — 법적 출발 승인·국가 책임
2. 성당(종탑) — 달력·몸·계절 동기화
3. 관측탑 — 시간·공간 좌표와 오차
4. 대기록소 — 역사주소·표적 기록 검증
5. 앙카 귀환다리 — 귀환석·복귀창·인원·소지품 등록
6. 현장요원 — 위험인지·현장행동·책임 동의

E006에서는 이 여섯을 강의로 순회하지 않는다. 각 담당이 **자기 항목만 확인하고 통과시키는 짧은 확인 행위**로만 나타난다.

## 5. Character State

### 에이든 로엔

- 목표: 도착해서 임무 시계를 시작시킨다
- 통과 중 상태: 좌표 붕괴와 몸의 부담을 기능적으로 감당. 감각 나열이 아니라 확인 절차로 표현
- 도착 후 즉시 과제: 체온·장비·위치가 아니라 **이 화에서는 위치 확인과 신분문서 판정까지만**
- 오류 가능성: 강제복귀 1회를 오착 수정에 쓰고 싶은 충동
- 금지: 도약 중 각성·환상 계시, 도착 즉시 현지인과 접촉

### 리아 세른

- 출발 전 마지막 전달을 시도하나 통과 중 **경고가 중간에 끊긴다**
- 이후 F0에 남는다. E006 이후 직접 등장하지 않는다
- 금지: 통과 중 텔레파시적 교신, 마지막 고백

### 여섯 기관 담당

- 기능으로만 등장하며 새 핵심 이름을 즉석 확정하지 않는다
- 어느 한 명도 방해자·배신자로 지정하지 않는다
- 각자 다른 실패를 막는 사람들이며 이번에는 그 방어선이 부족하다

### 아이리스 네르

- **E006에 등장하지 않는다** (overlay §6)
- 출발 전에 확보된 인물이 아니라 도착 뒤 만나는 살아 있는 현지 앵커이며, 회색 종과 귀환석의 공명을 보고 독자적으로 추적을 시작한다
- 금지: 에이든을 기다린 운명적 인물로 변경, E006에서 미리 얼굴을 보임

## 6. Mystery / Information Ceiling

Active mysteries:

- M16 회색 종은 무엇을 감지하는가 — 귀환석과의 공명이 처음 관측됨
- M04 F0 귀환좌표는 남아 있는가 — 오차·귀환점 소실이 배경으로 이어짐
- M02 세렌은 왜 재앙 창시자로 기록됐는가 — 인장의 다른 이름이 미해결로 유지

Reader may know:

- 최소 정족수 출발은 안전 승인이 아니라 위험 수용이다
- 오착·장비잠김·신분실패는 E004의 선택에서 나왔다
- 회색 종과 귀환석이 같은 박자로 반응한다

Reader must not know yet:

- 종이 무엇을 감지하는지 (추론 가능 시점은 E092)
- 세렌의 전체 기능과 지방 소거 지연
- 기록을 뒤집은 주체와 삭제된 증언자의 정체
- 19만 모델의 최종 오류구조
- 종과 귀환석 공명의 원리, 그리고 누가 그 반응을 보고 있는지

Final hook:

- 멀리서 울린 회색 종이 에이든의 귀환석과 같은 박자로 진동
- 금지: 원리 설명, 종을 유물·열쇠로 격상, 아이리스의 등장으로 즉시 회수

## 7. POV / Storycraft

- POV: 에이든 단일 근접 3인칭
- Scene Density: **X형 5~6장면** — [`scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) V1 표에서 **고정**. 본 CP는 **6장면**으로 설계
- Primary craft: 절차의 순차 붕괴 — 통과한 항목이 하나씩 실패로 되돌아옴
- Secondary A: 등록되는 것과 등록되지 않는 것
- Secondary B: 몸으로 지불하는 통과 (감각 나열 금지, 기능 서술)
- Hook: H1 물리·좌표 위험 + H2 정보 역전
- Reader reward: Subact 1A에서 서명한 위험이 정확히 그 항목대로 실현되는 인과의 만족

## 8. Scene Values

X형 6장면. 3장면으로 축약하지 않는다.

### Scene 1 — 동기화실

- Entry: 정족수가 성립했으니 출발은 관리된 절차다
- Opposition: 각 담당이 자기 항목만 보증하며 서로의 오차를 책임지지 않음
- Exit: 여섯 개의 부분 보증이 하나의 안전을 만들지 못한다는 사실이 드러남

### Scene 2 — 출발대 등록구역

- Entry: 필요한 것을 챙기면 현지에서 버틸 수 있다
- Opposition: 등록되지 않은 물건은 귀환 불가이며 일부는 반출 자체가 불가
- Choice: 에이든이 등록되지 않은 개인 물품을 두고 간다. 장갑 안쪽 경고는 신고하지 않는다
- Exit: 소지품 목록이 곧 현지에서 가능한 행동의 목록이 됨

### Scene 3 — 통과 개시

- Entry: 통과는 짧고 몸은 견딘다
- Opposition: 좌표가 붕괴하고 몸이 동기화 비용을 지불
- Exit: 리아의 마지막 경고가 중간에 끊김

### Scene 4 — 오차 구간

- Entry: 목표 좌표 근처로 나오면 된다
- Opposition: 오차가 상한을 향해 벌어지고 장비 일부가 시간 오차로 잠김
- Choice 압박: 강제복귀 1회를 오착 수정에 쓰면 귀환불능
- Exit: 오차를 수정하지 않고 그대로 착지하기로 함

### Scene 5 — 서부 격리촌 외곽 진흙 수로

- Entry: 도착만 하면 임무 시계가 시작된다
- Opposition: 예정 도시 내부가 아니라 약 18km 밖 수로. 잠긴 장비와 현지 법에 맞지 않는 신분문서
- Exit: 임무의 문제가 승인에서 생존·신분으로 바뀜

### Scene 6 — 수로 위 들판

- Entry: 남은 것은 이동과 시간 계산뿐이다
- Opposition: 멀리서 종이 울림
- Exit: 회색 종과 귀환석이 같은 박자로 진동. 누가 왜 반응하는지는 알 수 없음

## 9. Anti-Repeat

- E001의 삭제된 글자 훅, E005의 인장 이름 훅과 다른 층의 훅을 쓴다. E006의 훅은 문서가 아니라 **소리와 진동**이다
- E002처럼 여섯 기관을 순회하며 조건을 설명하지 않음. 각 담당은 자기 항목만 확인하고 지나간다
- E002의 귀환석 검사 장면을 재연하지 않음
- E003의 증거 대조, E004의 명단, E005의 협상 구성을 반복하지 않음
- 오착을 설명 없는 장치 고장으로 처리 금지 (overlay §8)
- 도약 감각을 형용사로 길게 나열하지 않음. 설계 지시는 기능적 서술이다
- 도착 즉시 현지인·아이리스와 조우하지 않음. 그것은 E007–E008의 기능이다
- 회색 종을 이 화에서 유물·열쇠·무기로 격상하지 않음
- 강제복귀를 써서 위기를 즉시 해결하지 않음

## 10. Active State / Props

- 균열 귀환석 (도착 뒤 잔여 체류 계산 시작)
- 등록 소지품 목록 / 두고 간 개인 물품
- 시간 오차로 잠긴 장비 일부
- 현지 법과 맞지 않는 신분문서
- 장갑 안쪽 리아의 경고 (미신고 소지품)
- 회색 종 — 원거리 음원, 접촉 없음

잠긴 장비와 미신고 소지품은 E007 이후 현지 은폐·검문 판정에 직접 사용되므로 A10 prop 등재 대상이다.

## 11. State Mutation Plan

E006 종료 시 기록:

- 도착 성공 판정과 실제 오차 거리
- 도착 시각 기준 잔여 체류시간
- 잠긴 장비 목록과 사용 가능 장비 목록
- 두고 온 물품과 반입된 미신고 물품
- 신분문서 불일치 항목
- 강제복귀 1회 미사용 상태
- 회색 종 공명 관측 기록 (해석 없음)
- Subact 1A 종료 / 1B 진입 상태: 신분 없음, 현지 앵커 없음, 언어는 통하나 계급 호칭 미숙

## 12. Ready Verdict

- Authority: RESOLVED
- Domain Readiness: READY
- Storycraft companion: REQUIRED / prepared separately
- POV: READY
- Scene density: X · 6장면 — 밀도 상한 5~6 안에서 설계 장면 수와 일치
- Permanent loss: 이 화에서 확정되는 영구손실 없음 (L001은 E023–E025)
- S0: 0
- S1: 0

E006 Storycraft Manifest와 E005 상태기록 확인 뒤 A18 호출 가능.
