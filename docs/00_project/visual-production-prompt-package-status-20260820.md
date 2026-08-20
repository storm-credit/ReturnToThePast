# Visual Production / Act Wiring / Obsidian Graph Status

Status: **D16.3 + D16.4 + D16.5 — COMPLETE / READY FOR JIT PRODUCTION**  
Date: 2026-08-20  
Base for D16.5: `main@58c2b811b2a0f4197cf5dbc24b7724f1b86e7bfc`  
Scope: Visual Production 실행 프롬프트, 모델 독립 제작명세, 검수·인수인계, Act/Volume/Subact/Episode CP 연결, Obsidian Graph-ready wiring  
Non-Scope: 사건/설정/결말/인물의도/유산 기능/신수 생태/원고 변경

## 1. 목적

D16/D16.1/D16.2의 비주얼 정체성을 실제 제작 가능한 Prompt/Handoff로 변환하고, 각 자산을 5 Grand Acts / 15 Volumes / 60 Subacts / E001–E375 생산선에서 **현재 상태로만 호출**하도록 연결한다.

D16.5는 여기에 한 단계 더해 이후 Obsidian Vault에서 다음 관계가 Graph edge로 추적되도록 만든다.

`Grand Act → Volume → Subact → Episode CP → Visual Resolver → Asset Matrix → Production Prompt`

핵심 원칙:

> 비주얼 설정집을 따로 읽어 기억해서 쓰는 것이 아니라, 현재 회차가 속한 Subact를 통해 필요한 자산 상태만 JIT로 불러온다.

## 2. 완료 범위

### D16.3 — Asset Production Prompt Coverage
- Character: **C01–C30 = 30/30**
- Relic: **R01–R12 = 12/12**
- Sovereign Beast: **B01–B05 = 5/5**
- Landmark: **L01–L08 = 8/8**
- Faction: **F01–F14 = 14/14**
- Total domain assets: **69/69**

### D16.3 — Production / QA
- Global Negative / Collision Rules: COMPLETE
- Visual Pilot Evaluation Sheet: COMPLETE
- Visual Pilot Copy-Ready Execution Bundle: COMPLETE
- External Artist / Image Model Handoff: COMPLETE
- Master Production Spec: COMPLETE
- Prompt Engineering Red Team: COMPLETE

### D16.4 — Act-map Binding
- Character Act/Volume state binding: **30/30**
- Relic lineage Act binding: **12/12**
- Sovereign Beast Act binding: **5/5**
- Landmark Act binding: **8/8**
- Faction causal/visual binding: **14/14**
- Grand Act visual questions: **5/5**
- Existing Volume Exposure Map compatibility: **15/15**
- Episode/JIT Visual CP Resolver: COMPLETE

### D16.5 — Full Act/Subact/Obsidian Wiring
- Grand Act physical hubs: **5/5**
- Volume scene-ready design nodes: **15/15**
- Subact physical hubs: **60/60**
- Episode allocation: **E001–E375 = 375/375**
- Episode gap: **0**
- Episode duplicate allocation: **0**
- Wiring Registry rows: **60/60**
- Episode Card Standard → Wiring Registry: COMPLETE
- Wiring Registry → Resolver: COMPLETE
- Resolver → D16.4 Visual Matrix: COMPLETE
- Visual Matrix → Production Prompt: COMPLETE
- Obsidian stable-ID migration contract: COMPLETE
- D16.5 Graph QA: PASS

## 3. 핵심 문서

### Project / Status / Errata
- `docs/00_project/visual-production-prompt-package-status-20260820.md`
- `docs/00_project/D16_5_GRAPH_WIRING_ERRATA_20260820.md`

### Production Master / Handoff
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

### Visual QA / Pilot
- `docs/99_quality_control/visual-negative-and-collision-rules-v1.md`
- `docs/99_quality_control/visual-pilot-evaluation-sheet-v1.md`
- `docs/99_quality_control/visual-pilot-execution-bundle-v1.md`
- `docs/99_quality_control/visual-prompt-engineering-red-team-v1.md`
- `docs/99_quality_control/d16-5-obsidian-graph-wiring-qa-v1.md`

### Act / Episode / Graph Integration
- `docs/10_story_architecture/visual-asset-act-usage-matrix-v1.md`
- `docs/10_story_architecture/visual-cp-resolver-rules-v1.md`
- `docs/10_story_architecture/obsidian-act-subact-visual-wiring-v1.md`
- `docs/10_story_architecture/episode-card-composition-standard-v1.md`

## 4. Production Rule

각 자산의 이미지 제작은 다음 5단계다.

1. `V0 Shape Exploration` — 흑백/무채색 구조 4안
2. `V1 Identity Exploration` — 얼굴/형태/재질 4안
3. `V2 Integrated Concept` — 대표소품·행동·환경 결합
4. `V3 Canon Variant` — 정본에 실제 존재하는 상태변형만
5. `V4 Production Sheet` — 정면/3-4면/후면/디테일/표정 또는 구조 시트

한 번에 V4로 점프하면 FAIL.

## 5. Story Production Routing Rule

E089 이후 회차 생산은 다음 순서를 강제한다.

`Episode → Grand Act → Volume → Subact → Scene Assets → Visual Matrix → Production Prompt`

실제 사용 필드:

`Asset ID / GA / Volume / Subact / Current State / Beat Type / 3-Second Anchor / Do Not Advance`

예:

```text
C02 / GA II / V04 / 4C / MULTI-ERA EVIDENCE / E-V / 세로 문서갑+겹판 / GA V PRIVATE LOSS 선행 금지
```

이 구조로 다음을 동시에 막는다.

- 375화 내내 같은 외형으로 고정
- 매 등장마다 새 디자인으로 드리프트
- 미래 Variant 선행노출
- 파괴/분해된 유산 원상복귀
- 사망한 인물의 현재형 Variant
- Graph link를 등장 허가로 오해하는 문제

## 6. Obsidian Graph Contract

현재 Markdown 파일명과 기존 링크를 유지한다. Obsidian Graph는 기존 Markdown 링크도 edge로 인식한다.

향후 Vault migration에서 권장 Properties:

```yaml
node_type: act|volume|subact|episode|character|relic|beast|landmark|faction|prompt
node_id: GA-II|V04|V04-4C|E089|C02|R05|B05|L06|F13
parent_act: GA-II
parent_volume: V04
parent_subact: V04-4C
visual_router: visual-cp-resolver-rules-v1
visual_matrix: visual-asset-act-usage-matrix-v1
```

Rules:

- `node_id`는 stable.
- Obsidian 때문에 파일명을 임의 개명하지 않는다.
- Properties는 정본 사실을 중복 저장하지 않고 관계/필터 메타데이터 중심으로 쓴다.
- wiki-link 전환은 선택사항이며 ghost node를 만들면 FAIL.
- Graph convenience는 Story Architecture/Canon authority를 넘지 못한다.

## 7. Stale Routing Errata

`docs/10_story_architecture/subacts/V04-4C.md`의 오래된 `Context Pack 없음` 문구는 현재 상태와 불일치한다.

실제 main 생산선에는 E089–E093 D12 Context Pack / Storycraft Manifest / Preflight / Ensemble Overlay가 존재한다.

따라서 `D16_5_GRAPH_WIRING_ERRATA_20260820.md`가 해당 read-only hub의 오래된 라우팅 설명을 대체한다.

Canon/plot conflict가 아니라 **routing/index staleness**로 처리하며 blocking issue는 0이다.

## 8. QA 결과

- 전체 자산 Prompt Coverage: **69/69**
- 전체 자산 Act Binding: **69/69**
- Grand Acts: **5/5**
- Volumes: **15/15**
- Subacts: **60/60**
- Episodes: **375/375**
- 특정 작품/배우/캐릭터 직접 모사 실행문구: **0**
- Model-specific syntax dependency: **0**
- Canon mutation: **0**
- New power/item/faction invention: **0**
- Manuscript change from D16.5: **0**
- Future Variant leakage: guarded
- Face/Body collision: guarded
- Relic final-upgrade contamination: guarded
- Beast petification: guarded
- C30 identity confirmation: guarded
- Obsidian node/edge migration safety: guarded

## 9. Visual Pilot Gate

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
- Act/Subact/CP state matching PASS
- 작가의 방향 승인

## 10. Final Verdict

**D16.3 Visual Production Prompt/Handoff: COMPLETE.**  
**D16.4 Act-map Visual Binding / JIT CP Resolver: COMPLETE.**  
**D16.5 5-Act / 15-Volume / 60-Subact / Obsidian Graph Wiring: COMPLETE.**

정확한 의미:

> 전체 69개 비주얼 자산은 독립 제작 프롬프트와 상태 규칙을 가지며, 실제 375화 집필에서는 현재 Grand Act → Volume → Subact를 통과한 뒤 해당 시점 상태만 JIT로 호출한다. 저장소를 향후 Obsidian Vault로 가져갈 때도 이 관계망을 stable node/edge graph로 확장할 수 있다.

다음 비주얼 단계는 **Visual Pilot 실물 검증**이며, 다음 소설 생산 단계는 **E089부터 이 Wiring을 실제 Episode CP에 적용하는 것**이다.
