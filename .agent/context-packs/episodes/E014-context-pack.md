# Episode Context Pack — E014

Status: D10 READY  
Episode: E014  
Title: 약품으로 산 열람시간  
Compiled By: A21 Context Pack Compiler  
Reference: `agent/1c-evidence-subact`

> 이 CP는 정본이 아니다. 충돌 시 원본 정본과 권한계층을 따른다. 각 항목의 근거 경로는 절마다 명시한다.

## 1. Authority / Architecture

Required sources:

- [`/AI_PROJECT.md`](../../../AI_PROJECT.md)
- [`docs/00_project/canon-constitution-v1.md`](../../../docs/00_project/canon-constitution-v1.md)
- [`docs/00_project/canon-naming-pack-v1.md`](../../../docs/00_project/canon-naming-pack-v1.md)
- [`docs/00_project/terminology-and-addressing-clarification-v1.md`](../../../docs/00_project/terminology-and-addressing-clarification-v1.md)
- [`docs/00_project/decision-log.md`](../../../docs/00_project/decision-log.md) — DEC-016·017·018·020·021
- [`docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md`](../../../docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md) — E014 행
- [`docs/10_story_architecture/detail/v01-scene-ready-design-v1.md`](../../../docs/10_story_architecture/detail/v01-scene-ready-design-v1.md) — E014 절
- [`docs/10_story_architecture/subact-causal-matrix-v1.md`](../../../docs/10_story_architecture/subact-causal-matrix-v1.md) — 1C 행
- [`docs/10_story_architecture/location-world-crosswalk-v1.md`](../../../docs/10_story_architecture/location-world-crosswalk-v1.md) — V01 1C
- [`docs/10_story_architecture/scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) — E014 행 (밀도 **고정**)
- [`.agent/context-packs/episodes/E013-context-pack.md`](E013-context-pack.md)
- [`docs/11_mystery/mystery-reinforcement-ladder-v1.md`](../../../docs/11_mystery/mystery-reinforcement-ladder-v1.md) — M02 사다리 E014 단

Episode function (registry E014 · v01 E014 · matrix 1C):

- Grand Act: GA I — 잘못된 치료
- Volume: V1 — 회색 종이 울리는 날
- Subact: 1C — 표적의 범죄 증거 확보
- Beat: 첫 장벽
- Goal: 공식 기록 원본에 접근하려면 지방 서기와 거래해야 한다
- Opposition: 문서 공개 시 지방 서기가 왕실 책임을 뒤집어쓸 위험, 뇌물을 받을 수 없는 감사 구조, 줄어드는 귀환용 자원
- Choice: 귀환용 응급자원 일부를 뇌물 대신 격리촌 환자 약품과 기록 사본 보호로 내준다
- Cost: 귀환 후 신체 안정에 쓸 약품이 줄어든다
- State Change: 임무의 비용이 ‘시간’에서 ‘에이든 자신의 귀환 안전’으로 바뀐다
- Hook: 보고서 원본 작성자의 서명이 이미 죽은 기록관의 이름이다

## 2. E013 Carryover

근거: [`E013-context-pack.md`](E013-context-pack.md), v01 E013.

### 확정된 것

- 왕실 피해보고서의 폐허 목록과 현지 세금대장의 납부 기록이 한 마을에서 어긋난다
- 왕실 지도의 갱신이 표시층에만 일어났다
- 주민은 그 마을을 알지만 길 방향을 서로 다르게 가리킨다
- 그 마을의 마지막 세금이 내일 날짜로 납부돼 있다

### 소모된 것

- 아이리스의 신원 보증 — 문턱을 여는 데 이미 썼다
- 기록소의 서기 교대 전 열람시간
- 사본 열람만으로 확인 가능한 범위는 E013에서 끝났다

### 유지되는 압박

- 본부가 앞당긴 제거 시한. 에이든은 이 사실을 아이리스에게 숨기고 있다
- 성당 구휼기사단 명부의 외지 치료보조자 등록 — 추적 가능
- 격리촌 환자들은 여전히 약품이 부족하다 (1B 잔여상태)
- 강제복귀 사실상 1회, 오착 약 18km ([`master-chronology-and-aging-ledger-v1.md`](../../../docs/01_timeline/master-chronology-and-aging-ledger-v1.md) §4 J01)

E014는 E013의 문서 대조를 반복하지 않는다. E013은 사본을 읽었고 E014는 **원본을 만진다.**

## 3. Time / Location

근거: master chronology §1·§4, crosswalk V01 1C.

- Era: N0 / CY 640 안개월, E013 직후
- 에이든: 41세 / 주관적 누적일 V1 24일 구간 내부
- 권역: 잿빛 변경
- Main locations:
  1. 기록소 협상실
  2. 격리촌 약품 인계지점
  3. 원본 열람실 (봉인 관리 구역)
  4. 사본대
- 도시 안팎 왕복 이동이 한 번 발생하므로 E013보다 실제 소요시간이 길다
- 이 회차에서 귀환창 자체는 단축되지 않는다. 줄어드는 것은 **물자**다

## 4. Transaction Package

근거: v01 E014, [`political-economy-record-law-v1.md`](../../../docs/08_institutions/political-economy-record-law-v1.md), [`economy-prices-professions-v1.md`](../../../docs/08_institutions/economy-prices-professions-v1.md), R05 서부 잿빛 변경.

거래는 매수가 아니라 **위험 재배치**다. 네 항목이 오간다.

### 서기가 잃을 위험

- 원본을 공개하면 왕실 책임 소재가 지방으로 내려올 수 있다
- 뇌물은 감사 대상이라 오히려 증거가 된다
- 가족이 지역에 남아 있어 압박받는다 (C12 dossier 한계)

### 에이든이 내놓는 것

- 귀환용 응급자원 일부 — 격리촌 환자 치료용 약품으로 전환
- 기록 사본 보호 — 원본이 회수돼도 지방에 사본이 남게 하는 조치
- 두 항목 모두 서기의 책임을 줄이지 않고 **주민 쪽 이득을 늘린다**

### 에이든이 얻는 것

- 원본 열람시간
- 사본 제작 허용 범위

### 실제로 깎이는 것

- 귀환 후 신체 안정에 쓸 약품 (v01 Cost)
- 이 감소는 새 영구손실이 아니며 [`permanent-loss-lock-v1.md`](../../../docs/12_losses/permanent-loss-lock-v1.md)의 L001–L016을 변경하지 않는다. V1 State Ledger 항목으로만 기록한다

## 5. Character State

근거: cast-canon-index-v2 C03·C06·C12, cast-encyclopedia-v1 C03·C06·C12, supporting-cast-dossiers-c11-c20-v2 C12, voice-relationship-state-bible-v1 §2·§3·§5.

### 에이든 로엔

- 목표: 원본을 직접 보고 혐의의 근거를 확정
- 어법: 목표 → 출구 → 비용 순서. 큰 숫자보다 입력과 제외대상을 확인
- 이 회차의 성장 표식: 처음으로 **자기 몸의 여유**를 대가로 내놓는다
- 오류 가능성: 자원을 내주었으니 원본이 답을 줄 것이라 기대함
- 금지: 영웅적 자기희생 연출, 약품을 건네며 미래를 암시하는 대사

### 아이리스 네르

- 협상 어법: 상대의 원칙보다 누가 언제 무엇을 잃는지 묻는다
- 이 회차의 변화: 에이든의 목적은 여전히 믿지 않지만, 그가 사람을 비용표로만 보지 않는다는 점은 인정한다 (v01 Character Change)
- 독립 판단: 약품이 실제로 환자에게 갔는지 자기 눈으로 확인한다
- 아이리스가 모르는 것: F0/F1의 전체 생존상태, 국가장치의 기술적 연쇄 (voice bible §5)
- 금지: 감동해서 협력 전면 전환, 로맨스 신호

### 지방 기록소 실무자 / 서기

- 정본 후보는 C12 엘사 네르. 이름 확정은 A13 판정 사항 — §12 gaps
- Want: 주민과 원본 기록을 함께 지킴 / Lie: 원본만 숨기면 언젠가 모든 권리를 복구할 수 있다
- Fear: 자기 선택으로 마을이 역사에서 완전히 사라짐
- 독립 행동: 중앙 수색 전에 장부 일부를 주민별로 분산한다. 그 과정에서 누가 무엇을 보관하는지 새 권력관계가 생긴다
- 금지: 고문·압박 한 번에 자료 전부 제공, 만능 기록관

### 세렌 바일

- 직접 등장하지 않는다
- 원본 보고서에 기술된 혐의 — 금지의식 관련 — 는 이 회차에서 무효화하지 않는다

## 6. Mystery / Information Ceiling

근거: mystery-reinforcement-ladder-v1 M02·M05·M12·M15, v01 E014.

Active mysteries:

- **M02 세렌 바일은 왜 창시자로 기록됐는가 — 사다리 E014 단: ‘왕실 보고서와 금지의식’.** 이 회차가 그 단을 실제로 놓는다
- M05 빈 세금장부 — 배경. 첫 단은 E036이므로 해석 선취 금지
- M12 최종 흑막 — 개인 흑막 지목 금지
- M03 리아는 왜 F0를 기억하는가 — 언급 금지. 리아는 이 회차에 없다

Reader may know:

- 왕실 보고서 원본이 존재하고 세렌의 금지의식 혐의를 기술한다
- 그 보고서가 사건 발생 **전** 날짜로 작성됐다
- 피해 수치가 나중에 덧씌워졌다
- 원본 작성자 서명란에 이미 죽은 기록관의 이름이 있다

Reader must not know yet:

- 누가 작성일을 앞당겼고 왜 그랬는가 (M02 사다리 E061까지 유예)
- 죽은 기록관이 누구이며 E003의 삭제된 증언자와 같은 사람인지
- 세렌이 지방 소거를 늦췄다는 전체 기능
- 19만 모델의 최종 오류구조
- 조작 주체가 왕실·성당·본부 중 어디인지

Final hook:

- 원본 작성자의 서명이 **이미 죽은 기록관의 이름**이다
- 의미: 작성일 역전이 필사 실수가 아니라 서명 주체 자체의 문제로 확대된다
- 금지: 이 이름을 E003의 삭제된 증언자와 동일인으로 확정, 세렌 무죄 확정, 죽은 자의 유령·잔향으로 설명

## 7. POV / Storycraft

근거: canon-constitution OPERATIONAL LOCKS, secondary-POV 배치표 §4 (E014 배정 없음), scene-density-map E014 행.

- POV: 에이든 단일 근접 3인칭
- Scene Density: **E형 4장면 (고정)** — 배정 사유: 지방 서기 협상, 약품 인계, 보고서 원본 발견에 더해 귀환용 응급자원 감소라는 비용이 실제로 계산되기 때문
- Primary craft: 대가가 먼저 지급되는 거래
- Secondary A: 제도적 겁 — 반대자가 악의가 아니라 책임소재 때문에 막는다
- Secondary B: 종이의 물리층 — 잉크·눌린 자국·서명란
- Secondary C: 회계로 표현하는 자기희생
- Hook: H2 정보 역전
- Reader reward: 임무 비용이 처음으로 에이든 자신의 몸에 청구되는 것을 숫자로 확인

## 8. Scene Values

### Scene 1 — 기록소 협상실

- Entry: 사본으로 안 되면 값을 치르고 원본을 본다
- Evidence: 서기가 거부하는 이유는 탐욕이 아니라 왕실 책임 전가 위험과 감사 구조
- Exit: 뇌물 경로가 완전히 막히고, 서기가 실제로 두려워하는 것이 드러난다

### Scene 2 — 격리촌 약품 인계

- Entry: 값은 물자로 치른다
- Evidence: 귀환용 응급자원이 현지 치료로 실제 전환되고 아이리스가 인계 현장을 본다
- Exit: 거래가 성립하지만 에이든의 귀환 후 여유가 줄어든다

### Scene 3 — 원본 열람실

- Entry: 원본은 사본이 감춘 것을 보여 준다
- Evidence: 보고서 작성일이 사건 발생일보다 앞서고, 피해 수치가 나중 잉크로 덧씌워졌다
- Exit: 혐의 자체는 남지만 공식 인과의 순서가 무너진다

### Scene 4 — 사본대

- Entry: 약속대로 사본을 남기고 정산한다
- Evidence: 남은 응급자원 재계산 결과와, 사본을 뜨는 과정에서 확인되는 서명란의 이름
- Exit: 임무 비용이 에이든의 몸으로 옮겨온 채로, 서명 주체가 죽은 사람이라는 사실이 남는다

## 9. Anti-Repeat

- E003처럼 압수품을 늘어놓고 증거 항목을 순회하지 않는다 — E014는 문서 **한 건**을 깊게 판다
- E003의 사망일 대조표 방식으로 날짜 역전을 보여주지 않는다. E014는 **잉크층과 눌린 자국**이라는 물리 증거로 보여준다
- E002·E004처럼 서명·승인 절차의 지연으로 긴장을 만들지 않는다 — 여기서 지연을 푸는 것은 물자다
- E011의 ‘사람이냐 임무냐’ 극적 구조 선택 반복 금지. E014의 희생은 극적 장면이 아니라 **회계상 감산**이다
- 뇌물 거절 → 감동 → 전면 협력 전개 금지
- 아이리스가 이 거래로 에이든을 신뢰하게 되는 전개 금지 — 인정하는 것은 한 항목뿐이다
- E001의 삭제된 글자 훅, E013의 미래 날짜 훅을 같은 형태로 반복하지 않는다. E014의 이상은 **사람의 이름**에 있다

## 10. Active State / Props

- 왕실 피해보고서 **원본** — 작성일·덧씌운 수치·서명란
- 귀환용 응급자원 (약품) — 잔량이 이 회차에서 확정됨
- 지방 기록 사본 — 보호 조치 대상, 이후 회차에서 회수 위험 발생 가능
- 서기가 주민별로 분산한 장부 조각 — 배경 상태
- E013의 ‘내일 날짜 납세’ 항목 — 유지, 이 회차에서 해명하지 않음
- E011 기록상자의 미래 날짜 문서 — 봉인 유지

약품 잔량과 사본 보호 조치가 E015 이후 임무 판단에 다시 쓰일 경우 A10이 상태·prop 등급을 판정한다.

## 11. State Mutation Plan

E014 종료 시 기록:

- 귀환용 응급자원 잔량과 귀환 후 신체 안정 여유의 감소폭
- 원본 보고서의 작성일·덧씌운 수치·서명자 이름의 검증 상태
- 세렌 금지의식 혐의의 현재 성립 여부 (성립 유지)
- 사본 보호 조치의 범위와 보관 주체
- 아이리스의 인정 항목 — ‘사람을 비용표로만 보지 않는다’ 한 건
- 본부 시한 단축 은폐 지속 여부
- 기록소 실무자가 부담하게 된 위험

## 12. Ready Verdict

- Authority: RESOLVED
- Domain Readiness: READY WITH GAPS
- Storycraft companion: REQUIRED / [`E014-storycraft-manifest.md`](../../../docs/10_story_architecture/craft-manifests/E014-storycraft-manifest.md)
- POV: READY (보조 POV 배정 없음)
- S0: 0
- S1: 3

S1 gaps:

1. v01 E014의 `지방 서기`와 C12 엘사 네르의 동일인 여부가 정본에 없다 (E013 gaps와 동일 항목)
2. `귀환용 응급자원`의 정본 품목 구성과 수량 단위가 어느 문서에도 없다. v01은 `귀환 후 신체 안정에 쓸 약품 감소`만 규정한다. 원고에서 구체 수치를 쓰려면 A16 확인 필요
3. 서명란의 `이미 죽은 기록관`의 이름·직위·사망시점이 정본에 없다. C12 계열 서임명(`네르`)인지, 대기록소 계열(`세른`)인지에 따라 M02 사다리 E061의 회수 방식이 달라진다. 새 인물 생성이므로 A02·A11 승인 필요

E014 Storycraft Manifest 확인 및 gaps 3건 판정 뒤 A18 호출 가능.
