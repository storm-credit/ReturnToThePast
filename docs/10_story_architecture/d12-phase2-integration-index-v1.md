# D12 Phase 2 Integration Index v1

Status: ACTIVE ROUTING INDEX  
Owner: A12 Architecture / A13 Continuity / A20 Storycraft / A21 Context Compiler  
Authority: `docs/00_project/D12_ENSEMBLE_RESOLUTION_AMENDMENT_20260820.md`  
Purpose: D11 이후 해결된 대표·POV·권리절차·V10→V12 회수선을 집필 전 필수 읽기 묶음으로 고정한다.

## 1. V4 E089–E093 필수 읽기

1. `docs/10_story_architecture/detail/v04-scene-ready-design-v1.md`
2. `docs/00_project/D11_STORY_ARCHITECTURE_AMENDMENT_20260820.md`
3. `docs/00_project/D12_ENSEMBLE_RESOLUTION_AMENDMENT_20260820.md`
4. `docs/10_story_architecture/detail/v04-e089-e093-d11-ensemble-overlay-v1.md`
5. `docs/08_institutions/v04-witness-zone-consent-protocol-v1.md`
6. `docs/10_story_architecture/parallel-plot-and-pov-governance-v1.md`
7. `docs/09_collection/sovereign-beast-encyclopedia-b01-b05-v1.md` B05

### Gate
- E089 = 리아 세른 P1.
- 나하 아노르는 E089 주소상실 주민 대표 기능 사용 가능.
- 백지사슴은 보조증거만.
- E092는 단일 과반투표가 아님.
- E093에서 옛 공권력은 복귀하지 않음.
- 외부세력은 내부 선택을 기다리지 않고 움직임.

---

## 2. V12 12A–12B 필수 읽기

1. `docs/10_story_architecture/detail/v12-scene-ready-design-v1.md`
2. `docs/03_systems/cross-era-council-protocol-v1.md`
3. `docs/10_story_architecture/detail/v12-era-o-representative-resolution-v1.md`
4. `docs/10_story_architecture/detail/v12-council-continuity-resolution-v1.md`
5. `docs/05_characters/supporting-cast-dossiers-c21-c30-v2.md` C21
6. `docs/10_story_architecture/detail/v10-scene-ready-design-v1.md` E239/E242/E248

### Representative Lock
- Era O: C21 레오르 세르바.
- Era N: C03 아이리스 네르.
- Future/F1: C04 마르칸 베르.

### Gate
- C05 오르바드 카르센 생환 금지.
- V10 상호인지는 유지.
- V12는 첫 물리적 공동출석·공동 법적절차.
- E239 실패 협상장 주소는 V12에서 회수.
- 대표 3명과 7개 운영권은 별개.
- 레오르가 미래에서 본 기억은 삭제하지 않음.

---

## 3. D12가 닫은 공백

| 공백 | 상태 |
|---|---|
| V12 Era O 대표 | CLOSED — C21 레오르 세르바 |
| C21 Era O 출신과 V15 핵심권 정합 | CLOSED — 제한 호송 + Era O 후속 정치 |
| V10 E248 vs V12 공식인지 반복 | CLOSED — 존재인지 vs 공동절차 |
| E239 실패 협상장 사용처 | CLOSED — V12 주소 원형 |
| E089 POV | CLOSED at design — Ria P1 |
| E089 나하 사용범위 | CLOSED — 주소상실 주민 조직 |
| E089 B05 진실판독기 위험 | CLOSED — support only |
| E092 단순 다수결 | CLOSED — rights-bucket consent |

---

## 4. 남은 Nonblocking Open

1. V4 군부 사령관 고유명 — 1회성 기능인물 유지 가능.
2. V14 강제덮어쓰기 정치 지도자 — V14 준비단계에서 반복 필요성 확인 후 결정.

둘 다 현재 Grand Act/Volume/Subact 설계를 막지 않는다.

---

## 5. Production Safety

설계 PASS와 원고 생산 가능 상태는 다르다.

현재 다음을 별도로 처리해야 한다.

- 최신 main 기준 생산 상태장부 재동기화.
- D11/D12 이전 E089–E093 PR #125를 병합하지 않음.
- #114–#118은 최신 정본 기준 재검증 없이 직접 병합하지 않음.
- E089 이후 집필 시 새 Context Pack / Craft Manifest에서 D11·D12를 반드시 포함.

---

## 6. Red Team

필수:
`docs/99_quality_control/d12-phase2-red-team-v1.md`

D12 Phase 2 결과:
- S0 = 0
- Story-architecture blocking S1 = 0
- Operational S1 = 2
- Nonblocking design OPEN = 2

---

## 7. Reader-Facing Target

V4에서는:

> 과거를 되찾고 싶은 사람, 현재 가족을 지키려는 사람, 방어선을 지켜야 하는 군인, 사라지기 전에 자기 존재를 증언해야 하는 사람이 같은 시한 안에서 충돌한다.

V12에서는:

> 서로 다른 시대가 존재한다는 사실을 아는 단계를 넘어, 각 시대에서 실제 사람을 살려야 하는 책임자들이 같은 자리에서 서로 양립할 수 없는 최소생존선을 제출한다.

이 두 구조가 연결되어야 D11의 `에이든은 중심이지만 세계의 유일한 스위치가 아니다`가 실제 장편 서사로 구현된다.
