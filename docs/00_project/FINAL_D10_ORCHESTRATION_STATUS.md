# FINAL D10 ORCHESTRATION STATUS

Status: **D10 MERGED / MAIN VERIFIED**  
Owner: A00 / A02 / A16 / A17 / A20 / A21  
D10 PR: #25  
D10 Merge SHA: `a34113d538f9ec22b396fdf0193dd82ab19328ec`

## 1. Selected Architecture

검토한 네 가지 운영안:

1. Claude·GPT·Codex 파일에 전체 규칙 각각 복제
2. 특정 채팅 프로젝트 지침에 전체 규칙 집중
3. 하나의 거대 오케스트라 프롬프트가 모든 권한 보유
4. 모델중립 정본 우선 계층형 오케스트라

선택: **4안**

이유:

- 모델을 바꿔도 같은 정본을 읽는다.
- [`CLAUDE.md`](../../CLAUDE.md)가 최상위 정본이 되는 것을 막는다.
- 설정 사실·작법 절차·자료 묶음·원고 구현을 분리한다.
- 한 에이전트의 오류가 Canon으로 자동 승격되지 않는다.
- ChatGPT·Codex·Claude Code를 같은 저장소에서 운용할 수 있다.

## 2. Final Authority Stack

`작가 결정`

→ `Canon Constitution`

→ `Canon Amendment / Errata`

→ `Decision Log`

→ `State Ledger / Gate Status`

→ `Domain Bible`

→ `Story Architecture`

→ `Storycraft / POV / Context Pack`

→ `Manuscript`

→ `Legacy / Reference`

다음은 NON-CANON 운영문서다.

- [`AI_PROJECT.md`](../../AI_PROJECT.md)
- [`CLAUDE.md`](../../CLAUDE.md)
- [`AGENTS.md`](../../AGENTS.md)
- Agent Contract
- Skill
- Harness
- Context Pack

## 3. Model Routers

- [`/AI_PROJECT.md`](../../AI_PROJECT.md): ChatGPT·Codex·Claude가 공유하는 모델중립 진입점
- [`/CLAUDE.md`](../../CLAUDE.md): Claude Code 전용 얇은 라우터
- [`/AGENTS.md`](../../AGENTS.md): Codex 전용 얇은 라우터
- ChatGPT Project 지침: [`/AI_PROJECT.md`](../../AI_PROJECT.md)와 저장소 정본을 읽도록 안내

세 라우터는 정본을 복사하지 않고 같은 원본을 가리킨다.

## 4. Active Agents

- A00 Story Orchestrator — 요청분류·호출·정족수·중단
- A01 Architecture PM — 범위·의존성·완료조건
- A02 Canon Controller — 권한·충돌·변경관리
- A03–A17 Domain / Audit / GitHub Agents
- A18 Prose Agent — READY CP만 원고화
- A19 Sentence Narration & Korean Prose Audit
- A20 Storycraft Director — 상황별 작법 Manifest
- A21 Context Pack Compiler & Harness Runner

권한분산:

- A00은 총괄하지만 정본 사실을 만들지 않는다.
- A02는 정본을 관리하지만 재미를 단독 승인하지 않는다.
- A20은 작법을 고르지만 사건을 바꾸지 않는다.
- A21은 자료를 묶지만 CP를 정본화하지 않는다.
- A18은 부족한 설정을 즉석 생성하지 않는다.
- A16은 S0/S1 상태에서 PASS를 선언하지 않는다.
- A17 확인 전 GitHub 완료를 보고하지 않는다.

## 5. Active Skills

### context-pack-compiler

- 필요한 정본의 원본경로·상태·기준 ref 추출
- Domain 누락·stale·충돌 검사
- Series / Volume / Subact / Episode CP 생성

### storycraft-orchestrator

- 상황에 맞는 중심 작법 1개와 보조 작법 최대 2개 선택
- 국소완결, 장면–반응, 정보간극, 공정단서, 정치·전투·생활 후과를 선택적으로 사용
- 동일 작법·훅의 기계적 반복 차단

### sentence-narrator

- 한 문장 낭독
- 자연스러운 한국어·번역체·묘사·공간·행동·이름·호칭·발음 검사

Skill은 정본 승인권이 없다.

## 6. Context Pack and Harness

CP levels:

- Series
- Grand Act
- Volume
- Subact
- Episode

Episode CP 필수 항목:

- Authority Sources
- Architecture Function
- Time / Location / Logistics
- Active Characters / Offscreen Actions
- Systems / Institution / Religion / Assets
- Mystery / Loss / Information Ceiling
- POV Allocation
- Storycraft companion
- Prohibitions
- State Mutation Plan
- Freshness / stale rule

Main Harness:

[`docs/13_writing_harness/orchestration-harness-v2.md`](../13_writing_harness/orchestration-harness-v2.md)

Execution:

`Authority Resolve → CP Compile → Domain Readiness → Craft Manifest → POV/Scene Architecture → Draft/Design → Prose Audit → Canon/Continuity → Reader/Red Team → GitHub Verification → State Mutation`

## 7. Domain Readiness

READY:

- 시간여행·기억·인과
- 지리·수도·이동·물류
- 생활문화·언어·달력
- 인구·경제·직업·가격
- 군사·외교·보급
- 종족·문화
- 종교·신화·의례·성직계급·구휼·재판
- 기관·법·행정
- 세력·대립자
- C01–C30 인물·관계·목소리·주인공 부재 행동
- R01–R12 유산
- B01–B05 주권신수
- 미스터리·복선·맥거핀
- 영구손실
- Grand Act / Volume / Arc / Subact / Episode 인과
- 장면밀도·훅

Conditional S2:

- 일반 소품이 반복되면 별도 prop index로 승격
- 실제 원고 반응에 따라 보조 POV 빈도를 미세조정

## 8. Secondary POV

- P1 단일 보조 POV 회차: 30화
- P2 다중 POV 회차: 15화
- P3 제한 관찰자 삽입: 8개

보조 POV에는 목적·정보상한·재합류 회차·상태변화가 있다.

## 9. Episode State

### E001

- Title: 마지막 도시의 다른 날짜
- PR: #24
- Merge SHA: `97d9195913a53eba96d7cde4360429125ee7c69b`
- Context Pack: READY / RETRO
- Craft Manifest: READY / RETRO
- D10 Retro Audit: PASS
- Manuscript rewrite required: NO
- Status: CANON MANUSCRIPT / COMPLETE

### E002

- Title: 여섯 개의 승인
- Context Pack: READY
- Craft Manifest: READY
- POV: 에이든 단일
- Scene Density: S형
- Primary Craft: 제한자원 선택
- Status: READY FOR A18 NOW

## 10. D10 Findings

Initial S1:

1. Canon Router 혼동
2. 종교 장면 상세 부족
3. 조연 dossier 불균형
4. 보조 POV 실제 배치 부재
5. Context Pack 부재
6. 상황별 작법 선택 체계 부재

Final:

- S0: 0
- S1: 0
- S2: 2
- S3: 지속 개선

## 11. GitHub Verification

- PR #25 state: CLOSED
- PR #25 merged: TRUE
- D10 squash merge SHA: `a34113d538f9ec22b396fdf0193dd82ab19328ec`
- changed files: 28
- additions: 4,603
- deletions: 315
- manuscript prose changed: NO
- main verified:
  - [`AI_PROJECT.md`](../../AI_PROJECT.md)
  - [`AGENTS.md`](../../AGENTS.md)
  - [`CLAUDE.md`](../../CLAUDE.md)
  - Agent Registry
  - Storycraft / Context Pack / Sentence Narrator skills
  - E001 / E002 Context Packs
  - Orchestration Harness
  - D10 Domain Readiness Audit

## Final Verdict

**PASS — 모델중립 정본 우선 오케스트라가 `main`에 병합됐고, 세계관·설정집·설계도·작법·POV를 회차 원고에 호출하는 구조가 준비됐다.**
