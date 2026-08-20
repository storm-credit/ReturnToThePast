# Visual Production Preflight Gate v1

Status: **D16.1 HARD GATE — NO IMAGE BEFORE PASS**  
Date: 2026-08-20  
Purpose: D16 문서설계가 실제 이미지 제작에서 유사얼굴·레퍼런스 복제·설정오염으로 무너지는 것을 막는다.

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
10. 본 `visual-production-preflight-gate-v1.md`

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

# 5. Face Clone Prevention Gate

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

FAIL이면 얼굴만 미세수정하지 않고 **골격/비율/자세 중 최소 2축을 다시 설계**한다.

---

# 6. Reference Integrity Gate

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

---

# 7. Canon Integrity Gate

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

# 8. Character Production Order

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

## Phase V4 — Production Sheet
- 정면/3-4면/후면 또는 필요한 턴어라운드
- 소재 close-up
- 손/소품 close-up
- 표정 3–5개

---

# 9. Relic Production Order

1. Black silhouette 4안
2. Material/age study
3. O Original
4. U In Use
5. C Contested
6. F Final
7. 4상태 한 줄 비교

R03/R06/R10/R12는 Final이 강화형처럼 보이면 FAIL.

---

# 10. Beast Production Order

1. Ecology notes 확인
2. Rest silhouette 4안
3. Moving silhouette
4. Human scale
5. Trace sheet
6. Environment interaction
7. 계약/거부 상황

신수만 흰 배경에 세워둔 ‘몬스터 도감’ 1장으로 완료 처리 금지.

---

# 11. Landmark Production Order

1. 생활행동 foreground
2. 제도/노동 midground
3. 역사/시간 landmark background
4. 낮/밤보다 상태변형 우선
5. 사람 없는 beauty shot은 마지막

랜드마크는 엽서가 아니라 **사람이 사는 제도적 공간**이어야 한다.

---

# 12. Pilot PASS Criteria

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

# 13. Human Approval Rule

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

# 14. Current Verdict

Reference Research: PASS  
Full Asset Coverage: PASS  
Face/Silhouette Scaffold: PASS  
Canon Mutation: 0  
Images Generated in this phase: **0**

**VISUAL PRODUCTION PREFLIGHT: PASS FOR PILOT, BUT PILOT NOT STARTED.**

다음 단계는 문서 누락 검증과 PR 상태 확인이며, 그 다음에만 Visual Validation Pilot을 시작한다.
