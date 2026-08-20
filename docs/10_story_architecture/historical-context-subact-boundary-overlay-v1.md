# Historical Context × Subact Boundary Overlay v1

Status: **D16.6 ROUTING OVERLAY / ACTIVE AFTER MERGE**  
Scope: historical Context/State packs that intentionally span a current Subact boundary  
Non-Scope: 사건 재설계, 기존 CP 삭제/분할, 원고 변경

## 1. Why This Exists

E001–E088 생산 과정에서 일부 묶음 Context/State Pack은 당시 작업단위 기준으로 작성되어 현재 D16.5의 60-Subact 경계와 정확히 일치하지 않는다.

이는 내용 충돌이 아니라 **artifact granularity 차이**다.

원칙:

> historical file range와 current narrative ownership이 다를 때, Episode의 current Subact 소속은 D16.5 Wiring Registry가 결정한다.

## 2. Exception A — E063–E069

Historical artifacts:

- `.agent/context-packs/episodes/E063-E069-context-pack.md`
- `manuscript/quality/E063-E069-state-mutation.md`

파일 자체 Scope도 `V3 / Subact 3C–3D`라고 명시한다.

Current routing:

| Episode | Current Subact | Historical source |
|---|---|---|
| E063 | V03-3C | E063–E069 pack |
| E064 | V03-3C | E063–E069 pack |
| E065 | V03-3C | E063–E069 pack |
| E066 | V03-3C | E063–E069 pack |
| E067 | V03-3C | E063–E069 pack |
| E068 | V03-3C | E063–E069 pack |
| E069 | **V03-3D** | E063–E069 pack |

Rules:

- E069를 3C로 해석하지 않는다.
- E069 재검수 시 3D architecture / D16.5 visual route를 JIT overlay한다.
- historical file을 2개로 물리 분할하지 않는다.

## 3. Exception B — E082–E088

Historical artifacts:

- `.agent/context-packs/episodes/E082-E088-context-pack.md`
- `manuscript/quality/E082-E088-state-mutation.md`

기존 CP가 이미 `4B — E082–E087 + 4C 진입 E088`이라고 명시한다.

Current routing:

| Episode | Current Subact | Historical source |
|---|---|---|
| E082 | V04-4B | E082–E088 pack |
| E083 | V04-4B | E082–E088 pack |
| E084 | V04-4B | E082–E088 pack |
| E085 | V04-4B | E082–E088 pack |
| E086 | V04-4B | E082–E088 pack |
| E087 | V04-4B | E082–E088 pack |
| E088 | **V04-4C** | E082–E088 pack |

Rules:

- E088은 4B의 마지막 화가 아니라 **4C의 첫 화**다.
- E088 Exit는 E089 Entry의 직접 선행상태다.
- E089 D12 CP는 E082–E088 State Mutation의 Exit를 직접 authority source로 사용한다.

## 4. Resolution Priority

Episode/Subact 판단 순서:

1. `obsidian-act-subact-visual-wiring-v1.md`
2. current Scene-Ready / D6 registry
3. this boundary overlay
4. historical grouped CP/state pack

Historical file title/range 때문에 current Subact를 바꾸지 않는다.

## 5. Future Rule

E089 이후 새 grouped CP/State Pack은 가능하면 하나의 Subact 안에서만 만든다.

Subact 경계를 넘겨야만 하는 경우:

- 각 Episode의 exact Subact를 header/table에 명시
- 경계 Episode의 Previous Exit / Next Entry를 따로 명시
- Visual Router가 current Subact를 우선함을 명시

## 6. Verdict

- historical cross-boundary packs: **2**
- content contradiction found: **0**
- routing ambiguity after overlay: **0**
- manuscript change required: **0**

**E069 = V03-3D / E088 = V04-4C are HARD ROUTING LOCKS.**
