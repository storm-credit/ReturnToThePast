# RTTP 엔진 에이전트 구성표

이 문서는 총괄 오케스트라가 언제 어떤 전문가를 고용하는지 정리한 표다.

상시 고정 전문가 기준은 `REQUIRED_EXPERT_LOCK.md`를 우선한다.

핵심 원칙은 단순하다.

- 총괄은 항상 `novel-orchestra-conductor`
- 병목이 생긴 도메인만 고른다
- 먼저 좁은 전문가를 쓰고, 더 큰 합성 판단이 필요할 때 상위 lane으로 올린다

---

## 1. 총괄

### `novel-orchestra-conductor`
- 역할: 범위 판단, lane 선택, 병합, 최종 결정
- 모델: `gpt-5.4`
- 추론: `high`
- 항상 직접 맡는 일:
  - 우선순위 결정
  - 하네스 선택
  - 결과 병합
  - 최종 커밋 기준 결정
  - setting-first 해제 여부 결정
  - 전문가 결과 승인 / 보류 / 폐기 판정

총괄 권한의 자세한 잠금은 `orchestra/CONDUCTOR_AUTHORITY_LOCK.md`를 우선한다.

---

## 2. 설정집 기본 전문가

### `character-architect`
- 인물, 욕망, 상처, 관계, 감정 손실
- 모델: `gpt-5.4`
- 추론: `high`

### `faction-strategist`
- 세력, 권력 논리, 정치 압박, 실무 구조
- 모델: `gpt-5.4`
- 추론: `high`

### `location-cartographer`
- 지역, 도시, 이동 압력, 분위기
- 모델: `gpt-5.4`
- 추론: `medium`

### `world-rule-keeper`
- 시간법칙, 대가, 역병, 세계 규칙
- 모델: `gpt-5.4`
- 추론: `high`

### `timeline-historian`
- 시간선, 고정점, 분기점, 사건 순서
- 모델: `gpt-5.4`
- 추론: `high`

---

## 3. RTTP 엔진 세분화 전문가

### `building-cartographer`
- 건물 내부도, 방 구조, 잠입 동선, 출입문, 경비선
- 언제 쓰나:
  - 황궁, 상아탑, 성전, 학회, 요새처럼 사건이 반복되는 건물
- 모델: `gpt-5.4-mini`
- 추론: `medium`

### `ritual-liturgist`
- 의식, 정화, 봉인, 제례, 성전/종교 마법 문법
- 언제 쓰나:
  - 성전, 봉인실, 정화 의식, 서약문이 핵심일 때
- 모델: `gpt-5.4`
- 추론: `medium`

### `street-apothecary`
- 하층 약방, 앰플, 부적, 응급 봉합, 약재 유통
- 언제 쓰나:
  - 회색 도시 생활 마법, 약방 장면, 저급 연금술 보강
- 모델: `gpt-5.4-mini`
- 추론: `medium`

### `monster-ecologist`
- 생태, 발생지, 환경 압력, 군집성과 오염 논리
- 언제 쓰나:
  - 괴물의 서식과 위협 지도, 역병 확산 구조
- 모델: `gpt-5.4`
- 추론: `medium`

### `bestiary-warden`
- 개별 괴물 시트, 위협 문법, 약점, 권역별 대표종
- 언제 쓰나:
  - 북부 마수, 사막 변이체, named horror 시트
- 모델: `gpt-5.4-mini`
- 추론: `medium`

### `relic-curator`
- 유물, 저주템, 무기, 소지품 연속성
- 모델: `gpt-5.4`
- 추론: `medium`

### `systems-chancellor`
- 경제, 화폐, 길드, 귀족, 카르텔, 생존 시스템
- 모델: `gpt-5.4`
- 추론: `medium`

---

## 4. 서사 설계 전문가

### `structure-architect`
- 엔딩 역순 설계, 볼륨 구조, 브리지 설계
- 모델: `gpt-5.4`
- 추론: `high`

### `arc-psychologist`
- 감정선, 신뢰 이동, 정체성 압박
- 모델: `gpt-5.4`
- 추론: `high`

### `reveal-choreographer`
- 비밀 공개 순서, 레드헤링, 진실 사다리
- 모델: `gpt-5.4`
- 추론: `high`

### `foreshadow-bookkeeper`
- 씨앗, 강화, 회수 장부
- 모델: `gpt-5.4`
- 추론: `high`

### `serial-tension-engineer`
- 웹소설 리텐션, 장면 압력, 화 끝 압박
- 모델: `gpt-5.4`
- 추론: `medium`

---

## 5. 집필/검수 전문가

이 레인은 `설정 우선`이 풀린 뒤에만 연다.

### `scene-smith`
- 본문 초안
- 모델: `gpt-5.4`
- 추론: `high`

### `hook-doctor`
- 오프닝, 회차 끝 hook, 당김
- 모델: `gpt-5.4-mini`
- 추론: `medium`

### `chapter-inspector`
- 최종 검수
- 모델: `gpt-5.4`
- 추론: `medium`

### `plausibility-warden`
- 병합 뒤 전체 개연성 스트레스 테스트
- 모델: `gpt-5.4`
- 추론: `medium`

---

## 6. 기본 고용 규칙

필수 기본 전문가 잠금은 `REQUIRED_EXPERT_LOCK.md`를 기준으로 한다.  
이 문서는 그 잠금을 바탕으로 `언제 호출하는가`를 더 풀어 쓴 운영 문서다.

### 설정집 단계
- 총괄 단독으로 범위를 잠근다
- 필요한 기본 전문가만 연다
- 세부 빈칸이 보이면 세분화 전문가를 추가한다
- 마지막 병합은 `plausibility-warden`으로 스트레스 테스트한다

### 집필 단계
- 먼저 `structure`/`arc`/`foreshadow`/`cadence`로 설계를 잠근다
- 그다음 `scene-smith`
- 마지막에 `hook-doctor`와 `chapter-inspector`

## 6-1. 잃어버리면 안 되는 기본 전문가

아래 전문가는 앞으로 RTTP 오케스트라가 기본으로 기억해야 하는 고정 roster다.

- 총괄: `novel-orchestra-conductor`
- 설정집 기본: `character-architect`, `faction-strategist`, `location-cartographer`, `world-rule-keeper`, `timeline-historian`
- 서사/집필 기본: `structure-architect`, `arc-psychologist`, `foreshadow-bookkeeper`, `serial-tension-engineer`, `scene-smith`, `chapter-inspector`
- 검수/스트레스 테스트 기본 후보: `plausibility-warden`, `hook-doctor`, `reveal-choreographer`

세분화 전문가와 하네스별 기본 조합은 `REQUIRED_EXPERT_LOCK.md`를 따른다.

---

## 7. 토큰 절약 원칙

- 큰 캐논 결정: `gpt-5.4 high`
- 좁은 도메인 보강: `gpt-5.4 medium`
- 반복적이고 좁은 시트 작업: `gpt-5.4-mini medium`
- 빠른 조회성 검토: `gpt-5.4-mini low~medium`

즉, "항상 최고"가 아니라 "병목에만 높은 추론"이 RTTP 엔진의 기본이다.

---

## 8. 총괄 우선 원칙

- 어떤 전문가도 총괄을 건너뛰어 캐논을 확정하지 않는다.
- 병렬 전문가는 조사와 제안에 강하고, 총괄은 병합과 승인에 강하다.
- 전문가 수가 늘수록 `CONDUCTOR_AUTHORITY_LOCK.md`의 우선순위가 올라간다.
