# 오케스트라 분리 가능성 감사 보고서

Date: 2026-04-07
Mode: `SETTING-FIRST`
Verdict: `PORTABLE WITH SEPARATION`

## 한줄 결론

현재 오케스트라는 **다른 소설에도 재사용 가능하다.**
다만 지금 상태는 `재사용 코어`와 `이 작품 전용 캐논`이 함께 엉켜 있으므로,
나중에 따로 떼어 쓰려면 `코어 / 프로젝트 설정 / 작품 본문`을 분리하는 작업이 필요하다.

즉, **못 쓰는 시스템이 아니라, 이미 쓸 만한데 아직 포장되지 않은 시스템**에 가깝다.

---

## 1. 지금 바로 재사용 가능한 코어

아래 요소는 작품이 달라져도 거의 그대로 옮길 수 있다.

### A. 운영 방식
- `오케스트라 총괄 -> 전문가 분기 -> 병합 -> 감사`라는 흐름
- `설정 보강 / 개연성 점검 / 복선 감사 / 구조 설계`를 서로 다른 lane으로 나누는 방식
- 필요할 때만 lane을 태우고, 전부 다 돌리지 않는 conductor 방식

### B. 패킷 계약
- [packet-contract.md](C:/Users/Raino%20PI/Documents/New%20project/repo_inspect/.agent/skills/novel-orchestra-conductor/references/packet-contract.md)
- 작업마다 `Mission`, `Target`, `Locked Facts`, `Editable Targets`, `Stop Conditions`를 잠그는 방식
- 전문가 출력 형식을 `Decision / Findings / Required Changes / Assumptions / Handoff`로 고정하는 방식

### C. 역할 분리 사상
- [role-map.md](C:/Users/Raino%20PI/Documents/New%20project/repo_inspect/.agent/skills/novel-orchestra-conductor/references/role-map.md)
- `lore / plausibility / structure / reveal / arc / foreshadow`를 분리하는 구조
- 설정이 흔들릴 때는 prose보다 canon repair를 먼저 한다는 규율

### D. 하네스 개념
- `LORE_AUDIT_HARNESS`
- `FORESHADOW_HARNESS`
- `STORYCRAFT_HARNESS`
- `SMOKE_AUDIT_HARNESS`

이 4개는 다른 장르로 가더라도 이름만 조금 바꾸면 그대로 쓸 수 있다.

---

## 2. 지금 작품에 강하게 묶여 있는 부분

아래는 그대로 복사하면 다른 소설에서 오히려 방해가 되는 영역이다.

### A. 폴더 구조 가정
- `lore_bible`
- `outline`
- `Guidelines`
- `Drafts`
- `orchestra`

현재 스크립트와 문서는 이 구조를 당연하게 전제한다.

### B. 작품 전용 진실 체계
- [SOURCE_OF_TRUTH.md](C:/Users/Raino%20PI/Documents/New%20project/repo_inspect/orchestra/SOURCE_OF_TRUTH.md)
- [Start_Here.md](C:/Users/Raino%20PI/Documents/New%20project/repo_inspect/Start_Here.md)
- [Prompt_Quick_Reference.md](C:/Users/Raino%20PI/Documents/New%20project/repo_inspect/Guidelines/Prompt_Quick_Reference.md)
- [Time_Travel_Frame.md](C:/Users/Raino%20PI/Documents/New%20project/repo_inspect/Guidelines/Time_Travel_Frame.md)

이건 이 작품의 시간여행 패러독스 프레임, 15권 구조, 톤 금지선까지 잠가 둔 레이어라 다른 작품엔 그대로 못 쓴다.

### C. 작품 전용 스모크 룰
- 권당 25화
- 화당 3,500자 이상
- 특정 복선 마커
- 특정 엔딩 수렴 마커
- 특정 세력/용어/캐논 충돌 검사

하네스 구조는 재사용 가능하지만, 규칙 파일 내용은 작품마다 새로 갈아야 한다.

### D. 스크립트의 직접 가정
- [build_work_packet.py](C:/Users/Raino%20PI/Documents/New%20project/repo_inspect/.agent/skills/novel-orchestra-conductor/scripts/build_work_packet.py)

현재는:
- `Vol_*`
- `Chapter_*`
- `Drafts/Vol_x/`
- `lore_bible/**`
같은 경로와 이름 규칙을 직접 전제한다.

즉 이 스크립트는 `재사용 불가`가 아니라, `설정 파일을 받지 않는 1작품용 빌더`다.

---

## 3. 분리 난이도 판정

### 쉬운 것
- 역할 체계
- 패킷 계약
- 총괄 운영 절차
- 하네스 개념
- 감사 리포트 형식

### 중간 난이도
- 스크립트 일반화
- 경로 규약 외부화
- 프로젝트별 설정 파일 도입

### 어려운 것
- 완전 자동화된 범용 하네스
- 장르마다 다른 규칙을 한 엔진에서 우아하게 처리하는 것

결론적으로,
`문서형 운영체계`는 분리하기 쉽고,
`스크립트형 자동화`는 한 번 더 추상화가 필요하다.

---

## 4. 추천 분리 구조

나중에 따로 떼어낼 때는 아래 3층 구조가 가장 안정적이다.

### 1층. Core Orchestra
이건 작품과 무관하게 유지한다.

- conductor 철학
- lane 체계
- packet contract
- handoff templates
- generic workflow
- generic smoke audit skeleton

### 2층. Project Config
작품마다 새로 갈아끼운다.

- 장르 프레임
- 권수/화수 규칙
- 금지어
- 이름 규칙
- source of truth 순서
- 폴더 구조
- smoke markers

### 3층. Project Canon
실제 작품 내용이다.

- lore
- outline
- timeline
- maps
- factions
- characters
- endings

이렇게 나누면 다른 소설에는 `2층`과 `3층`만 갈아끼우면 된다.

---

## 5. 다른 소설에 옮길 때 필요한 최소 파일

새 프로젝트를 만들 때 최소한 아래는 새로 작성해야 한다.

1. `Start_Here`
2. `SOURCE_OF_TRUTH`
3. `Prompt_Quick_Reference`
4. `Setting_Audit_Scope`
5. `Series_Production_Constraints`
6. `Series_Roadmap`
7. `Naming_Style_Guide`
8. 프로젝트별 감사 규칙 파일

즉, 코어를 옮긴 뒤에도 `프로젝트 설정 레이어`는 반드시 다시 써야 한다.

---

## 6. 지금 이 저장소에서 당장 가능한 분리 준비

지금 당장 무리하게 분리할 필요는 없다.
대신 아래처럼 `분리 준비`를 해두면 된다.

- 범용 문서와 작품 전용 문서를 구분해 태그 붙이기
- 스크립트가 직접 경로를 박지 않도록 추후 설정 파일 자리 만들기
- 새 작품 부트스트랩 체크리스트를 만들어 복제 단계를 표준화하기
- 지도, 인물, 세력, 복선 장부처럼 장르 불문 재사용되는 문서 유형을 템플릿화하기

---

## 7. 최종 판정

### 판정
- **다른 소설에도 적용 가능**: `예`
- **나중에 따로 분리해서 사용 가능**: `예`
- **지금 상태 그대로 복사만 하면 끝나는가**: `아니오`

### 이유
- 운영 사상과 문서 구조는 이미 충분히 강하다.
- 다만 현재는 `ReturnToThePast 전용 캐논`과 `오케스트라 코어`가 섞여 있다.
- 그래서 **한 번 더 레이어를 나누면, 이후 다른 작품에 재사용하는 시스템으로 충분히 독립시킬 수 있다.**

---

## 8. 다음 추천

다음 단계로 가장 효율적인 건 둘 중 하나다.

1. `오케스트라 부트스트랩 체크리스트`를 만들어서 다른 소설용 시작 절차를 표준화
2. `세계 이동 지도 / 도시 지도 / 건물 지도`를 보강해서, 이 작품 안에서도 재사용 가능한 배경 설계 체계를 더 단단하게 만들기

이번 패스에서는 두 번째 작업과 함께, 첫 번째의 기초 문서도 같이 만드는 것이 가장 효율적이다.

---

## 9. 현재 마련된 분리 준비 문서

- `CORE_LAYER_MAP.md`: 코어 / 프로젝트 설정 / 작품 캐논 분리 기준
- `modules/novel-orchestra-core/README.md`: 현재 재사용 코어에 붙인 모듈 이름과 경계
- `templates/NOVEL_ORCHESTRA_BOOTSTRAP_CHECKLIST.md`: 새 작품 시작 체크리스트
- `templates/PROJECT_PROFILE_TEMPLATE.md`: 프로젝트 설정층 프로필 틀
- `templates/SOURCE_OF_TRUTH_TEMPLATE.md`: 문서 우선순위 템플릿
- `templates/SETTING_AUDIT_RULES_TEMPLATE.json`: 새 작품용 자동감사 규칙 뼈대

즉, 지금은 `분리 가능` 판정만 있는 상태가 아니라,
실제로 다음 작품에 옮길 때 쓸 수 있는 최소 템플릿까지 갖춘 상태다.
