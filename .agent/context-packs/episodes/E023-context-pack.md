# Episode Context Pack — E023

Status: D10 READY  
Episode: E023  
Title: 미래를 위한 한 번의 칼  
Compiled By: A21 Context Pack Compiler  
Reference: `agent/1d-subact-context-packs`

> 이 CP는 정본이 아니다. 충돌 시 원본 정본과 권한계층을 따른다. 각 항목의 원본 경로는 절마다 명시한다.

## 1. Authority / Architecture

Required sources:

- [`/AI_PROJECT.md`](../../../AI_PROJECT.md)
- [`docs/00_project/canon-constitution-v1.md`](../../../docs/00_project/canon-constitution-v1.md) — IMMUTABLE 1·2·4·5·7·10
- [`docs/00_project/canon-naming-pack-v1.md`](../../../docs/00_project/canon-naming-pack-v1.md)
- [`docs/00_project/terminology-and-addressing-clarification-v1.md`](../../../docs/00_project/terminology-and-addressing-clarification-v1.md)
- [`docs/00_project/decision-log.md`](../../../docs/00_project/decision-log.md) — DEC-016~021
- [`docs/00_project/GATE_STATUS.md`](../../../docs/00_project/GATE_STATUS.md)
- [`docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md`](../../../docs/10_story_architecture/detail/ga01-episode-registry-e001-e075.md) — E023 행, V01 Exit-State Lock
- [`docs/10_story_architecture/detail/v01-scene-ready-design-v1.md`](../../../docs/10_story_architecture/detail/v01-scene-ready-design-v1.md) — Subact 1D, E022–E024, Volume Exit State Ledger
- [`docs/10_story_architecture/subact-causal-matrix-v1.md`](../../../docs/10_story_architecture/subact-causal-matrix-v1.md) — 1D
- [`docs/10_story_architecture/location-world-crosswalk-v1.md`](../../../docs/10_story_architecture/location-world-crosswalk-v1.md) — V01
- [`docs/10_story_architecture/scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) — V1 E023
- [`docs/10_story_architecture/scene-density-and-pacing-overlay-v1.md`](../../../docs/10_story_architecture/scene-density-and-pacing-overlay-v1.md) — §2 E형, §5 훅 유형
- [`docs/05_characters/cast-canon-index-v2.md`](../../../docs/05_characters/cast-canon-index-v2.md) — C01·C03·C06
- [`docs/05_characters/voice-relationship-state-bible-v1.md`](../../../docs/05_characters/voice-relationship-state-bible-v1.md) — §2·§4·§5·§6
- [`docs/11_mystery/mystery-reinforcement-ladder-v1.md`](../../../docs/11_mystery/mystery-reinforcement-ladder-v1.md) — M02·M04·M16
- [`docs/12_losses/permanent-loss-lock-v1.md`](../../../docs/12_losses/permanent-loss-lock-v1.md) — L001·L003, LD·LR 표
- [`docs/01_timeline/master-chronology-and-aging-ledger-v1.md`](../../../docs/01_timeline/master-chronology-and-aging-ledger-v1.md) — §1·§2·§5 시간선 확정 지연
- [`docs/02_world/atlas-region-dossiers-v1.md`](../../../docs/02_world/atlas-region-dossiers-v1.md) — R05 서부 잿빛 변경
- [`.agent/context-packs/episodes/E022-context-pack.md`](E022-context-pack.md)

Episode function — 출처: 레지스트리 E023 행, v01 설계 E023, subact-causal-matrix 1D

- Grand Act: GA I — 잘못된 치료
- Volume: V1 — 회색 종이 울리는 날
- Subact: 1D — 표적 제거와 귀환
- Beat: 선택
- Goal: 불완전한 증거와 미래 사망자 수치 사이에서 비가역 선택을 실행
- Opposition: 좁은 기록실, 파괴하면 안 되는 장부와 환자 통로, 도주 대신 시간을 끄는 표적, 몇 분뿐인 잔여 시간
- Choice: 에이든이 표적을 죽이고 연대기 접근을 차단한다
- Cost: 표적 사망은 잠기며 다른 시간대 버전으로 대체 불가능하다 (L001)
- State Change: 에이든은 명령 수행자에서 자기 판단으로 사람을 죽인 자가 된다. `명령만 따랐다`는 자기정당화가 영구히 불가능해진다
- Hook: 도시 전체의 회색 종이 동시에 울리고 주민 이름이 장부에서 흐려진다
- Next Cause: E024에서 임무가 공식 성공으로 판정되고 등록 용량 제한 아래 절검과 소거명부 일부만 회수한다

## 2. E022 Carryover

출처: [`E022-context-pack.md`](E022-context-pack.md), v01 설계 E022

### 에이든 로엔

- 봉쇄권 이전 협상이 결렬됐다. 남은 출구가 없다
- 세렌이 건넨 소거 명단을 소유하고 있다. 결과를 모른 채 죽이는 상태가 아니다
- 주민 탈출로를 열었고 그 대가로 추격·설득 시간을 잃었다
- 무기를 이미 뽑았다. E023은 그 동작의 연속선에서 시작한다
- 표적을 여전히 역할명으로 부른다

### 세렌 바일 (C06)

- 저항을 선택했다
- 미래 기관의 검증 불가능한 약속을 끝까지 거부했다
- 자기 생체인장이 서부 봉쇄의 강제키임을 알고 있으며, 죽으면 왕실이 기록망을 장악한다는 것도 안다 (E019)
- 도주가 아니라 시간 끌기를 택한다 — 대피 중인 사람들이 더 멀리 가도록

### 아이리스 네르 (C03)

- 탈출로를 통해 환자 수레를 움직이는 중이다
- E023 본편에는 직접 개입하지 않는다. 그의 선택은 E024 이별 장면에서 확정된다
- 귀환표식 연결권을 여전히 쥐고 있다

### 외부 상태

- 왕실군 포위와 단계적 진입이 진행 중이다
- 본부 시한과 F0 잔여일 11일 수치가 유지된다
- 회색 종이 한 번 울렸고 귀환창은 마지막 단계에 진입했다

## 3. Time / Location

출처: [`master-chronology-and-aging-ledger-v1.md`](../../../docs/01_timeline/master-chronology-and-aging-ledger-v1.md) §1·§2·§5, [`location-world-crosswalk-v1.md`](../../../docs/10_story_architecture/location-world-crosswalk-v1.md) V01, [`atlas-region-dossiers-v1.md`](../../../docs/02_world/atlas-region-dossiers-v1.md) R05

- Era: N — CY 640, E022 직후 연속
- 진행 시간: 선택 가능한 시간은 몇 분뿐이다 (v01 설계 E023 Entry)
- 에이든: 41세. 세렌: 42세
- 권역: 서부 잿빛 변경
- Main locations:
  1. 은신처 좁은 기록실
  2. 기록실 밖 서부 상공·마을 방향 (Scene 4 시야)
- 공간 제약: 장부와 환자 통로를 파괴하지 않는 조건 아래 싸운다. 좁은 실내이므로 이동·회피 여지가 거의 없다
- 시간선 확정 지연 규칙 적용: 개입 직후 모든 것이 즉시 바뀌지 않는다. 1단계 국소 잔향까지만 E023에서 발생한다. 인과 결속·동기화 경계·현재 확정은 E024–E025의 몫이다

## 4. 사망과 봉쇄 해제의 인과

출처: v01 설계 E019·E023, [`permanent-loss-lock-v1.md`](../../../docs/12_losses/permanent-loss-lock-v1.md) L001·L003, [`canon-constitution-v1.md`](../../../docs/00_project/canon-constitution-v1.md) IMMUTABLE 5

### 물리 인과 순서

1. 세렌이 치명상을 입는다
2. 생체인장이 꺼진다
3. 서부 봉쇄가 풀린다
4. 왕실 기록망이 서부를 덮는다
5. 도시 전체의 회색 종이 동시에 울리고 주민 이름이 장부에서 흐려진다

이 순서는 뒤바꾸지 않는다. 특히 4·5는 에이든의 의도가 아니라 그의 행위가 만든 반대편의 능동행동이다.

### 영구손실 잠금

- L001 — 세렌 바일(C06) 영구 사망. 재시도·부활·다른 시간대 버전 대체 금지
- L003 — 에이든의 첫 살인 책임. 기억상실·본부 명령으로 면책 금지
- 남는 것: 그의 개혁 의제가 후대 기록·잔문에 잔흔으로만 남는다
- IMMUTABLE 1: 회귀 금지. 이 죽음을 되돌리는 재도약 가능성을 암시하지 않는다
- IMMUTABLE 5: 다른 시대의 동일인 또는 잔향은 원본의 귀환이 아니다

### 살해의 성격 (정본 규정)

- `permanent-loss-lock` LD 표: 에이든이 불완전 기록을 믿고 직접 살해
- v01 설계 Character Cost: 에이든은 자신이 확신해서 죽인 것이 아니라 불확실성을 감당하지 못해 죽였음을 안다
- 따라서 이 장면은 정의의 집행도 오해의 비극도 아니다. 시간이 부족한 상태에서 판단을 유예할 수 없어 내린 결정이다

### 연대기 접근 차단

- 레지스트리 E023 Choice의 후반부다
- 세렌이 쥐고 있던 최초 연대기 접근 경로가 그의 사망으로 닫힌다 (M15, E016 세렌의 암호와 연결)
- E023에서 연대기의 정체·소재를 공개하지 않는다

## 5. Character State

출처: [`cast-canon-index-v2.md`](../../../docs/05_characters/cast-canon-index-v2.md), [`voice-relationship-state-bible-v1.md`](../../../docs/05_characters/voice-relationship-state-bible-v1.md) §2·§4·§5

### 에이든 로엔 (C01)

- 목표: 시간이 끝나기 전에 결정한다
- 감정곡선 위치: V1–V3 곡선의 `불편함 → 죄책감` 전이 지점
- 전투 태도: 승리의 쾌감이 없다. 공간 제약 때문에 기술이 아니라 각도와 순서의 문제로 싸운다
- 죽인 직후 반응: 안도도 자책 독백도 아니다. 다음 절차를 확인하려다 확인할 것이 없음을 발견한다
- 금지: 명령을 핑계로 삼는 자기변호, 죽이며 확신을 회복하는 연출, 표적을 악당으로 재정의해 마음을 정리하는 서술

### 세렌 바일 (C06)

- 목표: 대피 중인 사람들이 더 멀리 가도록 시간을 끈다
- 도주하지 않는다. 이것이 무모함이 아니라 계산이라는 점이 드러나야 한다
- 마지막 말은 자기 변론도 저주도 아니다. 명단과 같은 층위 — 취급과 인계에 관한 것이다
- 금지: 유언조 진실 폭로, 순교자 선언, 재앙을 늦춘 자기 기능의 설명, 에이든을 용서하는 대사
- L001 잠금 실행 회차

### 아이리스 네르 (C03)

- E023 본편에 직접 등장시키지 않는 것을 기본값으로 한다. 등장하더라도 결과 통보 수준을 넘지 않는다
- 그의 판정과 결별은 E024 자산이다. 여기서 선소비하지 않는다

### 왕실 기록망 측

- 인물이 아니라 제도적 능동행동으로 표현한다
- 새 개인 흑막을 지정하지 않는다 (M12 정보상한)
- 봉쇄 해제 후의 접수는 신속하고 절차적이다. 이 신속함 자체가 준비돼 있었음을 보여주지만 누가 준비시켰는지는 말하지 않는다

## 6. Mystery / Information Ceiling

출처: [`mystery-reinforcement-ladder-v1.md`](../../../docs/11_mystery/mystery-reinforcement-ladder-v1.md), [`canon-constitution-v1.md`](../../../docs/00_project/canon-constitution-v1.md) IMMUTABLE 7·10

Active mysteries:

- M02 세렌 바일은 왜 창시자로 기록됐는가 — 사다리 다음 단은 E033이다. E023은 단을 추가하지 않고 질문의 무게만 키운다
- M16 회색 종은 무엇을 감지하는가 — 도시 규모 동시 울림이 최대 규모 관측 사례가 된다. 원리 설명은 E092까지 금지
- M15 최초 연대기는 어디 있는가 — 접근 경로가 닫히는 것으로만 전진
- M04 F0 귀환좌표는 남아 있는가 — E033 귀환패 파편의 전조로만 기능

Reader may know:

- 표적의 사망과 봉쇄 해제가 직접 연결돼 있다
- 왕실 기록망은 봉쇄가 풀리자마자 서부를 덮을 준비가 돼 있었다
- 회색 종은 개인이 아니라 도시 규모의 무언가에도 반응한다
- 주민 이름이 장부에서 흐려지는 현상은 물리적 파괴가 아니다

Reader must not know yet:

- 세렌이 지방 소거를 늦추고 있었다는 전체 기능 (E072 확정)
- 기록 조작·책임 전가의 주체 (E061 이후)
- 삭제된 증언자의 정체
- 19만 생존증가 모델의 최종 오류구조
- 회색 종의 작동 원리
- F1이 어떤 모습으로 형성되는가

금지 연출:

- 죽어가는 세렌이 진실을 요약해 말하기
- 에이든이 죽인 직후 자기 판단의 오류를 확정적으로 깨닫기
- 회색 종·기록망의 원리를 서술로 해설하기
- 새 시간법칙이나 새 유산을 이 장면에서 도입하기 (IMMUTABLE 10)

## 7. POV / Storycraft

출처: [`scene-density-map-v1.md`](../../../docs/10_story_architecture/scene-density-map-v1.md) V1 E023, [`scene-density-and-pacing-overlay-v1.md`](../../../docs/10_story_architecture/scene-density-and-pacing-overlay-v1.md) §2·§5

- POV: 에이든 단일 근접 3인칭. 보조 POV 없음 (POV 배치표는 E025부터 리아를 허용)
- Scene Density: **E형 · 4장면**
- 배정 사유(원문): 좁은 기록실 전투와 치명상에 이어 생체인장이 꺼지며 왕실 기록망이 서부를 덮는 반대편의 능동행동이 즉시 발생한다
- E형 운용 규칙: 네 번째 장면은 단순 에필로그가 아니라 비용 또는 반대편의 능동행동이어야 한다
- Primary craft: 제약된 공간의 비가역 실행
- Secondary A: 확신이 아니라 시간 부족이 방아쇠라는 인과 배치
- Secondary B: 개인의 죽음이 즉시 제도의 확장으로 번역되는 규모 전환
- Hook: H5 미래 변형 + H4 제도 변화
- Reader reward: 임무 성공이 곧 재앙의 착수임을 인물보다 독자가 먼저 본다

## 8. Scene Values

**설계 장면 수 4 — §7 밀도값과 일치한다.** 네 번째 장면은 에필로그가 아니라 반대편의 능동행동이다.

### Scene 1 — 좁은 기록실

- Entry: 시간이 없어도 제압만 하면 된다
- Opposition: 장부와 환자 통로를 파괴할 수 없다는 제약, 도주 대신 시간 끌기를 택한 표적
- Turn: 세렌의 목적이 이기는 것이 아니라 지연이라는 사실이 드러난다. 에이든이 이길수록 시간을 잃는다
- Exit: 제압으로는 끝나지 않는다는 것이 확정된다

### Scene 2 — 치명상

- Entry: 아직 다른 방법이 있을 수 있다
- Opposition: 남은 시간, F0 사망자 수치, 귀환 시한
- Choice: 에이든은 세렌이 거짓말쟁이라서가 아니라 F0 사망자 수치와 귀환 시한을 우선해 치명상을 입힌다
- Exit: 비가역 실행 완료. 되돌릴 수 없는 상태로 진입

### Scene 3 — 생체인장 소등

- Entry: 죽음으로 임무는 끝났다
- Opposition: 인장이 꺼지며 봉쇄가 풀린다. 죽음이 종료가 아니라 작동이었다
- Character Cost: 에이든은 자신이 확신해서 죽인 것이 아니라 불확실성을 감당하지 못해 죽였음을 안다
- Exit: 표적 사망 잠금(L001) 성립. 그러나 상황은 닫히지 않고 열린다

### Scene 4 — 서부를 덮는 기록망

- Entry: 남은 일은 회수와 귀환뿐이다
- 반대편의 능동행동: 왕실 기록망이 봉쇄가 풀린 서부를 즉시 접수한다. 준비돼 있었던 속도다
- Opposition: 에이든이 손에 쥔 명단과 눈앞의 현실이 같은 이름들을 다르게 처리하고 있다
- Exit / Hook: 도시 전체의 회색 종이 동시에 울리고 주민 이름이 장부에서 흐려진다
- 금지: 에이든이 이 현상의 의미를 정확히 해석하는 서술

## 9. Anti-Repeat

직전 회차들과 실제로 달라야 하는 지점:

- E022의 협상 구조를 전투 중 대사로 재연하지 않는다. E023에는 협상이 없다
- E021의 오해 → 정정 구조를 반복하지 않는다
- E020의 시간 산술을 다시 계산하지 않는다. 여기서는 시간이 재는 대상이 아니라 이미 없는 것이다
- E019의 표적 자기설명 대화를 임종 대사로 되살리지 않는다
- E003의 두 문서 대조를 반복하지 않는다
- E001의 삭제된 글자가 되살아나는 훅을 반복하지 않는다. 여기서 이름은 나타나는 것이 아니라 대규모로 흐려진다 — 방향이 반대다
- E002의 기관 순회·물건 검사 구조를 반복하지 않는다
- 회색 종을 E007·E009처럼 개인 곁에서 울리는 방식으로 쓰지 않는다. 규모가 다르다
- 전투를 무술 시퀀스로 전시하지 않는다. Arc 02 Anti-Repeat 조항이 판단 실패를 정보 부족과 시간 압박의 결합으로 규정한다
- 살해 직후 회한 독백으로 회차를 닫지 않는다. 회차는 반대편의 행동으로 닫힌다
- 4장면을 3장면으로 압축하지 않는다

## 10. Active State / Props

- 세렌의 생체인장 — E023에서 소등. 이후 재점화·복제 가능성을 암시하지 않는다
- 세렌의 절검 (R03) — 저항의 무기. E023 종료 시 유주물이 되고 E024에서 등록·회수 대상이 된다. V15 E366 파괴까지 잠금
- 소거 명단 — E022 인계분. E023에서는 읽지 않고 소지한다. Scene 4의 대조 대상
- 장부 — 파괴 금지 제약물. E023에서 검증되지 않는다
- 환자 통로 — 파괴 금지 제약물이자 Scene 1 전투의 지형 조건
- 회색 종 — 도시 전체 동시 울림. 최대 규모 사례로 기록
- 귀환표식 — 아이리스가 연결권 보유. E024 자산
- 주민 장부의 흐려지는 이름 — 새 유물이 아니라 현상이다. 물건으로 승격하지 않는다

## 11. State Mutation Plan

E023 종료 시 기록:

- L001 세렌 바일 영구사망 확정 — 회차·상황·직접 행위자
- L003 에이든의 첫 살인 책임 개시
- 생체인장 소등과 서부 봉쇄 해제 확정
- 왕실 기록망의 서부 접수 범위
- 회색 종 도시 전체 동시 울림 기록 (M16 관측 사례)
- 주민 장부 이름 흐려짐의 관측 범위
- 절검의 유주물 상태와 위치
- 소거 명단의 소지 상태와 미확인 항목
- 연대기 접근 경로 차단 확정
- 귀환창 잔여와 아이리스의 연결 상태
- 에이든의 표적 호칭 상태 변화 여부

## 12. Ready Verdict

- Authority: RESOLVED
- Domain Readiness: READY
- Scene density conformance: PASS — E형 4장면, 설계 4장면, 4장면이 반대편 능동행동
- POV: READY
- Storycraft companion: REQUIRED — [`E023-storycraft-manifest.md`](../../../docs/10_story_architecture/craft-manifests/E023-storycraft-manifest.md)
- Permanent-loss lock: L001 실행 회차 — A13 확인 필요
- Information ceiling: PASS
- S0: 0
- S1: 3 — §gaps 참조

Pre-Writing Gate는 [`GATE_STATUS.md`](../../../docs/00_project/GATE_STATUS.md)를 따른다. E022 상태기록 확인 뒤 A18 호출 가능.

## gaps

정본에서 도출할 수 없어 이 CP가 확정하지 않은 항목이다. 임의 창작하지 않았다.

1. **세렌 바일 사망의 정본 화수 불일치.** 레지스트리 E023 Choice와 v01 설계 E023 Scene 3은 E023 사망으로 기술한다. 그러나 `cast-canon-index-v2.md` C06과 `master-chronology` §2는 `E024 부근`, `permanent-loss-lock` L001은 `E023–E025`로 적는다. `permanent-loss-lock` 자체가 이 건을 미해결로 등재해 두었다. 이 CP는 회차 설계 원본을 우선해 E023을 사망 회차로 설계했으나, A02·A13의 단일 화 확정이 필요하다.
2. **은신처 기록실의 정식 지명.** v01 설계는 `좁은 기록실`로만 쓴다. 크로스워크 V01은 첫 개혁가의 살해를 1C 주무대 `반쪽성·절검의 언덕`에 배치하고 아틀라스 R05는 절검의 언덕을 “첫 개혁가의 저항과 죽음이 연결된 장소”로 규정하지만, 기록실과 절검의 언덕을 동일 장소로 명시한 정본은 없다.
3. **`연대기 접근 차단`의 실체.** 레지스트리 E023 Choice에 명시되지만, 차단되는 접근 경로가 세렌의 암호(M15 E016)인지 봉쇄권인지 별도 물건인지를 규정한 정본을 찾지 못했다. 이 CP는 경로가 닫힌다는 사실만 기록하고 실체를 확정하지 않았다.
4. **주민 이름이 장부에서 흐려지는 현상의 물리.** v01 설계 Hook의 표현이며, 이 현상이 마나열병·잔문·기록망 접수 중 무엇의 결과인지 규정한 정본이 없다. M16 사다리는 E092까지 원리 공개를 막으므로 현상만 제시하도록 설계했다.
5. **세렌 바일의 말투 항목 부재.** `voice-relationship-state-bible-v1.md`에 C06 항목이 없다. 임종 대사 규칙은 v01 설계의 행동기술과 cast index C06 금지조항에서만 도출했다.
