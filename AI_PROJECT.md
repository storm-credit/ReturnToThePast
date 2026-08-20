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
2. [`docs/00_project/canon-constitution-v1.md`](docs/00_project/canon-constitution-v1.md)
3. 최신 Canon Amendment / Errata
4. [`docs/00_project/decision-log.md`](docs/00_project/decision-log.md)
5. 활성 State Ledger와 Gate Status
6. 분야별 Domain Bible
7. Story Architecture
8. Craft / POV / Context Pack
9. Manuscript
10. Legacy / Reference

라우터·에이전트·스킬·하네스·CP에는 정본 승인권이 없다.

## 3. Tool-Specific Routers

- Claude Code: [`/CLAUDE.md`](CLAUDE.md)
- Codex: [`/AGENTS.md`](AGENTS.md)
- ChatGPT Project: 이 파일과 저장소 정본을 프로젝트 지침에서 참조

도구별 라우터는 이 파일과 Governance를 가리키는 얇은 진입점이어야 한다. 정본 내용을 복사해 별도 버전으로 유지하지 않는다.

## 4. Required Startup Read

모든 작업은 다음을 확인한다.

1. 이 파일
2. [`docs/00_project/canon-constitution-v1.md`](docs/00_project/canon-constitution-v1.md)
3. 최신 Amendment와 [`docs/00_project/decision-log.md`](docs/00_project/decision-log.md)
4. [`docs/00_project/GATE_STATUS.md`](docs/00_project/GATE_STATUS.md)
5. [`manuscript/PROGRESS.md`](manuscript/PROGRESS.md)
6. [`docs/00_project/PROJECT_COMPLETION_SCORECARD_20260820.md`](docs/00_project/PROJECT_COMPLETION_SCORECARD_20260820.md)
7. [`.agent/orchestra/governance-and-routing-v2.md`](.agent/orchestra/governance-and-routing-v2.md)
8. [`.agent/orchestra/agent-registry.md`](.agent/orchestra/agent-registry.md)
9. 작업 유형별 Domain Bible
10. 관련 Story Architecture
11. 관련 Context Pack과 Harness

## 5. Legacy Quarantine — Mandatory

레거시 격리 원본:
[`docs/00_project/legacy-quarantine-index-v1.md`](docs/00_project/legacy-quarantine-index-v1.md)

다음은 **startup / Canon / current state / current ending source로 사용 금지**다.

- `outline/`
- `Drafts/`
- `Ending_Scenarios.md`
- `Lore_Bible_Master_Index.md`
- `02_SESSION_SUMMARY.md`
- DEPRECATED로 표시된 root legacy files

`Guidelines/`는 현재 `.agent/skills/`와 `docs/13_writing_harness/`보다 우선하지 않는다. 활성 라우터가 특정 파일을 명시적으로 가리킬 때만 보조자료로 사용한다.

GitHub 검색에서 Legacy가 먼저 나와도 다음 요소를 현재 정본으로 가져오지 않는다.

- 172회차·무한 회귀·죽음 리셋
- 현대 환생 / 신·영원한 관찰자 엔딩
- 발타자르를 C05 현재 이름으로 사용
- 12사도·창백한 의회·영시·세라핌 등 구 세계관을 자동 복구
- `F1 지휘관`, `F1 친구 슬롯`, `[WORKING]` 표기를 최신 C01–C30 이름보다 우선

인물명은 [`docs/05_characters/cast-canon-index-v2.md`](docs/05_characters/cast-canon-index-v2.md)가 우선한다.

## 6. Orchestration Roles

- A00 Story Orchestrator: 요청분류, 호출순서, 정족수, 중단조건 관리
- A02 Canon Controller: 정본 우선순위와 충돌 판정
- A20 Storycraft Director: 상황별 작법 조합 선택
- A21 Context Pack Compiler: 필요한 정본만 출처와 함께 묶고 누락검사
- A18 Prose Agent: 승인된 CP와 설계만 원고화
- A19 Sentence Narration & Korean Prose Audit: 문장·낭독·호칭·이름·행동 감사
- A16 Red Team: S0/S1 차단
- A17 GitHub State Verifier: branch/PR/merge/SHA/main 실재 확인

전체 역할과 승인범위는 [`.agent/orchestra/agent-registry.md`](.agent/orchestra/agent-registry.md)와 [`expert-contracts-v1.md`](.agent/orchestra/expert-contracts-v1.md)를 따른다.

## 7. Active Skills

- [`.agent/skills/storycraft-orchestrator/SKILL.md`](.agent/skills/storycraft-orchestrator/SKILL.md)
- [`.agent/skills/context-pack-compiler/SKILL.md`](.agent/skills/context-pack-compiler/SKILL.md)
- [`.agent/skills/sentence-narrator/SKILL.md`](.agent/skills/sentence-narrator/SKILL.md)
- [`.agent/skills/human-prose-audit/SKILL.md`](.agent/skills/human-prose-audit/SKILL.md)
- [`.agent/skills/naming-audit/SKILL.md`](.agent/skills/naming-audit/SKILL.md)

Skill은 반복 절차다. 설정·사건·결말을 독자적으로 승인하거나 변경할 수 없다.

`human-prose-audit`은 AI 자체로 `AUTHOR REVIEW READY`까지만 판정할 수 있다. 최종 `HUMAN PROSE PASS`는 작가가 실제 원고를 읽고 승인한 경우에만 기록한다.

`naming-audit`은 한국 웹소설 판타지 명명 규칙을 검사하지만 기존 정본 이름을 작가 승인 없이 변경하지 않는다.

## 8. Context Pack Rule

작업 전 CP를 컴파일한다.

- Series CP
- Grand Act CP
- Volume CP
- Subact CP
- Episode CP

CP는 원본 경로, 기준 commit/ref, 추출한 사실, 정보상한, 현재 상태를 기록한다. CP 안에서 새 설정을 만들지 않는다. 빠진 정보는 Domain Bible 단계로 되돌린다.

Legacy 자료가 필요한 경우 CP에 provenance를 표시하고 현재 Canon/Architecture와 재검증한다.

## 9. Harness

주 실행 하네스:

[`docs/13_writing_harness/orchestration-harness-v2.md`](docs/13_writing_harness/orchestration-harness-v2.md)

실행 순서:

`Authority Resolve → CP Compile → Domain Readiness → Craft Manifest → POV/Scene Architecture → Draft/Design → Sentence/Prose Audit → Human Prose Audit → Canon/Continuity → Reader/Red Team → Author Review → GitHub Verification → State Mutation`

작가가 AI 티를 지적한 원고는 구조·정본 검사를 통과했더라도 다음 화로 진행하지 않는다.

## 10. Current State Routing

정확한 현재 집필 회차·완료 PR·다음 작업은 다음을 따른다.

- [`docs/00_project/GATE_STATUS.md`](docs/00_project/GATE_STATUS.md)
- [`manuscript/PROGRESS.md`](manuscript/PROGRESS.md)
- [`docs/00_project/PROJECT_COMPLETION_SCORECARD_20260820.md`](docs/00_project/PROJECT_COMPLETION_SCORECARD_20260820.md)

이 라우터에는 회차별 상태와 main SHA를 중복 하드코딩하지 않는다.

## 11. Hard Stops

다음 중 하나라도 있으면 원고 또는 설계 승격을 중단한다.

- 정본 충돌 미해결
- 필요한 Domain Bible 부재
- stale 또는 출처 없는 CP
- 작법 Manifest 부재
- POV 정보상한·재합류 상태 부재
- 상태장부 갱신계획 부재
- S0 또는 S1 미해결
- Human Prose Audit 미실행
- 작가가 AI 티를 지적한 원고의 재검토 미완료
- 명명 감사에서 S1로 분류된 기관·종교·시간·장비 이름의 미해결
- 이전 화가 `AUTHOR REVIEW READY`에 도달하지 못함
- branch가 main보다 뒤처짐
- Legacy/DEPRECATED 문서를 현재 Canon/Ending/State 근거로 사용함

## 12. GitHub Rule

- 최신 main에서 branch 생성
- 의도한 범위만 변경
- compare에서 `behind_by=0`
- PR 생성
- main 머지는 작가의 명시적 승인 후에만 수행
- 병합 시 PR `closed/merged=true` 확인
- 실제 merge SHA 기록
- main의 대표파일 재확인

예상 상태를 실제 상태로 보고하지 않는다.
