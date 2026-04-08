# rttp-engine

`rttp-engine`는 《나는 과거로 간다》 전용 소설 제작 엔진 모듈이다.

이 모듈은 재사용 코어인 `novel-orchestra-core` 위에 올라가는
`프로젝트 전용 작문/운영 엔진층`이다.

## 목적

- 이 작품의 시간여행 패러독스 문법을 잠근다.
- 대가, 감정 손실, 복선, 리빌, 리텐션을 한 시스템으로 묶는다.
- 총괄 오케스트라가 어떤 전문가를 언제 어떤 모델로 고용할지 기준을 준다.

## 핵심 문서

- `orchestra/RTTP_ENGINE.md`
- `orchestra/RTTP_ENGINE_AGENT_ROSTER.md`
- `orchestra/RTTP_ENGINE_EXECUTION_PROTOCOL.md`
- `orchestra/CONDUCTOR_AUTHORITY_LOCK.md`
- `orchestra/MCP_SKILLS_AGENTS_HOOKS_HARNESS_MAP.md`
- `orchestra/HARNESS_RUNTIME_RULES.md`
- `orchestra/SETTING_FIRST_MODE.md`
- `orchestra/SOURCE_OF_TRUTH.md`
- `orchestra/ORCHESTRA_EXECUTION_PLAN_2026-04-07.md`

## 포함되는 것

- RTTP 전용 작문 알고리즘 묶음
- RTTP 전용 전문가 에이전트 체계
- RTTP 전용 모델/추론 선택 기준
- 설정 우선 -> 집필 전환 규칙
- 총괄 편집권 잠금
- 도구/에이전트/훅/하네스 역할 분리 규약

## 포함되지 않는 것

- 재사용 코어 자체
- 다른 소설에도 공통으로 쓰는 하네스 원본
- 작품 개별 lore/outline 본문

## 관계

- 아래층: `novel-orchestra-core`
- 현재층: `rttp-engine`
- 위층: `lore_bible/**`, `outline/**`, `Guidelines/**`
