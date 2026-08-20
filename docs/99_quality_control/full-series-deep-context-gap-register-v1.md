# Full-Series Deep Context Gap Register v1

Status: **ACTIVE GAP GATE / DO NOT INVENT MISSING CANON**
Scope: E001–E375 Static Deep Context + episode JIT preflight

## 1. Why this register exists

Full-Series Deep Context Pack의 목적은 기존 Architecture를 깊게 집필 입력으로 컴파일하는 것이다. 상위 설계 자체에 없는 값을 Context가 새로 만드는 작업이 아니다.

현재 main의 Subact/Character/World source에는 실제로 `[설계 미정]`이 남아 있다. 따라서 `375/375 Static Context coverage`와 `375/375 모든 세부값 확정`은 서로 다른 상태다.

이 Register는 그 차이를 강제한다.

## 2. Gap classes

### GAP-NB — Non-Blocking
현재 Episode의 핵심 선택·인과·정보상한·법적 가능성을 바꾸지 않는 세부값.

예:
- 아직 이름이 없는 작은 실내/시설
- 장면 기능에 영향을 주지 않는 정확한 거리
- 분 단위 이동시간이 필요하지 않은 경우의 세부 소요시간
- 정본에 배정되지 않은 부차 기능인물 이름
- 연·월·일이 장면 메커니즘에 필요하지 않은 경우의 exact calendar detail

처리:
- Pack에 `[GAP-NB]`로 노출
- 임의 이름/숫자 생성 금지
- 실제 집필에서 필요해지는 순간 JIT ruling

### GAP-B — Blocking
정하지 않으면 장면 자체를 안전하게 쓸 수 없는 값.

예:
- POV/Lead 주체
- 누가 핵심 선택을 하는지
- 특정 인물 정체를 확정해야 하는 장면
- 이동 가능 여부를 결정하는 거리/시간
- 법적으로 누가 어떤 권한을 갖는지
- Mystery 단서가 이번 화에서 공개 가능한지
- 영구손실/사망/소유권 변경 여부

처리:
- JIT Preflight STOP
- 상위 정본/Author decision으로 ruling 후에만 원고 진행
- Context가 추론으로 채우면 S0

## 3. Known regression examples

### V15-15D
Source Hub가 이미 다음을 명시한다.

- E369–E372 일부 POV/Lead가 명시되지 않음
- 15D exact 연·월·일 없음
- 여러 기능 장소의 정확한 지명/거리/동선 없음
- C27의 E371 배정은 대조상 대응되지만 회차번호를 직접 적은 정본은 아님

분류 원칙:
- exact 날짜/지명 자체가 장면 선택을 바꾸지 않으면 `GAP-NB`
- E369–E372를 실제 쓰는데 POV가 필요하고 active POV source에도 배정이 없다면 `GAP-B`
- C27 E371 배치가 장면 주체 결정에 필요하면 `GAP-B / ruling required`

### E089
이미 D12/current overlay가 리아 P1을 명시하므로 POV gap이 아니다.

### E007
active POV source가 아이리스 네르 P1을 명시하므로 gap이 아니라 **known historical manuscript conflict**다.

## 4. Gap handling by Static Deep Pack

Static Pack은 다음 3가지를 구분해야 한다.

1. **Resolved** — 상위 source가 값을 제공함
2. **Runtime-only** — 이전 실제 원고가 있어야 값이 생김
3. **Gap** — 상위 source 자체에 값이 없음

`Runtime-only`와 `Gap`을 같은 것으로 취급하면 안 된다.

예:
- E200의 직전 화에서 실제 누가 다쳤는가 = Runtime-only
- E371의 장면 Lead가 상위 정본에 정말 없다 = Gap

## 5. No silent completion

다음 표현은 금지한다.

- `375화의 모든 세부설계가 완전히 확정됨`
- `모든 위치/날짜/POV가 확정됨`
- `[설계 미정] 없음`

현재 안전한 표현:

> E001–E375 전체에 Static Deep Context routing이 존재하며, 상위 정본의 확정값과 미정값을 구분해 보존한다. 개별 회차는 JIT Preflight에서 GAP-B=0을 확인한 뒤 집필한다.

## 6. QA Gate

Episode JIT 전에 반드시 확인:
- `GAP-B = 0`
- `Runtime-only values resolved from actual previous Exit`
- `GAP-NB가 임의 확정값으로 변환되지 않음`

**Gap preservation is a correctness feature, not an incompleteness to hide.**
