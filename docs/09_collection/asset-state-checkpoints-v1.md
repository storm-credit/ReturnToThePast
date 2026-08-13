# Asset State Checkpoints v1

Status: ACTIVE LEDGER  
Owner: Collection / Continuity

| Asset | First State | Transfer / Reuse | Final State |
|---|---|---|---|
| 회색 종 | 성당의 열병 탐지물 | 도시 주소·현재 증언 감지로 재해석 | 지역 감사망에 반환, 감염자 낙인 기능 폐지 |
| 빈 세금장부 | 삭제된 지방 부담의 흔적 | F2 폭로·무명명부·시민권 증거 | 공공 무명명부 원본, 개인 소유 금지 |
| 개혁가의 절검 | 에이든 전리품처럼 보임 | 유족 소유권 인정, 증거·방어에 제한 사용 | E366 파괴, 복원 금지 |
| F0 귀환패 | 원래 미래 복원키처럼 보임 | 현재 고정망 주소·구조에 사용 | F0 복원키 아님을 공개, 봉인 |
| 백지도 | 사라진 도시 위치표 | 건국 경로·무명권·전쟁 지도에 재사용 | 새 지역 협약지도 기반 |
| 카르둔 경계갑 | 공동소유 방어구 | 에이든 신분 부식, 다중 시대 방어 | 분해되어 지역 고정망 재료가 됨 |
| 건국 모루 | 공동 기반시설 제작도구 | 감사권·생활망 구축에 재사용 | 지역망 제작 후 원위치/공동관리 |
| 에르나 기억피 | 개인 신체 기억 | 성인신화 해체·젊은 에이든·최초연대기 검증 | 공공 증거 전환 후 기능 상실 |
| 네바르 장례보석 | 사망 증언 저장 | 건국·지휘관 사망·최종 기록 검증 | 지휘관 증언 보존 후 매장 |
| 초대왕의 무관 | 단독 승인권 후보 | 공동승인·감사 협약의 법적 증거 | 중앙 승인 해체와 함께 녹여 분산인장 제작 |
| 다른 에이든의 방패 | 다른 미래의 전투유산 | 실패한 선택 증거·최종 방어 | 공공보관, 원주인 대체 금지 |
| 최종 감사인장 | 중앙 정지키처럼 보임 | 다중 거부권·기능분리 절차 | 한 물건이 아니라 공개 감사절차로 분산 |

## Sovereign Beast State Rule

- 주권신수는 보유목록이 아니라 동맹·증언·이동·감지 관계로 추적한다.
- 계약 종료·이탈·거부가 가능하다.
- 사망 시 다른 시대 개체로 대체하지 않는다.

## Volume Custody Track V1–V15

이 절은 기존 3단계 표(최초/이전/최종)를 대체하지 않는다. 같은 12개 자산을 **권별 소유·보관·사용가능** 축으로 다시 추적한다.

### 1. 표기 코드

상태코드는 새로 만들지 않고 `relic-encyclopedia-r01-r12-v1.md` §유산 상태코드를 그대로 쓴다.

| 코드 | 원문 정의 | 이 절의 사용 |
|---|---|---|
| A | ACTIVE — 본래 기능 사용 가능 | 조건 없이 사용 가능 |
| L | LIMITED — 일부 기능·동의 조건 | 조건부 사용 |
| E | EVIDENCE — 증거 기능만 유지 | 증거 제출용, 도구 사용 불가 |
| S | SHARED — 공동소유·다중승인 | 다중 서명·공동체 승인 필요 |
| R | RETURNED — 원공동체 반환 | 점유가 원권리자에게 있음 |
| DM | DISMANTLED — 생활인프라로 분해 | 유산으로서 사용 불가 |
| SE | SEALED — 접근 제한·재심 가능 | 봉인, 사용 불가 |
| DS | DESTROYED — 복구 불가 | 소멸 |
| · | — | 해당 권의 정본 근거 없음 (미추적) |

### 2. 마스터 그리드 — 자산 × 권

| ID | 자산 | V1 | V2 | V3 | V4 | V5 | V6 | V7 | V8 | V9 | V10 | V11 | V12 | V13 | V14 | V15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R01 | 회색 종 | S | E | E⚠ | E⚠ | · | · | · | E | · | · | · | · | E | · | R |
| R02 | 빈 세금장부 | ·⚠ | E | E | E | · | E | · | · | · | · | · | · | E | · | S |
| R03 | 개혁가의 절검 | L | E | R | · | · | · | L | · | · | L | · | ·⚠ | · | · | DS |
| R04 | F0 귀환패 | · | L | L | L | L | · | · | · | · | · | · | · | E | SE | SE |
| R05 | 존재하지 않는 도시의 지도(백지도) | · | · | · | L | · | · | L | · | · | L | · | · | L | · | S |
| R06 | 카르둔 경계갑 | · | · | · | · | S | R | L | · | · | S | L | L | · | · | DM |
| R07 | 건국 모루 | · | · | · | · | · | E | S | · | S | · | · | · | L | · | DM |
| R08 | 에르나 기억피 | · | · | · | E | · | · | S | E | E | · | E | · | · | E | E |
| R09 | 네바르 장례보석 | · | · | · | · | · | · | · | E | · | · | · | E | · | E | E |
| R10 | 초대왕의 무관 | · | · | · | · | · | · | · | · | S | · | · | S | · | · | ⚠ |
| R11 | 다른 에이든의 방패 | · | · | · | · | · | · | · | · | · | L/SE | L | · | · | L | SE |
| R12 | 최종 감사인장 | · | · | · | ⚠ | · | · | · | · | · | · | · | S | S | S | S |

⚠ = 정본 간 충돌 또는 근거 불명. §6 참조.

### 3. 권별 소유·보관·사용 상세

| ID | 권 | 법적 소유권자 | 실제 보관·점유 | 사용 가능 여부 | 근거 |
|---|---|---|---|---|---|
| R01 | V1 | 벨하임 마을 공동체 + 성당 공동소유 | 현지 종루에 잔존 (칼레온 대기록소가 증거물 압수 시도, 지역 반환의무 존재). 종 조각 일부는 F0 임무평의회가 역사주소 산출용으로 압수 보관 | S — 현지 잔존, 에이든 귀환석과 공명 | RE, V01, OV1 |
| R01 | V2 | 동일 | F1 재료검사실에 파편 기록만 존재 | E — 실물 아닌 기록 대조 | V02 |
| R01 | V3–V4 | 동일 | 현지 | E — 개혁가 주장 입증 보조 | RE, MAL |
| R01 | V8 | 동일 | 현지 | E — 기억문·장례보석과 함께 소실도시 이름 고정 | V08 |
| R01 | V13 | 동일 | 현지 | E — 혈통명부가 아닌 현재 증언에 반응, 움브라 시민권 보조 | G5(E304), V13, RE |
| R01 | V15 | 지역 감사망 | 지역 감사망 경보장치 | R — 주인공 장비가 되지 않음 | RE, CHK |
| R02 | V2 | 지방관청 원본 / 주민 공동정보권 | 에이든이 확보 후 개인 소유가 아닌 분산 보관. 영웅 접근권 일부를 리아에게 이양 | E | G1(E036–E037), V02 |
| R02 | V3 | 동일 | 왕실이 원본 소각을 강요 → 분산 복제, 일부 원본 포기 | E — 중앙 부담배분표와 대조 가능 | G1(E060), V03 |
| R02 | V4 | 동일 | 분산 사본 | E — 백지도·생존자 기억과 3중 대조 | V04 |
| R02 | V6 | 동일 | 분산 사본 | E | MAL |
| R02 | V13 | 주민 공동정보권 | 움브라 임시명부 근거자료 | E | G5(E305), V13, MML(M05) |
| R02 | V15 | 공공 | 복수원본 공공기록 | S — 단일 성물화 금지, 개인 소유 금지 | RE, CHK, WSC |
| R03 | V1 | 세렌 바일 유족·운동·현지 공동체 | 에이든이 표적 사망 후 회수해 F1로 동반 등록 | L — 기능·소유권 미확정, 전리품 아님 | G1(E024), V01, RE |
| R03 | V2 | 동일 | F1 재료검사실 → 분산 법적 보관처 | E — F1에 존재하지 않는 카르둔 공방 제작자명 확인 | G1(E032), V02 |
| R03 | V3 | 유족 | 유족 반환청구권 인정, 에이든 소유권 포기 | R — 에이든 독점 금지, 봉인절단·증거에 한정 | G1(E062), V03 |
| R03 | V7 | 유족 | 에이든 휴대 | L — Era O 생존연합에 공개하지 않기로 선택 (비사용) | V07 |
| R03 | V10 | 유족 | 에이든 휴대 | L | MAL |
| R03 | V15 | 유족 | 파편 상태 | DS — 복원파 강제경로 지연에 소모 후 완전 파괴, 재주조 금지 | G5(E366), V15, RE |
| R04 | V2 | F0 본부 장비였으나 발급기관 소멸로 법적 공백 | 파편을 리아가 보관, 에이든 사용 제한 | L | MAL, G1(E033–E037), V02 |
| R04 | V3 | 동일 | 리아 | L — 강제복원에 사용하지 않음 | V03 |
| R04 | V4 | 동일 | 원정대 자원 | L — 잔여 자원 부족 상태로 계산됨 | V04 |
| R04 | V5 | 동일 | 에이든 | L → 고립자 주소 고정에 소모. F0 잔류서명 대부분 소실 | G2(E105, E122), V05 |
| R04 | V13 | 소유권자 부재 | 법정 제출 | E — 개인전유 아닌 공공증거·제한사용 유산으로 판정 | G5(E307), V13 |
| R04 | V14 | 공공 | 공개검증 후 분산봉인 | SE — F0 복원키 아님을 공개 | G5(E349), V14, RE |
| R04 | V15 | 공공 | 봉인 | SE — 기능 종료. 에이든의 출발인장은 최종 다리에 소모 | V15, RE |
| R05 | V4 | 측량사 길드 · 도시 생존자 · 칼레온 대기록소 공동주장 | 원정대 휴대 | L — 도시명·경계 절반만 기록됨. 통행 가능성을 보장하지 않음 | G2(E076–E080), V04, RE |
| R05 | V7 / V10 / V13 | 동일 | 도시 증언자들이 갱신 | L | MAL |
| R05 | V15 | 공공 | 공개 지리레이어로 분해 보존 | S — 단일 비밀지도 금지, 새 협약 지역지도 기반 | RE, MAL, CHK |
| R06 | V5 | 카르둔 공방 · 국경 정비조 공동소유 (왕실 보관물이나 카르둔이 제작·장례 소유권 주장) | 사용권 대여 | S — 공동소유 조건 수용, 에이든 전유물 등록 금지. 대가는 공적 신분 부식 | G2(E107–E112, E123), V05, RE |
| R06 | V6 | 카르둔 | 반환·수리 단계 | R — 에이든 이름 부식 지속 | V06 |
| R06 | V7 | 카르둔 | 파편을 건국 모루에 시험 | L — 후대 소유권 충돌로 모루가 거부반응 | V07 |
| R06 | V10 | 카르둔 | 대여 | S | MAL |
| R06 | V11 | 카르둔 | 착용 | L — 착용자의 현재 이름을 인식하지 못하기 시작 | G4(E258), V11 |
| R06 | V12 | 카르둔 | 착용 | L | MAL |
| R06 | V15 | 카르둔 공방 합의 | 계절·의료·토지 노드 재료로 재제작 | DM — 시간저항 기능 대부분 영구 상실 | G5(E357), V15, RE |
| R07 | V6 | 건국 다종족 연합 공동소유 | 파편만 존재 | E — Era O 좌표 연결증거 | G2(E145), V06 |
| R07 | V7 | 동일 | 카르둔 공방과 공동 제작권 | S — 미래 합금 거부. 공동관리·공개로그·중단권 잠금 | G3(E157–E162), V07 |
| R07 | V9 | 동일 | 현지 공동운영에 남김 | S | V09 |
| R07 | V13 | 동일 | 생활안정망 재료로 전환 시작 | L — 전투·건국상징 기능 상실 | G5(E323), V13 |
| R07 | V15 | 동일 | 지역 의료·수문·고정망 부품으로 소모 | DM — 원형기능 상실. 제작 후 원위치·공동관리 | G5(E357), V15, RE, CHK |
| R08 | V4 | 기억 보유자 (철회 가능한 동의가 최우선) | 에르나 증언자 본인 | E — 네바르 장례기록과 대조해 성인 이름 검증 | V04 |
| R08 | V7 | 동일 | 증언자 참여 | S — 모루 가동 5조건 중 하나 | V07 |
| R08 | V8 | 동일 | 열람 | E — 미래 상처 오염 발견. 증언자 한 명의 기억문 손실 | V08 |
| R08 | V9 | 동일 | 열람 | E — 서명 직후 기억문이 변형되는 것을 관측 | V09 |
| R08 | V11 / V14 | 동일 | — | E — 강제사용 금지 | MAL |
| R08 | V15 | 동일 | 공공증거는 익명화·분산보존, 사적기억은 보호 | E — 동의 기반. 공공 전환 후 원기능 상실 | RE, CHK, WSC |
| R09 | V8 | 네바르 유족 (동의 필수) | 장례 절차 보관 | E — 마지막 감각만 재생, 인격 아님. 기억문과 다른 창립자를 지목 | G3(E184), V08 |
| R09 | V12 | 동일 | 마르칸 베르의 마지막 증언 기록 | E — 지휘관의 영구사망을 대체하지 않음 | G4(E298), V12, RE |
| R09 | V14 | 동일 | — | E | MAL |
| R09 | V15 | 동일 | 공공장례 기록으로 매장 | E | RE, CHK |
| R10 | V9 | 세르바 왕실 vs 건국연합 후손·지역대표 분쟁 | Era O 왕관 형성 현장 | S — 빈 중심틀 구조 확인 후 독립인장·정족수·물리분리 회로 삽입, 승인권 분할 | SCM(9C), V09, RE |
| R10 | V12 | 동일 | — | S — 공동승인·감사 협약의 법적 증거 | MAL, CHK |
| R10 | V15 | 미확정 (§6-4 충돌) | 미확정 | ⚠ | MAL, RE, CHK, WSC |
| R11 | V10 | 제작 공동체 · 다른 에이든의 피해자 · 현재 보관자 모두 권리 보유 | F3 한 국가의 금고 → 보관계약 확인 후 다자증거보관 | L(외피 제한사용) / SE(기억코어 봉인) — 방패가 현재 에이든을 원주인으로 거부. 압수 주장 대치 | G4(E238–E243), V10, RE |
| R11 | V11 / V14 | 동일 | 다자증거보관 | L — 사용 시 다른 미래의 피해잔향으로 정신·신체 부담 | MAL, RE |
| R11 | V15 | 동일 | 공공보관 | SE — 외피기능 소진, 기억코어 봉인. 현재 에이든의 상징무기로 계승 금지 | G5(E366), V15, RE, CHK |
| R12 | V11 | 일곱 운영권 분산 | 위치정보만 확보 | · — 한 사람이 쓸 열쇠가 아님이 확정됨 | G4(E275), V11 |
| R12 | V12 | 왕좌 목적·솔라 종탑 동기화·아스트라 관측탑 좌표·기록주소·귀환·지역부담·독립감사 7권 | 조립 완료 | S — 일곱 서명 필수, 단독 사용 봉인 | G4(E280–E287), V12, RE |
| R12 | V13 | 동일 | 지역 거부권과 결합 | S — 중앙 재가동 회로 차단에 사용 | V13 |
| R12 | V14 | 동일 | 최종 감사망 가동 | S | SCM(14D), MAL |
| R12 | V15 | 지역 감사망 | 표준절차로 분해 | S — 한 물건이 아니라 공개 감사절차. 재조립 금지 | V15, RE, CHK |

### 4. 추적 규칙

- **미추적 칸(`·`)은 부재가 아니라 정본 미기재다.** 해당 권에서 자산을 등장시키려면 먼저 상위 정본에 사용처를 기재한다.
- `[ASSUMPTION]` **상태 유지 규칙**: 명시적 이전·소모·파괴 사건이 없는 권에서는 직전 권의 소유·보관 상태가 유지된다. 정본이 권별 재확인을 하지 않으므로, 연속성 판정의 기본값으로만 쓴다.
- **소유 판정은 6층을 모두 본다**: 법적 소유권 / 제작 공동체의 문화적 권리 / 현재 보유자의 점유 / 사용자의 접근권 / 피해자의 반환 요구 / 유산 자체의 거부권. 에이든은 모든 층을 자동 획득하지 않는다. 위 표의 「법적 소유권자」와 「실제 보관·점유」가 갈리는 행은 이 규칙의 정상 작동이다.
- **하향 불가역**: A→L→E/S→R→SE→DM/DS 방향으로만 이동한다. 파괴·분해·봉인된 자산이 후속 권에서 상위 코드로 돌아가지 않는다.
- **복제품은 코드를 승계하지 않는다.** 사본·파편은 원본의 역사주소·증언권을 복제하지 못하므로 최대 E까지만 부여한다.
- **누적 사용가능 자산 상한 없음, 그러나 합산 금지**: 최종부에서 유산을 합쳐 초월무기를 만들지 않는다.

### 5. 주권신수 권별 관계 추적

주권신수는 보유목록이 아니므로 「보관처」 열을 두지 않는다. 관계·계약 상태만 추적한다.

| ID | 정식명(SOFT LOCK) | 관계 발생 권 | 계약 상대 | 거부권 발동 조건 | 최종 관계 |
|---|---|---|---|---|---|
| B01 | 길등짐승 `[WORKING]` | V1, V7, V13 | 라하크 이동단 (계절 단위) | 이동로 강제변경, 군사징발 | 국경선·이동로 분리 협약의 생태 증인. 라하크 부족도 소유 불가 |
| B02 | 종울음새 `[WORKING]` | V5, V10, V15 | 카르둔과 상호계약 | 광산 파괴 시 인간 거부 | 지역 공개관측망 편입 |
| B03 | 유리등각수 `[WORKING]` | — | 카르둔 (채굴금지구역 교환) | 사냥·강제채굴 | 지역 생활망 광물 공급 감시자 |
| B04 | 역조고래 `[WORKING]` | V4, V10 | 남부 선주·마레사 자유해안동맹 | 사냥, 관측선 거리·소음 위반 | 국제 상호감사의 자연 기준점. 국가 전략무기 지정 금지 |
| B05 | 백지사슴 `[WORKING]` | V13–V15 | 에이든과 일시 동맹 (종속 아님) | 추적·포획 | E371 움브라 아이 학적등록, E374 증언자의 길과 시각 연결 후보 |

`MAL` §Sovereign Beasts의 B02/B03 기능 배정과 `SBE`의 B02/B03 개체 정의가 1:1로 대응하지 않는 부분은 §6-10 참조.

### 6. 이 절이 판정하지 않은 충돌

| # | 항목 | 충돌 내용 | 상태 |
|---|---|---|---|
| 1 | R03 파괴 시점 | `MAL`은 "V12 방어 중 파괴", `RE`·`G5(E366)`·`V15`·`CHK`는 V15 | 다수·화 단위 근거를 따라 V15로 기재. `MAL` 정정 필요 |
| 2 | R01 재사용 권 | `RE`는 V3, `MAL`은 V4 | 양쪽 모두 E로 표기, 판정 보류 |
| 3 | R02 최초 등장 | `RE`는 "V1–V4", `MAL`·`G1(E036)`은 V2 | V2를 최초 확보로 기재 |
| 4 | R10 최종상태 | `CHK`·`MAL`은 "녹여 분산인장 제작", `RE`·`WSC`는 "비활성 공공증거 보존" | 녹이면 보존이 불가능하므로 V15 칸 판정 불가 |
| 5 | R12 V4 언급 | `V04`에 "감사인장" 사용 장면이 있으나 `MAL` 최초 사용은 V12 | 동일 물건 여부 정본 없음 |
| 6 | R05 명칭 | `CHK`=백지도 / `RE`=존재하지 않는 도시의 지도 / `MAL`=존재하지 않는 도시 지도 | 정식명 미확정 |
| 7 | R09 개혁가 증언 | `RE`는 개혁가의 마지막 증언을 플롯에 포함하나 해당 권 미지정 | 그리드 반영 불가 |

### 7. 이 절의 근거 파일

| 토큰 | 경로 |
|---|---|
| CHK | `docs/09_collection/asset-state-checkpoints-v1.md` (본 문서 상단 3단계 표) |
| RE | `docs/09_collection/relic-encyclopedia-r01-r12-v1.md` |
| MAL | `docs/09_collection/major-assets-ledger-v1.md` |
| RBO | `docs/09_collection/relics-beasts-ownership-v1.md` |
| SBE | `docs/09_collection/sovereign-beast-encyclopedia-b01-b05-v1.md` |
| SCM | `docs/10_story_architecture/subact-causal-matrix-v1.md` |
| WSC | `docs/01_timeline/world-state-continuity-matrix-v1.md` |
| MML | `docs/11_mystery/mystery-macguffin-ledger-v1.md` |
| G1–G5 | `docs/10_story_architecture/detail/ga0{1..5}-episode-registry-*.md` |
| V01–V15 | `docs/10_story_architecture/detail/v{01..15}-scene-ready-design-v1.md` |
| OV1 | `docs/10_story_architecture/detail/v01-d9-correction-overlay.md` |
| — | `docs/00_project/canon-constitution-v1.md` (IMMUTABLE 5 영구손실, 편의적 해결 금지) |
| — | `docs/00_project/canon-naming-pack-v1.md` (기관·권역·인물 정식명) |
| — | `docs/05_characters/cast-canon-index-v2.md` (C04 E298–E299 영구사망, C13 유산 분해 합의) |

### 근거 문서

- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/09_collection/asset-state-checkpoints-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/00_project/canon-constitution-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/00_project/canon-naming-pack-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/05_characters/cast-canon-index-v2.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/09_collection/relic-encyclopedia-r01-r12-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/09_collection/major-assets-ledger-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/09_collection/relics-beasts-ownership-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/09_collection/sovereign-beast-encyclopedia-b01-b05-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/subact-causal-matrix-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/01_timeline/world-state-continuity-matrix-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/11_mystery/mystery-macguffin-ledger-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v01-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v01-d9-correction-overlay.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v02-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v03-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v04-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v05-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v06-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v07-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v08-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v09-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v10-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v11-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v12-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v13-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v14-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v15-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/ga02-episode-registry-e076-e150.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/ga03-episode-registry-e151-e225.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/ga04-episode-registry-e226-e300.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/ga05-episode-registry-e301-e375.md

### 정본 근거가 없어 채우지 못한 항목

- R03 개혁가의 절검 파괴 시점이 정본 간 충돌한다. major-assets-ledger는 'V12 방어 중 파괴', relic-encyclopedia·ga05(E366)·v15-scene-ready·본 문서 상단 표는 V15. 어느 쪽이 정본인지 결정 필요.
- R10 초대왕의 무관 최종상태 충돌. asset-state-checkpoints와 major-assets-ledger는 '녹여 분산인장 제작', relic-encyclopedia와 world-state-continuity-matrix는 '비활성 공공증거로 보존'. 녹임과 보존이 양립하지 않아 V15 소유·보관·사용가능을 채울 수 없었다.
- R01 회색 종의 중반 재사용 권이 relic-encyclopedia(V3)와 major-assets-ledger(V4)로 갈린다.
- R02 빈 세금장부의 최초 등장이 relic-encyclopedia(V1–V4)와 major-assets-ledger·ga01 E036(V2)으로 갈린다.
- R12 최종 감사인장이 v04-scene-ready E088–E093 구간 장면에 '감사인장'으로 언급되나 major-assets-ledger 최초 사용은 V12다. V4의 것이 동일 물건인지, 별개의 지역 인장인지 정본 없음.
- R05의 정식 명칭이 세 문서에서 다르다(백지도 / 존재하지 않는 도시의 지도 / 존재하지 않는 도시 지도). naming-pack §3 주요 장소표에 등재되어 있지 않다.
- R05의 V7·V10·V13 재사용은 major-assets-ledger의 권 번호만 있고, 해당 권 scene-ready design에 장면 근거가 없다. 그 권의 보관처·사용 주체를 채울 수 없었다.
- R08 에르나 기억피의 V11·V14 사용, R09 네바르 장례보석의 V14 사용도 권 번호만 있고 장면 근거가 없다.
- R09의 '개혁가의 마지막 증언' 사용이 relic-encyclopedia 플롯란에 있으나 해당 권이 지정되지 않았다. 세렌 바일 사망은 E024(V1)인데 장례보석 최초 사용은 V8로 되어 있어 시점이 비어 있다.
- 각 자산의 권별 '물리적 보관 기관명'이 대부분 미지정이다. 특히 V2의 '서로 다른 법적 보관처에 분산'이 어느 기관인지(칼레온 대기록소 / 아고라 회당 / 지역 기록소) 정본에 없어 표의 보관처 열을 서술로만 채웠다.
- 소유권 이전 시점의 화 번호(E)가 R05·R08·R09·R10의 상당수 구간에서 미지정이다.
- 주권신수 B01–B05의 종명이 모두 [WORKING] 상태이며 canon-naming-pack에 등재되어 있지 않다. 정식명 확정 전까지 신수 표의 명칭은 잠정이다.
- major-assets-ledger의 B02(거리·경계 불안정 감지, 카르둔 상호계약)와 sovereign-beast-encyclopedia B02(종울음새, 도시·성당 군집 비행신수) / B03(유리등각수, 카르둔 지하길 안내)의 기능 배정이 어긋난다. 카르둔 계약 신수가 B02인지 B03인지 확정 필요.
