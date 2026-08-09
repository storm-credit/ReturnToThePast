# D10 분야별 상세도·원고호출 준비도 감사

Status: **PASS — D10 ORCHESTRATION READY**  
Owner: A00 / A02 / A16 / A21  
Purpose: 문서 존재 여부가 아니라 실제 원고 장면에 호출 가능한 깊이와 라우팅을 판정

## 판정 기준

- READY: 장면에 필요한 기능·제약·상태·사용처가 있고 CP로 호출 가능
- CONDITIONAL: 핵심은 있으나 첫 사용 전 추가 dossier 필요
- BLOCKED: 원고 해결에 필수인데 상세도·연결·권한이 부족

## 종합표

| 분야 | 주요 정본·운영문서 | 최종 판정 | D10 조치 |
|---|---|---|---|
| 권한·정본 계층 | Constitution / Amendment / Decision Log / Governance | READY | Constitution의 [`CLAUDE.md`](../../CLAUDE.md) 의존 제거, 모델중립 권한계층 확정 |
| 모델별 진입점 | [`AI_PROJECT.md`](../../AI_PROJECT.md) / [`CLAUDE.md`](../../CLAUDE.md) / [`AGENTS.md`](../../AGENTS.md) | READY | 공통 정본을 가리키는 NON-CANON 얇은 라우터로 분리 |
| 시간여행·기억·인과 | `docs/03_systems/` | READY | CP에서 회차 관련 규칙만 추출, 새 규칙 후출 차단 |
| 지리·도시·공간 | Atlas / Capital / Geography | READY | 이동·출입·피난·보급을 Episode CP 필수 필드화 |
| 생활문화·언어·달력 | Culture / Language / Era Contrast | READY | 시대·지역에 필요한 항목만 선택 호출 |
| 인구·경제·직업·가격 | Demographic / Economy | READY | 수치 사용 시 A13 검증 |
| 군사·외교·물류 | Military Bibles | READY | 전투 CP에서 공간·통신·보급·부상 후과 동시 호출 |
| 종족·문화 | Peoples & Cultures | READY | 종족 전체 동일반응 금지 유지 |
| 종교·신화 | Nine Wounds + [`religion-ritual-clergy-encyclopedia-v2.md`](../02_world/religion-ritual-clergy-encyclopedia-v2.md) | READY | 성직계급·의례순서·축일·금기·성물·구휼·재판·생활 신앙 보강 |
| 기관·법·행정 | `docs/08_institutions/` | READY | 승인자·소요시간·우회로·실제 효용을 CP 필수화 |
| 세력·대립자 | `docs/04_factions/` | READY | 권/회차별 활성파벌과 독립행동 추출 |
| 핵심 인물 C01–C10 | Character Bibles | READY | D9 정식명과 ID 기준 정규화 |
| 조연 C11–C20 | [`supporting-cast-dossiers-c11-c20-v2.md`](../05_characters/supporting-cast-dossiers-c11-c20-v2.md) | READY | 외형·배경·말투·관계·부재 중 행동·전환·금지 보강 |
| 조연 C21–C30 | [`supporting-cast-dossiers-c21-c30-v2.md`](../05_characters/supporting-cast-dossiers-c21-c30-v2.md) | READY | 장면용 독립 dossier 완성, C30 익명성 잠금 |
| 관계·목소리 | Voice/Relationship Bible | READY | 핵심·조연 dossier와 CP 연결 |
| 연대유산 R01–R12 | Relic Encyclopedia | READY | 현재 소유·보관·접근·파손상태 추출 |
| 주권신수 B01–B05 | Beast Encyclopedia | READY | 생태·계약·거부권·정치 의미 호출 |
| 일반 소품·문서·의약·도구 | Daily Life / Economy / Institution | READY BY CP | 회차별 추출, 반복 사용 시 별도 prop index 승격 |
| 미스터리·복선·맥거핀 | M01–M17 / Reinforcement Ladder | READY | 공개상한·재점화·독자추론 시점 강제 |
| 영구손실 | Loss Ledger | READY | 매 회차 활성 손실과 회복금지 포함 |
| Grand Act·권·Subact 인과 | Architecture | READY | 국소완결→비용→Next Cause 유지 |
| 장면밀도·훅 | D9 Overlay | READY | Q/S/E/X와 훅 7종을 Craft Manifest에 연결 |
| 상황별 작법 선택 | `storycraft-orchestrator` | READY | 중심 작법 1개+보조 최대 2개, 부적합 작법·반복검사 |
| 보조 POV 실제 배치 | [`secondary-pov-and-offscreen-action-allocation-v1.md`](../10_story_architecture/secondary-pov-and-offscreen-action-allocation-v1.md) | READY | P1 30화, P2 15화, P3 8개 삽입과 재합류·정보상한 고정 |
| Context Pack | A21 / Compiler / Template / E001·E002 CP | READY | 원본경로·기준 ref·상태·stale Hook 확정 |
| Writing Harness | [`orchestration-harness-v2.md`](../13_writing_harness/orchestration-harness-v2.md) | READY | Authority→CP→Domain→Craft→POV→Draft→Audit→GitHub→State 연결 |
| E001 원고 | Manuscript / CP / Manifest / Retro Audit | READY / PASS | 사건·문장 재작성 없이 D10 소급감사 통과 |
| E002 준비 | E002 CP / Manifest | READY | D10 merge 후 A18 호출 가능 |

## 최초 차단항목과 종결

### S1-01 — Canon Router 혼동

- 발견: Constitution이 [`CLAUDE.md`](../../CLAUDE.md)를 상위 의존성처럼 사용
- 수정: 권한계층 분리, [`AI_PROJECT.md`](../../AI_PROJECT.md) 모델중립 라우터, Claude/Codex 얇은 라우터
- 상태: **CLOSED**

### S1-02 — 종교 장면 상세도

- 발견: 네 층 진실과 분파는 있으나 장면용 의례·계급·성물·금기·구휼·재판 부족
- 수정: [`religion-ritual-clergy-encyclopedia-v2.md`](../02_world/religion-ritual-clergy-encyclopedia-v2.md)
- 상태: **CLOSED**

### S1-03 — 조연 dossier 불균형

- 발견: C11–C30 일부가 역할·욕망 수준
- 수정: C11–C20, C21–C30 독립 장면용 dossier
- 상태: **CLOSED**

### S1-04 — 보조 POV 배치 부재

- 발견: 허용 원칙만 있고 회차별 목적·정보상한·재합류가 없음
- 수정: P1/P2/P3 회차 배치와 주인공 부재 행동 장부
- 상태: **CLOSED**

### S1-05 — Context Pack 부재

- 발견: 원고 에이전트가 필요한 정본을 읽었다는 증거 없음
- 수정: A21, CP Compiler, template, E001 소급 CP, E002 선행 CP
- 상태: **CLOSED**

### S1-06 — 상황별 작법 선택 체계 부재

- 발견: 결말 역산·맥거핀·장면 기능 규칙이 흩어져 있고 선택조건이 없음
- 수정: `storycraft-orchestrator`, Craft Manifest, E001/E002 적용
- 상태: **CLOSED**

## 오케스트라 권한 분리 결과

- A00: 총괄 라우팅, 정본 독단승인 금지
- A02: 정본·충돌·변경관리
- A20: 상황별 작법 선택, 사건 추가 금지
- A21: 정본 묶음·하네스, CP 정본화 금지
- A18: 승인된 설계 원고화, 즉석 설정 금지
- A19: 문장·낭독·이름·호칭·행동 품질
- A16: S0/S1 차단
- A17: GitHub 실재 검증

## 집필 상태 판정

- Gate Authorization: OPEN
- D10 Infrastructure: READY
- E001: CANON MANUSCRIPT / D10 PASS
- E002: CP READY / CRAFT READY / A18 NEXT
- E003+: 회차별 CP와 Manifest를 선행 생성한 뒤 진행

## 완료 정의 충족

1. 필요한 분야 상세 존재 — PASS
2. 권한 계층 명확 — PASS
3. Episode CP가 원본 출처·상태를 묶음 — PASS
4. Craft Manifest가 상황별로 선택됨 — PASS
5. 보조 POV와 주인공 부재 행동 추적 — PASS
6. Hook가 누락·충돌·stale을 차단 — PASS
7. 원고 후 상태 장부 갱신 경로 존재 — PASS

## Final Severity

- S0: 0
- S1: 0
- S2: 2
  - 실제 집필에서 보조 POV 빈도·리듬 조정 가능
  - 일반 소품이 반복되면 prop index 분리 필요
- S3: 지속 개선

**D10 판정: PASS — 모델중립 정본 우선 오케스트라가 설계·세계관·설정집을 회차 원고에 호출할 수 있는 구조로 준비됨.**
