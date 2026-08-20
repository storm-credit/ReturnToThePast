# Manuscript-Independent Context Audit — 2026-08-21

Status: **EXECUTED / LEGACY MANUSCRIPT DEMOTED TO PROVENANCE**
Base: `main@9fdf2faa3278201bae624421ce6600ee871a95f5`
Scope: 설계·라우팅 레이어의 기존 원고 의존성 전수 검사와 강등
Non-Scope: **원고 수정 0** · 사건·설정·인물·결말 변경 0 · 원고 파일 삭제 0

## 0. 시험 질문

> **기존 `manuscript/` 전체를 삭제했다고 가정해도 이 시스템이 살아 있는가?**

이 문서는 그 질문에 답하고, `아니오`인 지점을 **PROVENANCE ONLY**로 강등한다.

## 1. 방향 결정 — 작가 지시 (2026-08-21)

기존 `manuscript/volume-01` ~ `volume-04` (E001–E088, 88파일)는 이번 감사부터 다음으로 취급한다.

```text
LEGACY / REFERENCE / PROVENANCE ONLY
```

목표는 E001–E088을 살리는 것이 아니다. 목표는

> **Canon + World + Act + Volume + Subact + D6 + Mystery + Character + Craft + Context Pack만으로 E001부터 완전히 새 원고를 쓸 수 있는 시스템**

이다. 따라서 다음이 금지된다: E007 원고 수리 · E008–E088 복구 · E089 작성 · **기존 원고의 Exit를 설계 정답으로 사용** · HUMAN PROSE PASS · 새 사건/설정/주요인물/결말 추가.

## 2. 원고 의존성 전수 등록부

### D-01 · GATE_STATUS 게이트 전체가 원고 파일 상태로 정의됨 — **BLOCKING → 강등**

`docs/00_project/GATE_STATUS.md`

| 문구 | 문제 |
|---|---|
| `Physical Main Manuscript Coverage: E001–E088 files present` | 원고 파일 존재를 게이트 지표로 사용 |
| `Sequential Current-Clean Boundary: E006` | 과거 원고의 순차 인증 상태 |
| `Blocking Manuscript Boundary: E007` | **과거 원고가 에이든 시점으로 쓰였다**는 사실이 시스템 차단 사유 |
| `E089는 현재 Next Valid Prose가 아니다` / `E089 DIRECT ROUTING: FORBIDDEN` | 과거 원고 연속성 보호 목적 |
| §6 `E007 blocker를 건너뛰고 E089부터 집필` 금지 | 같은 목적 |

**판정**: 새 원고 기준에서 **전부 무효**다. E007 설계는 완전하다 — cold-start harness §4에서 POV(C03 아이리스 네르 P1) · 정보상한 · 장소 · 훅 · 다음 인과가 모두 resolve됐다. RED-ARCH는 **설계 결손이 아니라 과거 원고와의 불일치**였다.

**조치**: GATE_STATUS를 NEW-MANUSCRIPT 기준으로 개정. 원고 관련 지표는 `LEGACY PROVENANCE` 절로 격리.

### D-02 · Previous Exit Source가 과거 원고를 authoritative로 지목 — **BLOCKING → 강등**

`docs/10_story_architecture/episode-context-state-pipeline-v1.md` §3:

```text
1. 직전 회차의 current State Mutation
2. current grouped State Mutation의 해당 episode row/exit
3. actual manuscript exit + next CP carryover      ← 과거 원고
4. State Ledger / active checkpoint
```

`docs/00_project/D16_6_CONTEXT_STATE_PIPELINE_20260820.md` §2 권한계층 8번 = `actual accepted manuscript`, §9 = `E089의 직전 상태 = actual E088 manuscript`.

**판정**: 새 원고 런타임에서 3번은 **읽으면 안 되는 소스**다. E089를 쓸 시점에 존재하는 E088은 **새 원고의 E088**이지 legacy E088이 아니다.

**조치**: §4 신규 Previous Exit 규칙으로 대체.

### D-03 · Historical Backfill / GREEN 판정이 원고 존재를 조건으로 함 — **NON-BLOCKING → 강등**

D16.6 §6–§7: `actual manuscript exists` = GREEN 조건 1번. `Manuscript coverage 88/88`, `Context Pack coverage 88/88`, `verified broken handoff 0`.
`episode-context-state-pipeline-v1.md` §11: 기존 88화 GREEN 유지 조건.

**판정**: 새 시스템에서 이 GREEN/YELLOW/RED 판정은 **적용 대상이 없다**. 삭제하지 않고 `HISTORICAL RECORD` 로 표기한다.

### D-04 · Subact Hub의 원고 링크와 CP 파생 동선 — **NON-BLOCKING**

V01-1A~1D Hub는 `회차별 실제 동선`을 각 회차 CP §3·§4에서 가져오고, 회차 분해표에 `[원고](../../../manuscript/volume-01/E0xx-*.md)` 링크를 단다.

| Hub | manuscript 링크 수 |
|---|---:|
| V01-1A | 6 |
| V01-1B | 6 |
| V01-1C | 6 |
| V01-1D | 2 |
| 그 외 53개 | 각 0–1 (대부분 `원고 없음` 서술문) |

**판정**: 링크 대상은 원고지만, **동선·소품·인물 상태는 CP(설계 문서)에서 왔지 원고 문장에서 온 것이 아니다.** 원고를 지워도 Hub의 값은 그대로 남는다. 링크는 provenance로 유지한다.

**조치**: 새 원고 작성 시 이 링크를 **열지 않는다** (`minimum-context-resolver-v1` §3.3 DO NOT LOAD).

### D-05 · 44개 Hub의 사실과 다른 stale 문구 — **ACCURACY DEFECT / NON-BLOCKING**

| 문구 | 등장 Hub 수 | 실제 |
|---|---:|---|
| `.agent/context-packs/episodes/ 는 E001–E025까지만 존재` | **44** | 실제로는 E001–E026 개별 + E027–E093 묶음 = **38파일** |
| `manuscript/ 에는 volume-01 뿐` | **33** | 실제로는 volume-01~04 = **88파일** |
| `Context Pack 없음` | **22** | 위와 같은 원인 |

`D16_5_GRAPH_WIRING_ERRATA_20260820.md`는 이 중 **V04-4C 하나만** 정정했다 → 43/44 미정정.

**판정**: 새 원고 시스템에서 이 문구가 만든 결과는 **오히려 옳다** — 해당 구간의 장면 단위 동선을 `[설계 미정]`(=JIT 확정)으로 남겼기 때문이다. 그러나 문구 자체는 사실이 아니다.

**조치**: 44개 Hub를 수정하지 않는다(대량 편집 대비 이득 없음). 대신 §5 Errata 확장으로 **전역 supersede**를 선언한다.

### D-06 · Deep Master의 `Previous Exit input` 표기 — **CLEAN**

`.agent/context-packs/deep/V01-1A-deep-context-master.md` §3:

```text
E001 | SERIES ENTRY
E002 | E001 actual Exit/JIT
```

**판정**: `actual Exit`는 **직전 회차의 실제 결과**를 뜻하며 legacy 원고를 특정하지 않는다. 새 원고에서도 그대로 성립한다. **강등 불필요.**

### D-07 · 권한계층의 `→ Manuscript →` 항 — **표기 정정 필요 / NON-BLOCKING**

`CLAUDE.md` · `AGENTS.md` · `deep-context-pack-production-standard-v1` §7 · scorecard RTG01 등이 권한계층에 `Manuscript`를 둔다.

**판정**: 이 `Manuscript`는 앞으로 **새 원고**를 가리킨다. Legacy 88화는 그 자리에 들어가지 않는다. `deep-context-pack-production-standard-v1` §7은 이미 `Manuscript provenance`로 정확히 적고 있다.

**조치**: 정의를 §3에 고정한다. 각 라우터 파일을 개별 수정하지 않는다.

### D-08 · E007 RED-ARCH — **소멸**

`e001-e010-current-context-overlay-d16-7.md` §5: `The historical E007 Aiden-POV manuscript cannot be certified current-clean under this lock.`

**판정**: `historical ... manuscript`가 대상이다. 새 원고 E007은 처음부터 C03 P1으로 쓰인다. **차단 사유 없음.** 문서는 historical record로 유지하되, 그 안의 **POV 잠금 표(§5)는 여전히 활성 설계 정본**이다 — 강등 대상은 판정문이지 잠금이 아니다.

## 3. 새 런타임 구조

```text
STATIC DESIGN STATE                     ← 60 Subact Hub · D6 · 30 Character Hub · Ladder · Ledger
        +
NEW MANUSCRIPT RUNTIME STATE            ← 새 원고가 만든 State Mutation만
        ↓
NEXT EPISODE JIT
```

### 3.1 절대 규칙

- **legacy runtime state는 자동 상속되지 않는다.** `manuscript/state/E0xx-state-mutation.md` 26개와 `manuscript/quality/*-state-mutation.md`는 **PROVENANCE**다. 새 원고의 Entry State로 사용하면 FAIL.
- 권한계층의 `Manuscript`는 **새 원고만** 가리킨다.
- Legacy 원고·CP·State는 삭제하지 않는다. **열지 않을 뿐이다.**

### 3.2 Previous Exit 규칙 (D-02 대체)

| 회차 | Previous Exit |
|---|---|
| **E001** | **SERIES ORIGIN STATE** — §3.3 |
| E002–E375 | **직전 회차의 새 원고 State Mutation**. 그것만이 유일한 소스다 |

직전 새 원고가 없으면 그 회차를 쓰지 않는다. **건너뛰기 금지.** 과거 원고나 과거 State Mutation으로 대체하지 않는다.

### 3.3 SERIES ORIGIN STATE — E001의 시작 상태

E001은 이전 회차가 없는 유일한 회차이며, 시작 상태를 **정적 설계에서 전부** 가져온다.

| 항목 | 값 | 출처 |
|---|---|---|
| 세계 상태 | F0는 회색 재앙과 기반시설 붕괴로 생존 한계 | V01-1A Hub `Entry State` |
| 시각 | 건국력 664년 장야월 18일 또는 그 직후 | V01-1A Hub 무대 |
| 주인공 | C01 에이든 로엔 · **41세 · 주관적 누적일 0** · F0 요원, 본부 신뢰 | V01-1A Hub 인물표 |
| 관계 | C02 리아 = F0 기록관, 감사표식 상태 / 원본층 접근 제한. C03 아이리스 = **미등장** | 같은 표 |
| 자산 | R01 회색 종 = **S 공동소유**, 소리 없이 떨기만 함. R02 빈 세금장부 = 미등장. R03 절검 = 미등장 | V01-1A Hub 활성 아이템 |
| 손실 | **0** — L001 영구사망은 E023 | V01-1A Hub |
| 미스터리 | M01·M02·M04·M05·M12·M15·M16 활성, 어느 것도 추론 개방 전 | V01-1A Hub 활성 미스터리 |
| 기관 | 7기관 활성, 단독 승인 불가 | V01-1A Hub 활성 기관 |
| 시간선 | F0 단일. F1 이후 정보 **전부 미존재** | Hub 금지 E001 |

**이 표 외의 시작 상태 값은 E001 집필 중 JIT로 정하고 E001 State Mutation에 기록한다.**

### 3.4 State Mutation 계약 (JIT 모호성 해소)

각 회차 종료 시 **실제로 바뀐 것만** 아래 13범주로 기록한다. 변하지 않은 설정은 복사하지 않는다.

```text
EPISODE
SOURCE_MANUSCRIPT          # 새 원고 파일 경로
STATUS                     # FIRST DRAFT | AUTHOR REVIEW READY  (HUMAN PROSE PASS는 작가만)
TIMELINE_STATE             # Era / 날짜 / 주관적 누적일
CHARACTER_MUTATIONS        # 상태·지식·부상. C-ID 필수
RELATIONSHIP_MUTATIONS     # 신뢰·부채·권한·비밀·호칭 중 바뀐 축
INSTITUTION_FACTION_MUTATIONS
ASSET_MUTATIONS            # R-ID · ownership/contract/custody/damage
LOCATION_MUTATIONS
MYSTERY_INFORMATION_MUTATIONS   # M-ID · 이 화에서 실제로 열린 rung
PERMANENT_LOSS_OR_IRREVERSIBLE_CHOICE   # L-ID
CLOCK_MOVEMENT
UNCHANGED_CRITICAL_LOCKS   # 필요할 때만, 짧게
NEXT_ENTRY_HANDOFF         # 다음 회차 Entry State가 되는 문장
JIT_RESOLVED_VALUES        # 이 회차에서 GAP-NB로 확정한 값 (지명·이름·수량·시각)
```

`JIT_RESOLVED_VALUES`는 신설 항목이다. GAP-NB로 즉석 확정한 값이 다음 회차에서 다시 흔들리는 것을 막는다.

### 3.5 Handoff 불변식

```text
Entry(N+1) = Exit(N) + 명시적으로 허용된 offscreen 전이 + 잠긴 시간·장소 이동
```

FAIL 조건: 설명 없는 관계 복구 · 소유권 순간 복귀 · 손상/사망/영구손실 리셋 · 이전 화에 없던 정보가 POV 지식으로 자동 진입 · 법적 상태가 이유 없이 뒤집힘 · 그래프 링크만으로 등장 허가.

## 4. 강등 결과

| ID | 항목 | 이전 | 이후 |
|---|---|---|---|
| D-01 | GATE_STATUS 원고 게이트 | BLOCKING | **LEGACY PROVENANCE** (§5 개정) |
| D-02 | Previous Exit = actual manuscript | AUTHORITATIVE | **PROVENANCE ONLY** (§3.2 대체) |
| D-03 | E001–E088 GREEN backfill | ACTIVE | **HISTORICAL RECORD** |
| D-04 | Hub 원고 링크 | 참조 | **PROVENANCE / DO NOT LOAD** |
| D-05 | 44 Hub stale 문구 | 미정정 43건 | **전역 supersede** (§5) |
| D-06 | Deep Master Previous Exit 표기 | — | **CLEAN, 변경 없음** |
| D-07 | 권한계층 `Manuscript` 항 | 모호 | **= 새 원고** 로 정의 고정 |
| D-08 | E007 RED-ARCH | BLOCKING | **소멸.** POV 잠금표는 활성 유지 |

**새 원고 시작을 막는 원고 의존성: 0**

## 5. Global Stale-Source Errata (D-05 확장)

D16.5 Errata가 V04-4C에 대해 선언한 것을 **60개 Hub 전체로 확장**한다.

> 모든 Subact Hub에서 `.agent/context-packs/episodes/ 는 E001–E025까지만 존재` · `manuscript/ 에는 volume-01 뿐` · `Context Pack 없음` 취지의 문구는 **작성 시점의 상태 기술이며 현재 정본 라우팅이 아니다.**
>
> - 실제 CP 파일: E001–E026 개별 + E027–E093 묶음 = 38파일
> - 실제 원고 파일: E001–E088 = 88파일
> - 다만 **새 원고 생산에서는 둘 다 PROVENANCE이며 필수 입력이 아니다.**
> - 그 문구를 근거로 붙은 `[설계 미정]` 표기는 **유효하다** — 해당 값은 실제로 정본에 없으며 JIT 확정 대상이다.

Hub 44개를 개별 수정하지 않는다. 이 절이 supersede한다.

## 6. 검증

| 검사 | 결과 |
|---|---|
| Cold-start 11화 중 원고를 읽어야 resolve되는 항목 | **0** (`context-map-cold-start-harness-20260821.md`) |
| Static Context가 원고 문장을 소스로 요구하는 지점 | **0** — Hub의 동선은 CP(설계)에서 옴 |
| Historical CP를 authoritative로 요구하는 활성 규칙 | **0** (D-02 대체 후) |
| Legacy runtime state 자동 상속 경로 | **0** (§3.1) |
| manuscript prose 변경 | **0** |
| 원고 파일 삭제 | **0** |
| 새 사건·설정·인물·결말 추가 | **0** |

## 7. 연결

- [`../10_story_architecture/minimum-context-resolver-v1.md`](../10_story_architecture/minimum-context-resolver-v1.md) — §3.3 DO NOT LOAD
- [`context-map-cold-start-harness-20260821.md`](context-map-cold-start-harness-20260821.md)
- [`../10_story_architecture/episode-context-state-pipeline-v1.md`](../10_story_architecture/episode-context-state-pipeline-v1.md) — §3·§11이 이 문서로 supersede됨
- [`../00_project/D16_6_CONTEXT_STATE_PIPELINE_20260820.md`](../00_project/D16_6_CONTEXT_STATE_PIPELINE_20260820.md) — §2·§6·§7·§9가 이 문서로 supersede됨
- [`../00_project/GATE_STATUS.md`](../00_project/GATE_STATUS.md)
