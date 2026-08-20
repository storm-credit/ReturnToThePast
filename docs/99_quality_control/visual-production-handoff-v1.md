# Visual Production Handoff v1

Status: **D16.3 EXTERNAL PRODUCTION HANDOFF**  
Audience: 이미지 생성 모델 운영자 / 콘셉트 아티스트 / 일러스트레이터 / 3D·굿즈 디자이너

---

# 1. 작품 비주얼 한 문장

**서로 다른 시대의 구조와 기록이 한 표면에서 완전히 지워지지 않고 겹쳐 보이는 판타지 문명.**

그러나 모든 것을 ‘겹침 효과’로 표현하지 않는다. 인물·유산·신수·장소는 직업, 재질, 손상, 생활, 권리관계로 구분한다.

---

# 2. 제작자가 먼저 읽을 문서

필수 순서:
1. `visual-production-master-spec-v1.md`
2. 대상별 Production Prompt Pack
3. `visual-negative-and-collision-rules-v1.md`
4. 대상의 기존 D16 Visual Identity/Relic/Beast/Landmark Bible
5. Pilot이면 `visual-pilot-evaluation-sheet-v1.md`

레거시 원고/구 설정을 빈칸 보충용으로 사용하지 않는다.

---

# 3. 절대 발명 금지

- 새 무기
- 새 마법
- 새 유산 기능
- 새 종족 특징
- 새 가족/연애관계
- 새 세력 문장 의미
- 흉터의 서사적 원인
- 죽은 인물의 생존
- 파괴된 유산의 복원
- C30의 정체 확정

브리프에서 비어 있는 세부는 `PRODUCTION SOFT`로만 제안한다.

---

# 4. 제출 단위

한 자산의 첫 제출은 완성일러스트 1장이 아니다.

## Character
- V0 shape 4안
- V1 face 4안
- 선택안 V2 integrated concept 1–2안

## Relic
- silhouette 4안
- scale/material study
- 선택안 O/U/C/F 계보

## Beast
- rest 4안
- moving 2안
- human scale / trace

## Landmark
- establishing composition 4안
- 선택안 functional/life layer

## Faction
- shape/material/behavior board
- 로고 없는 silent read test

---

# 5. Annotation Required

각 시안에는 짧게 표기한다.
- 어떤 HARD를 보존했는가
- 어떤 SOFT를 탐색했는가
- 어떤 위험대상과 차별화했는가
- 장식 3개 이하의 이유
- 가장 중요한 silhouette anchor 1개

설명할 수 없는 장식은 제거 후보.

---

# 6. Image Model Prompt Handoff

모델별 문법으로 바꿀 때도 의미 블록은 유지한다.

```text
[SUBJECT]
[SHAPE]
[MATERIAL]
[FUNCTION]
[WEAR]
[GESTURE]
[STATE]
[COMPOSITION]
[LIGHT]
[DO NOT]
```

특정 모델의 style preset이 얼굴 다양성을 줄이면 preset보다 D16 규칙을 우선한다.

---

# 7. Human Artist Handoff

일러스트레이터에게는 ‘유명작 A+B’ 무드보드보다 다음을 우선 제공한다.
- silhouette board
- material board
- occupational action
- wear/provenance
- contrast targets
- canon hard stop

레퍼런스 이미지는 복제대상이 아니라 문제해결 사례로만 사용한다.

---

# 8. 3D / Figure Translation

피규어화 시:
- 중력/지지점이 캐릭터 동작과 맞아야 함
- 대표소품이 없더라도 실루엣이 남아야 함
- 유산 Final state도 제품화 가능해야 함
- R03 파편, R06 분해부품, R10 분산인장처럼 ‘상실형 Final’을 삭제하지 않음
- 신수는 인간 탑승/소유 관계로 포즈를 바꾸지 않음

---

# 9. Cover Translation

표지는 production sheet와 다르다.

허용:
- 회화적 구도
- 강한 명암
- 상징적 배치

보존:
- 얼굴 DNA
- Primary Silhouette
- 핵심 재질
- 소유권/상태

금지:
- 표지 멋을 위해 새 무기/의상 추가
- 에이든을 왕자/성기사형으로 재해석
- 리아를 마법사형 기록관으로 재해석

---

# 10. Revision Protocol

수정 요청은 `예쁘게/더 멋있게` 대신 축을 지정한다.

예:
- face width +12%
- shoulder slope lower
- coat length shorten to mid-thigh or above
- prop visual weight reduce
- material gloss remove
- center of gravity lower
- landmark horizontal axis stronger

한 번에 3축 이상 큰 수정 시 새 option으로 관리한다.

---

# 11. Approval & File State

- `EXPLORE`: 자유 탐색
- `STRUCTURAL PASS`: 형태 통과
- `SOFT APPROVED`: 작가 방향 승인
- `PRODUCTION READY`: 시트/변형 제작 가능
- `HARD VISUAL LOCK`: 작가 최종 승인

파일명에 상태를 남긴다.

---

# 12. Pilot First

전체 양산 전에 대표 5종 Pilot을 수행한다.

Pilot이 50/50 Core + T1–T10을 통과하기 전:
- C01–C30 전체 최종렌더 금지
- 대규모 굿즈라인 설계 금지
- 얼굴 HARD LOCK 금지

---

# 13. Delivery Checklist

납품 시 함께 제출:
- 이미지 원본
- 축소 thumbnail
- grayscale
- silhouette
- prompt/brief version
- asset state
- revision notes
- known collision risks

이 패키지가 없으면 ‘완성 이미지’만 있어도 production complete로 처리하지 않는다.
