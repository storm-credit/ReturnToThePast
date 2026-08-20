# D16.5 Obsidian Graph Wiring QA v1

Status: **D16.5 GRAPH / ROUTING QA — PASS**  
Date: 2026-08-20  
Scope: 5 Grand Acts · 15 Volumes · 60 Subacts · E001–E375 · Visual Asset Router  
Non-Scope: 사건/설정/결말/원고/인물의도 변경

## 1. Executive Verdict

D16.5는 기존 Story Architecture를 다시 쓰지 않고, 그 위에 **Act → Volume → Subact → Episode → Visual Asset** 생산 경로를 강제하는 Graph/Routing Overlay를 추가한다.

검증 결과:

- Grand Act Hub: **5/5 PASS**
- Volume Scene-Ready Design: **15/15 PASS**
- Subact Hub: **60/60 PASS**
- Episode Range: **E001–E375 full coverage PASS**
- Episode Card → Wiring Registry: **PASS**
- Wiring Registry → Resolver: **PASS**
- Resolver → Visual Matrix: **PASS**
- Visual Matrix domain assets: **69/69 preserved**
- Production Prompt routing: **PASS**
- Canon mutation: **0**
- Manuscript mutation: **0**

## 2. Physical Node Audit

### Grand Acts

Existing architecture hubs:

- `acts/GA-I.md`
- `acts/GA-II.md`
- `acts/GA-III.md`
- `acts/GA-IV.md`
- `acts/GA-V.md`

Result: **5/5**.

### Volumes

Existing scene-ready designs:

- `detail/v01-scene-ready-design-v1.md`
- `detail/v02-scene-ready-design-v1.md`
- `detail/v03-scene-ready-design-v1.md`
- `detail/v04-scene-ready-design-v1.md`
- `detail/v05-scene-ready-design-v1.md`
- `detail/v06-scene-ready-design-v1.md`
- `detail/v07-scene-ready-design-v1.md`
- `detail/v08-scene-ready-design-v1.md`
- `detail/v09-scene-ready-design-v1.md`
- `detail/v10-scene-ready-design-v1.md`
- `detail/v11-scene-ready-design-v1.md`
- `detail/v12-scene-ready-design-v1.md`
- `detail/v13-scene-ready-design-v1.md`
- `detail/v14-scene-ready-design-v1.md`
- `detail/v15-scene-ready-design-v1.md`

Result: **15/15**.

### Subacts

Physical hub sequence exists continuously from:

- `subacts/V01-1A.md`

through:

- `subacts/V15-15D.md`

Each of 15 Volumes has A/B/C/D four Subacts.

Result: `15 × 4 = 60/60`.

## 3. Episode Range Integrity

Each Volume uses four Subact ranges in the established 25-episode distribution:

- A = 6 episodes
- B = 6 episodes
- C = 6 episodes
- D = 7 episodes

Examples:

- V01: E001–006 / E007–012 / E013–018 / E019–025
- V04: E076–081 / E082–087 / E088–093 / E094–100
- V15: E351–356 / E357–362 / E363–368 / E369–375

The Wiring Registry follows this pattern for all 15 Volumes.

Result:

- Gap: **0**
- Duplicate episode allocation: **0**
- Out-of-range episode: **0**
- Full series coverage: **375/375**

## 4. Mandatory Routing Audit

Required production route:

`Grand Act → Volume → Subact → Episode → Scene Assets → Visual Matrix → Production Prompt`

### Episode Card Standard

`episode-card-composition-standard-v1.md` now requires:

- Grand Act
- Volume
- Subact
- Architecture Hub
- Primary Visual Asset
- Current Visual State
- Do Not Advance
- Visual Resolver Route

E001–E088 are not retroactively rewritten only for these fields; E089+ uses them JIT.

Verdict: **PASS**.

### Visual Resolver

`visual-cp-resolver-rules-v1.md` now forbids Act/Volume → Asset direct jumps.

Mandatory resolution order:

`Episode → Wiring Registry → Grand Act → Volume → Subact → Scene Assets → Visual Matrix → Production Prompt`

Verdict: **PASS**.

### Wiring Registry

`obsidian-act-subact-visual-wiring-v1.md` contains one row for every Subact and links:

- Act Hub
- Volume Design
- Subact Hub
- Visual Resolver
- Visual Matrix

Verdict: **60/60 PASS**.

## 5. Visual Asset Preservation Audit

D16.5 does not replace D16.4.

D16.4 remains authority for current visual state/variant timing:

- Character: C01–C30 = 30
- Relic: R01–R12 = 12
- Sovereign Beast: B01–B05 = 5
- Landmark: L01–L08 = 8
- Faction: F01–F14 = 14

Total: **69/69**.

D16.5 only determines **which Act/Volume/Subact context is used before those asset states are resolved**.

Verdict: **PASS**.

## 6. Graph Edge Model

Target Obsidian graph path:

`GA Hub ↔ Volume Design ↔ Subact Hub ↔ Wiring Registry ↔ Episode CP ↔ Visual Resolver ↔ Asset Matrix ↔ Production Prompt`

Existing Character/Institution/Asset links inside Subact hubs remain additional graph edges.

Important:

- Graph edge existence does not authorize a character/item to appear in a scene.
- Scene/Architecture authority remains higher than Graph convenience.
- Prompt documents never become Canon authority.

## 7. Obsidian Properties Migration Contract

Current D16.5 keeps repository filenames stable.

Later Obsidian migration may add:

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

1. `node_id` must be stable.
2. File rename is not required for graph migration.
3. Properties must not duplicate Canon facts already maintained elsewhere.
4. Wiki-link conversion is optional; existing Markdown links are valid graph edges.
5. Unresolved wiki-links that create ghost nodes are FAIL.
6. Tags are for filtering, not authority.

## 8. Stale-State Audit

Detected issue:

`subacts/V04-4C.md` still contains old text saying E089–E093 Context Pack does not exist.

Actual repository contains:

- `.agent/context-packs/episodes/E089-E093-context-pack-d12.md`
- `docs/10_story_architecture/craft-manifests/E089-E093-storycraft-manifest-d12.md`
- `manuscript/quality/E089-E093-d12-preflight.md`
- `docs/10_story_architecture/detail/v04-e089-e093-d11-ensemble-overlay-v1.md`

Resolution:

`docs/00_project/D16_5_GRAPH_WIRING_ERRATA_20260820.md` supersedes this stale routing statement.

This is a **routing/index staleness issue**, not a Canon/plot conflict.

Blocking status after Errata: **0**.

## 9. Failure Conditions for Future Production

FAIL if:

- Episode does not resolve to exactly one Subact.
- Act/Volume bypasses Subact and selects an asset directly.
- Visual Matrix future Variant is used early.
- a graph link is mistaken for permission to introduce an asset.
- destroyed/disassembled/final-state relic resets.
- dead character receives a current-time live Variant.
- C30 graph proximity to C01 is used as identity proof.
- B05 is used as a truth judge.
- Obsidian migration renames files and silently breaks existing links.
- Properties begin duplicating and contradicting Canon ledgers.

## 10. Final QA Verdict

**D16.5 ACT/SUBACT/OBSIDIAN GRAPH WIRING: PASS.**

Production meaning:

> E089 이후 회차를 만들 때 Grand Act와 Volume만 보고 설정을 가져오는 것이 아니라, 반드시 현재 Subact를 통과해 장면에 실제 존재하는 자산을 찾고, 그 다음 D16.4 Visual Matrix에서 현재 상태를 선택한다.

Obsidian meaning:

> 현재 Markdown 저장소 구조를 그대로 Vault로 가져가도 Act/Volume/Subact/Visual Router 연결을 그래프에서 추적할 수 있으며, 이후 stable `node_id` Properties를 추가하면 필터 가능한 지식 그래프로 확장할 수 있다.
