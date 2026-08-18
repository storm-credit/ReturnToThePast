# Episode Context Pack — E008

Status: D10 READY  
Episode: E008  
Title: 이름 없는 검문  
Compiled By: A21 Context Pack Compiler  
Reference: Subact 1B · Era N 신분·현지 앵커 확보

> 이 CP는 정본이 아니다. 충돌 시 원본 정본과 권한계층을 따른다.

## 1. Authority / Architecture

Required sources:

- [`/AI_PROJECT.md`](../../../AI_PROJECT.md)
- [`docs/00_project/canon-constitution-v1.md`](../../../docs/00_project/canon-constitution-v1.md)
- [`docs/00_project/canon-naming-pack-v1.md`](../../../docs/00_project/canon-naming-pack-v1.md)
- [`docs/00_project/terminology-and-addressing-clarification-v1.md`](../../../docs/00_project/terminology-and-addressing-clarification-v1.md)
- [`docs/00_project/decision-log.md`](../../../docs/00_project/decision-log.md) — DEC-016·017·018·020·021
- [`docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md`](../../../docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md) E008 행
- [`docs/10_story_architecture/detail/v01-scene-ready-design-v1.md`](../../../docs/10_story_architecture/detail/v01-scene-ready-design-v1.md) E008 절
- [`docs/10_story_architecture/detail/v01-d9-correction-overlay.md`](../../../docs/10_story_architecture/detail/v01-d9-correction-overlay.md) §6
- [`docs/10_story_architecture/subact-causal-matrix-v1.md`](../../../docs/10_story_architecture/subact-causal-matrix-v1.md) 1B
- [`docs/10_story_architecture/scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) E008 `E · 4장면 고정`
- [`docs/10_story_architecture/secondary-pov-and-offscreen-action-allocation-v1.md`](../../../docs/10_story_architecture/secondary-pov-and-offscreen-action-allocation-v1.md) §6 E008
- [`docs/11_mystery/mystery-reinforcement-ladder-v1.md`](../../../docs/11_mystery/mystery-reinforcement-ladder-v1.md) M01
- [`.agent/context-packs/episodes/E007-context-pack.md`](E007-context-pack.md)

Episode function (registry E008 행 + 1B dossier):

- Grand Act: GA I — 잘못된 치료
- Volume: V1 — 회색 종이 울리는 날
- Subact: 1B — 격리촌의 통행증
- Beat: 첫 장벽
- Goal: 격리촌 검문과 언어·화폐 차이를 통과해야 한다
- Opposition: 존재하지 않는 왕조 형식의 문서, 책임소재를 피하려는 검문관, 부러진 수레 축, 그를 관찰하는 현지인
- Choice: 환자 호송을 돕는 조건으로 임시 통행권을 얻는다
- Cost: 임무 시간과 이동 자유를 호송 일정에 묶고, 얼굴·발음·손기술이 검문 기록에 남는다
- State Change: ‘숨어서 통과하는 외지인’이 ‘조건을 지고 등록된 노동자’가 됨
- Hook: 한 아이가 존재하지 않는 가족의 이름과 집 위치를 정확히 말하고, 처음 본 에이든에게 ‘두 번째로 늦게 왔다’고 한다

## 2. E007 Carryover

Source: E007 CP §11, v01 scene-ready E007

### 에이든

- 오착지에서 회복, 미래 장비는 은폐 상태이나 완전하지 않다
- 냉각으로 귀환용 마력 일부 소모
- 행렬 내 임시 역할은 운반인 — 무보수·무등록
- 회색 종의 반응을 한 번 관측했고 원인은 모른다
- 계급 호칭과 증거문법 오류로 이미 ‘기억되는 외지인’이다

### 아이리스 네르

- 종과 귀환석의 공명을 보고 독자적으로 추적 중
- 호송 경로·순번에 현지 거부권을 행사할 수 있다 — 에이든이 마주하는 경로는 그가 바꾼 결과다
- 에이든의 임무 목적은 모른다
- 그를 왕실 첩자·기록밀수자·질병원 중 하나로 의심한다

### 행렬

- 목적지는 격리촌 관문이며 환자와 가족이 함께 이동한다
- 수레·약품·식수는 부족하고 순번은 무게로 정해진다

### 본부

- 단방향 잔여시한 신호만 도달
- 현지 상황을 실시간으로 확인하지 못한다

## 3. Time / Location

Source: master-chronology §4 J01, v01 scene-ready E008

- Date: 건국력 640년 안개월 4일 늦은 시각부터 이튿날 구간 (E007 직후 연속)
- Era: N0
- 에이든: 41세 / 주관적 누적 1~2일
- Main locations:
  1. 격리촌 관문 검문선
  2. 관문 앞 대기 구역의 파손 수레
  3. 임시 대기막 — 아이의 발작
  4. 관문 바깥 순번 재배치 지점
- 이동 없음. 한 장소의 네 구역에서 시간이 흐르며 대기열이 실제 비용이 된다
- 회차 안에서 도시 진입은 일어나지 않는다. 그것은 E012다

## 4. 검문·통행 제도 패키지

Sources:

- [`docs/08_institutions/economy-prices-professions-v1.md`](../../../docs/08_institutions/economy-prices-professions-v1.md) §1·§3·관문 통행세
- [`docs/08_institutions/political-economy-record-law-v1.md`](../../../docs/08_institutions/political-economy-record-law-v1.md)
- [`docs/02_world/daily-life-language-era-contrast-v1.md`](../../../docs/02_world/daily-life-language-era-contrast-v1.md) Era N
- [`docs/02_world/religion-ritual-clergy-encyclopedia-v2.md`](../../../docs/02_world/religion-ritual-clergy-encyclopedia-v2.md) §8

### 검문이 확인하는 것

- 통행증
- 가족관계 — 누구의 가구에 속한 사람인가
- 세금표 — 어느 장부에 부담이 기록됐는가

세 가지는 신원 확인이 아니라 **책임 귀속 확인**이다. 문제가 생겼을 때 누구 장부로 넘길지가 검문의 실제 기능이다.

### 에이든 문서의 실패 방식

- 위조가 조잡해서가 아니라 형식 자체가 이 왕조에 존재하지 않는다
- 검문관은 위조범으로 단정하지 않고 ‘처리 불가’로 분류한다
- 처리 불가는 체포보다 위험하다. 아무 장부에도 올라가지 않으면 어떤 권리도 발생하지 않는다

### 통과 경로

- 뇌물은 성립하지 않는다 — 검문관이 피하려는 것은 손해가 아니라 책임이다
- 성립하는 것은 **책임을 대신 지는 노동** — 임시 노역표와 호송 조건
- 노역표는 신분이 아니라 기한부 등록이며, 등록되는 순간 추적도 가능해진다
- 미래 도구를 쓰지 않고 현지 재료만으로 수레를 수리해야 한다

### 화폐

- 철편·은각·금관, 장부이체는 기록주소에 묶인다
- 무등록자는 임금이 낮고 사고보상·주소증언을 받기 어렵다

## 5. Character State

Sources: cast-canon-index-v2 C01·C03·C10·C26, voice-relationship-state-bible-v1 §2·§2-A, v01-d9-correction-overlay §6

### 에이든 로엔

- 목표: 관문을 통과하고 표적 접근 경로를 유지한다
- 전문: 구조·수리·현장 판단. 도구 없이도 파손 원인을 읽는다
- 압박: 호송 조건을 받으면 임무 시간이 줄고, 거절하면 등록 자체가 불가능하다
- 오류 가능성: 아이의 발작을 감염 신호로 먼저 해석한다
- 금지: 미래 도구 사용, 무력 돌파, 정체 노출

### 검문관

- 부패한 악역이 아니다. 상급 보고와 책임 귀속을 피하려는 실무자다
- 행렬 전체를 돌려보내는 것이 그에게는 가장 안전한 선택이다
- 조건을 붙여 책임을 옮길 수 있을 때만 통과를 허가한다
- 새 핵심 이름을 즉석 확정하지 않는다

### 아이리스 네르

- 대사와 이름이 이 회차에서 처음 확정될 수 있다
- 관찰 대상은 에이든의 수리기술과 발음
- 그는 도움에 감사하지 않고 능력의 출처를 의심한다
- 협력 제안은 하지 않는다. 조건을 걸 준비만 한다
- 금지: 안내자화, 에이든 임무 목적 인지

### 발작한 아이

- 마나열병 환자 증인 C26 아벨 네르로 도출된다 — cast-canon-index-v2 C26이 V1 첫 핵심권의 유일한 환자 증인이다. 최종 확정은 A08 판정 대상
- 예언자가 아니다. 정확한 이름과 위치를 말할 뿐 의미를 모른다
- 가족은 아이를 부정하지도 신비화하지도 않는다
- 같은 가족 안에서 유사 증상이 함께 나타난다 — M01 E008 단계

### 메이라 솔 (P3 제한 관찰자)

- 아홉 상처 대성당 구휼사. 현장구휼사 계열
- 이름 → 오늘 날짜 → 여기가 어디인지를 순서대로 묻는다
- 병명을 확정하지 않는다 — ‘아직 구분되지 않은 사람’
- 격리와 재심을 같은 호흡으로 말한다
- 달력기관은 대사에서 반드시 `종탑`으로 부른다. `솔라` 단독 사용 금지
- 분량 1,200자 이내, 마나열병 정답 설명 금지

## 6. Mystery / Information Ceiling

Source: mystery-reinforcement-ladder-v1 M01·M16·M02

Active mysteries:

- M01 마나열병은 전염병인가 — E008은 사다리의 첫 계단 `같은 가족 집단발병`
- M16 회색 종은 무엇을 감지하는가 — 종은 이 회차에서 울리지 않는다. 부재로 유지
- M02 세렌 바일은 왜 창시자로 기록됐는가 — 접근 지연으로만 유지

Reader may know:

- 발병이 가족·가구 단위로 묶여 나타난다
- 아이가 존재하지 않는 가족과 집을 정확히 말한다
- 검문 제도가 사람을 확인하는 것이 아니라 책임을 배정한다
- 현지인 한 명이 에이든의 기술을 의심하며 지켜본다

Reader must not know yet:

- 마나열병이 감염이 아니라는 정답 (M01 추론 가능 시점 E176)
- 아이의 두 번째 기록의 존재 — 그것은 E009다
- 세렌의 전체 기능·조작 주체
- 삭제된 증언자의 정체
- 19만 모델의 최종 오류구조
- 아이리스가 협력자가 된다는 사실

Final hook:

- 아이가 처음 보는 에이든에게 ‘두 번째로 늦게 왔다’고 말한다
- 의미: 아이의 기억이 이 시간선의 순서와 다른 순서를 세고 있다
- 금지: 아이를 예언자로 처리, 시간여행 인지 확정, 전염 정답 확정

## 7. POV / Storycraft

- POV: 에이든 단일 근접 3인칭 + P3 제한 관찰자 1회 (메이라 솔)
- P3 삽입은 Scene 3 말미의 짧은 관찰창이며 독립 장면으로 세지 않는다. 총 장면 수는 4로 유지한다
- Scene Density: E형 4장면 — scene-density-map-v1 E008 `E · 4장면 고정`
- 4번째 장면은 밀도 규칙에 따라 반대편의 능동행동이다 — 아이리스의 순번 재배치
- Primary craft: 책임 귀속 협상
- Secondary A: 기술로 증명하고 신분으로 실패하기
- Secondary B: 증상과 기록이 함께 어긋나는 첫 관측
- Hook: H2 정보 역전
- Reader reward: 판타지 관문 장면을 무력·뇌물이 아니라 제도의 논리로 통과하는 쾌감

## 8. Scene Values

### Scene 1 — 검문선

- Entry: 행렬에 섞여 있으면 통과할 수 있다
- Opposition: 통행증·가족관계·세금표 삼중 확인, 형식이 없는 문서
- Exit: 숨는 것으로는 통과 불가. 어떤 장부에든 올라가야 한다는 조건으로 바뀜

### Scene 2 — 파손 수레

- Entry: 문서를 대신할 것은 없다
- Opposition: 부러진 축, 돌려보내려는 검문관, 미래 도구 사용 금지
- Exit: 현지 재료 수리로 임시 노역표를 얻지만 호송 조건이 붙는다

### Scene 3 — 아이의 발작

- Entry: 등록을 얻었으니 남은 문제는 시간이다
- Opposition: 아이가 존재하지 않는 가족과 집을 정확히 부르고, 같은 가구에서 유사 증상이 함께 나타난다
- P3 관찰창: 메이라 솔이 감염병과 구분되지 않는 상태를 실무로 처리한다
- Exit: 에이든의 미래 지식이 첫 오답 방향으로 정렬된다

### Scene 4 — 순번 재배치

- Entry: 조건을 지불했으니 행렬 안에서의 위치는 안정적이다
- Opposition: 아이리스가 그의 순번과 호송 위치를 바꾼다. 이유를 설명하지 않는다
- Exit: 그는 통행을 얻는 대신 관찰 아래 놓인다. 비용이 등록과 감시의 형태로 확정된다

## 9. Anti-Repeat

- E007의 은폐 장면을 반복하지 않는다. E008의 문제는 숨기기가 아니라 등록이다
- E002의 여섯 기관 순회식 절차 나열 금지 — 검문은 한 창구에서 세 항목으로만 진행된다
- E003의 문서 대조 구조 금지 — 여기서 대조되는 것은 문서가 아니라 책임이다
- 뇌물·협박·무력 돌파로 관문을 여는 구성 금지
- 아이를 신비한 예언자로 연출 금지
- 메이라 솔이 병명을 확정하거나 설교로 장면을 채우지 않는다
- 아이리스가 도움에 감동해 협력하는 전개 금지

## 10. Active State / Props

- 형식이 존재하지 않는 신분문서
- 임시 노역표 — 기한부 등록이며 추적 가능
- 부러진 수레 축과 현지 재료 (쐐기·젖은 밧줄·목재)
- 환자 행렬의 순번표
- 은폐된 미래 장비 — 이 회차에서 사용 금지
- 귀환석 — 반응 없음. 종도 울리지 않는다
- 아이의 가족이 부르는 노래·집 위치 진술

노역표가 이후 회차에서 반복 사용될 경우 A10이 prop 승격 여부를 판정한다.

## 11. State Mutation Plan

E008 종료 시 기록:

- 임시 노역표 발급 여부·기한·조건
- 호송 의무로 확정된 임무 시간 손실
- 검문 기록에 남은 항목 (발음·수리기술·인상착의)
- 아이의 진술 내용과 목격자 범위
- 같은 가구 내 유사 증상자 수
- 메이라 솔의 판정 — 격리 또는 기록재심 보류
- 아이리스와의 접촉 등급과 그가 아는 것의 범위
- 본부 잔여 시한 갱신

## 12. Ready Verdict

- Authority: RESOLVED
- Domain Readiness: READY
- Storycraft companion: REQUIRED / prepared separately
- POV: READY — P3 배치는 allocation §6 조건 준수
- Scene count vs density map: PASS — E형 4장면 일치
- S0: 0
- S1: 0

Open item: 아이의 정본 신원을 C26 아벨 네르로 확정할지는 A08 판정 대상이다. 확정 전에는 원고에서 이름을 부르지 않고 가족 호칭으로만 처리한다.

E007 상태기록 확인 뒤 A18 호출 가능.
