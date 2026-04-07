# 시간 사실 데이터 가이드

이 문서는 `lore_bible/temporal_facts.json`을 사람이 읽기 쉽게 풀어 둔 설명층이다.

## 이 파일이 하는 일

- 시간선별 사건 상태를 그래프 엔진이 읽기 쉽게 적재한다.
- 같은 사건이 `이전 시간선`과 `현재 시간선`에서 어떻게 달라졌는지 비교할 수 있게 한다.
- 패러독스 점검 시 어떤 사실이 언제 유효한지 빠르게 확인하게 돕는다.

## 핵심 키 뜻

- `entity`: 추적 대상 사건 또는 인물
- `status`: 해당 시점에서의 상태
- `timeline`: 어느 시간선에 속하는지
- `valid_at`: 이 상태가 유효해지는 기준 연도
- `invalid_at`: 이 상태가 더 이상 유효하지 않은 시점

## 현재 시간선 표기 읽는 법

- `Previous`: 멸망으로 향한 이전 시간선
- `Current`: 에이든이 돌아온 뒤 다시 진행 중인 현재 시간선
- `9999`: 사실상 상한이 열려 있다는 뜻의 임시 종료값

## 운용 원칙

- JSON 구조는 그래프 적재를 위해 유지한다.
- 사람이 읽는 설명은 이 문서나 관련 역사 문서에서 보강한다.
- 상태 설명은 짧게 유지하되, 설정집 본문과 충돌하는 표현은 쓰지 않는다.

## 수정할 때 주의할 점

- `entity`, `status`, `timeline`, `valid_at`, `invalid_at`는 그래프 엔진이 직접 읽는다.
- 시간선 이름이나 상태 표면을 함부로 바꾸면 조회 결과가 달라질 수 있다.
- 사건 의미를 길게 풀고 싶으면 JSON 대신 역사 문서에 적는다.

## 같이 읽을 문서

- `lore_bible/history/Timeline_Original.md`
- `lore_bible/history/Fixed_Points_and_Branches.md`
- `lore_bible/history/Fixed_Point_Pressure_Map.md`
- `orchestra/ENGINE_DATA_LAYER_POLICY.md`
