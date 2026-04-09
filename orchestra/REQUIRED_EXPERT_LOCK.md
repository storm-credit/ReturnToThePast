# 필수 전문가 잠금

이 문서는 RTTP 오케스트라가 앞으로 잃어버리면 안 되는 `필수 전문가 풀`을 고정한다.

이 문서는 선택 메모가 아니라 `상시 기준 문서`다.  
총괄은 이 문서를 기준으로 전문가를 부르고, 하네스는 이 문서를 기준으로 기본 lane을 판정한다.

## 1. 총괄 고정

### `novel-orchestra-conductor`
- 역할: 범위 판단, 하네스 선택, 전문가 고용, 병합, 최종 승인
- 상태: `항상 고정`
- 비고: 어떤 전문가도 총괄 승인 없이 캐논을 확정하지 않는다.

## 2. 설정집 필수 전문가

아래 5명은 `설정집 단계 기본 고정 전문가`다.

### `character-architect`
- 인물, 욕망, 상처, 관계, 감정 손실

### `faction-strategist`
- 세력, 권력 논리, 정치 압박, 실무 구조

### `location-cartographer`
- 지역, 도시, 이동 압력, 분위기, 현장성

### `world-rule-keeper`
- 시간법칙, 대가, 역병, 세계 규칙

### `timeline-historian`
- 시간선, 고정점, 분기점, 사건 순서

## 3. 서사/집필 필수 전문가

아래 6명은 `집필 단계 기본 고정 전문가`다.

### `structure-architect`
- 엔딩 역순 설계, 권 구조, 브리지 설계

### `arc-psychologist`
- 감정선, 관계 이동, 상실 압박

### `foreshadow-bookkeeper`
- 복선 씨앗, 강화, 회수 장부

### `serial-tension-engineer`
- 웹소설 리듬, 장면 압력, 회차 끝 훅

### `scene-smith`
- 본문 초안

### `chapter-inspector`
- 화 단위 최종 검수

## 4. 필요 시 자동 호출하는 세분화 전문가

아래 전문가는 `항상 켜두진 않지만`, 병목이 보이면 총괄이 우선적으로 호출해야 하는 고정 후보들이다.

### 인물/세력/배경
- `building-cartographer`
- `relic-curator`
- `systems-chancellor`

### 마법/의식/생활 실무
- `ritual-liturgist`
- `street-apothecary`

### 몬스터/재난/역병
- `monster-ecologist`
- `bestiary-warden`

### 검수/스트레스 테스트
- `plausibility-warden`
- `hook-doctor`
- `reveal-choreographer`

## 5. 하네스별 기본 전문가 잠금

### `Lore Harness`
- 기본: `character-architect`, `faction-strategist`, `location-cartographer`, `world-rule-keeper`, `timeline-historian`
- 선택: `building-cartographer`, `ritual-liturgist`, `street-apothecary`, `monster-ecologist`, `bestiary-warden`, `relic-curator`, `systems-chancellor`

### `Foreshadow Harness`
- 기본: `structure-architect`, `foreshadow-bookkeeper`, `reveal-choreographer`
- 선택: `arc-psychologist`, `serial-tension-engineer`

### `Storycraft Harness`
- 기본: `structure-architect`, `arc-psychologist`, `serial-tension-engineer`
- 선택: `scene-smith`, `hook-doctor`

### `Smoke Harness`
- 기본: `chapter-inspector`
- 선택: `plausibility-warden`

### `Drafting Harness`
- 기본: `scene-smith`, `chapter-inspector`
- 선택: `hook-doctor`, `plausibility-warden`, `foreshadow-bookkeeper`, `arc-psychologist`

## 6. 분실 방지 규칙

- 총괄은 새 배치를 시작할 때 이 문서를 먼저 본다.
- 하네스는 `기본 전문가` 없이 시작하지 않는다.
- 전문가를 생략할 수는 있지만, 그 경우는 `총괄이 의도적으로 생략했다`고 본다.
- 새 전문가를 추가하면 이 문서에 먼저 등록한다.
- 등록되지 않은 전문가는 `임시 전문가`로만 취급한다.

## 7. 우선순위

전문가 관련 문서가 충돌하면 우선순위는 아래와 같다.

1. `REQUIRED_EXPERT_LOCK.md`
2. `CONDUCTOR_AUTHORITY_LOCK.md`
3. `HARNESS_RUNTIME_RULES.md`
4. `RTTP_ENGINE_AGENT_ROSTER.md`
