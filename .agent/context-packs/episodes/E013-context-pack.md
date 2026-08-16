# Episode Context Pack — E013

Status: D10 READY  
Episode: E013  
Title: 한쪽 장부에만 있는 마을  
Compiled By: A21 Context Pack Compiler  
Reference: `agent/1c-evidence-subact`

> 이 CP는 정본이 아니다. 충돌 시 원본 정본과 권한계층을 따른다. 각 항목의 근거 경로는 절마다 명시한다.

## 1. Authority / Architecture

Required sources:

- [`/AI_PROJECT.md`](../../../AI_PROJECT.md)
- [`docs/00_project/canon-constitution-v1.md`](../../../docs/00_project/canon-constitution-v1.md)
- [`docs/00_project/canon-naming-pack-v1.md`](../../../docs/00_project/canon-naming-pack-v1.md)
- [`docs/00_project/terminology-and-addressing-clarification-v1.md`](../../../docs/00_project/terminology-and-addressing-clarification-v1.md)
- [`docs/00_project/decision-log.md`](../../../docs/00_project/decision-log.md) — DEC-016·017·018·020·021
- [`docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md`](../../../docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md) — E013 행
- [`docs/10_story_architecture/detail/v01-scene-ready-design-v1.md`](../../../docs/10_story_architecture/detail/v01-scene-ready-design-v1.md) — Subact 1C / E013 절
- [`docs/10_story_architecture/subact-causal-matrix-v1.md`](../../../docs/10_story_architecture/subact-causal-matrix-v1.md) — 1C 행
- [`docs/10_story_architecture/location-world-crosswalk-v1.md`](../../../docs/10_story_architecture/location-world-crosswalk-v1.md) — V01 1C
- [`docs/10_story_architecture/scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) — E013 행
- [`docs/10_story_architecture/secondary-pov-and-offscreen-action-allocation-v1.md`](../../../docs/10_story_architecture/secondary-pov-and-offscreen-action-allocation-v1.md) — §4 (E013 배정 없음)

Episode function (registry E013 · v01 E013 · matrix 1C):

- Grand Act: GA I — 잘못된 치료
- Volume: V1 — 회색 종이 울리는 날
- Arc: Arc 02 — 성공한 암살과 사라진 미래
- Subact: 1C — 표적의 범죄 증거 확보 / 증거가 맞고 진실이 틀릴 때
- Beat: 진입
- Goal: 개혁가의 범죄 혐의를 현장에서 검증한다
- Opposition: 서기 교대까지로 제한된 체류시간, 왕실 문서와 지방 문서의 서로 다른 관할, 무력행사 시 전 문서 봉인
- Choice: 왕실 보고서와 현지 세금장부를 대조한다
- Cost: 아이리스의 신원 보증을 소모하고, 도시 안에서 에이든의 조회 이력이 남는다
- State Change: 혐의 검증이 ‘본부 문서를 다시 읽는 일’에서 ‘현지 문서·지도·사람이 서로 어긋나는 일’로 바뀐다
- Hook: 해당 마을의 마지막 세금이 내일 날짜로 이미 납부돼 있다

## 2. E012 Carryover

근거: [`v01-scene-ready-design-v1.md`](../../../docs/10_story_architecture/detail/v01-scene-ready-design-v1.md) E010–E012, registry E010–E012.

### 에이든

- 환자 호송 참여로 도시 임시 통행권 확보
- 성당 구휼기사단 명부에 외지 치료보조자로 등록됨 — 추적 가능 상태
- 본부가 제거 시한을 앞당겼다는 사실을 아이리스에게 숨기고 있음
- 표적 접촉 가능 시간은 E011에서 이미 반나절 줄어 있음

### 아이리스 네르

- 도시 안내와 현지 신원 보증을 제공하는 조건부 협력자
- 조건: 환자들을 표적 접근 수단으로 쓰면 귀환표식을 끊는다
- 에이든의 목적을 믿지 않으며 장비의 정체에 대한 답을 아직 받지 못함

### 미해결 물증

- E011에서 건진 기록상자 안의 문서 하나가 에이든의 출발일보다 뒤 날짜로 작성돼 있음
- 도시 종루의 회색 종이 울리지 않았는데 환자들이 동시에 귀를 막은 사건
- 미래 장비 일부가 물에 노출돼 은폐가 약해짐

### 장치 상태

- 오착 약 18km, 강제복귀 사실상 1회 ([`master-chronology-and-aging-ledger-v1.md`](../../../docs/01_timeline/master-chronology-and-aging-ledger-v1.md) §4 J01)
- 귀환창은 본부 시한 단축으로 이미 압축된 상태이며 E013에서는 더 줄지 않는다

E013은 E012의 통행권 발급 절차나 회색 종 장면을 재연하지 않는다. 통행권은 기록소 문턱에서 한 번 기능할 뿐이다.

## 3. Time / Location

근거: [`master-chronology-and-aging-ledger-v1.md`](../../../docs/01_timeline/master-chronology-and-aging-ledger-v1.md) §1·§3·§4, [`location-world-crosswalk-v1.md`](../../../docs/10_story_architecture/location-world-crosswalk-v1.md) V01, [`atlas-region-dossiers-v1.md`](../../../docs/02_world/atlas-region-dossiers-v1.md) R05.

- Era: N0 / 건국력(CY) 640, 안개월
- 도착 기준일: 안개월 4일 (J01). E013은 그 며칠 뒤이며 정확 일자는 미확정
- 에이든: 41세 / 주관적 누적일 V1 총 24일 구간 내부
- 권역: 잿빛 변경 (서부)
- 1C 주무대: 두 역사의 라베른 · 절검의 언덕 (crosswalk V01)
- E013 실내: 지방 기록소 — 세금대장실, 지도대, 기록소 앞 대기공간
- 이동은 도시 내부이며 장거리 이동시간 문제 없음
- Tactical: 체류 가능 시간은 서기 교대 전까지. 무력침입 시 모든 문서가 즉시 봉인된다 (v01 E013 Tactical Logic)

## 4. Record Conflict Package

근거: v01 E013, [`political-economy-record-law-v1.md`](../../../docs/08_institutions/political-economy-record-law-v1.md), R05 서부 잿빛 변경.

E013이 다루는 문서·물건은 네 종류이며 서로 다른 층에서 어긋난다.

### 왕실 피해보고서

- 세렌 바일 사건의 피해지역 목록을 담고 있음
- 중앙 관할 문서이며 지방 관할 문서와 작성 목적이 다름
- 이 회차에서 위조로 확정하지 않는다

### 현지 세금대장

- 지방 기록소가 관리하는 납세 기록
- 왕실 보고서가 폐허로 적은 지역 중 일부가 정상 납부지로 남아 있음
- 납세기록은 남았으나 납세자의 존재가 사라진 사례가 이 권역에 이미 존재함 (R05 빈 세금소)

### 왕실 지도

- 같은 마을을 폐허로 표시
- 지도와 장부는 서로 다른 기관의 승인 절차를 거쳤으므로 한쪽을 거짓말로 단정할 근거가 아직 없음

### 주민의 몸

- 현지인은 그 마을을 알고 있으며 이름·풍습·거리를 말할 수 있음
- 그러나 길을 설명할 때 서로 다른 방향을 가리킨다
- 주민은 문서 외에도 벽흔·가족노래·묘표·공동식사 순번으로 존재를 증명한다 (R05 생활)

## 5. Character State

근거: [`cast-canon-index-v2.md`](../../../docs/05_characters/cast-canon-index-v2.md), [`cast-encyclopedia-v1.md`](../../../docs/05_characters/cast-encyclopedia-v1.md) C03·C06·C12, [`supporting-cast-dossiers-c11-c20-v2.md`](../../../docs/05_characters/supporting-cast-dossiers-c11-c20-v2.md) C12, [`voice-relationship-state-bible-v1.md`](../../../docs/05_characters/voice-relationship-state-bible-v1.md).

### 에이든 로엔

- 목표: 본부가 준 혐의를 현지 자료로 한 번 더 확인하고 표적 접근 근거를 확보
- 습관: “이 물건이 무엇인가”가 아니라 “누가 언제 어디서 그것을 썼는가”를 묻는다
- 임무중 어법: 목표 → 출구 → 비용 순서
- 죄책감 표식: 세렌을 이름 대신 ‘표적’으로 부른다 (voice bible §2)
- 오류 가능성: 지방 문서가 왕실 문서를 이긴다고 성급히 뒤집는 것
- 금지: 이 회차에서 세렌 무죄 판단, 본부 전체를 적으로 규정

### 아이리스 네르

- 이 회차의 기능: 문턱을 여는 신원 보증과 현지 통역
- 평시 어법: 사람·장소·오늘 필요한 물자를 구체적으로 언급
- 협상 어법: 상대의 원칙보다 누가 언제 무엇을 잃는지 묻는다
- 독립 목표: 마을이 지워지고 있다면 그 주민의 현재 안전이 먼저다 — 증거 확보가 아니다
- 금지: 에이든의 조수화, 정보 제공기 역할, 삼각관계 암시 (voice bible §7·§8)

### 지방 기록소 실무자

- 정본 후보는 C12 엘사 네르 (지방 세금·출생·장례 기록관, V1 첫 핵심권, ‘V1 세 날짜 불일치의 현지 원천’)
- v01 설계가 E013에서 이름을 명시하지 않으므로 원고에서 이름을 즉석 확정하지 않는다 — §12 gaps 참조
- 습관: 상대가 이름을 말하면 반드시 다시 확인한다. 중앙 관료 앞에서는 지나치게 공손한 반어
- Boundary: 살아 있는 사람을 죽은 자 명부에 올리지 않는다
- 금지: 모든 진실을 숨겨 둔 만능 기록관, 압박 한 번에 자료 전부 제공

### 세렌 바일

- E013에 직접 등장하지 않는다. 문서와 혐의로만 존재
- 유죄·무죄 확정 금지. 영구사망 HARD LOCK은 E024 부근이며 이 회차와 무관

## 6. Mystery / Information Ceiling

근거: [`mystery-reinforcement-ladder-v1.md`](../../../docs/11_mystery/mystery-reinforcement-ladder-v1.md), v01 E013 Information Ceiling.

Active mysteries:

- M02 세렌 바일은 왜 창시자로 기록됐는가 — 사다리 다음 단은 E014
- M05 빈 세금장부에 무엇이 있었는가 — **사다리 첫 단은 E036**. E013은 장부를 무대로 쓰되 ‘비용 배분표’ 해석을 선취하지 않는다
- M12 최종 흑막은 누구인가 — 개인 흑막 암시 금지
- M14 원래 시간선은 진짜인가 — 배경 진동만. 언급 금지

Reader may know:

- 왕실 문서와 지방 문서가 같은 마을을 서로 다르게 기록한다
- 주민의 기억에는 그 마을이 남아 있다
- 마을이 ‘지워지고 있다’는 추론이 가능하다

Reader must not know yet:

- 무엇이 마을을 지우는가 — 장치인지 행정인지 사람인지
- 누가 어떤 이유로 세렌에게 책임을 뒤집었는가
- 세렌이 지방 소거를 늦췄다는 전체 기능
- 삭제된 증언자의 정체
- 19만 생존증가 모델의 최종 오류구조

Final hook:

- 그 마을의 마지막 세금이 **내일 날짜로 이미 납부돼** 있다
- 의미: 기록이 현재보다 앞서 움직이고 있다. 위조라면 너무 조잡하고, 사실이라면 시간이 어긋나 있다
- 금지: 이 한 줄로 시간장치의 존재·기능을 설명하는 대사, 세렌 무죄 확정, 새 시간법칙 추가

## 7. POV / Storycraft

근거: [`canon-constitution-v1.md`](../../../docs/00_project/canon-constitution-v1.md) OPERATIONAL LOCKS, secondary-POV 배치표 §4 (E013 배정 없음), scene-density-map E013 행.

- POV: 에이든 단일 근접 3인칭
- Scene Density: **S형 3장면** — 배정 사유: 세금대장실·지도대·주민확인으로 사라지는 마을을 추론하는 기록 조사 회차
- Primary craft: 세 층위의 어긋남 — 문서 / 지도 / 사람
- Secondary A: 제한 체류시간(서기 교대)이 만드는 절차적 압박
- Secondary B: 부재의 물질화 — 없는 것을 있는 물건으로 보여주기
- Hook: H2 정보 역전
- Reader reward: 혐의 검증을 하러 들어갔다가 혐의보다 큰 것이 어긋나 있음을 발견

## 8. Scene Values

### Scene 1 — 세금대장실

- Entry: 본부 혐의를 현지 문서로 확인하면 표적 접근 근거가 완성된다
- Evidence: 왕실 피해보고서의 지역 목록과 현지 세금대장의 납부 기록
- Exit: 목록 중 한 곳이 두 문서에서 서로 다른 상태로 살아 있다

### Scene 2 — 지도대

- Entry: 둘 중 하나가 낡았거나 갱신되지 않았을 뿐이다
- Evidence: 왕실 지도의 폐허 표시와 지방 장부의 정상 납부지 기록. 두 문서는 다른 기관의 승인을 각각 거쳤다
- Exit: 어느 쪽도 무효화할 수 없고, 마을은 한쪽 기록에만 존재한다

### Scene 3 — 기록소 앞 주민확인

- Entry: 사람에게 물으면 종이의 다툼이 끝난다
- Evidence: 주민들은 마을을 알지만 길을 설명할 때 서로 다른 방향을 가리킨다. 마지막 납세 항목의 날짜가 내일이다
- Exit: 검증 목표가 ‘표적의 혐의’에서 ‘무엇이 지워지고 있는가’로 옮겨간다

## 9. Anti-Repeat

- **E003처럼 문서 두 장을 나란히 놓고 날짜를 대조하는 방식으로 회차를 닫지 않는다.** E013의 결정적 증거는 종이가 아니라 주민이 가리키는 손이다
- E001의 ‘삭제된 글자 하나가 되살아난다’ 훅 금지. E013의 이상은 지워진 것이 아니라 **아직 오지 않은 날짜**다
- E002의 기관 순회·귀환석 토양 재사용 금지
- E009의 ‘진품 인장 두 장’ 구조 반복 금지 — 여기서는 문서 종류가 다르고 관할이 다르다
- 기록관이 비밀 원본을 몰래 꺼내 주는 전개 금지
- ‘모든 왕실 문서가 위조였다’ 단순 반전 금지
- 회색 종을 다시 울려 장면을 닫지 않는다 — 종은 E012에서 이미 썼다

## 10. Active State / Props

- 왕실 피해보고서 (E014에서 원본으로 다시 등장)
- 현지 세금대장과 납부 항목 행
- 왕실 지도의 폐허 표시
- 아이리스의 신원 보증 — 이 회차에서 소모됨
- 성당 구휼기사단 명부의 외지 치료보조자 등록 — 배경 추적 위험
- E011 기록상자의 미래 날짜 문서 — 봉인 상태 유지, 이 회차에서 열지 않음

내일 날짜 납세 항목이 E014 이후 재등장할 경우 A10이 prop/relic 승격 여부를 판정한다.

## 11. State Mutation Plan

E013 종료 시 기록:

- 왕실 보고서와 현지 세금대장의 대조 결과 및 불일치 마을 식별자
- 아이리스 신원 보증의 소모 여부와 잔여 신뢰도
- 기록소 접근권의 남은 조건 (서기 교대·문서 봉인 규칙)
- 주민 증언의 방향 불일치 기록
- ‘내일 날짜 납세’ 항목의 활성 상태
- 본부 시한 단축 은폐가 아이리스에게 아직 발각되지 않았음

## 12. Ready Verdict

- Authority: RESOLVED
- Domain Readiness: READY WITH GAPS
- Storycraft companion: REQUIRED / [`E013-storycraft-manifest.md`](../../../docs/10_story_architecture/craft-manifests/E013-storycraft-manifest.md)
- POV: READY (보조 POV 배정 없음)
- S0: 0
- S1: 2

S1 gaps:

1. E012에서 진입한 도시의 정식명이 v01 설계에 없다. crosswalk V01 1C 주무대가 `두 역사의 라베른`·`절검의 언덕`이므로 라베른으로 두는 것이 가장 가까우나, CP는 새 설정을 만들지 않는다. A13 확인 필요
2. v01 E013·E014의 `지방 서기`/기록소 실무자와 C12 엘사 네르의 동일인 여부가 정본에 없다. C12는 V1 첫 핵심권이며 ‘세 날짜 불일치의 현지 원천’이므로 후보이나 확정은 A13 판정 사항

E013 Storycraft Manifest 확인 뒤 A18 호출 가능.
