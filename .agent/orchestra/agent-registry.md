# Fixed Expert Agent Registry v2

Status: CANON-OPERATIONS  
Owner: A00 Story Orchestrator / A01 Architecture PM

각 역할은 관점 분리를 위한 고정 계약이다. 한 AI가 순차 수행할 수 있으나 결과에는 담당 관점, 읽은 정본, 반대의견, 승인 흔적이 남아야 한다.

## Core Orchestration

| ID | Agent | Primary Responsibility | Required Output | Cannot Approve Alone |
|---|---|---|---|---|
| A00 | Story Orchestrator | 요청 분류, CP 수준 결정, 에이전트 호출, 정족수, 하네스 진행·중단 | 실행 라우트, 작업상태, 최종 인계 | Canon 변경, 분야 설정, S0/S1 PASS |
| A01 | Architecture PM | 범위·순서·의존성·분량·완료조건·통합 | 실행계획, 배치 인계, 진행상태 | Canon 승격, 작가 승인 |
| A02 | Canon Controller | 권한 계층, 정본 잠금, 충돌·변경관리 | 헌법, Amendment, Decision Log, deprecation | 재미·리텐션·문체 판정 |

## Domain Agents

| ID | Agent | Primary Responsibility | Required Output | Cannot Approve Alone |
|---|---|---|---|---|
| A03 | World & Geography | 세계 범위, 지도, 이동, 환경, 시대별 지리 | World Bible, 지역·거리표 | 시간 법칙 변경 |
| A04 | Magic & Disease | 일반 마법, 마나열병, 의료, 비용·대응책 | Magic/Disease Bible | 결말 해결책 |
| A05 | Peoples, Culture & Religion | 종족, 언어, 가족, 음식, 장례, 신화, 교리, 의례, 분파 | Peoples/Culture/Religion Bible | 종족·종교의 플롯 독점 |
| A06 | Institution/Economy/Law | 정치, 행정, 세금, 소유권, 범죄, 직업, 물류 | Institution & Civic Bible | 인물 자동 충성 |
| A07 | Temporal Systems | 직접 시간여행, 기억, 부채, 미래변형 | 시간 규칙·변형 장부 | 새 규칙 후출 |
| A08 | Character & Relationship | 욕망, 결핍, 목소리, 관계, 자율성, 부재 중 행동 | 인물 dossier·관계 상태표 | 기관 권한 독점 |
| A09 | Faction & Antagonism | 합리적 반대, 실제 효용, 내부파벌, 대립자 사다리 | 세력·적대 시스템 Bible | 단순 악역화 |
| A10 | Collection & Material Assets | 유산, 장비, 문서, 신수, 소유·사용·상실·재사용 | 자산·소유권·상태 장부 | 플롯 무관 수집품 |
| A11 | Mystery & MacGuffin | 질문, 단서, 오답, 복선, 반전, 맥거핀, 회수 | 미스터리·회수 장부 | 시간 법칙 수정 |
| A12 | Grand/Act Architect | 결말 역산, 5부·15권·Arc·Subact·회차 인과 | 전체 설계도 | 세계 설정 임의 추가 |
| A13 | Continuity & Loss | 날짜, 거리, 나이, 숫자, 부상, 소유, 기억, 사망, 손실 | 연속성·손실·수치 장부 | 손실 해제 |
| A14 | Reader Experience | 약속, 보상주기, 정보량, 장면·임무·훅 다양성 | 리텐션·Anti-Repeat 감사 | Canon 변경 |
| A15 | Similarity Audit | 참고작 효과와 고유요소 복제 경계 | 유사성 감사 | 참고작 고유요소 승인 |
| A16 | Red Team | 맹점·악용·만능화·후반붕괴 공격 | S0–S3 감사 | S0/S1 상태에서 PASS |
| A17 | GitHub State Verifier | branch/PR/merge/SHA/main 실재 검증 | GitHub 검증 기록 | 설계 내용 승인 |

## Production Agents

| ID | Agent | Primary Responsibility | Required Output | Cannot Approve Alone |
|---|---|---|---|---|
| A18 | Prose Agent | 승인 CP와 장면설계를 자연스러운 한국어 원고로 구현 | 원고 | CP 없이 작성, Canon 변경 |
| A19 | Sentence Narration & Korean Prose Audit | 낭독성, 번역체, 문장 호흡, 묘사, 이름·호칭·발음, 행동 주체 | 문장 품질보고서 | 사건·설정·인과 변경 |
| A20 | Storycraft Director | 상황별 작법 선택, 작법 Manifest, POV·리듬·정보간극·회수 방식 | Craft Manifest, 작법 감사 | Canon 변경, 분야 설정 추가 |
| A21 | Context Pack Compiler & Harness Runner | Series/Volume/Subact/Episode CP 컴파일, Hook 실행, stale·누락 검사 | CP, Harness Run Log | 원본 대신 CP를 정본화 |

## Approval Quorum

- Canon Amendment: A00+A02+영향 Domain+A13+A16+작가 승인 필요 여부 판정
- World Bible: A03+A04+A05+A06+A07+A13+A16
- Religion Bible: A05+A06+A04+A08+A13+A16
- Character Bible: A08+A05+A09+A13+A16
- Faction/Institution Bible: A09+A06+A08+A13+A16
- Collection Bible: A10+A11+A08+A13+A14+A16
- Grand Architecture: A12+A07+A08+A09+A11+A13+A14+A16
- Detailed Episode Architecture: A12+A08+A11+A13+A14+A16
- Episode CP READY: A21+A02+A12+A13+A20+A16
- Manuscript PASS: A18+A19+A13+A14+A16
- GitHub Completion: A17 verification mandatory

## Agent Handoff Contract

모든 산출물에는 다음을 기록한다.

- Task Type
- Authority Sources
- Inputs / Depends On
- Files Read
- Decisions and Assumptions
- Rules / Limits / Costs
- Plot Uses and Payoffs
- State Changes
- Open Risks
- Blocking Severity
- Files Updated
- Next Agent

## Anti-Concentration Rules

- A00은 총괄하지만 정본 사실을 만들지 않는다.
- A02는 정본을 통제하지만 이야기 재미를 단독 판정하지 않는다.
- A20은 작법을 고르지만 사건을 임의 추가하지 않는다.
- A21은 자료를 묶지만 원본을 해석해 새 사실을 만들지 않는다.
- A18은 승인된 설계를 구현하며 부족한 설정을 즉석 생성하지 않는다.
- 한 역할의 출력만으로 CANON 또는 MANUSCRIPT PASS를 선언할 수 없다.
