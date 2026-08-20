# Visual Production Prompt / Handoff Package Status

Status: **D16.3 + D16.4 — PRODUCTION PROMPT ENGINEERING + ACT-MAP VISUAL BINDING / COMPLETE**  
Date: 2026-08-20  
Base: `main@7ff1ada8332887155d210926555ffa8281e43542`  
Scope: Visual Production 실행 프롬프트, 모델 독립 제작명세, 검수·인수인계 규칙, 5 Grand Acts / 15 Volumes / Episode CP 연결  
Non-Scope: 사건/설정/결말/인물의도/유산 기능/신수 생태 변경

## 1. 목적

D16/D16.1/D16.2의 비주얼 정체성을 실제 이미지 생성 모델 또는 전문 일러스트레이터가 일관되게 재현할 수 있는 실행 패키지로 변환하고, **각 비주얼 자산을 실제 Act Map / Volume / Episode Context Pack에서 정확한 상태로 호출하도록 연결한다.**

핵심 원칙:

> 이미지를 대량 생성하지 않는다. 먼저 제작명세와 서사 사용 위치를 모두 잠그고, 결과 이미지는 별도 Visual Pilot에서 검증한다.

## 2. 완료 범위

### Asset Production Prompt Coverage
- Character: **C01–C30 = 30/30**
- Relic: **R01–R12 = 12/12**
- Sovereign Beast: **B01–B05 = 5/5**
- Landmark: **L01–L08 = 8/8**
- Faction: **F01–F14 = 14/14**
- Total domain assets: **69/69**

### Production / QA
- Global Negative / Collision Rules: COMPLETE
- Visual Pilot Evaluation Sheet: COMPLETE
- Visual Pilot Copy-Ready Execution Bundle: COMPLETE
- External Artist / Image Model Handoff: COMPLETE
- Master Production Spec: COMPLETE
- Prompt Engineering Red Team: COMPLETE

### D16.4 Act-map Binding
- Character Act/Volume state binding: **30/30**
- Relic lineage Act binding: **12/12**
- Sovereign Beast Act binding: **5/5**
- Landmark Act binding: **8/8**
- Faction causal/visual binding: **14/14**
- Grand Act visual questions: **5/5**
- Existing Volume Exposure Map compatibility: **15/15**
- Episode/JIT Visual CP Resolver: COMPLETE

## 3. 문서

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

### QA / Pilot
- `docs/99_quality_control/visual-negative-and-collision-rules-v1.md`
- `docs/99_quality_control/visual-pilot-evaluation-sheet-v1.md`
- `docs/99_quality_control/visual-pilot-execution-bundle-v1.md`
- `docs/99_quality_control/visual-prompt-engineering-red-team-v1.md`

### Act / Episode Integration
- `docs/10_story_architecture/visual-asset-act-usage-matrix-v1.md`
- `docs/10_story_architecture/visual-cp-resolver-rules-v1.md`

## 4. Production Rule

각 자산은 다음 5단계로 제작한다.

1. `V0 Shape Exploration` — 흑백/무채색 구조 4안
2. `V1 Identity Exploration` — 얼굴/형태/재질 4안
3. `V2 Integrated Concept` — 대표소품·행동·환경 결합
4. `V3 Canon Variant` — 정본에 실제 존재하는 상태변형만
5. `V4 Production Sheet` — 정면/3-4면/후면/디테일/표정 또는 구조 시트

한 번에 V4로 점프하면 FAIL.

## 5. Act-map Matching Rule

액트맵·서브액트·Episode CP에서 자산 ID를 부를 때 ID만 쓰지 않는다.

필수:

`Asset ID / GA / Volume / Current State / Beat Type / 3-Second Anchor / Do Not Advance`

예:

```text
C01 / GA IV / V11 / ADDRESS-LOSS entering / V-D / 사선외투+빈 고리 / FINAL LOSS 선행 금지
```

이렇게 해야 같은 캐릭터가 375화 내내 같은 외형으로 고정되거나, 반대로 매 등장마다 새 디자인으로 드리프트하는 것을 동시에 막을 수 있다.

## 6. Lock Levels

### HARD
- 역할, 기능, 사건, 소유권, 최종상태
- 종족/문화/직업 정본
- 관계와 정보천장
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

## 7. QA 결과

- 전체 자산 Prompt Coverage: **69/69**
- 전체 자산 Act Binding: **69/69**
- Grand Acts: **5/5**
- Volumes: **15/15 existing Exposure Map compatible**
- 특정 작품/배우/캐릭터 직접 모사 실행문구: **0**
- Model-specific syntax dependency: **0**
- Canon mutation: **0**
- New power/item/faction invention: **0**
- Future Variant leakage: guarded
- Face/Body collision dangerous clusters: guarded
- Relic final-upgrade contamination: guarded
- Beast petification: guarded
- Landmark theme-park flattening: guarded
- Faction logo/color dependency: guarded
- C30 identity confirmation: guarded

## 8. Visual Pilot Gate

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
- Act-map/CP state matching PASS
- 작가의 방향 승인

외부 실행자는 `visual-pilot-execution-bundle-v1.md`를 복사해 V0 5종을 생성할 수 있다.

## 9. Final Verdict

**D16.3 Visual Production Prompt/Handoff: COMPLETE.**  
**D16.4 Act-map Visual Binding / JIT CP Resolver: COMPLETE.**

정확한 의미:

> **전체 69개 비주얼 자산은 각각 독립적인 제작 프롬프트·충돌금지·변형규칙을 가지며, 동시에 5 Grand Acts / 15 Volumes / Episode CP에서 어느 상태를 언제 호출할지 매칭되었다. 다음 단계는 Visual Pilot 실물 검증이다.**
