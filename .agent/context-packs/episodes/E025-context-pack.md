# Episode Context Pack — E025

Status: D10 READY  
Episode: E025  
Title: 내가 모르는 영웅  
Compiled By: A21 Context Pack Compiler  
Reference: `agent/1d-subact-context-packs`

> 이 CP는 정본이 아니다. 충돌 시 원본 정본과 권한계층을 따른다.

## 1. Authority / Architecture

Required sources:

- [`/AI_PROJECT.md`](../../../AI_PROJECT.md)
- [`docs/00_project/canon-constitution-v1.md`](../../../docs/00_project/canon-constitution-v1.md) — IMMUTABLE 4·5·8, Memory Rule
- [`docs/00_project/canon-naming-pack-v1.md`](../../../docs/00_project/canon-naming-pack-v1.md) — §5 C01·C02·C07, §6
- [`docs/00_project/terminology-and-addressing-clarification-v1.md`](../../../docs/00_project/terminology-and-addressing-clarification-v1.md)
- [`docs/00_project/decision-log.md`](../../../docs/00_project/decision-log.md) — DEC-016·017·018·020·021
- [`docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md`](../../../docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md) — E025 행, Exit-State Lock
- [`docs/10_story_architecture/detail/v01-scene-ready-design-v1.md`](../../../docs/10_story_architecture/detail/v01-scene-ready-design-v1.md) — E025 절, Volume Exit State Ledger
- [`docs/10_story_architecture/subact-causal-matrix-v1.md`](../../../docs/10_story_architecture/subact-causal-matrix-v1.md) — 1D
- [`docs/10_story_architecture/scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) — V1 E025
- [`docs/10_story_architecture/secondary-pov-and-offscreen-action-allocation-v1.md`](../../../docs/10_story_architecture/secondary-pov-and-offscreen-action-allocation-v1.md) — §2 P2, §5 E025
- [`docs/10_story_architecture/location-world-crosswalk-v1.md`](../../../docs/10_story_architecture/location-world-crosswalk-v1.md) — V01 1D
- [`docs/01_timeline/future-state-checkpoints-v1.md`](../../../docs/01_timeline/future-state-checkpoints-v1.md) — F1 행
- [`docs/05_characters/cast-canon-index-v2.md`](../../../docs/05_characters/cast-canon-index-v2.md) — C01·C02·C07
- [`docs/05_characters/character-state-checkpoints-v1.md`](../../../docs/05_characters/character-state-checkpoints-v1.md) — E025 열
- [`docs/05_characters/voice-relationship-state-bible-v1.md`](../../../docs/05_characters/voice-relationship-state-bible-v1.md) — §2, §3, §2-A C07
- [`docs/12_losses/permanent-loss-lock-v1.md`](../../../docs/12_losses/permanent-loss-lock-v1.md) — L002, LR
- [`docs/11_mystery/mystery-reinforcement-ladder-v1.md`](../../../docs/11_mystery/mystery-reinforcement-ladder-v1.md) — M03·M14·M16
- [`.agent/context-packs/episodes/E024-context-pack.md`](E024-context-pack.md)

Episode function:

- Grand Act: GA I — 잘못된 치료
- Volume: V1 — 회색 종이 울리는 날
- Subact: 1D — 표적 제거와 귀환
- Beat: 후폭풍 / 권말
- Goal: 첫 변형 미래를 즉시 보상으로 제시한다 (registry E025)
- Opposition: 보상이 실제로 크다는 사실. 더 많은 사람이 살아 있고, 그를 맞는 사람들의 호의가 진심이다
- Choice: 에이든은 F1의 영웅 대우를 거부하지 않고 받는다. 대신 사라진 이름들을 혼자 확인한다
- Cost: F0 지휘관·동료 관계 다수 소실 — 사망이 아니라 부재 (`LOCK` L002)
- State Change: F1이 현재 현실이 되고, 에이든은 국가 영웅이자 기억 이방인이 된다 (`character-state-checkpoints` E025)
- Hook: 낯선 친구가 그를 평생의 전우라 부른다 (registry E025)
- Final Image: 회색 종이 없는 미래 본부에서 에이든의 귀환석만 혼자 운다 (`V01` E025)

## 2. E024 Carryover

### 에이든 로엔

- 절검과 소거명부 일부를 동반 등록해 반입했다. 나머지 원본은 Era N에 남겼다
- 임무 성공 판정을 자기 이름으로 수령했다
- 아이리스 네르에게 용서받지 못한 채 갈라졌고, ‘명단을 잊지 말 것’이라는 요구만 받았다
- 통과 직전, 좌표 표시의 명칭이 출발 본부와 달랐고 출발 인장에서 F0 동료 이름이 사라졌다. 그는 장비 오류로 처리했다

### 시간선

- 세렌 바일 영구 사망(L001)이 인과 결속과 동기화 경계를 통과해 현재 확정 단계에 들어갔다 (`master-chronology` §5)
- F1 트리거: E023 표적 제거 후 E025 귀환 (`future-state-checkpoints` F1)
- 이전 미래는 평행세계로 계속 존재하지 않는다

### 물품

- 절검 (R03) — 반입 등록 완료, 기능·소유권 미확정
- 소거명부 일부 — 누락·오염 포함
- 귀환석 — 3갈래 균열, 수명과 좌표 신뢰도 하락 (`V01` Volume Exit State Ledger)
- 리아의 개인 경고 쪽지 (E005) — 장갑 안쪽 보관 유지

## 3. Time / Location

- Timeline: F1, 건국력 664년 — 귀환 직후
- 에이든: 41세 / 주관적 누적일 V1 종료 시점 24일 (`master-chronology` §3)
- Main locations (X형 6장면):
  1. F1 귀환실
  2. 근무·전몰 명부 단말
  3. 영접·공식 서사 제시 자리
  4. 거주구 통로
  5. 반입품 접수·격리 보관실
  6. 기록관 대조실 — 리아 세른 시점
- 이동은 F1 본부 내부이며 수도 외부로 나가지 않는다. `location-world-crosswalk` V01 1D의 `F1 수도 잔존부` 범위 안이다
- 공적 전시회랑·환영식·의료검사 절차는 E026 담당이므로 E025에서 소비하지 않는다 (`v02-scene-ready-design-v1.md` E026 Entry)
- F0 숙소 자리의 추모벽은 E027 훅이므로 사용하지 않는다. E025는 문서상의 부재만 다룬다

## 4. F1 Arrival State

Sources: `future-state-checkpoints-v1.md` F1 / `V01` E025·Volume Exit State Ledger / `character-state-checkpoints-v1.md` E025 열

### 달라진 것 — 보여 줄 범위

- 본부의 구조·계급·문장이 다르다
- 그를 맞는 인물이 다르다
- 익숙한 동료 이름이 근무명부에도 전몰기록에도 없다. 죽은 것이 아니라 등록된 적이 없다
- 그의 표적 제거가 왕국과 미래를 구한 결정으로 교육돼 있다
- 공식 서사에는 그가 하지 않은 후속 사건이 그의 공적으로 붙어 있다
- 회색 종이 이 본부에 없다

### 달라진 것 — E025에서 확정하지 않을 범위

- 재앙 발생일이 20년 앞당겨졌다는 사실 — E029 훅
- 공적에 포함된 학살 항목의 구체 확인 — E026 훅
- 다렌 모트가 F0에서 적대 세력 문장을 썼다는 확정 — E030 훅
- 리아 세른이 F0를 얼마나 기억하는지 — E028
- F1이 F0보다 더 많은 생존자를 확보했다는 수치 제시 — E029

### 진짜여야 하는 것

- F1 시민은 실재하는 현재의 사람들이며 가짜·환상·연극이 아니다
- 그를 맞는 호의는 연기가 아니다
- F1을 부정하는 것은 살아 있는 사람을 부정하는 일이 된다
- 금지: ‘모든 것이 가짜였다’ 반전, 기억상실 처리, 꿈·환각 처리

## 5. Character State

### 에이든 로엔 (C01)

- 목표: 자신이 아는 이름들이 어디 있는지 확인한다
- 내적 압박: 확인할수록 그가 받은 보상이 커진다
- 습관: 상대의 이름보다 역할·조건을 먼저 확인한다 (`voice bible` §2)
- 오류 가능성: 이 세계가 잘못됐다고 판단하기 전에, 자기 기억이 잘못됐을 가능성을 먼저 계산한다
- 금지: 즉석 폭로 시도, 시간선 변경의 원리를 스스로 정리해 명명, F1 사람들을 가짜라고 부르기 (`voice bible` §4 V4–V6에서야 도달하는 지점)
- 정보상한: 변화한 미래의 개인관계, 복원 결과의 예측을 모른다 (`voice bible` §5)

### 리아 세른 (C02)

- E025 상태: F0 파편 보존자 (`character-state-checkpoints` E025)
- 보조 POV 회차 기능: 첫 귀환 뒤 F1 변화의 외부 후과를 독립적으로 관찰
- 공개상한: 리아도 F0 전체를 모른다 (`secondary-pov` §5 E025)
- 말투: 출처와 확실성 등급을 명확히 하고, ‘기억한다’와 ‘증명할 수 있다’를 구분한다
- 금지: 예언자 말투, 정답 선취, 에이든과의 기억 대조 — 대조는 E028이다
- 이 회차에서 두 사람은 서로를 붙잡고 확인하지 않는다

### 다렌 모트 (C07)

- F1에서 에이든의 오랜 전우로 존재하나 에이든은 그를 기억하지 못한다 (`character-state-checkpoints` C07 V1–V3 칸)
- 과거를 증명하려 애쓰지 않고 현재의 행동과 가족을 보여 준다 (`voice bible` §3)
- 말투: 재회 인사에 안부 대신 오늘의 생활 숫자를 먼저 댄다 — 아이 나이, 배급표 장수, 다음 근무 시각 (`voice bible` §2-A C07)
- 옛일은 한 문장으로 끊고 곧바로 현재 약속으로 갈아탄다
- 금지: 원망조 회상, 교단 구호, 가족을 협상 카드로 사용, 세뇌된 친구 연출

### F1 영접 기능선

- 새 핵심 인물을 즉석 확정하지 않는다. 마르칸 베르는 V2 첫 핵심권이며 E025에서 등장 확정을 하지 않는다 (`cast-canon-index` C04)
- 호의는 진심이고 절차는 합리적이다
- 금지: 감시자·흑막 암시로 장면을 채우기

## 6. Mystery / Information Ceiling

Active mysteries:

- M03 리아는 왜 F0를 기억하는가 — 사다리 첫 칸은 E028이므로 E025는 질문만 세운다
- M14 원래 시간선은 진짜인가 — E027이 사다리 첫 칸. E025는 ‘원래’라는 말이 도덕적 특권이 아님을 감각으로만 심는다
- M16 회색 종은 무엇을 감지하는가 — 종이 없는 곳에서 귀환석이 우는 변형 단서

독자가 알아도 되는 것:

- 시간선은 실제로 바뀌었고 F1이 현재 현실이다
- F0 동료들은 죽은 것이 아니라 기록상 존재한 적이 없다
- 공식 서사가 에이든의 실제 행위보다 크다
- 이 미래에는 회색 종이 없다

독자가 아직 몰라야 하는 것:

- 세렌의 행위가 지방 소거를 늦추고 있었다는 전체 기능
- 기록을 뒤집은 주체와 이유
- 삭제된 증언자의 정체
- 19만 증가 모델의 최종 오류구조
- 무엇이 F0와 F1의 차이를 만들었는지의 인과 전체
- 리아의 기억 보존 원리와 범위
- F0 역시 순수한 원본이 아니라는 사실

Final hook:

- 낯선 친구가 그를 평생의 전우라 부른다
- 의미: 상실이 빈자리가 아니라 채워진 자리로 나타난다. 잃은 것을 알아보려면 새로 생긴 것을 부정해야 한다
- 금지: 그 친구를 수상한 인물로 연출, 에이든이 그를 F0의 적으로 지목, 가족을 감정 인질로 사용

## 7. POV / Storycraft

- POV: **에이든 → 리아** (P2 X형 다중 POV, `secondary-pov` §5 E025 승인 배치)
- 전환 규칙: 전환마다 시간·장소·인물 표식을 분명히 한다. 전환은 1회만 사용한다 (`secondary-pov` §2 P2)
- 리아 시점 상한: 자기 Bible과 정보상한을 넘지 않고, 정답을 먼저 설명하지 않는다
- Scene Density: **X형 5~6장면 → 6장면 설계** (`scene-density-map` V1 E025 — 고정)
- 배정 사유(원문): 권말이자 첫 변형 미래 제시로 낯선 본부·조작된 영웅 서사·낯선 친구의 가족이 동시에 밀려온다
- Primary craft: 보상으로 도착하는 상실
- Secondary A: 부재의 행정적 증명 — 죽음이 아니라 미등록
- Secondary B: 호의의 무게
- Secondary C: 외부 시점 종결 — 주인공이 보지 못하는 장면으로 권을 닫는다
- Hook: H2 정보 역전 + H4 제도변화
- Reader reward: 첫 시간개입의 대가를 설명이 아니라 명부·호칭·가족사진으로 체감

## 8. Scene Values

### Scene 1 — F1 귀환실 (에이든)

- Entry: 돌아왔다. 보고하고 쉬면 된다
- Opposition: 절차·계급·문장이 다르고, 그를 맞는 인물이 다르다
- Turn: 에이든이 F0 동료의 이름을 호명하지만 아무도 그 이름을 모른다
- Exit: 그는 자신이 도착지를 잘못 짚었을 가능성부터 계산한다

### Scene 2 — 근무·전몰 명부 단말 (에이든)

- Entry: 명부를 확인하면 오해가 풀린다
- Opposition: 이름들은 전몰기록에도 없다. 사망 기록이 없는 이유는 등록된 적이 없기 때문이다
- Turn: 그는 사망을 찾다가 부재를 찾게 된다
- Exit: L002 관계 소실이 사실로 확정된다. 애도할 대상이 서류상 존재하지 않는다

### Scene 3 — 영접·공식 서사 (에이든)

- Entry: 이 사람들에게 사정을 설명하면 된다
- Opposition: 그들은 그를 이미 안다. 그의 표적 제거는 왕국과 미래를 구한 결정으로 교육돼 있다
- Turn: 서사가 그가 한 일보다 크다. 그가 하지 않은 뒷일까지 그의 공적로 붙어 있다
- Exit: 정정하려면 자신이 죽인 사람의 이름을 다시 꺼내야 한다는 것을 안다

### Scene 4 — 거주구 통로 (에이든)

- Entry: 아는 얼굴이 하나도 없다
- Opposition: 다렌 모트가 평생의 전우처럼 다가온다. 아이 나이, 배급표 장수, 다음 근무 시각부터 말한다
- Turn: 가족사진이 이 현재의 실재를 증명한다. 이 사람의 삶은 에이든의 선택 위에 서 있다
- Exit: 잃은 것을 주장하려면 이 사람의 현재를 부정해야 한다는 구조가 성립한다

### Scene 5 — 반입품 접수·격리 보관실 (에이든)

- Entry: 최소한 그가 가져온 물건은 그의 판단을 증명한다
- Opposition: F1 절차는 절검과 소거명부를 다른 분류로 접수한다. 그가 대는 F0 기관명 일부는 이 본부에 존재하지 않는다
- Turn: 그는 반입품을 지키기 위해 이 체계의 영웅 신분을 처음 사용한다
- Exit: 영웅 대우를 거부하지 않기로 한다. 그것이 유일하게 남은 접근권이기 때문이다

### Scene 6 — 기록관 대조실 (리아 세른 · 보조 POV)

- Entry: 귀환 등록 대조는 통상 업무다
- Opposition: 대조표의 F0 쪽 항목들이 오류로 뜨지 않고 조용히 정합처리돼 있다. 지워진 흔적이 아니라 처음부터 없던 것처럼 맞아떨어진다
- Turn: 리아는 그 상태를 기록하되 원인·주체를 판정하지 않는다. 기억한다와 증명할 수 있다를 구분한다
- Exit/Final Image: 회색 종이 없는 이 본부에서 격리 보관실의 귀환석만 혼자 운다. 리아는 그 이유를 모른다

## 9. Anti-Repeat

- E001의 ‘삭제된 글자 하나가 회색으로 되살아남’을 반복하지 않는다. E025의 상실은 흔적조차 남기지 않고 정합된 상태로 나타난다
- E002의 여섯 기관 순회·귀환석 검사 반복 금지. 이 회차의 기관 접촉은 반입품 접수 한 번뿐이다
- E003의 두 문서 대조 구성 금지. 대조는 리아 장면에서 ‘어긋남이 없음’을 확인하는 역방향으로만 쓴다
- E024의 목록 작성·등록 선택 반복 금지. E025의 반입품 장면은 선택이 아니라 분류 통보다
- E023의 도시 전체 회색 종 동시 타종을 반복하지 않는다. 종이 없는 곳에서 귀환석 하나가 우는 축소·역전으로 쓴다
- 낯선 미래를 폐허·디스토피아 몽타주로 소개하지 않는다. F1은 더 살아 있고 더 정상적이다
- 다렌 모트를 수상한 감시자·세뇌된 친구로 연출하지 않는다
- 에이든이 즉시 폭로·항의·탈주를 시도하는 전개 금지 — 그 시도는 E026–E031이 담당한다
- 기억상실·꿈·환각·정신오염으로 처리 금지 — 정신오염 검사는 E031 훅이다
- 리아와 에이든이 재회해 서로의 기억을 확인하는 장면 금지 — E028
- 보조 POV를 사망예고·정답 설명으로 사용 금지
- 권말이라는 이유로 요약 독백·연대기 나열로 닫지 않는다

## 10. Active State / Props

- 절검 (R03) — F1 절차로 접수, 기능·소유권 여전히 미확정
- 소거명부 일부 — 누락·오염 포함, 분류 통보 대상
- 귀환석 — 균열 상태로 F1 도착, 수명·좌표 신뢰도 하락, 최종 이미지의 소리원
- 출발 인장 — F0 동료 이름이 사라진 상태
- 근무·전몰 명부 — 부재를 증명하는 문서
- 다렌 모트의 가족사진 — 현재의 실재를 증명하는 물건, 감정 인질 금지
- 회색 종 — **부재**로만 존재. F1 본부에 없다
- 리아의 개인 경고 쪽지 (E005) — 보관 유지, 열지 않음

## 11. State Mutation Plan

E025 종료 시 기록:

- 시간선 상태 F1 확정 및 F0 접근 불가
- 소실된 F0 관계 목록의 확인 범위 (L002)
- 에이든의 F1 영웅 신분 획득과 그것을 접근권으로 사용하기로 한 판단
- 공식 서사와 실제 행위의 격차 인지 수준
- 다렌 모트와의 관계 개시 상태 — 상대는 오랜 전우, 에이든은 초면
- 리아 세른의 관측 기록 상태와 미판정 항목
- 절검·소거명부의 F1 보관·접근 조건
- 귀환석 상태와 F1 본부에 회색 종이 없다는 사실
- V1 Volume Exit State Ledger 및 Permanent Loss 반영

## 12. Ready Verdict

- Authority: RESOLVED
- Domain Readiness: READY
- Storycraft companion: REQUIRED / `docs/10_story_architecture/craft-manifests/E025-storycraft-manifest.md`
- POV: READY — P2 다중 POV 승인 배치 확인 완료, 전환 1회
- Scene Density: X · 5~6장면 — 설계 장면 수 6으로 일치
- Permanent Loss: L002 확정 기재 필요
- S0: 0
- S1: 3 (§13 참조)

## 13. Open Gaps

정본 근거가 없어 채우지 못했거나 상위 판정이 필요한 항목이다. CP 안에서 새 설정으로 메우지 않았다.

- **S1 — 중복 훅 3건**: `v01-scene-ready-design-v1.md` E025 Scene 2·3이 담은 사실 두 가지가 레지스트리에서는 뒤 회차의 훅이다. ① 하지 않은 학살이 공적에 포함 = E026 훅, ② 친구가 F0에서 적대 세력 문장을 사용 = E030 훅. 본 CP는 E025에서 위화감까지만 제시하고 확정은 뒤 회차에 넘기는 것으로 읽었다. A11·A12 확인 대상이다.
- **S1 — 귀환 시각 간격**: F0 출발은 CY 664 장야월 21일(`master-chronology` J01)인데, F1 귀환 시각이 출발 시각과 어떤 간격을 갖는지 정본에 없다. 본 CP는 ‘F1 CY 664, 귀환 직후’까지만 적었다.
- **S1 — 리아의 F1 소속·직위 상태**: `character-state-checkpoints`는 E025의 리아를 ‘F0 파편 보존자’로만 규정하고, F1 본부에서의 직위·근무지·접근권은 명시하지 않는다. 보조 POV 장면의 장소를 ‘기록관 대조실’로만 두고 기관 소속을 확정하지 않았다.
- 다렌 모트가 E025에 이름으로 등장하는지 여부. `canon-naming-pack` §5 C07과 `character-state-checkpoints` C07 행이 F1 전우 신분을 규정하지만 `cast-canon-index-v2.md`는 첫 핵심권을 V2로 적는다. 본 CP는 E025 등장은 하되 관계 서사의 본격 전개는 V2로 두었다.
- F1 본부의 정식 명칭·문장·계급 체계의 구체값이 정본에 없다. `최후 연대국`이라는 미래국가명만 있으며 F0/F1 간 명칭 차이는 미지정이다.
- 소실된 F0 동료들의 개별 이름·인원. 어느 정본에도 명단이 없다. ‘F0 지휘관·동료 다수’까지만 규정된다.
- 회색 종이 F1 본부에 없는 이유의 제도적 근거. `V01` E025 Final Image가 사실만 규정하고 설명은 없다. M16 사다리에서도 E025는 칸이 없다.
