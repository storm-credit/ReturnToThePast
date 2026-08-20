# Minimum Context Resolver v1

Status: **ACTIVE PRODUCTION ROUTER — CONTEXT ECONOMY LAYER**
Date: 2026-08-21
Scope: E001–E375
Authority: routing only. Canon Constitution → Amendment/Errata → Decision Log → State Ledger → Domain Bible → Story Architecture 가 상위다.
Non-Scope: 사건·설정·인물·결말 생성, Canon 변경, 원고 작성

## 0. 왜 필요한가

Context Map은 완성됐지만, 한 회차를 쓰려고 관련 문서를 전부 열면 **약 360KB**를 읽게 된다. 측정값(E260 기준, naive full-bundle 21개 문서):

| 항목 | 값 |
|---|---|
| naive 번들 문서 수 | 21 |
| naive 번들 바이트 | **359,834** |
| 최대 단일 문서 | `scene-density-map-v1.md` 72,720 (해당 회차 유효 정보는 **247바이트**) |

이 상태로는 집필 입력만으로 컨텍스트가 소진된다. **Context Map 100%여도 호출량이 과하면 생산 시스템으로는 실패다.**

이 문서는 회차별로 무엇을 **통째로 읽고 / 조각만 읽고 / 아예 읽지 않는지**를 확정한다.

## 1. 결정적 경로 공식 — 파일을 찾기 위해 인덱스를 읽지 않는다

Episode ID `E###` 하나로 아래가 계산된다. 검색·탐색 불필요.

```text
n        = int(E###)
GA       = ceil(n / 75)                     # 1..5
V        = ceil(n / 25)                     # 1..15
SUBACT   = 60-Subact 소속표 §2에서 조회      # V##-#A|B|C|D
```

경로 규칙 (60/60 · 15/15 · 5/5 실측 확인됨):

| 소스 | 경로 공식 |
|---|---|
| Subact Hub | `docs/10_story_architecture/subacts/{SUBACT}.md` |
| Volume Scene-Ready | `docs/10_story_architecture/detail/v{V:02d}-scene-ready-design-v1.md` |
| D6 Registry | `docs/10_story_architecture/detail/ga{GA:02d}-episode-registry-e{start:03d}-e{end:03d}.md` |
| Deep Context Master | `.agent/context-packs/deep/{SUBACT}-deep-context-master.md` |
| Character Hub | `docs/05_characters/hubs/C##-{이름}.md` |

D6 Registry 범위: GA1=E001–E075 / GA2=E076–E150 / GA3=E151–E225 / GA4=E226–E300 / GA5=E301–E375.

> **주**: `.agent/context-packs/deep/` 의 60개 Master 중 48개는 소스 경로를 문장으로만 적는다(`활성 원장`, `GA III D6` 등). 이 §1 공식이 그 문장을 **결정적 경로로 확정**한다. 48개 Master를 재작성하지 않는다.

## 2. Subact 소속표 — Episode → Subact

| Subact | Episodes | Subact | Episodes | Subact | Episodes |
|---|---|---|---|---|---|
| V01-1A | E001–E006 | V06-6A | E126–E131 | V11-11A | E251–E256 |
| V01-1B | E007–E012 | V06-6B | E132–E137 | V11-11B | E257–E262 |
| V01-1C | E013–E018 | V06-6C | E138–E143 | V11-11C | E263–E268 |
| V01-1D | E019–E025 | V06-6D | E144–E150 | V11-11D | E269–E275 |
| V02-2A | E026–E031 | V07-7A | E151–E156 | V12-12A | E276–E281 |
| V02-2B | E032–E037 | V07-7B | E157–E162 | V12-12B | E282–E287 |
| V02-2C | E038–E043 | V07-7C | E163–E168 | V12-12C | E288–E293 |
| V02-2D | E044–E050 | V07-7D | E169–E175 | V12-12D | E294–E300 |
| V03-3A | E051–E056 | V08-8A | E176–E181 | V13-13A | E301–E306 |
| V03-3B | E057–E062 | V08-8B | E182–E187 | V13-13B | E307–E312 |
| V03-3C | E063–E068 | V08-8C | E188–E193 | V13-13C | E313–E318 |
| V03-3D | E069–E075 | V08-8D | E194–E200 | V13-13D | E319–E325 |
| V04-4A | E076–E081 | V09-9A | E201–E206 | V14-14A | E326–E331 |
| V04-4B | E082–E087 | V09-9B | E207–E212 | V14-14B | E332–E337 |
| V04-4C | E088–E093 | V09-9C | E213–E218 | V14-14C | E338–E343 |
| V04-4D | E094–E100 | V09-9D | E219–E225 | V14-14D | E344–E350 |
| V05-5A | E101–E106 | V10-10A | E226–E231 | V15-15A | E351–E356 |
| V05-5B | E107–E112 | V10-10B | E232–E237 | V15-15B | E357–E362 |
| V05-5C | E113–E118 | V10-10C | E238–E243 | V15-15C | E363–E368 |
| V05-5D | E119–E125 | V10-10D | E244–E250 | V15-15D | E369–E375 |

Coverage: E001–E375 연속 · ownership gap **0** · duplicate **0** (실측).

경계 주의: **E069 = 3D**(3C 아님) · **E088 = 4C**(4B 아님). 과거 묶음 지원팩 `E063-E069` / `E082-E088`은 provenance이며 소속은 이 표가 정본이다.

## 3. 3분류 — ALWAYS / CONDITIONAL / DO NOT LOAD

### 3.1 ALWAYS LOAD (12 bundle, 회차 불문)

| # | 소스 | 로딩 형태 | 이 회차에서 무엇을 결정하는가 |
|---:|---|---|---|
| 1 | `docs/00_project/canon-constitution-v1.md` | 전문 | 권한계층·IMMUTABLE |
| 2 | Subact Hub (§1 공식) | **전문** | 이 회차 Context의 본체 — 인과·무대·인물·금지·기관·자산·미스터리·회차분해 |
| 3 | D6 Registry | **해당 행 + 소속 Volume 헤더 + Exit-State Lock** | Goal / Choice & State Change / Hook |
| 4 | `scene-density-map-v1.md` | **해당 행만** | 실제 장면 수 + 배정 사유 |
| 5 | `scene-density-and-pacing-overlay-v1.md` | 전문 | 밀도 유형 규칙 · 훅 유형 H1–H7 · 장면 전환 규칙 |
| 6 | `grand-acts-v1.md` | **해당 GA 블록만** | Promise/Revelation/Loss/**Anti-Repeat** |
| 7 | POV 인물 Hub (§1 공식) | 전문 | 목소리 · **이 인물이 모르는 것** · 호칭 · 금지 |
| 8 | `.agent/skills/storycraft-orchestrator/SKILL.md` | 전문 | 진단 범주 → 중심/보조 작법 |
| 9 | `.agent/skills/sentence-narrator/SKILL.md` | **§2, §5–§12, §15–§16** | 문체·호흡·묘사·대사·호칭·정보상한 |
| 10 | `.agent/skills/human-prose-audit/SKILL.md` | 전문 | AI 티 차단 |
| 11 | `docs/13_writing_harness/anti-padding-policy-v1.md` | 전문 | 분량 채우기 금지 |
| 12 | `secondary-pov-and-offscreen-action-allocation-v1.md` + `d15-pov-allocation-supplement-v1.md` | **해당 Volume 절만** | 이 회차에 보조 POV 배정이 **있는지 없는지** 자체 |

`prose-style-references-v1.md`는 §4 장면유형 매핑 표만 인용해 Craft Resolver가 주입한다(§9 참조).

> **12번이 ALWAYS인 이유**: Subact Hub 60개 중 **10개는 POV를 한 번도 언급하지 않는다** — V01-1A · V01-1B · V02-2A · V02-2B · V02-2D · V03-3A · V03-3B · V10-10B · V11-11D · V15-15C (약 60화 분량). 이 구간은 배정 유무를 Hub만 봐서는 알 수 없다. 배정표를 열기 전에는 `배정 없음`을 결론으로 삼지 않는다.
>
> 실증: **E007 = C03 아이리스 네르 P1**은 V01-1B Hub 어디에도 없고 배정표 §4 V1 행과 `e001-e010-current-context-overlay-d16-7.md` §5에만 있다. 이것을 놓치면 E007을 에이든 시점으로 쓰게 된다.

### 3.2 CONDITIONAL LOAD — 트리거가 있을 때만

| 조건 | 추가 로딩 | 형태 |
|---|---|---|
| Subact Hub 인물표에 C01 외 이름이 있음 | 그 인물의 Character Hub | 전문 |
| Hub 인물표에 이름 없는 기능인물이 장면을 짐 | `functional-cast-speech-spec-v1.md` | 전문 |
| Hub `활성 기관` 표에 항목 존재 | `institution-org-procedure-bible-v1.md` | **해당 기관 절만** |
| Hub `활성 아이템` 표에 R##/유산 존재 | `asset-state-checkpoints-v1.md` | **해당 R## 행 + 현재 권 열** |
| 신수·수호수 등장 | 해당 beast bible | 해당 항목만 |
| Hub `활성 미스터리` 표에 M## 존재 | `mystery-reinforcement-ladder-v1.md` + `mystery-semantic-crosswalk-e001-e375-v2.md` | **해당 M## 행만** |
| Hub `이 구간이 끝날 때` 또는 `발생하지 않는 것`에 L### 존재 | `permanent-loss-lock-v1.md` | **해당 L### 행만** |
| 배정표에 이 회차 P1/P2/P3가 있음 | `parallel-plot-and-pov-governance-v1.md` | §1·§3 (운용 규칙) |
| E001–E010 구간 | `e001-e010-current-context-overlay-d16-7.md` | 해당 행 + §5 |
| 시대·나이·달력 값이 장면에 필요 | `master-chronology-and-aging-ledger-v1.md` | 해당 Era 절만 |
| 실제 그림 발주가 필요 | `visual-cp-resolver-rules-v1.md` + `visual-asset-act-usage-matrix-v1.md` | 해당 Act 열만 |
| 새 고유명 생성이 발생 | `korean-webnovel-fantasy-naming-rules-v1.md` + `naming-source-verification-gate-v1.md` | 전문 |
| 장소 이동·지리가 장면 인과 | `location-world-crosswalk-v1.md` | 해당 Volume 행만 |
| 세력 간 이해 충돌이 중심 | `faction-causal-track-v1.md` | 해당 Volume 절만 |

**Visual은 기본 CONDITIONAL이다.** 서사 자산이 먼저 정해진 뒤에만 호출한다 (`episode-context-state-pipeline-v1.md` §9).

### 3.3 DO NOT LOAD — 읽으면 오염이다

- 다른 Volume의 Subact Hub
- 이 회차 Hub의 `활성 미스터리` 표에 없는 M##
- **독자 추론 가능 시점이 이 회차보다 뒤인 미스터리의 회수 내용**
- 미래 Episode의 D6 행 (다음 회차 1행 = Next Cause 확인용만 예외)
- 미래 Volume의 Scene-Ready / Exit State Ledger
- **`manuscript/` 이하 전부** — LEGACY / PROVENANCE ONLY (`manuscript-independent-context-audit-20260821.md`)
- `Drafts/`, `lore_bible/`, `outline/`, `Guidelines/` — LEGACY
- `.agent/context-packs/episodes/` 의 과거 CP — provenance. 새 원고의 필수 입력이 아니다
- `docs/00_project/` 의 D9–D16 Amendment 전문 — 해당 Subact Hub가 이미 결론을 인용한다. Hub가 `[설계 미정]`을 남긴 항목에 대해서만 원문 확인
- `CLAUDE.md` / `AGENTS.md` / `AI_PROJECT.md` — 라우터이며 정본 아님. 이미 이 문서가 라우팅을 대신한다

## 4. 측정 — 실측 절감

E260(V11-11B, X형 5~6장면) 기준.

| 방식 | 문서 수 | 바이트 | 비고 |
|---|---:|---:|---|
| naive full-bundle | 21 | 359,834 | 관련 문서를 전부 전문 로드 |
| **이 Resolver (§3.1 + 필요 CONDITIONAL)** | **12** | **113,201** | 조각 로딩 적용 |
| 절감 | −9 | **−68.5%** | |

가장 큰 절감원:

| 소스 | 전문 | 조각 | 절감 |
|---|---:|---:|---:|
| `scene-density-map-v1.md` | 72,720 | 247 | −99.7% |
| D6 Registry | 18,523 | 647 | −96.5% |
| `visual-asset-act-usage-matrix-v1.md` | 22,130 | 0 (CONDITIONAL) | −100% |
| `permanent-loss-lock-v1.md` | 36,126 | 해당 L### 행 | −95% 이상 |
| `asset-state-checkpoints-v1.md` | 25,309 | 해당 R## 행 | −95% 이상 |

**목표는 숫자 5 이하가 아니다.** 목표는 **필요 최소한의 coherent bundle**이며, Subact Hub(12–41KB)는 조각내지 않는다 — 그것이 이 시스템의 압축된 Context 본체이기 때문이다.

## 5. 조각 로딩 방법

인덱스 문서에서 행만 뽑는다. 예:

```bash
grep -E "^\| E260 \|" docs/10_story_architecture/scene-density-map-v1.md
grep -E "^\| E260 \|" docs/10_story_architecture/detail/ga04-episode-registry-e226-e300.md
sed -n '/## Grand Act IV/,/## Grand Act V/p' docs/10_story_architecture/grand-acts-v1.md
```

행을 뽑을 때 **해당 표의 헤더 행과 그 절의 규칙 문단을 함께** 가져온다. 값만 떼어 오면 단위·권한·예외를 잃는다.

## 6. Gap Triage — 어떤 `[설계 미정]`이 집필을 멈추는가

Subact Hub에는 `[설계 미정]` **921건**, `⚠` 경고 **314건**(그중 209건이 `[설계 미정]` 동반)이 있다. 이는 결함이 아니라 **빈칸을 숨기지 않은 결과**다. 그러나 지금까지 어느 문서도 이것을 `GAP-B`/`GAP-NB`로 분류하지 않았다 (저장소 전체 `GAP-B` 마커 **0건**).

집필자는 회차 Preflight에서 **그 회차에 걸린 ⚠만** 아래 규칙으로 분류한다.

### GAP-NB — 계속 쓴다. JIT에서 확정하고 State Mutation에 기록한다

- 지명·건물명·방 이름·거리·분 단위 시각
- 표기 불일치(`서부절점` vs `국경 고정요새` 등) — **Hub가 지정한 우선 표기를 쓰고 나머지는 별칭 처리**
- 원본 간 해상도 차이(crosswalk 1칸 vs 설계 3장소) — **설계 카드의 장소 수를 따른다**
- 단역·기능인물의 이름
- 소품 수량·색·재질
- 일자·계절이 인과에 걸리지 않는 경우

관측된 ⚠ 유형 중 `해상도 차이`(11) · `지명/고유명 없음`(13) · `표기 차이`(1) · `일자·계절 미정`(3) 등이 여기 속한다.

### GAP-B — 이 회차 집필을 멈추고 작가 판정을 받는다

- **POV 주체**가 두 원본에서 다름
- **미스터리 단(rung)이 어느 장면에 얹히는지 정본에 없음** — 공개/비공개 경계가 정해지지 않음
- **훅이 두 원본에서 한 칸씩 어긋남** (관측 2건)
- **장면의 감정 축을 지는 인물에게 ID·이름이 없음** (관측 2건: `인물 공백이 이 구간의 최대 결손이다`)
- 법적 권한·정족수 성립 여부가 정본에서 판정되지 않음 (관측 1건)
- 영구손실·사망·소유권의 시점이 원본끼리 충돌
- `원본 간 불일치`(관측 10건) 중 위 항목에 해당하는 것

### 판정 규칙

> ⚠ 하나를 GAP-NB로 내리려면 **그 값을 임의로 정해도 이 회차의 선택·인과·정보상한·영구손실이 바뀌지 않아야 한다.** 하나라도 바뀌면 GAP-B다.

GAP-B는 **회차 단위로 멈춘다.** 시리즈 전체를 멈추지 않는다. E173의 GAP-B는 E001–E172 집필을 막지 않는다.

## 7. 회차 Preflight 체크 (7항목)

집필 직전 아래를 통과해야 원고를 시작한다.

1. §1 공식으로 Subact / Volume / GA / D6 행이 **유일하게** 확정됐다
2. §3.1 ALWAYS 12개를 지정된 형태로 로드했다
3. §3.2 트리거를 Hub 표로 판정해 CONDITIONAL을 확정했다 (트리거 없는 문서는 열지 않았다)
4. §3.3 DO NOT LOAD를 하나도 열지 않았다
5. 이 회차에 걸린 ⚠ 를 §6으로 분류했고 **GAP-B = 0** 이다
6. Craft Route가 `craft-context-resolver-v1.md`로 확정됐다
7. Previous Exit이 확정됐다 — E001은 **SERIES ORIGIN STATE**, 그 외는 **직전 회차의 새 원고 State Mutation**

하나라도 실패하면 원고를 시작하지 않는다.

## 8. 갱신 조건

- Subact 소속 경계가 바뀌면 §2를 먼저 고친다
- 새 Volume Scene-Ready / Registry 파일명이 §1 공식을 벗어나면 **파일명을 공식에 맞춘다** (공식을 예외로 늘리지 않는다)
- ALWAYS 목록에 문서를 추가할 때는 **무엇을 CONDITIONAL로 내리는지 함께 적는다**

## 9. 연결

- Craft 선택: [`craft-context-resolver-v1.md`](craft-context-resolver-v1.md)
- 원고 독립성: [`../99_quality_control/manuscript-independent-context-audit-20260821.md`](../99_quality_control/manuscript-independent-context-audit-20260821.md)
- 22-field 계약: [`deep-context-pack-production-standard-v1.md`](deep-context-pack-production-standard-v1.md)
- 생산 루프: [`episode-context-state-pipeline-v1.md`](episode-context-state-pipeline-v1.md)
