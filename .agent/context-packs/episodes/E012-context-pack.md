# Episode Context Pack — E012

Status: D10 READY  
Episode: E012  
Title: 조건부 통행권  
Compiled By: A21 Context Pack Compiler  
Reference: `agent/1b-subact-context-packs`

> 이 CP는 정본이 아니다. 충돌 시 원본 정본과 권한계층을 따른다.

## 1. Authority / Architecture

Required sources:

- [`/AI_PROJECT.md`](../../../AI_PROJECT.md)
- [`docs/00_project/canon-constitution-v1.md`](../../../docs/00_project/canon-constitution-v1.md)
- [`docs/00_project/canon-naming-pack-v1.md`](../../../docs/00_project/canon-naming-pack-v1.md)
- [`docs/00_project/terminology-and-addressing-clarification-v1.md`](../../../docs/00_project/terminology-and-addressing-clarification-v1.md)
- [`docs/00_project/decision-log.md`](../../../docs/00_project/decision-log.md) — DEC-016·017·018·020·021
- [`docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md`](../../../docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md) — E012 행
- [`docs/10_story_architecture/detail/v01-scene-ready-design-v1.md`](../../../docs/10_story_architecture/detail/v01-scene-ready-design-v1.md) — Subact 1B / E012 절
- [`docs/10_story_architecture/detail/v01-d9-correction-overlay.md`](../../../docs/10_story_architecture/detail/v01-d9-correction-overlay.md) — §6
- [`docs/10_story_architecture/subact-causal-matrix-v1.md`](../../../docs/10_story_architecture/subact-causal-matrix-v1.md) — 1B → 1C 전이
- [`docs/10_story_architecture/location-world-crosswalk-v1.md`](../../../docs/10_story_architecture/location-world-crosswalk-v1.md) — V01 1B / 1C
- [`docs/10_story_architecture/scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) — V1 E012 행 (고정)
- [`docs/05_characters/cast-canon-index-v2.md`](../../../docs/05_characters/cast-canon-index-v2.md) — C01 · C03 · C10
- [`docs/05_characters/voice-relationship-state-bible-v1.md`](../../../docs/05_characters/voice-relationship-state-bible-v1.md) — §2 · §2-A C10 · §3 · §5
- [`docs/03_systems/causal-propagation-and-memory-protocol-v1.md`](../../../docs/03_systems/causal-propagation-and-memory-protocol-v1.md) — 살아 있는 현지 앵커 · 귀환 판정
- [`docs/03_systems/mana-fever-gray-calamity-v1.md`](../../../docs/03_systems/mana-fever-gray-calamity-v1.md)
- [`docs/09_collection/major-assets-ledger-v1.md`](../../../docs/09_collection/major-assets-ledger-v1.md) — R01 회색 종
- [`docs/11_mystery/mystery-reinforcement-ladder-v1.md`](../../../docs/11_mystery/mystery-reinforcement-ladder-v1.md) — M01 · M16
- [`docs/12_losses/permanent-loss-lock-v1.md`](../../../docs/12_losses/permanent-loss-lock-v1.md)
- [`.agent/context-packs/episodes/E011-context-pack.md`](E011-context-pack.md)

Episode function:

- Grand Act: GA I — 잘못된 치료
- Volume: V1 — 회색 종이 울리는 날
- Subact: 1B — 격리촌의 통행증 (국소 해결 / 1C 전이)
- Beat: 국소 해결
- Goal: 환자 호송 성공을 근거로 임시 신뢰와 도시 진입권을 얻는다
- Opposition: 관문 최종 검사, 아이리스의 조건과 거부권, 본부의 시한 단축
- Choice: 미래 목적을 숨긴 채 현지 협력을 받아들인다
- Cost: 상호 불신을 안은 동맹, 그리고 숨김이 만든 부채
- State Change: Subact 1B의 ‘신분 없음’ 문제가 해소되고, 문제가 ‘조건부 신분과 짧아진 시한’으로 교체됨
- Hook: 도시 종루의 회색 종은 울리지 않았는데 모든 환자가 동시에 귀를 막는다
- Next Cause: E013에서 아이리스의 신원 보증으로 지방 기록소에 접근해 표적 혐의를 검증하기 시작한다

## 2. E011 Carryover

원본: `E011-context-pack.md` §11 · `v01-scene-ready-design-v1.md` E011

### 에이든

- 사람 → 기록상자 순서로 구조를 수행했고 표적 접촉 가능 시간을 반나절 잃었다
- 미래 장비 일부가 물에 노출돼 은폐 등급이 내려갔다
- 성당 구휼기사단 명부에 외지 치료보조자로 등재된 상태가 유지된다
- 작성일이 어긋난 문서 한 장을 확보했으나 아무에게도 알리지 않았다

### 아이리스

- 에이든의 구조 순서를 직접 보았고 감시를 개시했다
- 장비의 정체를 물었으며 답을 받지 못했다
- 귀환표식 연결·차단에 동의권을 가진다
- 여전히 에이든의 임무 목적을 모른다

### 호송·환자

- 호송은 계속됐고 도시 관문 앞에 도달한다
- 별도 수레 문제와 환자 가족의 요구는 미해결로 남아 있다

### 본부

- 잔여시간 신호에 대한 에이든의 미응답·지연이 기록됐다
- 본부는 현지 상황을 실시간으로 보지 못한다

E012는 E011의 현장 구조를 재연하지 않고, 그 결과를 **문서와 조건으로 환산하는 절차**로 전환한다.

## 3. Time / Location

원본: `master-chronology-and-aging-ledger-v1.md` §1–§3 · `location-world-crosswalk-v1.md` V01 1B→1C

- Era: N
- 기준연도: 건국력(CY) 640
- 에이든: 41세
- Main locations:
  1. 도시 관문 검사대 — 호송의 마지막 검사
  2. 성당 사무소 — 임시 통행권 발급 창구
  3. 사무소 밖 대기 자리 — 아이리스의 거래
  4. 은폐 가능한 구석 — 본부 신호 수신
  5. 관문 안쪽 종루 아래 — 도시 진입 지점
- 이동은 관문 전후 도보 거리이며 장거리 이동시간 문제 없음
- 이 회차에서 처음으로 격리촌 바깥, 도시 안쪽 공간이 열린다

## 4. Access, Anchor, Deadline

원본: `v01-scene-ready-design-v1.md` E012 · `causal-propagation-and-memory-protocol-v1.md` · `v01-d9-correction-overlay.md` §6

### 임시 통행권

- 발급 근거는 에이든의 구조행위와 치료노역이다 — E010·E011에서 실제로 지불한 대가가 문서로 환산된다
- 발급 주체는 성당 사무소이며, 이는 은혜가 아니라 절차의 결과다
- 통행권은 임시이며 조건과 기한을 가진다. 신분의 완전 해결이 아니다
- 발급은 동시에 등록이다. 도시 안에서 그의 위치가 기록되기 시작한다

### 살아 있는 현지 앵커

- 아이리스는 미래 본부가 지정한 안내자가 아니라 도착 뒤 만난 인물이다
- 그의 협력은 안전·신분·귀환 안정조건이며 출발의 절대 조건이 아니다
- 제공: 도시 안내와 현지 신원 보증
- 조건: 에이든이 환자들을 표적 접근 수단으로 쓰면 귀환표식을 끊는다
- 정본 규칙: 살아 있는 현지 앵커가 귀환표식을 거부하면 자동 강제귀환이 불가능하다
- 따라서 이 거래는 호의가 아니라 **상호 거부권의 성립**이다

### 본부 시한 단축

- 목표 접근 지연을 이유로 제거 시한이 앞당겨진다
- 본부의 계산에는 실제 근거가 있으나 현지 상황을 보지 못한다
- 에이든은 시한 단축 사실을 아이리스에게 숨긴다 — 이 숨김이 1C 상호 불신의 출발점이다

### 명칭 규칙

- 성당 사무소·구휼 장면은 `아홉 상처 대성당` 계열로 표기한다
- 도시의 종은 `회색 종`이며 시설은 `종루`다. `솔라 종탑`은 F0 승인기관이므로 이 장면에 등장하지 않는다
- 구휼사는 대사에서 `솔라`를 단독으로 쓰지 않는다 (DEC-017)

## 5. Character State

원본: `cast-canon-index-v2.md` · `voice-relationship-state-bible-v1.md` · `v01-d9-correction-overlay.md` §6

### 에이든 로엔

- 목표: 도시 진입권을 확보하고 표적 조사 경로를 여는 것
- 압박: 방금 얻은 협력자에게 가장 중요한 사실을 숨긴 채 협력을 시작해야 함
- 습관: 목표 → 출구 → 비용. 이 회차에서는 비용 항목 하나를 일부러 비워 둔다
- 오류 가능성: 숨김을 ‘아직 말할 단계가 아님’으로 분류해 부채로 세지 않음
- 금지: 임무 목적 자백, 아이리스를 설득해 임무에 동원, 시한 단축을 협상 카드로 사용

### 아이리스 네르 (C03)

- 목표: 환자와 주민의 안전, 그리고 외지인의 목적 확인
- 수단: 신원 보증과 도시 안내를 제공하되 귀환표식 차단권을 남긴다
- 말투: 상대의 원칙보다 누가 언제 무엇을 잃는지 묻는다. 조건에는 기한과 판정 기준을 붙인다
- 모르는 것: F0/F1의 전체 생존상태, 국가장치의 기술적 연쇄, 본부 시한 단축
- 금지: 로맨스 축 진입, 감화에 의한 무조건 협력, 에이든의 정체를 이 회차에서 간파

### 메이라 솔 (C10) — 아홉 상처 대성당 구휼사

- 통행권 발급 근거를 노역·구조 실적으로 제시한다
- 완전한 거절 대신 조건을 붙여 문장을 이어 간다
- 감당할 수 없는 약속이 먼저 튀어나온 뒤 스스로 수를 다시 세는 습관이 압박 장면에서 드러난다
- 금지: 마나열병 여부 확정 진단, 설교로 장면 채우기, 대사에서 `솔라` 단독 사용

### 관문 검사관

- 책임소재를 피하려 하며 뇌물이 아니라 근거 문서를 요구한다
- 기능인물이며 새 핵심 인물 이름을 즉석 확정하지 않는다

### 환자들

- 도시 진입은 그들에게 생존 조건이지 주인공의 배경이 아니다
- 마지막 장면의 동시 반응은 연출이 아니라 그들 자신에게 일어난 사건이다

### 본부 (신호로만 등장)

- 시한 단축 통보는 짧고 계산에 근거한다
- 금지: 악역 목소리 연출, 통신 낭독으로 장면 채우기

## 6. Mystery / Information Ceiling

원본: `mystery-reinforcement-ladder-v1.md` M01 · M16 · `major-assets-ledger-v1.md` R01

Active mysteries:

- M16 회색 종은 무엇을 감지하는가 — 종이 울리지 않았는데 반응이 발생한다
- M01 마나열병은 전염병인가 — 환자 집단이 동시에 같은 것에 반응한다
- M02 세렌 바일은 왜 창시자로 기록됐는가 — 도시 진입으로 검증 경로가 열린다

Reader may know:

- 구조행위와 치료노역이 실제 문서상 자격으로 환산된다
- 현지 협력은 신뢰가 아니라 조건과 거부권으로 성립한다
- 귀환표식은 현지인의 동의에 걸려 있다
- 본부의 시한이 짧아졌고 에이든이 그것을 숨겼다
- 환자들이 소리 없이 무언가에 동시 반응한다

Reader must not know yet:

- 회색 종의 감지 대상 (독자 추론 가능 시점 E092)
- 마나열병이 장치·주소 문제라는 정답 (독자 추론 가능 시점 E176)
- 세렌이 지방 소거를 늦췄다는 전체 기능
- 누가 어떤 이유로 책임을 뒤집었는지
- 삭제된 증언자의 정체
- 19만 계산의 최종 오류구조
- E011 문서의 작성자와 기록상자의 전체 내용

Final hook:

- 도시 종루의 회색 종은 울리지 않았는데 모든 환자가 동시에 귀를 막는다
- 의미: 반응의 원인이 소리가 아니며, 환자들은 에이든이 듣지 못하는 것을 함께 겪는다
- 금지: 종의 기능 설명, 마나열병 정답 제시, 에이든이나 아이리스가 원인을 추정해 확정, 종을 울려 장면을 마감

## 7. POV / Storycraft

원본: `scene-density-map-v1.md` V1 E012 행 (고정) · `secondary-pov-and-offscreen-action-allocation-v1.md` §4–§6

- POV: 에이든 단일 근접 3인칭 (E012에는 P1·P2 배치 없음. P2 다중 POV는 E025부터)
- **Scene Density: X형 5장면** (밀도표 X형 5~6장면 범위, 본 설계는 5장면)
- 배정 사유: 통행권 발급, 아이리스의 귀환표식 조건, 본부의 시한 단축이 겹치며 도시 진입권과 상호 불신이 동시에 성립하는 서브액트 전환점이다
- X형 규칙: 여러 권한 영역·세력이 같은 회차에서 병렬로 움직이는 교차 회차. 한 장소 3단 진행으로 축약하지 않는다
- Primary craft: 상호 거부권 협상
- Secondary A: 실적의 문서 환산
- Secondary B: 말하지 않은 것으로 만드는 부채
- Secondary C: 침묵으로 만드는 훅
- Hook: H2 정보 역전 + H4 제도변화
- Reader reward: 신분 문제의 해소와 동시에 더 나쁜 조건이 채워지는 서브액트 전환의 체감

## 8. Scene Values

밀도표 X형 5~6장면 범위 중 **5장면**으로 설계한다.

### Scene 1 — 관문 검사대

- Entry: 호송이 끝났으니 도시는 열린다
- Evidence: 마지막 검사는 사람 수가 아니라 근거 문서를 요구하고, 에이든의 서류는 여전히 이 왕조의 것이 아니다
- Exit: 성공한 호송이 자동으로 진입권이 되지 않음이 확정

### Scene 2 — 성당 사무소

- Entry: 자격이 없으면 남는 길은 우회나 잠입뿐이다
- Evidence: 구조행위와 치료노역이 실적으로 계상되고 임시 통행권이 발급된다
- Exit: 신분 문제 해소. 그러나 통행권은 조건·기한과 함께 그를 도시 기록에 올린다

### Scene 3 — 아이리스의 거래

- Entry: 문서를 얻었으니 현지인은 더 필요하지 않다
- Evidence: 도시 안내와 신원 보증의 실제 가치, 그리고 귀환표식 차단권이 아이리스에게 있다는 사실
- Choice: 에이든은 조건을 받아들인다 — 환자들을 표적 접근 수단으로 쓰면 귀환표식이 끊긴다
- Exit: 협력이 신뢰가 아니라 상호 거부권으로 성립

### Scene 4 — 본부 신호

- Entry: 조건을 지키면서도 임무 일정은 유지할 수 있다
- Evidence: 접근 지연을 이유로 제거 시한이 앞당겨진다
- Choice: 에이든은 시한 단축을 아이리스에게 숨긴다
- Exit: 방금 맺은 조건이 그가 지킬 수 없는 것이 됨

### Scene 5 — 종루 아래

- Entry: 도시에 들어왔고 오늘의 일은 끝났다
- Evidence: 종은 울리지 않았는데 환자들이 동시에 귀를 막는다
- Exit/Hook: 에이든이 얻은 진입권 안쪽에서, 그가 듣지 못하는 사건이 이미 진행 중임이 드러남

## 9. Anti-Repeat

- E002의 여섯 기관 순회를 관문·사무소·창구 순회로 바꿔 재현하지 않는다. 발급 절차는 한 장면으로 끝낸다
- E010의 명부 등재 비용 구조를 반복하지 않는다. 이번 비용은 등록이 아니라 **숨김**이다
- E011의 현장 구조를 회상이나 재연으로 다시 보여 주지 않는다. 실적은 문서 위의 항목으로만 나타난다
- E007처럼 회색 종이 울려서 훅을 만들지 않는다. 이번 훅은 종이 울리지 **않는** 데서 온다
- E001의 삭제된 글자, E003의 두 문서 대조를 훅 형식으로 재사용하지 않는다
- 아이리스가 에이든의 정체나 임무를 간파해 폭로하지 않는다
- 본부 시한 단축을 통신 대사 낭독만으로 처리하지 않는다
- 통행권 획득을 승리 장면으로 연출하지 않는다. 획득과 손실이 같은 회차에서 성립한다

## 10. Active State / Props

- 임시 통행권 — 신규 확보. 조건·기한 포함
- 아이리스의 신원 보증 — 조건부이며 철회 가능
- 귀환표식 — 아이리스의 동의로 안정화되되 차단권이 그에게 남는다
- 본부 시한 단축 통보 — 에이든만 아는 정보
- 기록상자와 작성일 모순 문서 — E011에서 이월, 미공개 유지
- 성당 구휼기사단 명부 등재 — 배경상태로 유지
- 도시 종루의 회색 종 — 현지 잔존 자산(R01). 이 회차에서 울리지 않는다
- 미래 장비 — 은폐 등급 하락 상태로 이월

통행권과 신원 보증이 1C에서 반복 사용되므로 A10이 상태자산 등록 여부를 판정한다.

## 11. State Mutation Plan

E012 종료 시 기록:

- 임시 통행권의 조건·기한·발급 근거
- 아이리스 신원 보증의 범위와 철회 조건
- 귀환표식 안정화 등급과 차단권 보유자
- 단축된 제거 시한의 새 값과 그것을 아는 사람 목록
- 에이든이 숨긴 정보 항목 (1C 불신 부채로 이월)
- 도시 진입 사실과 접근 가능해진 기관·구역
- 종루 미반응 상태에서 발생한 환자 동시반응의 관측 기록
- Subact 1B 종료 판정과 1C 진입 조건

## 12. Ready Verdict

- Authority: RESOLVED
- Domain Readiness: READY
- Storycraft companion: REQUIRED / prepared separately
- POV: READY
- Scene density conformance: X형 5~6장면 → 설계 5장면 · PASS
- Subact transition: 1B 종료 / 1C 진입조건 성립
- S0: 0
- S1: 0

E012 Storycraft Manifest와 E011 상태기록 확인 뒤 A18 호출 가능.
