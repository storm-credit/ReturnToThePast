# Design Detail and Episode Length Policy v2

Status: CANON-OPERATIONS  
Owner: Architecture PM / Story Architecture / Reader Experience / Continuity  
Date: 2026-08-07  
Pre-Writing Gate: CLOSED  
Manuscript: BLOCKED

## 1. Episode Length Rule

작가 지시: **최저 글자수만 검사하며, 내용상 필요하면 길어져도 허용한다.**

- Working Minimum: `[ASSUMPTION]` 공백 포함 7,000자.
- Maximum: 없음.
- 권장 분량이나 평균치를 맞추기 위해 사건·감정·묘사를 삭제하지 않는다.
- 최저치를 채우기 위한 반복 설명, 의미 없는 대화, 이동 장면 늘이기를 금지한다.
- 한 회차가 길어도 하나의 중심 선택과 상태변화를 완결한다면 유지한다.
- 서로 독립된 절정·선택·상태변화가 두 개 이상이면 분할을 검토한다.
- 플랫폼 확정 뒤 플랫폼 최저치가 7,000자보다 높으면 더 높은 기준을 적용한다.
- 글자수 검사는 원고 단계에서만 수행한다. 설계 카드는 글자수를 채우지 않는다.

## 2. Detail Levels

### D0 — Concept
한 줄 콘셉트와 장르 약속.

### D1 — World / Canon
세계의 규칙, 지리, 마법, 종족, 기관, 법, 경제, 생활, 유산, 손실.

### D2 — Grand Architecture
시리즈 결말, 5 Grand Acts, 승리→다음 문제 연결.

### D3 — Volume / Arc Architecture
15 Volume Acts와 30 Arcs. 각 Arc에는 독립 목표·대항·선택·대가·회수·출구상태가 필요하다.

### D4 — Subact Architecture
60 Subacts. 각 Subact에는 다음이 필요하다.

- Entry State
- Local Goal
- POV / Lead Character
- Time / Location / Travel Logic
- Active Cast and independent agendas
- Opposition and rational benefit
- Mystery question / false interpretation / reveal
- Asset or institution use
- Escalation sequence
- Irreversible choice
- Cost / loss
- Exit State
- Next Cause
- Anti-Repeat marker

### D5 — Functional Episode Card
375화 각각의 독자 약속, 목표, 선택, 상태변화, 훅, 정보상한.

### D6 — Scene-Ready Episode Card
원고로 바로 옮길 수 있는 집필 직전 설계. 각 화마다 다음을 가진다.

- 3–7 scene beats
- scene별 장소와 시간
- 장면 목표와 방해
- 등장인물별 목적·정보·거부 가능성
- 공간 동선·전술·보급 논리
- 공개 정보와 숨길 정보
- 감정 및 관계 변화
- 기관·유산·맥거핀 상태 변화
- 보상과 영구 비용
- 마지막 이미지 또는 훅
- 다음 화 진입 상태
- 관련 정본 링크와 금지사항

### D7 — Cross-Audited Detailed Design
375개 D6 카드, 모든 상태 장부, 숫자·연대·거리·반복·미스터리 회수 검사가 PASS한 상태.

## 3. Current Honest Status

- World / Canon: D1 complete, author review pending.
- Grand Acts: D2 complete.
- Volume Acts: D3의 Volume 부분 complete.
- 30 Arc dossiers: not yet complete.
- 60 Subacts: 기능형 D4 초안 complete; 전체 필드 확장 필요.
- E001–E375: D5 complete.
- E001–E375 D6 scene-ready cards: not complete.
- Therefore full detailed design D7 is **NOT YET COMPLETE**.

앞선 `DESIGN COMPLETE` 표기는 `FUNCTIONAL DESIGN COMPLETE`로 해석·정정한다.

## 4. Push / PR Completion Workflow

상세화는 권 단위로 진행한다.

1. 최신 main에서 `agent/detail-vXX` 브랜치 생성.
2. 해당 권의 Volume Act dossier 보강.
3. 2개 Arc dossier 작성.
4. 4개 Subact dossier 작성.
5. 25개 D6 Scene-Ready Episode Card 작성.
6. 인물·기관·자산·미스터리·손실 상태 갱신.
7. 글자수 정책은 카드에 `Minimum 7,000 / No Maximum`으로 연결하되 원고는 작성하지 않음.
8. Red Team / continuity / anti-repeat 감사.
9. main과 비교해 behind_by=0 확인.
10. PR 생성, squash merge, PR merged 상태와 실제 SHA 확인.
11. main 대표 파일 직접 확인.
12. 다음 권으로 이동.

## 5. Completion Rule

다음 조건 전에는 “디테일하게 전부 완료”라고 보고하지 않는다.

- 30 Arc dossiers complete
- 60 expanded Subact dossiers complete
- 375 D6 cards complete
- state ledgers synchronized through E375
- mystery and MacGuffin payoff coverage complete
- S0=0 and S1=0
- final cross-audit PASS
- files actually merged into main

완료돼도 Pre-Writing Gate는 자동으로 열지 않는다.
