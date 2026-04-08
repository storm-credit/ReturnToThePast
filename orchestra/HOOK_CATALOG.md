# 훅 카탈로그

이 문서는 RTTP 엔진에서 쓰는 훅을 `이름 / 발동 시점 / 하는 일 / 하지 않는 일` 기준으로 잠근다.

## 1. 공통 런타임 훅

### `preflight`
- 발동 시점: pass 시작 직후
- 하는 일:
  - 병목 한 줄 정의 확인
  - 하네스 선택 확인
  - no-touch 파일 잠금
  - required reads 잠금
- 하지 않는 일:
  - 파일 병합
  - 캐논 승인

### `dispatch`
- 발동 시점: preflight 직후
- 하는 일:
  - 총괄이 전문가 사용 여부 결정
  - 모델 / 추론 강도 선택
  - packet 범위 분배
- 하지 않는 일:
  - 총괄 없는 자동 전문가 증식

### `merge`
- 발동 시점: 전문가 findings 수집 뒤
- 하는 일:
  - 충돌 목록 정리
  - 반영 / 유예 / 기각 분류
  - 병합 순서 결정
- 하지 않는 일:
  - 하네스 PASS만 보고 자동 승인

### `verify`
- 발동 시점: 수정 반영 뒤
- 하는 일:
  - 관련 하네스 재실행
  - smoke 재실행
  - 빠진 마커 및 링크 확인
- 하지 않는 일:
  - FAIL 상태 push 허용

### `checkpoint`
- 발동 시점: pass 종료 직전
- 하는 일:
  - self-contained 여부 확인
  - 커밋 범위 재확인
  - session state / 큐 갱신 필요성 확인
- 하지 않는 일:
  - 사용자 상태 파일 자동 포함

## 2. Lore 훅

### `lore-gap-hook`
- 얇은 인물, 세력, 장소, 규칙, 마법, 몬스터 층을 경고한다.

### `canon-conflict-hook`
- 동일 사건의 대가, 시간법칙, 적대축 설명이 문서마다 어긋나면 경고한다.

### `naming-conflict-hook`
- 작명 계통 충돌, 의미 중복, 톤 불일치를 경고한다.

### `setting-first-hook`
- 설정집에서 끝낼 일을 초안 lane으로 밀어 넘기려 할 때 경고한다.

## 3. Foreshadow 훅

### `seed-payoff-hook`
- 회수는 있는데 씨앗이 없거나, 씨앗은 있는데 회수가 없을 때 경고한다.

### `reveal-fairness-hook`
- 레드헤링만 있고 진짜 단서가 얇을 때 경고한다.

### `ending-convergence-hook`
- 후반 리빌이 엔딩 감정과 따로 놀면 경고한다.

## 4. Storycraft 훅

### `arc-pressure-hook`
- 권/장면 압력이 늘어지거나 중간부 동력이 약해질 때 경고한다.

### `bridge-gap-hook`
- 권과 권, 장면과 장면 사이 이동 이유가 약하면 경고한다.

### `tone-guard-hook`
- 중2병 서사, 허세형 운명론, 과장된 파멸 미학을 경고한다.

### `serial-retention-hook`
- 화 끝 압박, 잔여 질문, 다음 화 당김이 부족할 때 경고한다.

## 5. Smoke 훅

### `marker-hook`
- 핵심 지도, 복선 장부, 엔딩 수렴 문서 누락을 경고한다.

### `link-integrity-hook`
- 깨진 링크, 없는 문서, 인덱스 미동기화를 경고한다.

### `banned-surface-hook`
- 금지 표면어, 구형 캐논어, 과한 혈색 수사를 경고한다.

### `volume-structure-hook`
- 권별 outline/timeline 쌍, 25화 구조, 핵심 제작 제약 누락을 경고한다.

## 6. 운영 원칙

- 훅은 `경보와 게이트`다.
- 훅은 캐논을 직접 수정하지 않는다.
- 훅은 자동으로 pass를 시작할 수는 있어도 병합 승인을 대신하지 않는다.
- 훅 결과의 최종 해석은 총괄이 맡는다.
