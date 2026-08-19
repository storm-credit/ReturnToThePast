# Production Gate Status

Status: **ACTIVE — MAIN VERIFIED THROUGH E088 / CONTINUATION RECONCILIATION REQUIRED**  
Effective: 2026-08-19  
Verified Main SHA: `c3130ba8ccb095959d02d8bec8862e1a37e3e6cb`  
Current Production Unit: E089+ continuation reconciliation from latest `main`

## Why This File Was Updated

이 문서는 2026-08-07의 `E001 AUTHOR PROSE REVIEW` 상태에 멈춰 있었지만, 실제 GitHub `main`과 PR 이력은 이후 크게 진행됐다.

현재 확인된 실제 상태:

- `main`에는 `manuscript/volume-01`~`volume-04`가 존재한다.
- `manuscript/volume-04`에는 E076~E088이 존재한다.
- 최신 `main` SHA는 `c3130ba8ccb095959d02d8bec8862e1a37e3e6cb`이다.
- PR #120에서 V1 E001~E025 수술본이 정본 원고 경로에 반영됐다.
- PR #121에서 E082~E088 최신 정본 재작성본이 병합됐다.
- PR #122에서 E026~E050 V2 정본 기준 수술이 병합됐다.
- 따라서 과거의 `E001에서 생산 중단` 표기는 현재 저장소 실재 상태와 일치하지 않는다.

이 갱신은 사건·설정·결말을 변경하지 않는다. GitHub 실재 상태를 장부에 맞추는 작업이다.

## Main-Verified Manuscript Boundary

### E001~E088

- GitHub state: **MAIN에 존재 / 원격 확인됨**
- 현재 main 기준 마지막 확인 원고: `manuscript/volume-04/E088-가족관계가-바뀌는-의식.md`
- `HUMAN PROSE PASS`는 작가 전용 판정이므로 AI가 일괄 부여하지 않는다.
- main 존재와 Human Prose 최종승인은 별개 상태다.

## Unmerged Continuation Chain

아래 원고는 `main`에 없는 초고다.

| 범위 | PR | 상태 | 주의 |
|---|---:|---|---|
| E089~E094 구판 | #90 | OPEN / DRAFT / NOT MERGED | E094는 #114 정본 재작성으로 대체됨. E089~E093만 salvage 후보 |
| E094~E100 | #114 | OPEN / DRAFT / NOT MERGED | 최신 main 기준 재검증·재기반 필요 |
| E101~E106 | #115 | OPEN / DRAFT / NOT MERGED | #114 인계 상태 의존 |
| E107~E112 | #116 | OPEN / DRAFT / NOT MERGED | #115 인계 상태 의존 |
| E113~E118 | #117 | OPEN / DRAFT / NOT MERGED | #116 인계 상태 의존 |
| E119~E125 | #118 | OPEN / DRAFT / NOT MERGED | #117 인계 상태 의존 |

2026-08-19 재확인 기준:

- PR #90 head `agent/manuscript-e089-e094`: 최신 main 대비 **ahead 9 / behind 279 / diverged**
- PR #114 head `agent/manuscript-e094-e100-v2`: 최신 main 대비 **ahead 10 / behind 279 / diverged**
- #115~#118 역시 PR 생성 당시 동일한 구형 main 계열을 인계받은 연쇄 초고이므로, 사용 전 각각 최신 main 기준 freshness 검증이 필수다.

## Superseded / Legacy Draft Warning

저장소에는 E003~E024 및 기타 구간의 오래된 OPEN/DRAFT PR이 다수 남아 있다. 이후 정본 병합본 또는 최신 재작성본이 존재하는 경우 해당 PR을 현행 집필 기준으로 사용하지 않는다.

특히:

- 구판 #89 E082~E088은 #121 최신 재작성 병합으로 대체됨.
- #113 E095~E100은 정본 불일치로 CLOSED / NOT MERGED이며 #114가 후속 기준이다.
- #112 E025는 정본 카드 불일치로 CLOSED / NOT MERGED이며 #77 계열이 반영됐다.

## Human Prose Rule

- AI는 `AUTHOR REVIEW READY`까지만 판정할 수 있다.
- 최종 `HUMAN PROSE PASS`는 작가가 실제 원고를 읽고 승인한 경우에만 기록한다.
- `main에 존재`와 `HUMAN PROSE PASS`를 혼동하지 않는다.
- 작가가 AI 티를 지적한 구간은 사건을 바꾸지 않고 문장·대사·호흡·생활감만 재수술한다.

## Resume / Continuation Rule

E089 이후를 이어갈 때는 다음 순서를 강제한다.

1. 최신 `main`에서 새 작업 브랜치를 만든다.
2. E089~E093은 PR #90의 사건을 자동 채택하지 말고 현재 Scene-Ready Design / CP / State Ledger와 다시 대조한다.
3. E094는 #90 버전을 폐기하고 #114의 정본 사건선을 기준으로 재검증한다.
4. E094~E125의 기존 초고는 사건·수치·훅을 현재 정본과 대조한 뒤 필요한 부분만 salvage한다.
5. branch가 `behind_by=0`인지 확인한다.
6. 원고 Validator / Canon / Information Ceiling / Scene Density / Human Prose Audit을 통과시킨다.
7. 원격 브랜치에 푸시하고 PR을 만든다.
8. **작가의 명시적 승인 전 `main`에는 병합하지 않는다.**

## Current Hard Stops

다음 중 하나라도 있으면 `main` 병합 금지다.

- 최신 main보다 뒤처진 branch
- 구판 PR의 사건선을 최신 정본 대조 없이 그대로 재사용
- E094의 #90 구판과 #114 재작성본을 혼합
- 정본 충돌 미해결
- 필요한 Context Pack / Craft Manifest / State Mutation 부재
- S0 또는 S1 미해결
- 작가 승인 없이 `HUMAN PROSE PASS` 선언
- 작가의 명시적 main 병합 승인 부재

## Next Production Unit

**E089~E093 최신-main 정본 재검증 및 clean continuation branch 구성.**

그다음 E094~E100 → E101~E106 → E107~E112 → E113~E118 → E119~E125 순으로 오래된 연쇄 초고를 최신 main에 맞춰 재검증한다.
