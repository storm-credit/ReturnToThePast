# Visual CP Resolver Rules v1

Status: **D16.5 PRODUCTION ROUTER — ACT/SUBACT GRAPH WIRED**  
Purpose: 5 Grand Acts / 15 Volumes / 60 Subacts / E001–E375에서 Visual Bible을 실제 집필 Context Pack에 필요한 만큼만 주입한다.

## 1. Resolver Input

Episode CP 생성 시 다음 입력만 사용한다.

1. Episode ID / Volume / Subact
2. 현재 Grand Act / Volume / Subact 허브
3. `obsidian-act-subact-visual-wiring-v1.md`
4. POV
5. 장면에 이미 존재하는 캐릭터·유산·신수·장소·세력
6. `visual-asset-act-usage-matrix-v1.md`
7. 각 domain Production Prompt / Visual Identity Bible
8. 현재 상태 체크포인트

새 자산을 ‘비주얼을 위해’ 장면에 추가하지 않는다.

### Mandatory Resolution Order

`Episode → Wiring Registry → Grand Act → Volume → Subact → Scene Assets → Visual Matrix → Production Prompt`

Act나 Volume만 보고 Episode 자산을 바로 고르지 않는다. 반드시 해당 Subact까지 내려간다.

## 2. Resolver Priority

### P0 — Scene Necessity
장면에 실제 존재하고 독자가 인지해야 하는 대상.

### P1 — Act Visual Question
현재 Grand Act의 시각 질문을 강화하는 대상.

### P2 — Continuity Echo
20화 이상 공백 후 재등장하거나 손상/소유권 상태를 다시 확인해야 하는 대상.

### P3 — Merch/Collection Appeal
P0–P2를 만족하는 대상 안에서만 고려. 상품성을 위해 장면을 만들지 않는다.

## 3. Per-Episode Budget

- Primary: 1
- Secondary Echo: 0–2
- New grammar: 0–2
- Full-body re-description: 0 after first full reveal
- Variant transition: 0–1 unless Volume climax already requires more

## 4. State Resolution

Resolver는 ID만 보고 외형을 호출하지 않는다.

예:
`C01` → 현재 Volume을 확인 → `F0 FIELD / ALTERED-WORN / ADDRESS-LOSS / FINAL LOSS` 중 하나만 선택.

같은 방식:
- R계열: O/U/C/F
- B계열: 생태/계약 상태
- L계열: 시대/제도 Variant
- F계열: 조직 상태/부패/분산 상태

미래 상태를 현재 회차에 당겨 쓰면 S1 오류로 기록한다.

## 5. Asset Type Resolver

### Character
출력:
`Silhouette anchor / material / gesture / current wear / forbidden future variant`

얼굴 전체 설명은 첫 강한 Reveal 이후 기본 생략.

### Relic
출력:
`current lineage state / holder or custody / visible damage / what must not look upgraded`

### Beast
출력:
`presence trace / movement / ecological relation / refusal condition`

신수를 매번 전신으로 보여주지 않는다. 흔적만으로 Echo 가능.

### Landmark
출력:
`foreground life / midground institution / background landmark / current era mutation`

beauty shot보다 생활·제도 우선.

### Faction
출력:
`shape / material / behavior mark`

문장·로고가 없어도 세력이 읽혀야 한다.

## 6. Grand Act Resolver Themes

### GA I — 잘못된 치료
Filter: 기록 vs 생활 / 중앙 vs 현장 / 표적 vs 잔여증거.

### GA II — 살아남은 미래의 권리
Filter: 소유권 / 현재생활 / 귀환권 / 공동사용 / 외부계약.

### GA III — 건국의 아홉 상처
Filter: 공동건설 / 문화혼합 / 생태계약 / 건국 전 원형.

### GA IV — 세 시대의 전쟁
Filter: 동일 대상의 다른 미래 / 손실 / 책임 / 표준화와 독점.

### GA V — 남길 역사
Filter: 분산 / 반환 / 생활 / 공개검증 / 불완전하지만 지속 가능한 정상성.

## 7. Subact Transition Rule

Subact 첫 회:
- 새로운 Visual Grammar 최대 1–2개 허용.

Subact 중간:
- Echo/손상/행동 중심.

Subact 마지막:
- `D/T/V/F`가 정본 사건에서 발생할 때만 외형변화를 명시.

다음 Subact 첫 회는 직전 변경을 기억해야 한다.

### D16.5 Wiring Requirement

각 Subact는 `obsidian-act-subact-visual-wiring-v1.md`의 60개 행 중 정확히 1개와 대응한다.

- 60/60 Subact 모두 Wiring 행을 가진다.
- Episode가 어느 Subact에 속하는지 불명확하면 원고 생산 중지.
- Subact Hub에 등장하지 않는 자산을 Wiring만으로 새로 추가하지 않는다.
- Subact에서 이미 링크된 캐릭터·기관·자산·장소가 실제 후보군이다.

## 8. Volume Transition Rule

Volume 시작 CP는 직전 Volume의 다음 상태만 가져온다.

필수 확인:
- 캐릭터 장비가 멀쩡하게 리셋되지 않았는가
- 유산 소유권/손상이 역행하지 않았는가
- 신수 계약/거부상태가 리셋되지 않았는가
- 장소가 이전 시대상태로 복귀하지 않았는가
- 세력표식이 인과 변화 없이 다시 과거형이 되지 않았는가

## 9. Production Prompt Matching

실제 이미지가 필요한 경우 CP에서 자산 ID를 다음 문서로 라우팅한다.

- C01–C10 → `docs/05_characters/production-prompts-c01-c10-v1.md`
- C11–C20 → `docs/05_characters/production-prompts-c11-c20-v1.md`
- C21–C30 → `docs/05_characters/production-prompts-c21-c30-v1.md`
- R01–R12 → `docs/09_collection/production-prompts-r01-r12-v1.md`
- B01–B05 → `docs/09_collection/production-prompts-b01-b05-v1.md`
- L01–L08 → `docs/02_world/production-prompts-l01-l08-v1.md`
- F01–F14 → `docs/02_world/production-prompts-f01-f14-v1.md`

모든 요청에는 `visual-negative-and-collision-rules-v1.md`를 함께 적용한다.

## 10. Visual CP Output Template

```text
VISUAL_CP
Episode: E###
Grand Act / Volume / Subact:
Architecture Hub:
Wiring Registry Row:
Primary Asset:
Current State:
Beat Type:
3-Second Anchor:
Material Anchor:
Gesture/Behavior Anchor:
Damage/Ownership Memory:
Secondary Echo 1:
Secondary Echo 2:
Do Not Re-explain:
Do Not Advance:
Production Prompt Route:
Collision Check Against:
```

## 11. Obsidian Graph Compatibility

D16.5는 파일명이나 정본 구조를 바꾸지 않고 링크 레이어를 추가한다.

Graph에서 최소 다음 경로가 보여야 한다.

`GA Hub ↔ Subact Hub ↔ Wiring Registry ↔ Visual Resolver ↔ Visual Matrix`

기존 Subact Hub가 캐릭터/장소/자산 허브로 가진 Markdown 링크도 그대로 Graph edge가 된다.

향후 Obsidian properties는 다음 키만 권장한다.

- `node_type`
- `node_id`
- `parent_act`
- `parent_volume`
- `parent_subact`
- `visual_router`
- `visual_matrix`

properties 도입 때문에 정본 파일명을 개명하지 않는다.

## 12. E089 Production Example

E089는 기존 D12/D15 lock을 따른다.

```text
Episode: E089
Grand Act / Volume / Subact: GA II / V04 / 4C
Architecture Hub: V04-4C
Wiring Registry Row: V04-4C / E088–E093
Primary Asset: C02 리아 세른
Current State: MULTI-ERA EVIDENCE
3-Second Anchor: 비대칭 겹소매 / 세로 문서갑 / 얇은 투명판
Gesture: 이름·출처를 확인하며 작은 출처점을 남김
Do Not Re-explain: 전신 소개와 미모평가
Do Not Advance: GA V의 PUBLIC EVIDENCE / PRIVATE LOSS
Collision: C12 엘사, C22 하렌
```

이 예시는 새 사건을 만들지 않는다. E089 실제 장면에서 존재하는 행동만 사용한다.

## 13. QA Gate

FAIL:
- Act에서 Subact를 건너뛰어 Episode 자산 직접 선택
- 장면에 없는 자산을 굿즈/비주얼 목적으로 추가
- 미래 Variant 선행
- 색/머리만으로 캐릭터 구분
- 한 회 4개 이상 신규 아이콘
- 손상 리셋
- 유산 Final 역행
- B05 진실판정자화
- C30 정체시각 확정
- Wiring Registry와 Episode range 불일치

PASS:
- Episode → Act/Volume/Subact 경로가 유일하게 해석됨
- 자산 ID가 현재 Act/Volume 상태와 일치
- 1–3개의 짧은 인지단서만 원고에 사용
- 실제 콘셉트아트 제작이 필요할 때만 Production Prompt로 라우팅

**VISUAL CP RESOLVER: D16.5 WIRED / READY FOR JIT USE.**
