# Episode Context Pack — E015

Status: D10 READY  
Episode: E015  
Title: 병원처럼 보이는 실험실  
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
- [`docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md`](../../../docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md) — E015 행
- [`docs/10_story_architecture/detail/v01-scene-ready-design-v1.md`](../../../docs/10_story_architecture/detail/v01-scene-ready-design-v1.md) — E015 절
- [`docs/10_story_architecture/subact-causal-matrix-v1.md`](../../../docs/10_story_architecture/subact-causal-matrix-v1.md) — 1C 행
- [`docs/10_story_architecture/location-world-crosswalk-v1.md`](../../../docs/10_story_architecture/location-world-crosswalk-v1.md) — V01 1C
- [`docs/10_story_architecture/scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) — E015 행
- [`.agent/context-packs/episodes/E014-context-pack.md`](E014-context-pack.md)
- [`docs/12_losses/permanent-loss-lock-v1.md`](../../../docs/12_losses/permanent-loss-lock-v1.md) — L001

Episode function (registry E015 · v01 E015 · matrix 1C):

- Grand Act: GA I — 잘못된 치료
- Volume: V1 — 회색 종이 울리는 날
- Subact: 1C — 표적의 범죄 증거 확보
- Beat: 잘못된 해석
- Goal: 개혁가 조직의 은신처가 병원인지 실험실인지 판별한다
- Opposition: 시설 외형이 두 해석을 모두 지지하고, 아이리스와 목표가 갈리며, 시설 내부에 실제 위법 행위가 있다
- Choice: 에이든은 실험 증거로 해석하고 잠입한다
- Cost: 아이리스와 서로 다른 통로로 갈라져 각자의 우선순위가 드러난다
- State Change: ‘개혁가는 재앙을 퍼뜨리는 자’라는 해석이 무너지지만, 무고하다는 결론으로 대체되지 않는다
- Hook: 개혁가의 실험기록에 에이든의 출발 인장 구조가 그려져 있다

## 2. E014 Carryover

근거: [`E014-context-pack.md`](E014-context-pack.md), v01 E014.

### 문서 상태

- 왕실 보고서 원본의 작성일이 사건 발생일보다 앞선다
- 피해 수치가 나중 잉크로 덧씌워졌다
- 서명란의 이름이 이미 죽은 기록관의 것이다
- 세렌의 금지의식 혐의 자체는 여전히 성립한다
- E013의 ‘내일 날짜 납세’ 항목은 미해명 상태로 남아 있다

### 자원 상태

- 귀환용 응급자원이 격리촌 치료로 전환돼 잔량이 줄었다
- 귀환 후 신체 안정 여유가 감소했다 — V1 State Ledger 항목
- 강제복귀 사실상 1회, 오착 약 18km는 변동 없음

### 관계 상태

- 아이리스는 에이든의 목적을 여전히 믿지 않으나 ‘사람을 비용표로만 보지 않는다’는 한 항목을 인정했다
- 아이리스의 조건은 유효하다 — 환자들을 표적 접근 수단으로 쓰면 귀환표식을 끊는다
- 에이든은 본부의 시한 단축을 여전히 숨기고 있다

E015는 문서 검토를 반복하지 않는다. 종이가 답을 주지 못했으므로 **현장을 본다.**

## 3. Time / Location

근거: master chronology §1·§4, crosswalk V01 1C, [`atlas-region-dossiers-v1.md`](../../../docs/02_world/atlas-region-dossiers-v1.md) R05.

- Era: N0 / CY 640 안개월, E014 직후
- 에이든: 41세 / 주관적 누적일 V1 24일 구간 내부
- 권역: 잿빛 변경. 1C 주무대는 두 역사의 라베른 · 절검의 언덕 (crosswalk V01)
- Main locations:
  1. 은신처 외곽 관찰지점
  2. 두 갈래 침입 통로 (환자 이동로 / 봉인실 접근로)
  3. 명단실
- 야간 또는 인계시간대 이동이며 도시 경비·성당 순찰 회피가 전제된다
- 이 회차에서 귀환창은 단축되지 않는다. 줄어드는 것은 **은폐 여유**다

## 4. Facility Reading Package

근거: v01 E015, [`mana-fever-gray-calamity-v1.md`](../../../docs/03_systems/mana-fever-gray-calamity-v1.md), [`magic-and-mana-v1.md`](../../../docs/03_systems/magic-and-mana-v1.md), R05 서부 잿빛 변경, cast-encyclopedia C06.

시설은 두 해석을 **동시에** 지지한다. 어느 쪽도 오독이 아니게 설계한다.

### 실험실로 읽히는 근거

- 환자가 계속 들어가고 나오는 양이 치료 규모를 넘는다
- 마력기구가 병상보다 많다
- 봉인실이 따로 있고 출입이 통제된다
- 명단이 감염자 분류표처럼 정렬돼 있다

### 병원·대피소로 읽히는 근거

- 실제 치료 물자와 식수 배분이 존재한다
- 환자 가족이 함께 머문다
- 이동 방향이 격리가 아니라 **바깥으로** 향한다

### 실제 상태 (v01 False Interpretation)

- 개혁가 조직은 기록 소거 전에 주민을 대피시키고 있다
- 명단은 감염자 목록이 아니라 삭제예정지 주민과 족보 목록이다

### 개혁가가 무고하지 않은 근거 (v01 Opposition)

- 시설에는 동의 없는 기억채취가 있다
- 이 사실은 이 회차에서 축소하거나 정당화하지 않는다
- C06의 결함: 폭로 속도를 주민대피보다 우선할 수 있음 / 동맹과 정보를 일부 숨김

## 5. Character State

근거: cast-canon-index-v2 C03·C06, cast-encyclopedia-v1 C03·C06, voice-relationship-state-bible-v1 §2·§3·§5, permanent-loss-lock-v1 L001.

### 에이든 로엔

- 목표: 문서로 확인되지 않은 것을 현장에서 판별
- 초기 해석: 실험 증거가 있다 — 이것이 이 회차의 합리적 오답이다
- 임무중 어법: 목표 → 출구 → 비용
- 죄책감 표식: 여전히 ‘표적’이라는 역할명을 쓴다
- 오류 가능성: 해석이 뒤집힌 뒤 반대편으로 과잉 이동하는 것
- 금지: 세렌 무죄 확정, 임무 취소 결정, 이 회차에서 세렌과 대면

### 아이리스 네르

- 이 회차의 독립 목표: 환자 탈출로 확보. 증거 확보가 아니다
- 전문: 지역조직, 대피, 토지·증언, 귀환표식 차단, 민병·배급 협상
- 갈라지는 이유는 불신이 아니라 **우선순위**다
- 거짓 믿음: 눈앞의 사람을 지키면 후대·외부의 비용은 나중에 해결할 수 있다
- 금지: 에이든 구출용 장치, 로맨스 신호, 삼각관계 암시

### 개혁가 조직 (세렌 측)

- 세렌 바일 본인은 **등장하지 않는다.** 첫 조우는 E016의 짧은 조우다
- 조직원은 헌신적이면서 동시에 위법을 실행 중인 사람들이다
- 기억채취 대상자 중 동의하지 않은 사람이 있다
- 금지: 성인화된 저항군, 전부 악의적인 광신집단

### 환자·주민

- 대피 대상이지 배경 소품이 아니다
- 주민은 문서 외에도 벽흔·가족노래·묘표·공동식사 순번으로 존재를 증명한다 (R05)

## 6. Mystery / Information Ceiling

근거: mystery-reinforcement-ladder-v1 M02·M05·M10·M12, v01 E015.

Active mysteries:

- M02 세렌 바일은 왜 창시자로 기록됐는가 — E015는 해석을 흔들되 사다리 다음 단(E033·E061)을 선취하지 않는다
- M05 빈 세금장부 — 삭제예정지 명단이 배경으로 닿지만 ‘희생 분배표’ 해석은 E036 이후
- M10 출생 원인이 사라져도 에이든은 왜 남는가 — 출발 인장이 처음으로 **타인의 자료 안에서** 관측된다. 사다리 첫 단 E045를 앞당기지 않는다
- M12 최종 흑막 — 개인 흑막 지목 금지

Reader may know:

- 시설은 병원이면서 실험시설처럼 보이도록 실제로 두 기능을 겸한다
- 명단은 감염자가 아니라 삭제예정지 주민과 족보 목록이다
- 개혁가 조직은 소거 전에 주민을 빼내고 있다
- 그 조직에 동의 없는 기억채취가 존재한다
- 개혁가의 실험기록에 에이든의 출발 인장 구조가 그려져 있다

Reader must not know yet:

- 무엇이 삭제예정지를 정하는가
- 세렌이 지방 소거를 늦췄다는 전체 기능
- 개혁가가 출발 인장 구조를 어떻게 알았는가 — E016 훅의 자리
- 삭제된 증언자의 정체, E014 서명자의 정체
- 19만 모델의 최종 오류구조
- 조작 주체가 어느 기관인가

Final hook:

- 개혁가의 실험기록에 **에이든의 출발 인장 구조**가 그려져 있다
- 의미: 미래에서 온 요원의 존재 조건이 이미 이 시대 자료 안에 있다
- 금지: 개혁가를 시간여행자로 만들기, 새 시간법칙 추가, 인장 기능을 이 회차에서 설명, E005 훅처럼 ‘다른 이름이 비친다’ 방식 반복

## 7. POV / Storycraft

근거: canon-constitution OPERATIONAL LOCKS, secondary-POV 배치표 §4 (E015 배정 없음 / 다음 보조 POV는 E016 리아), scene-density-map E015 행.

- POV: 에이든 단일 근접 3인칭
- Scene Density: **S형 3장면** — 배정 사유: 외곽 관찰·잠입·명단실 확인의 표준 잠입 3장면
- Primary craft: 이중 판독 가능한 무대 — 관찰자가 옳게 읽어도 틀리게 결론 낸다
- Secondary A: 갈라지는 동행 — 같은 공간, 다른 우선순위
- Secondary B: 오답의 대칭 — 해석이 뒤집혀도 상대가 결백해지지 않음
- Hook: H2 정보 역전
- Reader reward: 자기가 에이든과 함께 내린 결론이 무너지는 경험. 그러나 안도가 아니라 더 큰 불안으로 끝남

## 8. Scene Values

### Scene 1 — 은신처 외곽 관찰

- Entry: 문서가 답을 주지 못했으니 현장이 판별해 준다
- Evidence: 환자 이동량, 병상보다 많은 마력기구, 통제된 봉인실
- Exit: 실험시설이라는 해석이 성립하고 잠입 결정이 내려진다

### Scene 2 — 두 갈래 통로

- Entry: 같은 목적지로 들어가면 같은 것을 본다
- Evidence: 아이리스는 환자 탈출로를, 에이든은 증거실을 우선한다. 두 통로가 보여주는 시설의 얼굴이 다르다
- Exit: 동행이 갈라지고, 에이든이 보는 시설은 점점 실험실로 보인다

### Scene 3 — 명단실

- Entry: 감염자 명단이 실험 대상 목록일 것이다
- Evidence: 명단은 삭제예정지 주민과 족보 목록이다. 동시에 옆 기록에는 동의 없는 기억채취 항목이 있다
- Exit: 해석은 뒤집히지만 개혁가는 결백해지지 않고, 실험기록에서 에이든 자신의 출발 인장 구조가 발견된다

## 9. Anti-Repeat

- **E013·E014가 실내 문서 회차였으므로 E015는 몸·공간·동시행동으로 압박한다.** 문서를 읽는 장면은 마지막 장면 하나로 제한한다
- E010의 분류대 반복 금지 — 성당 기사단이 환자를 별도 수레에 싣던 장면과 같은 구도를 개혁가 측으로 옮겨 재연하지 않는다
- E009의 ‘진품 문서 두 장’ 구조 반복 금지
- E001의 삭제된 글자 훅, E013의 미래 날짜 훅, E014의 죽은 이의 서명 훅과 같은 형태를 반복하지 않는다. E015의 훅은 **도면**이다
- E005의 ‘출발 인장에 다른 이름이 비친다’ 방식 반복 금지 — 여기서는 이름이 아니라 구조도이며, 비치는 것이 아니라 누군가 손으로 그린 것이다
- 아이리스가 위기의 에이든을 구해 주는 전개 금지 — 두 사람은 각자 자기 목표를 완수한다
- ‘사실 개혁가는 완전히 결백했다’ 반전 금지 — 기억채취는 실재한다
- 전투로 국면을 정리하지 않는다. Arc 01의 Anti-Repeat 규칙이 V1 전체에 적용된다

## 10. Active State / Props

- 삭제예정지 주민·족보 명단
- 동의 없는 기억채취 기록
- 개혁가의 실험기록과 그 안의 출발 인장 구조도
- 봉인실과 마력기구 — 기능 확정은 하지 않음
- 아이리스가 확보한 환자 탈출로
- E014의 보호된 기록 사본 — 배경 유지
- E011 기록상자의 미래 날짜 문서 — 봉인 유지

출발 인장 구조도가 E016에서 개혁가의 인지 근거로 재등장하므로 A10이 prop/relic 등급을 판정한다.

## 11. State Mutation Plan

E015 종료 시 기록:

- 은신처의 기능 판정 상태 — 병원·대피소·기억채취 시설의 복합
- 삭제예정지 명단의 확보 여부와 범위
- 동의 없는 기억채취 사실의 등록 — 세렌 유죄 요소로 유지
- 에이든의 표적 해석 변화 — ‘재앙 확산자’ 해석 붕괴, 무죄 판단은 없음
- 아이리스가 확보한 환자 탈출로와 그 사실을 에이든이 아는지 여부
- 출발 인장 구조도 노출 상태와 E016 인지 근거로의 이월
- 아이리스 조건(귀환표식 차단)의 위반 여부 판정

## 12. Ready Verdict

- Authority: RESOLVED
- Domain Readiness: READY WITH GAPS
- Storycraft companion: REQUIRED / [`E015-storycraft-manifest.md`](../../../docs/10_story_architecture/craft-manifests/E015-storycraft-manifest.md)
- POV: READY (보조 POV 배정 없음. 다음 배정은 E016 리아 세른)
- S0: 0
- S1: 2

S1 gaps:

1. `기억채취`의 정본 절차·부작용·동의 요건이 어느 systems 문서에도 정의돼 있지 않다. v01 E015·E017이 행위만 규정한다. 원고에서 묘사 수위를 정하려면 A08·A16 확인 필요
2. 은신처의 정식 장소명이 v01에 없다. crosswalk V01 1C 주무대는 `두 역사의 라베른`·`절검의 언덕`이며 은신처가 그 둘 중 하나인지 별개 건물인지 미확정. A13 확인 필요

E015 Storycraft Manifest 확인 및 gaps 2건 판정 뒤 A18 호출 가능.
