# Episode Context Pack — E020

Status: D10 READY  
Episode: E020  
Title: 검증할 시간, 돌아갈 시간  
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
- [`docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md`](../../../docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md) — E020 행
- [`docs/10_story_architecture/detail/v01-scene-ready-design-v1.md`](../../../docs/10_story_architecture/detail/v01-scene-ready-design-v1.md) — E020 절
- [`docs/10_story_architecture/subact-causal-matrix-v1.md`](../../../docs/10_story_architecture/subact-causal-matrix-v1.md) — 1D 행
- [`docs/10_story_architecture/scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) — V1 E020 행
- [`docs/10_story_architecture/location-world-crosswalk-v1.md`](../../../docs/10_story_architecture/location-world-crosswalk-v1.md) — V01
- [`.agent/context-packs/episodes/E019-context-pack.md`](E019-context-pack.md)
- [`docs/05_characters/cast-canon-index-v2.md`](../../../docs/05_characters/cast-canon-index-v2.md) — C01·C03·C06
- [`docs/05_characters/voice-relationship-state-bible-v1.md`](../../../docs/05_characters/voice-relationship-state-bible-v1.md)
- [`docs/11_mystery/mystery-reinforcement-ladder-v1.md`](../../../docs/11_mystery/mystery-reinforcement-ladder-v1.md) — M02·M05
- [`docs/12_losses/permanent-loss-lock-v1.md`](../../../docs/12_losses/permanent-loss-lock-v1.md) — Loss Transfer Ledger
- [`docs/01_timeline/master-chronology-and-aging-ledger-v1.md`](../../../docs/01_timeline/master-chronology-and-aging-ledger-v1.md) — J01

Episode function — 출처: 레지스트리 E020 행 / V01 설계 E020 절:

- Grand Act: GA I — 잘못된 치료
- Volume: V1 — 회색 종이 울리는 날
- Subact: 1D — 표적 제거와 귀환
- Beat: 1D · 첫 장벽
- Goal: 표적을 살리면 귀환과 미래 생존이 위험해지는 조건을 만든다
- Opposition: 이동·돌파·검증의 소요시간이 서로 겹침, 왕실군의 단계적 진입, 본부의 강제 귀환 준비 경고
- Choice: 에이든이 표적의 장부 검증 시간을 요구한다
- Cost: 검증에 배정한 시간만큼 돌파와 귀환 이동 여유가 사라진다
- State Change: `표적을 죽일 것인가`가 `세 목표 중 무엇을 버릴 것인가`로 구체화된다
- Hook (레지스트리): 왕실군이 은신처를 포위한다
- Hook (V01 설계 Exit/Hook): 개혁가의 부하들이 도주 준비를 시작한다

두 Hook의 조정: 왕실군의 단계적 진입은 Scene 3의 외부 압박으로 배치하고, 종료 훅은 설계대로 `부하들의 도주 준비`로 둔다. E019에서 이미 포위가 완성됐으므로 E020의 새 정보는 진입 단계 상승이다.

## 2. E019 Carryover

출처: E019 CP §11 / V01 설계 E019 절.

- 세렌의 생체인장이 서부 봉쇄의 강제키임이 확인됨. 아이리스가 현지 장치 구조로 검증
- 세렌이 그 권한을 자발적으로 내려놓은 적이 없다는 사실도 함께 확인됨
- 에이든은 미래 멸망과 자기 임무를 제한 공개했고, 그 정보는 회수 불가
- 본부 통신: `표적 생존 시 F0 잔여일 11일`
- 아이리스의 E012 조건 유지: 환자를 표적 접근 수단으로 쓰면 귀환표식 차단
- 귀환창은 E018에서 하루 단축된 상태

## 3. Time / Location

출처: 마스터 연대기 J01 / 위치교차표 V01 / V01 설계 E020.

- Era: N (N0), CY 640 안개월. E019 직후
- 에이든: 41세
- 무대: 개혁가 조직 은신처 — 전술도가 놓인 작전 공간, 협상 공간, 외곽 관측 지점
- 이동은 은신처 내부이며 이 회차에서 실제 돌파·귀환은 발생하지 않는다
- 정본 소요시간 (V01 설계 E020 Logistics):
  - 귀환표식까지 이동 40분
  - 포위 돌파 최소 25분
  - 장부 검증 최소 1시간
- 위 세 값의 합계가 남은 귀환창을 초과한다는 것이 이 회차의 물리적 전제다. 잔여 귀환창의 단일 수치는 정본 미지정 → `gaps`

## 4. 세 시계 — 이동·돌파·검증

출처: V01 설계 E020 Logistics·Choice Deferred / E002 CP §5 귀환석 규칙.

허용 사실:

- 세 목표는 각각 합리적이며 어느 하나도 사치가 아니다
  1. 장부 검증 — 표적의 혐의와 봉쇄 주장의 근거를 확인
  2. 포위 돌파 — 은신처에서 빠져나가는 최소 조건
  3. 귀환표식 이동 — 미래로 돌아가는 유일한 경로
- 세 목표를 모두 달성할 수 없음을 회차 안에서 명확히 한다
- 귀환석은 무제한 귀환키가 아니며 강제복귀는 사실상 한 번이다
- 본부는 강제 귀환 준비를 경고한다

금지:

- 시간 수치를 마법·장비·요령으로 단축
- 귀환표식을 만능 탈출구로 제시
- `시간이 없다`는 대사만으로 압박을 선언하고 실제 계산을 생략
- 세 목표 중 하나를 명백히 무가치한 선택지로 만들어 딜레마를 해소

## 5. Character State

출처: cast-canon-index-v2 C01·C03·C06 / cast-encyclopedia C03·C06 / voice bible §2·§3·§5.

### 에이든 로엔 (C01)

- 목표: 검증 시간을 확보하되 귀환 가능성을 잃지 않는 배분을 찾는다
- 이 회차의 행동: 세렌에게 장부와 봉쇄권을 넘기면 생존을 돕겠다고 제안한다
- 오류 가능성: 세 목표의 시간을 조금씩 깎으면 전부 담을 수 있다는 계산
- 말투: `목표·출구·비용` 순서. 협상에서도 조건과 기한을 먼저 말한다
- 금지: 미래 기관의 이름으로 검증 불가능한 보증을 남발, 임무 취소 선언

### 세렌 바일 (C06)

- 목표: 주민 주소를 보호하는 조건이 없으면 아무것도 넘기지 않는다
- 거부 근거: 미래 기관의 약속을 현지에서 검증할 방법이 없다
- 결함: 폭로 속도를 주민대피보다 우선할 수 있고, 동맹과 정보를 일부 숨긴다
- 이 회차에서 숨기는 것: 부하들이 이미 이동 준비를 시작했다는 사실
- 금지: 협상 중 무죄 증명 문서 제시, 자기 죽음의 의미 선포

### 아이리스 네르 (C03)

- 이 회차의 기능: 전술도 앞에서 대피로·포위선·귀환표식 위치를 현지 지식으로 채운다
- 자기 일정: 환자 수레와 주민 대피가 그의 우선순위이며 에이든의 계산에 종속되지 않는다
- 협상 태도: 상대의 원칙보다 누가 언제 무엇을 잃는지 묻는다
- 금지: 에이든의 부관 역할, 세렌의 대변인 역할

### 왕실군

- 단계적 진입을 시작한다. 무차별 학살이 아니라 기록 확보와 봉쇄 유지가 목표다 (E016 기준 유지)
- 얼굴 없는 배경 병력으로 처리하지 않는다
- 금지: 개인 악역 지휘관을 새로 확정

### 본부

- 강제 귀환 준비를 경고한다. 통신 수치와 절차로만 등장
- 금지: 개인 흑막 지목

## 6. Mystery / Information Ceiling

출처: 미스터리 사다리 M02·M05 / 인물 정보상한 §5.

Active mysteries:

- M02 세렌 바일은 왜 창시자로 기록됐는가 — 장부가 검증 대상으로 올라오지만 E020에서 결론이 나오지 않는다
- M05 빈 세금장부에 무엇이 있었는가 — 세렌의 장부가 이 계열과 이어진다는 암시만 허용

독자가 알아도 되는 것:

- 세 목표의 실제 소요시간과 그 합이 남은 시간을 넘는다는 사실
- 세렌이 거부하는 이유가 고집이 아니라 검증 불가능한 약속에 대한 합리적 불신이라는 것
- 본부가 강제 귀환 카드를 준비했다는 것

독자가 아직 몰라야 하는 것:

- 장부의 실제 내용과 결재계보
- 세렌이 지방 소거를 늦추고 있었다는 전체 기능
- 기록을 뒤집은 주체
- 삭제된 증언자의 정체
- 19만 모델과 잔여일 계산의 최종 오류구조

## 7. POV / Storycraft

출처: 밀도지도 V1 E020 행 / DEC-021.

- POV: 에이든 단일 근접 3인칭
- **Scene Density: S · 3장면** — 밀도지도 사유: 전술도 계산·협상·외부 압박으로 이동 40분과 검증 1시간이 양립 불가함을 보여주는 3장면
- V01 설계의 기능 비트 3개와 실제 장면 수가 1:1로 대응하는 회차다
- Primary craft: 양립 불가능한 세 시계
- Secondary A: 검증할 수 없는 약속의 협상
- Secondary B: 반대편의 단계적 행동으로 만드는 압박
- Hook: H1 물리적 귀환위험 + H3 상대의 독립 행동
- Reader reward: 딜레마가 감정 선언이 아니라 분 단위 숫자로 성립하는 경험

## 8. Scene Values — 3장면

### Scene 1 — 은신처 전술도

- Entry: 검증도 하고 돌아갈 수도 있다
- Action: 대피로·왕실 포위선·귀환표식 위치를 계산한다. 이동 40분, 돌파 최소 25분, 검증 최소 1시간이 표에 올라간다. 아이리스가 현지 지식으로 빈칸을 채우며 자기 우선순위도 표에 올린다
- Exit: 세 목표의 합계가 남은 시간을 넘는다

### Scene 2 — 협상

- Entry: 표적이 협조하면 시간이 줄어든다
- Action: 에이든이 장부와 봉쇄권을 넘기면 생존을 돕겠다고 제안한다. 세렌은 주민 주소가 보호되지 않으면 거부한다. 미래 기관의 보증은 현지에서 검증할 수 없다
- Exit: 협조로 시간을 벌 길이 막히고, 에이든은 검증 시간을 스스로 요구해 배정한다

### Scene 3 — 외부 압박

- Entry: 배정한 시간표대로 움직이면 된다
- Action: 왕실군이 단계적 진입을 시작하고 본부가 강제 귀환 준비를 경고한다. 시간표가 두 방향에서 동시에 깎인다
- Exit: 선택은 유예되지만 선택지 자체가 줄어든다. 세렌의 부하들이 도주 준비를 시작한다

## 9. Anti-Repeat

- E002의 승인 대기 지연을 재연하지 않는다. E002는 제도 절차가 시간을 먹었고, E020은 이동·돌파·검증의 물리 소요시간이 서로를 먹는다
- E003처럼 세 장면을 모두 자료 검토로 채우지 않는다
- E019의 두 사람 대면 구도를 반복하지 않는다. 세 장면에 각각 다른 인물 구성이 들어간다
- E001의 삭제된 글자 훅, E002의 귀환석 토양, E003의 두 문서 대조를 되살리지 않는다
- 숫자 카운트다운을 장면마다 되풀이하지 않는다. 시간은 표에서 한 번 확정되고 이후에는 깎이는 원인만 보여 준다
- `시간이 없다`는 대사로 압박을 선언하지 않는다
- 왕실군을 얼굴 없는 포위선으로만 쓰지 않는다
- 세렌의 거부를 비합리적 고집으로 그리지 않는다
- 협상 결렬을 E022의 최종 결렬과 같은 방식으로 처리하지 않는다. E020은 조건 부재로, E022는 상호 책임 대상의 차이로 결렬된다

## 10. Active State / Props

- 은신처 전술도 — 이동·돌파·검증 시간이 기입되는 물건
- 세렌의 장부 — 검증 대상. 내용은 아직 공개되지 않는다
- 세렌의 생체인장 — 봉쇄 강제키. E019에서 기능 확정
- 귀환표식 — 아이리스의 차단 권한 아래 있는 귀환 경로
- 본부 강제 귀환 경고
- 절검 — 배경 유지
- 회색 종 — 이 회차에서 울리지 않는다

## 11. State Mutation Plan

E020 종료 시 기록한다.

- 세 시계의 확정 수치와 잔여 귀환창
- 에이든이 검증에 배정한 시간과 그로 인해 깎인 항목
- 봉쇄권 이전 제안의 조건과 거부 사유
- 세렌이 요구한 주민 주소 보호의 구체 조건
- 왕실군 진입 단계
- 본부 강제 귀환 준비 상태
- 아이리스의 우선순위와 귀환표식 조건 상태
- 세렌 부하들의 이동 준비 인지 여부 — 에이든은 아직 목적을 모른다

## 12. Ready Verdict

- Authority: RESOLVED
- Domain Readiness: READY
- Storycraft companion: REQUIRED / 별도 준비 완료
- POV: READY
- Scene Density 일치: PASS — S · 3장면 / 설계 장면 3개
- S0: 0
- S1: 0

E020 Storycraft Manifest와 E019 상태 확인 뒤 A18 호출 가능.
