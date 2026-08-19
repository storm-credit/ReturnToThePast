# Governance & Routing v2

Status: CANON-OPERATIONS  
Owner: A00 Story Orchestrator / A02 Canon Controller

## 1. CLAUDE.md의 지위

[`CLAUDE.md`](../../CLAUDE.md)는 Bootstrap Router다.

할 수 있는 일:
- 시작 시 읽어야 할 핵심 파일을 가리킴
- 작업 유형에 맞는 에이전트·스킬·하네스를 호출
- 현재 Gate와 저장소 규칙을 요약

할 수 없는 일:
- 독립적으로 정본 생성
- 작가 결정·헌법·개정안 덮어쓰기
- 분야별 Bible을 생략하고 요약문만으로 원고 작성
- 설정 충돌을 자기 해석으로 해결

규칙: 어떤 사실이 [`CLAUDE.md`](../../CLAUDE.md)에만 있고 정본 문서에는 없다면 그 사실은 비정본이다.

## 2. 권한 순서

0. 작가 최신 명시 결정
1. Canon Constitution
2. 승인 Canon Amendment / Errata
3. Decision Log
4. 현재 State Ledger
5. 분야별 Bible
6. Story Architecture
7. Craft / POV / CP Overlay
8. Manuscript
9. Legacy Reference

충돌은 위 순서로 해결하며 A02가 판정한다.

## 3. A00 Story Orchestrator

A00은 총괄 지휘자다. 정본 소유자가 아니다.

책임:
- 요청을 작업 유형으로 분류
- 필요한 CP 수준 결정
- 담당 에이전트 호출
- 승인 정족수 구성
- 작법 선택과 설정 의존성 누락 확인
- 하네스 단계 진행·중단
- S0/S1이 있으면 원고·병합 차단
- 최종 결과와 GitHub 실제 상태 일치 확인

금지:
- 분야별 설정 임의 생성
- A02 없이 정본 충돌 해결
- A16 반대가 남은 상태에서 PASS
- A17 검증 없이 병합 완료 보고

### 3.1 Minimum Action Agent OS — Local Routing Lanes

작업 방법론은 `storm-credit/minimum-action-agent-os`의 bounded local action space 원칙을 따른다. 상세 감사와 예외는 [`minimum-action-agent-os-adoption-v1.md`](minimum-action-agent-os-adoption-v1.md)를 참조한다.

A00은 A01~A21을 한 번에 평면 선택지로 펼치지 않고 다음 5개 Lane 중 필요한 Lane만 선택한다.

| Lane | Existing Agents | Direct choices after entering Lane |
|---|---|---:|
| L1 Authority & Planning | A01, A02 | 2 |
| L2 World Systems | A03, A04, A05, A06, A07 | 5 |
| L3 Narrative Systems | A08, A09, A10, A11, A12 | 5 |
| L4 Evaluation & Release | A13, A14, A15, A16, A17 | 5 |
| L5 Production | A18, A19, A20, A21 | 4 |

규칙:

- 전체 Agent 수는 제한하지 않는다.
- 한 reasoning node에서 직접 선택 가능한 Agent/Tool/Skill/MCP/기타 callable action은 기본 `<= 5`로 유지한다.
- 기존 Agent를 삭제·병합하지 않는다. Lane은 새 Agent가 아니라 라우팅 그룹이다.
- 작업 유형 라벨은 분류값이지 peer callable action이 아니다.
- 필수 quorum과 Harness 단계는 선택지가 아니라 고정 순서이므로 인원을 줄이지 않는다.
- 여러 Lane이 필요하면 한 node에서 모두 펼치지 않고 Harness 순서대로 이동한다.
- Skill은 전역 action menu가 아니라 담당 Agent 내부에서 lazy-load한다.
- 실제 MCP가 세부 action을 많이 제공하면 담당 Agent가 task-relevant subset만 노출한다.

`Item / Relic / Beast`의 optional specialist 6개는 한 번에 노출하지 않는다. 먼저 L2의 A04/A05/A06 중 필요한 Agent를 고르고, 이어 L3의 A08/A11/A12 중 필요한 Agent를 고른다. 역할·정족수·승인권은 변하지 않는다.

## 4. 작업 유형별 라우팅

### Canon Change
필수: A00 + A02 + 영향 분야 Agent + A13 + A16
출력: Amendment / Decision Log / 영향 파일 / 상태 이행표

### World Detail
필수: A03/A04/A05/A06/A07 중 관련 Agent + A13 + A16
필요 시: A08/A09/A10/A11/A12
출력: 분야 Bible + Plot Uses + State Effects

### Character Detail
필수: A08 + A13 + A16
필요 시: A05/A06/A09/A12/A19
출력: Character Dossier + Relationship State + Voice Rules

### Item / Relic / Beast
필수: A10 + A13 + A16
필요 시: A04/A05/A06/A08/A11/A12
Local Action Rule: optional specialist는 `L2(A04/A05/A06) → L3(A08/A11/A12)` 순서로 분리 선택한다.
출력: Ownership / Access / Cost / Refusal / State / Plot Uses

### Religion / Myth / Ritual
필수: A05 + A06 + A04 + A13 + A16
필요 시: A03/A08/A09/A11/A12
출력: Doctrine Layers / Rites / Clergy / Material Practice / Political Uses

### Story Architecture
필수: A12 + A07 + A08 + A09 + A11 + A13 + A14 + A16
출력: Promise / Goal / Opposition / Choice / Cost / State / Next Cause

### Episode Manuscript
필수 순서:
A21 CP compile → A20 craft selection → A12 scene fit → A18 draft → A19 prose audit → A13 continuity → A14 reader experience → A16 red team → A17 GitHub

## 5. CP 수준

### Series CP
변하지 않는 핵심 명제·시간법칙·결말·영구손실·금지선.

### Grand Act CP
해당 3권의 약속·주제·상태 시작·상태 종료·대립축.

### Volume CP
25화 목표·주요 인물·장소·기관·맥거핀·손실·권말 상태.

### Subact CP
6~7화 국소 목표·현재 자원·해결 조건·비용·다음 원인.

### Episode CP
POV·시간·장소·등장인물 상태·작법·단서·아이템·종교·기관·후과·금지선.

CP는 출처 경로와 commit SHA를 기록하며, 새 설정을 생성하지 않는다.

## 6. Agent와 Skill 구분

Agent:
- 상황 판단
- 분야 소유권
- 승인·거부
- 충돌 해결 참여

Skill:
- 반복 절차
- 템플릿
- 검사 방법
- 출력 형식

스킬은 Agent의 판단을 대체하지 않는다.

Minimum Action 적용 시 Skill은 담당 Agent 내부의 lazy-loaded procedure로 취급한다. Active Skills 목록에 존재한다는 이유만으로 A00의 직접 peer choice에 포함하지 않는다.

## 7. Hook

### Pre-Context Hook
- 최신 main 확인
- Authority Stack 확인
- 관련 정본 파일 존재 확인

### Pre-Draft Hook
- Episode CP 존재
- Files Read 비어 있지 않음
- POV 정당화
- Primary Craft 1개, Secondary Craft 최대 2개
- 상태 시작값 확정
- S0/S1 없음

### Post-Draft Hook
- 정본 밖 새 사실 탐지
- 이름·직함·발음 검사
- 시간·거리·부상·소유권 검사
- 복선 공개시점 검사
- 장면 가치변화 검사
- 최소 글자수 검사

### Pre-Merge Hook
- 품질보고서
- 상태변경 목록
- Decision Log 필요 여부
- behind_by=0
- PR 단위 1화 원칙

### Post-Merge Hook
- 실제 merge SHA 기록
- main 재읽기
- 인물·기관·자산·미스터리·손실 장부 갱신
- 다음 화 CP 입력상태 생성

## 8. 원고 중단 조건

- CP 필수 분야 누락
- 인물의 현재 상태 불명
- 아이템 소유권 불명
- 종교·기관 절차가 장면 해결에 필요한데 미설계
- 시간법칙 충돌
- 결말 또는 영구손실 변경 가능성
- 동일 작법·POV·훅의 반복 위험
- S0/S1 미해결

위 조건에서는 A18을 호출하지 않는다.
