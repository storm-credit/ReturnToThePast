# 오케스트라 코어 레이어 맵

이 문서는 이 저장소의 오케스트라를
`재사용 코어`, `프로젝트 엔진`, `프로젝트 설정`, `작품 캐논`으로 나눠 보는 기준표다.

## 1. 재사용 코어

다른 소설로 옮길 때 가능한 한 그대로 유지하는 층이다.

### 포함 문서

- `WORKFLOW.md`
- `HANDOFF_PACKET_PLAYBOOK.md`
- `LORE_AUDIT_HARNESS.md`
- `FORESHADOW_HARNESS.md`
- `STORYCRAFT_HARNESS.md`
- `SMOKE_AUDIT_HARNESS.md`
- `templates/WORK_PACKET.md`
- `templates/HANDOFF_LORE_REPAIR.md`
- `templates/HANDOFF_FORESHADOW_REPAIR.md`
- `templates/HANDOFF_BRIDGE_REINFORCEMENT.md`
- `templates/REVISION_LEDGER.md`

### 유지 원칙

- 역할 분기 방식은 유지한다.
- 패킷 구조는 유지한다.
- 감사 리포트 형식은 유지한다.
- 특정 작품의 인물명, 세력명, 장르 규칙은 넣지 않는다.

## 2. 프로젝트 엔진층

재사용 코어 위에 올라가는 작품 전용 작문/운영 엔진층이다.

### 포함 문서

- `RTTP_ENGINE.md`
- `RTTP_ENGINE_AGENT_ROSTER.md`
- `RTTP_ENGINE_EXECUTION_PROTOCOL.md`
- `modules/rttp-engine/README.md`
- `modules/rttp-engine/module-manifest.json`

### 여기서 잠그는 것

- 작품 전용 작문 알고리즘 묶음
- 작품 전용 전문가 구성
- 작품 전용 모델/추론 선택 원칙
- 총괄자의 실행 알림 방식

## 3. 프로젝트 설정층

작품마다 새로 갈아끼우는 층이다.

### 포함 문서

- `SOURCE_OF_TRUTH.md`
- `SETTING_FIRST_MODE.md`
- `templates/PROJECT_PROFILE_TEMPLATE.md`로 만든 프로젝트 프로필
- `templates/SOURCE_OF_TRUTH_TEMPLATE.md`로 만든 우선순위 문서
- 프로젝트 전용 감사 규칙 파일

### 여기서 잠그는 것

- 장르 프레임
- 권수 / 화수 / 분량 규칙
- 금지어
- 이름 계통 규칙
- 필수 지도와 장부 종류
- 어떤 실수를 자동감사로 잡을지

## 4. 작품 캐논층

실제 소설 내용이 들어가는 층이다.

### 포함 문서

- `lore_bible/**`
- `outline/**`
- `Guidelines/**`
- 필요 시 `Drafts/**`

### 여기서 잠그는 것

- 인물
- 세력
- 장소
- 법칙
- 복선
- 엔딩
- 권별 구조

## 5. 분리 순서

1. 재사용 코어를 먼저 복사한다.
2. 프로젝트 엔진층을 작품 전용으로 다시 쓴다.
3. 프로젝트 설정층 문서를 새 작품 기준으로 다시 쓴다.
4. 그 다음 작품 캐논을 채운다.
5. 마지막으로 프로젝트 전용 감사 규칙을 붙인다.

## 6. 가장 중요한 원칙

- 코어 문서에 특정 작품의 이름을 넣지 않는다.
- 엔진층에는 작품의 작문법과 운용법만 넣고, 실제 lore는 넣지 않는다.
- 프로젝트 설정층에 작품 규칙을 몰아넣는다.
- 작품 캐논은 lore/outline/guidelines 쪽에만 쌓는다.
- 코어와 캐논이 섞이기 시작하면, 다음 작품으로 옮길 때 다시 무거워진다.
