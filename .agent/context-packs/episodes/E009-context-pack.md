# Episode Context Pack — E009

Status: D10 READY  
Episode: E009  
Title: 두 개의 출생증명  
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
- [`docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md`](../../../docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md) E009 행
- [`docs/10_story_architecture/detail/v01-scene-ready-design-v1.md`](../../../docs/10_story_architecture/detail/v01-scene-ready-design-v1.md) E009 절
- [`docs/10_story_architecture/scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) E009 `S · 3장면`
- [`docs/10_story_architecture/subact-causal-matrix-v1.md`](../../../docs/10_story_architecture/subact-causal-matrix-v1.md) 1B
- [`docs/03_systems/mana-fever-gray-calamity-v1.md`](../../../docs/03_systems/mana-fever-gray-calamity-v1.md)
- [`docs/11_mystery/mystery-reinforcement-ladder-v1.md`](../../../docs/11_mystery/mystery-reinforcement-ladder-v1.md) M01·M16
- [`.agent/context-packs/episodes/E008-context-pack.md`](E008-context-pack.md)

Episode function (registry E009 행 + 1B dossier):

- Grand Act: GA I — 잘못된 치료
- Volume: V1 — 회색 종이 울리는 날
- Subact: 1B — 격리촌의 통행증
- Beat: 잘못된 해석
- Goal: 마나열병이 전염병처럼 보이게 한다
- Opposition: 두 장 모두 진품인 출생증명, 격리를 요구하는 미래 지식과 그것을 거부하는 관측 결과
- Choice: 에이든은 아이를 격리하려 하지만 증상이 기록 오류와 함께 나타난다
- Cost: 미래 지식으로 내린 첫 판단이 현지에서 틀리고, 가족과 아이리스의 불신이 커진다
- State Change: ‘아는 사람으로서의 개입’이 ‘모른다는 사실을 인정한 관찰’로 바뀜
- Hook: 아이의 두 번째 고향이 공식 지도에 존재하지 않는다

## 2. E008 Carryover

Source: E008 CP §11, v01 scene-ready E008

### 에이든

- 임시 노역표 보유 — 기한부 등록이며 추적 가능
- 호송 조건으로 임무 시간이 이미 줄어 있다
- 검문 기록에 발음·수리기술·인상착의가 남았다
- 아이의 진술을 기억하고 있으며 감염 가설 쪽으로 판단이 정렬돼 있다
- 미래 장비는 은폐 상태, 사용 금지 상태 유지

### 행렬과 아이

- 아이의 발작 이후 행렬 전체가 강제 격리 위험에 놓였다
- 같은 가구에서 유사 증상이 함께 나타났다
- 가족은 아이를 부정하지도 신비화하지도 않는다

### 아이리스 네르

- 에이든의 순번과 호송 위치를 바꿔 놓았다
- 능력의 출처를 한 번 물었고 답을 받지 못했다
- 에이든의 임무 목적은 여전히 모른다

### 메이라 솔

- 격리 또는 기록재심 결정을 보류한 상태
- 병명을 확정하지 않는다

## 3. Time / Location

Source: master-chronology §4 J01·§3 V1, v01 scene-ready E009

- Date: 건국력 640년 안개월 5일 전후 (E008 직후 연속 구간)
- Era: N0
- 에이든: 41세 / 주관적 누적 2~3일
- Main locations:
  1. 임시진료막
  2. 서류대
  3. 증상관찰 구역
- 이동은 격리촌 관문 안쪽 구역 내부로 제한된다
- 행렬은 아직 도시에 들어가지 못했다. 대기 자체가 환자에게 비용이다

## 4. 마나열병 관측 패키지

Sources:

- [`docs/03_systems/mana-fever-gray-calamity-v1.md`](../../../docs/03_systems/mana-fever-gray-calamity-v1.md)
- [`docs/02_world/religion-ritual-clergy-encyclopedia-v2.md`](../../../docs/02_world/religion-ritual-clergy-encyclopedia-v2.md) §8
- [`docs/02_world/atlas-region-dossiers-v1.md`](../../../docs/02_world/atlas-region-dossiers-v1.md) R05

### 이 회차에서 관측 가능한 것

- 고열, 낯선 이름·장소의 꿈, 순간적 기시감 — 1단계 잔향열
- 서로 모순되는 가족·직업·기억이 나타남 — 2단계 이중기록
- 같은 가족·가구에서 함께 발생
- 문서를 읽거나 낭독할 때 열과 마력 폭주가 악화
- 가족이 손을 잡으면 안정

### 전염병처럼 보이는 합리적 이유

- 같은 가족·마을·길드가 동일한 기록과 토지주소를 공유한다
- 환자의 폭주 마나가 주변 인장의 불일치를 드러낸다
- 격리 정책이 주민등록과 생업을 끊어 2차 환자를 만든다
- 곰팡이·광물 분진이 증상을 악화시키는 것도 사실이다

### 성당 진단 절차

1. 체온·피부·호흡 검사
2. 이름·날짜·장소 문답
3. 가족·토지·세금 기록 비교
4. 회색 종 또는 주소 반응 검사
5. 격리 또는 기록재심 결정

E009는 절차 2~4에 머문다. 5단계 결정은 보류된 채 회차가 끝난다.

### 서부 변경의 생활 관습

- 주민은 문서 외에도 벽흔·가족노래·묘표·공동식사 순번으로 존재를 증명한다
- 아이에게 한 개의 공적 이름과 두 개의 사적 기억이름을 주는 관습이 있다
- 이 관습은 두 장의 출생증명을 설명하지 못한다. 관습은 이름의 문제이고 증명서는 부모·생일·고향이 다르다

### 절대 금지

- 마나열병이 감염이 아니라는 정답 공개
- 회색 종 반응 원리의 설명
- 두 문서 중 하나가 위조라는 확정
- 치료법 제시

## 5. Character State

Sources: cast-canon-index-v2 C01·C03·C10·C26, voice-relationship-state-bible-v1 §2·§2-A, mana-fever-gray-calamity-v1

### 에이든 로엔

- 목표: 확산을 막고 행렬 전체의 발이 묶이는 것을 피한다
- 근거: 미래 본부는 초기에 감염원 제거 논리로 오판했다. 그는 그 논리를 몸에 지니고 왔다
- 죄책감 표식: 아이를 이름이 아니라 ‘환자’로 부른다
- 전환: 관측 결과가 가설과 어긋날 때 가설을 방어하지 않고 관측을 다시 센다
- 금지: 즉석에서 정답에 도달, 미래 의료지식으로 치료, 자기 오판을 남 탓으로 돌리기

### 아이리스 네르

- 두 장의 출생증명을 가지고 있으며 그것을 무기가 아니라 반증으로 내민다
- 격리 주장에 반대하는 이유는 감상이 아니라 격리가 만들어 온 2차 피해다
- 에이든이 무엇을 아는 사람인지 이 회차에서 처음 저울질한다
- 금지: 정답을 먼저 알고 있는 인물로 처리, 감동에 의한 협력

### 아이 (E008 CP §5의 도출 대상)

- 증상은 실제이고 진술도 실제다. 둘 중 하나를 거짓으로 만들지 않는다
- 기록을 읽을 때 악화되고 가족의 손을 잡으면 안정된다
- 자기 상태를 설명하지 못한다. 예언자화 금지

### 메이라 솔

- 병명을 확정하지 않으며 격리와 재심을 같은 호흡으로 말한다
- 거절 근거로 교리를 대지 않고 침상 수·물·오늘 밤 들어올 사람 수를 댄다
- 감당할 수 없는 약속이 먼저 튀어나오고 곧바로 수를 다시 센다
- 달력기관은 대사에서 `종탑`으로만 부른다

### 아이의 가족

- 두 개의 기억이름을 주는 관습을 설명하되 그것으로 증명서를 해명하지 못한다
- 아이를 지키는 방법으로 증언과 접촉을 선택한다
- 감정적 인질로 소비하지 않는다

## 6. Mystery / Information Ceiling

Source: mystery-reinforcement-ladder-v1 M01·M16·M13

Active mysteries:

- M01 마나열병은 전염병인가 — E008 가족 집단발병에 이어 기록 연동 관측이 추가된다
- M16 회색 종은 무엇을 감지하는가 — 사다리 E009 단계 `환자 곁에서 울림`
- M13 움브라는 어디서 왔는가 — 존재하지 않는 고향이라는 형태로만 예고

Reader may know:

- 두 장의 출생증명이 모두 진품이며 종이와 잉크 연대가 같다
- 증상이 기록을 읽는 행위와 연동해 악화된다
- 가족의 접촉이 증상을 안정시킨다
- 회색 종이 이번에는 환자 곁에서 울린다

Reader must not know yet:

- 마나열병이 연속성 불일치 반응이라는 정답 (추론 가능 시점 E176)
- 회색 종이 주소 불일치를 감지한다는 정답 (추론 가능 시점 E092)
- 두 기록 중 무엇이 먼저이고 누가 손댔는지
- 세렌의 전체 기능·조작 주체·삭제 증언자의 정체
- 19만 모델의 최종 오류구조

Final hook:

- 아이의 두 번째 고향이 공식 지도에 존재하지 않는다
- 의미: 문제는 아이의 몸이 아니라 장소가 사라지는 방식일 수 있다
- 금지: 지도 삭제의 주체·이유 공개, 세렌 사건과의 연결 확정

## 7. POV / Storycraft

- POV: 에이든 단일 근접 3인칭
- Scene Density: S형 3장면 — scene-density-map-v1 E009 `S · 3장면`
- Primary craft: 합리적 오답의 실패 실연
- Secondary A: 진품 두 장의 역설
- Secondary B: 몸으로 검증되는 단서
- Hook: H2 정보 역전
- Reader reward: 주인공이 틀리는 장면을 무능이 아니라 정보 구조의 결과로 읽는 경험

## 8. Scene Values

### Scene 1 — 임시진료막

- Entry: 확산을 막으려면 분리가 우선이다
- Opposition: 침상·물·인력의 실제 수치, 격리가 만들어 온 2차 피해, 가족의 거부
- Exit: 격리 주장은 관철되지 않고, 그가 근거로 든 전염 모델이 시험대에 오른다

### Scene 2 — 서류대

- Entry: 두 기록 중 하나는 위조일 것이다
- Opposition: 부모·생일·고향이 다르지만 인장은 모두 진품이고 종이와 잉크 연대도 같다
- Exit: 위조 가설이 무너지고, 문서가 아니라 사람 쪽을 봐야 한다는 조건으로 바뀜

### Scene 3 — 증상관찰

- Entry: 남은 설명은 여전히 질병 하나뿐이다
- Opposition: 기록을 읽을 때 악화되고 가족의 손을 잡으면 안정되는 반응, 그리고 환자 곁에서 울리는 회색 종
- Exit: 생물학적 전염만으로 설명할 수 없음을 인정하고, 두 번째 고향이 지도에 없다는 사실이 남는다

## 9. Anti-Repeat

- E003의 두 문서 대조 구조 반복 금지 — 여기서 두 문서는 모순을 만들지 않는다. 둘 다 진품이고 결론은 종이가 아니라 아이의 몸과 가족의 접촉에서 나온다
- E008의 검문·협상 구성을 반복하지 않는다. 이 회차에는 통과할 관문이 없다
- E007의 은폐 장면과 종의 도입 방식을 반복하지 않는다 — 종은 이번에 사람 곁에서 운다
- E001의 삭제된 글자 훅 반복 금지
- 미래 의료지식으로 병을 진단하거나 치료하는 전개 금지
- 아이를 예언자로, 가족을 감정 장치로 소비 금지
- ‘사실 전부 조작이었다’는 단순 반전 금지
- 격리를 주장한 에이든을 악인화하거나 즉시 사과시키지 않는다

## 10. Active State / Props

- 두 장의 출생증명 — 부모·생일·고향 상이, 인장 모두 진품, 종이·잉크 연대 동일
- 임시 노역표
- 회색 종 (R01) — 이번에는 환자 곁에서 울린다. 여전히 지역 공동소유물
- 진료막의 침상·물·소금 수량
- 아이의 가족노래와 집 위치 진술
- 공식 지도 사본 — 두 번째 고향이 없는 판본

## 11. State Mutation Plan

E009 종료 시 기록:

- 격리 주장의 처리 결과와 남은 격리 위험 등급
- 두 출생증명의 검증 상태 (진품 / 위조 아님 / 선후 미확정)
- 아이의 증상·진술 관측 항목
- 회색 종 두 번째 관측 기록 (환자 곁, E007과 다른 대상)
- 에이든의 전염 가설 신뢰도 하향과 대체 가설 부재
- 아이리스·가족의 신뢰도 변화
- 메이라 솔의 판정 보류 지속 여부
- 임무 가용시간 추가 손실

## 12. Ready Verdict

- Authority: RESOLVED
- Domain Readiness: READY
- Storycraft companion: REQUIRED / prepared separately
- POV: READY
- Scene count vs density map: PASS — S형 3장면 일치
- S0: 0
- S1: 0

E008 상태기록 확인 뒤 A18 호출 가능.
