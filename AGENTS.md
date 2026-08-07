# AGENTS.md — Codex Bootstrap Router

Status: NON-CANON ROUTER  
Applies To: repository-wide Codex work

## Authority

이 파일은 정본이 아니다. Codex 작업을 저장소의 모델중립 구조로 연결하는 진입점이다.

먼저 `/AI_PROJECT.md`를 읽는다. 작품 사실과 변경권한은 다음 순서를 따른다.

`작가 결정 → Canon Constitution → Amendment/Errata → Decision Log → State Ledger → Domain Bible → Story Architecture → Craft/POV/CP → Manuscript → Legacy`

`AGENTS.md`, `CLAUDE.md`, Skill, Harness, CP는 상위 정본을 덮어쓸 수 없다.

## Required Reads

1. `/AI_PROJECT.md`
2. `docs/00_project/canon-constitution-v1.md`
3. 최신 Canon Amendment와 `docs/00_project/decision-log.md`
4. `docs/00_project/GATE_STATUS.md`
5. `.agent/orchestra/governance-and-routing-v2.md`
6. `.agent/orchestra/agent-registry.md`
7. 작업에 필요한 Domain Bible
8. 관련 Story Architecture
9. 해당 Context Pack과 Harness

## Routing

- A00: 요청분류·호출순서·승인 정족수
- A02: Canon 충돌과 변경관리
- A20: 상황별 Storycraft Manifest
- A21: Context Pack 컴파일·출처·신선도 검사
- A18: 승인된 설계의 원고 구현
- A19: 한국어·낭독·이름·호칭·행동 검사
- A16: S0/S1 Red Team
- A17: GitHub 상태검증

## Active Skills

- `.agent/skills/storycraft-orchestrator/SKILL.md`
- `.agent/skills/context-pack-compiler/SKILL.md`
- `.agent/skills/sentence-narrator/SKILL.md`
- `.agent/skills/human-prose-audit/SKILL.md`

Skill은 절차이고 정본 승인권이 없다.

`human-prose-audit`은 AI가 `AUTHOR REVIEW READY`까지만 판정한다. `HUMAN PROSE PASS`는 작가 승인 없이는 기록하지 않는다.

## Harness

`docs/13_writing_harness/orchestration-harness-v2.md`

원고 작업은 READY Episode CP, Storycraft Manifest, POV allocation, State Mutation Plan 없이는 시작하지 않는다.

원고 구현 뒤에는 반드시 다음 순서를 거친다.

1. `sentence-narrator`
2. `human-prose-audit`
3. Canon / Continuity / Reader / Red Team
4. 작가 Human Prose 검토

작가가 AI 티를 지적한 원고는 구조·정본 PASS만으로 다음 화를 진행하지 않는다.

## Repository Boundaries

- 새 원고: `manuscript/`
- 기존 `Drafts/`: LEGACY / REFERENCE ONLY
- 정본 변경: Amendment + Decision Log + 담당 quorum
- CP 안에서 새 설정 생성 금지
- 첫 등장 인물·아이템·종교·기관은 해당 dossier를 확인
- S0/S1이 있으면 푸시·병합 금지
- Human Prose Audit 미완료 상태에서는 다음 화 집필 금지

## GitHub Workflow

- latest main 확인
- 작업 branch 생성
- 의도한 파일만 변경
- compare에서 `behind_by=0`
- PR 생성
- squash merge
- PR의 `closed/merged=true`와 실제 merge SHA 확인
- main 파일 재확인

## Current Production

정확한 완료 회차와 다음 생산 단위는 다음 파일만 따른다.

- `docs/00_project/GATE_STATUS.md`
- `manuscript/PROGRESS.md`

이 라우터에는 회차별 상태를 복제하지 않는다.
