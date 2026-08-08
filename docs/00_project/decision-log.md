# Decision Log

## DEC-001 — A+C 직접 시간여행 방향

Date: 2026-08-07  
Original: 다크 판타지 무한 회귀 구조  
Changed To: 미래 시간요원 + 왕국 문명 전체 시간장치  
Reason: 회귀 공략물이 아니라 여러 시대를 직접 오가며 미래가 실제로 변하는 판타지 시간여행물  
Author Approval: APPROVED — “a+c”, “회귀 말고 타임트래블”

## DEC-002 — 기존 저장소 유지와 원고 동결

Changed To: `ReturnToThePast`를 계속 사용하고 `Drafts/`는 LEGACY / REFERENCE ONLY  
Reason: 설계 이력은 보존하되 새 정본과 원고를 섞지 않음  
Author Approval: APPROVED

## DEC-003 — 15권 / 375화 설계 목표

Changed To: 5 Grand Acts × 3 Volumes, 권당 25화, E001–E375  
Reason: 15권 규모가 세 시대·다종족·정치·시간인과를 수용하며 권별 독립 완결과 장기 회수를 제공  
Adjustment: 실제 연재 분량 변경은 decision log와 전체 인과 감사를 거쳐야 함  
Author Approval: APPROVED BY AUTOMATIC DESIGN MANDATE — “15권 구조 괜찮으면 하자”, “자동으로 끝까지”

## DEC-004 — 아홉 상처, 사도 조직 폐기

Changed To: 이름·기억·몸·장소·경계·계절·출발·귀환·대가의 신화적 원리  
Rejected: 9사도/12사도 비밀조직, 친구의 광신, 한 명씩 제거하는 보스전  
Reason: 참고작 직접 연상과 기계적 숫자채우기를 피함

## DEC-005 — 마나열병 정체

Changed To: 몸·기억·공적 기록·장소 주소가 다른 역사에 속할 때 발생하는 연속성 불일치 반응  
Reason: 질병, 시간여행, 행정, 종족, 정치 비용을 하나의 세계 엔진으로 연결

## DEC-006 — 다종족 공동 건국

Changed To: 인간·에르나·카르둔·라하크·네바르 공동체가 장치를 공동 건설하고, 무명종은 시간선 주소 탈락으로 발생  
Names: SOFT LOCK  
Reason: 인간만의 세계를 피하면서 종족을 단순 능력 슬롯으로 만들지 않음

## DEC-007 — 수집 설계

Changed To: 유산·신수·권한·증언을 Plot Use에서 역산  
Rejected: 등급 인플레이션, 모든 유산의 에이든 독점, 신수 포획 도감  
Reason: 수집욕구를 지워진 진실·소유권·상실·재사용 추적으로 전환

## DEC-008 — 결말 기능

Changed To: 중앙 연대개입을 폐쇄하고 생활 안정 기능을 지역·종족·시민 감사가 있는 분산망으로 이전  
Permanent Cost: F0 미복원, 에이든 공적 주소·귀환권 소실, Ria 개인기억 손실, 백지권 잔존  
Reason: 복원/유지/파괴의 단순 3지선을 넘어 초반의 권한·기록·대가 문제를 해결

## DEC-009 — 정식 제목과 인물명

Title: 《왕국은 과거를 먹고 산다》  
Project Code: `ReturnToThePast`  
Core Names: D9 정본 명명 패키지와 `cast-canon-index-v2.md`를 따른다.  
Status: CANON WITH ID-PRESERVING REPLACEMENT RULE

## DEC-010 — 전문가 오케스트라 고정

Changed To: A01–A18 고정 역할·승인 정족수·교차감사 체계  
Source Basis: 작가가 제공한 3개 MD

## DEC-011 — 한 문장 낭독·한국어 문체 스킬

Date: 2026-08-07  
Changed To: `.agent/skills/sentence-narrator/`를 활성 스킬로 등록  
Functions: 한 문장 낭독, 자연스러운 한국어, 번역체, 생동감, 행동·공간, 인물별 대사, 이름·호칭·발음, 시점·스포일러 검사  
Rule: 낭독 모드에서 원문 자동수정 금지. 검토 요청 시에만 최소 교체문장 제시.  
Author Approval: APPROVED — “한줄씩읽는 낭독스킬”, “자연스러운 문장, 생동감 있는 묘사, 번역체 금지, 이름관련 제대로 부르기”

## DEC-012 — Pre-Writing Gate OPEN 및 편당 푸시

Date: 2026-08-07  
Previous State: CLOSED / A18 DISABLED  
Changed To: OPEN / A18 ENABLED / A19 Sentence Narration & Prose Audit ENABLED  
Start: E001  
Publishing Unit: 한 화마다 `agent/manuscript-eNNN` 브랜치, 원고 1개, 품질보고서 1개, PR 1개, squash merge  
Length: 공백 포함 최소 7,000자, 상한 없음, 분량 채우기 금지  
Author Approval: APPROVED — “스킬등록후 끝까지 써줘. 한편마다 푸쉬해주고.”  
Scope Limit: 원고 제작 승인이지 정본·결말·영구손실의 무단 변경 승인이 아니다.

## DEC-013 — D10 모델중립 정본 우선 오케스트라

Date: 2026-08-07  
Problem: `CLAUDE.md`가 정본처럼 비대해지고, 상황별 장편 작법·회차별 Context Pack·보조 POV 실제 배치·조연/종교 장면 상세가 원고 하네스와 분리되어 있었다.  
Compared Options:

1. 도구별 파일에 전체 규칙 복제
2. ChatGPT/Claude 프로젝트 지침에 전체 규칙 집중
3. 단일 거대 오케스트라 프롬프트
4. 모델중립 정본 우선 계층형 오케스트라

Selected: **4안 — 모델중립 정본 우선 계층형 오케스트라**

Structure:

- `/AI_PROJECT.md`: 모델중립 NON-CANON 진입점
- `/CLAUDE.md`: Claude Code 전용 얇은 라우터
- `/AGENTS.md`: Codex 전용 얇은 라우터
- Canon / Amendment / Decision Log / State Ledger: 실제 권한
- Domain Bible: 세계관·인물·종교·기관·자산의 사실 원본
- A00: 총괄 라우팅, 정본 독단 승인 금지
- A20: 상황별 작법 선택과 Craft Manifest
- A21: Context Pack 컴파일과 Harness 실행
- Skills: 반복 절차, 정본 승인권 없음
- CP: 읽기 묶음, 원본 대체 금지
- Harness: Authority→CP→Domain→Craft→POV/Scene→Draft→Audit→GitHub→State 순서 강제

Additional Completion:

- 종교 의례·성직계급·생활 기능 상세화
- C11–C30 장면용 조연 dossier 확장
- E001–E375 보조 POV·주인공 부재 행동 배치
- E001 소급 Context Pack·Craft Manifest·D10 재감사

Author Direction: APPROVED BY CONTINUATION — “클라우드성 MD는 클라우드 거잖아… 따로 또 만들어야 돼?”, “이어서 진행”  
Canon Effect: 정본 사실 변경이 아니라 권한·호출·검증 구조의 운영 변경. 기존 결말·사건·영구손실 유지.

## DEC-014 — 검증 통과 후 main 자동 병합

Date: 2026-08-08  
Changed To: 원고 또는 운영 문서 작업이 완료되고 관련 검증을 통과하면 작업 브랜치에 커밋·푸시하고 PR을 생성한 뒤 `main`까지 squash merge한다.  
Exception: 검증 실패, 정본 충돌, 미해결 리뷰, 사용자에게 선택이 필요한 내용 변경이 있으면 자동 병합하지 않고 중단 상태를 보고한다.  
Numeric Style: 원고의 명확한 수량·시간·날짜·서수·시설번호·인원·기간은 아라비아 숫자로 표기하고 한글 숫자와 혼용하지 않는다.  
Author Approval: APPROVED — “메인까지 다 머지해줘. 앞으론 작성되면 메인까지 머지하도록”

## DEC-015 — 라베른 정식명 확정

Date: 2026-08-08
Original: `두겹성 라베른` (D8 명명 패키지 정식명 후보)
Changed To: **`두 역사의 라베른`**
Working Alias: `반쪽성` — 검색용으로 보존 (naming-pack §10)

Reason: 이 장소에서 겹치는 것은 성이 아니라 주민의 기억이다. `두겹성`은 `겹`을 구조 수식어로 써서 성이 둘이라는 오독을 만든다. `두 역사의`는 겹치는 대상을 역사로 명시하므로 첫 청취에서 구조 오해가 발생하지 않는다.

Preserved Function: `지도에는 한 성이지만 주민은 서로 다른 두 역사로 기억한다` (atlas R05). V01 1C에서 첫 개혁가의 실제 역할과 지역 대피를 드러내는 무대라는 서사 기능은 변경되지 않는다.

Rejected: `라베른 쌍성`(물리 구조 오도), `라베른 성`(두 역사 중첩이라는 핵심 정체성 삭제 위험)

Scope: 명칭 표층 변경. 장소의 물리 구조·역사·서사 배치·복선은 변경 없음. Canon Constitution의 HARD LOCK 항목이 아니므로 Amendment 없이 Decision Log로 처리한다.

Updated Files: `canon-naming-pack-v1.md` §3, `pronunciation-lexicon.md`, `naming-source-verification-gate-v1.md` §6, `naming-audit-errata-lavern-v1.md` §6, 명명 감사 3종

Manuscript Impact: 없음. E001·E002에 이 장소는 등장하지 않는다.

Author Approval: APPROVED — “두 역사의 라베른 / 가장 직접적. 첫 청취 즉시 이해”
