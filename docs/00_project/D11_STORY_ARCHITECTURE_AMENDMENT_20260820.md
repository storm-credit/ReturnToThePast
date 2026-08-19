# D11 Story Architecture Amendment — 2026-08-20

Status: CANON AMENDMENT  
Authority: AUTHOR DECISION  
Scope: terminology / protagonist-vs-world causality / architecture overlays  
Does Not Change: 5 Grand Acts, 15-volume structure, 60 Subact event spine, permanent losses, final ending function

## D11-01 — Mana Fever / Gray Calamity

### Author Decision

**마나열병과 회색 재앙은 같은 현상의 다른 이름이다.**

### Canon Rule

- 둘을 서로 다른 질병·재난으로 병렬화하지 않는다.
- `마나열병이 있고 별도로 회색 재앙이 있다`는 설정은 폐기한다.
- 개인/지역/사회 규모 차이가 필요할 때는 `개인 발병 / 집단 발병 / 광역 붕괴`로 구분한다.
- `회색열`은 민간 통칭으로 사용 가능하다.
- 병리 원인은 기존 정본대로 **연속성 불일치 반응**이다.

### Updated Source

`docs/03_systems/mana-fever-gray-calamity-v1.md`

---

## D11-02 — Protagonist and Independent World Causality

### Author Decision

에이든 로엔은 작품의 중심 주인공이지만 **모든 사건과 세력이 에이든을 중심으로만 움직여서는 안 된다.**

시간여행 장편의 세계는 에이든이 없는 동안에도 다른 인물·기관·국가·시대가 독립적으로 행동하고, 그 행동이 서로 충돌하며 다음 상태를 만든다.

### Canon-Architecture Rule

- 에이든은 메인 POV와 감정적 책임선의 중심을 유지한다.
- 에이든은 세계의 유일한 의사결정자·중재자·역사변경자가 아니다.
- 주요 세력은 에이든의 허가 없이 독립 행동을 실행한다.
- 에이든이 귀환하거나 도착했을 때 이미 바뀐 기정사실이 존재할 수 있다.
- 적대세력도 실제 생존기능과 내부 합리성을 가진다.
- 최종 해법은 에이든 혼자 만든 체제가 아니라 여러 세력·지역·종족·실무자가 축적한 운영기능을 결합한 결과여야 한다.
- 에이든의 최종 희생은 새 체제의 유일한 창조행위가 아니라 **중앙 독점망의 마지막 연결비용**이다.

### Required Architecture Overlays

- `docs/04_factions/faction-conflict-engine-v1.md`
- `docs/10_story_architecture/faction-causal-track-v1.md`
- `docs/10_story_architecture/parallel-plot-and-pov-governance-v1.md`

---

## D11-03 — Existing Spine Preservation

이번 보강은 다음을 폐기하거나 다시 쓰는 작업이 아니다.

- Grand Act I–V 유지
- V1–V15 유지
- E001–E375 목표 유지
- `subact-causal-matrix-v1.md`의 60 Subact Goal / Resolution / Cost / Next Cause 유지
- 주요 영구손실 유지
- F0 완전복원 거부 유지
- 중앙 연대개입 폐쇄 + 생활 안정 기능 분산 결말 유지
- 에이든 공적 이름·역사주소·귀환권 소실 유지
- 리아의 사적 F0 기억 영구손실 유지

보강 대상은 **누가 독립적으로 움직이며, 그 행동이 어떻게 병렬 인과를 만드는가**다.

---

## D11-04 — Known Architecture Corrections

### E089

- 상위 POV 배치: 리아 세른 P1 유지.
- 별도 원고 브랜치의 에이든 POV E089는 설계 충돌 상태.
- 해당 원고는 재작업 전 main 병합 금지.

### E128

- 마르칸 베르 P1 유지.
- 기존 POV 설명을 V6 D6에 맞춰 교정한다.
- 마르칸은 외국 중립 계약기록과 양 진영 수치를 대조해 `둘 다 부분진실`임을 인정하고, 그럼에도 F1 시민책임 때문에 E130 체포명령 논리를 형성한다.
- 사건 순서 자체는 변경하지 않는다.

---

## D11-05 — Cross-Era Council

V12의 세 시대 협상은 새로운 초능력이나 무비용 통신을 추가하지 않는다.

`docs/03_systems/cross-era-council-protocol-v1.md`의 방식처럼 기존 파견·귀환·역사주소·분산귀환망 규칙을 조합해 성립시킨다.

세부 대표 인물 배정은 기존 C01–C30과 시대/핵심권을 재검토한 뒤 확정한다. 기존 정본과 충돌하면 이 Amendment만으로 신규 핵심 인물을 자동 추가하지 않는다.

---

## D11-06 — Red Team Gate

E089 이후 새 원고를 진행하기 전에 최소 다음을 확인한다.

1. 해당 Volume 주요 세력 3–5개
2. 각 세력의 독립 행동 1개 이상
3. 이름 있는 반복 인물 연결
4. 에이든이 모르는 부분정보
5. 정치결정의 생활 후과
6. 다음 Subact에 남는 기정사실
7. POV 설계와 D6 카드 충돌 없음
8. 마나열병/회색 재앙 용어 분리 없음

세부 맹점은 `docs/99_quality_control/deep-world-architecture-blindspot-audit-v1.md`를 따른다.
