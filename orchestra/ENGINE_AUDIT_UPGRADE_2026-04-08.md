# 엔진 점검 및 업그레이드 - 2026-04-08

## 목적

RTTP 엔진과 오케스트라 코어에서 `총괄 권한`, `MCP/스킬/에이전트/훅 역할 분리`, `하네스 런타임 규칙`이 충분히 잠겨 있는지 점검하고 부족한 층을 보강한다.

## 확인된 부족점

- 총괄 편집권이 여러 문서에 암묵적으로만 존재했다.
- MCP, 스킬, 에이전트, 훅, 하네스가 무엇을 하고 무엇을 하지 않는지 한 장으로 잠긴 문서가 없었다.
- 하네스 PASS가 곧 승인처럼 읽힐 여지가 있었다.
- 훅과 자동 실행이 어디까지 할 수 있는지 명시적 금지선이 약했다.

## 이번 업그레이드

- `CONDUCTOR_AUTHORITY_LOCK.md` 추가
- `MCP_SKILLS_AGENTS_HOOKS_HARNESS_MAP.md` 추가
- `HARNESS_RUNTIME_RULES.md` 추가
- `RTTP_ENGINE.md`에 총괄 권한/역할 분리 문단 추가
- `RTTP_ENGINE_EXECUTION_PROTOCOL.md`에 권한 분리 규칙 추가
- `RTTP_ENGINE_AGENT_ROSTER.md`에 역할 경계 추가
- `WORKFLOW.md`에 merge authority와 하네스 해석 규칙 추가
- `rttp-engine`와 `novel-orchestra-core` 모듈 README에 잠금 문서 연결

## 현재 판정

- 총괄 권한: 명시적 잠금 완료
- 역할 분리: 명시적 잠금 완료
- 하네스 런타임 규칙: 명시적 잠금 완료
- 남은 일: 운영 중 실제 패스에서 이 규칙을 계속 지키는 것
