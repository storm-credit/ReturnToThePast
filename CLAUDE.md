# CLAUDE.md — Bootstrap Router

Status: NON-CANON ROUTER  
Project: 《왕국은 과거를 먹고 산다》 / `ReturnToThePast`

## Authority Warning

이 파일은 최상위 정본이 아니다.

- 작가 결정·Canon Constitution·Amendment·Decision Log·State Ledger를 덮어쓸 수 없다.
- 이 파일에만 있는 사실은 작품 정본으로 사용할 수 없다.
- 설정·인물·아이템·종교·결말을 이 파일의 요약만 보고 쓰지 않는다.
- 충돌은 A02 Canon Controller와 정본 권한계층으로 해결한다.

권한 구조:

`작가 결정 → Canon Constitution → Amendment/Errata → Decision Log → State Ledger → Domain Bible → Story Architecture → Craft/POV/CP → Manuscript → Legacy`

## Start Here

모든 작업은 다음 순서로 시작한다.

1. `docs/00_project/canon-constitution-v1.md`
2. 최신 Canon Amendment와 `docs/00_project/decision-log.md`
3. `docs/00_project/GATE_STATUS.md`
4. `.agent/orchestra/governance-and-routing-v2.md`
5. `.agent/orchestra/agent-registry.md`
6. `.agent/orchestra/expert-contracts-v1.md`
7. 작업 유형에 필요한 Domain Bible
8. 관련 Story Architecture
9. 해당 CP와 Harness

## Orchestration

- A00 Story Orchestrator: 작업 분류·호출·정족수·중단
- A02 Canon Controller: 권한·충돌·변경관리
- A20 Storycraft Director: 상황별 작법 선택
- A21 Context Pack Compiler: 필요한 정본 묶음·Hook·Harness
- A18 Prose: 승인된 CP와 설계만 원고로 구현
- A19 Prose Audit: 자연스러운 한국어·낭독·이름·호칭·행동 검사
- A16 Red Team: S0/S1 차단
- A17 GitHub Verifier: 실제 PR·merge·SHA 확인

전체 역할은 `.agent/orchestra/agent-registry.md`를 따른다.

## Active Skills

- `.agent/skills/storycraft-orchestrator/SKILL.md`
- `.agent/skills/context-pack-compiler/SKILL.md`
- `.agent/skills/sentence-narrator/SKILL.md`

스킬은 절차이며 정본 승인권이 없다.

## Context Packs

CP는 작업별 읽기 전용 묶음이다.

- `.agent/context-packs/README.md`
- `.agent/context-packs/templates/episode-context-pack-template.md`

Episode CP가 READY가 아니면 A18을 호출하지 않는다.

## Harness

- `docs/13_writing_harness/orchestration-harness-v2.md`

핵심 흐름:

`Authority Resolve → CP Compile → Domain Readiness → Craft Manifest → Scene Architecture → Draft → Prose Audit → Canon/Continuity → Reader/Red Team → GitHub → State Mutation`

## Current Production State

정확한 상태는 `docs/00_project/GATE_STATUS.md`만 따른다.

이 파일의 상태 요약이 Gate 문서와 다르면 Gate 문서가 우선한다.

## Repository Rules

- 새 원고는 `manuscript/`에만 작성
- `Drafts/`는 LEGACY / REFERENCE ONLY
- 한 화마다 별도 branch / PR / squash merge
- 정본 변경은 Amendment와 Decision Log 필요
- CP에만 새 설정을 추가하지 않음
- S0/S1 또는 stale CP가 있으면 집필·병합 중단
- GitHub 완료는 A17이 main에서 재확인한 상태만 보고
