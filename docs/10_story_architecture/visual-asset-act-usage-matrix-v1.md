# Visual Asset × Act Usage Matrix v1

Status: **D16.4 — ACT-MAP VISUAL BINDING / PRODUCTION OVERLAY**  
Date: 2026-08-20  
Scope: C01–C30 / R01–R12 / B01–B05 / L01–L08 / F01–F14를 5 Grand Acts·15 Volumes·E001–E375 집필 파이프라인에 연결한다.  
Rule: 새 사건·새 등장·새 기능을 만들지 않는다. 기존 `collectibility-exposure-and-variant-map-v1.md`, 캐릭터 상태 체크포인트, 세력 인과선, 유산·신수 정본을 **시각 호출 규칙**으로만 번역한다.

## 1. 사용법

액트맵·서브액트·Episode Context Pack에서 자산 ID를 사용할 때 아래 6개 필드를 함께 호출한다.

`Asset ID / Act-Volume Range / Current Visual State / Primary Anchor / Allowed Beat / Do-Not-Advance`

Allowed Beat:
- `R` Reveal — 첫 강한 인지
- `E` Echo — 이미 아는 단서 재호출
- `D` Damage — 손상·마모·상실
- `T` Transfer — 소유·권한 이전
- `V` Variant — 시대·상태 변화
- `F` Final — 파괴·분해·반환·봉인·최종 생활상태

한 회에서 Visual Anchor는 Primary 1개, Secondary Echo 최대 2개다.

---

# 2. Character Act Binding — C01–C30

| ID | Grand Act / Volume | Current Visual State | Act에서 우선 보일 것 | 허용 Beat | 금지 |
|---|---|---|---|---|---|
| C01 에이든 로엔 | GA I V1–3 | F0 FIELD | 사선 짧은 외투, 비대칭 어깨, 귀환패/빈 고리, 출구 확인 습관 | R/E/D | 초반부터 ADDRESS-LOSS 외형 선행 금지 |
| C01 | GA II V4–6 | ALTERED/WORN | 여러 시대 수선재, 장비의 불균질성, 중앙 표식 감소 시작 전 단계 | E/V | 영웅 갑주 업그레이드 금지 |
| C01 | GA III V7–9 | ALTERED/WORN | 건국기 재료가 추가돼도 F0 요원 골격은 유지 | E/V | Era O 현지인처럼 완전 동화 금지 |
| C01 | GA IV V10–12 | ALTERED/WORN → ADDRESS-LOSS 진입 | C08과 얼굴보다 장비·생활 차이를 강조 | V/D | C08과 동일 의상·동일 자세 금지 |
| C01 | GA V V13–15 | ADDRESS-LOSS → FINAL LOSS | 공적 표식 제거, 빈 자리, 기능 생활복 | V/F | C30=에이든 시각확정 금지 |
| C02 리아 세른 | GA I V1–3 | PRIVATE+OFFICIAL MIX | 겹소매, 세로 문서갑, 투명 겹판, 출처점 | R/E | 냉미녀 기록관 클리셰 금지 |
| C02 | GA II–III V4–9 | MULTI-ERA EVIDENCE | 개인 기록보다 복수 출처·겹판 증가 | E/V | 마법서/예언자 이미지 금지 |
| C02 | GA IV V10–12 | MULTI-ERA EVIDENCE | 여러 시대 증거를 다루되 몸은 기록노동자 유지 | E/D | 전투형 변신 금지 |
| C02 | GA V V13–15 | PUBLIC EVIDENCE / PRIVATE LOSS | 공공복제 표식 증가, 개인 기표의 빈자리 | V/F | 사적 기억 기적복원 표현 금지 |
| C03 아이리스 네르 | GA I–II V1–6 | WESTERN FIELD | 걷은 소매, 주민표식, 손으로 사람 흐름 정리 | R/E | 전형적 여전사 포즈 금지 |
| C03 | GA III–IV V7–12 | REGIONAL NEGOTIATOR | 현장복 위 최소 공식표식, 지역 대표의 실무성 | V/E | 중앙귀족 예복화 금지 |
| C03 | GA V V13–15 | P1 AUDIT DESIGNER | 주민 현장으로 돌아갈 수 있는 옷 + 감사표식 | V/F | 관료 정장형 최종폼 금지 |
| C04 마르칸 베르 | GA I–II V2–6 | F1 ORDER | 직사각 군복, 배급토큰, 방어지도 | R/E | 검/갑옷 영웅화 금지 |
| C04 | GA IV V10–12 | EVACUATION-WORN / LAST COMMAND | 계급보다 대피흔적, 떼어낸 표식 | D/V/F | 사망 이후 생존 Variant 금지 |
| C05 오르바드 카르센 | GA III V7–9 | TEMPORARY COALITION → STANDARDIZATION PRESSURE | 다문화 작업복, 도면통, 측정도구 | R/V | 왕관·현자로브 권위 금지 |
| C06 세렌 바일 | GA I V1 | AUDITOR / TARGET | 감사 실무복, R03 절검, 장부끈 | R/D/F | 사망 후 현재시점 생존 외형 재등장 금지 |
| C06 | GA I–V V2–15 | ABSENT ECHO | 사람 대신 절검·기록·빈자리로 기억 | E | 새로운 세렌 Variant 제작 금지 |
| C07 다렌 모트 | GA I–II V2–6 | MILITARY + FAMILY LIFE | 군복 사이 생활물품·가족흔적 | R/E/V | 마르칸 축소판 금지 |
| C08 젊은 에이든 로엔 | GA IV V10–12 | YOUNG / LOCAL-AID | C01 골격 일부 공유, 열린 허리선, 귀환표식 없음 | R/E/V | 현재 에이든 장비진화 복제 금지 |
| C09 나하 아노르 | GA II V4–6 | ADDRESS-LOSS RESIDENT | 얼굴보다 신발·수선선·현재 생활물건 | R/E | 얼굴변형을 괴물화 금지 |
| C09 | GA V V13–15 | PRESENT-RIGHTS | 현재 생활표식·공동명부와 연결 | V/F | 과거 복구가 현재성보다 우선해 보이게 금지 |
| C10 메이라 솔 | GA I V1 | FIELD MEDICAL | 진료앞치마, 접힌 소매, 약품/붕대 케이스 | R/E | 성녀/힐러 로브 금지 |
| C10 | GA V V15 | CIVIC MEDICAL CONTINUITY | 생활 의료 기능과 분산체계 연결 | E/F | 새로운 초월치유 능력 암시 금지 |
| C11 테온 리브 | GA I V2–3 | CALCULATION / ERROR RANGE | 잉크소매, 화상손가락, 투명 오차판 | R/E | 리아와 동일 기록가 이미지 금지 |
| C11 | GA V V15 | PUBLIC AUDIT | 오차범위와 수정흔적이 더 공개적으로 보임 | V/F | 완벽한 정답표 금지 |
| C12 엘사 네르 | GA II V4 | LOCAL DISTRIBUTED RECORD | 팔목 문서끈, 화상흉터, 작은 분산기록 | R/E | 하렌식 원본상자 금지 |
| C13 도르칸 카르바 | GA II V5 | WORKSHOP OWNER | 비대칭 도구걸이, 접합부 확인, 오래된 가죽도구 | R/E | 판타지 대장장이 클리셰 금지 |
| C13 | GA III V7–8 | FOUNDING COBUILDER | 문화 혼합 재료가 실제 접합흔적으로 추가 | V/E | 전설무기 제작자로 축소 금지 |
| C13 | GA V V15 | DISMANTLER | 유산 분해를 생활망 부품으로 연결 | V/F | 강화제작 Final 금지 |
| C14 사하드 렌 | GA II V5 | ROUTE / NON-OWNERSHIP | 발목 매듭, 손등 길표식, 빈 등 | R/E | 깃털·동물머리 장식 금지 |
| C14 | GA III V7–9 | FOUNDING ROUTE WITNESS | 끊긴/늘어난 매듭으로 길 변화 표현 | V/E | 신수 소유자처럼 보이게 금지 |
| C15 베사르 움 | GA I V3 | FUNERAL LAW | 빈 보석틀, 판결끈, 무광 장례천 | R/E | 사신/언데드 금지 |
| C15 | GA III V8 / GA IV V12 / GA V V14 | WAR WITNESS → LIMITED EVIDENCE | 죽음증언과 법적 한계가 외형에 누적 | V/E/F | 죽은 자 부활 암시 금지 |
| C16 마리엔 레바 | GA II V4 | COASTAL NOTARY | 방수문서함, 소금바랜 코트, 항해거리 고리 | R/E | 해적/선장 디자인 금지 |
| C16 | GA V V14 | INTERNATIONAL AUDIT | 공증·외부검증 표식 강화 | V/F | 중앙관료화 금지 |
| C17 유나 벨 | GA I V3 seed / GA II V6 main | MEMORY OF FAMILY | 평범한 민간복, 숨긴 가족사진 조각, 교사가방 | R/E/V | 혁명가 깃발/카리스마 복식 금지 |
| C18 카시안 로드 | GA III V9 준비 / GA IV V10–12 | TIME INDUSTRY | 방진코트, 세로 기능인장열 | R/E/V | 미래 CEO 정장 금지 |
| C19 에스라 마레사 | GA IV V10 | SEA DAMAGE / EXTERNAL PRESSURE | 항구매듭, 젖은 신발, 항로 노동흔적 | R/E | 마리엔과 공증 이미지 중복 금지 |
| C20 오렐 바스 | GA I V3 | PROCEDURAL STABILITY | 수선 행정복, 붉은 밀랍 손, 얇은 문서판 | R/E | C21 왕권 실루엣 중복 금지 |
| C20 | GA V V15 | TERM-LIMITED P1 | 같은 옷의 수선 누적 + 임기 한계 표식 | V/F | 영구관료 권위화 금지 |
| C21 레오르 세르바 | GA III V7–9 | HEIR → CENTRALIZING RULER | 승인판, 검지 인장흉터, 수직 의례복 | R/V | 보석왕관만으로 권력 표현 금지 |
| C21 | GA IV V12 | DISTRIBUTED-SYSTEM OPPOSITION | 표식은 남되 효력이 흔들리는 상태 | V/E | 단순 악역외형 금지 |
| C22 하렌 세른 | GA II V4 / GA V V14 | ORIGINALISM → OPEN VERIFICATION | 정사각 원본상자, 잉크손톱, 곧은 실끈 | R/V/F | 리아/엘사의 유동형 기록문법 금지 |
| C23 미라 라디아 | GA II V4 / GA V V15 | FOOD/WATER/NEXT SEASON | 갈라진 손, 삼중 곡물주머니, 수문 실무층 | R/E/F | 풍요여신·상인 디자인 금지 |
| C24 브란 케르 | GA II V5 | CONDITIONAL COMMAND | 짧은 방풍갑, 명령패+철회조건패, 동상귀 | R/E | 마르칸 국가군정 실루엣 금지 |
| C25 케론 셀카르 | GA II V5 / GA V V15 | MATERIAL REPAIR → P1 NETWORK | 균열추, 무릎보호, 수리도구 | R/V/F | 도르칸 제작자 이미지와 중복 금지 |
| C26 아벨 네르 | GA I V1 / GA V V13 | PATIENT WITNESS → RIGHTS RECOGNIZED | 수정 이름표, 평범한 생활복, 어긋난 보호동작 | R/V/F | 발광혈관·괴물화 금지 |
| C27 시아 아노르 | GA V V13–15 | SCHOOL / ORDINARY RIGHTS | 큰 학적명부판, 낮은 도구가방, 분필손 | R/E/F | 성녀·마법학교 교장화 금지 |
| C28 토마르 마레이 | GA II V4 | PORT LABOR | 어깨 화물끈, 손보호대, 화물패 | R/E | 해적/선장 이미지 금지 |
| C29 렌 바르 | GA IV V10–11 | STAYED TRAVELER | 빈 귀환슬롯, 개조 도구함, 현지생활 패치 | R/E/V | C01의 ‘돌아가려는 사람’ 문법 복제 금지 |
| C30 이름 없는 여행자 | GA V V15 E374–375 | SINGLE EPILOGUE STATE | 일반 여행복, 비대칭 가방끈, 임시표 | R/F | C01 장비·얼굴·흉터 연결 금지; Variant 추가 금지 |

---

# 3. Relic Act Binding — R01–R12

| ID | Act / Volume | 사용 상태 | 시각 목적 | Beat | 금지 |
|---|---|---|---|---|---|
| R01 회색 종 | GA I V1 | O/U Reveal | 빈 이름흔적과 공동체 물건의 불길한 인지 | R/E | 휴대형 마법아이템화 금지 |
| R01 | GA I V3 / GA V V13–15 | C/F | 압수·반환·지역망의 공개기록과 결합 | E/T/F | 주인공 소유물화 금지 |
| R02 빈 세금장부 | GA I V2–3 | U/C | 이름 없는 합계·분산 사본의 권리증거 | R/E | 발광 마법책 금지 |
| R02 | GA II V6 / GA V V13 | C/F | 부담배분·현재권리의 공개 근거 | E/F | 완전 복원본 1권으로 통합 금지 |
| R03 개혁가의 절검 | GA I V1 | O/U | 잘린 군용검, 세렌의 기록절단 도구 | R/D | 성검/대검화 금지 |
| R03 | GA I V2–3 | C/T | 유족·소유권 표식, 에이든 전리품 아님 | E/T | 에이든 전용무기 고정 금지 |
| R03 | GA V V15 E366 | F | 파편과 파괴기록이 Final | F | 재주조·강화형 Final 금지 |
| R04 F0 귀환패 | GA I V2 | O/U | 귀환 기대와 군용 신분성 | R/E | 만능 귀환키 금지 |
| R04 | GA IV V11 / GA V | C/F | 기능 상실과 빈 연결부 | D/V/F | 복원키 결말 금지 |
| R05 존재하지 않는 도시 지도 | GA II V4 | O/U/C | 겹친 도시·복수주소를 물성으로 이해 | R/E/V | 보물지도화 금지 |
| R05 | GA IV V10 / GA V V13–14 | C/F | 공개 지리레이어와 권리충돌 | E/T/F | ‘진짜 지도 1장’ 결론 금지 |
| R06 카르둔 경계갑 | GA II V5 | O/U | 공동 정비장비와 조건부 사용 | R/E | 영웅 판금갑옷 금지 |
| R06 | GA II V6 / GA IV V11 | C/T | 소유·사용권과 마모 누적 | T/D | 에이든 영구전용장비 금지 |
| R06 | GA V V15 | F | 생활 안정망 부품으로 분해 | F | 최종 강화갑주 금지 |
| R07 건국 모루 | GA III V7 | O/U | 공동공사·다종족 제작 시스템 | R/E | 휴대 성물화 금지 |
| R07 | GA III V9 / GA V | C/F | 왕실 성물화 장식 제거, 공공설비 회복 | V/F | 전설 대장장이 단독소유 금지 |
| R08 에르나 기억피 | GA III V8 | O/U | 몸과 증언, 동의표식의 긴장 | R/E | 기억영상 만능기기 금지 |
| R08 | GA V V14 | C/F | 공개·익명화·사생활 한계 | T/F | 완전 기억복구 금지 |
| R09 네바르 장례보석 | GA III V8 | O/U | 마지막 감각과 균열의 긴장 | R/E | 부활 매개체 금지 |
| R09 | GA IV V12 / GA V V14 | C/F | 마르칸 마지막 증언 후 봉안 | E/F | 반복 재생으로 죽은 인물 소비 금지 |
| R10 초대왕의 무관 | GA III V9 | O/U/C | 열린 슬롯, 후대 혈통 독점의 흔적 | R/V | 보석왕관화 금지 |
| R10 | GA V V14–15 | F | 용해·분산인장·과정 공개 | F | 새 왕관 Final 금지 |
| R11 다른 에이든의 방패 | GA IV V10 | O/U | ‘익숙하지만 아닌’ 다른 삶 | R/E | 현재 에이든 최종장비화 금지 |
| R11 | GA IV V11 / GA V V14 | C/F | 소유압력과 공공보관 | D/T/F | 대체 타임라인 승계 금지 |
| R12 최종 감사인장 | GA IV V12 | O/U/C | 7조각과 빈 자리, 공동거부권 | R/E | 7개=최강권한 연출 금지 |
| R12 | GA V V14–15 | F | 물건보다 절차·기관으로 분산 | T/F | 단독사용 완전체 금지 |

---

# 4. Sovereign Beast Act Binding — B01–B05

| ID | Act / Volume | 시각 호출 | 역할 | Beat | 금지 |
|---|---|---|---|---|---|
| B01 길등짐승 | GA I V1 보조 / GA III V7 main | 낮고 넓은 등, 길무늬, 경로흔적 | 이동로·계약의 생태적 증언 | E/R | 안장·탑승펫 금지 |
| B01 | GA V V15 | 지역 생활망과 공존하는 경로 | 비소유 결말의 생활성 | E/F | 주인공 소환수화 금지 |
| B02 종울음새 | GA II V5 | 군집 나선, 공명기관, 소리의 빈 공간 | 경보생태·보호구역 계약 | R/E | 단독 화려한 새 몬스터화 금지 |
| B03 유리등각수 | GA II V5 / GA III V8 | 암석층 등선, 진동흔적 | 지질·채굴·생활 위험 | R/E | 수정갑옷 괴수화 금지 |
| B03 | GA V V15 | 생활망 주변 경보생태 | 분산체계와 공존 | E/F | 인간 장비 장착 금지 |
| B04 역조고래 | GA III V8 / GA IV V10 | 수면 위 등선·역조·항로흉터 | 인간 달력 밖의 생태주기 | R/E | 하늘고래/탑승물 금지 |
| B05 백지사슴 | GA V V13 | 발자국·고개각·관찰판 불일치 | 현재성·관찰 불일치 증거 | R/E | 순백 성수·진실판정자 금지 |
| B05 | GA V V15 | 관찰차이 유지, 생활권 속 흔적 | 비확정 상태의 지속 | E/F | 에이든/C30 정체 증명도구 금지 |

---

# 5. Landmark Act Binding — L01–L08

| ID | Act / Volume | 대표 상태 | 액트 기능 | Beat | 금지 |
|---|---|---|---|---|---|
| L01 아르켄 왕관수도 | GA I V3 | CENTRAL LAYERS | 중앙기관·왕실·기록·하항의 겹친 권력 | R/E | 범용 판타지 왕도 aerial shot만 사용 금지 |
| L01 | GA III V9 / GA IV V12 | CENTRALIZATION VARIANT | 같은 공간이 권력집중으로 변한 차이 | V | 새 도시처럼 재설계 금지 |
| L01 | GA V V14–15 | DISTRIBUTED AFTERIMAGE | 중앙표식 약화·공개기록·빈 벽 | V/F | 완전 유토피아화 금지 |
| L02 서부 잿빛 변경/벨하임 | GA I V1 | REPAIRED EDGE | 끊긴 성벽 아래 학교·시장·겹문패 | R/E | 폐허 전용 배경 금지 |
| L02 | GA II / GA V | RIGHTS VARIANT | 주민증언표·생활권의 공식화 | V/F | 모든 흔적 새것으로 복원 금지 |
| L03 셀카르 유리산맥 | GA II V5 / GA III V7–8 | LIVING WORKSHOP | 공방·무덤·광맥·수리의 동시성 | R/E | 크리스털 왕국 테마파크화 금지 |
| L03 | GA V V15 | DISMANTLED WORKFACE | 유산재료가 생활망으로 이동한 빈 작업면 | V/F | 더 화려한 최종도시 금지 |
| L04 라디아 곡창초승달 | GA II V4 / GA V V15 | WATER/FOOD CALENDAR | 수문·배급·밀밭이 하나의 제도 | R/E/F | 목가적 풍요 배경만 사용 금지 |
| L05 조류도시연맹 | GA II V4 / GA IV V10 | TIDE CITY | 간조/만조가 시장·행정·항로를 바꿈 | R/V | 베네치아풍 장식도시로 축소 금지 |
| L06 아노르 백지권 | GA V V13 | REDRAWN DAILY LIFE | 공동명부·관찰차이·같은 식탁 | R/E | 공포 안개공간만으로 표현 금지 |
| L06 | GA V V15 | P1 APPEAL LIFE | 임시표식과 이의제기 양식의 병렬 | V/F | 불확정성 완전 해소 금지 |
| L07 Era F 생존구 | GA I V2 / GA II V6 | HERO POSTER / REAL WALL | 선전과 생활수선의 대비 | R/V | 디스토피아 네온도시 일반화 금지 |
| L07 | GA IV V10–12 | FUTURE VARIANT | 같은 통로의 다른 선전·배급체계 비교 | V | 미래마다 완전히 다른 건축 금지 |
| L08 P1 증언자의 길/지역망 | GA V V15 | WORLD AFTER HERO | 학교·병원·수문·게시판의 낮은 생활축 | R/F | 거대한 승리기념비·완벽한 신도시 금지 |

---

# 6. Faction Act Binding — F01–F14

| ID | 핵심 Act / Volume | Visual Grammar 사용 위치 | 상태 변화 | 금지 |
|---|---|---|---|---|
| F01 왕실 중앙유지파 | GA I V1–3 / GA III V9 / GA IV V12 | 닫힌 고리·황동·붉은 밀랍·중앙정렬 | 후반으로 갈수록 다른 슬롯을 덮는 폐쇄성 | 단순 흑색 악역제복 금지 |
| F02 성당 정통력파 | GA I V1 / GA II 일부 | 3중 상처선·석회·진료천·종합금 | 구휼/달력/종말 노선 차이를 생활시설로 표현 | 종교=검은 사제복 단일화 금지 |
| F03 마탑 계산연합 | GA I V2 / GA II V6 / GA V V15 | 교차축+오차범위, 관측유리 | 단일정답 압력 vs 공개오차 | 마법사 로브·발광룬 의존 금지 |
| F04 대기록소·주소관료단 | GA I V1–3 / GA II V4 / GA V V14 | 겹문장·수정표식·원본/수정/증언 물리차 | 폐쇄 보존 → 공개검증 | 도서관 길드 미학으로 축소 금지 |
| F05 국경 고정환 수비연합 | GA II V4–5 | 열린 고리+요새/마을표식, 명령패/철회패 | 군사필요와 주민조건 충돌 | F08 국가군정과 동일 제복 금지 |
| F06 서부 변경개혁연합 | GA I V3 / GA II | 겹문패·열린 원·주민 증언점 | 지역 조사망→권리연합 연결 | 혁명깃발 단일 상징 금지 |
| F07 복원파 | GA I V3 / GA II V4–6 | 봉합선, 가족기록, 옛 제복조각 | 구원 욕망→현재 덮어쓰기 위험 | 사악한 컬트 외형 금지 |
| F08 F1 군정 | GA I V2–3 / GA II V6 | 직사각 구역망·배급토큰·영웅포스터 | 질서효율→현재 시민권 방어와 통제의 양면 | 나치풍 단순 악역 코딩 금지 |
| F09 자유해안 계약동맹 | GA II V4 / GA IV V10 | 열린 파도선·계약매듭·방수재 | 외부공증→봉쇄/항로압력 | 해적국가 미학 금지 |
| F10 북부 공방동맹 | GA II V5 / GA III V7 / GA V V15 | 드러난 접합부·수리흔적·공방도장 | 공동소유→분산 생활망 제작 | 스팀펑크 톱니 장식 과잉 금지 |
| F11 라하크 이동단 협의회 | GA II V5 / GA III V7–9 | 닫히지 않는 경로선·매듭·이동표식 | 경로 거부권과 건국 참여 | 유목민 깃털·동물머리 클리셰 금지 |
| F12 네바르 장례법정 | GA I V3 / GA III V8 / GA IV V12 / GA V V14 | 빈 중심·판결끈·불완전 결정 | 죽음/부재/소거 구분→공개한계 | 언데드/사신 미학 금지 |
| F13 백지권 권리연합 | GA II V4 seed / GA V V13–15 | 비어도 이어지는 선·복수 증언점·현재생활물 | 비등록 생존→현재권리 제도화 | 추상 인권 로고만 사용 금지 |
| F14 F3 연대개입산업연합 | GA III V9 seed / GA IV V10–12 | 기능별 모듈 인장열·표준금속·방진천 | 효율적 계약망→공통 소켓 위험 노출 | 사이버기업 네온미학 금지 |

---

# 7. Grand Act Visual Load Map

## GA I — 잘못된 치료 / V1–3
Primary grammar:
- C01/C02/C03/C06 중심
- R01/R02/R03/R04
- L02/L07/L01
- F01/F02/F03/F04/F06/F08

Visual question: **‘공식기록과 현장생활이 왜 다르게 보이는가?’**

## GA II — 살아남은 미래의 권리 / V4–6
Primary grammar:
- 현재 주민·분산기록·공방·해안·수비
- R05/R06
- B02/B03
- L03/L04/L05
- F05/F07/F09/F10/F13

Visual question: **‘누가 이 물건·도시·귀환권을 가질 수 있는가?’**

## GA III — 건국의 아홉 상처 / V7–9
Primary grammar:
- 다문화 공동건설, 이동·장례·재료
- R07/R08/R09/R10
- B01/B03/B04
- L03/L05/L01의 원형/초기상태
- F10/F11/F12/F01 초기형

Visual question: **‘왕국이 완성되기 전에는 무엇이 공동체를 실제로 움직였는가?’**

## GA IV — 세 시대의 전쟁 / V10–12
Primary grammar:
- C01/C08/C29의 차별
- R11/R12, R04/R06 손실
- L07의 미래별 Variant
- F08/F14/F01의 권력문법 충돌

Visual question: **‘같은 사람·같은 제도가 다른 미래에서 무엇을 잃고 무엇을 얻었는가?’**

## GA V — 남길 역사 / V13–15
Primary grammar:
- 현재성·학교·병원·감사·분산망
- B05
- R03/R06/R10/R12 Final
- L06/L08
- C30은 마지막에만 단일상태

Visual question: **‘무엇을 소유하지 않고도 남길 수 있는가?’**

---

# 8. Episode/CP Binding Contract

E089 이후 Context Pack에는 아래를 의무 삽입한다.

```text
VISUAL BINDING
Primary Visual Anchor: <ID + name>
Act/Volume State: <GA / V / state>
Beat Type: <R/E/D/T/V/F>
3-Second Anchor: <silhouette/material/gesture 중 1–3개>
Secondary Echo: <최대 2개>
Do Not Re-explain: <이미 독자가 아는 외형>
Do Not Advance: <미래 Variant/Final 상태>
```

### 예: E089 리아 세른
- Primary Visual Anchor: `C02 리아 세른`
- Act/Volume State: GA II / V4 / MULTI-ERA EVIDENCE 진입
- Beat: E/V 중 해당 장면 설계가 허용한 것만
- 3-Second Anchor: 비대칭 겹소매 + 세로 문서갑 + 얇은 투명판
- Do Not Re-explain: 머리/얼굴 전체 소개 반복 금지
- Do Not Advance: GA V PUBLIC EVIDENCE/PRIVATE LOSS를 선행 묘사 금지

이 Contract는 사건을 추가하지 않고 기존 장면의 시각정보량만 통제한다.

---

# 9. Exit Gate

- Character: 30/30 Act binding
- Relic: 12/12
- Beast: 5/5
- Landmark: 8/8
- Faction: 14/14
- 총 domain assets: **69/69**
- Grand Act: 5/5 visual question defined
- Volume: 15/15 기존 Exposure Map과 호환
- Plot mutation: 0
- New asset/function: 0
- Future-state leakage guard: ACTIVE

**D16.4 ACT-MAP VISUAL BINDING: COMPLETE.**
