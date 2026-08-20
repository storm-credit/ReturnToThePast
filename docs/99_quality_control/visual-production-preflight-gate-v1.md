# Visual Production Preflight Gate v1

Status: **D16.2 HARD GATE — NO IMAGE BEFORE PASS**  
Date: 2026-08-20  
Purpose: D16 문서설계가 실제 이미지 제작에서 유사얼굴·레퍼런스 복제·설정오염·AI 수렴·과상품화로 무너지는 것을 막는다.

---

# 1. Scope Distinction

## Reference / Design Documentation
**전체를 먼저 한다.**

- C01–C30 30명
- R01–R12 12개
- B01–B05 5종
- 핵심 배경 8축
- F01–F14 14세력
- Era O / N / F / P1 4상태

부분 샘플만 조사하고 이미지로 내려가는 것을 금지한다.

## Visual Validation Pilot
문서 전체 PASS 후 실제 이미지 검증은 대표 소수로 시작할 수 있다.

Pilot 후보:
- C01 에이든 로엔 — 주인공/시간요원/손실형 변형 검증
- C02 리아 세른 — 비전투 핵심인물/기록직업 검증
- R03 개혁가의 절검 — ‘갖고 싶음 → 놓아줘야 함’ 유산 검증
- B05 백지사슴 — 관찰차이/비펫 신수 검증
- L01 아르켄 또는 L02 서부 변경 — 배경 고유성 검증

Pilot 5개는 **조사범위 5개**가 아니라 **전체 문서가 작동하는지 보는 실물 샘플 5개**다.

---

# 2. Mandatory Documents Before First Image

다음이 모두 존재하고 PASS여야 한다.

1. `D16_IP_COLLECTIBILITY_DEEP_DESIGN_AMENDMENT_20260820.md`
2. C01–C30 Visual Identity Bible 3개
3. `collectible-relic-lineage-r01-r12-v1.md`
4. `sovereign-beast-iconography-b01-b05-v1.md`
5. `landmark-faction-visual-collection-bible-v1.md`
6. `collectibility-exposure-and-variant-map-v1.md`
7. `visual-reference-research-matrix-v1.md`
8. `visual-reference-coverage-all-assets-v1.md`
9. `face-silhouette-collision-gate-v1.md`
10. `d16-visual-collectibility-blindspot-brainstorm-v1.md`
11. 본 `visual-production-preflight-gate-v1.md`

Missing 1개라도 있으면 이미지 생성 금지.

---

# 3. Reference Research Gate

PASS 조건:

- 만화/애니/게임/영화·TV 최소 4매체 조사
- 얼굴 다양성 원리 확보
- 대규모 캐스트 식별 원리 확보
- 복식·직업·계층 원리 확보
- 세력 공통문법+개인차 원리 확보
- 유산/소품 마모·provenance 원리 확보
- 신수 생태 원리 확보
- 배경/랜드마크 원리 확보
- 각 참조작의 `가져오지 않을 것` 명시
- 특정 화풍/캐릭터 직접 모사 지시 0

Current: PASS.

---

# 4. Full Coverage Gate

PASS 조건:

- C 30/30
- R 12/12
- B 5/5
- Landmark 8/8
- Faction 14/14
- Era 4/4

Current: PASS.

---

# 5. D16.2 Blindspot / Brainstorm Gate

첫 이미지 전 다음 위험에 방어규칙이 있어야 한다.

- AI 미형화·대칭화
- 연령·체형 수렴
- 성별 시각코딩
- 선악 얼굴코딩
- 기록/군사/공방/해안/중앙권력 직업군 수렴
- C01/C08/C29/C30 시간요원계열 혼동
- 대표소품 기믹화
- 유산 스케일 단조
- 유산 Final Emotion 반복
- 신수 장엄화/펫화
- 랜드마크의 ‘겹침’ 모티프 반복
- 세력 로고·유니폼화
- Era 직선발전·P1 유토피아화
- 레퍼런스 누출
- 화풍이 얼굴다양성을 억압
- Variant 동일인 얼굴 드리프트
- 그룹샷 포즈·시선 수렴
- 팬덤/상품성에 의한 영구손실 침식

Current: **PASS — guards documented.**

Art Direction은 D16.2의 4안 중 `Hybrid Graphic Realism`을 **Pilot 기본안으로 추천**하지만 HARD LOCK하지 않는다.
Collectibility 운영은 `Braided Collection`을 추천한다.

---

# 6. Face Clone Prevention Gate

첫 캐릭터 이미지 전에도 적용하고, 매 캐릭터 승인 전 재적용한다.

## Before generation
- Face DNA 지정
- Body DNA 지정
- Gesture DNA 지정
- Silhouette DNA 지정
- 위험 충돌 대상 1–3명 지정

## After generation
- grayscale face crop 비교
- black silhouette 비교
- prop-less 비교
- 동일 성별/연령 위험군 비교
- hair/color masking 비교
- age spread 비교

FAIL이면 얼굴만 미세수정하지 않고 **골격/비율/자세 중 최소 2축을 다시 설계**한다.

---

# 7. Reference Integrity Gate

생성 전 프롬프트에서 다음을 검사한다.

## 금지 문장
- `X 스타일로`
- `X 캐릭터 같은 얼굴`
- `X와 Y를 섞은 디자인`
- 특정 배우 이름을 얼굴 템플릿으로 사용
- 특정 게임의 갑옷/무기를 그대로 변형

## 허용
- 역사적·기능적 일반 재료
- 직업에서 나온 도구
- 날씨·노동·계층에서 나온 마모
- D16 문서의 독립 실루엣
- Reference Matrix에서 추출된 추상 설계 원리

결과물 자체가 특정 참고작 캐릭터·복식·무기를 먼저 떠올리게 하면 `Reference Leak`로 FAIL 처리한다.

---

# 8. Canon Integrity Gate

이미지가 멋있다는 이유로 다음을 새 Canon으로 만들지 않는다.

- 새 마법능력
- 새 유산 기능
- 새 무기
- 새 세력
- 새 가문관계
- 인물간 가족관계
- 새 상처의 서사적 원인
- C30=에이든 암시
- 죽은 인물의 생존 변형

Visual Production은 **설정을 그린다. 설정을 발명하지 않는다.**

얼굴흉터 등 Production Soft DNA는 작가 승인 전 ‘서사 사건’의 증거가 아니다.

---

# 9. Character Production Order

전원 한꺼번에 생성하지 않는다.

## Phase V0 — Shape Exploration
- 흑백 실루엣
- 얼굴 없는 전신 구조
- 큰 재질덩어리

## Phase V1 — Face Exploration
- 4안
- 머리색/장식의존 최소
- 동일 조명 face crop

## Phase V2 — Integrated Concept
- 얼굴+전신+대표소품
- 기본자세
- 생활/직업 흔적

## Phase V3 — Variant
- 해당 캐릭터에게 실제 정본 Variant가 있는 경우만
- 색만 바꾸는 스킨 금지
- 승인된 Face DNA를 새로 설계하지 않는다

## Phase V4 — Production Sheet
- 정면/3-4면/후면 또는 필요한 턴어라운드
- 소재 close-up
- 손/소품 close-up
- 표정 3–5개

---

# 10. Relic Production Order

1. Black silhouette 4안
2. Human scale comparison
3. Material/age study
4. O Original
5. U In Use
6. C Contested
7. F Final
8. 4상태 한 줄 비교

R03/R06/R10/R12는 Final이 강화형처럼 보이면 FAIL.
R01–R12 전체는 최소 4개 Scale Band에 분산되는지 별도 확인한다.

---

# 11. Beast Production Order

1. Ecology notes 확인
2. Rest silhouette 4안
3. Moving silhouette
4. Human scale
5. Trace sheet
6. Environment interaction
7. 계약/거부 상황
8. Presence Type 비교

신수만 흰 배경에 세워둔 ‘몬스터 도감’ 1장으로 완료 처리 금지.
5종 모두가 ‘거대하고 장엄한 신비생물’로 읽히면 FAIL.

---

# 12. Landmark Production Order

1. 생활행동 foreground
2. 제도/노동 midground
3. 역사/시간 landmark background
4. 낮/밤보다 상태변형 우선
5. Region Primary Verb 확인
6. 사람 없는 beauty shot은 마지막

랜드마크는 엽서가 아니라 **사람이 사는 제도적 공간**이어야 한다.

Region Primary Verb:
- 아르켄 = 증축한다
- 서부 = 수선한다
- 셀카르 = 파고/접합한다
- 라디아 = 흐르게/막는다
- 조류도시 = 잠기고/드러난다
- 백지권 = 다시 적는다
- Era F = 재사용한다
- P1 = 나눠 맡는다

---

# 13. Pilot PASS Criteria — Core 50 Checks

대표 5종 Visual Validation Pilot은 다음 10문항을 각각 통과해야 한다.

1. 이름을 가리고도 무엇인지 구별 가능한가
2. 다른 판타지 작품의 캐릭터/물건/지역처럼 바로 읽히지 않는가
3. D16 실루엣이 실제 이미지에서 작동하는가
4. 재질이 직업/역사와 연결되는가
5. 장식이 이유 없이 추가되지 않았는가
6. 정본에 없는 능력/설정을 암시하지 않는가
7. 64px thumbnail에서 식별 가능한가
8. grayscale에서도 식별 가능한가
9. 팬이 소장하고 싶은 한 가지 포인트가 있는가
10. 그 소장욕이 서사적 의미를 해치지 않는가

5종 × 10문항 = 50 checks.

**50/50 전부 PASS 전에는 전체 Visual Production 양산 금지.**

---

# 14. D16.2 Additional Production Tests T1–T10

Core 50 Checks와 별도로 다음 10개를 수행한다.

### T1 Face Entropy Board
30명 face scaffold를 동일 조명·무표정으로 배열.

### T2 Body Entropy Board
소품·머리 제거 black silhouette.

### T3 Age Spread Board
청년/중년/노년의 조직량·피부·자세가 실제로 다른지 검사.

### T4 Moral Neutrality Board
주역/대립자 이름을 숨기고 악역 시각코딩 여부 검사.

### T5 Job Cluster Board
기록/군사/공방/해안/중앙권력 위험군만 따로 배열.

### T6 Group Scene Board
8명 이상 군중장면에서 자세·높이·시선·손동작 분산.

### T7 Relic Scale Board
R01–R12를 같은 인간 실루엣 옆에 놓아 크기분포 확인.

### T8 Beast Presence Board
본체가 아니라 발자국/소리/환경반응만으로 B01–B05를 구별 가능한지 확인.

### T9 Landmark Verb Board
8지역의 구조 스케치가 서로 다른 동사로 읽히는지 확인.

### T10 Reference Leak Check
특정 참고작 캐릭터·의상·무기가 먼저 떠오르는 결과는 재설계.

**T1–T10 중 하나라도 FAIL이면 전체 양산 금지.**

---

# 15. Group Composition Gate

8명 이상 그룹샷에서:

- 중심 높이 3단계 이상
- 몸 방향 최소 4종
- 손 사용 4종 이상
- 앉음/기댐/작업/이동 중 최소 2종
- 모든 인물이 카메라를 보는 단체사진 금지
- 세력별 색 덩어리로 단순 분리 금지

개별 캐릭터가 PASS해도 그룹에서 무너지면 Production PASS가 아니다.

---

# 16. Human Approval Rule

Visual Pilot에서 AI가 할 수 있는 판정:
- Structural PASS
- Collision PASS
- Canon PASS
- Reference Integrity PASS
- Production Ready

AI가 할 수 없는 최종 판정:
- `이 얼굴이 에이든의 최종 얼굴이다`
- `이 표지가 최종이다`
- `이 디자인이 작가 취향상 10/10이다`

최종 얼굴/대표이미지 SOFT LOCK → HARD LOCK 승격은 작가 승인 필요.

---

# 17. Current Verdict

Reference Research: PASS  
Full Asset Coverage: PASS  
D16.2 Blindspot Sweep: PASS  
D16.2 Constrained Brainstorm: PASS  
Face/Silhouette Scaffold: PASS  
Canon Mutation: 0  
Images Generated in this phase: **0**

**VISUAL PRODUCTION PREFLIGHT: PASS FOR PILOT, BUT PILOT NOT STARTED.**

다음 단계는 PR 상태와 문서 누락을 다시 검증하고, 작가 승인 뒤에만 Visual Validation Pilot을 시작한다.
