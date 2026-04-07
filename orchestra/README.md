# 오케스트라 개요

이 폴더는 저장소 로컬 소설 오케스트라의 운영 중심이다.

## 여기 있는 것

- `SOURCE_OF_TRUTH.md`: 문서 우선순위 기준
- `WORKFLOW.md`: lane 순서와 병합 규율
- `HANDOFF_PACKET_PLAYBOOK.md`: 반복 작업용 패킷 시작점
- `LORE_AUDIT_HARNESS.md`: 설정집 감사 하네스
- `FORESHADOW_HARNESS.md`: 복선/회수 감사 하네스
- `STORYCRAFT_HARNESS.md`: 구조/감정선/리텐션 설계 하네스
- `SMOKE_AUDIT_HARNESS.md`: 빠른 자동 정합성 게이트
- `ENGINE_DATA_LAYER_POLICY.md`: JSON/엔진 데이터층 운영 기준
- `../lore_bible/Relationship_Map.md`: 핵심 관계 손상 문법
- `../lore_bible/Supporting_Cast_Witness_Map.md`: 측면 인물 목격 문법
- `../lore_bible/Front_Half_Foreshadow_Map.md`: 전반부 복선 의무 지도
- `../lore_bible/Ending_Convergence_Map.md`: 후반 엔딩 수렴 지도
- `SESSION_STATE.md`: 현재 작업 상태
- `ORCHESTRA_PORTABILITY_AUDIT_2026-04-07.md`: 재사용 경계 감사
- `CORE_LAYER_MAP.md`: 코어 / 프로젝트 설정 / 캐논 레이어 구분
- `ORCHESTRA_EXECUTION_PLAN_2026-04-07.md`: 총괄 실행 계획
- `BRANCH_CHECKPOINT_POLICY.md`: 브랜치/커밋/푸시 규칙
- `modules/novel-orchestra-core/README.md`: 명명된 재사용 코어 모듈 안내
- `templates/`: 패킷, 핸드오프, 리포트 템플릿
- `scripts/`: 보조 스크립트와 패킷 빌더
- `runs/`: 실행 때마다 생기는 산출물

활성 보조 도구는 가능하면 `orchestra/scripts`나 `backend/` 아래에 두고, 루트의 일회성 유틸은 계속 비워 두는 편이 진입점을 깨끗하게 유지한다.

## 사용 원칙

- 먼저 총괄자부터 태운다. 총괄자가 필요한 전문가만 고르고 packet을 만든다.
- 모든 lane을 다 돌리지 않는다. 현재 병목을 풀 lane만 태운다.
- 반복 작업은 매번 새로 쓰지 말고 `HANDOFF_PACKET_PLAYBOOK.md`와 해당 템플릿부터 쓴다.
- smoke audit는 빠른 구조 게이트이지, 소설가 판단을 대신하는 것은 아니다.
- 인간적 대가, 진실 공개, 엔딩 수렴이 걸린 작업은 흩어진 문서를 다시 조립하지 말고 관련 지도 문서부터 읽는다.

## 재사용과 계획

- 다른 소설에 이식할 때는 `ORCHESTRA_PORTABILITY_AUDIT_2026-04-07.md` -> `CORE_LAYER_MAP.md` -> `templates/` 순으로 읽는다.
- 이름이 붙은 재사용 경계는 `modules/novel-orchestra-core/`다.
- 계획형 운영은 `ORCHESTRA_EXECUTION_PLAN_2026-04-07.md`와 `BRANCH_CHECKPOINT_POLICY.md`를 기준으로 잡는다.

## 3대 하네스

### Lore Audit

세계관, 인물, 세력, 장소, 타임라인 정합성을 다룰 때 쓴다.

### Foreshadow Audit

복선 공정성, 레드헤링, 회수 부채를 다룰 때 쓴다.

### Storycraft

구조, 진실 공개 순서, 감정선, 회차 리텐션 같은 소설가 측 설계를 다룰 때 쓴다.
