# 패킷 기준 장부

> 이 문서는 RTTP 엔진이 쓰는 모든 패킷이 최소한 어떤 항목을 가져야 하는지 잠그는 장부다.

---

## 1. 공통 필수 항목

모든 패킷은 아래 항목을 포함한다.

- `Required Reads`
- `Locked Facts`
- `Editable Targets`
- `No-Touch Files`
- `Deliverable`
- `Stop Conditions`

## 2. 패킷별 강조점

### 챕터 집필 패킷
- Required Reads: 현재 권 Outline, Timeline, 공통 잠금, 핵심 캐릭터 파일
- Locked Facts: 부상, 위치, 대가, 관계, 진실 노출 한계
- Deliverable: 본문
- Stop Conditions: 캐논 충돌, 진실 과노출, 분량 미달

### 설정 보강 패킷
- Required Reads: 관련 캐논 문서, 인덱스, 진입점
- Locked Facts: 기존 정식명, 권별 사건 고정선
- Deliverable: 새 시트 또는 보강 문서
- Stop Conditions: 기존 캐논을 갈아엎어야 하는 상황

### 복선 보강 패킷
- Required Reads: 복선 장부, 엔딩 수렴 지도, 현재 권 아웃라인
- Locked Facts: 회수 위치, 레드헤링 공정성, 진실 공개 순서
- Deliverable: 복선 추가안 또는 수정안
- Stop Conditions: 속임수가 사기로 느껴지는 수준

### 검수 패킷
- Required Reads: 공통 잠금, 체크리스트, 관련 캐논 문서
- Locked Facts: 금지어, 고유명사, 시간법칙
- Deliverable: Critical / Warning / Minor findings
- Stop Conditions: 기준 문서 부재

## 3. 운영 규칙

- 패킷은 길기보다 `자급자족 가능`해야 한다.
- 직전 초안이 없으면 `Continuity_Input_Ledger.md`를 함께 읽힌다.
- 패킷이 기준을 못 채우면 dispatch 전에 총괄이 먼저 보강한다.
