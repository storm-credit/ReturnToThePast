# FINAL D10 ORCHESTRATION STATUS

Status: **D10 READY — PENDING GITHUB MERGE VERIFICATION**  
Owner: A00 / A02 / A16 / A17 / A20 / A21  
Scope: 정본 권한, 모델별 라우터, 에이전트, Skills, Context Packs, Harness, 분야별 상세도, POV, E001 소급감사

## 1. Architecture Decision

검토한 네 가지 운영안:

1. Claude·GPT·Codex 파일에 전체 규칙 각각 복제
2. 특정 채팅 프로젝트 지침에 전체 규칙 집중
3. 하나의 거대한 오케스트라 프롬프트가 모든 권한 보유
4. 모델중립 정본 우선 계층형 오케스트라

선택: **4안**

선택 이유:

- 모델을 바꿔도 같은 정본을 읽음
- `CLAUDE.md`가 최상위 정본이 되는 문제 방지
- 설정 사실, 작법 절차, 자료 묶음, 원고 구현을 분리
- 한 에이전트의 오류가 전체 Canon으로 승격되는 것을 차단
- ChatGPT·Codex·Claude Code를 같은 저장소에서 운용 가능

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

다음은 정본이 아니다.

- `AI_PROJECT.md`
- `CLAUDE.md`
- `AGENTS.md`
- Agent Contract
- Skill
- Harness
- Context Pack

## 3. Model Routers

### Common

- `/AI_PROJECT.md`
- 역할: 모델중립 프로젝트 진입점
- 권한: NON-CANON

### Claude Code

- `/CLAUDE.md`
- 역할: Claude 전용 Bootstrap Router
- 권한: NON-CANON

### Codex

- `/AGENTS.md`
- 역할: Codex 전용 Bootstrap Router
- 권한: NON-CANON

### ChatGPT Project

- 프로젝트 지침은 `/AI_PROJECT.md`와 정본을 읽도록 안내
- 대화나 프로젝트 지침만으로 Canon 변경 금지

## 4. Active Orchestration Agents

- A00 Story Orchestrator — 작업 분류·호출·정족수·중단
- A01 Architecture PM — 범위·의존성·완료조건
- A02 Canon Controller — 권한·충돌·변경관리
- A03–A17 Domain / Audit / GitHub Agents
- A18 Prose Agent — READY CP만 원고화
- A19 Sentence Narration & Korean Prose Audit
- A20 Storycraft Director — 상황별 작법 Manifest
- A21 Context Pack Compiler & Harness Runner

권한분산:

- A00은 총괄하지만 사실을 만들지 않음
- A02는 정본을 관리하지만 재미를 단독 승인하지 않음
- A20은 작법을 고르지만 사건을 바꾸지 않음
- A21은 자료를 묶지만 CP를 정본으로 만들지 않음
- A18은 설정을 즉석 생성하지 않음
- A16은 S0/S1 상태에서 PASS 금지
- A17 확인 전 GitHub 완료 보고 금지

## 5. Active Skills

### context-pack-compiler

- 필요한 정본 원본경로·상태·기준 ref 추출
- Domain 누락·stale·충돌 검사
- Series/Volume/Subact/Episode CP 생성

### storycraft-orchestrator

- 상황에 맞는 중심 작법 1개 + 보조 최대 2개 선택
- 국소완결, 장면–반응, 정보간극, 공정단서, 정치·전투·생활 후과를 선택 적용
- 동일 작법·훅 반복 차단

### sentence-narrator

- 한 문장 낭독
- 자연스러운 한국어·번역체·묘사·공간·행동·이름·호칭·발음 검사

Skill은 정본 승인권이 없다.

## 6. Context Pack Structure

- Series CP
- Grand Act CP
- Volume CP
- Subact CP
- Episode CP

Episode CP 필수:

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

Completed examples:

- E001 Context Pack — RETRO-COMPILED / READY
- E002 Context Pack — READY BEFORE DRAFT

## 7. Harness

Main Harness:

`docs/13_writing_harness/orchestration-harness-v2.md`

Execution:

1. Authority Resolve
2. CP Compile
3. Domain Readiness
4. Craft Manifest
5. POV / Scene Architecture
6. Draft or Design
7. Sentence / Prose Audit
8. Canon / Continuity
9. Reader Experience / Red Team
10. GitHub Verification
11. State Mutation

누락 단계가 있으면 다음 단계로 넘어가지 않는다.

## 8. Domain Readiness

### READY

- 시간여행·기억·인과
- 지리·수도·이동·물류
- 생활문화·언어·달력
- 인구·경제·직업·가격
- 군사·외교·보급
- 종족·문화
- 종교·신화·의례·성직계급·구휼·재판
- 기관·법·행정
- 세력·대립자
- C01–C30 인물·관계·목소리·부재 중 행동
- R01–R12 유산
- B01–B05 주권신수
- 미스터리·복선·맥거핀
- 영구손실
- Grand Act / Volume / Arc / Subact / Episode 인과
- 장면밀도·훅

### Conditional S2

- 일반 소품이 반복 사용될 경우 별도 prop index 승격
- 실제 원고 반응에 따라 보조 POV 빈도 미세조정

## 9. Secondary POV

- P1 단일 보조 POV 회차: 30화
- P2 다중 POV 회차: 15화
- P3 제한 관찰자 삽입: 8개

허용 목적:

- 에이든이 볼 수 없는 독립 선택
- 지역·기관·F1의 실제 효용과 피해
- 동시 사건
- 잘못된 판단을 정답누설 없이 다른 각도에서 제시

보조 POV는 정보상한·재합류 회차·상태변화를 가진다.

## 10. E001 Result

- Manuscript: main merged
- PR: #24
- Merge SHA: `97d9195913a53eba96d7cde4360429125ee7c69b`
- Context Pack: READY / RETRO
- Craft Manifest: READY / RETRO
- D10 Retro Audit: PASS
- Manuscript rewrite required: NO
- S0: 0
- S1: 0

## 11. E002 Readiness

- Title: 여섯 개의 승인
- CP: READY
- Craft Manifest: READY
- POV: 에이든 단일
- Scene Density: S형
- Primary Craft: 제한자원 선택
- A18: D10 merge 뒤 호출 가능

## 12. D10 Severity

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

## 13. GitHub Verification

현재 문서는 merge 전 상태다.

A17은 다음을 완료해야 최종 `MERGED / MAIN VERIFIED`로 갱신한다.

- branch가 main보다 `behind_by=0`
- 변경파일 범위 확인
- PR 생성
- squash merge
- PR `closed / merged=true`
- 실제 merge SHA 기록
- main에서 `AI_PROJECT.md`, `AGENTS.md`, `CLAUDE.md`, Agent Registry, Skills, CP, Harness, D10 Audit 재확인

## Final Pre-Merge Verdict

**PASS — D10 구조와 상세도 보강은 완료됐으며 GitHub 병합검증만 남음.**
