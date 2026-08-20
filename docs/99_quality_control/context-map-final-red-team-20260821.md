# Context Map Final Red Team — 2026-08-21

Status: **EXECUTED / 10 VECTORS / 4 CONFIRMED-AND-FIXED · 2 CONFIRMED-RESIDUAL · 4 REFUTED**
Base: `main@9fdf2faa3278201bae624421ce6600ee871a95f5`
Method: 적대적 검사. `문서가 존재한다`를 근거로 PASS를 주지 않는다. 실제 파일을 세고 열어 확인한다.
Non-Scope: 원고 수정, 사건·설정 변경

## A. Context completeness illusion — **CONFIRMED · FIXED**

> 375/375 파일이 있다는 이유만으로 writeability를 PASS 처리했는가.

**했다.** `.agent/context-packs/deep/` 60개 Master의 실측 분포:

| 구간 | 파일 수 | 명시 소스 경로 수 |
|---|---:|---:|
| 2,500바이트 이상 (FULL) | **5** | 3–14 |
| 1,000–2,500 (MID) | **7** | 0–3 |
| **1,000바이트 미만 (STUB)** | **48** | **0** |

V02-2C부터 V15-15D까지 **48개(E038–E375 담당)에 `docs/...md` 형태의 소스 경로가 한 건도 없다.** 소스를 `활성 원장`, `GA III D6` 같은 문장으로만 적는다. 전형적인 예 (V08-8B 전문, 700바이트):

> `Deep sources: V08-8B Hub / V08 scene-ready / GA III D6 / active ledgers.`

`deep-context-pack-production-standard-v1` §3은 `source pointer만 있고 소스가 없거나, 어느 값을 읽어야 할지 모호하면 COMPLETE가 아니다`라고 규정한다. 48개는 이 기준을 만족하지 않는다. `SOURCE-BOUND COMPLETE` 표기는 과대다.

**그러나 시스템은 살아 있다.** 실제 Context 본체는 Deep Master가 아니라 **Subact Hub 60개**에 있고, 이쪽은 12,526–41,265바이트로 후반 권일수록 더 깊다 (V13–V15 평균 33KB). Deep Master는 얇은 라우터일 뿐이다.

**조치**: 48개를 재작성하지 않는다. `minimum-context-resolver-v1.md` §1이 `활성 원장` 같은 문장을 **결정적 경로 공식**으로 확정한다 (60/60 · 15/15 · 5/5 실측 검증).

**잔여 표기 문제**: 48개 Master의 `status: STATIC DEEP CONTEXT / SOURCE-BOUND COMPLETE`는 §1 공식이 적용될 때만 참이다. 이 Red Team 문서가 그 조건을 명시한다.

## B. Hidden manuscript dependency — **CONFIRMED · FIXED**

> 기존 원고가 없으면 시작상태를 못 잡는 회차가 있는가.

**8건 발견.** 전수 등록부는 [`manuscript-independent-context-audit-20260821.md`](manuscript-independent-context-audit-20260821.md) §2.

가장 심각한 것:

- **D-01** `GATE_STATUS.md` 전체가 원고 파일 상태로 게이트를 정의. `Blocking Manuscript Boundary: E007`의 실제 사유는 **설계 결손이 아니라 과거 원고가 에이든 시점으로 쓰였다는 사실**이다.
- **D-02** `episode-context-state-pipeline-v1` §3이 `actual manuscript exit`를 Previous Exit 소스 3순위로 지목.

**검증**: Cold-start 11화 전부에서 원고를 읽어야만 resolve되는 항목 **0건**. E007조차 POV(C03 P1)·정보상한·장소·훅·다음 인과가 전부 설계에서 나온다.

**조치**: §3 신규 런타임 구조 + SERIES ORIGIN STATE 정의. 원고는 PROVENANCE ONLY로 강등.

## C. Future leak — **CONFIRMED · RESIDUAL (구조적으로 방어됨)**

> 후반 진실·결말·관계상태가 앞 회차 Context에 새어 들어가는가.

**샌다. 다만 항상 금지문과 함께 샌다.**

실례:

| 위치 | 누출 내용 | 동반 방어 |
|---|---|---|
| V04-4C Hub (E088–E093) | M12 결론 `한 명이 아니라 독점된 선택권` | `추론 가능 시점은 E298` + 금지표 |
| V04-4C Hub | M13 `추론 가능 시점은 E173` | `E089는 얼굴 인식 오류 단서 하나뿐` |
| V01-1A Hub (E001–E006) | M02·M04·M16 추론 개방 회차 번호 | `1A에서는 어느 것도 열리지 않는다` |
| V10-10A Hub | GA IV Revelation 전문 | `10A에서 말로 설명하지 않는다` |

즉 **누출은 설계 의도**다 — 집필자가 `지금 무엇을 열면 안 되는지` 알려면 답을 알아야 한다. 문제는 **모델이 금지문보다 답을 더 강하게 학습할 위험**이다.

**잔여 위험 등급**: 중. 완전 제거 불가.

**조치**:
1. `minimum-context-resolver-v1` §3.3에 `독자 추론 가능 시점이 이 회차보다 뒤인 미스터리의 회수 내용` DO NOT LOAD 명시.
2. `craft-context-resolver-v1` §12 Craft Manifest에 **`이 회차에서 말하지 않는 것`을 필수 출력 필드**로 지정. 답을 아는 상태에서 무엇을 참았는지 명시적으로 쓰게 한다.
3. Hub `공정성 규칙` 절은 **항상 금지문과 붙여서** 인용한다. 답 문장만 떼어 CP에 넣지 않는다.

## D. Craft abstraction — **CONFIRMED · FIXED**

> `Craft Route`가 이름만 있고 실제 문장 생산에 도움이 안 되는가.

**그랬다. 최악 수준이었다.**

| 검사 | 결과 |
|---|---|
| 60개 Deep Master에서 craft/prose/storycraft/문체/scene-density 문서를 가리키는 소스 포인터 | **0건** |
| `craft` 단어가 등장하는 Master | **1개** (V01-1A, 22-field 계약 16번의 라벨) |
| E094–E375의 회차별 Craft Manifest | **0개** (manifest는 E001–E093까지만) |

22-field 계약 16번이 `scene density / craft route / anti-repeat`를 요구하는데, **어느 문서 어느 절을 여는지 지정한 곳이 없었다.** `storycraft 문서를 참조` 수준이었다.

**반전**: 실제 작법 자산은 풍부하다 — `storycraft-orchestrator`(14 진단 범주 + 9 조합), `sentence-narrator`(§5.3 호흡 정량 기준 · §9 6인 목소리 · §10 정보상한), `human-prose-audit`(AI 티 6패턴), `prose-style-references` §4(7 장면유형 매핑), `scene-density-and-pacing-overlay`(4 밀도유형 + 7 훅유형 + 장면 전환 규칙), `scene-density-map`(**375/375 회차별 밀도 + 배정 사유 문장**). **연결만 없었다.**

**조치**: [`craft-context-resolver-v1.md`](../10_story_architecture/craft-context-resolver-v1.md) 신설. 입력 신호 4개(밀도/기능/POV/층위) → 진단 → 조합 → 표본 → Anti-Repeat 3층. 요구된 24개 영역 전부에 `어느 문서 어느 절`을 §9 결정표로 확정. **새 문체 규칙은 만들지 않았다.**

## E. Context overload — **CONFIRMED · FIXED**

> 한 화를 쓰기 위해 수십 문서를 읽어야 하는가.

**읽어야 했다.** E260 기준 naive full-bundle = **21개 문서 / 359,834바이트**. 그중 `scene-density-map-v1.md` 72,720바이트에서 해당 회차 유효 정보는 **247바이트**(0.34%)다.

**조치**: `minimum-context-resolver-v1.md` ALWAYS 12 / CONDITIONAL 트리거 / DO NOT LOAD 3분류 + 행 단위 조각 로딩.

| | 문서 수 | 바이트 |
|---|---:|---:|
| naive | 21 | 359,834 |
| resolver | **12** | **113,201** |
| 절감 | −9 | **−68.5%** |

**Subact Hub(12–41KB)는 조각내지 않는다.** 그것이 압축된 Context 본체다. 목표는 `문서 5개 이하`가 아니라 **필요 최소한의 coherent bundle**이다.

## F. Character voice collapse — **REFUTED**

> C01–C30의 역할은 다르지만 실제 대사 생산 규칙은 비슷하지 않은가.

**아니다.** 실측:

| 자산 | 커버리지 |
|---|---:|
| `docs/05_characters/hubs/C##-*.md` | **30/30**, 11,043–23,545바이트 |
| 각 Hub의 `§3 목소리` · `§4 이 인물이 모르는 것` · `§2 호칭` · `§8 금지` | 30/30 |
| `supporting-cast-dossiers-c21-c30-v2.md` | 64,316바이트, 인물별 `말투`·`욕망/필요/거짓믿음`·`주인공 부재 중 행동`·`금지` |
| `voice-relationship-state-bible-v1.md` | 핵심 6인 말투 + 6개 관계 매트릭스 + 권역별 감정곡선 + 정보상한 |
| `functional-cast-speech-spec-v1.md` | 이름 없는 기능인물 — **회피 유형 8종 + 결함 축 + 배정 규칙** |

C22 하렌 세른 예: `리아(C02)와 같은 기록관 층이지만, 리아가 자기 확실성 등급을 낮추는 데 쓰는 도구를 하렌은 **상대의 자격을 깎는 데** 쓴다` — 같은 직업층 안에서도 축이 분리돼 있다.

**잔여 위험**: `sentence-narrator` §9만 로드하면 **6인만** 커버된다. → `craft-context-resolver-v1` §6 표가 POV·주요 대사 인물마다 해당 C-Hub를 로드하도록 강제한다. 추가로 `한 장면에 이름 있는 인물이 2인 이상이면 각자 §3에서 서로 다른 축을 하나씩 고르고, 완성도를 균일하게 만들지 않는다`(human-prose-audit §3.4)를 규칙화했다.

## G. Act tone flattening — **REFUTED (아키텍처) · FIXED (작법 결속)**

> GA I~V가 Context level에서는 다른데 실제 Craft layer에서는 똑같이 쓰이게 되어 있지 않은가.

아키텍처는 갈라져 있다. `grand-acts-v1.md` 5/5 전부에 **Anti-Repeat 조항**이 있고 서로 다른 행동 문법을 지정한다.

| GA | Anti-Repeat |
|---|---|
| I | 첫 귀환 반전은 E025에만. 이후 권 결말을 귀환 반전으로 끝내지 않음 |
| II | 암살 대신 법·도시·귀환 인프라·내전 |
| III | 탐사·건설·협상·재난. **보스 제거 구조 금지** |
| IV | 전투보다 동시 임무 조율·자기 인과·권한 해체 |
| V | 적 처치·유물 완성보다 헌법·동의·희생의 실행 |

`parallel-plot-and-pov-governance-v1` §6도 GA별 병렬성 강도를 낮음→중간 / 중간→높음 / 높음 / 최고 / 높음→분산으로 나눈다.

**문제는 이 조항이 작법 레이어에 연결되지 않았다는 것**이었다 (D와 같은 원인).

**조치**: `craft-context-resolver-v1` §11 Anti-Repeat 3층 — GA 조항 / 병렬성 강도 / 직전 3화 대조. 세 층 모두 통과해야 원고를 시작한다.

## H. Subact sameness — **CONFIRMED · GUARD 추가**

> 60 Subact가 Goal/Cost만 다르고 장면 경험은 반복되지 않는가.

**비트 라벨은 완전히 동일하다.** D6 Registry 375행 전수:

| Subact Beat | 등장 |
|---|---:|
| 진입 | 60 |
| 첫 장벽 | 60 |
| 잘못된 해석 | 60 |
| 대항 세력 | 60 |
| 선택 | 60 |
| 국소 해결 | 60 |
| 후폭풍 | 15 |

**60개 Subact 전부가 같은 6비트 템플릿을 쓴다.** 이는 `DEC-021`이 이미 해결한 `Scene 1/2/3` 문제와 동일한 구조다 — 설계 편의를 위한 기능 라벨을 그대로 집필 리듬으로 읽으면 375화가 같은 호흡이 된다.

**반대 증거 (변주 장치는 존재한다)**:

| 장치 | 상태 |
|---|---|
| 밀도 Q/S/E/X 375/375 배정 | 권당 분포 15/15 통과, S형 14화 초과 0권 |
| 같은 밀도 **4회 이상** 연속 | **0건** (규칙 준수) |
| 훅 유형 H1–H7 · 동일 훅 3화 연속 금지 | 규칙 존재 |
| GA별 Anti-Repeat | 5/5 |
| POV 변주 (P1/P2/P3) | 배정표 존재 |

**추가 발견 — 검증표 오류**: `scene-density-map-v1.md` §0 검증 결과가 `같은 밀도 4회 이상 연속 0건 — **최장 연속은 2회**`라고 적는다. 실측하면 **최장 연속은 3회**이며 3연속 구간이 5곳 있다: **E105–E107(S) · E117–E119(E) · E191–E193(S) · E306–E308(E) · E361–E363(S)**.
구속 규칙(`4회 이상 금지`)은 지켜졌으므로 **BLOCKING이 아니다.** 그러나 검증표의 근거 문장이 사실과 다르다 → §5 Errata.

**조치**:
1. **6비트 라벨은 기능 라벨이지 장면 리듬이 아니다** — `DEC-021`과 같은 취급. `craft-context-resolver-v1` §5가 실제 장면 분할을 밀도지도 배정 사유에서 가져오게 한다.
2. §11 3층 Anti-Repeat의 층 3이 `장면 시작 방식`을 대조 항목에 포함한다 — 같은 `진입` 비트라도 앞 3화와 다른 방식으로 열어야 한다.
3. 위 5개 3연속 구간은 **훅 유형과 POV를 반드시 다르게** 배치한다 (회차 Preflight 항목).

## I. Mystery overspecification — **CONFIRMED · RESIDUAL**

> Context가 정답을 너무 많이 알려 모델이 독자보다 먼저 설명해버릴 위험이 없는가.

**있다.** C와 같은 뿌리다. Subact Hub는 각 M##의 심기·중간단·**추론 가능 시점**·**회수 회차**·**최종 답의 내용**을 함께 적는다.

동시에 **방어 장치도 이미 촘촘하다**:

- 60개 Hub 전부에 `공정성 규칙` 절
- `추론 가능 시점`과 `인물의 정답 인지`를 명시적으로 분리 (`등장인물의 정답 인지와 독자의 추론 시점은 분리할 수 있다`)
- `50화 넘게 방치 후 인물 대사로 정답 설명 금지`
- `리아/오르바드 한 명의 증언으로 진실 확정 금지`
- `최종 회수 직전 새 핵심단서 추가 금지`
- `공정 단서 = 문서·물질·행동·제도결과·생태반응 중 최소 3종`
- 두 rung을 한 장면에서 함께 회수 금지 (V04-4C M16/M13)

**잔여 위험 등급**: 중. 이것은 문서로 완전히 없앨 수 없고 **원고 감사에서 잡는 항목**이다.

**조치**: Craft Manifest 필수 필드 `FALSE INTERPRETATION / 이 회차에서 말하지 않는 것`. 원고 감사에서 `설명형 대사`(sentence-narrator §8) + `의미 재해설`(human-prose-audit §3.3)로 이중 검사.

## J. JIT ambiguity — **CONFIRMED · FIXED**

> 새 원고 작성 후 무엇을 State Mutation으로 남겨야 하는지가 불명확하지 않은가.

**두 겹의 불명확이 있었다.**

**J-1 · 무엇이 집필을 멈추는가**
`deep-context-pack-production-standard-v1` §4가 `GAP-NB`(보류 가능) / `GAP-B`(집필 STOP)를 정의한다. 그러나 실측:

| 검사 | 결과 |
|---|---:|
| Subact Hub의 `[설계 미정]` | **921건** |
| Subact Hub의 `⚠` 경고 | **314건** (209건이 `[설계 미정]` 동반) |
| 저장소 전체의 `GAP-B` 마커 | **0건** |
| 저장소 전체의 `GAP-NB` 마커 | **0건** |

**분류 규칙은 있는데 적용된 곳이 한 군데도 없다.** 집필자는 921개 중 어느 것이 STOP인지 알 수 없다.

**조치**: `minimum-context-resolver-v1` §6 Gap Triage — GAP-NB/GAP-B 판별 기준과 관측된 ⚠ 유형별 귀속. 판정 규칙:
> ⚠ 하나를 GAP-NB로 내리려면 그 값을 임의로 정해도 이 회차의 **선택·인과·정보상한·영구손실이 바뀌지 않아야 한다.** 하나라도 바뀌면 GAP-B다.

Cold-start 11화 적용 결과 GAP-B 2건(E173 · E199) 검출.

**J-2 · 즉석 확정값이 다음 회차에서 흔들림**
기존 State Mutation 스키마 13범주에 **GAP-NB로 즉석 확정한 값을 기록할 자리가 없었다.** E173에서 지명을 정하면 E174가 그것을 어디서 읽는가.

**조치**: `manuscript-independent-context-audit-20260821` §3.4에 `JIT_RESOLVED_VALUES` 필드 신설.

## 종합

| 벡터 | 판정 | 조치 |
|---|---|---|
| A Context completeness illusion | CONFIRMED | 경로 공식으로 48 STUB 구제 |
| B Hidden manuscript dependency | CONFIRMED | 8건 강등, 원고 의존 0 |
| C Future leak | CONFIRMED · RESIDUAL | DO NOT LOAD + Manifest 필드 |
| D Craft abstraction | CONFIRMED | craft resolver 신설, 24영역 결정표 |
| E Context overload | CONFIRMED | −68.5% |
| F Character voice collapse | **REFUTED** | 로딩 규칙만 보강 |
| G Act tone flattening | **REFUTED** (아키텍처) | 작법 결속 추가 |
| H Subact sameness | CONFIRMED | 6비트 = 기능 라벨 규칙화 + 3연속 구간 가드 + 검증표 Errata |
| I Mystery overspecification | CONFIRMED · RESIDUAL | Manifest 필드 + 원고 감사 이중 검사 |
| J JIT ambiguity | CONFIRMED | Gap Triage + `JIT_RESOLVED_VALUES` |

**S0: 0 · 새 원고 시작을 막는 blocking issue: 0 · 회차 단위 GAP-B: 2 (E173 · E199)**

## 5. Errata

| # | 대상 | 정정 |
|---:|---|---|
| E-1 | `scene-density-map-v1.md` §0 검증표 | `최장 연속은 2회` → **실측 최장 연속 3회** (E105–E107 · E117–E119 · E191–E193 · E306–E308 · E361–E363). 구속 규칙 `4회 이상 연속 금지`는 여전히 **0건 위반**이다 |
| E-2 | 48개 STUB Deep Master의 `SOURCE-BOUND COMPLETE` | `minimum-context-resolver-v1` §1 경로 공식이 적용될 때에 한해 참이다 |
| E-3 | 44개 Subact Hub의 CP/원고 범위 문구 | [`manuscript-independent-context-audit-20260821.md`](manuscript-independent-context-audit-20260821.md) §5가 전역 supersede |

Errata는 라우팅·검증 기술만 정정한다. **사건·설정·인물·결말 변경 0.**
