# Episode Context Pack — E024

Status: D10 READY  
Episode: E024  
Title: 성공 판정  
Compiled By: A21 Context Pack Compiler  
Reference: `agent/1d-subact-context-packs`

> 이 CP는 정본이 아니다. 충돌 시 원본 정본과 권한계층을 따른다.

## 1. Authority / Architecture

Required sources:

- [`/AI_PROJECT.md`](../../../AI_PROJECT.md)
- [`docs/00_project/canon-constitution-v1.md`](../../../docs/00_project/canon-constitution-v1.md)
- [`docs/00_project/canon-naming-pack-v1.md`](../../../docs/00_project/canon-naming-pack-v1.md)
- [`docs/00_project/terminology-and-addressing-clarification-v1.md`](../../../docs/00_project/terminology-and-addressing-clarification-v1.md)
- [`docs/00_project/decision-log.md`](../../../docs/00_project/decision-log.md) — DEC-016·017·018·020·021
- [`docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md`](../../../docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md) — E024 행
- [`docs/10_story_architecture/detail/v01-scene-ready-design-v1.md`](../../../docs/10_story_architecture/detail/v01-scene-ready-design-v1.md) — Subact 1D, E024 절
- [`docs/10_story_architecture/subact-causal-matrix-v1.md`](../../../docs/10_story_architecture/subact-causal-matrix-v1.md) — 1D
- [`docs/10_story_architecture/scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) — V1 E024
- [`docs/10_story_architecture/location-world-crosswalk-v1.md`](../../../docs/10_story_architecture/location-world-crosswalk-v1.md) — V01 1D
- [`docs/05_characters/cast-canon-index-v2.md`](../../../docs/05_characters/cast-canon-index-v2.md) — C01·C03·C06
- [`docs/05_characters/voice-relationship-state-bible-v1.md`](../../../docs/05_characters/voice-relationship-state-bible-v1.md) — §2·§3·§5
- [`docs/09_collection/relic-encyclopedia-r01-r12-v1.md`](../../../docs/09_collection/relic-encyclopedia-r01-r12-v1.md) — R03
- [`docs/09_collection/asset-state-checkpoints-v1.md`](../../../docs/09_collection/asset-state-checkpoints-v1.md) — R03 V1 행
- [`docs/12_losses/permanent-loss-lock-v1.md`](../../../docs/12_losses/permanent-loss-lock-v1.md) — L001, LD, LR
- [`docs/11_mystery/mystery-reinforcement-ladder-v1.md`](../../../docs/11_mystery/mystery-reinforcement-ladder-v1.md) — M02·M15·M16
- [`docs/01_timeline/master-chronology-and-aging-ledger-v1.md`](../../../docs/01_timeline/master-chronology-and-aging-ledger-v1.md) — J01

Episode function:

- Grand Act: GA I — 잘못된 치료
- Volume: V1 — 회색 종이 울리는 날
- Subact: 1D — 표적 제거와 귀환
- Beat: 국소 해결
- Goal: 임무를 공식적으로 종결하고 귀환 조건을 성립시킨다 (registry E024)
- Opposition: 등록 용량의 물리 한계, 아이리스 네르의 동행 거부, 마지막 단계에 든 귀환창, E023 직후 서부를 덮은 왕실 기록망
- Choice: 세렌 바일의 절검과 소거명부 일부를 동반 등록한다 (registry E024)
- Cost: 확보한 증거의 대부분을 현지에 남기고, 현지 관계와 용서 가능성을 잃는다
- State Change: ‘임무를 수행한 사람’이 ‘성공으로 판정된 사람’이 된다. 판정은 성립하지만 그 판정을 내리는 본부의 이름이 이미 달라져 있다
- Hook: 귀환 좌표 표시가 출발 본부와 다른 명칭을 띠고, 출발 인장에서 F0 동료의 이름이 사라진다 (registry E024 / V01 E024 Exit·Hook)

## 2. E019–E023 Carryover

### 에이든 로엔

- 세렌 바일을 직접 살해했다. 확신해서가 아니라 불확실성을 감당하지 못해 죽였음을 스스로 안다 (`V01` E023 Character Cost)
- 두 목표 중 ‘표적 제거’는 완료, ‘연대기 접근 차단’은 세렌의 생체인장 정지로 결과가 뒤집혀 있다
- E022에서 세렌에게서 소거될 마을·가족·환자 명단을 직접 건네받았다
- 죄책감 상태의 말버릇: 상대 이름을 피하고 `표적`·`환자`·`요원` 같은 역할명으로 부른다 (`voice bible` §2)

### 세렌 바일 (C06)

- 영구 사망. LOCKED. 재시도·부활·다른 시간대 버전 대체 금지 (`LOCK` L001)
- 그의 생체인장이 꺼지며 서부 봉쇄가 풀렸고 왕실 기록망이 서부를 덮었다 (`V01` E023 Scene 3)
- 유해·유품의 권리는 유족·운동·현지 공동체에 있다 (`relic-encyclopedia` R03 소유권)

### 아이리스 네르 (C03)

- E021에서 귀환 연결을 끊겠다고 선언한 상태로 E024에 들어온다
- E022의 탈출로 개방 덕분에 환자 수레 일부가 빠져나갔고, 일부는 왕실군에게 발견됐다
- 세계 구원 논리로 현지인을 희생시키는 데 동의하지 않는다 (`V01` 1D Independent Agency)

### 현지 상태

- 도시 전체의 회색 종이 동시에 울렸고 주민 이름이 장부에서 흐려졌다 (`V01` E023 Hook)
- 왕실 기록망이 서부 기록 접근을 확대 중 (`V01` Volume Exit State Ledger — Institutions)

### 귀환석·귀환창

- 중심층 3갈래 균열, 강제복귀 1회, 최대 오착 18km (`E002-state-mutation` §4)
- E018에서 귀환창 하루 단축, E022에서 마지막 단계 진입 (`V01` E018·E022)
- 현장수리 불가, 교체가 원칙

## 3. Time / Location

- Timeline: Era N (N0), 건국력 640년 안개월 하순 — 도착일 안개월 4일 기준 약 20일 경과 (`master-chronology` J01 + V1 주관경과 24일에서 도출)
- 에이든: 41세 / 주관적 누적일 V1 구간 말미
- Main locations (Q형 2장면):
  1. 귀환표식 앞 등록대 — 세렌의 은신처 기록실에서 회수한 물건을 정리·등록하는 자리
  2. 귀환표식 개방 지점 — 아이리스와 갈라지고 통과가 시작되는 자리
- 이동은 E023 기록실 → 귀환표식까지의 짧은 현지 이동이며, `V01` E020의 ‘귀환표식까지 40분’ 계산이 그대로 실행 조건이 된다
- 1D 주무대는 `귀환점·F1 수도 잔존부`이며 E024는 그중 귀환점 쪽만 사용한다 (`location-world-crosswalk` V01)

## 4. 귀환 등록 조건

Sources: `V01` E024 Logistics / `relic-encyclopedia` R03 / `asset-state-checkpoints` R03 / `time-travel-ontology` 계열 정본

### 등록 규칙

- 등록되지 않은 물건과 사람은 귀환할 수 없다
- 강제 추가등록은 귀환 실패를 부른다
- 귀환은 무제한 반출구가 아니라 질량·주소·승인을 가진 통로다
- 이 규칙은 관료의 심술이 아니라 오착·귀환불능을 막는 실제 안전조건이다

### 절검 (R03)

- 첫 개혁가가 군용검을 짧게 부러뜨려 기록봉인·구조 작업용으로 개조한 도구
- 전투력보다 고정 인장·봉인끈·장부결속을 절단한다
- 세렌이 남긴 손상·혈흔·사용기록 때문에 첫 임무의 물질 증거가 된다
- 에이든이 보유해도 전리품이 아니라 증거이자 부채다
- E024에서 기능·소유권을 확정하지 않는다 (`asset-state-checkpoints` R03: ‘L — 기능·소유권 미확정’)

### 소거명부 일부

- E022에서 세렌이 건넨 마을·가족·환자 명단
- 전부는 등록되지 않는다. 확보분에는 누락과 오염이 있다 (`V01` Volume Exit State Ledger — Assets)
- 무엇을 남기고 무엇을 가져갈지가 E024의 실제 선택이다

### 등록되지 못하는 것

- 현지 사람
- 부피가 큰 원본 묶음
- 등록 형식에 맞지 않는 현지 물품
- 아이리스가 지키기로 한 환자 관련 자료

## 5. Character State

### 에이든 로엔 (C01)

- 목표: 임무를 종결하고 살아서 돌아가되, 자신이 죽인 사람이 남긴 명단을 버리지 않는다
- 내적 압박: 성공 판정이 내려질수록 죽음이 절차상 정당해지는 감각
- 전문: 목표·출구·비용 순서로 말한다 (`voice bible` §2)
- 오류 가능성: 물건을 챙기는 행위로 죄책을 처리하려 함
- 금지: 자기 행동을 즉석에서 오판으로 선언하고 임무를 부인하는 참회 연설. 책임 확정은 E058–E075다 (`LOCK` L003)

### 아이리스 네르 (C03)

- 역할: 남는 사람. 환자 호송을 택하고 귀환하지 않는다 (`V01` E024 Scene 2)
- 요구: 명단을 잊지 말 것. 그러나 용서하지 않는다
- 말투: 사람·장소·오늘 필요한 물자를 구체적으로 말하고, 상대의 원칙보다 누가 언제 무엇을 잃는지 묻는다 (`voice bible` §2)
- 금지: 눈물의 배웅, 로맨스 신호, 미래 구원 논리에 대한 뒤늦은 동의

### 본부 귀환 관제 (앙카 귀환다리 기능선)

- 신호·판정으로만 존재하는 비대면 기능이며 새 핵심 인물을 즉석 확정하지 않는다
- 임무 성공 판정과 등록 승인은 서로 다른 절차다
- 판정 문구는 축하가 아니라 회계에 가깝다
- 금지: 판정자를 흑막으로 암시

### 세렌 바일 (C06)

- 시신·유품·인장으로만 등장한다
- 그의 개혁 의제는 이후 기록·잔문에 잔흔으로만 남는다 (`LOCK` LD L001)
- 금지: 사후 독백, 유언 영상, 장례보석 사용 — 장례보석 최초 사용은 V8이다

## 6. Mystery / Information Ceiling

Active mysteries:

- M02 세렌 바일은 왜 창시자로 기록됐는가
- M15 최초 연대기는 어디 있는가 — 세렌의 암호(E016)가 절검·명부와 함께 물러남
- M16 회색 종은 무엇을 감지하는가 — E023의 동시 타종 이후 잔여 상태

독자가 알아도 되는 것:

- 임무는 공식 절차상 성공으로 판정된다
- 세렌 제거가 서부 봉쇄를 실제로 해제했다
- 등록 가능한 증거의 총량이 물리적으로 제한된다
- 귀환 좌표 표시의 명칭이 출발지와 다르다

독자가 아직 몰라야 하는 것:

- 세렌의 행위가 지방 소거를 늦추고 있었다는 전체 기능
- 기록을 뒤집은 조작 주체와 이유
- 삭제된 증언자의 정체
- 19만 증가 모델의 최종 오류구조
- 좌표 명칭이 다른 이유, 즉 F1의 존재와 성격
- 절검의 후대 기능과 최종 운명

Final hook:

- 귀환 좌표 표시가 출발 본부와 다른 명칭을 띤다
- 귀환 직전 출발 인장에서 F0 동료의 이름이 사라진다
- 의미: 변경은 이미 시작됐고, 그것이 먼저 나타나는 곳은 세계가 아니라 그의 서류다
- 금지: 에이든이 이 자리에서 시간선 변경을 이해하고 명명하는 것

## 7. POV / Storycraft

- POV: 에이든 단일 근접 3인칭
- Scene Density: **Q형 2장면** (`scene-density-map` V1 E024 — 고정)
- 배정 사유(원문): 절검과 소거명부를 등록하는 과정과 아이리스와의 이별이 겹쳐 관계 손실을 확정하는 회차
- Primary craft: 반출 목록 선택 — 무엇을 등록할지가 곧 무엇을 버릴지
- Secondary A: 절차가 애도를 대신하는 아이러니
- Secondary B: 용서 없는 이별
- Hook: H2 정보 역전 + H4 제도변화
- Reader reward: 승리 장면 대신, 성공이 서류로 확정되는 순간의 온도

## 8. Scene Values

### Scene 1 — 귀환표식 앞 등록대

- Entry: 표적을 죽였으니 남은 일은 증거를 챙겨 돌아가는 절차뿐이다
- Opposition: 등록 용량과 형식이 확보한 증거보다 작다. 강제 추가등록은 귀환 실패를 부른다
- Turn: 에이든은 절검과 소거명부 일부를 등록하고 나머지를 현지에 남기는 목록을 직접 작성한다
- Exit: 증거의 대부분을 포기함으로써 그의 판단을 검증할 수단도 함께 줄어든다

### Scene 2 — 귀환표식 개방 지점

- Entry: 아이리스가 함께 가거나, 최소한 배웅하리라 기대한다
- Opposition: 아이리스는 환자 호송을 택하고 남는다. 요구는 하나, 명단을 잊지 말 것. 용서는 하지 않는다
- Choice: 에이든은 붙잡지 않고, 자기 이름으로 성공 판정을 수령한 뒤 통과에 들어간다
- Cost: 관계 손실 확정. 현지에 남긴 증거·사람에 대한 책임은 등록되지 않는다
- Exit/Hook: 좌표 표시가 다른 명칭을 띠고, 출발 인장에서 F0 동료의 이름이 사라진다

## 9. Anti-Repeat

- E001처럼 삭제된 글자 하나가 되살아나는 훅으로 되돌아가지 않는다. E024의 소실은 ‘되살아남’이 아니라 ‘조용히 없어짐’이다
- E002의 기관 순회·서명 릴레이를 반복하지 않는다. 등록은 한 자리에서 한 번에 끝난다
- E003의 두 문서 대조로 모순을 확인하는 구성을 쓰지 않는다. 여기서는 대조할 두 번째 문서가 이미 사라졌다
- E021의 ‘귀환표식을 끊겠다’는 위협을 재연하지 않는다. 아이리스는 위협하지 않고 그냥 남는다
- E022의 명단 수령 장면을 되풀이하지 않는다. 명단은 이미 손에 있고, 문제는 그중 얼마가 등록되는가다
- E023의 전투·회색 종 동시 타종을 재사용하지 않는다
- 절검을 각성 무기·전리품·유물 등급표로 다루지 않는다
- 아이리스가 마지막에 용서하거나 동행하는 전개 금지
- 세렌의 시신을 길게 감상하는 애도 연출 금지
- 등록 담당 기능을 냉혈한 악역 관료로 평면화 금지
- ‘사실 임무는 처음부터 취소돼 있었다’류의 반전 금지

## 10. Active State / Props

- 절검 (R03) — 동반 등록, 기능·소유권 미확정
- 소거명부 일부 — 누락·오염 포함
- 출발 인장 — 이름이 사라지는 매체
- 귀환석 — 3갈래 균열, 강제복귀 1회 잔여
- 세렌의 생체인장 — 정지 상태, 봉쇄 해제의 물증
- 회색 종 — 현지 잔존. E024에서는 울리지 않는 배경상태로만 유지
- 리아의 개인 경고 쪽지 (E005) — 장갑 안쪽 보관 상태 유지, 이 회차에서 열지 않음

절검과 소거명부가 E026 이후 재등장할 때 A10이 prop/relic 취급과 소유권 판정을 다시 확인한다.

## 11. State Mutation Plan

E024 종료 시 기록:

- 임무 성공 판정의 발신 주체와 문구 상태
- 등록된 물품 목록과 현지에 남긴 물품 목록
- 절검의 보유 형태 — 증거·부채이며 전리품 아님
- 소거명부 확보분의 누락·오염 정도
- 아이리스와의 관계 종료 조건 — 요구는 수령, 용서는 없음
- 귀환석 잔여 균열·강제복귀 사용 여부
- 좌표 명칭 불일치와 출발 인장의 이름 소실 발생 시각
- L001 세렌 바일 영구 사망 확정 기재

## 12. Ready Verdict

- Authority: RESOLVED
- Domain Readiness: READY
- Storycraft companion: REQUIRED / `docs/10_story_architecture/craft-manifests/E024-storycraft-manifest.md`
- POV: READY — 단일 POV
- Scene Density: Q · 2장면 — 설계 장면 수 2로 일치
- S0: 0
- S1: 2 (§13 참조)

## 13. Open Gaps

정본 근거가 없어 채우지 못했거나 상위 판정이 필요한 항목이다. CP 안에서 새 설정으로 메우지 않았다.

- **S1 — 현지 체류 단위 충돌**: `manuscript/state/E002-state-mutation.md` §4는 예상 체류를 `5시간 17분`으로, `master-chronology-and-aging-ledger-v1.md` §3은 V1 주관경과를 24일(Era N 약 20일)로 규정한다. E024의 귀환표식 개방 지속시간을 어느 단위로 쓸지 정본에 없다.
- **S1 — 세렌 사망 화수**: `permanent-loss-lock-v1.md` L001은 E023–E025, `cast-canon-index-v2.md` C06은 ‘E024 부근’으로 기재한다. `v01-scene-ready-design-v1.md`는 E023 Scene 2–3에서 살해를 명시하므로 본 CP는 E023 사망 / E024 사후처리로 읽었다. 단일 화 확정은 A02 판정 대상이다.
- E024 시점의 정확한 현지 날짜(안개월 몇 일)는 정본에 없다. 도착일 안개월 4일과 V1 주관경과에서 도출한 값만 적었다.
- 등록 용량의 구체 수치·단위(질량·부피·항목 수)가 정본에 없다. ‘모든 증거를 가져갈 용량은 없다’는 서술만 존재한다.
- 세렌 유해의 처리 주체와 절차가 정본에 없다. 소유권만 유족·운동·현지 공동체로 규정돼 있다.
- 귀환 성공 판정을 발신하는 F0 측 직책명이 정본에 없다. 본 CP는 새 이름을 만들지 않고 기능선으로만 두었다.
