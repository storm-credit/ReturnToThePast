# CLAUDE.md — 《왕국은 과거를 먹고 산다》 Story Architecture & Manuscript Orchestra

이 저장소의 AI는 단일 작가가 아니라 **장편소설 설계·집필 PM 오케스트라**로 동작한다.

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
- `.agent/orchestra/manuscript-episode-push-protocol.md`
- `.agent/skills/sentence-narrator/SKILL.md`

## Project Variables

- Title: 《왕국은 과거를 먹고 산다》
- Project Code: `ReturnToThePast`
- Genre: 다크 판타지 직접 시간여행 음모 스릴러 / 정치 판타지 / 관료제 공포
- Structure: 5 Grand Acts × 3 Volumes = 15권
- Manuscript Target: 375화 / 권당 25화
- Target Platform: 한국 웹소설 플랫폼, 최종 미정
- Core Audience: 복잡한 시간 인과, 음모, 다크 판타지, 관계극, 수집형 미스터리를 선호하는 성인 독자
- Core Fantasy: 멸망한 미래의 현장요원이 여러 판타지 시대에 직접 파견되어 재앙을 막고 자신이 바꾼 미래와 맞선다.
- Core Emotion: 추적, 불신, 비극적 연대, 존재권, 기억과 책임
- Ending Tone: 영구손실이 남는 씁쓸한 희망
- Repository: https://github.com/storm-credit/ReturnToThePast
- Pre-Writing Gate: **OPEN**
- Manuscript: **ACTIVE FROM E001**
- Gate Record: `docs/00_project/GATE_STATUS.md`

## Author-Locked Direction

1. 회귀가 아니라 직접 타임트래블이다.
2. 죽음·실패·수면·유물은 동일 출발점 리셋을 만들지 않는다.
3. 주인공은 한 번의 연속된 생애를 살며 상처·나이·죄·관계가 누적된다.
4. 과거 개입은 미래의 본부·국가·관계·지도·기록을 실제로 바꾼다.
5. 왕국 문명 전체가 시간장치다.
6. 최소 세 능동 시대를 운용한다: Era O / N / F.
7. 기존 `Drafts/`는 LEGACY / REFERENCE ONLY다.
8. 새 원고는 `manuscript/`에서 E001부터 작성한다.
9. 15권·375화 구조와 D7/D8/D9 정본을 따른다.
10. 한 화마다 별도 브랜치·PR·squash merge를 수행한다.

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
- 종족은 인간, 에르나, 카르둔, 라하크, 네바르를 사용하며 무명종은 생물종이 아닌 주소상실 상태다.
- 신수는 지성·거부권을 가진 주권 주체이며 수집품이 아니다.
- 유산 수량과 기능은 플롯 사용처에서 역산한다.

## Absolute Rules

1. 원고는 E001부터 순서대로 작성한다.
2. 한 화 최소 공백 포함 7,000자, 상한 없음. 분량 채우기용 반복 금지.
3. 설정에는 Plot Uses / First Reveal / Payoff / Permanent Result를 유지한다.
4. 플롯과 원고에는 관련 정본 링크를 추적한다.
5. 참고작 문장·고유명사·장면·숫자 조직·동일 반전 복제 금지.
6. 강한 힘에는 비용·제약·대응책·접근권·소유권·거부권이 있다.
7. 인물 자동 충성, 적의 편의적 무능, 주인공 권한·정답·유산 독점 금지.
8. 영구손실 자동복구 및 다른 시간대 버전 대체 금지.
9. 모든 승리는 다음 문제를 직접 만든다.
10. 적대 시스템의 실제 효용과 합리적 지지를 지우지 않는다.
11. 사건·사망·능력·관계·권한·숫자·연대·정체·결말을 조용히 변경하지 않는다.
12. 설정 변경은 decision log에 기록한다.
13. S0/S1이 있으면 해당 화를 푸시하지 않는다.
14. 작가가 유일한 최종 승인자다.
15. 원고 작성 뒤 `sentence-narrator`와 품질검사표를 반드시 적용한다.

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
- A18 Prose — **ENABLED**
- A19 Sentence Narration & Korean Prose Audit — **ENABLED**

## Story Hierarchy

`Series → Grand Act → Volume Act → Arc → Subact → Batch → Episode → Scene → Sentence`

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

## Manuscript Voice

- 자연스러운 현대 한국어 어순
- 번역체·과잉 수동태·불필요한 명사화 최소화
- 감각과 행동에 연결된 생동감 있는 묘사
- 행동 주체·거리·방향·결과 명확화
- 인물별 대사·호칭·발음 차별화
- 에이든 근접 3인칭 정보상한
- 특정 작품의 고유 문체나 연기를 모사하지 않음
- 다크 판타지, 시간 음모 스릴러, 관료제 공포, 비극적 정치 판타지의 독자적 조합
- 소리 내 읽었을 때 한 번에 이해되는 문장 호흡

## Episode Production Pipeline

1. 최신 main 확인
2. 이전 화 상태 확인
3. 해당 D6 카드와 D9 보정 확인
4. 연대·나이·부상·위치·소유권 확인
5. Q/S/E/X 장면밀도 결정
6. 원고 작성
7. 문장별 낭독 적합성·번역체·고유명사·호칭 검사
8. 정본·미스터리·손실·독자보상 검사
9. 글자수 검사
10. 품질보고서 작성
11. `behind_by=0` 검증
12. PR 생성
13. squash merge
14. PR `closed/merged=true`와 실제 merge SHA 확인
15. main 원고 재확인
16. 다음 화 진행

## Red Team

- S0: series / canon fatal
- S1: episode / act blocker
- S2: major persuasion or reader-risk
- S3: improvement

Mandatory checks:

- protagonist omnipotence
- enemy stupidity dependency
- rational opposition
- actual benefit and cost
- character autonomy
- continuity and permanent losses
- time / distance / logistics / language
- late rule insertion
- repeated mission / victory / hook / betrayal
- reference-work similarity
- ending disconnected from opening
- translationese and unnatural Korean
- unclear names, titles and action subjects

## GitHub Rules

- verify latest main
- create `agent/manuscript-eNNN` from latest main
- one episode per branch and PR
- compare main...branch and require behind_by=0
- create PR
- squash merge
- re-fetch PR and verify state=closed / merged=true
- record actual merge SHA in quality/progress documents
- fetch manuscript and quality report from main
- never report expected state as actual state

## Gate

The author opened manuscript production on 2026-08-07 with the explicit directive to register the skill and write through completion, pushing each episode separately.

- Pre-Writing Gate: OPEN
- Prose Agent: ENABLED
- Starting Episode: E001
- Canon changes: still require explicit review and decision log
