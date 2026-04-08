# novel-orchestra-core

`novel-orchestra-core`는 이 저장소의 소설 오케스트라에서
작품 고유 캐논을 걷어내도 남는 `재사용 코어`를 묶어 부르는 모듈 이름이다.

## 모듈 목적

- 총괄 오케스트라 운영 절차를 재사용한다.
- 전문가 lane 분기와 packet contract를 재사용한다.
- lore / foreshadow / storycraft / smoke audit 하네스 구조를 재사용한다.
- 총괄 권한 잠금과 하네스 런타임 규칙을 재사용한다.
- 다른 소설에 붙일 때는 이 모듈을 먼저 가져오고, 그 위에 프로젝트 설정층을 덧씌운다.

## 포함 범위

- `orchestra/WORKFLOW.md`
- `orchestra/HANDOFF_PACKET_PLAYBOOK.md`
- `orchestra/LORE_AUDIT_HARNESS.md`
- `orchestra/FORESHADOW_HARNESS.md`
- `orchestra/STORYCRAFT_HARNESS.md`
- `orchestra/SMOKE_AUDIT_HARNESS.md`
- `orchestra/CONDUCTOR_AUTHORITY_LOCK.md`
- `orchestra/MCP_SKILLS_AGENTS_HOOKS_HARNESS_MAP.md`
- `orchestra/HARNESS_RUNTIME_RULES.md`
- `orchestra/templates/WORK_PACKET.md`
- `orchestra/templates/HANDOFF_*.md`
- `orchestra/templates/REVISION_LEDGER.md`
- `orchestra/templates/NOVEL_ORCHESTRA_BOOTSTRAP_CHECKLIST.md`
- `orchestra/templates/PROJECT_PROFILE_TEMPLATE.md`
- `orchestra/templates/SOURCE_OF_TRUTH_TEMPLATE.md`
- `orchestra/templates/SETTING_AUDIT_RULES_TEMPLATE.json`
- `orchestra/CORE_LAYER_MAP.md`

## 포함하지 않는 것

- 작품 전용 캐논
- 작품 전용 Source of Truth
- 작품 전용 금지어와 자동감사 규칙
- 작품 전용 인물, 세력, 장소, 복선, 엔딩

## 사용 순서

1. `novel-orchestra-core`를 복사한다.
2. 새 작품의 프로젝트 설정층을 만든다.
3. 새 작품 캐논을 채운다.
4. 새 작품 전용 감사 규칙을 붙인다.

## 우선 참조 문서

- `../../ORCHESTRA_PORTABILITY_AUDIT_2026-04-07.md`
- `../../CORE_LAYER_MAP.md`
