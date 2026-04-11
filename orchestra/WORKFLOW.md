# 오케스트라 워크플로

이 문서는 저장소 로컬 소설 오케스트라가 어떻게 움직여야 하는지 설명한다.

## 목표

- 캐논 보수, 스토리크래프트 설계, 이후 초안, 감사 작업을 분리한다.
- 전문가들은 좁은 문제를 맡고, 총괄자는 병합 순서와 최종 판단을 맡는다.
- 현재 병목을 푸는 lane만 사용한다.
- `SETTING_FIRST_MODE.md`가 켜져 있는 동안엔 drafting lane을 기본적으로 잠근다.

## 핵심 문서

- `SESSION_STATE.md`: 현재 작업 상태와 타깃
- `WORKFLOW.md`: 운영 규칙과 lane 순서
- `SETTING_FIRST_MODE.md`: 아직 설정집 우선 모드임을 선언하는 문서
- `SOURCE_OF_TRUTH.md`: 문서 우선순위와 no-touch 기준
- `Guidelines/Setting_Audit_Scope.md`: 설정집 감사 표면 지도
- `HANDOFF_PACKET_PLAYBOOK.md`: 반복 작업용 빠른 packet 시작점
- `LORE_AUDIT_HARNESS.md`: 전 도메인 설정 감사 흐름
- `FORESHADOW_HARNESS.md`: 복선/회수 감사 흐름
- `STORYCRAFT_HARNESS.md`: 구조, 진실 공개, 감정선, 리텐션 설계 흐름
- `lore_bible/Mid_War_Emotional_Continuity.md`: 제4권~제8권 감정 연속성 캐논
- `lore_bible/history/Fixed_Point_Pressure_Map.md`: 고정점, 분기점, 패러독스 압력 문법
- `templates/WORK_PACKET.md`: 총괄 dispatch 포맷
- `templates/AGENT_REPORT.md`: 전문가 결과 보고 포맷
- `templates/REVISION_LEDGER.md`: 병합된 수정 기록
- `EXECUTION_PROGRESS_LEDGER.md`: `진행` 요청과 pass별 사용층/다음 큐 기록
- `scripts/Build-LoreAuditPackets.ps1`: lore audit packet 빌더

## 운영 규칙

1. 장기 작업의 목표나 범위가 바뀌면 `SESSION_STATE.md`를 갱신한다.
2. 총괄자는 먼저 진실 문서를 읽고 work packet을 만든다.
3. 반복 작업은 자유형 packet보다 handoff template이나 preset을 우선한다.
4. 전문가들은 packet과 required reads 기준으로만 움직인다.
5. 전문가들은 파일 수정 전에 구조화된 findings를 먼저 돌려준다.
6. 총괄자는 서로 양립 가능한 수정만 캐논 파일에 병합한다.
7. 사용자가 `진행` 또는 `계속`을 요청하면, 총괄은 pass 종료 전 `EXECUTION_PROGRESS_LEDGER.md`에 실제 사용한 총괄/전문가/MCP/스킬/훅/하네스와 다음 큐를 남긴다.

추가 잠금:
- 총괄의 위임 경계는 `CONDUCTOR_AUTHORITY_LOCK.md`를 따른다.
- MCP / 스킬 / 에이전트 / 훅 / 하네스의 계층 분리는 `MCP_SKILLS_AGENTS_HOOKS_HARNESS_MAP.md`를 따른다.
- pass 런타임과 실패 시 재진입은 `HARNESS_RUNTIME_RULES.md`를 따른다.

- 총괄만 lane을 연다.
- 총괄만 병합 순서를 바꾼다.
- 총괄만 캐논 반영 여부를 결정한다.
- 훅은 pass를 시작할 수는 있어도 merge authority를 갖지 않는다.
- 하네스는 경보와 게이트를 담당하고, 최종 해석은 총괄이 맡는다.

관련 문서:

- `CONDUCTOR_AUTHORITY_LOCK.md`
- `MCP_SKILLS_AGENTS_HOOKS_HARNESS_MAP.md`
- `HARNESS_RUNTIME_RULES.md`

## lane 패턴

### 캐논 구축 또는 보수

1. `novel-orchestra-conductor`
2. `lore-forgemaster`
3. `chrono-weaver`
4. `plausibility-warden`
5. 결과가 prose에 바로 닿으면 `chapter-inspector`

### 설정집 감사

1. `novel-orchestra-conductor`
2. 필요한 도메인 전문가
3. `chrono-weaver`
4. 감정 연속성이 병목이면 `arc-psychologist`
5. 실제 수리 패치가 필요하면 `lore-forgemaster`
6. `plausibility-warden`

고정점/분기점/패러독스 압력 작업은 아래 순서를 우선한다.

1. `novel-orchestra-conductor`
2. `chrono-weaver`
3. `world-rule-keeper`
4. `plausibility-warden`

세부 lane이 필요한 경우:

- `relic-curator`
- `monster-ecologist`
- `systems-chancellor`

### 스토리크래프트 설계

1. `novel-orchestra-conductor`
2. 뼈대나 엔딩 역산이 흔들리면 `structure-architect`
3. 감정선이 얇으면 `arc-psychologist`
4. 진실 공개 순서가 약하면 `reveal-choreographer`
5. 복선 장부가 비면 `foreshadow-bookkeeper`
6. 회차 압력이 약하면 `serial-tension-engineer`
7. `plausibility-warden`
8. `scene-smith`는 setting-first 해제 뒤에만
9. `chapter-inspector`도 setting-first 해제 뒤에만

### 복선 / 회수 감사

1. `novel-orchestra-conductor`
2. `foreshadow-bookkeeper`
3. `timeline-historian`
4. 규칙 의존 리빌이면 `world-rule-keeper`
5. `plausibility-warden`

총괄자 메모:

- 리빌이 시리즈 전체 의미를 바꾸면 복선 장부와 전반부 복선 지도를 함께 잠근다.
- 회수가 같은 권에서 처음 나온 단서에 기대면 under-seeded로 본다.

### 설정집 이후 초안/재작성

이 lane은 총괄자가 `setting-first mode`를 해제하기 전까지 비활성이다.

## packet 잠금 항목

모든 packet은 아래를 잠가야 한다.

- `Mission`
- `Lane`
- `Target`
- `State Snapshot`
- `Required Reads`
- `Locked Facts`
- `Editable Targets`
- `No-Touch Files`
- `Deliverable`
- `Blocking Decisions`
- `Stop Conditions`

## 금지 패턴

- 캐논 병목이 풀리기 전에 초안부터 쓰기
- setting-first 모드가 켜진 채 drafting lane 열기
- lore 발명과 prose 수정을 한 패스에 뒤섞기
- 좁게 풀 수 있는 문제를 여러 lane이 같은 파일에 동시에 건드리게 하기
- 설정집 작업을 outline/timeline 유지보수로만 오해하기
- 약한 구조를 반전 에너지나 고어 수사로 덮기
- merge step 없이 전문가 제안을 캐논에 바로 덮어쓰기
