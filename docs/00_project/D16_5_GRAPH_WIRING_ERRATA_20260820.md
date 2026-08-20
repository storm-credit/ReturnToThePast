# D16.5 Graph Wiring Errata — 2026-08-20

Status: **ACTIVE ERRATA / ROUTING ONLY**  
Scope: Act/Volume/Subact/Episode CP/Visual Router 연결 상태  
Non-Scope: 사건·설정·인물의도·결말·원고 변경

## 1. 목적

D16.5 Obsidian/Act-map wiring 과정에서 발견된 **상태 인덱스의 오래된 문구**를 정정한다.

정본 사건을 바꾸는 문서가 아니다. Read-only hub나 오래된 상태 설명이 최신 main 생산선과 충돌할 때 이 Errata가 라우팅 상태를 바로잡는다.

## 2. V04-4C Context Pack 상태 정정

`docs/10_story_architecture/subacts/V04-4C.md`에는 아직 다음 취지의 오래된 문구가 남아 있다.

- `Context Pack 없음`
- `.agent/context-packs/episodes/ 는 E001–E025만 존재`

현재 main 기준 이 문구는 **STALE**이다.

실제 존재하는 최신 생산 자료:

- `.agent/context-packs/episodes/E089-E093-context-pack-d12.md`
- `docs/10_story_architecture/craft-manifests/E089-E093-storycraft-manifest-d12.md`
- `manuscript/quality/E089-E093-d12-preflight.md`
- `docs/10_story_architecture/detail/v04-e089-e093-d11-ensemble-overlay-v1.md`

따라서 V04-4C / E089–E093 생산 시 `Context Pack 없음` 문구를 사용하지 않는다.

## 3. Current Routing Authority

V04-4C 생산 라우팅은 다음 순서로 해석한다.

1. Canon Constitution / Amendments / Decision Log
2. D11 / D12 / D15 locks
3. E089–E093 D12 Context Pack
4. E089–E093 Storycraft Manifest
5. E089–E093 Preflight
6. `obsidian-act-subact-visual-wiring-v1.md`
7. `visual-cp-resolver-rules-v1.md`
8. `visual-asset-act-usage-matrix-v1.md`
9. V04-4C Read-only Hub

Read-only Hub가 3–8번과 충돌하면 최신 생산선이 우선한다.

## 4. Obsidian Graph Rule

향후 Obsidian에서 V04-4C 노드를 볼 때 다음 링크를 함께 연결한다.

- `V04-4C.md`
- `E089-E093-context-pack-d12.md`
- `E089-E093-storycraft-manifest-d12.md`
- `E089-E093-d12-preflight.md`
- `obsidian-act-subact-visual-wiring-v1.md`
- `visual-cp-resolver-rules-v1.md`

이렇게 하면 오래된 hub 텍스트가 단독 권위 노드처럼 보이지 않는다.

## 5. Verdict

- Canon mutation: 0
- Plot mutation: 0
- Manuscript mutation: 0
- Routing correction: 1
- Blocking inconsistency after Errata: 0

**V04-4C routing stale-state issue: CLOSED BY ERRATA.**
