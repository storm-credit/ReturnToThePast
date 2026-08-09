# Project Skills Registry

## Authority Warning

Skill은 반복 작업 절차다. 작품 정본·사건·인물·결말을 독자적으로 만들거나 승인하지 못한다.

정본 권한과 시작 경로는 [`/AI_PROJECT.md`](../../AI_PROJECT.md)와 [`.agent/orchestra/governance-and-routing-v2.md`](../orchestra/governance-and-routing-v2.md)를 따른다.

## Active

### storycraft-orchestrator

Path: [`.agent/skills/storycraft-orchestrator/SKILL.md`](storycraft-orchestrator/SKILL.md)

Purpose:

- 작업 단위의 중심 장르·문제·독자 약속을 분류
- 상황에 맞는 중심 작법 1개와 보조 작법 최대 2개 선택
- 결말 역산, 국소완결, 장면–반응, 정보간극, 공정단서, 관계·정치·전투·생활 후과를 선택적으로 운용
- 같은 작법 조합과 훅의 기계적 반복 차단
- Storycraft Manifest 작성

Cannot:

- Canon 변경
- 부족한 세계관·인물·아이템 설정 즉석 생성
- 작법을 이유로 설계된 사건·결말 변경

### context-pack-compiler

Path: [`.agent/skills/context-pack-compiler/SKILL.md`](context-pack-compiler/SKILL.md)

Purpose:

- Series / Grand Act / Volume / Subact / Episode CP 컴파일
- 작업에 필요한 정본의 원본 경로와 현재 상태 추출
- 시간·지리·인물·기관·자산·미스터리·손실·POV 누락 검사
- CP의 기준 ref와 stale 여부 관리
- 원고 전 Domain Readiness Hook 실행

Cannot:

- CP를 정본으로 승격
- CP 안에서 새 사실 생성
- 원본 충돌을 임의로 화해

### sentence-narrator

Path: [`.agent/skills/sentence-narrator/SKILL.md`](sentence-narrator/SKILL.md)

Purpose:

- 원고를 한 문장씩 원문 그대로 낭독
- 자연스러운 한국어와 번역체 검사
- 생동감 있는 묘사와 공간·행동 정합성 검사
- 인물별 대사·호칭·고유명사 발음 검사
- 시점·정보상한·스포일러 검사
- Gate OPEN 뒤 A18 원고 품질검사에 역적용

Required companions:

- [`pronunciation-lexicon.md`](sentence-narrator/pronunciation-lexicon.md)
- [`prose-quality-checklist.md`](sentence-narrator/prose-quality-checklist.md)

### human-prose-audit

Path: [`.agent/skills/human-prose-audit/SKILL.md`](human-prose-audit/SKILL.md)

Purpose:

- 문장별 문법검사를 통과했지만 화 전체가 AI처럼 지나치게 정돈된 문제 감지
- 격언형 마감·대칭 대조·의미 재해설·균일한 대사·과기능 묘사 차단
- 사건·설정·인물 의도 변경 없이 문장·대사·호흡·정보 제시 순서 재수술
- 생활의 마찰과 인물별 불완전한 반응 복원
- 다음 화 진행 전 이전 화의 Human Prose 상태 확인

Authority:

- AI는 `AUTHOR REVIEW READY`까지만 판정 가능
- `HUMAN PROSE PASS`는 작가 승인 후에만 기록

## Required Order for Manuscript

1. `context-pack-compiler`
2. Domain Readiness 검사
3. `storycraft-orchestrator`
4. POV·장면 설계
5. A18 원고 구현
6. `sentence-narrator`
7. `human-prose-audit`
8. Canon·Continuity·Reader·Red Team 감사
9. 작가 Human Prose 승인

순서를 바꾸거나 CP 없이 A18을 호출하지 않는다.

작가가 AI 티를 지적한 원고는 구조·정본 PASS만으로 다음 화를 진행하지 않는다.

## Disabled

### chrono-weaver

Legacy regression-oriented skill. This project uses embodied direct time travel, not reset regression. Do not reactivate or reference it as canon.
