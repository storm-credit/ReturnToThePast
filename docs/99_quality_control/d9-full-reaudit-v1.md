# D9 세계관·설정집·설계도 전면 재감사 v1

Status: PASS AFTER REVISION — S0 0 / S1 0  
Date: 2026-08-07  
Owner: A02–A17 Orchestra  
Base Reviewed: main at `14887f0a1029e0d7caed68b75fc9efb833948210`  
Revision Branch: `agent/d9-red-team-revision`  
Pre-Writing Gate: CLOSED  
Manuscript: BLOCKED

## 1. 감사 방식

기존 D7·D8 PASS 선언을 근거로 재사용하지 않고 다음을 역방향 점검했다.

- 최상위 정본과 하위 문서의 상태·이름·OPEN 항목 충돌
- `[WORKING]`, `[ASSUMPTION]`, `DRAFT`, `REVIEW`, `SOFT LOCK` 잔존
- 시간여행 법칙과 실제 E001–E375 카드의 모순
- 정확한 연대·나이·주관적 경과·회복기간
- 국가·권역·종족·군사·미래 생존 규모
- 마법 능력·비용·대응책
- 엔진 정지와 생활기능 분리의 의존순서
- 17개 미스터리의 단서간격과 독자 추론 가능성
- 375화의 장면 수·훅·POV 리듬 반복
- 시스템 적대와 인간 대립자의 감정적 선명도
- 30개 인물 슬롯의 이름·첫 등장·최종상태
- 영구손실·유산·신수·법·경제·물류·결말 연속성

## 2. 재감사에서 발견된 S1과 조치

### S1-01 — 정본 계층 불일치

**발견**
- [`canon-constitution-v1.md`](../00_project/canon-constitution-v1.md)는 제목·로맨스·최종 적·엔딩·연대간격을 OPEN으로 유지했다.
- D8 완료문서는 같은 항목을 확정했다고 선언했다.
- 초기 DRAFT·REVIEW 문서가 최신 정본을 다시 덮을 위험이 있었다.

**조치**
- [`docs/00_project/D9_CANON_AMENDMENT.md`](../00_project/D9_CANON_AMENDMENT.md)
- 정본 우선순위와 확정값, 남은 제작 OPEN을 분리했다.

**결과**: CLOSED

### S1-02 — 첫 출발 앵커 규칙 충돌

**발견**
- 시간여행 온톨로지는 살아 있는 현지 연결점을 출발 필수처럼 적었다.
- V1 E004는 현지 앵커 없이 출발을 승인했다.

**조치**
- 필수인 **역사주소 앵커**와 안전조건인 **살아 있는 현지 앵커**를 분리했다.
- 첫 임무는 세렌 사건기록·회색 종·서부 장부를 역사주소로 사용한다.
- [`causal-propagation-and-memory-protocol-v1.md`](../03_systems/causal-propagation-and-memory-protocol-v1.md)
- [`v01-d9-correction-overlay.md`](../10_story_architecture/detail/v01-d9-correction-overlay.md)

**결과**: CLOSED

### S1-03 — 정확한 연대·나이·주관적 시간 부재

**발견**
- Era O/N/F는 있었으나 정확한 연도, 에이든과 젊은 에이든의 나이, 권간 체류·회복시간이 없었다.
- 장거리 시간여행물의 인과·부상·관계누적을 검증할 수 없었다.

**조치**
- CY 0 건국협약, Era N CY 640, F0 CY 664, 24년 간격 확정
- 에이든 출발 41세, 젊은 에이든 17세
- E001–E375 주관적 경과 1,214일 확정
- [`master-chronology-and-aging-ledger-v1.md`](../01_timeline/master-chronology-and-aging-ledger-v1.md)

**결과**: CLOSED

### S1-04 — 인구·병력·재난 규모 부재

**발견**
- 정치·생존률·기근을 다루면서 왕국 총인구, 미래 생존자, 군대와 사망규모 기준이 없었다.

**조치**
- Era N 실질 생활인구 약 880만
- 권역·문화권 인구, F0/F1/F2/F3/P1 생존규모
- 상비군 5.4만, 비상동원·시간요원 상한
- 회색 재앙과 장치 즉시정지 피해 범위
- [`demographic-and-scale-ledger-v1.md`](../02_world/demographic-and-scale-ledger-v1.md)

**결과**: CLOSED

### S1-05 — 장기 미스터리 재점화 부족

**발견**
- 기존 장부는 첫 단서·중간 반전·최종 회수만 있어 M03·M04·M06 등은 100~200화 넘게 약해질 수 있었다.

**조치**
- M01–M17 각각 재점화 회차, 오답 강화, 독자 추론 가능 시점 확정
- 핵심 미스터리 최대 50화 무언급 금지
- [`mystery-reinforcement-ladder-v1.md`](../11_mystery/mystery-reinforcement-ladder-v1.md)

**결과**: CLOSED

### S1-06 — 375화 3장면 획일화

**발견**
- 15개 D6 상세파일 모두 Scene 1–3을 사용하고 Scene 4는 존재하지 않았다.
- 기능 비트가 실제 고정 장면 수로 오해될 위험이 있었다.

**조치**
- 기존 세 장면을 목표·충돌·선택의 기능 비트로 재정의
- 실제 원고 장면 수 2~6
- Q/S/E/X 밀도형, 권별 변주 회차, 7개 훅 유형과 연속반복 제한
- [`scene-density-and-pacing-overlay-v1.md`](../10_story_architecture/scene-density-and-pacing-overlay-v1.md)

**결과**: CLOSED

### S1-07 — 일반 마법 운용 상한 부족

**발견**
- 네 마법 계열과 비용은 있었지만 전투·치료·통신의 범위·준비·지속·대응 기준이 정성적이었다.

**조치**
- L0 생활기술~L4 문명장치 구분
- 계열별 할 수 없는 것·비용·대응
- 단독 마법사·팀·기관방벽·치료·통신 기준
- [`magic-capability-and-counterplay-matrix-v1.md`](../03_systems/magic-capability-and-counterplay-matrix-v1.md)

**결과**: CLOSED

### S1-08 — 결말 기능분리의 기술 인과 부족

**발견**
- 시간개입과 생활안정을 분리한다는 결말은 정해졌지만 층별 의존성과 분리순서가 충분히 고정되지 않았다.

**조치**
- 생활안정층 A, 주소·부담층 B, 연대운영층 C, 강제개입층 D
- S1~S7 공개·대피·우선순위 잠금·출발폐쇄·귀환종료·지역복제·감사분산·D층 폐쇄 순서
- 실패 모드와 유산 분해 역할 확정
- [`engine-dependency-and-separation-protocol-v1.md`](../03_systems/engine-dependency-and-separation-protocol-v1.md)

**결과**: CLOSED

### S1-09 — 30개 인물 슬롯의 확정도 불일치

**발견**
- D8 상태는 인물 30명을 완료했다고 했지만 기존 백과에는 슬롯·후보·이름 미확정·로맨스 미정 표현이 남았다.

**조치**
- C01–C30 정식명, 시대, 핵심 등장권, 최종상태 확정
- C30만 결말 주제상 의도적으로 익명 유지
- [`cast-canon-index-v2.md`](../05_characters/cast-canon-index-v2.md)

**결과**: CLOSED

### S1-10 — 시스템 적대의 인간적 얼굴 부족

**발견**
- 구조적 적대는 강하지만 15권 동안 감정적으로 맞설 대립자가 흐려질 위험이 있었다.

**조치**
- GA I 아르덴 케르·세렌 바일
- GA II 마르칸 베르·다렌 모트
- GA III 오르바드 카르센·레오르 세르바
- GA IV 카시안 로드·젊은 에이든
- GA V 유나 벨·하렌 세른·레오르 계승축
- 수장 제거로 체제해결 금지
- [`antagonist-face-ladder-v1.md`](../04_factions/antagonist-face-ladder-v1.md)

**결과**: CLOSED

## 3. S0 재검사

### 회귀·리셋 오염
없음. 직접 육체시간여행과 한 줄의 주관적 생애 유지.

### 영구손실 우회
없음. 세렌·마르칸·변경도시·리아 사적기억·에이든 역사주소·백지권 일부 복구 금지.

### 평행세계 편의
없음. 귀환실패는 고립·오착·주소손상이며 편의적 새 세계를 만들지 않음.

### 주인공 권한독점
없음. 일곱 운영권과 지역·종족·당사자 거부권 유지.

### 장치파괴 자동해결
없음. A/B/C/D 층과 S1–S7 분리 절차 확정.

### 참고작 고유요소 복제
없음. 아홉 상처는 번호조직이 아니며 바이러스 원점·예언집단·간부 제거 구조 없음.

**S0 OPEN: 0**

## 4. 세계관·설정집 재판정

### 지리·도시·이동
- 8권역·수도 9구역·외부동맹·백지권
- 이동일·강운·항로·고정환·보급
- 인구와 식량 수요 추가
- PASS

### 문화·종족
- 인간·에르나·카르둔·라하크·네바르와 주소상실자
- 가족·교육·장례·언어·복식·내부파벌
- 이름 확정과 옛 WORKING 표기 우선순위 정리
- PASS

### 마법·질병
- 네 계열·L0–L4·비용·대응
- 마나열병 5단계·진단·치료·법적 악용
- PASS

### 경제·법·기관
- 화폐·물가·임금·세금·복지·신용
- 출생·혼인·사망·주소상실·상속·시간임무 절차
- A/B/C/D 의존층과 분리순서
- PASS

### 세력·인물
- 14개 세력·30 인물 ID
- Grand Act별 대립자와 지지기반
- 독립욕망·정보상한·최종상태
- PASS

### 유산·신수
- R01–R12, B01–B05
- 동의·소유·한계·최종상태
- 결말의 분해·봉인·파괴와 생활망 전환
- PASS

## 5. 설계도 재판정

- 5 Grand Acts: PASS
- 15 Volume Acts: PASS
- 30 Arc: PASS
- 60 Subact: PASS
- E001–E375 인과·상태변화: PASS
- 정확한 연대·주관적 경과: PASS AFTER REVISION
- 미스터리 재점화: PASS AFTER REVISION
- 장면밀도·훅 변주: PASS AFTER REVISION
- 대립자 감정축: PASS AFTER REVISION
- 엔딩 기술·행정 인과: PASS AFTER REVISION

## 6. 남은 S2

다음은 차단 문제가 아니라 제작·시장·표현 단계다.

1. 플랫폼별 무료·유료 전환과 회차 길이 최적화
2. 실제 이미지 형태의 대륙·수도 지도
3. 인물·복식·유산·주권신수 콘셉트 아트
4. Gate 개방 뒤 문체·대사·전투 전달력 샘플
5. 원고 집필 중 실제 독자반응에 따른 비차단 리듬 조정

## 7. 최종 판정

- 최초 재감사 발견 S1: 10건
- 수정 후 S1 OPEN: 0
- S0 OPEN: 0
- D7 Story Architecture: 유지·보정 완료
- D8 World Encyclopedia: 유지·보정 완료
- D9 Full Re-audit: PASS AFTER REVISION
- Manuscript: NOT STARTED
- Pre-Writing Gate: CLOSED

정확한 완료 표현:

> 세계관·설정집·375화 설계도는 상세설계 상태지만, D8 완료 선언 뒤 남아 있던 정본계층·출발조건·연대·규모·미스터리·장면리듬·마법상한·기능분리·인물확정·대립자축의 S1 열 건을 D9에서 발견하고 보정했다. 현재 차단 문제는 0건이며 원고와 실제 이미지는 아직 제작하지 않았다.
