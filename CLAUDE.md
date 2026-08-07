# CLAUDE.md — Claude Code Bootstrap Router

Status: NON-CANON ROUTER  
Project: 《왕국은 과거를 먹고 산다》 / `ReturnToThePast`

## Authority Warning

이 파일은 Claude Code용 진입점일 뿐 작품 정본이 아니다.

- 작가 결정·Canon Constitution·Amendment·Decision Log·State Ledger를 덮어쓸 수 없다.
- 이 파일에만 존재하는 사실은 작품 설정으로 사용할 수 없다.
- 설정·인물·아이템·종교·결말을 이 요약만 보고 작성하지 않는다.
- 충돌은 A02 Canon Controller와 정본 권한계층으로 해결한다.

정본 순서:

`작가 결정 → Canon Constitution → Amendment/Errata → Decision Log → State Ledger → Domain Bible → Story Architecture → Craft/POV/CP → Manuscript → Legacy`

## Start Here

1. `/AI_PROJECT.md`
2. `docs/00_project/canon-constitution-v1.md`
3. 최신 Canon Amendment와 `docs/00_project/decision-log.md`
4. `docs/00_project/GATE_STATUS.md`
5. `.agent/orchestra/governance-and-routing-v2.md`
6. `.agent/orchestra/agent-registry.md`
7. 작업 유형에 필요한 Domain Bible
8. 관련 Story Architecture
9. 해당 Context Pack과 Harness

Codex는 `/AGENTS.md`, ChatGPT 프로젝트는 `/AI_PROJECT.md`를 진입점으로 사용한다. 세 라우터는 정본을 복사하지 않고 같은 원본을 가리킨다.

## Orchestration

- A00 Story Orchestrator: 요청 분류·호출·정족수·중단
- A02 Canon Controller: 권한·충돌·변경관리
- A20 Storycraft Director: 상황별 작법 선택
- A21 Context Pack Compiler: 필요한 정본 묶음·Hook·Harness
- A18 Prose: 승인된 CP와 설계만 원고로 구현
- A19 Prose Audit: 자연스러운 한국어·낭독·이름·호칭·행동 검사
- A16 Red Team: S0/S1 차단
- A17 GitHub Verifier: 실제 PR·merge·SHA 확인

전체 역할과 승인범위는 `.agent/orchestra/agent-registry.md`를 따른다.

## Active Skills

- `.agent/skills/context-pack-compiler/SKILL.md`
- `.agent/skills/storycraft-orchestrator/SKILL.md`
- `.agent/skills/sentence-narrator/SKILL.md`

Skill은 절차이며 정본 승인권이 없다.

## Context Packs

- `.agent/context-packs/README.md`
- `.agent/context-packs/templates/episode-context-pack-template.md`

Episode CP가 READY가 아니면 A18을 호출하지 않는다. CP는 정본이 아니며 원본 경로와 기준 ref를 반드시 가진다.

## Harness

`docs/13_writing_harness/orchestration-harness-v2.md`

실행 흐름:

`Authority Resolve → CP Compile → Domain Readiness → Craft Manifest → POV/Scene Architecture → Draft/Design → Prose Audit → Canon/Continuity → Reader/Red Team → GitHub Verification → State Mutation`

## Production State

정확한 상태는 `docs/00_project/GATE_STATUS.md`만 따른다. 이 파일의 요약과 Gate 문서가 다르면 Gate 문서가 우선한다.

## Repository Rules

- 새 원고는 `manuscript/`에만 작성
- `Drafts/`는 LEGACY / REFERENCE ONLY
- 한 화마다 별도 branch / PR / squash merge
- 정본 변경은 Amendment와 Decision Log 필요
- CP 안에서 새 설정 생성 금지
- S0/S1 또는 stale CP가 있으면 집필·병합 중단
- GitHub 완료는 A17이 main에서 재확인한 상태만 보고
