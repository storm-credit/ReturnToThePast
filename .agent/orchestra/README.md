# Story Architecture Orchestra — Project Runtime

Status: CANON-OPERATIONS  
Scope: 세계관·설정집·설계도 전용  
Pre-Writing Gate: CLOSED  
Manuscript: BLOCKED

## Source Basis

이 실행체계는 작가가 처음 제공한 다음 세 문서를 최상위 방법론으로 사용한다.

1. `CLAUDE_story_project_template_v1.md` — **저장소 미보관**
2. [`story_architecture_master_prompt_v1.md`](../../story_architecture_master_prompt_v1.md) — 저장소 루트에 보관됨
3. `story_architecture_os_v1.md` — **저장소 미보관**

1번과 3번은 작가가 제공한 원본이지만 저장소에 커밋되어 있지 않다. 계승 규칙은 [`docs/00_project/source-precedence-and-automation.md`](../../docs/00_project/source-precedence-and-automation.md) `Method Sources`에 요약본만 남아 있으므로, 원본 확인이 필요한 판정에서는 작가에게 파일을 요청한다.

저장소의 [`CLAUDE.md`](../../CLAUDE.md)는 세 문서를 이 작품에 맞게 적용한 프로젝트 헌법이다. 전문 에이전트는 이 헌법과 Canon Constitution을 거슬러 설정을 확정할 수 없다.

## Mission

- 단일 작가 흉내가 아니라 역할별 검토를 순차 수행한다.
- 설정 수가 아니라 플롯 사용처·상태 변화·회수·검증으로 완료를 판정한다.
- 세계관 → 인물·세력 → 수집·성장 → 대서사 → 미스터리·손실 장부 → 회차 카드 순서를 지킨다.
- 한 단계의 해결책이 다음 단계 문제의 원인이 되게 한다.
- S0 또는 S1이 남으면 다음 정본 승격을 차단한다.
- 작가 질문 없이 진행 가능한 항목은 `[ASSUMPTION]`으로 기록하고 계속 진행한다.

## Fixed Runtime Order

1. Architecture PM이 범위와 의존성을 연다.
2. Canon Controller가 정본 충돌과 낡은 파일을 격리한다.
3. World Cluster가 지리·마법·질병·종족·생활·경제를 설계한다.
4. Institution/Character Cluster가 권한·세력·인물 자율성을 설계한다.
5. Collection/Mystery Cluster가 유산·신수·맥거핀·단서와 회수를 연결한다.
6. Grand Architecture가 결말에서 역산해 5 Grand Acts / 15 Volumes / Act / Arc / Subact / Episode를 만든다.
7. Continuity/Loss가 연대·거리·숫자·사망·기억·보유 상태를 대조한다.
8. Reader Experience와 Similarity Audit가 반복·과잉·참고작 유사성을 검사한다.
9. Red Team이 S0–S3를 판정한다.
10. GitHub Verifier가 main 비교, PR, 병합, 대표 파일을 검증한다.

## Absolute Blocks

- Gate 전 원고, 장면 산문, 시험 집필 금지
- 회귀·죽음 리셋 재도입 금지
- 에이든의 권한·정답·유산 독점 금지
- 사도 숫자를 먼저 정하고 인물을 채우는 방식 금지
- 엘프·드워프 등 외형만 바꾼 종족 추가 금지
- 플롯 사용처 없는 유물·신수·보석 추가 금지
- 마지막 반전을 위한 시간 법칙 후출 금지
- 영구손실의 다른 시간대 버전 대체 금지

## Completion Meaning

'끝까지'는 문서 수가 아니라 다음 조건을 뜻한다.

- 세계 규칙과 플롯이 상호참조됨
- 15권 전체 인과와 결말이 연결됨
- 목표 회차 카드가 존재함
- 인물·기관·자산·미스터리·손실 상태가 추적됨
- 전체 교차감사 PASS
- S0=0, S1=0
- main 병합 확인

이 조건을 충족해도 Gate는 자동으로 열리지 않는다.
