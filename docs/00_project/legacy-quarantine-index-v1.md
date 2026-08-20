# Legacy Quarantine Index v1

Status: **ACTIVE ROUTING / NON-CANON SAFETY INDEX**  
Owner: A00 Story Orchestrator / A02 Canon / A13 Continuity / A17 GitHub State / A21 Context Pack  
Effective: 2026-08-20  
Base Audit: `main@9b0edee394455726d2270ac0dae58d2919cf2731`

## 1. Purpose

이 문서는 과거 설계자료를 삭제하지 않으면서, 현재 정본·설계·집필에 잘못 유입되는 것을 막는다.

핵심 원칙:

> **Legacy는 provenance와 salvage를 위한 역사자료이지, 현재 Canon·State·Architecture의 근거가 아니다.**

Git 검색에서 오래된 파일이 먼저 발견되더라도 현재 정본으로 승격하지 않는다.

## 2. Current Startup Sources

새 세션과 에이전트는 다음 순서로 현재 상태를 읽는다.

1. `AI_PROJECT.md`
2. `docs/00_project/canon-constitution-v1.md`
3. 최신 Amendment / Errata / `docs/00_project/decision-log.md`
4. `docs/00_project/GATE_STATUS.md`
5. `manuscript/PROGRESS.md`
6. `docs/00_project/PROJECT_COMPLETION_SCORECARD_20260820.md`
7. 관련 Domain Bible
8. 관련 Story Architecture
9. 관련 Context Pack / Craft Manifest / Harness

## 3. Quarantined Root Files

다음 파일은 현재 정본·현재 상태·현재 엔딩의 근거로 사용하지 않는다.

- `00_CANON.md` — 이미 DEPRECATED 표시된 구 회귀 Canon
- `Ending_Scenarios.md` — 구 172회차/환생/관찰자 엔딩 자료; 현재 워킹트리는 deprecation wrapper로 교체
- `Lore_Bible_Master_Index.md` — 구 《나는 과거로 간다》 회귀·코스믹호러 설정집 인덱스; deprecation wrapper로 교체
- `Lore_Production_Roadmap.md` — 구 172회귀 세계관 구축 완료표; deprecation wrapper로 교체
- `02_SESSION_SUMMARY.md` — 비어 있던 구 세션 인계 방식; 현재 라우팅 wrapper로 교체
- `01_WORKING_NOTES.md` — 아이디어 메모 전용, Canon 아님

현재 엔딩은 반드시 다음을 따른다.

- `docs/10_story_architecture/series-promise-and-ending-v1.md`
- `docs/12_losses/permanent-loss-lock-v1.md`
- D11–D15 최신 Amendment / system / ending-operation 문서

## 4. Quarantined Directories / Legacy Trees

### `outline/`
구 회귀/타임루프 로드맵과 권별 타임라인이 다수 남아 있다. **REFERENCE ONLY**.

### `Drafts/`
구 회귀 Canon을 전제로 한 원고·초안이 남아 있다. **REFERENCE ONLY**.

### Legacy-era `lore_bible/`, `characters/`, `settings/`, `history/`, `style/`
구 `Lore_Production_Roadmap.md`가 참조하던 자산군이다. 현재 `docs/` Domain Bible과 `manuscript/` 체계보다 우선하지 않는다. 존재하는 파일을 읽을 경우 **REFERENCE ONLY**로 취급한다.

### `Guidelines/`
레거시 시대의 작성 가이드가 포함되어 있다. 현재 작업에서는 `.agent/skills/`와 `docs/13_writing_harness/`를 우선한다. 활성 라우터가 특정 `Guidelines/` 파일을 명시적으로 가리킬 때만 보조자료로 읽는다.

## 5. Forbidden Legacy Imports

아래 요소는 현재 정본으로 자동 가져오지 않는다.

- 172회차·무한 회귀·죽음 리셋
- 현대 대학생으로 환생하는 정사 엔딩
- 에이든이 신/영원한 시간관리자가 되는 엔딩
- 0회차 에이든을 최종 흑막으로 쓰는 구조
- 발타자르를 C05 정식 인물명 또는 최종 흑막으로 사용
- 12사도·창백한 의회·영시 등 구 조직을 현 정본 조직으로 자동 치환
- 세라핌 수도·구 회귀 설정의 장소명을 현 정본 지명으로 자동 사용
- 구 `F1 지휘관`, `F1 친구 슬롯`, `[WORKING]` 인물명을 정식명보다 우선

정식 인물명은 `docs/05_characters/cast-canon-index-v2.md`가 우선한다.

## 6. Active-but-Older Alias Documents

다음 D8-era 문서는 역할·인과 정보가 유용하지만 일부 이름이 `슬롯`/`WORKING` 상태로 남아 있을 수 있다.

- `docs/05_characters/cast-encyclopedia-v1.md`
- `docs/05_characters/character-faction-institution-bible-v1.md`

이 두 문서는 **폐기하지 않는다.** 다만 이름·첫/마지막 핵심권·최종상태가 `cast-canon-index-v2.md`와 다르면 Canon Index가 무조건 우선한다.

`core-character-arc-map-v1.md`의 주요 stale 명칭은 이번 감사에서 정식 이름으로 직접 교정했다.

## 7. Salvage Rule

Legacy에서 사건·문장·아이디어를 재사용하려면 다음을 모두 통과해야 한다.

1. 현재 Canon Constitution과 충돌 없음
2. 최신 Domain Bible과 충돌 없음
3. 최신 Story Architecture의 사건·선택·손실을 바꾸지 않음
4. 현재 인물 ID·이름·시대·POV와 정합
5. 시간여행 규칙을 새로 만들지 않음
6. 필요한 경우 Context Pack에 `Legacy provenance`를 명시
7. S0/S1 Red Team PASS

Legacy 문서에 `정사`, `Final`, `절대 기준`, `COMPLETE`라고 적혀 있어도 현재 권한을 갖지 않는다.

## 8. Search Safety

GitHub 검색 결과에 Legacy와 Active 문서가 함께 나오면:

- 파일 경로와 Status를 먼저 본다.
- `outline/`, `Drafts/`, §3·§4의 Legacy 자산은 정답 후보에서 제외한다.
- `[WORKING]`, `슬롯`, `후보`, `ASSUMPTION`은 최신 Canon Index와 대조한다.
- 상태/진행률은 `GATE_STATUS.md`와 `manuscript/PROGRESS.md` 이외의 오래된 하드코딩 수치를 신뢰하지 않는다.
- Grand Act READ-ONLY HUB에 남은 과거 production 숫자는 Architecture truth가 아니며 현재 상태장부가 우선한다.

## 9. Current Production Boundary

이 인덱스 작성 시점의 실제 설계 기준:

- Global Deep Design: COMPLETE / FROZEN
- 5 Grand Acts / 15 Volumes / 30 Arcs / 60 Subacts / E001–E375 D6: COMPLETE
- protagonist quantitative regression: PASS
- main manuscript boundary: E001–E088
- E089–E093 current Context Pack / Craft / Preflight: COMPLETE
- next prose unit after this cleanup: **E089, 리아 세른 P1**
- HUMAN PROSE PASS: AUTHOR ONLY

정확한 GitHub SHA와 최신 작업상태는 작업 시점에 다시 검증한다.
