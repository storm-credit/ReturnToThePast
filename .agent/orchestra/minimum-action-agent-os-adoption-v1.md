# Minimum Action Agent OS Adoption v1

Status: CANON-OPERATIONS / WORKING-METHOD ONLY  
Owner: A00 Story Orchestrator / A16 Red Team  
Adopted Method Source: `storm-credit/minimum-action-agent-os`  
Base Main Audited: `c3130ba8ccb095959d02d8bec8862e1a37e3e6cb`  
Date: 2026-08-19

## 1. Scope

이 문서는 `minimum-action-agent-os`를 《왕국은 과거를 먹고 산다》 프로젝트의 **작업 방법론**으로만 적용한다.

변경하지 않는 것:

- Canon Constitution / Amendment / Errata / Decision Log의 작품 사실
- 5 Grand Acts × 15권 × 375화 구조
- 인물·세계관·시간법칙·결말·영구손실
- 기존 Agent의 전문 역할과 승인 정족수
- 기존 Skill / Harness / Context Pack의 기능
- 원고 본문

이 문서는 공통 OS의 내용을 프로젝트 정본으로 복사하지 않는다. 도메인 사실은 언제나 이 저장소의 권한계층이 우선한다.

## 2. Recovered Existing Structure

### Bootstrap / Router

- `CLAUDE.md`: Claude Code용 NON-CANON Bootstrap Router
- `AI_PROJECT.md`: 모델중립 NON-CANON Project Router
- `AGENTS.md`: Codex Bootstrap Router
- `.claude/`: **현재 저장소에 없음**. 기존 구조가 `.agent/` 중심이므로 이번 적용에서 새 `.claude/` 트리를 만들지 않는다.

### Agent / Skill / Rule

- `.agent/orchestra/agent-registry.md`: A00~A21 고정 역할
- `.agent/orchestra/governance-and-routing-v2.md`: 작업 유형별 호출·권한·Hook
- `.agent/orchestra/expert-contracts-v1.md`: 전문가 계약
- `.agent/experts/`: 별도 expert 문서
- `.agent/skills/`: 활성 Skill 5개 + disabled legacy `chrono-weaver`

현재 활성 Skill:

1. `storycraft-orchestrator`
2. `context-pack-compiler`
3. `sentence-narrator`
4. `human-prose-audit`
5. `naming-audit`

### Canon / Spec / Lock

- `docs/00_project/canon-constitution-v1.md`: 작품 정본 헌법, IMMUTABLE/HARD LOCK
- `docs/00_project/decision-log.md`: 작가 승인·운영 결정 이력
- 별도 `*FREEZE*` 파일은 현재 main 검색에서 확인되지 않았다.
- 이 프로젝트의 Freeze 역할은 Canon Constitution의 IMMUTABLE/HARD LOCK, 승인 Amendment/Errata, Decision Log와 분야별 Canon Level이 담당한다.

### Current Status

- `current-work-status.md`라는 파일은 현재 main에 없음.
- 현행 상태 원본은 `docs/00_project/GATE_STATUS.md`와 `manuscript/PROGRESS.md`다.
- 2026-08-19 감사 시점에 두 상태 문서가 실제 main 원고 진행과 어긋나 있었고, 별도 Draft PR #123에서 E088 기준 동기화가 제안되어 있다. 이 OS 적용 PR은 해당 상태 변경을 중복하지 않는다.

### Harness / Eval / Test

- `docs/13_writing_harness/orchestration-harness-v2.md`: H0~H11 실행 Harness
- `docs/13_writing_harness/working-process-and-meta-prompting-v1.md`: 의도 확인·맹점·함정·4안·레퍼런스·이탈·메타 프롬프팅
- `.github/workflows/manuscript-validate.yml`: PR 원고 검증 CI
- `.agent/skills/sentence-narrator/scripts/validate_manuscript.py`: 원고 기계 검증
- A16 Red Team / A14 Reader Experience / A13 Continuity / A17 GitHub Verification: 독립 평가 축

## 3. Existing Workflow Primitive Preservation

공통 OS와 겹치는 절차는 **새로 만들지 않는다**.

| OS Primitive | Existing Project Mechanism | Action |
|---|---|---|
| Intent Interview | `working-process-and-meta-prompting-v1.md` §1 | KEEP |
| Blindspot Scan | 같은 문서 §2 + A16 | KEEP |
| Preflight Trap Check | 같은 문서 §3 | KEEP |
| Four Alternatives | 같은 문서 §4 | KEEP |
| Exemplar Research | 같은 문서 §5 + A15 | KEEP |
| Meta Prompting | 같은 문서 §7 | KEEP |
| Independent Critic / Red Team | A16 + 별도 Red Team expert | KEEP |
| Harness / Golden Case | orchestration harness + validator/CI | KEEP |
| Plan Drift Log | 같은 문서 §6 + Decision Log | KEEP |
| State / Canon Update | H11 + Decision Log/State Ledger | KEEP |

Agents added for duplicate OS primitives: **0**  
Skills added for duplicate OS primitives: **0**

## 4. Audit Counting Rule

Local Action Space는 시스템 전체 Agent 수를 세지 않는다.

다음만 한 reasoning node의 선택지로 센다.

- 서로 대체 가능한 peer Agent
- 직접 고를 수 있는 Tool/MCP action
- 직접 실행 가능한 Skill
- 다른 callable action

다음은 선택지로 중복 계산하지 않는다.

- 반드시 순서대로 실행해야 하는 고정 pipeline 단계
- 승인 정족수처럼 선택이 아니라 필수인 Agent 집합
- 하나의 Skill 뒤에 숨은 내부 단계
- 문서 Read 목록
- Agent registry에 존재하지만 현재 node에 lazy-load되지 않은 Agent

## 5. Local Action Space Audit — Before Adoption

| Major Node | Direct Agent Choices | Direct Tool Choices | Direct Skill Choices | Other Callable | Total | Result |
|---|---:|---:|---:|---:|---:|---|
| `CLAUDE.md` bootstrap surface | 8 | 0 | 5 | 1 Harness | 14 | **REVIEW** |
| `AI_PROJECT.md` bootstrap surface | 8 | 0 | 5 | 1 Harness | 14 | **REVIEW** |
| `AGENTS.md` bootstrap surface | 8 | 0 | 5 | 1 Harness | 14 | **REVIEW** |
| A00 top routing surface | 7 task-route labels exposed as peer routes | 0 | 0 | 0 | 7 | **REVIEW** |
| World Detail domain selection | A03~A07 중 관련 1개를 고르는 최대 5개 | 0 | 0 | 0 | 5 | PASS |
| Character optional specialist selection | A05/A06/A09/A12/A19 최대 5개 | 0 | 0 | 0 | 5 | PASS |
| Item optional specialist selection | A04/A05/A06/A08/A11/A12 = 6 | 0 | 0 | 0 | 6 | **REVIEW** |
| Religion optional specialist selection | A03/A08/A09/A11/A12 = 5 | 0 | 0 | 0 | 5 | PASS |
| A19 prose audit node | 0 | 0 | `sentence-narrator`, `human-prose-audit` | 0 | 2 | PASS |
| A20 craft node | 0 | 0 | `storycraft-orchestrator` | 0 | 1 | PASS |
| A21 context/harness node | 0 | 0 | `context-pack-compiler` | Harness run | 2 | PASS |
| A15 naming/similarity node | 0 | 0 | `naming-audit` when naming work | 0 | 1 | PASS |
| A17 GitHub node | 0 | runtime-dependent raw MCP surface not bounded in repository docs | 0 | GitHub verification | unknown | **REVIEW** |

### Findings

1. **Global Agent count is not the problem.** A00~A21 역할은 실제 권한·컨텍스트·실패모드 경계를 갖고 있어 삭제 근거가 없다.
2. 문제는 Bootstrap 문서가 핵심 Agent 8개와 Skill 5개를 같은 화면에 나열해 직접 action menu처럼 읽힐 수 있다는 점이다.
3. A00 task type 7개 역시 분류 라벨이지만 callable route처럼 구현될 여지가 있다.
4. Item/Relic/Beast의 optional specialist 6개는 실제 peer 선택지로 해석되면 5를 초과한다.
5. A17은 저장소 문서만으로 실제 Claude/ChatGPT/GitHub MCP의 raw action 노출 수를 강제할 수 없다.

## 6. Minimal Routing Adaptation

기존 A01~A21은 그대로 두고 A00이 직접 보는 상위 라우팅을 아래 **5개 Lane**으로 제한한다.

```text
A00 Story Orchestrator
├─ L1 Authority & Planning     → A01, A02
├─ L2 World Systems            → A03, A04, A05, A06, A07
├─ L3 Narrative Systems        → A08, A09, A10, A11, A12
├─ L4 Evaluation & Release     → A13, A14, A15, A16, A17
└─ L5 Production               → A18, A19, A20, A21
```

Lane은 새 Agent가 아니다. 기존 Agent를 찾기 위한 **router grouping**이다.

### Lane Rules

- A00의 직접 선택지는 L1~L5 최대 5개다.
- Lane에 진입한 뒤에만 해당 Agent를 lazy-load한다.
- 한 작업이 여러 Lane을 필요로 하면 한 번에 평면적으로 펼치지 않고 Harness 순서에 따라 Lane을 이동한다.
- 고정 quorum은 그대로 유지한다. quorum 인원을 줄이지 않는다.
- `Story Architecture`의 A12+A07+A08+A09+A11+A13+A14+A16처럼 5명을 넘는 필수 참여자는 삭제하지 않는다. 이는 peer choice가 아니라 고정 검증 chain이며 Lane별로 순차 실행한다.
- Skill은 Bootstrap에서 바로 고르는 전역 Toolbelt가 아니라 소유 Agent 안에서 필요할 때만 load한다.

## 7. Optional Specialist Overflow Fix

기존 `Item / Relic / Beast`에서 optional Agent가 6개였다.

기존:

`A04 / A05 / A06 / A08 / A11 / A12`

최소 변경:

- 먼저 L2 World Systems에서 `A04/A05/A06` 중 필요한 Agent만 선택한다. 최대 3.
- 다음 L3 Narrative Systems에서 `A08/A11/A12` 중 필요한 Agent만 선택한다. 최대 3.
- 두 그룹을 한 reasoning node의 6개 peer action으로 동시에 노출하지 않는다.

Agent 삭제·역할 변경은 없다.

## 8. Skill Ownership / Lazy Load

| Skill | Direct Owner Node | Local Count Effect |
|---|---|---:|
| `context-pack-compiler` | A21 | +1 |
| `storycraft-orchestrator` | A20 | +1 |
| `sentence-narrator` | A19 | +1 |
| `human-prose-audit` | A19 | +1 |
| `naming-audit` | A15 primary, A19 companion when prose impact exists | +1 at A15 |
| `chrono-weaver` | disabled legacy | 0 |

Active Skills 목록은 레지스트리로 보존하지만 Bootstrap의 peer action menu로 해석하지 않는다.

## 9. A17 GitHub Tool Surface

A17은 실제 GitHub Connector/MCP의 세부 함수 전부를 동시에 peer action으로 노출하지 않는 것을 기본 운영 규칙으로 한다.

A17의 작업 노드는 아래 최대 5개 **coherent verbs** 중 필요한 것만 load한다.

1. `Read State` — repo / branch / PR / file 상태 조회
2. `Compare` — base/head 차이·behind/ahead 확인
3. `Write Branch` — branch 및 의도한 파일 변경
4. `PR Operation` — PR 생성·메타데이터 갱신
5. `Verify Main` — merge 여부·SHA·main 대표파일 재확인

각 verb 내부의 실제 MCP 함수는 구현 세부이며 한 번에 전부 peer menu로 펼치지 않는다.

주의: 이 규칙은 Markdown 운영계약이다. 실제 클라이언트가 모든 MCP tool을 강제로 전역 노출하는 경우 저장소만으로 hard enforcement할 수 없다.

## 10. Local Action Space Audit — After Adoption

| Major Node | Direct Agent | Direct Tool | Direct Skill | Other Callable | Total | Result |
|---|---:|---:|---:|---:|---:|---|
| A00 top router | 0 agent IDs; 5 Lane routes | 0 | 0 | 5 Lane routes | 5 | PASS |
| L1 Authority & Planning | A01, A02 | 0 | 0 | 0 | 2 | PASS |
| L2 World Systems | A03~A07 | 0 | 0 | 0 | 5 | PASS |
| L3 Narrative Systems | A08~A12 | 0 | 0 | 0 | 5 | PASS |
| L4 Evaluation & Release | A13~A17 | 0 | 0 | 0 | 5 | PASS |
| L5 Production | A18~A21 | 0 | 0 | 0 | 4 | PASS |
| A15 naming node | 0 | 0 | 1 | 0 | 1 | PASS |
| A19 prose node | 0 | 0 | 2 | 0 | 2 | PASS |
| A20 craft node | 0 | 0 | 1 | 0 | 1 | PASS |
| A21 CP/Harness node | 0 | 0 | 1 | 1 | 2 | PASS |
| A17 GitHub node | 0 | up to 5 coherent verbs | 0 | 0 | 5 | PASS by documented contract |
| Episode Manuscript pipeline | next required stage only | on demand inside owner | on demand inside owner | fixed Harness transition | <= 3 at each stage | PASS |

## 11. Context / Authority Rule

각 node에는 다음만 전달한다.

- 현재 goal
- 해당 Lane/Agent가 필요한 정본 원문
- 제약·금지선
- acceptance criteria
- 현재 상태와 필요한 artifact

전체 대화·전체 Bible·전체 Agent Registry를 기본으로 한꺼번에 주지 않는다.

독립 평가는 builder rationale보다 `artifact + requirements + acceptance criteria + evidence`를 우선 전달한다.

## 12. Changes Made

- Agent 삭제: **0**
- Agent 추가: **0**
- Skill 삭제: **0**
- Skill 추가: **0**
- Canon/Spec/Manuscript 변경: **0**
- 새 runtime/orchestrator 코드: **0**
- 변경 종류: Bootstrap adoption pointer + 5-Lane routing interpretation + Skill lazy-load + A17 tool-surface contract

## 13. Known Risks

1. `.claude/`와 tool permission allowlist가 없어 실제 Claude Code runtime의 raw tool 노출은 저장소 문서만으로 강제할 수 없다.
2. `minimum-action-agent-os` plugin 설치 여부도 저장소에서 확인할 수 없다. plugin이 없어도 이 Markdown adoption rule 자체는 동작하지만 공통 OS command/agent 호출은 사용할 수 없을 수 있다.
3. main의 `GATE_STATUS.md` / `manuscript/PROGRESS.md`가 실제 원고 진행과 어긋난 문제는 별도 PR #123에서 다루고 있으며 이 OS 적용과 분리한다.
4. Harness 문서의 말미 `현재 집필 상태`도 오래된 상태 복사본이다. 상태 원본은 Gate/Progress를 따라야 하며 별도 상태 정리 작업에서 포인터화하는 것이 안전하다.

## 14. Recommended Next Step

이 적용을 먼저 검토·병합한 뒤, 실제 Claude Code 환경에서 OS plugin 또는 tool exposure를 확인하고 **A17 raw MCP action surface가 5개 이하로 lazy-load되는지 runtime audit**한다.

그 다음 소설 작업은 기존 정본/하네스대로 E089 이후 복구·집필을 계속한다.
