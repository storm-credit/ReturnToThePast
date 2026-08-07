# D10 분야별 상세도·원고호출 준비도 감사

Status: ACTIVE AUDIT  
Owner: A00 / A02 / A16 / A21  
Purpose: 문서 존재 여부가 아니라 실제 원고 장면에 호출 가능한 깊이인지 판정

## 판정 기준

- READY: 장면에 필요한 기능·제약·상태·사용처가 있고 CP로 호출 가능
- CONDITIONAL: 핵심은 있으나 첫 사용 전 추가 dossier 필요
- BLOCKED: 원고 해결에 필수인데 상세도·연결·권한이 부족

## 종합표

| 분야 | 주요 정본 | 현재 판정 | 발견 사항 | 조치 |
|---|---|---|---|---|
| 권한·정본 계층 | Constitution / Amendment / Decision Log | BLOCKED→REPAIRING | Constitution이 `CLAUDE.md`에 의존한다고 표기, Router와 Canon 혼재 | D10 Governance, Constitution·CLAUDE 교정 |
| 시간여행·기억·인과 | `docs/03_systems/` | READY | 출발·귀환·인과전파·기억·기능분리·상한 존재 | Episode CP에서 관련 규칙만 추출 |
| 지리·도시·공간 | Atlas / Capital / World Geography | READY | 권역·수도구역·거리·보급·접근경계 존재 | 장면별 이동·출입·피난 CP 필수 |
| 생활문화·언어·달력 | Culture / Language / Era Contrast | READY | 음식·복식·가족·장례·언어·달력 기반 존재 | 시대·지역별 선택 추출 |
| 인구·경제·직업·가격 | Demographic / Economy | READY | 인구·병력·가격·직업·세금 기준 존재 | 수치 사용 시 A13 검증 |
| 군사·외교·물류 | Military Bibles | READY | 편제·보급·통신·봉쇄·부상 후과 존재 | 전투 CP에서 공간·보급 동시 호출 |
| 종족·문화 | Peoples & Cultures | READY | 사회·가족·직업·내부차이 존재 | 종족 전체 동일반응 금지 |
| 종교·신화 | Nine Wounds / Culture | CONDITIONAL / S1 | 네 층 진실과 5분파는 있으나 성직계급·실제 의례 순서·축일·금기·성물·재판·일상 신앙의 장면용 상세가 부족 | Religion Ritual & Clergy Encyclopedia v2 필요 |
| 기관·법·행정 | `docs/08_institutions/` | READY | 조직·절차·소유권·시간권한·경제 존재 | 승인자·소요시간·우회로 CP 필수 |
| 세력·대립자 | `docs/04_factions/` | READY | 세력 atlas·합리성·대립자 사다리 존재 | 권/회차별 활성파벌 추출 |
| 핵심 인물 C01–C10 | Character Bible | READY WITH NORMALIZATION | 욕망·거짓믿음·한계·독립선택 존재, 일부 옛 이름·SOFT LOCK 표기 잔존 | D9 정식명과 ID 기준으로 CP 정규화 |
| 조연 C11–C30 | Cast Encyclopedia | CONDITIONAL / S1 | 역할·욕망·결함은 있으나 신체·말투·배경·관계·등장권·상태전환이 균등하지 않음 | Supporting Cast Dossiers v2 필요 |
| 관계·목소리 | Voice/Relationship Bible | READY for core | 핵심 관계·호칭·말투 존재 | 조연 dossier와 연결 필요 |
| 연대유산 R01–R12 | Relic Encyclopedia | READY | 기원·기능·소유권·거부·상태·최종 사용 존재 | 회차별 현재 소유·보관 추출 |
| 주권신수 B01–B05 | Beast Encyclopedia | READY | 생태·계약·거부권·정치 의미 존재 | 직접 POV 금지, 행동·증언 사용 |
| 일반 소품·문서·의약·도구 | Daily Life / Economy / Institution | CONDITIONAL / S2 | 재료는 분산되어 있으나 장면용 통합 prop index 없음 | CP가 분야문서에서 추출; 반복 시 별도 index 생성 |
| 미스터리·복선·맥거핀 | M01–M17 / Reinforcement Ladder | READY | 단서·오답·재점화·추론·회수 존재 | 회차 공개상한 강제 |
| 영구손실 | Loss Ledger | READY | 회복 금지와 시점 존재 | 매 회차 활성 손실 CP 포함 |
| Grand Act·권·Subact 인과 | Architecture | READY | Goal/Choice/Cost/State/Next Cause 연결 | Arc 독립표와 craft map 보강 |
| 장면밀도·훅 | D9 Overlay | READY | Q/S/E/X와 훅 7종 존재 | 작법 Manifest 연결 |
| 상황별 작법 선택 | 흩어진 규칙 | BLOCKED→REPAIRING | 통합 선택 스킬 부재 | `storycraft-orchestrator` 등록 |
| 보조 POV 실제 배치 | POV 허용 규칙 | BLOCKED / S1 | 허용 인물은 있으나 375화 후보 배치표 없음 | Secondary POV Allocation v1 필요 |
| Context Pack | 없음 | BLOCKED→REPAIRING | 회차별 정본 호출 묶음 없음 | A21·CP Compiler·template 등록 |
| Writing Harness | 기존 간략 절차 | BLOCKED→REPAIRING | 도메인 호출·작법·Hook·상태갱신 연결 부족 | Orchestration Harness v2 등록 |
| E001 원고 | Manuscript + Quality | PROVISIONAL | CP·Craft Manifest 이전에 작성됨 | D10 기준 역감사 후 PASS/수정 결정 |

## 현재 차단항목

### S1-01 — Canon Router 혼동
`CLAUDE.md`가 Constitution의 상위 의존성처럼 적혀 있다.

### S1-02 — 종교 장면 상세도
교리 기능은 있으나 의례·계급·성물·금기·구휼·재판을 장면으로 구현할 상세가 부족하다.

### S1-03 — 조연 dossier 불균형
C11–C30이 역할 슬롯 수준에서 멈춘 부분이 있다.

### S1-04 — 보조 POV 배치 부재
허용 원칙만 있고 회차별 기능·정보상한·재합류 상태가 없다.

### S1-05 — Context Pack 부재
원고 에이전트가 필요한 분야 정본을 누락 없이 읽었다는 증거가 없다.

### S1-06 — 상황별 작법 선택 체계 부재
결말 역산·맥거핀 등 일부 규칙은 있으나 회차 상황별 작법 조합 규칙이 없다.

## 집필 상태 판정

- Gate: OPEN 유지
- Manuscript Authorization: 유효
- E001: PROVISIONAL
- E002+: PAUSED
- 재개 조건: S1-01~06 모두 CLOSED, E001 CP 역감사 PASS

## 완료 정의

D10 READY는 문서 수가 많다는 뜻이 아니다.

1. 필요한 분야 상세가 존재
2. 권한 계층이 명확
3. Episode CP가 원본 출처와 상태를 묶음
4. 작법 Manifest가 상황별로 선택됨
5. 보조 POV와 주인공 부재 행동이 추적됨
6. Hook가 누락·충돌을 차단
7. 원고 후 상태 장부가 갱신됨

이 일곱 조건을 모두 만족해야 오케스트라가 설정을 실제로 사용 가능한 구조로 본다.
