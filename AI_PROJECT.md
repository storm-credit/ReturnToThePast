# AI_PROJECT.md — Model-Neutral Project Entry

Status: NON-CANON PROJECT ROUTER  
Project: 《왕국은 과거를 먹고 산다》 (`ReturnToThePast`)

## 1. Purpose

이 파일은 ChatGPT, Codex, Claude Code 및 다른 AI 도구가 동일한 정본과 실행구조를 찾도록 안내하는 모델중립 진입점이다.

이 파일은 작품 정본이 아니다.

- 세계관 사실을 새로 만들 수 없다.
- Canon Constitution, Amendment, Decision Log, State Ledger를 덮어쓸 수 없다.
- 이 파일의 요약과 정본이 충돌하면 정본을 따른다.
- 세부 설정은 반드시 원본 Domain Bible에서 읽는다.

## 2. Authority Order

1. 현재 작가가 명시적으로 확정한 결정
2. `docs/00_project/canon-constitution-v1.md`
3. 최신 Canon Amendment / Errata
4. `docs/00_project/decision-log.md`
5. 활성 State Ledger와 Gate Status
6. 분야별 Domain Bible
7. Story Architecture
8. Craft / POV / Context Pack
9. Manuscript
10. Legacy / Reference

라우터·에이전트·스킬·하네스·CP에는 정본 승인권이 없다.

## 3. Tool-Specific Routers

- Claude Code: `/CLAUDE.md`
- Codex: `/AGENTS.md`
- ChatGPT Project: 이 파일과 저장소 정본을 프로젝트 지침에서 참조

도구별 라우터는 이 파일과 Governance를 가리키는 얇은 진입점이어야 한다. 정본 내용을 복사해 별도 버전으로 유지하지 않는다.

## 4. Required Startup Read

모든 작업은 다음을 확인한다.

1. 이 파일
2. `docs/00_project/canon-constitution-v1.md`
3. 최신 Amendment와 `docs/00_project/decision-log.md`
4. `docs/00_project/GATE_STATUS.md`
5. `.agent/orchestra/governance-and-routing-v2.md`
6. `.agent/orchestra/agent-registry.md`
7. 작업 유형별 Domain Bible
8. 관련 Story Architecture
9. Context Pack과 Harness

## 5. Orchestration Roles

- A00 Story Orchestrator: 요청분류, 호출순서, 정족수, 중단조건 관리
- A02 Canon Controller: 정본 우선순위와 충돌 판정
- A20 Storycraft Director: 상황별 작법 조합 선택
- A21 Context Pack Compiler: 필요한 정본만 출처와 함께 묶고 누락검사
- A18 Prose Agent: 승인된 CP와 설계만 원고화
- A19 Sentence Narration & Korean Prose Audit: 문장·낭독·호칭·이름·행동 감사
- A16 Red Team: S0/S1 차단
- A17 GitHub State Verifier: branch/PR/merge/SHA/main 실재 확인

전체 역할과 승인범위는 `.agent/orchestra/agent-registry.md`와 `expert-contracts-v1.md`를 따른다.

## 6. Active Skills

- `.agent/skills/storycraft-orchestrator/SKILL.md`
- `.agent/skills/context-pack-compiler/SKILL.md`
- `.agent/skills/sentence-narrator/SKILL.md`

Skill은 반복 절차다. 설정·사건·결말을 독자적으로 승인하거나 변경할 수 없다.

## 7. Context Pack Rule

작업 전 CP를 컴파일한다.

- Series CP
- Grand Act CP
- Volume CP
- Subact CP
- Episode CP

CP는 원본 경로, 기준 commit/ref, 추출한 사실, 정보상한, 현재 상태를 기록한다. CP 안에서 새 설정을 만들지 않는다. 빠진 정보는 Domain Bible 단계로 되돌린다.

## 8. Harness

주 실행 하네스:

`docs/13_writing_harness/orchestration-harness-v2.md`

실행 순서:

`Authority Resolve → CP Compile → Domain Readiness → Craft Manifest → POV/Scene Architecture → Draft/Design → Prose Audit → Canon/Continuity → Reader/Red Team → GitHub Verification → State Mutation`

## 9. Current State

정확한 생산상태는 `docs/00_project/GATE_STATUS.md`만 따른다.

D10 감사 중에는 E001을 PROVISIONAL로 보존하며, E002 이후 집필은 Domain Readiness, Secondary POV Allocation, CP 역감사가 완료될 때까지 진행하지 않는다.

## 10. Hard Stops

다음 중 하나라도 있으면 원고 또는 설계 승격을 중단한다.

- 정본 충돌 미해결
- 필요한 Domain Bible 부재
- stale 또는 출처 없는 CP
- 작법 Manifest 부재
- POV 정보상한·재합류 상태 부재
- 상태장부 갱신계획 부재
- S0 또는 S1 미해결
- branch가 main보다 뒤처짐

## 11. GitHub Rule

- 최신 main에서 branch 생성
- 의도한 범위만 변경
- compare에서 `behind_by=0`
- PR 생성
- squash merge
- PR `closed/merged=true` 확인
- 실제 merge SHA 기록
- main의 대표파일 재확인

예상 상태를 실제 상태로 보고하지 않는다.
