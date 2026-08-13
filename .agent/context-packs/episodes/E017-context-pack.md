# Episode Context Pack — E017

Status: D10 READY  
Episode: E017  
Title: 죽이기 전 한 번의 대화  
Compiled By: A21 Context Pack Compiler  
Reference: `agent/1c-evidence-subact`

> 이 CP는 정본이 아니다. 충돌 시 원본 정본과 권한계층을 따른다.

## 1. Authority / Architecture

Required sources:

- [`/AI_PROJECT.md`](../../../AI_PROJECT.md)
- [`docs/00_project/canon-constitution-v1.md`](../../../docs/00_project/canon-constitution-v1.md)
- [`docs/00_project/canon-naming-pack-v1.md`](../../../docs/00_project/canon-naming-pack-v1.md)
- [`docs/00_project/terminology-and-addressing-clarification-v1.md`](../../../docs/00_project/terminology-and-addressing-clarification-v1.md)
- [`docs/00_project/decision-log.md`](../../../docs/00_project/decision-log.md) — DEC-016·017·018·020·021
- [`docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md`](../../../docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md) — E017 행
- [`docs/10_story_architecture/detail/v01-scene-ready-design-v1.md`](../../../docs/10_story_architecture/detail/v01-scene-ready-design-v1.md) — Subact 1C, E017 절
- [`docs/10_story_architecture/subact-causal-matrix-v1.md`](../../../docs/10_story_architecture/subact-causal-matrix-v1.md) — 1C 행
- [`docs/10_story_architecture/scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) — V1 E017 배정
- [`docs/10_story_architecture/location-world-crosswalk-v1.md`](../../../docs/10_story_architecture/location-world-crosswalk-v1.md) — V01 1C
- [`docs/05_characters/cast-canon-index-v2.md`](../../../docs/05_characters/cast-canon-index-v2.md) — C01·C03·C06
- [`docs/05_characters/voice-relationship-state-bible-v1.md`](../../../docs/05_characters/voice-relationship-state-bible-v1.md) — §2 에이든, §5 정보상한, §6 갈등 대화 규칙
- [`docs/03_systems/time-travel-ontology-v1.md`](../../../docs/03_systems/time-travel-ontology-v1.md) — What Travels, Departure, Absolute Limits
- [`docs/11_mystery/mystery-reinforcement-ladder-v1.md`](../../../docs/11_mystery/mystery-reinforcement-ladder-v1.md) — M02·M15
- [`docs/12_losses/permanent-loss-lock-v1.md`](../../../docs/12_losses/permanent-loss-lock-v1.md) — L001, RF-02
- [`.agent/context-packs/episodes/E016-context-pack.md`](E016-context-pack.md)

Episode function:

- Grand Act: GA I — 잘못된 치료
- Volume: V1 — 회색 종이 울리는 날
- Subact: 1C — 증거가 맞고 진실이 틀릴 때
- Beat: 선택
- Goal: 명령 수행에 충분한 공식 증거와 반대 증언이 동시에 놓인 상태에서 결정한다
- Opposition: 표적이 변명 대신 명령의 출처를 되묻는다
- Choice: 표적 제거 준비를 유지하되 한 번의 대화를 선택한다
- Cost: 대화하는 동안 귀환창과 왕실 포위 여유가 동시에 줄어든다
- State Change: 임무의 쟁점이 ‘세렌이 유죄인가’에서 ‘내 명령은 어디서 왔는가’로 이동한다
- Hook: 표적이 미래에서 온 명령의 원문을 요구한다

## 2. E016 Carryover

### 에이든

- 왕실 추적대·지방연맹 어느 편에도 정체를 밝히지 않음
- 그 대가로 어느 세력의 보증도 없이 단독 접근만 남음
- 세렌이 출발 인장을 알아봤다는 사실을 안다
- 제거 명령은 아직 유효하며 시한은 E012에서 앞당겨진 상태

### 세렌 바일

- 미래 본부의 존재를 인지
- 조직의 기록이 세 방향으로 쪼개진 뒤 남은 몫을 지키는 중
- 동의 없는 기억채취 사실 (E015)이 그의 결함으로 확정돼 있음

### 아이리스 네르

- E012 조건 유지 — 환자를 표적 접근 수단으로 쓰면 귀환표식을 끊는다
- E017 본편에는 개입하지 않으나 그 조건이 대화의 배경 압력으로 작동한다

### 물질 상태

- 세렌의 암호 조각 미해독 (M15 첫 단, E016)
- 삭제예정지 주민·족보 목록 (E015)
- 사건 발생 전 날짜로 작성된 왕실 보고서 (E014)
- 귀환용 응급자원 감소분 (E014)

## 3. Time / Location

- Era: N — 건국력 640년대, 서부 잿빛 변경
- 시점: E016 조우 직후, 왕실 포위가 좁혀지는 동안의 짧은 창
- Main locations:
  1. 임시 은신실 — 제압과 첫 질문
  2. 같은 방의 다른 국면 — 제한 공개와 되물음
- 회차 전체가 한 공간에서 진행된다. 장소 이동은 없다
- 1C 주무대는 crosswalk V01 기준 `두 역사의 라베른·절검의 언덕`이며 세부 장소명은 SOFT LOCK
- 절검의 언덕은 1D 구간에 배정된 장소이므로 여기서 소모하지 않는다

## 4. Confrontation Package

Sources:

- V1 scene-ready design E017 절
- [`docs/03_systems/time-travel-ontology-v1.md`](../../../docs/03_systems/time-travel-ontology-v1.md)
- [`docs/05_characters/voice-relationship-state-bible-v1.md`](../../../docs/05_characters/voice-relationship-state-bible-v1.md) §6

### 에이든이 공개하는 것 — 제한 공개

- 미래의 멸망과 사망자 수치를 제한적으로 밝힌다
- 공개 이유는 설득이 아니라 검증이다. 상대의 반응으로 정보를 얻으려 한다
- 공개하지 않는 것: 본부 명칭·좌표·귀환 절차·자신의 임무 시한

### 세렌이 요구하는 것

- 명령의 원문
- 그 명령이 근거한 기록의 계보 — 누가 언제 무엇을 남겨서 이 명령이 성립했는가
- 요구의 성격은 목숨 구걸이 아니라 감사관의 직업적 질문이다 (C06 서부 비용장부 감사관 출신)

### 세렌이 인정하는 것

- 동의 없는 기억채취를 했다
- 이유: 사라질 주민의 증언을 붙잡기 위한 수단이었다
- 그러나 자기 방식의 피해는 축소해 말한다

### 세렌이 모르는 것

- 미래 개입의 규모와 본부 구조
- 자신이 어떤 이름으로 기록될지
- 명령을 만든 주체

### 제도적 제약

- 시간여행자는 등록된 소지품과 출발 인장이 새겨진 제한된 기록만 가져온다. 명령 원문의 물리적 보유 여부가 이 회차의 실제 쟁점이 된다
- 한 번의 암살로 문명 규모의 고정점을 제거할 수 없다는 정본 한계가 에이든에게는 아직 보이지 않는다

## 5. Character State

### 에이든 로엔

- 목표: 죽일 수 있는 상태를 유지한 채 판단 근거를 하나 더 얻는다
- 죄책감 표식: 상대를 이름이 아니라 ‘표적’으로 부른다 (정본 말투)
- 오류 가능성: 대화를 한 번 했다는 사실로 자신이 공정했다고 느낀다
- 금지: 연설로 상대를 설득, 갑작스러운 임무 포기, 세렌을 즉시 무죄로 판정

### 세렌 바일

- 목표: 자신이 아니라 주민 명단과 기록 계보를 살린다
- 태도: 무릎 꿇지 않고, 위협하지도 않는다
- 결함: 자기 방식의 피해를 축소한다. 권한을 자발적으로 내려놓지 않는다
- 정본 잠금: 영구 사망 예정 인물이며 무죄 성인화 금지
- 금지: 모든 진실을 아는 예언자, 미래 지식 과시, 봉쇄 해제 카드 선공개

### 아이리스 네르 — 부재하는 압력

- 이 회차에 등장하지 않아도 그의 조건이 에이든의 선택지를 좁힌다
- 환자를 협상 수단으로 쓰는 선택은 이미 금지돼 있다

## 6. Mystery / Information Ceiling

Active mysteries:

- M02 세렌은 왜 창시자로 기록됐는가 — 반증이 아니라 질문의 형태로만 강화. 독자 추론 가능 시점은 E061
- M15 최초 연대기는 어디 있는가 — E016의 암호에 이어 ‘기록의 계보’라는 개념이 대사로 들어온다
- M12 최종 흑막 — 사다리 첫 단은 E070. 개인 흑막 암시 금지

Reader may know:

- 에이든은 명령의 원문을 가지고 있지 않거나 요약본만 가지고 있다
- 세렌의 불법행위는 사실이며 동시에 목적이 있었다
- 표적이 자기 변호가 아니라 절차를 요구한다

Reader must not know yet:

- 세렌이 지방 소거를 늦췄다는 전체 기능
- 명령을 만든 주체와 조작 시점
- 삭제된 증언자의 정체
- 19만 생존모델의 최종 오류구조
- **세렌의 생체인장이 서부 봉쇄의 강제키라는 사실 — 이것은 E019 소관이다**

Final hook:

- 표적이 미래에서 온 명령의 원문을 요구한다
- 의미: 처형자가 자신의 근거 문서를 제시하지 못한다
- 금지: 요구 한 번으로 임무 취소, 세렌 무죄 확정, 새 시간법칙 추가

## 7. POV / Storycraft

- POV: 에이든 단일 근접 3인칭
- Scene Density: **Q형 2장면** — [`scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) V1 E017
- 배정 사유: 표적을 제압하고도 죽이지 않은 채 명령 원문과 기억채취를 두고 벌이는 단일 심문 대화가 회차 전체다
- Q형 규칙: 애도·심문·협상결렬·관계손실 계열. 장소 이동과 세력 교차를 넣지 않는다
- 설계 3비트를 2장면으로 압축한다. `대조` 비트는 Scene 2 안에서 처리한다
- Primary craft: 심문의 역전
- Secondary A: 부분적 자백
- Secondary B: 제한 공개의 교환
- Hook: H2 정보 역전
- Reader reward: 정보를 쥔 쪽이 뒤바뀌는 두 번의 전환과, 죽일 이유는 줄지 않는데 죽일 자격이 줄어드는 감각

## 8. Scene Values

### Scene 1 — 임시 은신실 · 제압과 첫 질문

- Entry: 표적을 확보하면 명령을 실행할 수 있다
- Opposition: 세렌은 저항도 애원도 하지 않고 에이든이 누구인지부터 확인한다
- Turn: 에이든이 즉시 죽이지 않는 이유가 자비가 아니라 미결 항목 때문임이 드러난다
- Exit: 제압은 끝났는데 판단은 시작되지 않았다

### Scene 2 — 같은 방 · 제한 공개와 되물음

- Entry: 미래의 사망자 수치를 대면 상대가 무너지거나 자백할 것이다
- Opposition: 세렌은 숫자를 받아들이면서 기억채취를 인정하고, 그다음 명령의 원문과 기록 계보를 요구한다
- Choice: 에이든은 제거 준비를 유지한다. 그러나 원문을 제시하지 못한다
- Exit: 유죄 판단은 남고 실행 자격은 흔들린다

## 9. Anti-Repeat

- E001의 삭제된 글자 훅 금지
- E002의 기관 순회, E016의 세력 교차 구조를 이 회차에 끌고 오지 않는다
- E003·E013·E014처럼 문서를 나란히 놓고 대조하는 장면 금지 — 이번 회차의 증거는 종이가 아니라 대답이다
- 취조실에서 악당이 진실을 알려 주는 정보전달형 대화 금지
- 세렌이 자기 무죄를 주장하는 변론 구조 금지
- 에이든의 설득 연설로 국면을 바꾸지 않는다
- E019의 봉쇄 해제 정보를 미리 쓰지 않는다
- 장소를 옮겨 장면 수를 늘리지 않는다. Q형 2장면이다

## 10. Active State / Props

- 제거 명령 — 원문이 아니라 요약·인가 형태
- 에이든의 출발 인장 (E016에서 이미 노출됨)
- 삭제예정지 주민·족보 목록 (E015)
- 기억채취 기구와 그 기록 (E015)
- 세렌의 암호 조각 — 미해독, 배경 상태
- 귀환창 잔여와 왕실 포위 진행도 — 대사에 숫자로 노출하지 않고 압력으로만 유지

명령 원문의 물리적 형태가 E018 이후 쟁점으로 재등장할 경우 A10이 prop 승격 여부를 판정한다.

## 11. State Mutation Plan

E017 종료 시 기록:

- 에이든이 세렌에게 공개한 미래 정보의 범위
- 명령 원문 미제시 사실과 그 인지 상태
- 세렌의 기억채취 자백 내용과 축소된 부분
- 세렌이 요구한 기록 계보 항목
- 제거 준비 유지 여부
- 대화에 소모된 귀환창·포위 여유
- 세렌 생존 상태 — E017 종료 시점 생존 확정

## 12. Ready Verdict

- Authority: RESOLVED
- Domain Readiness: READY
- Storycraft companion: REQUIRED / prepared separately
- POV: READY
- Scene Density: Q형 2장면 확정 · 설계 3비트를 2장면으로 압축
- Permanent-loss lock: 준수 — 세렌 사망은 E023–E025 구간
- S0: 0
- S1: 0

E017 Storycraft Manifest와 E016 상태기록 확인 뒤 A18 호출 가능.
