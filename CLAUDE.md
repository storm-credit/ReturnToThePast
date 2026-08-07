# CLAUDE.md — 《왕국은 과거를 먹고 산다》 Story Architecture Orchestra

이 저장소의 AI는 단일 작가가 아니라 **장편소설 설계 PM 오케스트라**로 동작한다.

## Source Basis

작가가 제공한 다음 세 문서를 방법론 원본으로 따른다.

1. `CLAUDE_story_project_template_v1(1).md`
2. `story_architecture_master_prompt_v1(1).md`
3. `story_architecture_os_v1(1).md`

프로젝트 실행판:

- `.agent/orchestra/README.md`
- `.agent/orchestra/agent-registry.md`
- `.agent/orchestra/execution-protocol.md`
- `.agent/orchestra/completion-gates.md`

## Project Variables

- Project Code: 《나는 과거로 간다》 재설계판
- Recommended Working Title: 《왕국은 과거를 먹고 산다》
- Genre: 다크 판타지 직접 시간여행 음모 스릴러 / 정치 판타지
- Structure: 5 Grand Acts × 3 Volumes = 15권
- Design Target: 375화 / 권당 25화
- Target Platform: `[ASSUMPTION]` 한국 웹소설 플랫폼, 최종 미정
- Core Audience: 복잡한 시간 인과, 음모, 다크 판타지, 관계극, 수집형 미스터리를 선호하는 성인 독자
- Core Fantasy: 멸망한 미래의 현장요원이 여러 판타지 시대에 직접 파견되어 재앙을 막고 자신이 바꾼 미래와 맞선다.
- Core Emotion: 추적, 불신, 비극적 연대, 존재권, 기억과 책임
- Ending Tone: 영구손실이 남는 씁쓸한 희망
- Repository: https://github.com/storm-credit/ReturnToThePast
- Pre-Writing Gate: CLOSED
- Manuscript: BLOCKED

## Author-Locked Direction

1. 회귀가 아니라 직접 타임트래블이다.
2. 죽음·실패·수면·유물은 동일 출발점 리셋을 만들지 않는다.
3. 주인공은 한 번의 연속된 생애를 살며 상처·나이·죄·관계가 누적된다.
4. 과거 개입은 미래의 본부·국가·관계·지도·기록을 실제로 바꾼다.
5. 왕국 문명 전체가 시간장치다.
6. 최소 세 능동 시대를 운용한다: Era O / N / F.
7. 기존 Drafts는 LEGACY / REFERENCE ONLY다.
8. 세계관·설정집·설계도만 먼저 완성한다.
9. 원고는 Gate 명시 개방 뒤 새 설계 기준으로 처음부터 작성한다.
10. 15권 구조는 유지하며 375화 설계 목표로 진행한다.

## Time-Travel Identity Locks

- 직접 육체 이동
- 단일 가변 시간선
- 변형된 미래 귀환
- 미래 정보의 불완전성
- 영구손실 자동복구 금지
- 좌표·승인·동기화·주소·귀환·부담·감사 권한 분산
- 한 번의 암살로 문명 규모 고정점 해결 금지
- 무한 재시도·임의 날짜·대규모 군대 이동·자동 귀환 금지

## World Locks

- 일반 마법과 국가 규모 시간여행을 분리한다.
- 마나는 물질·기억·기록·관습의 일치에서 생기는 연속성 압력이다.
- 마나열병은 연속성 불일치 반응이며 단순 생물학적 전염병이 아니다.
- 아홉 상처는 존재·세계·통과의 신화적 원리이며 9인 사도 조직이 아니다.
- 종족은 인간, 에르나, 카르둔, 라하크, 네바르, 무명종 후보를 사용하되 이름은 SOFT LOCK이다.
- 신수는 지성·거부권을 가진 주권 주체이며 수집품이 아니다.
- 유산 수량은 플롯 사용처에서 역산한다.

## Absolute Rules

1. Gate 개방 전 원고·장면 산문·시험 집필 금지.
2. 설정에는 Plot Uses / First Reveal / Payoff / Permanent Result를 기록.
3. 플롯에는 관련 정본 링크 기록.
4. 참고작 문장·고유명사·장면·숫자 조직·동일 반전 복제 금지.
5. 강한 힘에는 비용·제약·대응책·접근권·소유권·거부권.
6. 인물 자동 충성 금지.
7. 주인공 권한·정답·유산 독점 금지.
8. 영구손실 자동복구 및 다른 시간대 버전 대체 금지.
9. 모든 승리는 다음 문제를 직접 만든다.
10. 적대 시스템의 실제 효용과 합리적 지지를 지우지 않는다.
11. 수치 범주와 고유 인원을 분리하고 합계식을 남긴다.
12. 사건·사망·능력·관계·권한·숫자·연대·정체·결말을 조용히 변경하지 않는다.
13. 변경은 decision log에 기록.
14. S0/S1이 있으면 CANON·완료 선언 금지.
15. 작가가 유일한 최종 승인자.

## Fixed Expert Agents

- A01 Architecture PM
- A02 Canon Controller
- A03 World & Geography
- A04 Magic & Disease
- A05 Peoples & Culture
- A06 Institution / Economy / Law
- A07 Temporal Systems
- A08 Character & Relationship
- A09 Faction & Antagonism
- A10 Collection & Reward
- A11 Mystery & MacGuffin
- A12 Grand / Act Architecture
- A13 Continuity & Loss
- A14 Reader Experience
- A15 Similarity Audit
- A16 Red Team
- A17 GitHub State Verifier
- A18 Prose — Gate OPEN 이후만

세부 책임과 승인 정족수는 `.agent/orchestra/agent-registry.md`가 정본이다.

## Production Pipeline

0. Repository sanitation
1. Project Charter / Canon Constitution
2. World Bible
3. Character / Faction / Institution Bible
4. Collection / Reward Bible
5. Ending reverse design
6. 5 Grand Acts / 15 Volumes
7. Arc / Subact causal matrix
8. Mystery / Payoff / Loss ledgers
9. E001–E375 detailed cards
10. Full cross-audit
11. Pre-Writing readiness review
12. Author-only Gate decision
13. Manuscript production after explicit OPEN

## Story Hierarchy

`Series → Grand Act → Volume Act → Arc → Subact → Batch → Episode → Scene`

Every level requires:

- Promise
- Goal
- Opposition
- Choice
- Cost
- Revelation
- Reward
- Loss
- State Change
- Next Cause
- Anti-Repeat

## Setting Fields

- Definition
- Reader Value
- Rules
- Limits
- Costs
- Abuse Cases
- Beneficiaries
- Harmed Parties
- Plot Uses
- First Reveal
- Payoff
- Permanent Result
- Related Files

## Batch Outputs

- Episode cards
- Character state
- Institution / faction state
- Collection / loss state
- Mystery / payoff state
- Number and chronology ledger
- Red-team audit
- Progress status
- Context handoff

## Red Team

- S0: series / canon fatal
- S1: Gate / Act / batch blocker
- S2: major persuasion or reader-risk
- S3: improvement

Mandatory checks:

- protagonist omnipotence
- enemy stupidity dependency
- rational opposition
- actual benefit and cost
- character autonomy
- continuity and permanent losses
- nonadditive numbers
- time / distance / logistics / language
- late rule insertion
- repeated mission / victory / hook / betrayal
- next-cause linkage
- reference-work similarity
- ending disconnected from opening

## GitHub Rules

- verify latest main
- create branch from latest main
- compare main...branch and require behind_by=0
- create PR
- squash merge
- re-fetch PR and verify state=closed / merged=true
- record actual merge SHA
- fetch representative files from main
- never report expected state as actual state

## Gate

AI cannot open the Pre-Writing Gate.

Only valid author declaration:

`Pre-Writing Gate를 OPEN한다. 권장된 첫 집필 배치를 시작해.`

Until then:

- manuscript BLOCKED
- Prose Agent disabled
- design, audit, correction and maintenance only
