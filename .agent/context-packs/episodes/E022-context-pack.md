# Episode Context Pack — E022

Status: D10 READY  
Episode: E022  
Title: 명단을 받은 살인자  
Compiled By: A21 Context Pack Compiler  
Reference: `agent/1d-subact-context-packs`

> 이 CP는 정본이 아니다. 충돌 시 원본 정본과 권한계층을 따른다. 각 항목의 원본 경로는 절마다 명시한다.

## 1. Authority / Architecture

Required sources:

- [`/AI_PROJECT.md`](../../../AI_PROJECT.md)
- [`docs/00_project/canon-constitution-v1.md`](../../../docs/00_project/canon-constitution-v1.md)
- [`docs/00_project/canon-naming-pack-v1.md`](../../../docs/00_project/canon-naming-pack-v1.md)
- [`docs/00_project/terminology-and-addressing-clarification-v1.md`](../../../docs/00_project/terminology-and-addressing-clarification-v1.md)
- [`docs/00_project/decision-log.md`](../../../docs/00_project/decision-log.md) — DEC-016~021
- [`docs/00_project/GATE_STATUS.md`](../../../docs/00_project/GATE_STATUS.md)
- [`docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md`](../../../docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md) — E022 행
- [`docs/10_story_architecture/detail/v01-scene-ready-design-v1.md`](../../../docs/10_story_architecture/detail/v01-scene-ready-design-v1.md) — Subact 1D, E019–E023
- [`docs/10_story_architecture/subact-causal-matrix-v1.md`](../../../docs/10_story_architecture/subact-causal-matrix-v1.md) — 1D
- [`docs/10_story_architecture/location-world-crosswalk-v1.md`](../../../docs/10_story_architecture/location-world-crosswalk-v1.md) — V01
- [`docs/10_story_architecture/scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) — V1 E022
- [`docs/10_story_architecture/scene-density-and-pacing-overlay-v1.md`](../../../docs/10_story_architecture/scene-density-and-pacing-overlay-v1.md) — §2 Q형, §5 훅 유형
- [`docs/05_characters/cast-canon-index-v2.md`](../../../docs/05_characters/cast-canon-index-v2.md) — C01·C03·C06
- [`docs/05_characters/voice-relationship-state-bible-v1.md`](../../../docs/05_characters/voice-relationship-state-bible-v1.md) — §2·§3·§5·§6
- [`docs/11_mystery/mystery-reinforcement-ladder-v1.md`](../../../docs/11_mystery/mystery-reinforcement-ladder-v1.md) — M02·M05·M15·M16
- [`docs/12_losses/permanent-loss-lock-v1.md`](../../../docs/12_losses/permanent-loss-lock-v1.md) — L001·L003
- [`docs/01_timeline/master-chronology-and-aging-ledger-v1.md`](../../../docs/01_timeline/master-chronology-and-aging-ledger-v1.md) — §1·§2·§4 J01·§5
- [`docs/02_world/atlas-region-dossiers-v1.md`](../../../docs/02_world/atlas-region-dossiers-v1.md) — R05 서부 잿빛 변경

Episode function — 출처: 레지스트리 E022 행, v01 설계 E022, subact-causal-matrix 1D

- Grand Act: GA I — 잘못된 치료
- Volume: V1 — 회색 종이 울리는 날
- Subact: 1D — 표적 제거와 귀환
- Beat: 대항 세력
- Goal: 왕실군·본부 시한·현지 주민의 압박이 동시에 걸린 상태에서 표적과의 마지막 합의를 시도
- Opposition: 세 압력의 요구가 서로를 상쇄한다 — 주민을 살리면 추격시간이 없고, 시한을 지키면 대피가 끊기고, 표적을 살리면 귀환과 F0 생존이 무너진다
- Choice: 주민 탈출로를 열고 표적과 단둘이 남는다
- Cost: 표적 추격·설득에 쓸 시간이 더 줄고, 합의 실패의 책임을 대리인 없이 혼자 진다
- State Change: 임무가 ‘죽여야 하는가’에서 ‘합의가 불가능하다면 누가 먼저 손을 대는가’로 좁혀진다
- Hook: 표적이 자신의 죽음 뒤 소거될 마을·가족·환자 명단을 건넨다 (레지스트리)
- Closing image: 회색 종이 한 번 울리고 귀환창이 마지막 단계로 진입한다 (v01 설계)
- Next Cause: E023에서 선택 가능한 시간이 몇 분으로 줄고 좁은 기록실 전투가 시작된다

## 2. E019–E021 Carryover

> E004–E021 구간에는 Episode CP가 없다. 아래 인계상태는 [`v01-scene-ready-design-v1.md`](../../../docs/10_story_architecture/detail/v01-scene-ready-design-v1.md) Subact 1D 절과 레지스트리 E019–E021 행에서만 도출했다.

### 에이든 로엔

- 미래 멸망과 자신의 임무를 표적에게 일부 공개한 상태 (E019)
- 표적의 생체인장이 서부 봉쇄의 강제키라는 주장을 들었고, 현지 장치 구조상 사실임을 확인받았다 (E019)
- 장부 검증에 필요한 시간과 귀환 가능 시간이 정확히 겹친다는 계산을 이미 했다 (E020)
- 세 목표를 모두 달성할 수 없음을 스스로 인정한 상태다 (E020)
- E021에서 장부 확보를 우선해 일부 대피를 돕지 않았고, 그 선택이 아직 청산되지 않았다

### 표적 — 세렌 바일 (C06)

- 순수 희생자가 아니라 위험한 권한을 선의로 독점한 개혁가다 (E019 Moral Shape)
- 주민 주소가 보호되지 않으면 봉쇄권과 장부를 넘기지 않겠다고 이미 거절했다 (E020)
- 조직의 위조신분은 삭제 예정 주민의 새 주소이고 무기는 호송 방어용임이 확인됐다 (E021)
- 부하들의 도주 준비는 대피 준비였다 (E020 Hook → E021 정정)

### 아이리스 네르 (C03)

- 에이든이 환자보다 장부와 표적만 택하면 귀환 연결을 끊겠다고 선언한 상태다 (E021)
- 세계 구원 논리에도 현지인을 희생시키는 데 동의하지 않는다 (E021 Independent Agency)
- E022에서 새 최후통첩을 반복하지 않는다. 선언은 이미 나왔고 E022는 그 선언의 이행 여부를 시험한다

### 외부 압력

- 왕실군 포위가 완성됐고 단계적 진입이 시작됐다 (E019·E020)
- 왕실군이 은신처 외곽 환자 수레에 불을 놓았다 (E021 직전 Hook)
- 첫 환자 수레가 왕실군에게 발견됐다 (E021 Hook)
- 본부는 ‘표적 생존 시 F0 잔여일 11일’이라는 수치를 보냈고 강제 귀환 준비를 경고했다 (E019·E020)

### 확정된 이동·검증 비용 (E020 Logistics)

- 귀환표식까지 이동 40분
- 포위 돌파 최소 25분
- 장부 검증 최소 1시간

E022는 이 세 수치를 다시 계산하지 않는다. 이미 확정된 값이며, E022에서는 그중 하나를 실제로 지불하는 장면만 남는다.

## 3. Time / Location

출처: [`master-chronology-and-aging-ledger-v1.md`](../../../docs/01_timeline/master-chronology-and-aging-ledger-v1.md) §1·§2·§4, [`location-world-crosswalk-v1.md`](../../../docs/10_story_architecture/location-world-crosswalk-v1.md) V01, [`atlas-region-dossiers-v1.md`](../../../docs/02_world/atlas-region-dossiers-v1.md) R05

- Era: N — CY 640
- J01 도착일: CY 640 안개월 4일 / 도착 오차 약 18km / 신분 실패
- E022 시점: 현지 체류 후반. 정확한 일자는 정본에 없다 (§ gaps 참조)
- 에이든: 41세 / 주관적 누적일은 V1 총 24일 안에서 진행 중
- 아이리스: CY 640 기준 29세
- 세렌 바일: CY 640 기준 42세
- 권역: 서부 잿빛 변경 — 마을·도로·사람이 기록에서 반복 누락되는 희생지
- Main locations:
  1. 은신처 외곽 탈출로
  2. 은신처 마지막 방
- 이동은 은신처 내부와 그 외곽으로 제한된다. 장거리 이동은 발생하지 않는다
- 크로스워크 V01은 첫 개혁가의 저항과 죽음을 `반쪽성·절검의 언덕` 권역에 배치한다. 은신처의 정식 지명은 설계에 없다

## 4. 삼면 압박 구조

출처: 레지스트리 E022 Goal, v01 설계 E019–E022, [`atlas-region-dossiers-v1.md`](../../../docs/02_world/atlas-region-dossiers-v1.md) R05

세 압력은 같은 방향으로 밀지 않는다. 각각 다른 것을 요구하고 서로를 상쇄한다.

### 왕실군

- 목적은 표적 제거가 아니라 봉쇄 해제와 서부 기록망 장악이다 (E019)
- 이미 환자 수레에 불을 놓았고 첫 수레를 발견했다
- 단순 악역이 아니라 자기 명령체계 안에서 합법적으로 움직인다. 얼굴 없는 추격 기계로 쓰지 않는다

### 본부 시한

- ‘표적 생존 시 F0 잔여일 11일’ 수치와 강제 귀환 경고
- 숫자는 현재의 실제 압박이며 선전 구호가 아니다
- 그러나 이 수치가 객관적 미래확정이라고 확정하지 않는다 — 정보상한 유지

### 현지 주민

- 대피 중인 환자·가족은 배경 군중이 아니라 이름과 순번을 가진 사람들이다 (R05: 벽흔·가족노래·묘표·공동식사 순번으로 존재를 증명)
- 아이리스의 요구는 감정 호소가 아니라 귀환 연결이라는 실물 지렛대를 쥔 정치 행위다

### 상쇄 관계

| 무엇을 지키면 | 무엇을 잃는가 |
|---|---|
| 주민 탈출로 | 표적 추격·설득 시간 |
| 본부 시한 | 대피 연결과 아이리스의 귀환 협조 |
| 표적의 생존 | 귀환창과 F0 잔여일 |

E022는 이 표에서 첫 행을 실제로 선택하고 대가를 지불하는 회차다.

## 5. Character State

출처: [`cast-canon-index-v2.md`](../../../docs/05_characters/cast-canon-index-v2.md), [`voice-relationship-state-bible-v1.md`](../../../docs/05_characters/voice-relationship-state-bible-v1.md) §2·§3·§5·§6

### 에이든 로엔 (C01)

- 목표: 봉쇄권 이전 합의를 마지막으로 시도한다
- 말투: 임무 중에는 목표·출구·비용 순서로 말한다
- 죄책감 표식: 상대의 이름을 피하고 `표적`이라는 역할명으로 부른다. E019에서 직접 대면했음에도 역할명이 유지되는 것 자체가 상태 표시다
- 오류 가능성: 미래 기관의 약속을 자신이 보증할 수 있다고 믿는다
- 금지: 표적을 이미 무죄로 확신한 채 행동, 본부 전체를 적으로 선언, 왕실군과 정면 교전으로 문제 해결

### 세렌 바일 (C06)

- 목표: 자기 죽음 이후의 주민 주소를 보장받는다
- 미래 기관의 검증 불가능한 약속을 거부한다 (E022 설계)
- 명단은 협박이 아니라 인계다. 죽음을 받아들이는 대신 책임을 넘기는 행위로 기능한다
- 금지: 성인화된 순교자 대사, 죽기 전 진실 폭로, 자기 무죄 증명 시도, 재앙을 늦춘 전체 기능의 자기 설명
- 영구사망 잠금 대상 (L001). E022에서는 아직 죽지 않는다

### 아이리스 네르 (C03)

- 말투: 사람·장소·오늘 필요한 물자를 구체적으로 언급한다
- 분노 방식: 미래의 숫자와 중앙의 수동태를 공격한다
- 정치협상: 상대의 원칙보다 누가 언제 무엇을 잃는지 묻는다
- E022 기능: 탈출로 개방의 실무 상대이지 감정적 양심 대변자가 아니다
- 금지: 로맨스 축 배치, 에이든의 결정을 대신함, E021 최후통첩의 반복 낭독

### 왕실군 지휘 인물

- 새 핵심 이름을 즉석 확정하지 않는다
- 봉쇄 해제라는 실제 목적과 자기 병사의 손실을 함께 안다
- 잔혹함의 전시가 아니라 명령 집행의 얼굴이다

## 6. Mystery / Information Ceiling

출처: [`mystery-reinforcement-ladder-v1.md`](../../../docs/11_mystery/mystery-reinforcement-ladder-v1.md), [`canon-constitution-v1.md`](../../../docs/00_project/canon-constitution-v1.md) IMMUTABLE 7·10

Active mysteries:

- M02 세렌 바일은 왜 창시자로 기록됐는가 — 다음 사다리 단은 E033이다. E022는 새 단을 추가하지 않는다
- M05 빈 세금장부에 무엇이 있었는가 — 명단은 이 사다리의 물질 전조이지 정답이 아니다
- M15 최초 연대기는 어디 있는가 — E016 세렌의 암호 이후 잠복 상태
- M16 회색 종은 무엇을 감지하는가 — 종결부의 단타 울림이 환기 기능만 수행

Reader may know:

- 표적의 생체인장이 서부 봉쇄의 강제키라는 사실은 현지 장치 구조상 성립한다
- 표적은 위험한 권한을 자발적으로 내려놓지 않았다
- 소거될 마을·가족·환자 명단이 실물로 존재한다
- 미래 기관의 보증은 현지에서 검증할 방법이 없다

Reader must not know yet:

- 세렌이 지방 소거를 늦췄다는 전체 기능
- 보고서 날짜층을 누가 왜 위조했는가
- 삭제된 증언자의 정체
- 19만 생존증가 모델의 최종 오류구조
- 명단에 적힌 사람들이 F1에서 어떻게 되는가

Hook 취급 규칙:

- 명단을 세렌 무죄의 확정 증거로 읽히게 하지 않는다. 명단은 그가 무엇을 알고 있었는지를 보여줄 뿐 누가 소거를 명령했는지는 말하지 않는다
- 명단을 그 자리에서 전부 낭독해 감정을 유도하지 않는다
- 새 시간법칙·새 유산·새 권한을 명단에 붙여 설명하지 않는다 (IMMUTABLE 10)

## 7. POV / Storycraft

출처: [`scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) V1 E022, [`scene-density-and-pacing-overlay-v1.md`](../../../docs/10_story_architecture/scene-density-and-pacing-overlay-v1.md) §2·§5

- POV: 에이든 단일 근접 3인칭. 보조 POV 없음
- Scene Density: **Q형 · 2장면**
- 배정 사유(원문): 마지막 방에서 소거 명단을 건네받고 봉쇄권 이전 합의에 실패하는 협상결렬 회차다
- Q형 운용 규칙: 한 장면을 길게 유지해 감정·논리·공간 압박을 깊게 하고, 이동·설명 장면을 따로 분리하지 않는다
- Primary craft: 양립 불가능한 두 책임체계의 협상결렬
- Secondary A: 대가 선지불 — 얻기 전에 잃는 순서
- Secondary B: 문서가 무기로 전환되는 역전
- Hook: H6 윤리적 질문 (명단) + H1 물리적 위험 (귀환창 최종 단계)
- Reader reward: 두 사람 중 누구도 거짓말하지 않는데 합의가 불가능하다는 사실의 구체적 확인

## 8. Scene Values

**설계 장면 수 2 — §7 밀도값과 일치한다.**

### Scene 1 — 은신처 외곽 탈출로

- Entry: 세 압력을 부분적으로라도 동시에 감당할 수 있다
- Action: 에이든이 최소한의 길을 열어 환자 수레가 빠져나가게 한다. 아이리스는 이 개방을 실무로 받아 넘긴다
- Opposition: 왕실군의 단계적 진입과 이미 발각된 첫 수레
- Cost: 표적 추격·설득에 쓸 시간이 더 줄어든다
- Exit: 주민 쪽 책임은 일부 이행되지만 임무 쪽 여유는 사라진다. 이제 남은 것은 표적 한 사람과의 시간뿐이다

### Scene 2 — 은신처 마지막 방

- Entry: 봉쇄권을 넘겨받으면 두 사람 다 사는 길이 있다
- Beat 1: 에이든이 봉쇄권 이전을 요구한다. 미래 기관의 보증을 담보로 건다
- Beat 2: 세렌은 검증 불가능한 약속을 거부한다. 미래의 어떤 기관도 여기서 확인할 수 없다는 것이 거부 사유다
- Beat 3: 세렌이 자신의 죽음 뒤 소거될 마을·가족·환자 명단을 건넨다
- Emotional Turn: 서로가 거짓말한다고 보는 대신 서로의 책임 대상이 다르다는 것을 이해한다
- Irreversible Setup: 에이든이 무기를 뽑고 세렌은 저항을 선택한다
- Exit: 회색 종이 한 번 울리고 귀환창이 마지막 단계로 진입한다. 합의는 완전히 닫혔고 남은 것은 실행뿐이다

## 9. Anti-Repeat

직전 회차들과 실제로 달라야 하는 지점:

- E019의 표적 자기설명 대화를 반복하지 않는다. E022의 표적은 설명하지 않고 물건을 넘긴다
- E020의 시간 산술 장면을 재연하지 않는다. 40분·25분·1시간은 이미 확정됐고 E022는 계산이 아니라 지불이다
- E021의 오해 → 정정 구조를 반복하지 않는다. E022에는 뒤집히는 오해가 없다. 두 사람 다 사실을 정확히 알고 있다
- E021의 아이리스 최후통첩을 다시 선언하게 하지 않는다
- E003의 두 문서 대조를 반복하지 않는다. 명단은 대조 대상이 아니라 인계 물품이다
- E001의 삭제된 글자가 되살아나는 훅을 반복하지 않는다
- E002의 기관 순회·검사대 구조를 반복하지 않는다
- 왕실군과의 정면 전투로 장면을 해결하지 않는다. V1 Arc 01 Anti-Repeat 조항이 전투 승리로 진행하지 않을 것을 요구한다
- 명단을 전부 소리 내어 읽는 낭독 연출을 하지 않는다
- 표적이 죽음을 예고하는 유언조 대사를 쓰지 않는다

## 10. Active State / Props

- 소거될 마을·가족·환자 명단 — E022에서 에이든에게 인계. E024 등록 대상 후보이며 그때 누락·오염이 확정된다
- 세렌의 생체인장 — 서부 봉쇄의 강제키. E022에서는 살아 있는 상태로만 존재
- 세렌의 절검 — R03. E022에서는 저항 선택의 물리적 표현으로만 등장하며 아직 에이든의 소유가 아니다
- 장부 — E020 검증 최소 1시간이라는 값이 붙어 있고 E022에서는 검증되지 않는다
- 귀환표식 — 아이리스가 연결을 쥐고 있다
- 회색 종 — 종결부 단타. 도시 전체 동시 울림은 E023 자산이므로 여기서 선소비하지 않는다
- 환자 수레 — 첫 수레는 이미 발각됐다

E024 등록 용량 제한이 걸리므로, E022에서 인계된 명단의 물리 형태와 분량을 A10이 기록한다.

## 11. State Mutation Plan

E022 종료 시 기록:

- 탈출로 개방 범위와 실제로 빠져나간 수레 수
- 아이리스의 귀환 연결 상태 — 유지·조건부·단절 중 무엇인가
- 봉쇄권 이전 협상의 최종 결렬 확정
- 명단의 인계 사실, 물리 형태, 확인된 항목 수
- 에이든이 표적을 부르는 호칭 상태 — 역할명 유지 여부
- 귀환창 잔여 단계
- 본부 시한과 F0 잔여일 수치의 갱신 여부
- 왕실군 진입 단계

## 12. Ready Verdict

- Authority: RESOLVED
- Domain Readiness: READY
- Scene density conformance: PASS — Q형 2장면, 설계 2장면
- POV: READY
- Storycraft companion: REQUIRED — [`E022-storycraft-manifest.md`](../../../docs/10_story_architecture/craft-manifests/E022-storycraft-manifest.md)
- Information ceiling: PASS
- S0: 0
- S1: 2 — §gaps 참조

Pre-Writing Gate는 [`GATE_STATUS.md`](../../../docs/00_project/GATE_STATUS.md)를 따른다. E021 상태기록 확인 뒤 A18 호출 가능.

## gaps

정본에서 도출할 수 없어 이 CP가 확정하지 않은 항목이다. 임의 창작하지 않았다.

1. **E022의 현지 정확 일자.** 연대장부는 J01 도착을 CY 640 안개월 4일로, V1 주관적 경과를 24일로만 규정한다. E007–E024의 일자 배분표가 없다.
2. **은신처의 정식 지명.** v01 설계는 `은신처`로만 쓴다. 크로스워크 V01은 첫 개혁가의 저항과 죽음을 `반쪽성·절검의 언덕`에 배치하고 아틀라스 R05는 절검의 언덕을 “첫 개혁가의 저항과 죽음이 연결된 장소”로 규정하지만, 은신처와 절검의 언덕이 같은 장소라고 명시한 정본은 없다.
3. **귀환창의 단위 충돌.** E002 CP는 예상 체류를 5시간 17분으로 기록하지만 v01 설계의 E018은 귀환창이 하루 줄어든다고 하고 V1 주관적 경과는 24일이다. 두 수치의 관계를 규정한 정본을 찾지 못해 E022는 `마지막 단계`라는 설계 표현만 사용했다.
4. **세렌 바일의 말투 항목 부재.** `voice-relationship-state-bible-v1.md` §2·§2-A에 C06 항목이 없다. 이 CP의 세렌 대사 규칙은 v01 설계의 행동기술과 cast index C06에서만 도출했다.
5. **Hook 이중 기재.** 레지스트리 E022 Hook은 `명단 전달`, v01 설계 E022 Hook은 `회색 종 한 번 + 귀환창 최종 단계`다. 둘 중 하나를 폐기할 근거가 없어 Hook과 Closing image로 병기했다.
