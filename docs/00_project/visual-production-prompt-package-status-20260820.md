# Visual Production Prompt / Handoff Package Status

Status: **D16.3 — PRODUCTION PROMPT ENGINEERING / COMPLETE — READY FOR VISUAL PILOT**  
Date: 2026-08-20  
Base: `main@7ff1ada8332887155d210926555ffa8281e43542`  
Scope: Visual Production 실행을 위한 프롬프트, 모델 독립 제작명세, 검수·인수인계 규칙  
Non-Scope: 사건/설정/결말/인물의도/유산 기능/신수 생태 변경

## 1. 목적

D16/D16.1/D16.2에서 설계한 비주얼 정체성을 실제 이미지 생성 모델 또는 전문 일러스트레이터가 일관되게 재현할 수 있도록 **실행 가능한 제작 패키지**로 변환한다.

핵심 원칙:

> 이미지를 대량 생성하지 않는다. 먼저 제작명세를 완성하고, 결과 이미지는 별도 Visual Pilot에서 검증한다.

## 2. 완료 범위

- Character: **C01–C30 = 30/30**
- Relic: **R01–R12 = 12/12**
- Sovereign Beast: **B01–B05 = 5/5**
- Landmark: **L01–L08 = 8/8**
- Faction: **F01–F14 = 14/14**
- Global Negative / Collision Rules: COMPLETE
- Visual Pilot Evaluation Sheet: COMPLETE
- External Artist / Image Model Handoff: COMPLETE
- Master Production Spec: COMPLETE
- Prompt Engineering Red Team: COMPLETE

## 3. 새 문서

### Project / Master
- `docs/00_project/visual-production-prompt-package-status-20260820.md`
- `docs/99_quality_control/visual-production-master-spec-v1.md`
- `docs/99_quality_control/visual-production-handoff-v1.md`

### Character Prompts
- `docs/05_characters/production-prompts-c01-c10-v1.md`
- `docs/05_characters/production-prompts-c11-c20-v1.md`
- `docs/05_characters/production-prompts-c21-c30-v1.md`

### Asset / World Prompts
- `docs/09_collection/production-prompts-r01-r12-v1.md`
- `docs/09_collection/production-prompts-b01-b05-v1.md`
- `docs/02_world/production-prompts-l01-l08-v1.md`
- `docs/02_world/production-prompts-f01-f14-v1.md`

### QA
- `docs/99_quality_control/visual-negative-and-collision-rules-v1.md`
- `docs/99_quality_control/visual-pilot-evaluation-sheet-v1.md`
- `docs/99_quality_control/visual-prompt-engineering-red-team-v1.md`

## 4. Production Rule

각 자산은 다음 5단계로 제작한다.

1. `V0 Shape Exploration` — 흑백/무채색 구조 4안
2. `V1 Identity Exploration` — 얼굴/형태/재질 4안
3. `V2 Integrated Concept` — 대표소품·행동·환경 결합
4. `V3 Canon Variant` — 정본에 실제 존재하는 상태변형만
5. `V4 Production Sheet` — 정면/3-4면/후면/디테일/표정 또는 구조 시트

한 번에 V4로 점프하면 FAIL.

## 5. Lock Levels

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

## 6. QA 결과

- 전체 자산 Prompt Coverage: **69/69 domain assets** (`30+12+5+8+14`)
- 특정 작품/배우/캐릭터 직접 모사 실행문구: **0**
- Model-specific syntax dependency: **0**
- Canon mutation: **0**
- New power/item/faction invention: **0**
- Face/Body collision dangerous clusters: covered
- Relic final-upgrade contamination: guarded
- Beast petification: guarded
- Landmark theme-park flattening: guarded
- Faction logo/color dependency: guarded
- C30 identity confirmation: guarded

## 7. Visual Pilot Gate

대표 5종:
- C01 에이든 로엔
- C02 리아 세른
- R03 개혁가의 절검
- B05 백지사슴
- L01 아르켄 또는 L02 서부 변경

실제 제작은 `V0 → V1 → V2` 순서로 먼저 검증한다.

전체 양산 전 필수:
- Pilot Core **50/50 PASS**
- D16.2 / D16.3 Production Tests PASS
- 작가의 방향 승인

## 8. Final Verdict

**D16.3 Visual Production Prompt / Handoff Package: COMPLETE.**

이 단계의 완료는 ‘실제 이미지가 10/10’이라는 뜻이 아니다. 정확한 의미는:

> **전체 비주얼 자산을 외부 이미지 모델 또는 전문 아티스트에게 넘길 수 있는 제작 명세·프롬프트·금지규칙·검수표가 준비되었다. 다음 단계는 Visual Pilot 실물 검증이다.**
