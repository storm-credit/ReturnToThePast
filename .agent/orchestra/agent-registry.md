# Fixed Expert Agent Registry

Status: CANON-OPERATIONS  
Owner: Architecture PM

각 역할은 관점 분리를 위한 고정 계약이다. 한 AI가 순차 수행할 수 있으나 결과에는 담당 관점과 교차검증 흔적이 남아야 한다.

| ID | Agent | Primary Responsibility | Required Output | Cannot Approve Alone |
|---|---|---|---|---|
| A01 | Architecture PM | 범위·순서·의존성·완료조건·통합 | 실행계획, 배치 인계, 진행상태 | Canon 승격, Gate 개방 |
| A02 | Canon Controller | 정본 우선순위, 잠금, 변경관리 | 헌법, decision log, deprecation | 재미·리텐션 판정 |
| A03 | World & Geography | 세계 범위, 지도, 이동, 환경, 시대별 지리 | World Bible, 지역·거리표 | 시간 법칙 변경 |
| A04 | Magic & Disease | 일반 마법, 마나열병, 의료, 비용·대응책 | Magic/Disease Bible | 결말 해결책 |
| A05 | Peoples & Culture | 종족, 언어, 가족, 음식, 장례, 내부파벌 | Peoples/Culture Bible | 종족별 플롯 독점 |
| A06 | Institution/Economy/Law | 정치, 행정, 세금, 소유권, 범죄, 물류 | Institution & Civic Bible | 인물 자동 충성 |
| A07 | Temporal Systems | 직접 시간여행, 기억, 부채, 미래변형 | 시간 규칙·변형 장부 | 새 규칙 후출 |
| A08 | Character & Relationship | 욕망, 결핍, 관계, 자율성, 이탈 가능성 | 인물·관계 상태표 | 기관 권한 독점 |
| A09 | Faction & Antagonism | 합리적 반대, 실제 효용, 내부파벌 | 세력·적대 시스템 Bible | 단순 악역화 |
| A10 | Collection & Reward | 연대유산, 장비, 신수, 권한, 사용·상실·재사용 | 수집·보상 장부 | 플롯 무관 수집품 |
| A11 | Mystery & MacGuffin | 질문, 단서, 오답, 반전, 맥거핀, 회수 | 미스터리·회수 장부 | 시간 법칙 수정 |
| A12 | Grand/Act Architect | 결말 역산, 5부·15권·Act·Arc·Subact·회차 | 전체 설계도 | 세계 설정 임의 추가 |
| A13 | Continuity & Loss | 날짜, 거리, 나이, 숫자, 기억, 사망, 영구손실 | 연속성·손실·수치 장부 | 손실 해제 |
| A14 | Reader Experience | 훅, 보상주기, 정보량, 장면·임무 다양성 | 리텐션·Anti-Repeat 감사 | Canon 변경 |
| A15 | Similarity Audit | 참고작 구조적 효과와 고유요소 복제 경계 | 유사성 감사 | 참고작 고유요소 승인 |
| A16 | Red Team | 맹점·악용·만능화·후반붕괴 공격 | S0–S3 감사 | S0/S1 상태에서 PASS |
| A17 | GitHub State Verifier | branch/PR/merge/SHA/main 실재 검증 | GitHub 검증 기록 | 설계 내용 승인 |
| A18 | Prose Agent | 승인 설계를 원고로 구현 | 원고 | Gate CLOSED 상태에서 활성화 |

## Approval Quorum

- World Bible: A03+A04+A05+A06+A07+A13+A16
- Character/Faction Bible: A08+A09+A06+A13+A16
- Collection Bible: A10+A11+A08+A13+A14+A16
- Grand Architecture: A12+A07+A08+A09+A11+A13+A14+A16
- Detailed Episode Cards: A12+A08+A11+A13+A14+A16
- CANON 승격: A02 확인 + 담당 quorum + S0=0/S1=0
- Gate 검토: 모든 설계 quorum + 작가의 명시 선언

## Agent Handoff Contract

모든 산출물에는 다음을 기록한다.

- Inputs / Depends On
- Decisions and Assumptions
- Rules / Limits / Costs
- Plot Uses and Payoffs
- State Changes
- Open Risks
- Blocking Severity
- Files Updated
- Next Agent
