# Deep Context Pack Blindspot Red Team v1

Status: ACTIVE — MUST PASS BEFORE FULL-SERIES MAIN MERGE
Date: 2026-08-20
Scope: E001–E375 Static Deep Context + JIT Runtime State Overlay

## 1. 목적

Context Pack을 깊게 만들수록 발생하는 역효과를 적대적으로 검수한다. Pack은 집필을 돕는 생산 입력이지, 새로운 정본이나 미래 사건 자동확정기가 아니다.

## 2. S0 — 즉시 중단 결함

1. Canon/결말/인물의도를 Pack이 새로 발명함
2. 미래 Episode의 실제 Exit/성공 여부를 선결정함
3. 영구사망·영구손실·소유권 변화가 이전 상태로 리셋됨
4. POV가 알 수 없는 정보를 현재 지식으로 주입함
5. Mystery 최종정답이 허용시점보다 선행함
6. Graph link 존재를 등장 허가로 오해함
7. 같은 Episode가 2개 Subact에 중복 소속됨
8. 다음 화 인과가 현재 화 선택/비용과 연결되지 않음

## 3. S1 — 반드시 수정해야 하는 맹점

### Authority / Staleness
- Historical CP와 Current Deep Pack의 권한 차이가 모호함
- 후대 Amendment가 Pack에 반영되지 않음
- 같은 사실을 여러 Pack에 복제해 서로 다른 값으로 드리프트
- 상태 문서와 실제 원고가 다르지만 Pack이 상태 문서만 신뢰

### Timeline / Boundary
- E063–E069, E082–E088 같은 Subact 경계 예외를 잘못 라우팅
- Volume/Grand Act 경계에서 관계·소유·기관 권한을 자동 리셋
- 날짜/나이/주관적 누적일 metadata가 chronology와 충돌

### POV / Character Agency
- 에이든 중심 시점으로 모든 보조인물 독립행동이 흡수됨
- P1/P2/P3를 장식용으로만 넣고 실제 정보상한을 구분하지 않음
- 아이리스·리아·나하 등이 주인공의 정보 제공기/양심으로 축소
- 같은 직업군 인물의 말투·결정 방식이 수렴

### Mystery / Evidence
- 이미 공개한 단서를 뒤에서 첫 단서처럼 반복
- 하나의 증거 유형으로 최종진실을 판정
- B05 등 생태증거를 truth judge로 승격
- 기록=거짓이라는 단일 해석으로 미스터리 전부 수렴
- false interpretation과 reader inference ceiling을 구분하지 않음

### Institution / Politics / Economy
- 관료제·왕실·성당·군을 편의적 악역으로 단순화
- 제도의 실제 효용과 비용이 Pack 압축 과정에서 사라짐
- 법적 권한과 물리적 능력을 혼동
- 경제/물류 비용 없이 결정이 실행됨

### Assets / Losses
- 유산을 에이든 개인 loot처럼 처리
- 법적 소유권·공동체 소유·보관처가 사라짐
- 신수를 펫/탈것/판정도구로 사용
- Final relic state를 강화형으로 오독
- 파괴/분산/매장된 자산을 후속 Pack에서 완전형으로 호출

### Visual
- 미래 Variant 선행
- C01/C08/C29/C30 시각문법 혼동
- 사망인물의 현재형 Variant 호출
- Visual Anchor를 장면 등장 근거로 역사용
- 모든 장소에 layered-history motif를 같은 방식으로 반복

### Craft / Pacing
- 모든 Pack이 Goal/Opposition/Choice/Cost 문구만 바꾼 같은 구조
- Q/S/E/X 밀도 차이가 실제 장면설계에서 사라짐
- 직전 화와 같은 회의→문서→경보 패턴 반복
- 미스터리·제도·감정 훅이 한 종류로 수렴
- 설명량이 과도해 실제 원고가 Bible 재진술이 됨

### Runtime State
- 아직 쓰지 않은 전 화의 결과를 exact state로 고정
- 'planned state change'와 'achieved state' 혼동
- offscreen transition 허용범위 미표시
- 이전 원고 Exit가 바뀌어도 Static Pack을 고치려 함 — Runtime Overlay에서 처리해야 함

### Obsidian
- wikilink 오타로 ghost node 생성
- alias 때문에 같은 인물이 복수 node로 분열
- Pack에 양방향 링크를 중복해 graph가 과밀해짐
- node_id가 파일명 변경에 따라 바뀜
- Graph centrality를 Canon importance로 오해

## 4. 알려진 초기 표본 결함

현재까지 실제 발견된 사례:

- E003: M02 사망일 단서가 후대 E033에 중복 배치된 stale mystery rung
- E006: chronology exact date와 historical CP/frontmatter 불일치
- E007: active POV allocation은 C03 Iris P1인데 historical CP/manuscript는 Aiden close 3rd
- E069: historical grouped pack이 3C→3D 경계를 가로지름
- E088: historical grouped pack이 4B→4C 경계를 가로지름

이 5종은 전체 375 Pack QA의 회귀 테스트로 사용한다.

## 5. Context Bloat Gate

Deep Pack은 깊되 Bible 복사본이 되면 FAIL.

Episode Entry는 다음을 중심으로 한다.
- 현재 장면에 실제 필요한 사실
- 현재 인물의 지식한계
- 이번 선택이 바꿔야 할 상태
- 금지/선취 방지
- 다음 인과

장문의 세계관 설명은 source pointer로 남긴다.

## 6. Cross-Pack tests

전체 생성 후 반드시 실행:

1. 375 Episode ownership uniqueness
2. 374 handoff edge 존재
3. 60 Subact Entry/Exit chain
4. 15 Volume Exit→Next Volume Entry
5. 5 Grand Act transition
6. permanent death/loss monotonicity
7. relic ownership/custody monotonicity
8. mystery first-plant/reinforcement/reveal chronology
9. POV P1/P2/P3 allocation coverage
10. visual variant chronology
11. institution/faction appearance legality
12. duplicate clue / duplicate hook / repeated scene pattern
13. runtime-only field premature-freeze scan
14. Obsidian ghost-node/link scan

## 7. Pass condition

- S0 = 0
- Blocking S1 = 0
- known E003/E006/E007/E069/E088 regression cases explicitly resolved
- 375/375 Static Deep Entry coverage
- 60/60 Subact masters complete
- 374/374 episode handoff edges identifiable
- main merge only after the above

HUMAN PROSE PASS는 별도이다.
