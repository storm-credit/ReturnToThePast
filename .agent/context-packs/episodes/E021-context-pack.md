# Episode Context Pack — E021

Status: D10 READY  
Episode: E021  
Title: 도주처럼 보이는 대피  
Compiled By: A21 Context Pack Compiler  
Reference: `agent/1d-target-removal-and-return`

> 이 CP는 정본이 아니다. 충돌 시 원본 정본과 권한계층을 따른다. 각 항목의 출처는 절마다 표시한다.

## 1. Authority / Architecture

Required sources:

- [`/AI_PROJECT.md`](../../../AI_PROJECT.md)
- [`docs/00_project/canon-constitution-v1.md`](../../../docs/00_project/canon-constitution-v1.md)
- [`docs/00_project/canon-naming-pack-v1.md`](../../../docs/00_project/canon-naming-pack-v1.md)
- [`docs/00_project/terminology-and-addressing-clarification-v1.md`](../../../docs/00_project/terminology-and-addressing-clarification-v1.md)
- [`docs/00_project/decision-log.md`](../../../docs/00_project/decision-log.md) — DEC-016·017·018·020·021
- [`docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md`](../../../docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md) — E021 행
- [`docs/10_story_architecture/detail/v01-scene-ready-design-v1.md`](../../../docs/10_story_architecture/detail/v01-scene-ready-design-v1.md) — E021 절
- [`docs/10_story_architecture/subact-causal-matrix-v1.md`](../../../docs/10_story_architecture/subact-causal-matrix-v1.md) — 1D 행
- [`docs/10_story_architecture/scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) — V1 E021 행
- [`docs/10_story_architecture/location-world-crosswalk-v1.md`](../../../docs/10_story_architecture/location-world-crosswalk-v1.md) — V01
- [`.agent/context-packs/episodes/E020-context-pack.md`](E020-context-pack.md)
- [`docs/05_characters/cast-canon-index-v2.md`](../../../docs/05_characters/cast-canon-index-v2.md) — C01·C03·C06
- [`docs/05_characters/cast-encyclopedia-v1.md`](../../../docs/05_characters/cast-encyclopedia-v1.md) — C03·C06
- [`docs/05_characters/voice-relationship-state-bible-v1.md`](../../../docs/05_characters/voice-relationship-state-bible-v1.md)
- [`docs/11_mystery/mystery-reinforcement-ladder-v1.md`](../../../docs/11_mystery/mystery-reinforcement-ladder-v1.md) — M02·M05·M13
- [`docs/12_losses/permanent-loss-lock-v1.md`](../../../docs/12_losses/permanent-loss-lock-v1.md) — Loss Transfer Ledger

Episode function — 출처: 레지스트리 E021 행 / V01 설계 E021 절:

- Grand Act: GA I — 잘못된 치료
- Volume: V1 — 회색 종이 울리는 날
- Subact: 1D — 표적 제거와 귀환
- Beat: 1D · 잘못된 해석
- Goal: 표적의 도주 준비가 유죄처럼 보이지만 환자 대피 계획임이 드러난다
- Opposition: 무기와 위조신분이라는 실제 물증, 남은 시간, 아이리스의 거부권
- Choice: 에이든은 대피를 돕지 않고 장부만 확보하려 한다
- Cost: 일부 대피를 돕지 않음. 현지 앵커와의 신뢰가 조건 위반 직전까지 감
- State Change: 오해는 정정되지만 행동은 정정되지 않는다. 정보의 정확성과 선택의 정당성이 처음으로 분리된다
- Hook: 현지 앵커가 귀환표식을 끊겠다고 위협한다 (레지스트리)
- Hook (V01 설계 Exit/Hook): 첫 환자 수레가 왕실군에게 발견된다

두 Hook의 조정: 아이리스의 단절 선언은 Scene 3의 종결값으로, 첫 환자 수레 발각은 Scene 4의 반대편 능동행동이자 회차 종료 훅으로 배치한다. 밀도지도 E021 사유가 이 순서를 명시한다.

## 2. E020 Carryover

출처: E020 CP §11 / V01 설계 E020 절.

- 세 시계 확정: 귀환표식까지 이동 40분, 포위 돌파 최소 25분, 장부 검증 최소 1시간. 합계가 남은 귀환창을 초과
- 에이든이 검증 시간을 요구해 배정했고 그만큼 다른 항목이 깎임
- 봉쇄권 이전 제안은 주민 주소 보호 조건 부재로 결렬
- 왕실군 단계적 진입 진행 중, 본부는 강제 귀환 준비 경고
- 세렌의 부하들이 이동 준비를 시작함 — 에이든은 목적을 모름
- 아이리스는 환자 수레와 주민 대피를 자기 항목으로 전술도에 올려 둔 상태
- E012 조건 유지: 환자를 표적 접근 수단으로 쓰면 귀환표식 차단

## 3. Time / Location

출처: 마스터 연대기 J01 / 위치교차표 V01 / V01 설계 E021.

- Era: N (N0), CY 640 안개월. E020 직후
- 에이든: 41세
- Main locations:
  1. 은신처 지하창고
  2. 수레열 집결 지점
  3. 귀환표식
  4. 은신처 외곽 — 왕실군 접촉 지점
- 이동은 은신처와 그 인접 구역 안. 귀환표식까지의 40분 이동은 이 회차에서 실행하지 않는다
- 회차 전체가 배정된 시간 안에서 진행되며, 장면마다 남은 시간이 줄어든다

## 4. 도주 증거와 대피 증거

출처: V01 설계 E021 Scene 1·2, `Independent Agency` / E015 False Interpretation 구조 / cast-encyclopedia C06 결함.

같은 물건이 두 가지로 읽히는 구조다.

### 도주·반란으로 읽히는 근거

- 지하창고에 무기가 있다
- 위조신분이 다량으로 준비돼 있다
- 조직이 왕실군 포위 중에 이동을 시작했다
- 세렌은 E020 협상에서 부하들의 이동 준비를 말하지 않았다

### 대피로 확인되는 근거

- 위조신분은 삭제 예정 주민의 **새 주소**다
- 무기는 호송 방어용이다
- 아이리스가 현지 지식으로 두 사실을 확인한다

### 정정 뒤에도 남는 것

- 세렌 조직은 실제로 무장했고 위조 문서를 만들었다. 불법행위 자체는 사라지지 않는다
- 세렌이 정보를 숨긴 것도 사실이다 — 그의 정본 결함이다
- 정정은 에이든의 판단을 바꾸지만 행동을 바꾸지 않는다

금지:

- 무기와 위조신분을 전부 선의로 세탁
- 세렌 조직을 무결한 구호단체로 전환
- 오해가 풀렸다는 이유로 에이든이 임무를 취소
- 이 회차에서 새 주소 목록의 전체 내용을 공개

## 5. Character State

출처: cast-canon-index-v2 C01·C03·C06 / cast-encyclopedia C03·C06 / voice bible §2·§3·§5·§6.

### 에이든 로엔 (C01)

- 목표: 배정한 검증 시간 안에 장부를 확보한다
- 이 회차의 행동: 정정을 듣고 사실로 받아들이면서도 대피를 돕지 않는다
- 죄책감 표식: 사람을 이름 대신 `환자·주민·표적`이라는 역할명으로 부른다
- 오류 가능성: `사실을 정확히 파악했으므로 내 선택도 정당하다`는 혼동
- 금지: 오해를 인정하며 임무 취소, 대피를 전면 지원, 아이리스를 설득해 조건을 철회시키기

### 아이리스 네르 (C03)

- 역할: 현지 앵커. 대피·귀환표식 차단·민병 협상 전문
- 이 회차의 기능: 오해를 정정하는 사람이자 거부권을 행사하는 사람
- 독립 선택: 세계 구원 논리에도 현지인을 희생시키는 데 동의하지 않는다
- 단절 선언은 배신이 아니라 E012에서 이미 통보한 조건의 집행이다
- 거짓 믿음: 눈앞의 사람을 지키면 후대와 외부국에 생기는 비용은 나중에 해결할 수 있다 — 이 회차에서 교정되지 않는다
- 금지: 감정적 배신 연출, 에이든의 양심 대변, 협박을 흥정 카드로 반복 사용

### 세렌 바일 (C06)

- 이 회차에서는 조직의 이동을 지휘하는 위치에 있으나 전면에 나서지 않는다
- 정보를 일부 숨긴 결함이 여기서 실제 대가를 만든다
- 금지: 자기 조직의 무장을 부인, 위조 문서를 도덕적으로 정당화하는 연설

### 왕실군

- 첫 환자 수레를 발견한다. 우연이 아니라 단계적 진입의 결과다
- 기록 확보와 봉쇄 유지가 목표이며 학살이 목적이 아니다
- 금지: 새 개인 악역 지휘관 확정

## 6. Mystery / Information Ceiling

출처: 미스터리 사다리 M02·M05·M13 / 인물 정보상한 §5.

Active mysteries:

- M02 세렌 바일은 왜 창시자로 기록됐는가 — 대피 계획은 정황이며 확정 근거가 아니다. 추론 가능 시점은 E061
- M05 빈 세금장부에 무엇이 있었는가 — `삭제 예정 주민의 새 주소`가 이 계열과 이어진다는 암시만 허용
- M13 움브라는 어디서 왔는가 — 주소를 잃는 사람들이 발생한다는 사실만. 집단 형성은 언급 금지

독자가 알아도 되는 것:

- 위조신분이 삭제 예정 주민의 새 주소이고 무기는 호송 방어용이라는 사실
- 세렌 조직이 실제로 무장했고 위조 문서를 만들었다는 사실
- 에이든이 정확한 정보를 얻고도 선택을 바꾸지 않는다는 사실
- 아이리스의 단절 조건이 새 위협이 아니라 기존 조건의 집행이라는 사실

독자가 아직 몰라야 하는 것:

- 새 주소 목록의 전체 내용과 규모
- 세렌이 지방 소거와 비용전가를 늦추고 있었다는 전체 기능
- 소거 결정의 결재계보와 기록을 뒤집은 주체
- 삭제된 증언자의 정체
- 19만 모델과 잔여일 계산의 최종 오류구조

## 7. POV / Storycraft

출처: 밀도지도 V1 E021 행 / DEC-021.

- POV: 에이든 단일 근접 3인칭
- **Scene Density: E · 4장면** — 밀도지도 `고정`. 사유: 지하창고의 오해, 수레열에서의 정정, 귀환표식에서 아이리스의 단절 선언이 이어지고 첫 환자 수레가 발각되는 반대편 행동이 붙는다
- V01 설계는 기능 비트 3개로 적혀 있다. DEC-021에 따라 실제 장면은 4개이며, 네 번째 장면은 밀도지도가 지정한 **반대편의 능동행동**이다
- Primary craft: 정정되는 정보와 정정되지 않는 행동
- Secondary A: 현지인의 거부권 집행
- Secondary B: 같은 물건의 두 가지 판독
- Hook: H3 상대의 독립 행동 + H1 물리적 귀환위험
- Reader reward: 진실을 알게 된 주인공이 그 진실대로 행동하지 않는 것을 보는 불편함

## 8. Scene Values — 4장면

### Scene 1 — 은신처 지하창고

- Entry: 표적 조직은 검증에 협조하지 않고 도망치려 한다
- Action: 무기와 위조신분이 발견된다. 포위 중의 이동, 숨겨진 준비, 무장이 도주·반란의 증거로 정렬된다
- Exit: 표적의 유죄 서사가 다시 강해진다

### Scene 2 — 수레열 집결 지점

- Entry: 물증은 도주를 가리킨다
- Action: 아이리스가 위조신분이 삭제 예정 주민의 새 주소이며 무기가 호송 방어용임을 현지 지식으로 확인한다. 동시에 조직이 실제로 무장했고 세렌이 이 사실을 숨겼다는 점도 남는다
- Exit: 해석은 정정되지만 시간은 정정되지 않는다. 에이든은 장부 확보를 우선하기로 한다

### Scene 3 — 귀환표식

- Entry: 정확히 알았으니 내 선택도 정당하다
- Action: 아이리스가 에이든이 환자보다 장부와 표적만 택하면 귀환 연결을 끊겠다고 선언한다. 이는 E012 조건의 집행이다
- Exit: 귀환 경로가 에이든의 통제 밖에 있음이 확정된다

### Scene 4 — 은신처 외곽

- Entry: 시간표대로 장부만 확보하면 된다
- Action: 왕실군의 단계적 진입 결과로 첫 환자 수레가 발견된다. 에이든이 돕지 않기로 한 대피의 첫 대가가 즉시 발생한다
- Exit: 선택의 비용이 미래가 아니라 이 자리에서 사람 단위로 청구된다

## 9. Anti-Repeat

- E015의 `병원처럼 보이는 실험실` 오해 구조를 반복하지 않는다. E015는 에이든의 해석이 뒤집혀 행동이 바뀌었고, E021은 해석이 뒤집혀도 행동이 바뀌지 않는다. 이것이 이 회차의 핵심 차이다
- E009의 두 출생증명, E003의 두 문서 대조 같은 서류 반전 구조를 쓰지 않는다. 여기서 판독이 갈리는 것은 무기와 신분증이라는 물건이다
- E001의 삭제된 글자 훅을 반복하지 않는다
- E002의 여섯 기관 순회와 귀환석 토양을 되살리지 않는다
- E019의 두 사람 대면 심문, E020의 전술도 계산을 다시 중심에 두지 않는다
- 아이리스의 단절 선언을 감정적 배신·연인 갈등처럼 연출하지 않는다
- 무기와 위조신분을 전부 선의로 세탁하지 않는다
- 첫 환자 수레 발각을 에이든의 실수 한 번으로 환원하지 않는다. 왕실군의 단계적 진입이라는 이미 진행 중인 원인의 결과다
- 네 번째 장면을 에필로그성 여운으로 쓰지 않는다. 반대편의 능동행동이어야 한다

## 10. Active State / Props

- 위조신분 문서 — 삭제 예정 주민의 새 주소. 내용 전체는 미공개
- 지하창고의 무기 — 호송 방어용. 불법성은 유지
- 환자 수레열 — 첫 수레가 발각됨
- 세렌의 장부 — 에이든의 우선 확보 목표. 이 회차에서 확보 완료되지 않는다
- 귀환표식 — 아이리스의 차단 권한이 처음으로 발동 선언됨
- 세렌의 생체인장 — 배경 유지
- 절검 — 배경 유지
- 회색 종 — 이 회차에서 울리지 않는다

위조신분 문서가 E022 이후 재등장할 경우 A10이 prop 승격 여부를 판정한다.

## 11. State Mutation Plan

E021 종료 시 기록한다.

- 위조신분·무기의 판독 결과와 정정 시점
- 에이든이 대피를 돕지 않은 범위와 그 이유
- 장부 확보 진행 상태
- 아이리스의 귀환표식 단절 선언 상태와 발효 조건
- 왕실군에게 발견된 첫 환자 수레의 처리 상태
- 남은 검증 시간과 잔여 귀환창
- 세렌이 정보를 숨긴 사실의 기록 — V03 무죄 입증 시에도 삭제되지 않는 결함
- 에이든–아이리스 신뢰 등급 변동

## 12. Ready Verdict

- Authority: RESOLVED
- Domain Readiness: READY
- Storycraft companion: REQUIRED / 별도 준비 완료
- POV: READY
- Scene Density 일치: PASS — E · 4장면 / 설계 장면 4개
- S0: 0
- S1: 0

E021 Storycraft Manifest와 E020 상태 확인 뒤 A18 호출 가능.
