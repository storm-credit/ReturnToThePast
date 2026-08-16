# Episode Context Pack — E016

Status: D10 READY  
Episode: E016  
Title: 세 편이 노리는 기록  
Compiled By: A21 Context Pack Compiler  
Reference: `agent/1c-evidence-subact`

> 이 CP는 정본이 아니다. 충돌 시 원본 정본과 권한계층을 따른다.

## 1. Authority / Architecture

Required sources:

- [`/AI_PROJECT.md`](../../../AI_PROJECT.md)
- [`docs/00_project/canon-constitution-v1.md`](../../../docs/00_project/canon-constitution-v1.md)
- [`docs/00_project/canon-naming-pack-v1.md`](../../../docs/00_project/canon-naming-pack-v1.md)
- [`docs/00_project/terminology-and-addressing-clarification-v1.md`](../../../docs/00_project/terminology-and-addressing-clarification-v1.md)
- [`docs/00_project/decision-log.md`](../../../docs/00_project/decision-log.md) — DEC-016·017·018·020·021
- [`docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md`](../../../docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md) — E016 행
- [`docs/10_story_architecture/detail/v01-scene-ready-design-v1.md`](../../../docs/10_story_architecture/detail/v01-scene-ready-design-v1.md) — Subact 1C, E016 절
- [`docs/10_story_architecture/subact-causal-matrix-v1.md`](../../../docs/10_story_architecture/subact-causal-matrix-v1.md) — 1C 행
- [`docs/10_story_architecture/scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) — V1 E016 배정
- [`docs/10_story_architecture/location-world-crosswalk-v1.md`](../../../docs/10_story_architecture/location-world-crosswalk-v1.md) — V01 1C
- [`docs/05_characters/cast-canon-index-v2.md`](../../../docs/05_characters/cast-canon-index-v2.md)
- [`docs/05_characters/voice-relationship-state-bible-v1.md`](../../../docs/05_characters/voice-relationship-state-bible-v1.md)
- [`docs/05_characters/character-faction-institution-bible-v1.md`](../../../docs/05_characters/character-faction-institution-bible-v1.md) — Factions 지방연맹·중앙 왕실
- [`docs/02_world/atlas-region-dossiers-v1.md`](../../../docs/02_world/atlas-region-dossiers-v1.md) — R05 서부 잿빛 변경
- [`docs/03_systems/time-travel-ontology-v1.md`](../../../docs/03_systems/time-travel-ontology-v1.md) — What Travels, Memory Continuity
- [`docs/11_mystery/mystery-reinforcement-ladder-v1.md`](../../../docs/11_mystery/mystery-reinforcement-ladder-v1.md) — M15 E016 단
- [`docs/12_losses/permanent-loss-lock-v1.md`](../../../docs/12_losses/permanent-loss-lock-v1.md)

Episode function:

- Grand Act: GA I — 잘못된 치료
- Volume: V1 — 회색 종이 울리는 날
- Subact: 1C — 증거가 맞고 진실이 틀릴 때
- Beat: 대항 세력
- Goal: 왕실 추적대와 지방연맹이 동시에 같은 기록을 노리는 상황에서 표적 추적을 이어 간다
- Opposition: 세 세력이 각자 합리적이지만 부분적인 목표를 가진다
- Choice: 어느 편에도 정체를 밝히지 않고 표적 추적을 계속한다
- Cost: 어느 세력의 보증도 얻지 못해 기록이 분산되고 단독 접근만 남는다
- State Change: 에이든이 ‘기록을 읽는 사람’에서 ‘세 세력에게 읽히는 사람’으로 위치가 바뀐다
- Hook: 개혁가가 에이든의 출발 인장을 알아본다 — 미래 본부의 존재를 알고 있다

## 2. E015 Carryover

### 에이든

- 개혁가 조직 은신처 잠입 성공, 증거실 우선 확보
- 감염자 명단으로 보이던 문서가 삭제예정지 주민·족보 목록임을 확인
- 실험시설이라는 초기 해석은 무너졌으나 무고 판정으로 뒤집지 않음
- 시설에 동의 없는 기억채취가 있어 개혁가가 완전히 무고하지 않다는 사실을 동시에 안다

### 아이리스 네르

- E015에서 에이든과 다른 통로로 진입해 환자 탈출로를 우선함
- E012 조건 유지: 환자를 표적 접근 수단으로 쓰면 귀환표식을 끊는다
- E014에서 에이든이 귀환용 응급자원을 현지 치료에 내준 것을 알고 있음

### 세렌 바일

- E015 훅에서 그의 실험기록에 에이든의 출발 인장 구조가 그려져 있음이 드러남
- E016에서 처음으로 에이든과 같은 공간에 있게 된다
- 유죄·무죄를 확정하지 않는다

### 본부

- E012에서 표적 제거 시한을 앞당김
- 에이든은 시한 단축 사실을 아이리스에게 숨긴 상태

## 3. Time / Location

- Era: N — 건국력 640년대, 서부 잿빛 변경
- 시점: E015 잠입 직후, 같은 밤에서 이튿날로 이어지는 연속 구간
- 에이든: F0 출발 시 41세, Era N 현지 체류 누적 중
- Main locations:
  1. 은신처 지붕길 — 왕실 추적대의 포위선을 위에서 본다
  2. 은신처 아래 지하통로 — 지방연맹 접촉선
  3. 기록 분산 지점 — 문서가 세 방향으로 쪼개지는 자리
  4. 짧은 조우 지점 — 세렌과의 첫 대면
- 1C 주무대는 [`location-world-crosswalk-v1.md`](../../../docs/10_story_architecture/location-world-crosswalk-v1.md) V01 기준 `두 역사의 라베른·절검의 언덕`이며 세부 장소명은 SOFT LOCK이다
- 절검의 언덕은 1D의 저항·사망 구간에 배정된 장소이므로 E016에서 소모하지 않는다
- 이동은 도시 구역 내부이며 장거리 이동시간 문제가 없다

## 4. Three-Faction Package

Sources:

- V1 scene-ready design E016 절
- [`docs/05_characters/character-faction-institution-bible-v1.md`](../../../docs/05_characters/character-faction-institution-bible-v1.md) Factions
- [`docs/02_world/atlas-region-dossiers-v1.md`](../../../docs/02_world/atlas-region-dossiers-v1.md) R05 정치

### 왕실 추적대

- 목표: 기록 확보. 환자 살해보다 기록 회수가 우선순위다
- 정당성: 중앙 왕실은 법·승계·재난지휘·토지체계를 실제로 운영한다
- 피해: 지방 주소와 종족 권리를 중앙 표준에 종속시킨다
- 금지: 재미로 학살하는 악역화, 기록을 원하는 이유가 없는 추격조

### 지방연맹

- 목표: 기록 공개. 주민·토지·민병·지역 기록 보호가 기능이다
- 장점: 현장 신뢰와 빠른 생활 대응
- 한계: 특정 귀족의 피해는 공개 대상에서 뺀다. 지역 이기주의와 타 지역 비용 전가가 정본 위험이다
- 금지: 순수한 민중 편으로 미화

### 개혁가 조직

- 목표: 삭제예정지 주민의 대피와 증언 보존
- 결함: 동의 없는 기억채취를 실제로 했다
- 세렌은 E016에서 도주가 아니라 확인을 택한다

### 세 세력의 공통점과 차이

- 셋 다 같은 기록 뭉치를 원한다
- 셋 다 서로 다른 부분만 원한다. 왕실은 회수, 연맹은 선택적 공개, 개혁가 조직은 주민 주소
- 어느 쪽도 전체를 갖지 못한 채 회차가 끝난다

## 5. Character State

### 에이든 로엔

- 목표: 세 세력의 충돌을 피해 표적에게 접근
- 방법: 정체를 밝히지 않고 각 세력의 실패조건만 읽는다
- 말투 정본: “목표·출구·비용” 순서, 짧은 확인 질문
- 오류 가능성: 어느 편에도 서지 않는 것이 중립이라고 믿는다
- 금지: 연설 한 번으로 세력을 돌려세우기, 전투 승리로 상황 정리

### 아이리스 네르

- 독립 목표: 환자와 주민의 오늘. 미래의 숫자와 중앙의 수동태를 공격한다
- 기능: 지방연맹 쪽 언어와 신뢰를 가진 유일한 통로
- 관찰: 에이든이 아무에게도 답하지 않는다는 사실 자체를 기록한다
- 금지: 도움을 받았다는 이유로 충성, 로맨스 삼각 배치

### 세렌 바일

- E016 기능: 표적이 처음으로 관찰자가 된다
- 아는 것: 에이든의 출발 인장이 무엇인지 알아볼 만큼의 구조 지식
- 모르는 것: 미래의 규모, 명령의 발신 주체, 자기 이름이 어떻게 기록될지
- 대사 기능: “당신들의 명령문은 누가 살아남긴 기록인가”
- 금지: 모든 진실을 아는 예언자, 즉석 무죄 선언

### 왕실 추적대 지휘자 / 지방연맹 대표

- 새 핵심 이름을 즉석 확정하지 않는다
- 각자 자기 지지자·주민·직무의 구체적 피해를 근거로 말한다
- 두 사람이 같은 반대논리를 쓰지 않는다

## 6. Mystery / Information Ceiling

Active mysteries:

- M15 최초 연대기는 어디 있는가 — 사다리 첫 단이 **E016 세렌의 암호**다. 이 회차에서 암호의 존재만 심는다
- M02 세렌은 왜 창시자로 기록됐는가 — 독자 추론 가능 시점은 E061이므로 여기서 확정하지 않는다
- M12 최종 흑막은 누구인가 — 사다리 첫 단은 E070이다. 개인 흑막 암시 금지
- M05 빈 세금장부 — E013·E014의 장부 흔적을 배경 상태로만 유지

Reader may know:

- 같은 기록을 세 세력이 서로 다른 이유로 원한다
- 왕실도 연맹도 주민을 위해 움직이지 않으며 동시에 둘 다 실제 기능을 한다
- 세렌은 미래에서 온 물건을 알아볼 만한 지식을 이미 갖고 있다
- 세렌이 남긴 문서 중 아무도 읽지 못하는 암호가 있다

Reader must not know yet:

- 세렌이 지방 소거를 늦췄다는 전체 기능
- 기록을 뒤집은 조작 주체
- 삭제된 증언자의 정체
- 19만 생존모델의 최종 오류구조
- 암호가 최초 연대기와 연결된다는 사실

Final hook:

- 개혁가가 에이든의 출발 인장을 알아보고 미래 본부의 존재를 안다는 것이 드러난다
- 의미: 조사하는 쪽과 조사받는 쪽의 위치가 한 번 뒤집힌다
- 금지: 세렌이 시간여행 원리를 설명하는 강의, 새 시간법칙 추가

## 7. POV / Storycraft

- POV: 에이든 단일 근접 3인칭
- Scene Density: **E형 4장면** — [`scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) V1 E016
- 배정 사유: 왕실 추적대·지방연맹·개혁가가 각자 합리적이지만 서로 다른 목표로 같은 기록을 노리므로 세력별 반응을 연결해야 한다
- E형 규칙: 4번째 장면은 비용 또는 반대편의 능동행동이다
- Primary craft: 하나의 물건을 둘러싼 삼각 이해충돌
- Secondary A: 정체 은닉의 실제 비용
- Secondary B: 대립자의 합리성 분할
- Hook: H2 정보 역전
- Reader reward: 적이 한 덩어리가 아니라는 확인과 표적이 먼저 이쪽을 읽었다는 역전

## 8. Scene Values

### Scene 1 — 지붕길

- Entry: 포위는 개혁가 조직을 죽이러 온 것이다
- Evidence: 추적대의 진입 순서·수레 배치·문서 상자 우선 확보 동선
- Exit: 그들이 원하는 것은 사람이 아니라 기록이다

### Scene 2 — 지하통로

- Entry: 기록 공개를 원하는 쪽은 우리 편일 수 있다
- Evidence: 지방연맹이 공개 목록에서 특정 귀족 피해를 빼려 한다
- Exit: 공개파도 자기 이름은 지운다

### Scene 3 — 기록 분산

- Entry: 정체를 숨기면 세 편 모두와 거래할 수 있다
- Evidence: 세 세력이 동시에 손을 대자 기록 뭉치가 세 방향으로 쪼개진다. 아무도 읽지 못하는 암호 조각이 남는다
- Exit: 아무 편도 아닌 사람은 아무 보증도 받지 못한다 — 이 장면이 E형의 비용 장면이다

### Scene 4 — 짧은 조우

- Entry: 표적은 아직 자신이 표적인 줄 모른다
- Evidence: 세렌이 에이든의 출발 인장을 알아보고 명령문의 계보를 되묻는다
- Exit: 조사자가 조사 대상이 된다

## 9. Anti-Repeat

- E002처럼 세력을 한 명씩 순서대로 소개하는 강의식 순회 금지
- E003·E013처럼 두 문서를 나란히 놓고 대조하는 이미지 반복 금지
- E015 잠입 구조를 다시 쓰지 않는다. 이번에는 이미 들어와 있는 상태에서 시작한다
- E001의 삭제된 글자·회색으로 되살아나는 이름 금지
- 세 세력이 같은 반대논리를 말하지 않는다
- 왕실=악, 지방연맹=선의 이분 구도 금지
- 전투 승리로 회차를 닫지 않는다. Arc 01·02 Anti-Repeat 조항이다
- 세렌이 자기 무죄를 주장하는 대사로 훅을 만들지 않는다

## 10. Active State / Props

- 개혁가 조직의 삭제예정지 주민·족보 목록 (E015 확보)
- 세렌의 실험기록 — 출발 인장 구조가 그려진 면
- 아무도 읽지 못하는 세렌의 암호 조각 — M15 첫 단
- 에이든의 출발 인장 — 동반 등록·기억 연속의 근거이며 이번 회차에 처음 타인에게 읽힌다
- 지방 세금대장 사본 (E013–E014 계열, 배경 상태)
- 귀환용 응급자원 감소분 (E014 비용, 배경 상태)

세렌의 암호 조각이 E017 이후 재등장할 경우 A10이 prop/relic 승격 여부를 판정한다.

## 11. State Mutation Plan

E016 종료 시 기록:

- 왕실 추적대의 포위 단계와 기록 회수 진척도
- 지방연맹과의 접촉 상태 및 공개 제외 항목
- 에이든의 정체 은닉 유지 여부와 세 세력별 노출 정도
- 세렌이 출발 인장을 인지했다는 사실
- 암호 조각의 보관 주체
- 아이리스가 관찰한 에이든의 무응답 기록
- 표적 제거 시한 잔여

## 12. Ready Verdict

- Authority: RESOLVED
- Domain Readiness: READY
- Storycraft companion: REQUIRED / prepared separately
- POV: READY
- Scene Density: E형 4장면 확정 · 설계 3비트를 4장면으로 전개
- S0: 0
- S1: 0

E016 Storycraft Manifest와 E015 상태기록 확인 뒤 A18 호출 가능.
