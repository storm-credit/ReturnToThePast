# Episode Context Pack — E002

Status: D10 READY  
Episode: E002  
Title: 여섯 개의 승인  
Compiled By: A21 Context Pack Compiler  
Reference: `agent/d10-storycraft-orchestration`

> 이 CP는 정본이 아니다. 충돌 시 원본 정본과 권한계층을 따른다.

## 1. Authority / Architecture

Required sources:

- [`/AI_PROJECT.md`](../../../AI_PROJECT.md)
- [`docs/00_project/canon-constitution-v1.md`](../../../docs/00_project/canon-constitution-v1.md)
- [`docs/00_project/D9_CANON_AMENDMENT.md`](../../../docs/00_project/D9_CANON_AMENDMENT.md)
- [`docs/00_project/decision-log.md`](../../../docs/00_project/decision-log.md)
- [`docs/00_project/GATE_STATUS.md`](../../../docs/00_project/GATE_STATUS.md)
- [`docs/10_story_architecture/detail/v01-scene-ready-design-v1.md`](../../../docs/10_story_architecture/detail/v01-scene-ready-design-v1.md)
- [`docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md`](../../../docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md)
- [`docs/10_story_architecture/subact-causal-matrix-v1.md`](../../../docs/10_story_architecture/subact-causal-matrix-v1.md)
- [`.agent/context-packs/episodes/E001-context-pack.md`](E001-context-pack.md)

Episode function:

- Grand Act: GA I
- Volume: V1
- Subact: 1A
- Beat: 첫 장벽
- Goal: 기록 검증을 기다리면서 여섯 분산 승인조건을 통과
- Opposition: 줄어드는 구조 가능 인원, 귀환석 균열, 승인순서 의존성
- Choice: 즉시 출발 대신 기록검증 서명을 기다림
- Cost: 현지 체류·귀환창 감소
- State Change: 파견 가능 여부가 ‘임무 찬반’에서 ‘제한된 조건의 출발’ 문제로 구체화
- Hook: 귀환석 내부에 출발지와 다른 시대의 흙

## 2. E001 Carryover

- 에이든: 브리핑 수령, 임무 동의 보류
- 리아: 비인가 잔문 접근 감지
- 제칠 방벽: 구조 가능 인원 감소, 구조대 31명 연락두절
- 기록: 구일·십이 일·십칠 일 / 빈 증언자 두 자리 / `세` 흔적
- 방위총감: 전체 생존계산을 근거로 승인 절차를 진행
- 19만 증가는 생존선별실 예측값이며 진실 확정 금지

E002는 E001의 붕괴 장면을 재연하지 않고, 숫자 갱신과 승인 대기 중 후과로만 환기한다.

## 3. Time / Location

- Date: 건국력 664년 장야월 18일, E001 직후
- 에이든: 41세 / 주관적 누적일 0
- Main locations:
  1. 승인 회랑
  2. 귀환석 검사대
  3. 대기실·검증서명 창구
- 이동은 중앙 복합시설 내부
- 승인 대기시간과 검사시간이 실제 현지 체류창을 감소시킴

## 4. Six Authority Functions

Sources:

- [`docs/08_institutions/institution-org-procedure-bible-v1.md`](../../../docs/08_institutions/institution-org-procedure-bible-v1.md)
- [`docs/08_institutions/temporal-authority-split-v1.md`](../../../docs/08_institutions/temporal-authority-split-v1.md)
- [`docs/03_systems/time-travel-ontology-v1.md`](../../../docs/03_systems/time-travel-ontology-v1.md)

Required functional roles:

1. 왕좌 보관자 — 법적 출발 승인·국가 책임
2. 성당 동기화관 — 달력·몸·계절 동기화
3. 탑 항법관 — 시간·공간 좌표와 오차
4. 기록관 — 역사주소·표적 기록 검증
5. 귀환관리자 — 귀환석·복귀창·인원·소지품 등록
6. 현장요원 — 위험인지·현장행동·책임 동의

Rules:

- 어느 한 기관도 단독 출발 승인 불가
- 승인 순서를 바꾸면 좌표·몸·귀환 오차 증가
- 서명은 정답 보증이 아니라 자기 책임범위 확인
- 기관마다 임무를 반대·찬성하는 이유가 아니라 서로 다른 실패를 막는 기능이 있음

## 5. Return Stone

Sources:

- [`docs/03_systems/time-travel-ontology-v1.md`](../../../docs/03_systems/time-travel-ontology-v1.md)
- [`docs/03_systems/magic-capability-and-counterplay-matrix-v1.md`](../../../docs/03_systems/magic-capability-and-counterplay-matrix-v1.md)
- [`docs/09_collection/major-assets-ledger-v1.md`](../../../docs/09_collection/major-assets-ledger-v1.md)

Allowed facts:

- 귀환석은 무제한 귀환키가 아님
- 균열·등록상태·동기화 순서가 사용가능시간을 줄임
- 강제복귀는 사실상 한 번이며 오착 수정에 쓰면 귀환불능 위험
- 목표 축소는 임무시간을 늘릴 수 있으나 조사·구조 범위를 줄임

Forbidden:

- 귀환석이 F0 완전복원키라는 암시
- 미래시간선 이동을 자유선택
- 균열을 간단한 마법·수리로 복구

## 6. Character State

### 에이든

- 목표: 불완전 기록을 더 검증하면서도 출발 가능성을 잃지 않음
- 압박: 구조대와 현재 생존자 수 감소
- 습관: 기관의 명칭보다 각 실패조건을 질문
- 선택: 빠른 출발보다 기록검증 서명을 기다림
- 오류 가능성: 모든 정보가 모일 때까지 결정 미루기

### 리아

- 비인가 접근 때문에 직접 승인선에 서기 어려움
- 기록검증 서명을 확보하려 하나 원본 전체를 보지 못함
- E002에서 에이든 대신 기관을 설득해 주지 않음

### 귀환관리자 / 항법관

- 이름을 새 핵심 인물로 즉석 확정하지 않음
- 목표축소 권고는 겁쟁이 행동이 아니라 실제 귀환확률 관리
- 수치·균열·오차범위를 명확히 말하되 정답을 아는 예언자 아님

## 7. Mystery / Plant

Active questions:

- 귀환석의 흙은 왜 목표 시대가 아닌 다른 층에서 왔는가?
- 이전에 누군가 같은 장치·좌표를 사용했는가?
- 승인체계는 실제 안전장치인가 책임분산 장치인가?

Reveal ceiling:

- 흙의 연대·지역을 E002에서 확정하지 않음
- 장치가 이미 여러 번 과거를 수정했다는 최종진실 공개 금지
- 승인기관 중 누군가를 즉시 배신자로 지정 금지

## 8. POV / Storycraft

- POV: 에이든 단일 근접 3인칭
- Scene density: S형 3장면
- Primary craft: 제한자원 선택
- Secondary A: 절차적 긴장과 협상카드
- Secondary B: 시도–실패–학습
- Hook: H2 정보 역전 + H1 물리적 귀환위험
- Reader reward: 시간여행의 힘이 아니라 허가·검증·귀환비용의 구체성

## 9. Scene Values

1. 승인 회랑: 출발 가능 → 서로 다른 실패조건 때문에 지연
2. 검사대: 귀환 보장 기대 → 균열과 짧은 사용창
3. 대기실: 빠른 출발 압박 → 검증을 기다리는 능동적 지연과 더 큰 비용

## 10. Anti-Repeat

- E001처럼 새로운 붕괴현장을 길게 보여 주지 않음
- 여섯 기관을 한 명씩 설명하는 강의식 순회 금지
- 모든 담당자가 같은 반대논리를 말하지 않음
- 회의→문서반전→경보의 E001 순서를 반복하지 않음
- 귀환석 흙을 곧바로 최종반전 열쇠로 만들지 않음

## 11. State Mutation Plan

E002 종료 시 기록:

- 여섯 승인 중 완료·보류 상태
- 귀환석 균열등급·예상 사용창
- 에이든의 목표 축소 수용 여부
- 리아의 기록검증 서명 상태
- 제칠 방벽 구조대 후과 환기
- 다른 시대 흙의 보관·접근권

## 12. Ready Verdict

- Authority: RESOLVED
- Domain Readiness: READY
- POV Allocation: READY
- Storycraft Manifest: required companion
- S0: 0
- S1: 0

A20 Manifest와 원고 전 상태조회가 완료되면 A18 호출 가능.
