# D10 Orchestration Harness v2

Status: CANON-OPERATIONS  
Owner: A00 / A21  
Applies To: 설계 보강, 원고 E001–E375, 품질감사, GitHub 병합

## 목적

에이전트·스킬·CP·Hook을 고정 순서로 실행해, 설정집이 실제 원고에 사용되고 조용한 정본 변경이 일어나지 않게 한다.

## H0 — Task Intake

A00이 작업을 분류한다.

- Canon Change
- World Detail
- Character Detail
- Item / Relic / Beast
- Religion / Culture
- Story Architecture
- Episode Manuscript
- Audit / Repair

출력:
- Task Type
- Scope
- Required Agents
- Required CP Level
- Required Quorum

## H1 — Authority Resolve

A02가 다음을 확인한다.

- 작가 최신 결정
- Canon Constitution
- Amendment / Errata
- Decision Log
- Gate

Hook:
- [`CLAUDE.md`](../../CLAUDE.md) 또는 CP에만 있는 사실이면 BLOCK
- 오래된 하위 문서가 상위 정본과 충돌하면 상위 정본 적용 후 영향 기록

## H2 — Context Pack Compile

A21이 필요한 CP를 컴파일한다.

순서:
Series → Grand Act → Volume → Subact → Episode

Hook:
- Base main SHA 누락 BLOCK
- Required Source Files 비어 있음 BLOCK
- 필수 분야가 장면에 필요하지만 미설계면 BLOCK
- stale CP BLOCK

## H3 — Domain Readiness

장면에 필요한 분야만 호출하되, 필요한 분야는 모두 호출한다.

- 지리/공간: A03
- 마법/질병: A04
- 종족/문화/종교: A05
- 기관/경제/법: A06
- 시간: A07
- 인물/관계: A08
- 세력/대립: A09
- 아이템/유산/신수: A10
- 미스터리/맥거핀: A11
- 인과구조: A12
- 연속성/손실: A13

Hook:
- 분야 문서가 존재해도 해당 장면에 필요한 세부필드가 없으면 READY가 아님
- 원고에서 즉석 설정 생성 금지

## H4 — Craft Selection

A20이 `storycraft-orchestrator`를 실행한다.

필수:
- Primary Craft 1개
- Secondary Crafts 최대 2개
- Reader Effect
- POV
- Information Gap
- Scene Density
- Hook Type
- Local Resolution
- Next Cause
- Anti-Repeat Difference

Hook:
- 이전 2화와 동일 조합 3연속 BLOCK
- 작법이 장면 목표와 무관하면 REVISE
- 보조 POV 정당화 없음 BLOCK

## H5 — Scene Architecture

A12+A08+A13+A20이 장면을 확정한다.

각 장면:
- 시간·장소·POV
- 목표
- 방해
- 선택
- 비용
- 가치 변화
- 세계관 요소의 실제 행동 기능
- 종료 상태

Hook:
- 정보 전달만 하고 가치변화 없는 장면 REVISE
- 이동·부상·보급·법적 후과 생략 REVISE
- 다음 화 원인이 없음 BLOCK

## H6 — Prose Draft

A18이 승인된 Episode CP와 Scene Architecture만 사용해 원고를 작성한다.

규칙:
- 공백 포함 최소 7,000자
- 상한 없음
- 분량 채우기 금지
- 자연스러운 한국어
- 에이든 근접 3인칭 기본
- 승인된 보조 POV만 사용
- 새 Canon 사실 생성 금지

## H7 — Prose & Read-Aloud Audit

A19가 검사한다.

- 번역체
- 불필요한 수동태·명사화
- 문장 호흡
- 생동감 있는 감각·행동
- 주체·거리·방향
- 이름·직함·호칭·발음
- 인물별 목소리
- 시점 정보상한

문제는 전체 재작성보다 위치와 최소 교체문장으로 고친다.

## H8 — Canon & Continuity Audit

A02+A07+A13이 검사한다.

- 날짜·주관적 경과일
- 나이·부상·피로
- 위치·이동시간
- 소유권·보관·파손
- 관계·호칭
- 기억·법적 주소
- 미스터리 공개시점
- 영구손실
- 정본 밖 새 사실

Hook:
- S0/S1 BLOCK
- Canon 변경이면 별도 Amendment/Decision Log 없이는 병합 금지

## H9 — Reader & Red Team Audit

A14+A16이 검사한다.

- 회차 약속 이행
- 독자 보상
- 긴장·이완
- 반복 장면·훅·POV·임무
- 대립자 무능 의존
- 주인공 만능화
- 문화·종교·아이템 장식화
- 편의적 해결
- 결말과 초반 연결

## H10 — Release Gate

필수 산출물:
- Episode CP
- Craft Manifest
- 원고
- 품질보고서
- 상태변경 목록
- 필요 시 Decision Log

A17 GitHub:
- latest main
- one episode branch
- behind_by=0
- PR
- squash merge
- state=closed / merged=true
- 실제 merge SHA
- main 파일 재확인

## H11 — Post-Merge State Mutation

A13+A21이 갱신한다.

- 인물 상태
- 관계 상태
- 기관·세력 상태
- 아이템·유산·신수 상태
- 미스터리·복선 상태
- 영구손실
- 연대·부상·위치
- 다음 화 CP 입력값

상태 장부 갱신 전에는 다음 화 CP를 READY로 만들지 않는다.

## 설계 보강 하네스

세계관·설정집 보강은 H0–H4 뒤 다음으로 진행한다.

1. 분야 스키마 확인
2. 기존 문서 상세도 감사
3. 실제 회차 사용처 확인
4. 누락 필드 보강
5. 인접 분야 교차검증
6. 상태·인과 영향 확인
7. A16 맹점 감사
8. A02 Canon 승격

## 현재 집필 상태

- Gate: OPEN
- E001: PROVISIONAL MANUSCRIPT
- E002 이후: D10 Domain Readiness와 CP 체계 통과 전 PAUSED
