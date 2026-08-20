# Visual Production Prompt / Handoff Package Status

Status: **D16.3 — PRODUCTION PROMPT ENGINEERING / IN PROGRESS**  
Date: 2026-08-20  
Base: `main@7ff1ada8332887155d210926555ffa8281e43542`  
Scope: Visual Production 실행을 위한 프롬프트, 모델 독립 제작명세, 검수·인수인계 규칙  
Non-Scope: 사건/설정/결말/인물의도/유산 기능/신수 생태 변경

## 1. 목적

D16/D16.1/D16.2에서 설계한 비주얼 정체성을 실제 이미지 생성 모델 또는 전문 일러스트레이터가 일관되게 재현할 수 있도록 **실행 가능한 제작 패키지**로 변환한다.

핵심 원칙:

> 이미지를 대량 생성하지 않는다. 먼저 제작명세를 완성하고, 결과 이미지는 별도 Visual Pilot에서 검증한다.

## 2. 완료 대상

- C01–C30 Character Production Prompt Pack
- R01–R12 Relic Production Prompt Pack
- B01–B05 Sovereign Beast Production Prompt Pack
- L01–L08 Landmark Production Prompt Pack
- F01–F14 Faction Visual Prompt Pack
- Global Negative Prompt / Collision Rules
- Visual Pilot Evaluation Sheet
- External Artist / Image Model Handoff
- Master Production Spec

## 3. Production Rule

각 자산은 다음 5단계로 제작한다.

1. `V0 Shape Exploration` — 흑백/무채색 구조 4안
2. `V1 Identity Exploration` — 얼굴/형태/재질 4안
3. `V2 Integrated Concept` — 대표소품·행동·환경 결합
4. `V3 Canon Variant` — 정본에 실제 존재하는 상태변형만
5. `V4 Production Sheet` — 정면/3-4면/후면/디테일/표정 또는 구조 시트

한 번에 V4로 점프하면 FAIL.

## 4. Lock Levels

### HARD
- 역할, 기능, 사건, 소유권, 최종상태
- 종족/문화/직업의 기존 정본
- 캐릭터 간 관계와 정보천장
- 유산 기능 및 파괴/분해/반환
- 신수 비소유/거부권
- C30 정체 불확정

### PRODUCTION SOFT
- 정확한 머리색/길이
- 일부 얼굴 디테일
- 작은 문양 위치
- 세부 버클/봉제선
- 정확한 팔레트

SOFT 필드는 Pilot에서 작가 승인 전 Canon HARD로 승격하지 않는다.

## 5. Exit Criteria

- Character 30/30 prompt coverage
- Relic 12/12
- Beast 5/5
- Landmark 8/8
- Faction 14/14
- Global negative/collision 100%
- Pilot evaluation sheet ready
- Handoff ready
- 특정 작품/배우/캐릭터 직접 모사 문구 0
- plot/canon mutation 0

문서 완료 뒤에만 실제 Visual Pilot을 진행한다.
