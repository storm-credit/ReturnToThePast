# Minimum Action Agent OS Integration — Independent Critic v1

Status: INDEPENDENT REVIEW  
Date: 2026-08-19  
Review Target Branch: `agent/adopt-minimum-action-agent-os`  
Base Main: `c3130ba8ccb095959d02d8bec8862e1a37e3e6cb`

## Acceptance Target

다음 요구만 기준으로 검증한다.

1. 기존 Canon / Spec / 원고 / 연구설계를 변경하지 않는다.
2. 기존 Agent를 삭제하거나 전체 수를 5 이하로 줄이지 않는다.
3. Local Action Space만 기본 `<= 5`로 관리한다.
4. 기존 절차가 있으면 중복 Agent/Skill/Rule을 만들지 않는다.
5. `CLAUDE.md`에는 짧은 adoption rule만 두고 OS 전체를 복사하지 않는다.
6. 프로젝트 도메인 정본이 공통 OS보다 우선한다.
7. 변경 후 각 주요 router/node의 직접 action surface가 5 이하로 설명 가능해야 한다.
8. 독립 평가와 남은 위험을 명시해야 한다.

## Evidence Reviewed

- branch compare: `ahead_by=5`, `behind_by=0`
- changed files before this critic report:
  - `.agent/orchestra/governance-and-routing-v2.md`
  - `.agent/orchestra/minimum-action-agent-os-adoption-v1.md`
  - `CLAUDE.md`
  - `AI_PROJECT.md`
  - `AGENTS.md`
- unchanged by branch compare:
  - Canon Constitution
  - Decision Log
  - Domain Bible
  - Story Architecture
  - Agent Registry
  - Skill implementation files
  - Harness implementation
  - Manuscript
  - CI workflow / validator code

## Independent Findings

### Blocking Findings

**없음.**

### Requirement Checks

| Requirement | Result | Evidence |
|---|---|---|
| Canon/Spec/Manuscript 보존 | PASS | compare에 도메인 정본·원고 파일 변경 0 |
| 기존 Agent 보존 | PASS | `agent-registry.md` 변경 0, Agent add/remove 0 |
| 전체 Agent 수 제한 금지 | PASS | adoption/governance에 global limit 아님을 명시 |
| Local Action Space `<=5` | PASS | A00 5 lanes; lane별 2/5/5/5/4 |
| 6개 optional Item specialists 해소 | PASS | L2 최대 3 → L3 최대 3으로 순차 선택 |
| Skill 중복 생성 금지 | PASS | Skill file 추가/삭제 0, 기존 절차 KEEP |
| CLAUDE 얇은 router 유지 | PASS | OS 본문 복사 없이 짧은 adoption + local pointer |
| 모델중립 적용 | PASS | `AI_PROJECT.md` 포인터 + `AGENTS.md` lane 해석 추가 |
| 독립 평가 보존 | PASS | 기존 A16 유지, 새 Critic Agent 생성 0 |
| GitHub freshness | PASS | branch `behind_by=0` |

## Non-Blocking Risks

### R1 — Runtime MCP Exposure Is Not Hard-Enforced

Severity: MEDIUM

저장소 문서는 A17의 GitHub action surface를 5개 coherent verbs로 제한하지만, 실제 Claude Code/ChatGPT client가 raw MCP 함수를 전역으로 노출하는지 여부는 repository Markdown만으로 통제할 수 없다.

이 문제는 설계 실패가 아니라 **runtime enforcement gap**이다.

Smallest corrective action:
- 실제 Claude Code 환경에서 plugin/tool exposure audit 1회 수행.
- raw peer actions가 5를 초과하면 tool allowlist 또는 on-demand loading을 사용.

### R2 — `.claude/` Directory Is Absent

Severity: LOW

현재 프로젝트는 `.agent/` 기반이며 `.claude/`가 없다. 이번 변경에서 중복 구조를 만들지 않은 것은 요구에 맞다. 다만 Claude Code project-specific permission/tool configuration을 나중에 hard-enforce하려면 `.claude/`가 필요할 수 있다.

Smallest corrective action:
- runtime audit에서 hard enforcement 필요성이 확인될 때만 추가한다.

### R3 — Production Status Drift Is Separate and Still Unmerged

Severity: MEDIUM / OUT OF OS SCOPE

main의 `GATE_STATUS.md` / `manuscript/PROGRESS.md`가 실제 E088 main 상태와 어긋난 문제는 별도 PR #123에서 수정 중이다. OS branch가 이를 중복 수정하지 않은 것은 scope preservation 측면에서는 맞지만, 두 PR이 모두 미병합이면 새 세션에서 낡은 상태를 읽을 가능성은 남는다.

Smallest corrective action:
- PR #123을 별도 검토 후 병합 여부 결정.

### R4 — Harness Footer Contains Stale Production Snapshot

Severity: LOW / OUT OF OS SCOPE

`orchestration-harness-v2.md` 말미의 현재 집필 상태가 오래된 복사본이다. Harness 본체는 정상이나 상태 중복이 drift를 만들 수 있다.

Smallest corrective action:
- 상태 정리 작업에서 해당 부분을 `GATE_STATUS.md` 포인터로 바꾼다. OS adoption PR에는 섞지 않는다.

## Critic Verdict

**PASS_WITH_RISKS**

이유:

- 요구한 최소 적용은 충족한다.
- 기존 구조·정본·Agent·Skill을 보존했다.
- 초과한 flat surface는 Agent 삭제 없이 5개 lane과 lazy-load 규칙으로 축소했다.
- 남은 문제는 실제 runtime MCP 노출과 별도 상태 drift이며, 이번 문서 변경 자체의 blocking defect는 아니다.

## Recommended Next Step

1. 이 OS adoption PR을 작가 검토 대상으로 유지하고 main에는 자동 병합하지 않는다.
2. 실제 Claude Code runtime에서 Local Action Space/tool exposure를 1회 검증한다.
3. 별도 PR #123의 production-state drift를 정리한 뒤 E089 이후 집필 복구를 진행한다.
