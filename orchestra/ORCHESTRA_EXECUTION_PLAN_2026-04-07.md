# Orchestra Execution Plan — 2026-04-07

## 목표

- 설정집을 계획적으로 마감한다.
- 오케스트라 코어와 프로젝트 설정층을 안정화한다.
- `SETTING-FIRST`를 무너뜨리지 않으면서 초안 투입 전 준비를 끝낸다.

## 총괄 원칙

- 총괄자는 언제나 `novel-orchestra-conductor`다.
- 모든 작업은 `한 번에 다`가 아니라 `도메인별 self-contained pass`로 끊는다.
- 각 pass는 `문서 반영 -> 스모크 감사 PASS -> 감사 메모 갱신 -> 커밋` 순서를 따른다.
- drafting lane은 `setting-first exit gate`를 통과하기 전까지 잠근다.

## Phase 1. 설정집 마감 정리

### 목표

- 설정집의 남은 optional polish를 끝내고, `구조적 공백 없음` 상태를 만든다.

### 투입 lane

- `novel-orchestra-conductor`
- `world-rule-keeper`
- `character-architect`
- `faction-strategist`
- `location-cartographer`
- `timeline-historian`
- `plausibility-warden`

### 현재 우선 작업

1. 엔진/JSON 표면 정리 여부 결정
2. 오케스트라 메타 문서 한국어 표면 정리
3. 이름 계통과 장소 어근 최종 점검

### 완료 기준

- `SETTING_PRIORITY_QUEUE_2026-04-07.md`의 optional polish가 더는 구조 리스크가 아니라고 판정됨
- 최신 스모크 감사가 PASS
- 새 이름/새 규칙이 진입 문서와 인덱스에 반영됨

## Phase 2. 드래프트 투입 준비

### 목표

- 설정집을 쓰기 위한 운영 문서와 패킷을 준비한다.

### 투입 lane

- `novel-orchestra-conductor`
- `structure-architect`
- `arc-psychologist`
- `foreshadow-bookkeeper`
- `serial-tension-engineer`

### 산출물

- 제1권용 handoff packet
- 제1권 핵심 장면 압력표
- 복선/회수 장부와 권별 연결 확인
- setting-first exit gate 판정 메모

### 완료 기준

- 제1권 초안에 들어가도 될 최소 패킷이 준비됨
- 구조, 감정선, 복선선이 같은 packet 안에서 읽힘

## Phase 3. setting-first exit gate

### 열기 전 확인

- `00_CANON`
- `Start_Here`
- `Series_Roadmap`
- `SOURCE_OF_TRUTH`
- 최신 smoke PASS
- 제1권 packet ready

### gate 통과 후 개방 lane

- `scene-smith`
- `hook-doctor`
- `chapter-inspector`

### gate 통과 후에도 유지할 것

- 설정 보강은 계속 conductor 승인하에만 병합
- 초안 수정보다 canon repair가 우선인 상황이면 drafting lane을 다시 멈춤

## Phase 4. 반복 운영

### pass 단위 반복

1. 목표 도메인 잠금
2. 필요한 specialist만 호출
3. 결과 병합
4. smoke PASS
5. 체크포인트 커밋

### 주간 반복

- 중간 체크포인트에서 integration branch 업데이트
- 주간 마감 체크포인트에서 summary + push
- 다음 주 시작 전에 queue 재정렬
