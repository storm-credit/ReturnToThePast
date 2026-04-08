# 🚀 프로젝트 진입점

> 이 문서는 **《나는 과거로 간다》** 프로젝트의 **유일한 진입점**입니다.
> 다른 파일(구버전)이 보이더라도, 이 가이드에 링크된 파일만 신뢰하십시오.

---

## 1. 🧭 필독 문서
집필을 시작하기 전에 아래 문서는 반드시 읽으십시오.

0.  **[설정 우선 모드](orchestra/SETTING_FIRST_MODE.md)**
    *   현재는 `설정집 선완성 모드`. 초안 집필보다 설정 고정이 먼저라는 운영 기준.
1.  **[15권 로드맵](outline/Series_Roadmap.md)**
    *   전체 줄거리, 회차별 타임 패러독스, 엔딩까지의 설계도.
2.  **[시리즈 제작 고정 규칙](Guidelines/Series_Production_Constraints.md)**
    *   권당 25화, 화당 공백 제외 3,500자 이상, 설계 문서 필수 규칙.
3.  **[시간여행 프레임](Guidelines/Time_Travel_Frame.md)**
    *   이 작품이 회귀물이 아니라 시간여행 패러독스물이라는 구조적 기준.
4.  **[고유명사 작명 가이드](lore_bible/style/Naming_Style_Guide.md)**
    *   지명, 세력명, 금기명이 고풍한 다크 판타지 어감을 유지하도록 맞추는 기준.
5.  **[정식명 장부](lore_bible/style/Canonical_Name_Register.md)**
    *   정식명, 별칭, 폐기명, 언어 계열을 함께 묶어 이름 재오염을 막는 장부.
6.  **[설정집 감사 범위](Guidelines/Setting_Audit_Scope.md)**
    *   설정 보강이 규칙, 인물, 세력, 장소, 용어, 복선, 아웃라인, 타임라인을 함께 본다는 운영 기준.
7.  **[금지 표면어 장부](Guidelines/Banned_Surface_Ledger.md)**
    *   현대/SF/게임 표면어, 중2병 서사 표면, 구형 캐논 단어를 어떤 말로 대체할지 정리한 금지어 장부.
8.  **[세계 이동 지도](lore_bible/locations/World_Travel_Atlas.md)**
    *   수도, 북부, 동부, 남부, 서부 권역의 거리감과 이동 압박을 잠그는 배경 지도.
9.  **[엔진 데이터 레이어 정책](orchestra/ENGINE_DATA_LAYER_POLICY.md)**
    *   JSON 키는 안정성 중심으로 두고, 사람용 설명층은 옆 문서로 분리한다는 운영 기준.
10.  **[규칙 데이터 가이드](lore_bible/Rules_Data_Guide.md)**
    *   `rules.json`의 금지어와 제약 조건을 사람이 읽는 말로 풀어 둔 안내서.
11.  **[시간 사실 데이터 가이드](lore_bible/Temporal_Facts_Guide.md)**
    *   `temporal_facts.json`의 시간선, 상태, 유효 구간을 사람이 읽는 말로 풀어 둔 안내서.
12.  **[심리 프로필 데이터 가이드](lore_bible/characters/Psych_Profile_Data_Guide.md)**
    *   캐릭터 심리 JSON 필드가 무엇을 뜻하는지 읽기 쉽게 정리한 문서.
13.  **[에이든 심리 데이터 레거시 가이드](lore_bible/characters/Protagonist_Psych_Legacy_Guide.md)**
    *   `Protagonist_psych.json`이 최신 심리 모델이 아니라 레거시 브리지 데이터라는 점을 정리한 안내서.
14.  **[집필 프롬프트 템플릿](Guidelines/Writing_Prompt_Template.md)**
    *   설정집이 잠긴 뒤 쓰는 후행 문서. 지금은 참고만 하고, 집필 시작 전 다시 읽을 것.
15.  **[챕터 감수 체크리스트](Guidelines/Chapter_Audit_Checklist.md)**
    *   설정집 완료 후 초안 단계에서 쓰는 후행 검수 기준.

---

## 2. 📚 현재 작업 축
지금은 초안 집필보다 설정집 고정이 먼저입니다. 아래 문서는 앞으로 집필을 가능하게 만들 핵심 설계 축입니다.

1.  **[1권 세부 개요](outline/Vol_1_Outline.md)**
    *   1화~25화까지의 상세 플롯과 사건 전개.
2.  **[1권 타임라인](outline/Vol_1_Timeline.md)**
    *   날짜별 이동 경로 및 사건 발생 시간 (D-Day 기준).
3.  **[상아 의정회](lore_bible/groups/Ivory_Consistory.md)**
    *   1권의 주적. 황실 연금술 학회 내부의 비밀 결사이자 시간 조작 실험의 핵심 축.

---

### 👥 1권 주요 인물
*   [에이든](lore_bible/characters/Protagonist.md): 172회차, 감정 마모.
*   [아이리스](lore_bible/characters/Iris.md): 몰락한 천재 용병, 파트너.
*   [리아](lore_bible/characters/Ria.md): 표본 702호, 예언자.
*   [발타자르](lore_bible/characters/Baltazar.md): 상아 의정회의 전 수석 연구원. 초반 흑막처럼 보이는 레드헤링.
*   [아레시온](lore_bible/characters/Aresion.md): 추격자, 금기 병기.

### 👥 1권 보조 인물
*   [세베린](lore_bible/characters/Severin.md): 상아 의정회의 표본 회수 및 장부 봉인을 맡는 실무 얼굴.
*   [하르켄](lore_bible/characters/Harken.md): 카르세인의 현장 포획과 검문을 지휘하는 쇄장.
*   [미렐](lore_bible/characters/Mirel.md): 검은 시장 약방과 앰플 유통선을 쥔 중개상.
*   [카시아](lore_bible/characters/Cassia.md): 황궁 하급 서기관 겸 필경사. 잠입 파트의 생활 얼굴.
*   [레오니드 3세](lore_bible/characters/Leonid_III.md): 황궁 상층의 최종 승인권자.
*   [아이린](lore_bible/characters/Irene.md): 황실의 체면과 계승을 대표하는 황녀.
*   [마르첼란](lore_bible/characters/Marcellan.md): 황궁 출입선과 의전선을 쥔 궁내대신. 상층 실무 권력의 얼굴.
*   [시그룬](lore_bible/characters/Sigrun.md): 북부 전선에서 이름과 후송 명단을 붙드는 기록병.
*   [아르카누스](lore_bible/characters/Arcanus.md): 침묵의 상아탑의 대마도사이자 관측자.
*   [오렐](lore_bible/characters/Orel.md): 침묵의 상아탑 정적의 도서관에서 봉인 장부를 지키는 기록관.
*   [벨로니스](lore_bible/characters/Velonis.md): 침묵의 상아탑 하층 학구와 거래 문법을 맡는 조교수.
*   [세라피나](lore_bible/characters/Seraphina.md): 루미나 성전의 대신관. 선별과 봉인을 쥔 최고 성직자.
*   [루세아](lore_bible/characters/Lucea.md): 루미나 성전에서 시련과 선별을 감시하는 제관.
*   [이셀라](lore_bible/characters/Ysela.md): 루미나 성전 순례길과 묵상막의 문턱을 맡는 등잔 사제.
*   [자르칸](lore_bible/characters/Zarkan.md): 사루크 천막성의 물자와 선금을 쥔 조달장.
*   [제1권 보조 인물 연결 지도](lore_bible/Vol_1_Supporting_Cast_Link_Map.md): 네 인물이 어느 화에서 어떤 기능으로 쓰이는지 고정한 연결 기준.

### 👥 적대축 보강 문서
*   [12사도](lore_bible/characters/The_12_Apostles.md): 역병, 장례, 구휼, 루머, 잠복기를 쥔 종말론 집단.
*   [12사도 좌석 지도](lore_bible/characters/Twelve_Apostles_Seat_Map.md): 각 좌석이 도시의 어느 숨구멍을 장악하는지 정리한 배치표.
*   [알바른](lore_bible/characters/Alvarn.md): 상아 의정회의 비밀 칙행단.
*   [알바른 집행 조 편성표](lore_bible/characters/Alvarn_Execution_Cells.md): 세브락, 모르가나, 발로크, 셰이다르가 각자 어떤 공포와 처분을 맡는지 정리한 운용표.
*   [모르가나](lore_bible/characters/Morgana.md): 몸과 저주를 비틀어 공포를 만드는 집행자.
*   [발로크](lore_bible/characters/Balrok.md): 공개 파괴와 공포 시위를 맡는 집행자.
*   [셰이다르](lore_bible/characters/Sheidar.md): 정보 흐름을 늦추고 꼬아 버리는 집행자.
*   [적대축 배치 지도](lore_bible/Secondary_Antagonist_Deployment_Map.md): 12사도와 알바른의 개별 얼굴이 어느 권에서 어떤 공포로 먼저 들어와야 하는지 잠근 배치표.

### 🏰 1권 주요 세력
*   [황실 에스페란자](lore_bible/groups/Imperial_Court.md): 황궁 상층의 허가, 의전, 기록을 쥔 제국 권력 중심.
*   [황궁 상층 귀족 가문 지도](lore_bible/settings/Imperial_Court_Families.md): 발테론과 코르베스가 황궁 질서를 어떻게 받치는지 정리한 가문 지도.
*   [카르세인](lore_bible/groups/Carsein.md): 상아 의정회 산하의 사설 포획 부대.
*   [펜리르](lore_bible/groups/Fenrir.md): 회색 도시의 늑대 세력.
*   [시네르](lore_bible/groups/Sinere.md): 빈민가 자경단/해결사 축.
*   [하층 권세도](lore_bible/groups/하층_권세도.md): 시네르, 펜리르, 검은 시장, 해결사의 실제 맞물림.
*   [상아 의정회](lore_bible/groups/Ivory_Consistory.md): 황실 연금술 학회 내부의 비밀 결사.
*   [침묵의 상아탑 기관층](lore_bible/groups/Silent_Ivory_Tower.md): 상아탑의 관측, 기록, 봉인, 금기 연구 체계.
*   [루미나 성직층](lore_bible/groups/Lumina_Clergy.md): 성전의 선별, 정화, 봉인 실무를 굴리는 성직 기관.

### 🗺️ 장소
*   [수도 세라핌](lore_bible/locations/Imperial_Capital.md): 빈민가와 그림자 시장.
*   [세계 이동 지도](lore_bible/locations/World_Travel_Atlas.md): 수도, 북부, 동부, 남부, 서부 권역의 거리감과 이동 압박.
*   [세라핌 이동선 지도](lore_bible/locations/Seraphim_Transit_Map.md): 수도 안에서 검문선, 승강기, 수로, 하역문이 어떻게 맞물리는지 정리한 동선 지도.
*   [황궁 동선도](lore_bible/locations/Imperial_Palace_Transit_Map.md): 제3 하역문, 시종 회랑, 서고, 대연회장, 의정회 열람실을 나눈 상층 잠입 지도.
*   [황궁 야간 기록선](lore_bible/locations/Imperial_Palace_Night_Record_Line.md): 필경실 당직, 야간 열람 허가, 비공식 봉인 문서 반출입 절차를 정리한 실무 시트.
*   [황궁 의전선 일정표](lore_bible/locations/Imperial_Palace_Ceremonial_Schedule.md): 새벽 하역선, 아침 기록선, 정오 의전선, 심야 비밀선이 어떻게 갈리는지 정리한 시간표.
*   [황실 연금술 학회 내부도](lore_bible/locations/Imperial_Alchemy_Academy_Inner_Map.md): 진료홀, 봉인 창고, 격리층, 소각층, 0호 실험실을 나눈 내부 지도.
*   [상아 의정회 밀의회실](lore_bible/locations/Ivory_Consistory_Council_Chambers.md): 심의선, 봉인 열람실, 표본 승인/폐기 결재선을 정리한 내부 실무 공간 시트.
*   [마수의 땅](lore_bible/locations/Northern_Frontier.md): 코스믹 호러 최전선.
*   [북부 전선 구역도](lore_bible/locations/Northern_Frontier_Zone_Map.md): 후방 보급권, 서리 요새, 얼음 송곳니, 파락 구역을 나눈 작전 지도.
*   [서리 요새 세부 구조도](lore_bible/locations/Frost_Keep_Structure.md): 성루, 지휘실, 후송막사, 보급 적재장을 나눈 북부 핵심 요새 구조도.
*   [얼음 송곳니 전초도](lore_bible/locations/Ice_Fang_Frontline_Map.md): 결계 말뚝선, 교대 참호, 전초 막사, 능선, 외곽 살육장을 나눈 북부 최전방 전초도.
*   [침묵의 상아탑](lore_bible/locations/Magic_Tower.md): 인과율 방관자들.
*   [침묵의 상아탑 층별도](lore_bible/locations/Magic_Tower_Floor_Map.md): 입구, 학구, 금기 연구소, 정적의 도서관, 공허의 눈을 나눈 층별 지도.
*   [상아탑 금기 열람 승인선](lore_bible/locations/Silent_Ivory_Tower_Approval_Line.md): 누가 어떤 값으로 금기 문서와 봉인 장부를 열람하는지 정리한 상아탑 실무 시트.
*   [루미나 성전 내부도](lore_bible/locations/Holy_Temple_Inner_Map.md): 순례 회랑, 대성전, 시련의 탑, 지하 서고, 고삐 봉인실을 나눈 내부 구조도.
*   [루미나 성전 접근도](lore_bible/locations/Holy_Temple_Approach_Map.md): 산기슭 순례길, 정화문, 묵상막, 외곽 회랑, 대성전 문턱으로 이어지는 외부 접근 구조도.
*   [루미나 봉인 기록선](lore_bible/locations/Lumina_Seal_Record_Line.md): 봉인 장부, 순례 판정, 정화 실패 기록이 어떻게 묶이는지 정리한 성전 실무 시트.
*   [붉은 사막 거점도](lore_bible/locations/Red_Desert_Hub_Map.md): 바르카 협곡문, 벨사르 우물장, 사루크 천막성, 카르둠 환투장을 묶은 서부 사막 거점도.
*   [사루크 천막성 내부도](lore_bible/locations/Saruk_Camp_Map.md): 생활 고리, 실무 고리, 전투 고리, 심부를 나눈 서부 용병 거점 내부도.
*   [카르둠 환투장 구조도](lore_bible/locations/Kardum_Arena_Structure.md): 입장 마당, 내기 회랑, 원형장, 채무 감방, 암막 통로를 나눈 아이리스 과거 공간 구조도.

### ⚔️ 설정
*   [인과율 마법](lore_bible/magic/Causality_Magic.md): 대가, 서클, 고통.
*   [강제 귀환술 운영 시트](lore_bible/Forced_Return_Operation_Sheet.md): 미래측이 어떤 희생과 절차로 귀환술을 떠받치는지 정리한 운영 시트.
*   [마법 계통과 대가 운용표](lore_bible/magic/Magic_Disciplines_and_Costs.md): 점화, 방벽, 연성, 탐지, 강화, 금기계가 실전에서 어떤 대가와 함께 쓰이는지 정리한 운용표.
*   [하층 마법과 거리의 주술](lore_bible/magic/Gutter_Magic_and_Street_Rites.md): 회색 도시의 싸구려 부적, 약탕, 방비문, 하수도 주술을 정리한 생활형 마법 문서.
*   [하층 약방과 부적 실무](lore_bible/magic/Gutter_Apothecary_and_Talisman_Practice.md): 약방, 부적, 앰플, 응급 봉합이 실제로 어떻게 굴러가는지 정리한 하층 실무 시트.
*   [기관별 마법 문법](lore_bible/magic/Institutional_Magic_Doctrines.md): 학회, 의정회, 상아탑, 성전, 하층이 같은 마법을 어떻게 다르게 쓰는지 정리한 기준표.
*   [루미나 성전 의식과 정화 문법](lore_bible/magic/Holy_Temple_Rites_and_Purification.md): 성전의 정화, 봉인, 선별 의식이 어떤 절차와 대가로 움직이는지 정리한 세부 시트.
*   [변이체 도감](lore_bible/monsters/Creatures_of_the_Glitch.md): 구울, 역병 변이체.
*   [괴물 생태와 서식권](lore_bible/monsters/Monster_Ecology_and_Habitats.md): 역병 변이체, 연성 봉합체, 인과 항체가 어디서 태어나고 어떻게 남는지 정리한 생태 문서.
*   [권역별 괴물 위협 지도](lore_bible/monsters/Regional_Threat_Atlas.md): 수도, 북부, 상아탑, 성전, 사막, 후반 인과 항체까지 권역별 대표 위협을 정리한 지도.
*   [북부 전선 마수 개별 시트](lore_bible/monsters/Northern_Frontier_Bestiary.md): 설원 망령, 얼음 거인, 흰 울음 짐승, 파락 잔체를 정리한 북부 개별 위협 시트.
*   [붉은 사막 변이체 시트](lore_bible/monsters/Red_Desert_Abnormalities.md): 사혈 전갈, 모래 수복체, 불목 매, 유리능선 메아리 등 사막권 위협 시트.
*   [저주받은 이물](lore_bible/items/Cursed_Artifacts.md): 리스크가 있는 무기들.
*   [회색 역병](lore_bible/rules/Infection_Levels.md): 앰플, 마나 거부 반응.
*   [해결사 실무 시트](lore_bible/settings/Fixer_Procedure_Sheet.md): 의뢰, 선금, 안전가옥, 시체 처리, 실패 패널티를 장면 단위로 푼 시트.
*   [거리 거래 값 시트](lore_bible/settings/Street_Transaction_Value_Sheet.md): 하층 약방, 검문 뇌물, 해결사 선금, 표본 거래의 체감 가격표.
*   [인간관계도](lore_bible/Relationship_Map.md): 에이든, 리아, 아이리스, 발타자르, 영시 축이 어떻게 상처와 빚으로 얽히는지 정리한 문서.
*   [측면 인물 목격 지도](lore_bible/Supporting_Cast_Witness_Map.md): 류드, 바르그, 토마르, 펜리르, 카르세인이 에이든의 손상을 어떤 각도에서 목격하는지 정리한 문서.
*   [제1권 보조 인물 연결 지도](lore_bible/Vol_1_Supporting_Cast_Link_Map.md): 세베린, 하르켄, 미렐, 카시아를 제1권 장면 흐름에 맞게 배치한 지도.
*   [권역별 얼굴 배치 지도](lore_bible/Regional_Face_Deployment_Map.md): 시그룬, 오렐, 루세아, 자르칸을 어느 권에 어떤 기능으로 먼저 투입할지 정리한 배치 기준.
*   [중반부 감정 연속성](lore_bible/Mid_War_Emotional_Continuity.md): 4권부터 8권까지 전쟁 상흔, 공포, 소거, 행복 상실이 어떻게 누적되는지 고정한 문서.
*   [전반부 복선 지도](lore_bible/Front_Half_Foreshadow_Map.md): 1권부터 5권까지 어떤 단서를 미리 심어야 후반 반전이 공정하게 보이는지 정리한 문서.
*   [고정점 압력 지도](lore_bible/history/Fixed_Point_Pressure_Map.md): 어디가 고정점이고 어디가 분기점이며 압력이 어떻게 되돌아오는지 정리한 문서.
*   [엔딩 수렴 지도](lore_bible/Ending_Convergence_Map.md): 11권부터 15권까지 반전, 대가, 인간적 여운이 어떤 순서로 결말에 모여야 하는지 정리한 문서.

---

## 3. 🎼 AI 오케스트라 운영

여러 전문가 에이전트로 작업할 때는 아래 문서를 먼저 읽으십시오.

1. **[오케스트라 기준 문서](orchestra/SOURCE_OF_TRUTH.md)**
    *   어떤 파일이 진실 원본인지, 무엇을 먼저 믿어야 하는지 정리한 기준표.
2. **[설정 우선 모드](orchestra/SETTING_FIRST_MODE.md)**
    *   지금은 설정집 선완성 모드이며, 초안 집필 lane이 기본 동작이 아니라는 선언문.
3. **[오케스트라 운영 절차](orchestra/WORKFLOW.md)**
    *   설정 추가, 개연성 보강, 집필, 검수의 역할 분담과 순서.
4. **[RTTP 엔진](orchestra/RTTP_ENGINE.md)**
    *   이 작품 전용 작문 알고리즘, 총괄 권한, 하네스 실행 구조를 묶은 엔진 문서.
5. **[총괄 권한 잠금](orchestra/CONDUCTOR_AUTHORITY_LOCK.md)**
    *   총괄 오케스트라만 캐논 승인과 병합 권한을 가진다는 잠금 문서.
6. **[역할 맵](orchestra/MCP_SKILLS_AGENTS_HOOKS_HARNESS_MAP.md)**
    *   MCP, 스킬, 에이전트, 훅, 하네스가 각각 어디까지 책임지는지 정리한 경계표.
7. **[하네스 런타임 규칙](orchestra/HARNESS_RUNTIME_RULES.md)**
    *   preflight, dispatch, merge, verify, checkpoint의 실행 순서를 잠근 런타임 문서.
8. **[훅 카탈로그](orchestra/HOOK_CATALOG.md)**
    *   어떤 훅이 언제 발동하고 무엇을 경고하는지 정리한 실행 자동층 문서.
9. **[하네스-훅 매트릭스](orchestra/HARNESS_HOOK_MATRIX.md)**
    *   Lore, Foreshadow, Storycraft, Smoke 하네스가 어떤 훅을 기본으로 태우는지 정리한 매핑표.
10. **[핸드오프 패킷 플레이북](orchestra/HANDOFF_PACKET_PLAYBOOK.md)**
    *   설정 보강, 브리지 보강, 복선 보강을 어떤 패킷으로 시작할지 빠르게 정리한 문서.
11. **[패킷 기준 장부](orchestra/Packet_Baseline_Register.md)**
    *   Required Reads, Locked Facts, No-Touch, Deliverable, Stop Conditions를 패킷별로 잠근 기준표.
12. **[연속성 입력 장부](orchestra/Continuity_Input_Ledger.md)**
    *   직전 초안이 없을 때 어떤 문서 순서로 입력을 이어받을지 정리한 장부.
13. **[스모크 감사 하네스](orchestra/SMOKE_AUDIT_HARNESS.md)**
    *   주요 설정집 지도와 복선/엔딩 마커가 빠지지 않았는지 빠르게 점검하는 자동감사 안내서.
14. **[제1권 제1화 사전 핸드오프 패킷](orchestra/packets/Vol_1_Chapter_1_PreDraft_Packet.md)**
    *   집필을 열 때 첫 화가 무엇을 지켜야 하는지 미리 잠가 둔 패킷.
15. **[제1권 핵심 장면 압력표](orchestra/Vol_1_Core_Pressure_Grid.md)**
    *   제1권이 막별로 어떤 긴장과 감각을 남겨야 하는지 정리한 장면 압력 지도.
16. **[설정 우선 해제 게이트 점검](orchestra/SETTING_FIRST_EXIT_GATE_CHECK_2026-04-07.md)**
    *   지금 상태에서 집필 레인을 열 수 있는지 판정한 체크 문서.

---

## 4. 🗑️ 삭제 권고 파일
이 파일들은 구버전이므로 무시하거나 삭제하십시오. (혼란 방지)
*   `lore_bible/monsters/Bestiary.md`
*   `lore_bible/magic/Magic_System.md`
*   `lore_bible/items/Four_Kings_Weapons.md`
*   `lore_bible/SciFi_Elements_in_Fantasy.md`
*   `lore_bible/settings/` 폴더 내 중복 도시/역병 요약 파일들 (통합됨, 개별 문서 확인)

---
**준비 완료. 먼저 설정집을 잠그십시오. 집필은 그다음입니다.**
