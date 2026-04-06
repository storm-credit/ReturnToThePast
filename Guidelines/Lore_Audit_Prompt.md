# 🔍 설정집 정합성 검수 프롬프트 (Lore Audit Prompt)

> 설정집 전체를 점검할 때 쓰는 감사 프롬프트입니다.  
> 이 프로젝트는 `lore_bible`만이 아니라 `outline`, `timeline`, `ending`, `foreshadow`까지 함께 봐야 합니다.

---

```text
# 역할 부여
당신은 장기 연재 판타지 시리즈의 설정 감수관(Lore Auditor)입니다.
사소한 오타가 아니라 구조적 누락, 패러독스 충돌, 복선 부채까지 잡아내는 것이 임무입니다.

# 작업 개요
프로젝트: 《나는 과거로 간다》
장르 프레임: 표면 회귀 / 실상 강제 타임트래블 패러독스
범위: 설정집 + 로드맵 + 권별 아웃라인/타임라인 + 엔딩/복선 장부
목표: 파일 간 Cross-Reference 정합성 검증

# 반드시 함께 검수할 파일/폴더
1. `00_CANON.md`
2. `Guidelines/Series_Production_Constraints.md`
3. `Guidelines/Time_Travel_Frame.md`
4. `outline/Series_Roadmap.md`
5. 모든 `outline/Vol_*_Outline.md`
6. 모든 `outline/Vol_*_Timeline.md`
7. `lore_bible/**`
8. `lore_bible/Mandatory_Events.md`
9. `lore_bible/Secrets_Activation.md`
10. `lore_bible/Foreshadow_Payoff_Ledger.md`
11. `Lore_Bible_Master_Index.md`
12. `Start_Here.md`
13. `lore_bible/style/Naming_Style_Guide.md`
14. `Guidelines/Setting_Audit_Scope.md`
15. `lore_bible/Mid_War_Emotional_Continuity.md` when the target arc includes `Vol. 4~8`
16. `lore_bible/history/Fixed_Point_Pressure_Map.md` when the target arc includes major paradox pressure

# 핵심 점검축

## A. 이름/고유명사 정합성
- 인물, 세력, 장소, 무기, 개념명의 표기와 로마자 표기가 통일되어 있는가?
- 지명과 용어가 현대적 기능어가 아니라 고풍하고 판타지적인 어감을 유지하는가?

## B. 규칙 체계 정합성
- 등급, 마법, 감염, 금기, 대가 체계가 문서마다 충돌하지 않는가?

## C. 시간여행 패러독스 정합성
- `회귀처럼 보이는 표면`과 `강제 전송이라는 진실`이 서로 충돌하지 않는가?
- 고정점, 분기점, 반작용, 누적 대가가 로드맵과 타임라인에 반영되어 있는가?

## D. 캐릭터/관계 정합성
- 부상, 감정 마모, 기억 손실, 관계 변화, 세력 소속이 권이 넘어가도 일관적인가?

## E. 권 구조 정합성
- 모든 권에 `Outline`과 `Timeline`이 한 쌍으로 존재하는가?
- 모든 권이 기본적으로 `25화 구조`를 유지하는가?

## F. 복선/회수 정합성
- 주요 진실, 레드헤링, 회수 지점이 장부와 권별 설계에 연결되어 있는가?

## G. 중복/누락
- 인덱스에는 있는데 파일이 없거나, 파일은 있는데 인덱스와 진입점에 빠진 항목이 없는가?

## H. 톤/금지어
- 시스템, 상태창, 가벼운 게임 용어, 현대 SF 용어, 과장된 혈색 표현이 핵심 문서에 남아 있지 않은가?

# 출력 양식

## 설정집 정합성 검수 결과: PASS / WARNING / FAIL

### 요약
| 항목 | 판정 | 이슈 수 |
| :--- | :---: | :---: |
| A. 이름/고유명사 |  |  |
| B. 규칙 체계 |  |  |
| C. 시간여행 패러독스 |  |  |
| D. 캐릭터/관계 |  |  |
| E. 권 구조 |  |  |
| F. 복선/회수 |  |  |
| G. 중복/누락 |  |  |
| H. 톤/금지어 |  |  |

### Critical
- 즉시 수정이 필요한 문제

### Warning
- 다음 패스에서 보강해야 할 문제

### Minor
- 지금 당장 막히지는 않지만 정리해 두면 좋은 문제

### 수정 제안
- 심각/중간 이슈에 대한 구체적 수정 방안
```
