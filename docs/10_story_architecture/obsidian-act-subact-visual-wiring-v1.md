# Obsidian Act × Subact × Visual Wiring Registry v1

Status: **D16.5 — FULL ACT/SUBACT WIRING OVERLAY**  
Date: 2026-08-20  
Scope: 5 Grand Acts · 15 Volumes · 60 Subacts · E001–E375  
Rule: 이 문서는 정본을 변경하지 않는 생산/그래프 라우팅 레이어다.

## 1. 목적

다음 경로를 단일 규칙으로 연결한다.

`Grand Act → Volume → Subact → Episode Card/Context Pack → Visual CP Resolver → Asset Act Matrix → Production Prompt`

Obsidian에서는 기존 Markdown 링크도 Graph edge로 인식하므로, 정본 문서를 위키링크 전용으로 재작성하지 않는다.

## 2. Mandatory Router

- [Episode Card Composition Standard](episode-card-composition-standard-v1.md)
- [Visual CP Resolver](visual-cp-resolver-rules-v1.md)
- [Visual Asset × Act Usage Matrix](visual-asset-act-usage-matrix-v1.md)
- [Collectibility Exposure & Variant Map](collectibility-exposure-and-variant-map-v1.md)

회차 제작 시 순서:

1. Episode ID로 Volume/Subact를 확정한다.
2. 아래 Wiring Registry의 Act/Volume/Subact 허브를 연다.
3. 해당 Subact에 실제 존재하는 자산만 후보로 수집한다.
4. Visual CP Resolver가 현재 Act/Volume 상태를 Matrix에서 선택한다.
5. `Primary 1 / Secondary 0–2 / Do-Not-Advance`를 Episode CP에 넣는다.
6. 실제 이미지가 필요할 때만 Production Prompt로 이동한다.

## 3. Obsidian Node Properties

향후 Obsidian properties를 붙일 때 아래 키를 사용한다.

```yaml
node_type: act|volume|subact|episode|asset|prompt
node_id: GA-II|V04|V04-4C|E089|C02|PROMPT-C02
parent_act: GA-II
parent_volume: V04
parent_subact: V04-4C
visual_router: visual-cp-resolver-rules-v1
visual_matrix: visual-asset-act-usage-matrix-v1
```

정본 문서에 properties를 일괄 삽입하는 것은 별도 Obsidian migration 단계에서 한다. 현재는 파일 경로와 링크를 안정적으로 유지한다.

## 4. 60-Subact Wiring Table

| Act | Volume | Subact | Episodes | Architecture Hub | Visual Route |
|---|---|---|---:|---|---|
| [GA-I](acts/GA-I.md) | [V01](detail/v01-scene-ready-design-v1.md) | [1A](subacts/V01-1A.md) | E001–E006 | `V01-1A` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-I](acts/GA-I.md) | [V01](detail/v01-scene-ready-design-v1.md) | [1B](subacts/V01-1B.md) | E007–E012 | `V01-1B` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-I](acts/GA-I.md) | [V01](detail/v01-scene-ready-design-v1.md) | [1C](subacts/V01-1C.md) | E013–E018 | `V01-1C` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-I](acts/GA-I.md) | [V01](detail/v01-scene-ready-design-v1.md) | [1D](subacts/V01-1D.md) | E019–E025 | `V01-1D` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-I](acts/GA-I.md) | [V02](detail/v02-scene-ready-design-v1.md) | [2A](subacts/V02-2A.md) | E026–E031 | `V02-2A` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-I](acts/GA-I.md) | [V02](detail/v02-scene-ready-design-v1.md) | [2B](subacts/V02-2B.md) | E032–E037 | `V02-2B` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-I](acts/GA-I.md) | [V02](detail/v02-scene-ready-design-v1.md) | [2C](subacts/V02-2C.md) | E038–E043 | `V02-2C` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-I](acts/GA-I.md) | [V02](detail/v02-scene-ready-design-v1.md) | [2D](subacts/V02-2D.md) | E044–E050 | `V02-2D` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-I](acts/GA-I.md) | [V03](detail/v03-scene-ready-design-v1.md) | [3A](subacts/V03-3A.md) | E051–E056 | `V03-3A` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-I](acts/GA-I.md) | [V03](detail/v03-scene-ready-design-v1.md) | [3B](subacts/V03-3B.md) | E057–E062 | `V03-3B` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-I](acts/GA-I.md) | [V03](detail/v03-scene-ready-design-v1.md) | [3C](subacts/V03-3C.md) | E063–E068 | `V03-3C` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-I](acts/GA-I.md) | [V03](detail/v03-scene-ready-design-v1.md) | [3D](subacts/V03-3D.md) | E069–E075 | `V03-3D` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-II](acts/GA-II.md) | [V04](detail/v04-scene-ready-design-v1.md) | [4A](subacts/V04-4A.md) | E076–E081 | `V04-4A` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-II](acts/GA-II.md) | [V04](detail/v04-scene-ready-design-v1.md) | [4B](subacts/V04-4B.md) | E082–E087 | `V04-4B` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-II](acts/GA-II.md) | [V04](detail/v04-scene-ready-design-v1.md) | [4C](subacts/V04-4C.md) | E088–E093 | `V04-4C` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-II](acts/GA-II.md) | [V04](detail/v04-scene-ready-design-v1.md) | [4D](subacts/V04-4D.md) | E094–E100 | `V04-4D` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-II](acts/GA-II.md) | [V05](detail/v05-scene-ready-design-v1.md) | [5A](subacts/V05-5A.md) | E101–E106 | `V05-5A` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-II](acts/GA-II.md) | [V05](detail/v05-scene-ready-design-v1.md) | [5B](subacts/V05-5B.md) | E107–E112 | `V05-5B` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-II](acts/GA-II.md) | [V05](detail/v05-scene-ready-design-v1.md) | [5C](subacts/V05-5C.md) | E113–E118 | `V05-5C` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-II](acts/GA-II.md) | [V05](detail/v05-scene-ready-design-v1.md) | [5D](subacts/V05-5D.md) | E119–E125 | `V05-5D` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-II](acts/GA-II.md) | [V06](detail/v06-scene-ready-design-v1.md) | [6A](subacts/V06-6A.md) | E126–E131 | `V06-6A` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-II](acts/GA-II.md) | [V06](detail/v06-scene-ready-design-v1.md) | [6B](subacts/V06-6B.md) | E132–E137 | `V06-6B` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-II](acts/GA-II.md) | [V06](detail/v06-scene-ready-design-v1.md) | [6C](subacts/V06-6C.md) | E138–E143 | `V06-6C` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-II](acts/GA-II.md) | [V06](detail/v06-scene-ready-design-v1.md) | [6D](subacts/V06-6D.md) | E144–E150 | `V06-6D` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-III](acts/GA-III.md) | [V07](detail/v07-scene-ready-design-v1.md) | [7A](subacts/V07-7A.md) | E151–E156 | `V07-7A` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-III](acts/GA-III.md) | [V07](detail/v07-scene-ready-design-v1.md) | [7B](subacts/V07-7B.md) | E157–E162 | `V07-7B` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-III](acts/GA-III.md) | [V07](detail/v07-scene-ready-design-v1.md) | [7C](subacts/V07-7C.md) | E163–E168 | `V07-7C` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-III](acts/GA-III.md) | [V07](detail/v07-scene-ready-design-v1.md) | [7D](subacts/V07-7D.md) | E169–E175 | `V07-7D` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-III](acts/GA-III.md) | [V08](detail/v08-scene-ready-design-v1.md) | [8A](subacts/V08-8A.md) | E176–E181 | `V08-8A` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-III](acts/GA-III.md) | [V08](detail/v08-scene-ready-design-v1.md) | [8B](subacts/V08-8B.md) | E182–E187 | `V08-8B` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-III](acts/GA-III.md) | [V08](detail/v08-scene-ready-design-v1.md) | [8C](subacts/V08-8C.md) | E188–E193 | `V08-8C` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-III](acts/GA-III.md) | [V08](detail/v08-scene-ready-design-v1.md) | [8D](subacts/V08-8D.md) | E194–E200 | `V08-8D` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-III](acts/GA-III.md) | [V09](detail/v09-scene-ready-design-v1.md) | [9A](subacts/V09-9A.md) | E201–E206 | `V09-9A` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-III](acts/GA-III.md) | [V09](detail/v09-scene-ready-design-v1.md) | [9B](subacts/V09-9B.md) | E207–E212 | `V09-9B` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-III](acts/GA-III.md) | [V09](detail/v09-scene-ready-design-v1.md) | [9C](subacts/V09-9C.md) | E213–E218 | `V09-9C` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-III](acts/GA-III.md) | [V09](detail/v09-scene-ready-design-v1.md) | [9D](subacts/V09-9D.md) | E219–E225 | `V09-9D` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-IV](acts/GA-IV.md) | [V10](detail/v10-scene-ready-design-v1.md) | [10A](subacts/V10-10A.md) | E226–E231 | `V10-10A` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-IV](acts/GA-IV.md) | [V10](detail/v10-scene-ready-design-v1.md) | [10B](subacts/V10-10B.md) | E232–E237 | `V10-10B` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-IV](acts/GA-IV.md) | [V10](detail/v10-scene-ready-design-v1.md) | [10C](subacts/V10-10C.md) | E238–E243 | `V10-10C` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-IV](acts/GA-IV.md) | [V10](detail/v10-scene-ready-design-v1.md) | [10D](subacts/V10-10D.md) | E244–E250 | `V10-10D` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-IV](acts/GA-IV.md) | [V11](detail/v11-scene-ready-design-v1.md) | [11A](subacts/V11-11A.md) | E251–E256 | `V11-11A` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-IV](acts/GA-IV.md) | [V11](detail/v11-scene-ready-design-v1.md) | [11B](subacts/V11-11B.md) | E257–E262 | `V11-11B` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-IV](acts/GA-IV.md) | [V11](detail/v11-scene-ready-design-v1.md) | [11C](subacts/V11-11C.md) | E263–E268 | `V11-11C` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-IV](acts/GA-IV.md) | [V11](detail/v11-scene-ready-design-v1.md) | [11D](subacts/V11-11D.md) | E269–E275 | `V11-11D` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-IV](acts/GA-IV.md) | [V12](detail/v12-scene-ready-design-v1.md) | [12A](subacts/V12-12A.md) | E276–E281 | `V12-12A` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-IV](acts/GA-IV.md) | [V12](detail/v12-scene-ready-design-v1.md) | [12B](subacts/V12-12B.md) | E282–E287 | `V12-12B` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-IV](acts/GA-IV.md) | [V12](detail/v12-scene-ready-design-v1.md) | [12C](subacts/V12-12C.md) | E288–E293 | `V12-12C` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-IV](acts/GA-IV.md) | [V12](detail/v12-scene-ready-design-v1.md) | [12D](subacts/V12-12D.md) | E294–E300 | `V12-12D` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-V](acts/GA-V.md) | [V13](detail/v13-scene-ready-design-v1.md) | [13A](subacts/V13-13A.md) | E301–E306 | `V13-13A` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-V](acts/GA-V.md) | [V13](detail/v13-scene-ready-design-v1.md) | [13B](subacts/V13-13B.md) | E307–E312 | `V13-13B` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-V](acts/GA-V.md) | [V13](detail/v13-scene-ready-design-v1.md) | [13C](subacts/V13-13C.md) | E313–E318 | `V13-13C` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-V](acts/GA-V.md) | [V13](detail/v13-scene-ready-design-v1.md) | [13D](subacts/V13-13D.md) | E319–E325 | `V13-13D` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-V](acts/GA-V.md) | [V14](detail/v14-scene-ready-design-v1.md) | [14A](subacts/V14-14A.md) | E326–E331 | `V14-14A` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-V](acts/GA-V.md) | [V14](detail/v14-scene-ready-design-v1.md) | [14B](subacts/V14-14B.md) | E332–E337 | `V14-14B` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-V](acts/GA-V.md) | [V14](detail/v14-scene-ready-design-v1.md) | [14C](subacts/V14-14C.md) | E338–E343 | `V14-14C` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-V](acts/GA-V.md) | [V14](detail/v14-scene-ready-design-v1.md) | [14D](subacts/V14-14D.md) | E344–E350 | `V14-14D` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-V](acts/GA-V.md) | [V15](detail/v15-scene-ready-design-v1.md) | [15A](subacts/V15-15A.md) | E351–E356 | `V15-15A` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-V](acts/GA-V.md) | [V15](detail/v15-scene-ready-design-v1.md) | [15B](subacts/V15-15B.md) | E357–E362 | `V15-15B` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-V](acts/GA-V.md) | [V15](detail/v15-scene-ready-design-v1.md) | [15C](subacts/V15-15C.md) | E363–E368 | `V15-15C` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |
| [GA-V](acts/GA-V.md) | [V15](detail/v15-scene-ready-design-v1.md) | [15D](subacts/V15-15D.md) | E369–E375 | `V15-15D` | [Resolver](visual-cp-resolver-rules-v1.md) → [Matrix](visual-asset-act-usage-matrix-v1.md) |

## 5. Act-level Visual Questions

| Grand Act | Visual Question |
|---|---|
| GA I | 공식기록과 현장생활이 왜 다르게 보이는가 |
| GA II | 누가 물건·도시·귀환권을 가질 수 있는가 |
| GA III | 왕국 이전에 공동체를 실제로 움직인 것은 무엇인가 |
| GA IV | 같은 사람·제도가 다른 미래에서 무엇을 잃고 얻었는가 |
| GA V | 무엇을 소유하지 않고도 남길 수 있는가 |

## 6. Direct Use in Episode CP

Episode CP에는 아래 블록만 JIT로 넣는다.

```text
ACT_WIRING
Grand Act:
Volume:
Subact:
Architecture Hub:
Primary Visual Asset:
Current State:
Allowed Beat:
Secondary Echo 1:
Secondary Echo 2:
Do Not Advance:
Production Prompt Route:
```

## 7. Graph Integrity Rule

- Act가 Subact 없이 Episode에 직접 점프하면 FAIL.
- Subact가 Matrix를 우회해 미래 Variant를 직접 호출하면 FAIL.
- 자산이 장면에 없는데 그래프 연결 때문에 등장시키면 FAIL.
- Production Prompt가 Canon/Architecture보다 상위 근거가 되면 FAIL.
- 기존 Markdown 링크를 Obsidian 그래프용이라는 이유로 위키링크로 강제 변환하지 않는다.
- 나중에 Obsidian migration 시 `node_id`만 추가하고 파일명/경로를 임의 변경하지 않는다.

**D16.5 Wiring Registry: 5/5 Acts · 15/15 Volumes · 60/60 Subacts.**
