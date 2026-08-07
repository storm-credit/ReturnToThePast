# Pre-Writing Gate Status

Status: **OPEN — D10 ORCHESTRATION READY**  
Effective: 2026-08-07  
Author Directive: `스킬등록후 끝까지 써줘. 한편마다 푸쉬해주고.`  
Current Production Unit: E003

## Authorization

작가는 낭독·한국어 문체 스킬을 등록한 뒤 E001부터 E375까지 순차 집필하고, 한 화마다 별도 PR로 푸시하도록 명시적으로 승인했다.

이 승인은 원고 제작에만 적용된다. 다음 사항을 조용히 바꿀 권한은 아니다.

- Canon Constitution
- 결말과 영구손실
- 인물 정체·사망·관계
- 시간법칙·연대·인과
- 15권·375화의 핵심 사건

## D10 Infrastructure

- PR: #25
- Status: MERGED / MAIN VERIFIED
- Merge SHA: `a34113d538f9ec22b396fdf0193dd82ab19328ec`
- S0: 0
- S1: 0

## Per-Episode Operating Condition

원고 승인은 유효하지만 각 회차는 다음 D10 조건을 개별 통과해야 한다.

1. 최신 main 기준 Episode Context Pack READY
2. 필요한 Domain Bible의 장면 상세도 READY
3. Storycraft Manifest READY
4. POV·정보상한·주인공 부재 행동 확인
5. 이전 화 상태와 State Mutation Plan 확인
6. S0=0 / S1=0
7. A18 원고 작성
8. A19 문장·낭독·이름·호칭·행동 검사
9. A13/A14/A16 교차감사
10. 한 화당 branch / PR / squash merge / main 재확인

CP·Skill·Harness는 정본을 덮어쓸 수 없다.

## Current State

### E001

- Title: 마지막 도시의 다른 날짜
- PR: #24
- Merge SHA: `97d9195913a53eba96d7cde4360429125ee7c69b`
- D10 Retro-Audit: PASS
- Status: **CANON MANUSCRIPT / COMPLETE**

### E002

- Title: 여섯 개의 승인
- PR: #27
- Merge SHA: `f33141d42634e0d7f634ae5886a0b63ad3a8b88f`
- Context Pack: READY
- Storycraft Manifest: READY
- Quality: PASS
- Main manuscript: VERIFIED
- Status: **CANON MANUSCRIPT / COMPLETE**

### E003

- Title: 창시자의 증거
- Episode CP: READY
- Storycraft Manifest: READY
- POV: 에이든 단일 근접 3인칭
- Scene Density: S형 3장면
- Primary Craft: 경쟁하는 증거사다리
- Status: **READY FOR A18 AFTER STATUS MERGE**

## Active Agents

- A00 Story Orchestrator: ENABLED
- A02 Canon Controller: ENABLED
- A18 Prose Agent: ENABLED PER READY EPISODE
- A19 Sentence Narration & Korean Prose Audit: ENABLED
- A20 Storycraft Director: ENABLED
- A21 Context Pack Compiler & Harness Runner: ENABLED

## Length

- 원고 최소 공백 포함 7,000자
- 상한 없음
- 분량을 맞추기 위한 반복설명·무의미한 이동·대화 늘리기 금지

## Pause Conditions

다음 중 하나라도 발생하면 해당 화만 PAUSED로 전환한다.

- 정본 충돌
- stale 또는 출처 없는 CP
- 필요한 인물·아이템·종교·기관 상세 부재
- 보조 POV 정보상한·재합류 상태 부재
- 새 설정의 즉석 생성 필요
- S0 또는 S1
- branch가 main보다 뒤처짐

전체 Gate를 다시 닫지 않고 문제 회차와 영향범위만 차단한다.
