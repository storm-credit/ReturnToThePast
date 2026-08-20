# Visual Prompt Engineering Red Team v1

Status: **D16.3 PROMPT QA**  
Purpose: 설계가 좋아도 이미지 모델의 프롬프트 해석 특성 때문에 결과가 망가지는 생산 리스크를 사전 차단한다.

---

# P1 — Prompt Bloat

위험: 모든 설정을 한 프롬프트에 넣어 Primary Silhouette가 묻힘.

방어:
- 한 생성 단계당 목적 1개
- V0에서는 얼굴/세부색/서사 설명 제거
- V1에서는 전신소품 최소화
- V2에서만 통합
- Prompt 핵심 8–12개 시각단서 이내

FAIL 신호: 결과마다 임의 장식이 늘고 핵심 shape가 약해짐.

---

# P2 — Negative Prompt Overreliance

위험: `no long coat`만 반복해도 모델이 long coat 개념을 오히려 강화할 수 있음.

방어:
- 긍정 구조를 먼저 명시: `short diagonally cut jacket ending above mid-thigh`
- negative는 마지막 Guard로 사용
- 금지요소가 반복되면 composition/shape를 바꿔 해결

---

# P3 — Four Options That Are Actually One

위험: 4안이 색/버클만 다른 동일 디자인.

방어:
각 옵션은 다음 중 최소 2축 변화:
- proportion
- center of gravity
- negative space
- major material block
- prop placement
- posture

A/B/C/D의 차이를 생성 전 문장으로 적는다.

---

# P4 — Model Beauty Prior

위험: 모델이 모두 젊고 매력적인 얼굴로 자동 보정.

방어:
- age texture 명시
- occupational wear 명시
- skull/face proportion을 캐릭터마다 다르게
- `attractive/handsome/beautiful` 같은 가치형용사 제거
- 동일 조명 face board로 비교

---

# P5 — Style Preset Eats Character DNA

위험: 특정 preset/LoRA/style reference가 얼굴을 한 템플릿으로 통일.

방어:
- V1 face exploration은 style 강도 최소
- Face DNA 통과 후 style layer 추가
- 스타일 추가 전/후 face crop 비교
- 얼굴앵커 5개 중 4개 미만 유지 시 style 적용 취소

---

# P6 — Reference Leak

위험: 레퍼런스 작품명을 프롬프트에 넣어 결과가 표면복제로 이동.

방어:
- 작품명은 Research Matrix에서만 존재
- 실행 프롬프트에는 추상 원리만 이동
- 특정 캐릭터/배우/작가명 0
- 결과물도 역검색 감각으로 ‘누가 바로 떠오르는지’ 검사

---

# P7 — Prompt-to-Canon Leak

위험: 모델이 만든 흉터/문양/무기를 나중에 설정으로 역수입.

방어:
- 생성된 새 디테일은 기본 `NON-CANON PRODUCTION ACCIDENT`
- 작가 승인 없는 신규 디테일을 원고에 사용 금지
- V2 Review에서 `Canon / Soft / Accident` 3분류

---

# P8 — Variant Face Drift

위험: 같은 캐릭터 상태변형이 다른 사람처럼 생성.

방어:
- Base face 승인 전 Variant 금지
- 5 Face Anchors를 매 프롬프트 앞에 재기재
- age/wear/gear만 변경
- Variant face crop overlay 비교

---

# P9 — Same Character, Same Pose Forever

위험: 일관성을 유지하려다 모든 그림이 동일 포즈.

방어:
Identity anchor와 pose를 분리한다.
- 얼굴/체형/재질은 고정
- 제스처는 캐릭터의 행동문법 안에서 3–5종 순환

---

# P10 — Generic Fantasy Auto-Fill

위험: 비어 있는 부분을 모델이 망토/검/룬/금장으로 자동 보충.

방어:
- 빈 공간을 의도적으로 명시
- `empty back, no trophy object`
- `plain functional closure`
- `unornamented working surface`

장식 추가보다 `negative space`를 디자인 요소로 사용.

---

# P11 — Medium Translation Failure

위험: 캐릭터 일러스트 프롬프트를 그대로 피규어/표지/3D에 사용.

방어:
- Concept / Turnaround / Cover / Figure를 별도 brief로 변환
- Canon anchor만 공유
- composition instruction은 매체별 분리

---

# P12 — Model-Specific Syntax Lock-In

위험: 특정 이미지 모델이 없어지면 문서 전체가 무용해짐.

방어:
정본 프롬프트는 자연어 의미블록으로 유지.
모델 adapter는 별도 일회성 레이어.

`SUBJECT → SHAPE → MATERIAL → FUNCTION → WEAR → GESTURE → STATE → COMPOSITION → LIGHT → DO NOT`

이 구조가 tool-independent source of truth.

---

# P13 — Seed Consistency Illusion

위험: 같은 seed가 곧 같은 캐릭터 정체성이라고 착각.

방어:
- seed는 기술 보조
- Face/Body/Material/Gesture text anchors가 정본
- 모델 변경 후에도 anchor로 재생성 가능해야 함

---

# P14 — One Great Image Bias

위험: 우연히 멋있는 1장을 보고 충돌/정본 위반을 무시.

방어:
최종 판단은 최소:
- face crop
- silhouette
- prop-off
- thumbnail
- integrated concept

5면에서 통과해야 한다.

---

# P15 — Pilot Overfit

위험: C01/C02/R03/B05/L01만 잘 되고 나머지 50+ 자산에 적용 불가.

방어:
Pilot 통과 후 즉시 위험군 mini-batch 검증:
- C08/C29/C30
- C12/C22
- C24
- R06/R10/R12
- B02/B04
- L06/L08

이 mini-batch까지 통과해야 대량생산.

---

# P16 — Prompt Language Ambiguity

위험: `짧은`, `무겁지 않은`, `현장형` 등 상대형용사가 모델마다 다르게 해석.

방어:
가능하면 구조적 기준으로 교체:
- `outerwear ends above mid-thigh`
- `shoulder line narrower than heroic armored silhouette`
- `bag occupies less than 15% of torso width`

정확 수치는 필요할 때만 Production Soft로 둔다.

---

# P17 — Negative List Becomes IP Identity

위험: 금지사항이 너무 많아 결과가 무색무취.

방어:
각 자산마다 반드시 **positive desire hook 1개**를 앞에 둔다.

예:
- C01 빈 귀환고리와 사선 외투
- R03 잘린 검의 이유
- B05 관찰판 불일치
- L02 성벽 아래 살아 있는 학교/시장

---

# Final Verdict Gate

Prompt package PASS 조건:
- 전체 자산 coverage 100%
- 실행 프롬프트에서 직접 작품/배우 모사 0
- 각 자산 positive hook 존재
- 각 위험군 collision rule 존재
- V0/V1/V2/V3/V4 분리
- model-agnostic source 유지
- Canon mutation 0

실제 이미지가 나오기 전에는 `VISUAL QUALITY 10/10`을 선언하지 않는다. 문서 상태만 `PRODUCTION PROMPT READY`로 판정한다.
