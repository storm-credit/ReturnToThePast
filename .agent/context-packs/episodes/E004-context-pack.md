# Episode Context Pack — E004

Status: D10 READY  
Episode: E004  
Title: 지연의 사망자  
Compiled By: A21 Context Pack Compiler  
Reference: `agent/e003-finalize-status`

> 이 CP는 정본이 아니다. 충돌 시 원본 정본과 권한계층을 따른다.

## 1. Authority / Architecture

Required sources:

- [`/AI_PROJECT.md`](../../../AI_PROJECT.md)
- [`docs/00_project/canon-constitution-v1.md`](../../../docs/00_project/canon-constitution-v1.md)
- [`docs/00_project/canon-naming-pack-v1.md`](../../../docs/00_project/canon-naming-pack-v1.md)
- [`docs/00_project/terminology-and-addressing-clarification-v1.md`](../../../docs/00_project/terminology-and-addressing-clarification-v1.md)
- [`docs/00_project/decision-log.md`](../../../docs/00_project/decision-log.md) — DEC-016·017·018·020·021
- [`docs/00_project/GATE_STATUS.md`](../../../docs/00_project/GATE_STATUS.md)
- [`docs/10_story_architecture/detail/v01-scene-ready-design-v1.md`](../../../docs/10_story_architecture/detail/v01-scene-ready-design-v1.md) — E004 절
- [`docs/10_story_architecture/detail/v01-d9-correction-overlay.md`](../../../docs/10_story_architecture/detail/v01-d9-correction-overlay.md) — §3 E004 교체 판정
- [`docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md`](../../../docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md) — E004 행
- [`docs/10_story_architecture/subact-causal-matrix-v1.md`](../../../docs/10_story_architecture/subact-causal-matrix-v1.md) — 1A
- [`docs/10_story_architecture/location-world-crosswalk-v1.md`](../../../docs/10_story_architecture/location-world-crosswalk-v1.md) — V01 1A
- [`docs/10_story_architecture/scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) — V1 E004 = Q · 2장면 **고정**
- [`docs/12_losses/permanent-loss-lock-v1.md`](../../../docs/12_losses/permanent-loss-lock-v1.md)
- [`.agent/context-packs/episodes/E003-context-pack.md`](E003-context-pack.md)
- [`manuscript/state/E002-state-mutation.md`](../../../manuscript/state/E002-state-mutation.md)

Episode function (registry E004 행 + v01 설계 E004 절):

- Grand Act: GA I — 잘못된 치료
- Volume: V1 — 회색 종이 울리는 날
- Subact: 1A — 출발표에 서명하는 사람
- Beat: 대항 세력
- Goal: 추가검증에 필요한 시간과 F0의 잔여 생존일이 정면으로 충돌하는 자리에서 지연의 실제 사망자를 확인한다
- Opposition: 하루 지연 시 약품 중단 대상 명단 / 살아 있는 현지 앵커 정보의 공백 / ‘현지에서 확보하라’는 지휘부 반박
- Choice: 기록 누락을 감수하고 출발표에 서명
- Cost: 살아 있는 현지 앵커 없이 고위험 출발이 승인되고, 그 위험을 에이든이 문서로 떠안음
- State Change: ‘의심은 있으나 실행 합리성이 큰 임무’가 ‘기다리는 것 자체가 이름 있는 사망을 만드는 임무’로 변함
- Hook: 목표 시대의 귀환점 목록이 한 칸씩 사라짐

## 2. E003 Carryover

출처: [`E003-context-pack.md`](E003-context-pack.md) §11 State Mutation Plan + E003 종료 상태 인계. E003 state-mutation 문서는 아직 없으므로 A18 호출 전 상태조회로 재확인한다.

### 에이든

- 압수품·피해명부·19만 증가 모델을 직접 확인
- 삭제된 증언자의 사망일이 세렌의 범행일보다 아홉 날 앞섬을 발견
- 그럼에도 임무를 취소하지 않고 **현지 추가검증**을 유지하기로 결정
- 세렌 유죄 가설과 제거 임무에 심리적·제도적으로 더 깊이 묶인 상태

### 리아

- 감사표식 상태 유지, 원본층 접근 제한
- 대조표의 순번 다섯과 안개월 3일을 외움
- 세렌의 무죄도 유죄도 확정하지 않음

### 귀환석

- 중심층 3갈래 균열
- 예상 체류 5시간 17분
- 최대 오착 18km
- 강제복귀 1회
- 미확인 토양은 아스트라 관측탑·앙카 귀환다리 공동봉인 상태

### 현재 피해

- 제칠 방벽 마지막 표시 구조 가능 인원 1,312명 (E002 표시값)
- 서부 구조대 31명 연락두절 지속
- 숫자는 최종 생존자 수가 아니라 현재 구조계산값

E004는 E003의 증거 검토를 재연하지 않는다. 압수품·19만 모델은 배경 상태로만 환기한다.

## 3. Time / Location

출처: v01 설계 E004 절 / [`docs/01_timeline/master-chronology-and-aging-ledger-v1.md`] 계열 (E001·E002 CP 추출값 승계)

- Date: 건국력 664년 장야월 18일, E003 직후
- Era: F0
- 에이든: 41세 / 주관적 누적일 0
- Main locations:
  1. 배급실 — 약품 배분대
  2. 개인 장비실
- 이동은 중앙 복합시설 내부이며 장거리 이동시간 문제 없음
- 설계 E004의 `승인회의` 비트는 **독립 장면이 아니라 배급실 장면 안의 대립**으로 접힌다. 밀도가 Q형 2장면이기 때문이다 `[DEC-021]`
- E004 안에서 실제 출발은 일어나지 않는다

## 4. 지연 비용과 역사주소 앵커

Sources:

- v01 설계 E004 절
- [`docs/10_story_architecture/detail/v01-d9-correction-overlay.md`](../../../docs/10_story_architecture/detail/v01-d9-correction-overlay.md) §1·§3
- [`docs/00_project/terminology-and-addressing-clarification-v1.md`](../../../docs/00_project/terminology-and-addressing-clarification-v1.md) §2
- [`docs/08_institutions/political-economy-record-law-v1.md`](../../../docs/08_institutions/political-economy-record-law-v1.md)

### A. 지연의 실제 사망자

- 선별실은 방위지휘부 산하 생존 예측 부서이며, 개입 시 늘어나는 생존자 수를 계산한다
- E004에서 제시되는 것은 예측 총량이 아니라 **하루 지연 시 약품 중단 대상 명단**이다
- 명단에는 에이든이 아는 가족이 포함된다
- 명단은 협박 소품이 아니라 실제 배급·병상·약품 상한에서 도출된 배분 결과다
- 선별실은 잔혹해서가 아니라 실제로 더 많은 환자를 살려 온 기능을 가진다

### B. 앵커 판정 — 정본 교체 문구

기존 설계의 `현지 앵커 없는 출발 허용`은 다음으로 대체된다 (overlay §3).

> 살아 있는 현지 앵커를 확보하지 못한 채, 세렌 바일 사건기록·회색 종 잔향·서부 세무층을 역사주소로 묶어 고위험 출발을 승인한다.

두 앵커는 다른 것이다.

- **역사주소 앵커**: 출발 필수조건. 사건기록·물질층·공공기록이 서로 가리키는 범위로 성립
- **살아 있는 현지 앵커**: 필수조건이 아니라 안전·신분·귀환 안정조건

### C. 받아들이는 위험 (overlay §3 실제 비용)

- 예정 도시 내부가 아니라 약 18km 떨어진 수로에 오착
- 현지 신분과 통행보증 없음
- 귀환창 단축
- 현지 협력자가 생기기 전까지 귀환표식 불안정
- 본부가 현지 사망·이동·정치 변화를 실시간으로 확인하지 못함

이 비용은 E006에서 그대로 실현되며, 장치 고장이 아니라 E004에서 승인한 위험의 직접 결과다.

## 5. Character State

### 에이든 로엔

- 목표: 지연이 만드는 사망과 출발이 만드는 위험 중 어느 쪽을 자기 이름으로 떠안을지 결정
- 습관: “목표·출구·비용” 순서로 말함 (voice bible §2)
- 죄책감 표식: 상대 이름을 피하고 역할명으로 부름 — 명단 앞에서 이 습관이 깨지는 것이 E004의 인물 변화다
- 오류 가능성: 서명이 위험을 관리한다고 느낌. 실제로 서명은 책임 주체만 만든다
- 금지: 지휘부를 악으로 규정하고 회의장을 이탈, 명단을 던지거나 파기

### 리아 세른

- 역할: 살아 있는 현지 앵커 정보가 비어 있다는 이유로 연기를 요구
- 근거: 기록의 부재는 사실이며 해석이 아님. 확정·미확정·검증불가를 구분해 말함
- 제한: 감사표식 때문에 공식 승인선에 직접 서지 못함
- 금지: 에이든 대신 결정, 숨겨둔 결정적 반증 제시, 예언자 말투

### 선별실 담당 / 지휘부 대립자

- `선별실`은 부서명이며 `생존선별파`는 F1 이후의 정치 세력이다. E004는 F0이므로 **선별실**을 쓴다 (terminology §2)
- 대립자의 얼굴은 [`docs/05_characters/cast-canon-index-v2.md`](../../../docs/05_characters/cast-canon-index-v2.md) §3 아르덴 케르(F0 임무평의회 대표, 불완전한 증거와 즉시 생존을 저울질하는 얼굴 있는 대립자)를 쓸 수 있다
- 새 핵심 이름을 즉석 확정하지 않는다
- 방위총감은 E001의 기능인물 직책이며 마르칸 베르와 동일인이 아니다
- 금지: 숫자만 외치는 냉혈 관료 caricature

## 6. Mystery / Information Ceiling

Sources: [`docs/11_mystery/mystery-reinforcement-ladder-v1.md`](../../../docs/11_mystery/mystery-reinforcement-ladder-v1.md)

Active mysteries:

- M02 세렌은 왜 재앙 창시자로 기록됐는가 — 배경 유지, 새 증거 없음
- M04 F0 귀환좌표는 남아 있는가 — 귀환점 목록 소실이 좌표·운영망 계열 단서로 처음 놓임
- M12 조작을 한 한 명의 흑막이 있는가 — 개인 흑막 암시 금지

Reader may know:

- 기다리는 선택에도 이름이 붙은 사망자가 있다
- 살아 있는 현지 앵커 없이 출발한다는 사실과 그 위험 목록
- 목표 시대의 귀환점 목록이 줄어들고 있다

Reader must not know yet:

- 세렌이 지방 소거를 늦췄다는 전체 기능
- 기록을 뒤집은 주체와 이유
- 삭제된 증언자의 정체
- 19만 계산의 최종 오류구조
- 귀환점 목록이 왜 줄어드는지, 누가 지우는지, 그것이 조작인지 운영결과인지

Final hook:

- 목표 시대의 귀환점 목록이 한 칸씩 사라짐
- 의미: 출발을 늦출수록 도착 가능한 자리 자체가 줄어든다 — 지연비용이 사람에서 좌표로 확장
- 금지: 사라지는 원인을 이 화에서 설명, 적의 방해로 단정, 새 시간법칙 추가

## 7. POV / Storycraft

- POV: 에이든 단일 근접 3인칭
- Scene Density: **Q형 2장면** — [`scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) V1 표에서 **고정**
- Primary craft: 명단 대 명단 — 지연비용의 인격화
- Secondary A: 대항 세력의 실제 효용
- Secondary B: 서명의 물질화
- Hook: H4 제도 변화 + H1 물리·운영 위험
- Reader reward: 기다림이 중립이 아니라는 것을 숫자가 아니라 이름으로 체감

## 8. Scene Values

Q형 2장면. 3장면으로 늘리지 않는다.

### Scene 1 — 배급실

- Entry: 검증을 더 기다리는 것이 신중한 판단이다
- Opposition: 하루 지연 시 약품이 끊기는 사람들의 명단, 그 안의 아는 가족 / 리아의 연기 요구는 정당하지만 지휘부는 ‘현지에서 확보하라’로 되받음
- Turn: 에이든이 명단의 산출근거와 제외대상을 묻고, 계산이 실제 배분에서 나왔음을 확인
- Exit: 기다림이 중립 상태가 아니라 이름이 적힌 선택으로 바뀜

### Scene 2 — 개인 장비실

- Entry: 서명은 형식이며 조건을 붙이면 위험을 줄일 수 있다
- Opposition: 책임서는 위험을 없애지 않고 책임 주체만 만든다 / 등록 가능한 물품과 불가능한 물품이 갈림
- Choice: 누락 위험을 인지했다는 책임서에 서명하고 살아 있는 현지 앵커 없는 출발을 수용
- Exit: 고위험 출발이 승인되고, 목표 시대의 귀환점 목록이 한 칸씩 사라짐

## 9. Anti-Repeat

- E001처럼 삭제된 글자·회색으로 되살아나는 이름을 훅으로 쓰지 않음
- E002처럼 승인기관을 한 명씩 순회하지 않음. 여섯 기관 명칭 나열 금지
- E002의 귀환석 토양을 다시 열어보지 않음
- E003처럼 두 문서를 나란히 놓고 대조하는 장면을 반복하지 않음. E004의 종이는 대조 대상이 아니라 **사람 명단과 자기 서명**이다
- 구조 가능 인원 숫자 카운트다운을 장면마다 갱신하지 않음. E004의 압박은 총량이 아니라 개별 이름이다
- 명단을 익명 숫자로만 제시하지 않음
- 선별실을 조작·악의로 처리하지 않음. 반대로 선별실이 옳다고 확정하지도 않음
- ‘사실은 명단이 위조였다’ 반전 금지
- 리아가 몰래 원본을 열어 결정적 반증을 내놓는 전개 금지

## 10. Active State / Props

- 하루 지연 시 약품 중단 대상 명단
- 누락 위험 인지 책임서 = 출발표
- 목표 시대 귀환점 목록
- 리아의 앵커 공백 의견서
- 등록 가능·불가능 개인 물품 구분 (E006 동기화실에서 회수)
- 압수 도구·피해명부·19만 모델·토양 표본은 배경 상태로만 유지

명단과 책임서가 E005 이후 재등장할 경우 A10이 prop 승격 여부를 판정한다.

## 11. State Mutation Plan

E004 종료 시 기록:

- 에이든의 출발표 서명 상태와 서명 시각
- 살아 있는 현지 앵커 부재 판정과 수용된 위험 목록
- 약품 중단 대상 명단의 확정·보관 상태
- 리아의 연기 요구 기록과 기각 사유
- 귀환점 목록의 잔여 칸 수와 감소 관측 여부
- 귀환창·체류창의 갱신값
- 성당 재검사·최종 정족수 진행상태

## 12. Ready Verdict

- Authority: RESOLVED
- Domain Readiness: READY
- Storycraft companion: REQUIRED / prepared separately
- POV: READY
- Scene density: Q · 2장면 — 설계 장면 수와 일치
- S0: 0
- S1: 0

E004 Storycraft Manifest와 E003 main 상태 확인 뒤 A18 호출 가능.
