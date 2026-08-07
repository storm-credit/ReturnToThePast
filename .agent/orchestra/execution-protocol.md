# Automatic Design Execution Protocol

Status: CANON-OPERATIONS

## No-Repeated-Interview Rule

작가가 이미 확정한 A+C 직접 시간여행, 15권 유지 의향, 설계 우선, 원고 금지는 다시 묻지 않는다. 작품의 본질을 바꾸는 차단 결정만 질문한다. 그 밖의 공백은 비교안 최대 4개를 내부 감사한 뒤 `[ASSUMPTION]`으로 채우고 decision log에 남긴다.

## Phase Pipeline

### P0 — Repository Sanitation
- 낡은 회귀 Canon과 원고 생성 스킬을 DEPRECATED로 전환
- Legacy Drafts는 REFERENCE ONLY
- 정본 계층과 출처 우선순위 고정

### P1 — World Foundation
- 세계 밖/국경/지도/거리
- 마나와 일반 마법
- 마나열병과 의료
- 종족·문화·언어·가족
- 신화·종교와 실제 역사
- 행정·세금·법·경제·범죄
- 군사·신수·유산
- Era O/N/F 생활·기술 차이

### P2 — Character/Faction Foundation
- 핵심 인물명은 문화·명명 규칙 후 재심사
- 인물별 욕망·거짓 믿음·이탈 가능성
- 기관별 실제 효용·지지층·개혁비용
- 적대 시스템은 단일 최종보스보다 상충하는 합리성으로 구성

### P3 — Collection/Mystery Foundation
- 플롯에서 필요한 자산을 먼저 계산하고 수량을 나중에 확정
- 무기·방어구·보석·신수는 연대유산/독립 동맹으로 통합
- 시리즈/Grand Act/Volume별 맥거핀과 질문·오답·회수 배치

### P4 — Macro Architecture
- 결말 조건부터 역산
- 5 Grand Acts × 3 Volumes = 15권
- 설계 목표 375화, 권당 25화
- 구조: Series → Grand Act → Volume Act → Arc → Subact → Episode
- 각 Subact는 국소 문제를 해결하고 다음 Subact 원인을 생성
- 각 권 결말은 상태·관계·기관·시간선 중 최소 하나를 비가역적으로 변경

### P5 — Detailed Architecture
- 375화 전체 카드
- 인물·기관·자산·미스터리·손실 장부 동시 갱신
- 20–30화 단위 배치 감사

### P6 — Cross Audit
- 정본, 인과, 시간/거리, 숫자, 반복, 유사성, 독자 보상, 영구손실
- S0/S1 수정 후 재감사

### P7 — Pre-Writing Readiness
- 설계 완료 문서는 작성하되 Gate는 CLOSED 유지
- 작가 선언 전 Prose Agent 호출 금지

## Subact Completion Rule

모든 Subact는 다음 11개 필드를 가진다.

Promise / Goal / Opposition / Choice / Cost / Revelation / Reward / Loss / State Change / Next Cause / Anti-Repeat

'해결'은 문제가 사라지는 것이 아니라, 주인공이 값을 지불해 국소 목표를 달성하고 세계 상태가 바뀌는 것을 뜻한다.

## Stop Conditions

자동 진행을 멈추는 경우는 다음뿐이다.

- 작가가 선택하지 않으면 서로 양립 불가능한 결말 철학
- 법적·안전상 진행 불가
- GitHub 쓰기 권한 실패
- S0가 현재 정보로 해결 불가능

그 외에는 대안·채택·파급효과를 기록하고 계속 진행한다.
