# Visual Production Master Spec v1

Status: **D16.3 PRODUCTION SPEC**  
Depends On: D16 IP Collectibility, D16.1 Reference Research, D16.2 Blindspot/Brainstorm, Visual Production Preflight  
Purpose: 이미지 모델/일러스트레이터가 작품 설정을 발명하지 않고, 기존 설계를 일관된 제작 결과로 번역하도록 한다.

---

# 1. Master Principle

> **서사적으로는 소유하지 못해도, 독자는 기억하고 갖고 싶어해야 한다.**

비주얼은 강함·희귀도·가챠 등급이 아니라 `형태 + 재질 + 사용흔적 + 소유권 + 관계 + 시대변형`으로 기억된다.

---

# 2. Model-Agnostic Prompt Architecture

모든 프롬프트는 다음 순서로 작성한다.

1. `SUBJECT` — 대상과 역할
2. `SHAPE` — 체형/실루엣/빈 공간
3. `MATERIAL` — 천·금속·종이·석재·생체표면
4. `FUNCTION` — 직업/생활 때문에 필요한 구조
5. `WEAR` — 손상/수선/사용흔적
6. `GESTURE` — 몸 쓰는 방식 또는 이동 리듬
7. `STATE` — O/N/F/P1 또는 인물/유산 상태
8. `COMPOSITION` — 검증 목적에 맞는 화면
9. `LIGHT` — 재질과 실루엣이 읽히는 중립광
10. `DO NOT` — 중복·클리셰·정본오염 금지

특정 작품명/배우명/캐릭터명을 프롬프트의 스타일 지시로 쓰지 않는다.

---

# 3. Art Direction — Pilot Default

D16.2 추천 기본안: `Hybrid Graphic Realism`.

정의:
- 얼굴/체형/실루엣: 과감하게 차별화
- 재질/생활흔적: 현실적 물성
- 장식: 기능에서 나오지 않으면 제거
- 대표 이미지: 회화적 구도 허용
- Production Sheet: 중립적이고 설명 가능한 조명

금지:
- 동일 미형 얼굴 템플릿
- 모든 남성 넓은 어깨/장신
- 모든 여성 가는 허리/장발
- 선악을 얼굴 미추로 코딩
- 영화 스틸처럼 어둡게 가려 실루엣 검증 불가
- 과도한 보케/연기/역광으로 디자인을 숨김

---

# 4. V0–V4 Production Sequence

## V0 Shape Exploration
목적: 얼굴/색/소품 없이도 구별되는지 검사.

출력:
- 4안 한 화면 또는 동일 조건 4장
- 흑백 또는 저채도
- 정면/3-4면 실루엣
- 단순한 배경

PASS:
- Primary shape가 3초 안에 읽힘
- 위험 충돌 대상과 60% 이상 실루엣 차이

## V1 Identity Exploration
목적: 얼굴/형태/재질의 독립성.

출력:
- 얼굴 4안
- 동일 렌즈/조명/표정
- 헤어/장식 의존 최소

PASS:
- 머리색을 회색으로 바꿔도 얼굴 구별
- 나이/체형/생활흔적이 역할과 연결

## V2 Integrated Concept
목적: 인물/물건/생물/장소의 대표이미지.

출력:
- 대표소품/행동 포함
- 기능이 화면에서 읽힘
- 장식의 이유 설명 가능

## V3 Canon Variant
정본에 실제 상태 변화가 존재하는 경우만 제작.

금지:
- 단순 팔레트 스킨
- 인기 때문에 만든 비정본 최종폼
- 죽은 인물 생존형
- 파괴된 유산 복원형

## V4 Production Sheet
최종 승인 전 제작기준.

캐릭터:
- 정면 / 3-4면 / 후면
- face close-up
- hands / prop
- 표정 3–5
- 재질 close-up

유산:
- front / side / scale
- O/U/C/F 비교
- 손상/접합 디테일

신수:
- rest / moving / human scale / trace / environment

배경:
- one-shot / functional section / state variant

---

# 5. Prompt Strength Hierarchy

충돌 시 우선순위:

1. Canon HARD
2. D16 visual identity
3. Collision/Blindspot Gate
4. 본 Master Spec
5. Asset Prompt
6. Model-specific syntax
7. 미적 우연

‘이미지가 예쁘다’는 1–5를 뒤집는 사유가 아니다.

---

# 6. Four-Option Rule

다음은 첫 승인 전에 반드시 4안을 비교한다.

- C01–C30의 V0와 V1
- R01–R12의 기본 실루엣
- B01–B05의 rest/moving shape
- L01–L08의 establishing composition

4안은 색만 다른 변형이 아니다. 최소 2개 이상의 구조축이 달라야 한다.

구조축 예:
- 비례
- 무게중심
- 큰 빈 공간
- 소품 위치
- 재질 덩어리
- 건축 수평/수직 구조
- 신수 이동 자세

---

# 7. Canon-Safe Descriptive Vocabulary

권장:
- worn, repaired, work-used, asymmetrical, layered, documented, locally modified
- practical, occupational, weathered, weight-bearing, public-use, distributed
- imperfect, non-ornamental, hand-repaired, evidence-bearing

주의:
- legendary, divine, ultimate, supreme, sacred, chosen, godlike

후자는 정본에 실제로 그런 의미가 있을 때만 쓴다.

---

# 8. Reference Translation Rule

레퍼런스 작품에서 가져오는 것은 결과물이 아니라 원리다.

예:
- `작품 X 스타일` → 금지
- `배우 Y 같은 얼굴` → 금지
- `캐릭터 Z의 갑옷처럼` → 금지

허용 변환:
- 강한 얼굴 비율 차이
- 직업이 만든 몸짓
- 환경이 만든 옷의 구조
- 마모가 물건의 provenance를 설명
- 세력 공통문법 속 개인차
- 생태에서 외형을 역산

---

# 9. Consistency Anchors

캐릭터마다 승인 후 다음을 텍스트 기준으로 고정한다.

- 5 Face Anchors
- 4 Body Anchors
- 3 Material Anchors
- 2 Gesture Anchors
- 1 Primary Silhouette

이미지 seed/model 기능은 보조수단일 뿐 정본은 이 텍스트 앵커다.

---

# 10. Approval States

- `EXPLORE` — 방향 탐색
- `STRUCTURAL PASS` — 형태/충돌 통과
- `SOFT APPROVED` — 작가가 방향 승인
- `PRODUCTION READY` — V4 제작 가능
- `HARD VISUAL LOCK` — 작가 명시 승인 후만 가능

AI는 자동으로 HARD VISUAL LOCK을 선언하지 않는다.

---

# 11. Batch Rule

한 번에 전체 30명을 최종 렌더하지 않는다.

권장 캐릭터 배치:
- Batch A: C01/C02/C03/C04/C05
- Batch B: C06–C10
- Batch C: C11–C15
- Batch D: C16–C20
- Batch E: C21–C25
- Batch F: C26–C30

각 배치 승인 전에 동일 기능 위험군과 교차 비교한다.

---

# 12. Production Stop Conditions

즉시 중지/재설계:
- 얼굴 clone 느낌
- 헤어/색을 지우면 식별 불가
- 특정 유명 캐릭터가 바로 연상됨
- 정본에 없는 무기/마법/가문표식 생성
- 신수 펫화/안장/포획표현
- 유산 상위등급화
- P1 완벽한 유토피아화
- C30=에이든 시각 확정
- 파괴/사망/영구손실을 상품 Variant로 되돌림

---

# 13. Output Naming

`<ASSET>-<STAGE>-<OPTION>-<STATE>-vNN`

예:
- `C01-V0-A-BASE-v01`
- `R03-V2-B-U-v02`
- `B05-V1-C-OBS-B-v01`
- `L01-V2-A-P1-v01`

파일명에 특정 레퍼런스 작품명을 넣지 않는다.
