# Episode Context Pack — E029

Status: D10 READY  
Episode: E029  
Title: 더 많은 생존자  
Compiled By: A21 Context Pack Compiler  
Reference: `agent/2a-identity-in-f1`

> 이 CP는 정본이 아니다. 충돌 시 원본 정본과 권한계층을 따른다. 각 항목의 출처는 절마다 표시한다.

## 1. Authority / Architecture

Required sources:

- [`/AI_PROJECT.md`](../../../AI_PROJECT.md)
- [`docs/00_project/canon-constitution-v1.md`](../../../docs/00_project/canon-constitution-v1.md)
- [`docs/00_project/canon-naming-pack-v1.md`](../../../docs/00_project/canon-naming-pack-v1.md)
- [`docs/00_project/terminology-and-addressing-clarification-v1.md`](../../../docs/00_project/terminology-and-addressing-clarification-v1.md) — §1·§2
- [`docs/00_project/decision-log.md`](../../../docs/00_project/decision-log.md) — DEC-016·017·018·020·021
- [`docs/10_story_architecture/subacts/V02-2A.md`](../../../docs/10_story_architecture/subacts/V02-2A.md) — 이 구간 허브
- [`docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md`](../../../docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md) — Volume 02 머리, E029 행
- [`docs/10_story_architecture/detail/v02-scene-ready-design-v1.md`](../../../docs/10_story_architecture/detail/v02-scene-ready-design-v1.md) — Arc 03 / Subact 2A / E029 절
- [`docs/10_story_architecture/subact-causal-matrix-v1.md`](../../../docs/10_story_architecture/subact-causal-matrix-v1.md) — 2A 행
- [`docs/10_story_architecture/scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) — V2 E029 행
- [`docs/10_story_architecture/location-world-crosswalk-v1.md`](../../../docs/10_story_architecture/location-world-crosswalk-v1.md) — V02 2A
- [`docs/10_story_architecture/secondary-pov-and-offscreen-action-allocation-v1.md`](../../../docs/10_story_architecture/secondary-pov-and-offscreen-action-allocation-v1.md) — V2 E028 행
- [`.agent/context-packs/episodes/E025-context-pack.md`](E025-context-pack.md) — V1 종료 상태
- [`docs/01_timeline/future-state-checkpoints-v1.md`](../../../docs/01_timeline/future-state-checkpoints-v1.md) — F1 행
- [`docs/01_timeline/master-chronology-and-aging-ledger-v1.md`](../../../docs/01_timeline/master-chronology-and-aging-ledger-v1.md) — §1·§3 V2
- [`docs/02_world/demographic-and-scale-ledger-v1.md`](../../../docs/02_world/demographic-and-scale-ledger-v1.md) — §5 F0/F1 행, §6 회색 재앙, §8 수치 표현 규칙
- [`docs/05_characters/cast-canon-index-v2.md`](../../../docs/05_characters/cast-canon-index-v2.md) — C01·C02·C04·C07·C11, §6
- [`docs/05_characters/character-state-checkpoints-v1.md`](../../../docs/05_characters/character-state-checkpoints-v1.md) — E025 열, Continuity Locks
- [`docs/05_characters/hubs/C01-에이든-로엔.md`](../../../docs/05_characters/hubs/C01-에이든-로엔.md)
- [`docs/05_characters/hubs/C04-마르칸-베르.md`](../../../docs/05_characters/hubs/C04-마르칸-베르.md)
- [`docs/05_characters/hubs/C07-다렌-모트.md`](../../../docs/05_characters/hubs/C07-다렌-모트.md)
- [`docs/05_characters/hubs/C11-테온-리브.md`](../../../docs/05_characters/hubs/C11-테온-리브.md)
- [`docs/05_characters/voice-relationship-state-bible-v1.md`](../../../docs/05_characters/voice-relationship-state-bible-v1.md) — §2·§3·§5
- [`docs/08_institutions/institution-org-procedure-bible-v1.md`](../../../docs/08_institutions/institution-org-procedure-bible-v1.md) — §12.1, 금지 모순
- [`docs/09_collection/asset-state-checkpoints-v1.md`](../../../docs/09_collection/asset-state-checkpoints-v1.md) — §2 V2열, §3
- [`docs/11_mystery/mystery-reinforcement-ladder-v1.md`](../../../docs/11_mystery/mystery-reinforcement-ladder-v1.md) — M01~M17, §4
- [`docs/12_losses/permanent-loss-lock-v1.md`](../../../docs/12_losses/permanent-loss-lock-v1.md) — L001·L002·L009
- [`.agent/skills/sentence-narrator/pronunciation-lexicon.md`](../../skills/sentence-narrator/pronunciation-lexicon.md)

Episode function — 출처: 레지스트리 E029 행 / V02 설계 E029 절 / 인과행렬 2A행:

- Grand Act: GA I — 잘못된 치료
- Volume: V2 — 내가 모르는 나의 영웅담
- Subact: 2A — 내가 하지 않은 공적
- Beat: 2A · 대항 세력
- Goal: F1 지휘관이 실제로 더 많은 생존자를 보여준다
- Opposition: F1 체제는 선전만이 아니라 실제 효율과 생존 성과가 있다 (설계 Opposition Benefit)
- Choice: 에이든은 즉시 체제 전복을 시도하지 않는다 / 즉시 적대하지 못한다
- Cost: 2A 전체의 비용은 `F0를 주장할수록 정신오염자로 분류`이며, E029 단독 비용은 정본에 별도 명시가 없다 `[설계 미정]`
- State Change: `F1은 내가 만든 오류다`가 `F1은 실제로 사람을 더 살렸고, 그 대가는 다른 곳에 있다`로 바뀐다
- Hook (레지스트리): 서부 재앙 발생일이 20년 앞당겨졌다
- Hook (V02 설계 Hook): 앞당겨진 첫 발병지는 개혁가의 사망지가 아니다

두 Hook의 조정: `재앙 20년 조기화`는 [`future-state-checkpoints-v1.md`](../../../docs/01_timeline/future-state-checkpoints-v1.md) F1 행에 이미 확정된 상태값이므로 Scene 3에서 **에이든이 처음 확인하는 사실**로 배치하고, 종료 훅은 설계대로 `첫 발병지가 개혁가의 사망지가 아니다`로 둔다. 조기화 자체는 결과이고, 훅의 새 정보는 **위치 불일치**다.

## 2. E028 Carryover

출처: V02 설계 E027·E028 절 / [`secondary-pov-and-offscreen-action-allocation-v1.md`](../../../docs/10_story_architecture/secondary-pov-and-offscreen-action-allocation-v1.md) V2 E028 행 / V02-2A 허브.

- 에이든은 기록소에서 F0 문서 배열 암호를 썼다. 공개 대화가 감시된다는 전제는 유지된다
- 리아 세른은 암호에 반응했으나 세부 기억 일부가 에이든과 다르다. 그는 에이든의 기억을 정답으로 인정하지 않고 상호 검증을 요구했다
- 리아의 일지에는 에이든이 개혁가를 **두 번** 만났다고 적혀 있고, 두 번째 만남 날짜가 에이든의 출발 전날이다. 에이든은 이 모순을 해소하지 못한 채 들고 있다
- 리아 자신도 F0가 원본이라는 확신이 없다 (E028 보조 POV 공개상한)
- E027에서 F0를 주장할 경우의 기억오염 격리·권한정지 법조항을 고지받았고, 신분국에 전 동선이 기록된다
- E027 Cost: F1 친구가 에이든이 감추는 것이 있음을 알아챘다
- E026에서 확인한 숙청 명단 첫 줄에 Era N에서 그가 구했던 환자의 이름이 있다
- 2A Irreversible Choice는 유지된다 — 에이든은 F0 공개주장을 보류하고 영웅 신분을 이용한다

## 3. Time / Location

출처: 마스터 연대기 §1·§3 / 위치교차표 V02 2A / V02-2A 허브 동선 / V02 설계 E029.

- Era: F1, 건국력 CY 664. E028 직후
- 에이든: 41세. V2 구간은 주관적 41일이며 E029의 구간 내 정확한 경과일은 정본 미지정 `[설계 미정]`
- 무대: F1 왕관수도 — 2A 주무대는 `F1 왕관수도·영웅회랑`이며 기능은 공식서사·배급·군정 효용
- 2A 동선상 E029의 세 지점 (허브 §무대):
  1. 생존구역 시찰 — F0에서는 폐허였던 병원·곡창·주거구
  2. 지휘관 브리핑 — 방위지휘부 주관
  3. 재앙 연대표 확인
- 최후 연대국은 **한 지하 시설 안에서** 운영된다 (institution §12.1). 이동은 그 시설과 그 관할 생존구역 범위 안이며 Era N으로 나가지 않는다
- 위 세 지점의 **정식 시설명은 정본에 없다** `[설계 미정]`. 새 시설명을 만들지 않는다

## 4. 반대편의 이익 — F1이 실제로 살린 것

출처: [`demographic-and-scale-ledger-v1.md`](../../../docs/02_world/demographic-and-scale-ledger-v1.md) §5·§6·§8 / [`future-state-checkpoints-v1.md`](../../../docs/01_timeline/future-state-checkpoints-v1.md) F1 행 / institution §12.1 / V02 설계 E029 Opposition Benefit.

허용 사실:

- F0 생존 인구 **42만**, F1 생존 인구 **61만**이다. F1은 F0보다 더 많은 현재 생존자를 **실제로** 살렸다
- 같은 표가 F1을 `군정 효율로 생존 증가, 지방·움브라 제외 심화`로 규정한다. 늘어난 것과 빠진 것이 한 줄에 같이 있다
- 군정은 미등록자를 제외해 생존률을 높게 보일 수 있다 (§8 수치 표현 규칙). 자료가 거짓이어서가 아니라 **세는 대상이 정해져 있어서** 그렇다
- F1 상태 정본에 `재앙 20년 조기화`가 포함된다. 전체 생존은 늘고 재앙 시작은 앞당겨졌다는 두 사실이 동시에 성립한다
- 회색 재앙 관련 정본 수치는 §6의 것뿐이다 — Era N 초기 확인 환자 약 4만, 잠재 주소불일치자 20만~35만. F1 시점의 별도 재앙 수치는 정본에 없다 `[설계 미정]`
- 방위지휘부는 구조·군사·생존배분 실무 지휘기관이며 마르칸 베르가 수장이다. 선별실은 그 산하 생존 예측 부서이고 **결정권이 없다**
- 최후 연대국은 Era N의 7개 분산 권한을 형식상 유지하지만 한 시설에 모여 있어 견제가 약하다. 이것이 F1 중앙 독점의 구조적 원인이다

금지 — 이 회차에서 하면 안 되는 것:

- **F1이 F0보다 `더 나은가`를 판정하기.** 2A는 차이만 체감시킨다 (E026 Information Ceiling, 2A 허브 금지표)
- F1 체제를 선전만으로 그리기. 실제 효율과 생존 성과가 있다
- 마르칸을 최종 흑막·단순 최종악역·독재자 한 단어로 축소, 고함치는 군사독재자 말투 (C04 허브 §8)
- 단일 지도자가 전권을 쥔 군사독재 묘사. 정족수 원칙은 축소된 형태로 유지된다 (§12.1)
- 기관장 한 명이 전체 실무자를 대표하거나 서명 한 번으로 절차를 생략하기 (institution 금지 모순)
- 선별실에 결정권을 주기. 선별실은 부서이고 생존선별파는 정치 세력이다 — 이 회차에서 둘을 같은 것으로 쓰지 않는다 (terminology §2)
- 미래 충격 뒤 즉시 도주·전복 시도. 법·의학·기록 절차 안에서 증거를 모은다 (Arc 03 Anti-Repeat)
- 리아 한 명의 증언, 또는 다렌 한 명의 증언으로 진실을 확정하기 (미스터리 §4, C07 허브 §4)
- 20년 조기화의 **원인**을 이 회차에서 확정하기. 개혁가 사망과 재앙 가속의 인과 확정은 E072다
- 2B 이후 자산 선취 — 회색 종(R01)·절검(R03)·F0 귀환패(R04)·빈 세금장부(R02)는 이 구간 미등장이다
- E030·E031의 사건 선취 — 친구의 가족·가족사진, 접근심사, 정신오염 정밀검사 명령
- 폐기명 사용 — `연대출귀원`·`성력국`·`중앙관측탑연합`·`무명종`·`잔문감사실`·`아르켄 관측탑` (DEC-016·017·018)
- 성 단독 호칭 — `로엔`·`베르`·`모트`·`리브` 단독 (DEC-018). `베르 사령관`은 되고 `베르`는 안 된다
- `방위총감`(E001 F0 기능인물)과 마르칸 베르를 병합하기

## 5. Character State

출처: cast-canon-index-v2 §2·§6 / character-state-checkpoints E025 열·Continuity Locks / 인물 허브 C01·C04·C07·C11 / voice bible §2·§3·§5 / V02-2A 허브 인물표.

### 에이든 로엔 (C01)

- 이 회차의 상태: **F1 영웅 / 기억 이방인** (E025 체크포인트). 기억 혼선을 숨기고 영웅 역할을 연기하는 중이다
- 목표: F1 지휘관을 적으로 규정하려 하지만, 그 전에 현재 성과를 확인해야 한다 (설계 Entry)
- 이 회차의 행동: 자료와 현장을 대조하고, 반박이 성립하지 않는 지점을 스스로 확인한다
- 오류 가능성: 출발 미래(F0)를 `원래 세계`로 특권화한다. 이 편향은 아직 깨지지 않는다
- 말투: `목표 → 출구 → 비용` 순서. 죄책감이 오면 이름을 버리고 역할명(`표적·환자·요원`)으로 후퇴한다
- 정보상한: 변화한 미래의 개인관계, 복원 결과의 완전한 예측, 본부 기록 조작의 주체, 새 미래 전체를 모른다. 기억상태는 `DECAYING`이며 **잘못된 확신**을 가질 수 있다
- 금지: 즉석 폭로·전복·도주, 시간선 변경의 원리를 스스로 정리해 명명, 연설 한 번으로 세력을 돌려세우기, `로엔` 단독 호칭

### 마르칸 베르 (C04)

- 이 회차의 상태: **첫 핵심권 진입**. F1 방위사령관, 합리적 상관 (E025 체크포인트)
- 이 회차의 기능: 생존구역·수치 자료를 제시하고, **이상 징후를 은폐한다** (2A 허브 인물표)
- 단위: 61만 시민·배급량·방어선·제한시간. 반박이 오면 개인을 총량으로 갈아 끼운다. 이것은 죄책감이 아니라 직무다
- 사적 장면에서는 부하의 **이름과 가족상태**를 놀라울 정도로 기억한다. 총량으로 말하는 사람이 그렇다는 것이 반전이 된다
- 에이든에게: 영웅 호칭과 위험인물 호칭을 의도적으로 번갈아 쓴다. 에이든을 **체제자산**으로 취급한다
- 이 인물이 모르는 것: 계산 밖 주소상실자 총수 / F0의 사적 관계 진실 / 중앙정지 뒤 지역자치의 가능성
- 금지: 최종 흑막 지목, 정치적 악역화, 고함 화법, 가족·개인 상실을 근거로 한 단순 복수자 축소, `베르` 단독 호칭, E298–E299 사망(L009)의 선취 암시

### 리아 세른 (C02)

- 이 회차의 상태: **F0 파편 보존자** (E025 체크포인트). E028에서 상호 검증을 요구한 상태가 유지된다
- **E029 장면 배정이 정본에서 어긋난다.** 보조 POV 배치표는 E028의 재진입을 `E029 에이든과 증거범위 협상`으로 적지만, V02 설계 E029 카드와 2A 허브 동선에는 리아 장면이 없다. 이 CP는 설계 카드를 우선해 **E029 등장을 확정하지 않는다** `[설계 미정]` → `gaps`
- 등장시키더라도 금지: 기억 대조 재연(E028 소비), 예언자 말투, 정답 선취, 리아 증언 한 건으로 F1 자료를 무효화하기

### 다렌 모트 (C07)

- 이 회차의 상태: **에이든의 오랜 전우로 존재하나 에이든은 기억하지 못한다**. E027에서 에이든이 감추는 것이 있음을 알아챈 상태다
- **E029 장면 배정 없음** `[설계 미정]`. 그의 회차는 E030이며, 생활 세계·가족·가족사진은 E030 자산이다
- 등장시키더라도 금지: 관계 회복의 진전 선취, 악역·추종자·감시자 연출, 가족을 협상 카드로 사용, F0 소속 노출(E030 사항)

### 테온 리브 (C11)

- 이 회차의 상태: 마탑 계산원. **첫 핵심권 V2** — V2에서 에이든의 정신오염 판정에 계산상 이의를 제기한다
- **2A 등장 회차가 정본 미지정** `[설계 미정]`이며 E029 배정 근거가 없다. 이 CP는 등장을 확정하지 않는다
- 등장시키더라도 금지: 에이든에게 편리한 해킹키 제공, 무표정 천재 연출, 숫자 하나로 윤리문제를 닫기, 한 장면 설명용 단역 소모, `리브` 단독 호칭

### 생존구역 실무자 / 브리핑 배석자

- 정본에 개별 인물 지정이 없다 `[설계 미정]`. 기능인물로만 다루고 **새 고유명·새 개인 이름을 만들지 않는다**
- 금지: 얼굴 없는 체제 대변자로만 처리, 개인 악역 지정, 기관장 한 명이 실무자 전체를 대표하기

## 6. Mystery / Information Ceiling

출처: [`mystery-reinforcement-ladder-v1.md`](../../../docs/11_mystery/mystery-reinforcement-ladder-v1.md) §2·§4 / V02-2A 허브 §활성 미스터리 / voice bible §5.

Active mysteries:

- **2A 국소 미스터리** — 에이든이 하지 않은 학살과 두 번째 표적 접촉은 **누가 기록했는가**. E029는 이 질문을 해소하지 않는다
- **2A 국소 단서 — 앞당겨진 재앙**: E029에서 첫 발병지가 개혁가의 사망지가 아니라는 사실만 놓는다
- M01 마나열병은 전염병인가 — 사다리 칸은 E026이며 **E029 칸은 없다**. 새 단서를 추가하지 않는다
- M02 세렌 바일은 왜 창시자로 기록됐는가 — 사다리 칸은 E014·E033·E061·E072다. **E029 칸은 없다**. 재앙 조기화를 개혁가의 실제 기능과 연결하지 않는다
- M14 원래 시간선은 진짜인가 — 사다리 칸은 E027이며 E029 칸은 없다
- 공정성 규칙: 2A에서 독자는 어떤 미스터리의 정답도 확정할 수 없다. 2A는 사다리의 **2단째 단서만** 놓는다

독자가 알아도 되는 것:

- F1의 생존 성과가 실재한다는 것. F0 42만 → F1 61만이며 이 숫자는 조작이 아니다
- 그 계산이 지방·움브라·미등록자를 제외한 위에 서 있다는 **구조**
- F0에서 폐허였던 병원·곡창·주거구가 F1에서는 운영된다는 것
- 회색 재앙의 시작이 20년 앞당겨졌다는 것
- 앞당겨진 첫 발병지가 개혁가의 사망지가 **아니라는** 것
- 지휘관이 제시하는 자료에 채워지지 않은 칸이 있다는 정황
- 에이든이 즉시 적대하지 못하는 이유가 겁이 아니라 자료라는 것

독자가 아직 몰라야 하는 것 — 이 회차보다 뒤에 배치된 답이다. 서술로도 암시로도 쓰지 않는다:

1. 마나열병이 감염이 아니라 장치·주소 문제라는 것 (M01, 독자 추론 E176)
2. 개혁가가 지방 소거를 늦추고 있었다는 실제 기능 (M02, E072)
3. 개혁가 사망이 재앙을 가속했다는 인과의 확정 (M02, E072)
4. 보고서 날짜층 위조와 책임을 뒤집어씌운 주체 (M02, 독자 추론 E061)
5. 리아가 예언자가 아니라 **손상된 보존자**라는 것 (M03, 독자 추론 E260)
6. F0 귀환좌표가 원래 미래 복원키가 아니라는 것 (M04, 독자 추론 E303)
7. 빈 세금장부가 반역명단이 아니라 희생 분배표라는 것 (M05, 독자 추론 E173)
8. 칼레온 국경 안정이 신의 방벽이 아니라 분산 인프라라는 것 (M06, 독자 추론 E286)
9. 시간장치를 초대왕이 단독 창조하지 않았다는 것 (M07, 독자 추론 E186)
10. 아홉 상처가 사람 명단이 아니라 원리라는 것 (M08, 독자 추론 E190)
11. 몸과 대가에 담당 좌가 없는 이유 (M09, 독자 추론 E286)
12. 육체와 역사주소가 분리된다는 원리 (M10, 독자 추론 E275)
13. 젊은 에이든의 요원 경로가 운명이 아니라 누적된 선택이라는 것 (M11, 독자 추론 E266)
14. 최종 흑막이 한 사람이 아니라 **독점된 선택권**이라는 것 (M12, 독자 추론 E298) — 마르칸을 흑막으로 지목하는 연출을 포함한다
15. 움브라가 다양한 종족의 주소탈락자라는 것 (M13, 독자 추론 E173)
16. F0도 절대 원본이 아니라는 것 (M14, 독자 추론 E220)
17. 한 권의 절대 최초 연대기가 없다는 것 (M15, 독자 추론 E332)
18. 회색 종이 감염·악의가 아니라 주소불일치에 반응한다는 것 (M16, 독자 추론 E092)
19. 최종 감사인장이 버튼이 아니라 절차·권한 묶음이라는 것 (M17, 독자 추론 E344)
20. 하지 않은 학살과 두 번째 표적 접촉을 **누가** 기록했는가의 답 (2A 국소, 2A 내 미해결)
21. 재앙 20년 조기화의 원인 구조와 발병지가 옮겨간 이유
22. 리아의 일지에 적힌 두 번째 만남의 의미와 그 날짜의 해석 (E028 훅의 답)
23. F0 물질 증거의 존재와 성질 — 절검의 F1 미존재 제작자명, 귀환패 파편 (2B, E032–E037)
24. 다렌 모트가 F0에서 적대 세력 문장을 썼다는 사실 (E030 훅)
25. 봉인목록에 `F0`라는 분류명이 이미 존재한다는 것 (E031 훅)
26. 마르칸 베르의 최종 상태 — E298–E299 시민 대피 후 영구 사망 (L009)

## 7. POV / Storycraft

출처: 밀도지도 V2 E029 행 / DEC-021 / 보조 POV 배치표 / V02 설계 E029.

- POV: 에이든 단일 근접 3인칭. 보조 POV 배치표에 **E029 배정이 없다**
- **Scene Density: S · 3장면** — 밀도지도 사유: 생존구역 시찰·지휘관 브리핑·재앙 연대표 확인으로 F1의 실제 성과를 검증하는 조사 3장면
- V02 설계의 기능 비트 3개와 실제 장면 수가 1:1로 대응하는 회차다 (DEC-021 해석 규칙)
- Primary craft: 반박할 수 없는 반대편의 자료
- Secondary A: 총량과 단위의 충돌 — 61만 대 한 사람
- Secondary B: 좋은 소식 안에 들어 있는 나쁜 소식
- Hook: H2 정보 역전
- Reader reward: 주인공이 적을 미워하지 못하게 되는 경험. 그리고 그 자료가 옳다는 사실이 훅의 무게를 만든다

## 8. Scene Values — 3장면

### Scene 1 — 생존구역 시찰

- Entry: 이 미래는 내가 만든 오류다
- Action: F0에서는 폐허였던 병원·곡창·주거구가 운영되는 것을 직접 본다. 에이든은 F0의 같은 자리를 기억하고 있고, 두 그림이 겹치지 않는다
- Exit: 오류라고 부르려면 지금 눈앞의 운영을 부정해야 한다

### Scene 2 — 지휘관 브리핑

- Entry: 성과가 있어도 근거는 다를 것이다
- Action: 마르칸이 개혁가 제거와 서부 통제 강화로 수십 년간 더 많은 인구가 살아남았다는 자료를 제시한다. 그는 총량 단위로 말하고, 자료는 실제로 맞는다. 동시에 채워지지 않은 칸이 있다
- Exit: 에이든은 반박할 근거를 찾지 못하고, 즉시 적대하지 않기로 한다

### Scene 3 — 재앙 연대표

- Entry: 늘어난 생존자가 이 체제의 전부다
- Action: 전체 생존은 늘었지만 회색 재앙의 시작이 20년 앞당겨졌음을 연대표에서 확인한다
- Exit: 선택은 유예되고 질문이 바뀐다. 앞당겨진 첫 발병지가 개혁가의 사망지가 아니다

## 9. Anti-Repeat

- E026의 공적 전시회랑을 반복하지 않는다. E026은 **기록된 서사**가 그를 키웠고, E029는 **실제 운영 성과**가 그를 막는다
- E027의 추모벽 앞 부재 확인을 반복하지 않는다. E029에는 빈자리가 아니라 채워진 자리가 있다
- E028의 두 사람 대조 심문 구도를 반복하지 않는다. E029의 대조는 사람 대 사람이 아니라 **자료 대 기억**이다
- E025의 명부 검색으로 상실을 확인하는 구조를 되살리지 않는다
- 세 장면을 모두 문서 검토로 채우지 않는다. 1장면은 현장, 2장면은 사람, 3장면은 문서다 (E003·E018 반복 회피)
- E020의 분 단위 카운트다운식 압박을 재연하지 않는다. E029의 숫자는 줄어드는 시간이 아니라 **늘어난 사람 수**다
- 낯선 미래를 폐허·디스토피아 몽타주로 소개하지 않는다 (E025 규칙 유지). F1은 더 살아 있고 더 정상적이다
- 마르칸을 얼굴 없는 체제 대변자나 개인 악역으로 처리하지 않는다
- E030의 생활 세계 체감과 가족사진, E031의 접근심사·의료명령을 선취하지 않는다
- 재앙 조기화를 에이든의 자책 독백으로 닫지 않는다. 책임 인정은 3B 이후의 것이다
- `내가 잘못했다`류의 결론 선언으로 회차를 끝내지 않는다. 이 회차는 질문이 바뀌는 회차다

## 10. Active State / Props

출처: [`asset-state-checkpoints-v1.md`](../../../docs/09_collection/asset-state-checkpoints-v1.md) §2 V2열·§3 / V02-2A 허브 §활성 아이템 / E025 CP §10.

- **재앙 연대표** (E029) — 회색 재앙 시작이 20년 앞당겨진 것이 기입된 문서. 이 회차의 중심 물건
- 생존구역 운영·배급 수치 자료 — 마르칸이 제시하는 것. 자료 자체는 진짜다
- 숙청 명단 (E026) — 배경 유지. 이 회차에서 다시 펼치지 않는다
- 서부 희생자 추모벽 (E027) — 배경 유지
- 문서 배열 암호 / 리아의 일지 (E028) — 인지 상태로 유지. 이 회차에서 재대조하지 않는다
- 귀환석 — 균열 상태 유지 (E025 Exit Ledger)
- 회색 종 (R01) — V2 코드 **E**. F1 재료검사실에 파편 기록만 존재하며 **회차 근거는 2B(E032)**. E029 미등장
- 개혁가의 절검 (R03) · F0 귀환패 (R04) · 빈 세금장부 (R02) — **이 구간 미등장**. 근거 회차는 E032 이후
- 가족사진 (E030) · 봉인목록 (E031) — 이 회차에서 등장시키지 않는다

## 11. State Mutation Plan

E029 종료 시 기록한다.

- 에이든이 확인한 F1 생존 성과의 범위와 그가 반박하지 못한 항목
- 마르칸이 제시한 자료 항목과 **채워지지 않은 칸**의 목록
- 회색 재앙 20년 조기화의 에이든 인지 확정
- 첫 발병지와 개혁가 사망지의 불일치 — 에이든의 인지 범위를 `위치가 다르다`까지로 고정하고 원인은 미판정으로 둔다
- `즉시 체제 전복을 시도하지 않는다`는 선택의 등록
- 마르칸 베르와의 관계 개시 상태 — 영웅과 지휘관, 체제자산 취급
- 2A Irreversible Choice(F0 공개주장 보류) 유지 여부
- 리아·다렌·테온의 E029 등장 여부 판정 결과 — 현재 `[설계 미정]`

## 12. Ready Verdict

- Authority: RESOLVED
- Domain Readiness: READY
- Storycraft companion: REQUIRED / `docs/10_story_architecture/craft-manifests/E029-storycraft-manifest.md`
- POV: READY — 보조 POV 배정 없음, 단일 POV
- Scene Density 일치: PASS — S · 3장면 / 설계 기능 비트 3개
- Permanent Loss: 이 회차에 신규 잠금 없음. L001·L002는 확정 상태로 배경 유지
- S0: 0
- S1: 5 (§gaps 참조)

E029 Storycraft Manifest와 E028 상태 확인 뒤 A18 호출 가능하다.

## gaps

정본에서 도출할 수 없어 이 CP가 확정하지 않은 항목이다. 임의 창작하지 않았다.

1. **S1 — 리아 세른의 E029 배정 충돌.** `secondary-pov-and-offscreen-action-allocation-v1.md` V2 E028 행의 Re-entry가 `E029 에이든과 증거범위 협상`인데, `v02-scene-ready-design-v1.md` E029 카드와 V02-2A 허브 동선에는 리아 장면이 없다. 이 CP는 설계 카드를 우선해 등장을 확정하지 않았다. A11·A12 판정 필요.
2. **S1 — E029 단독 Cost 부재.** 인과행렬은 2A 전체의 Cost만 규정하고, 레지스트리·설계 어느 쪽도 E029의 회차 단위 비용을 적지 않는다. Scene 3이 훅으로 끝나므로 비용 장면을 창작하지 않았다.
3. **S1 — 세 장면 지점의 정식 시설명.** `생존구역`·`지휘관 브리핑` 장소·`재앙 연대표` 열람 지점의 시설명이 정본에 없다. `location-world-crosswalk-v1.md`는 2A 주무대를 `F1 왕관수도·영웅회랑`으로만 규정한다.
4. **S1 — F1 시점 회색 재앙 수치.** `demographic-and-scale-ledger-v1.md` §6은 Era N 기준 수치만 규정한다. `20년 앞당겨졌다`의 기준 연도와 F1에서의 환자·사망 수치가 정본에 없다.
5. **S1 — 개혁가 사망지의 정식 지명.** E023 CP가 이미 등재한 미해결이다. `좁은 기록실`과 `절검의 언덕`을 동일 장소로 명시한 정본이 없다. E029 훅이 `사망지`를 대조 대상으로 쓰므로 이 회차에서 처음으로 지명이 필요해질 수 있다. 상위 판정 필요.
6. **V2 권 제목 표기 불일치.** 레지스트리·V02 설계는 `내가 모르는 나의 영웅담`, `location-world-crosswalk-v1.md`는 `영웅의 기록과 사라진 친구`로 적는다. 이 CP는 레지스트리를 따랐다. 원고 영향 없음.
7. **테온 리브의 2A 등장 회차.** C11 허브와 V02-2A 허브 모두 `[설계 미정]`으로 등재한 기존 공백이다. E029 배정 근거가 없어 등장시키지 않았다.
