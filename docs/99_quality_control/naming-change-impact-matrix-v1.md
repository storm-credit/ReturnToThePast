# 개명 영향표 v1

Status: AUDIT ARTIFACT — NO CANON CHANGE
Branch: `agent/naming-system-full-audit-v1`
Base: `main` @ `06ef0b7c97cfeabdbb5e92dece12c11dce18886d`
Depends On: [`naming-full-audit-v1.md`](naming-full-audit-v1.md)

## 0. 측정 방법

- 대상: 저장소 전체 `*.md` (`.git` 제외)
- 이번 감사에서 새로 만든 4개 문서(`naming-inventory-v1`, `naming-source-evidence-matrix-v1`, `naming-full-audit-v1`, `cultural-naming-phonology-v1`)는 **제외**하고 집계했다
- 측정 시점: `main` @ `06ef0b7`
- `files`: 해당 문자열이 등장하는 파일 수 / `hits`: 총 출현 행 수

집계는 단순 문자열 검색이다. 실제 치환 시에는 부분일치(`잔문` ⊂ `잔문감사실`)를 분리해야 한다.

---

## 1. 기관층 — 개명 후보가 제시된 대상

| 대상 | files | hits | 원고 영향 | 위험 | 비고 |
|---|---:|---:|---|---|---|
| **연대출귀원** | 9 | 16 | E001 | 낮음 | 기능 HARD LOCK은 institution §6이 보유. 표층 명칭만 이동 |
| **성력국** | 6 | 16 | E001 | 낮음 | Domain Bible 원문 `달력국`으로 회귀. 단 E001 L101 권한 서술 정정 동반 필요 |
| **중앙관측탑(연합)** | 8 | 10 | E001 | 낮음 | `마탑`은 명명규칙 §2.4 허용어이며 institution §4가 사용 조건 충족 |
| **지역 연대감사소** | 3 | 5 | 없음 | 매우 낮음 | 결말부 기관. 원고 미등장 |

**소계: 4개 대상 / 26개 파일 / 47행 / 원고 1편(E001)**

---

## 2. 기관층 — 설정 확인 필요로 중단한 대상

후보를 제시하지 않았으므로 영향 계산은 참고용이다.

| 대상 | files | hits | 중단 사유 |
|---|---:|---:|---|
| 최후 연대국 | 13 | 19 | 조직 구조 Domain Bible 부재 |
| 왕좌승인원 | 8 | 10 | `세르바 왕실평의회`와의 포함관계 미확정 |
| 잔문감사실 | 4 | 5 | `잔문` ↔ `팔림프세스트` 표기 구분 미확정 |
| 연대개입산업연합 | 4 | 4 | crosswalk V10 한 줄 외 근거 없음 |
| 방위지휘부 | 3 | 8 | 원고 전용. 정본 미등재 |
| 선별실 | 3 | 5 | 원고 전용. 정본 미등재 |
| 고정환 관리연합 | 2 | 2 | 지리명/조직명 분리 여부 선결 |

### 부분일치 주의

| 문자열 | files | hits | 문제 |
|---|---:|---:|---|
| 잔문 | 18 | 28 | `잔문감사실`(5행)과 설정어 `잔문`(23행)이 섞여 있다 |
| 팔림프세스트 | 17 | 22 | `잔문`과 동의어 병존. 어느 쪽을 원고 표층으로 쓸지 미확정 |

**→ `잔문감사실` 치환 시 설정어 `잔문`을 함께 건드리지 않도록 정규식 경계 필요.**

---

## 3. 용어층

| 대상 | files | hits | 위험 | 판정 |
|---|---:|---:|---|---|
| **무명종** | **52** | **96** | **매우 높음** | 개명 검토 최우선이나 **저장소 최대 참조 항목** |
| **역사주소** | **43** | **76** | **높음** | 설정어 유지 + 원고 노출 최소화 (개명 아님) |
| 주소상실 | 19 | 25 | 중간 | 위와 동일 |
| 연대유산 | 13 | 16 | 중간 | `연대` 접두어 계열 일괄 재설계에 포함 |
| 구흔교리 | 3 | 5 | 낮음 | **이름 불필요** 판정. 가장 저렴한 정리 대상 |

### 판단

`무명종`은 이름이 설정을 오독시키는 유일한 사례(`-종`이 생물종을 연상시키나 실제로는 주소 탈락 상태)지만, 동시에 **저장소 전체에서 가장 많이 참조되는 명칭**이다. 개명 이득과 치환 비용이 정면으로 부딪친다.

**대안**: 총칭 `무명종`을 설계문서 전용으로 유지하고, **원고 표층에서만** `기록에서 이름이 사라진 사람들`로 풀어 쓴다. 이 방식은 96행 치환 없이 독자 오독을 제거한다. 명명규칙 §4.8과 E001 L437 선례가 이 방향을 지지한다.

---

## 4. 음운 충돌 해소 — 변경 비용 순

| 대상 | files | hits | 비용 | 비고 |
|---|---:|---:|---|---|
| **세르나** (관문도시) | **1** | **1** | **최저** | `[WORKING]` 미등재. atlas R01 한 줄뿐 |
| **카센 언덕** | 2 | 2 | 매우 낮음 | 작업명 `절검의 언덕` 승격이면 추가 창작 불필요 |
| 마레이 | 6 | 9 | 낮음 | 남부 `마레-` 충돌 |
| 마레사 | 9 | 14 | 낮음 | 남부 `마레-` 충돌 |
| **네르바** (권역) | 9 | 18 | 중간 | 아이리스 네르의 어원. constitution HARD LOCK 인물 연쇄 |
| **네바르** (종족) | **37** | **55** | **높음** | 종족 P05. 장례어·장례법정·검시단 연쇄 |

### 판단

`네르바 ↔ 네바르` 충돌은 **권역 쪽 변경이 비용 1/3**이다(18행 vs 55행). 다만 `네르`(아이리스·엘사)가 권역명에서 파생된 이름이므로 인물명 어원 설명이 함께 바뀐다. 어느 쪽이든 작가 결정 사항이며 감사자가 선택하지 않는다.

`세르나`는 **1파일 1행**이다. 세/셀 클러스터 9개 중 유일하게 사실상 무비용으로 해소 가능한 항목이다.

---

## 5. 원고 영향

| 파일 | 관련 명칭 출현 |
|---|---:|
| [`manuscript/volume-01/E001-마지막-도시의-다른-날짜.md`](../../manuscript/volume-01/E001-마지막-도시의-다른-날짜.md) | 11 |
| [`manuscript/volume-01/E002-여섯-개의-승인.md`](../../manuscript/volume-01/E002-여섯-개의-승인.md) | 1 |
| [`manuscript/quality/E001-read-aloud-reaudit.md`](../../manuscript/quality/E001-read-aloud-reaudit.md) | 1 |
| [`manuscript/quality/E002-quality-report.md`](../../manuscript/quality/E002-quality-report.md) | 1 |
| [`manuscript/state/E002-state-mutation.md`](../../manuscript/state/E002-state-mutation.md) | 2 |

**원고는 2편뿐이다.** 375화 설계 중 0.5% 지점이므로 개명 실행 시점으로는 최적이다.

E001에는 §1 대상 명칭 외에 현대 외래어 6건(`스피커`·`시스템`·`단말`·`브리핑실`·`조작판`·`화면`)이 별도로 존재한다 — [`naming-full-audit-v1.md`](naming-full-audit-v1.md) §5.1.

---

## 6. 개명 실행 시 동반 갱신 대상

명명규칙 §6 `정본 개명 정족수`가 요구하는 일괄 갱신 범위다.

| 계층 | 파일 |
|---|---|
| 정본 | [`docs/00_project/canon-naming-pack-v1.md`](../00_project/canon-naming-pack-v1.md) §6·§7 |
| Amendment 판정 | [`docs/00_project/decision-log.md`](../00_project/decision-log.md) (DEC-009 갱신 여부) |
| Domain Bible | [`docs/08_institutions/institution-org-procedure-bible-v1.md`](../08_institutions/institution-org-procedure-bible-v1.md), [`docs/02_world/atlas-region-dossiers-v1.md`](../02_world/atlas-region-dossiers-v1.md), [`docs/02_world/calendar-language-naming-bible-v1.md`](../02_world/calendar-language-naming-bible-v1.md) |
| Architecture | [`docs/10_story_architecture/location-world-crosswalk-v1.md`](../10_story_architecture/location-world-crosswalk-v1.md), `docs/10_story_architecture/detail/` 하위 v01~v15 scene-ready 15종 |
| Context Pack | `.agent/context-packs/episodes/` 하위 E001~E003 3종 |
| 원고 | `manuscript/volume-01/E001`, `E002` |
| 검증기 | [`.agent/skills/sentence-narrator/pronunciation-lexicon.md`](../../.agent/skills/sentence-narrator/pronunciation-lexicon.md), `scripts/validate_e001_canon.py` |
| 품질 보고서 | `manuscript/quality/*` |

`validate_e001_canon.py`가 명칭 문자열을 검사한다면 개명과 동시에 갱신하지 않으면 검증이 깨진다. **개명 PR에서 반드시 스크립트를 함께 확인해야 한다.**

---

## 7. 총계

| 구분 | 대상 수 | files | hits |
|---|---:|---:|---:|
| 후보 제시됨 (기관) | 4 | 26 | 47 |
| 후보 제시됨 (음운) | 2 | 3 | 3 |
| 이름 불필요 | 2 | 7 | 10 |
| 설정 확인 필요 (중단) | 8 | 37 | 53 |
| 작가 선택 필요 (음운 충돌) | 4 | 61 | 96 |

**후보가 제시된 6개 대상의 실제 치환 규모는 29개 파일 / 50행이다.** 예상보다 작다. 근거는 [`naming-full-audit-v1.md`](naming-full-audit-v1.md) §1.2 — Domain Bible이 이미 평이한 이름을 사용하고 있어, 명명 패키지 표층만 조정하면 되기 때문이다.
