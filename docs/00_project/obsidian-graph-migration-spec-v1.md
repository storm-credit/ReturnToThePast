# Obsidian Graph Migration Spec v1

Status: **DESIGN FREEZE FOR FUTURE VAULT MIGRATION**  
Date: 2026-08-20  
Scope: ReturnToThePast Markdown repository → future Obsidian knowledge graph  
Non-Scope: 지금 당장 375개 Episode node 파일 생성, Canon 재작성, 파일명 대규모 변경

## 1. 목표

현재 GitHub Markdown 구조를 유지하면서, 향후 Obsidian에서 다음 계층과 교차관계를 추적할 수 있게 한다.

`Series → Grand Act → Volume → Subact → Episode`

그리고 서사 노드에서 다음 도메인 노드로 연결한다.

`Character / Faction / Institution / Relic / Beast / Landmark / Mystery / Loss / Visual Prompt`

핵심 목표는 예쁜 Graph가 아니라 **집필 중 현재 회차에 필요한 정본과 상태를 역추적할 수 있는 작업 그래프**다.

## 2. 기존 기반

저장소에는 이미 GitHub/Obsidian 공용 Markdown 링크 정리 이력이 있으며, 기존 허브와 링크를 최대한 유지한다.

D16.5는 추가로 다음 생산 라우팅을 고정한다.

`Grand Act → Volume → Subact → Episode CP → Visual Resolver → Asset Matrix → Production Prompt`

관련 문서:

- [D16.5 Wiring Registry](../10_story_architecture/obsidian-act-subact-visual-wiring-v1.md)
- [Episode Card Standard](../10_story_architecture/episode-card-composition-standard-v1.md)
- [Visual CP Resolver](../10_story_architecture/visual-cp-resolver-rules-v1.md)
- [Visual Asset Matrix](../10_story_architecture/visual-asset-act-usage-matrix-v1.md)
- [D16.5 QA](../99_quality_control/d16-5-obsidian-graph-wiring-qa-v1.md)

## 3. Graph는 정본이 아니다

Obsidian Graph / Properties / Tags는 탐색과 생산을 돕는 메타데이터다.

Authority는 기존 프로젝트 위계를 따른다.

- Canon / Amendment / Errata / Decision Log
- State Ledger
- Domain Bible
- Story Architecture
- Context Pack / Craft Manifest
- Manuscript
- Graph metadata

Graph에서 가까이 붙어 보인다는 이유로 관계·정체·원인을 확정하지 않는다.

특히:

- C30과 C01이 graph-neighbor라도 동일인 증거가 아니다.
- B05가 어떤 인물 노드와 많이 연결되어도 truth judge가 아니다.
- Production Prompt는 Canon보다 낮다.

## 4. Node Classes

### Tier A — 반드시 독립 파일 노드

현재 또는 장기적으로 독립 탐색 가치가 높은 노드다.

- Series / Project MOC: 1
- Grand Act: 5
- Volume: 15
- Subact: 60
- Major Character: C01–C30 = 30
- Episode manuscript: 실제 작성된 회차 파일
- Canon/Amendment/Decision/State docs

### Tier B — Full IP Graph 단계에서 독립 Hub 권장

현재 일부는 집합 문서의 행으로 존재한다. Obsidian Full Graph 전환 시 read-only Hub로 분리할 수 있다.

- Relic R01–R12 = 12
- Beast B01–B05 = 5
- Landmark L01–L08 = 8
- Faction F01–F14 = 14
- Mystery Mxx
- Permanent Loss / stateful high-value assets

Hub는 새 Canon이 아니라 **원본 경로를 모으는 read-only index**다.

### Tier C — 기본적으로 별도 Node를 만들지 않음

- 한 장면용 소품
- 일회성 직책
- 모든 대사 화자
- Production prompt의 세부 옵션 4안
- 한 번만 쓰이는 시각 디테일

Graph node 수를 늘리기 위해 설정을 세분화하지 않는다.

## 5. Episode Node Policy

### 현재

- E001–E088 실제 manuscript 파일은 이미 독립 파일이므로 Graph node가 될 수 있다.
- E089+는 실제 원고/CP가 생길 때 node가 생긴다.
- Episode registry의 표 행은 Obsidian Graph에서 독립 node가 아니다.

### 향후 Full 375 Graph가 필요할 때

375개 빈 원고 파일을 미리 만들지 않는다.

대신 필요 시 lightweight episode hub를 별도 생성한다.

예:

```text
docs/10_story_architecture/episodes/E089.md
```

내용은 최소화한다.

- Episode ID
- Act / Volume / Subact
- D6 registry link
- Context Pack link
- manuscript link if exists
- Primary/Secondary asset links
- State mutation link

이 Hub는 원고를 복제하지 않는다.

## 6. Stable Properties Schema

Properties는 사실 본문을 복제하지 않고 **식별·관계·필터 정보**만 가진다.

### Common

```yaml
node_type: subact
node_id: V04-4C
status: active
canon_level: read-only-index
```

### Narrative hierarchy

```yaml
parent_act: GA-II
parent_volume: V04
parent_subact: V04-4C
episode_start: E088
episode_end: E093
```

### Asset

```yaml
node_type: character
node_id: C02
asset_type: character
visual_router: visual-cp-resolver-rules-v1
visual_matrix: visual-asset-act-usage-matrix-v1
```

### Production

```yaml
production_status: prompt-ready
pilot_status: not-run
```

## 7. Stable IDs

IDs are more stable than filenames and display titles.

Recommended:

- `SERIES-RTTP`
- `GA-I` … `GA-V`
- `V01` … `V15`
- `V01-1A` … `V15-15D`
- `E001` … `E375`
- `C01` … `C30`
- `R01` … `R12`
- `B01` … `B05`
- `L01` … `L08`
- `F01` … `F14`

Display name may change; node_id does not.

## 8. Link Direction Policy

Obsidian Graph는 링크 하나만 있어도 두 파일 사이 edge를 보여 주며 backlinks로 역방향 탐색이 가능하다.

따라서 모든 관계를 두 파일에 중복 작성하지 않는다.

### 권장 정방향

- Act → Volume / Subact
- Volume → Subact
- Subact → Character / Asset / Location / Faction
- Episode → Subact / Primary Asset / CP / State Mutation
- Character/Asset Hub → Canon source / Production Prompt
- Production Prompt → Negative/Collision Rules

### 역방향

기본적으로 Obsidian backlinks를 사용한다.

명시적 역링크는 해당 파일을 독립적으로 열었을 때 상위 문맥이 반드시 필요한 경우만 둔다.

## 9. MOC Policy

Graph 전체를 한 화면에 보여 주려 하지 않는다.

추천 MOC:

1. `Story Architecture MOC`
2. `Character MOC`
3. `World / Institution MOC`
4. `Relic / Beast / Collection MOC`
5. `Visual Production MOC`
6. `Current Production MOC`

각 MOC는 링크 집합이며 Canon을 새로 요약하지 않는다.

## 10. Graph Filters / Groups

Obsidian에서 추천 그룹 필터:

- `node_type:act`
- `node_type:volume`
- `node_type:subact`
- `node_type:episode`
- `node_type:character`
- `asset_type:relic`
- `asset_type:beast`
- `node_type:faction`
- `production_status:prompt-ready`
- `pilot_status:not-run`

Global Graph보다 Local Graph를 우선한다.

예:

`E089` Local Graph depth 2를 열면 이상적인 범위는:

- V04-4C
- GA-II / V04
- C02 리아
- C01 에이든
- C09 나하
- 관련 current evidence / faction nodes
- D12 CP / Craft Manifest / Preflight
- Visual Resolver / current prompt route

## 11. Anti-Explosion Rules

Graph가 커질수록 다음을 금지한다.

- 모든 명사를 node로 만들기
- 태그와 Properties와 링크에 같은 사실 3중 저장
- 동일 인물의 시대별 Variant를 별도 Character node로 무조건 분리
- `C01-F0`, `C01-GA2`, `C01-Final`을 각각 인물 노드로 만드는 방식
- 4개 prompt option을 각각 node로 만들기
- 링크가 많아 보이게 의미 없는 cross-link 추가

Variant는 기본적으로 **같은 Asset node + state property/ledger**로 관리한다.

예외: 다른 에이든 C08처럼 Canon상 독립 캐릭터 ID가 이미 있는 경우.

## 12. Naming / Alias Policy

파일명은 현재 GitHub 경로 안정성을 우선한다.

Obsidian aliases는 검색 편의를 위해 사용할 수 있다.

예:

```yaml
aliases:
  - 에이든 로엔
  - Aiden Roen
```

하지만 alias로 서로 다른 Canon 인물을 합치지 않는다.

## 13. Wiki-link Migration Policy

기존 Markdown links가 GitHub와 Obsidian 양쪽에서 작동하므로 전면 `[[wiki-link]]` 변환은 필요하지 않다.

Wiki-link를 쓸 경우:

- 실제 파일이 존재하는 경우만 사용
- 같은 basename 파일이 여러 폴더에 있으면 path 포함
- ghost node 0 유지
- GitHub 가독성을 해치지 않도록 핵심 네비게이션은 Markdown link 유지 가능

## 14. Production Workflow in Obsidian

E089 이후 권장 작업:

1. `Current Production MOC`에서 E089 선택
2. E089 → V04-4C 확인
3. V04-4C → D12 CP/Craft/Preflight 확인
4. D16.5 Wiring → 현재 scene assets 후보 확인
5. D16.4 Matrix → current visual state 결정
6. 필요한 경우 Prompt Pack 이동
7. 초고 작성
8. State Mutation 기록
9. QA/Human Prose Audit
10. author review

## 15. Migration Phases

### O1 — Current Repository Graph-ready — **DONE BY D16.5**
- 기존 Markdown links 유지
- Act/Volume/Subact wiring
- Resolver routing
- stable property schema 설계

### O2 — Properties Injection — FUTURE
- Act 5
- Volume 15
- Subact 60
- Character hubs 30
- high-value domain hubs

자동 삽입 전 sample 5개를 먼저 검증한다.

### O3 — Asset Hub Expansion — FUTURE
- R12 / B5 / L8 / F14 read-only hubs
- 원본 문서 중복 금지

### O4 — Episode Graph Expansion — FUTURE / JIT
- 실제 집필 회차 우선
- 필요할 때 lightweight episode hub 생성
- 빈 375개 note 선생성 금지

### O5 — Views / Filters / Canvas — FUTURE
- authoring view
- continuity view
- visual production view
- mystery/loss view

## 16. Migration QA

PASS 조건:

- broken link 0
- ghost wiki node 0
- duplicate node_id 0
- one Episode → one Subact
- one Subact → one Volume / one Act
- Canon fact duplication 최소
- current-state source가 하나로 추적됨
- Graph만 보고 미래 Variant가 현재처럼 오해되지 않음

## 17. Final Decision

**현재 저장소는 D16.5 기준 Graph-ready로 설계한다.**

실제 Obsidian migration은 파일 재배치가 아니라:

`기존 링크 보존 + stable node_id Properties + 선택적 lightweight Hub + MOC/Filter`

방식으로 진행한다.

이 구조는 GitHub 작업성과 Obsidian 탐색성을 동시에 유지하며, 375화 장기 집필에서 Graph가 정본을 대체하지 않고 **정본으로 가는 길을 보여 주는 탐색 레이어**가 되도록 한다.
