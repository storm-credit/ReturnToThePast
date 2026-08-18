# Permanent Loss Lock v1

Status: ACTIVE LEDGER  
Owner: Loss / Continuity  
Last Reviewed: 2026-08-07  
Canon Level: HARD LOCK

## Principles

1. 시간선 변경은 손실을 없애기보다 다른 사람·제도·지역에 이전할 수 있다.
2. 다른 시간대의 동일인은 죽은 사람의 대체품이 아니다.
3. 기억이 남아도 관계·권리·공동 경험이 자동 복원되지 않는다.
4. F0 복원은 새 미래의 생존자를 소거할 수 있으므로 기본 선이 아니다.
5. 모든 권말 개입은 최소 하나의 비가역 결과를 남긴다.

## Locked Losses

| ID | Episode / Cause | Permanent Loss | Recovery Prohibition |
|---|---|---|---|
| L001 | E023 첫 표적 제거 | 개혁가 영구 사망 | 재시도·부활·다른 버전 대체 금지 |
| L002 | E025 F1 귀환 | F0 지휘관·동료·관계 다수 소실 | F1 시민을 유지하며 관계만 복구 불가 |
| L003 | E058–E075 진실 확정 | 에이든의 첫 살인 책임 | 기억상실·본부 명령으로 면책 금지 |
| L004 | E092–E100 증언도시 절충 | 옛 도시의 완전한 영토·지배권 | 과거 도시 통째 복원 금지 |
| L005 | E111–E125 경계갑 사용 | 에이든 공적 신분의 누적 부식 | 치료·장비로 초기화 금지 |
| L006 | E198–E200 건국 변경도시 선택 | 변경도시와 일부 문화 영구 소실 | 후대 복원 퀘스트로 회수 금지 |
| L007 | E219–E225 개정 귀환 | 건국 동맹 한 문화의 정본 기록 소실 | 단일 완전 기록 회수 금지; 잔흔만 가능 |
| L008 | E263–E275 젊은 에이든 독립 | 에이든 고향·가족 기억 일부와 귀환조건 | 젊은 에이든을 대체 기억으로 사용 금지 |
| L009 | E298–E299 협상장 방어 | F1 지휘관 영구 사망 | 다른 시간대 지휘관으로 감정 대체 금지 |
| L010 | E297–E337 기록 인장화 | Ria의 개인 F0 기억·관계 세부 | 기록 열람으로 감정·관계 자동 복원 금지 |
| L011 | E311–E312 시간선 상속 판결 | 일부 옛 소유권·가문 권리 영구 포기 | 전면 원상복구 금지 |
| L012 | E336–E349 최초 연대기 해체 | 하나의 절대 정본과 Ria 사적 약속 | 숨겨진 완전판 등장 금지 |
| L013 | E366 | 개혁가의 절검 파괴 | 재제작·과거 회수 금지 |
| L014 | E367–E375 최종 기능분리 | 에이든 공적 이름·역사주소·귀환권 | 영웅 복귀·비밀 원상복구 금지 |
| L015 | Final | F0 완전복원 포기 | 에필로그 리셋 금지 |
| L016 | Final | 백지권 일부와 중앙 효율 | 모든 지역·기능의 완전 회복 금지 |

## Injury / Aging Rule

시간여행 육체 비용은 배치별 상태표에 누적한다. 최종 정확한 흉터·감각손상 수치는 집필 전 상태 감사에서 확정하되, 이전 부상 전체 회복은 금지한다.

---

## Source Key

이 확장절의 표에서 쓰는 근거 약호다. 새 문서를 만들지 않고 기존 정본만 가리킨다.

| 약호 | 원본 파일 |
|---|---|
| `CC` | `docs/00_project/canon-constitution-v1.md` |
| `NAME` | `docs/00_project/canon-naming-pack-v1.md` |
| `DEC` | `docs/00_project/decision-log.md` |
| `CAST` | `docs/05_characters/cast-canon-index-v2.md` |
| `V01`–`V15` | `docs/10_story_architecture/detail/vNN-scene-ready-design-v1.md` |
| `LOCK` | 이 문서 §Locked Losses (L001–L016) |

## Loss Class Codes

분류 코드는 새 설정이 아니라 기존 L001–L016과 권별 State Ledger를 검색·검증하기 위한 색인이다. 세계 안의 용어가 아니므로 원고에 노출하지 않는다.

| 코드 | 분류 | 무엇이 사라지는가 | 자동 동반 여부 |
|---|---|---|---|
| LD | 인물 사망 | 한 사람의 생물학적 생존 | LD는 LR을 동반한다. 역은 성립하지 않는다 (`CC` IMMUTABLE 5) |
| LR | 관계 소실 | 공동 경험·신뢰·상호 인지 | LD 없이도 단독 발생한다 (`LOCK` Principles 3) |
| LI | 제도 소거 | 기관·법적 지위·정당성·운영권 | 인물이 살아 있어도 발생한다 |
| LM | 기억 손상 | 개인 기억·기록문·증언 접근 | 기억이 남아도 LR은 복구되지 않는다 (`LOCK` Principles 3) |
| LG | 지역 소실 | 장소·토지·주소·연결 | 주민 생존과 별개로 발생한다 |
| LA | 물질·유산 소실 | 유물의 원형·기능·재제작 가능성 | 기능 이전과 원형 소실을 구분한다 |
| LX | 권리·권한 소실 | 소유권·귀환권·승인권·독점 | 자발적 포기도 영구손실로 계산한다 |
| LB | 육체 누적 | 흉터·감각손상·노화 | 이 문서 §Injury / Aging Rule을 따른다 (`CC` IMMUTABLE 2) |

## LD — 인물 사망

| ID | 대상 | 확정 시점 | 사망의 성격 | 남는 것 | 복구 금지 | 근거 |
|---|---|---|---|---|---|---|
| L001 | 세렌 바일 (C06) | E023 | 에이든이 불완전 기록을 믿고 직접 살해 | 그의 개혁 의제가 후대 기록·잔문에 잔흔으로만 | 재시도·부활·다른 버전 대체 금지 | `LOCK` L001, `CAST` C06, `V01` |
| L009 | 마르칸 베르 (C04) | E298–E299 | 마지막 배급·병원구역에 스스로 남아 시민 대피 후 사망 | 장례보석에 기록된 마지막 감각 | 다른 시간대 지휘관으로 감정 대체 금지 | `LOCK` L009, `CAST` C04, `V12` E296–E299 |
| L029 | 에이든 가족 일부 | V11 (E263–E268 구간) | 세뇌·협박이 아니라 구호대·병원 환자를 위한 자발적 잔류의 결과 | 젊은 에이든이 잇는 현지 구호망 | 가족 전원 생존 시나리오 재개 금지 | `V11` Permanent Loss, `V11` E265, E267 |
| L036 | 익명 사상자 — 중앙대응 제한분 | V08 (E198–E200) | 공개투표·느려진 공사로 신속 대응을 포기해 발생 | 협약에 남은 위임금지 원리 | 사후 소급 구조 금지 | `V08` Permanent Loss |
| L037 | 익명 사상자 — 실험·정지분 | V09 중단실험 / `V12` E284, E290, E292 | 시범정지·계절동기 붕괴로 수술환자·수확지 피해 | 공개된 피해수치와 원인분리 기록 | 피해를 선전으로 부인하거나 중앙재가동으로 취소 금지 | `V09` Permanent Loss, `V12` E284–E285, E290, E292 |
| L038 | 익명 사상자 — 수도 방벽 약화분 | E355 | 지방소거를 거부한 대가로 수도 구역 위험 수용 | 비밀희생 금지 원칙 | 비밀 희생 재개 금지 | `V15` E354–E355 |

`[ASSUMPTION]` L036–L038은 각 권 State Ledger가 "실제 사상자·실제 피해"를 명시하지만 §Locked Losses에 ID가 없어, 인물 사망 항목으로 승격해 번호를 부여했다. 개별 이름·수치는 정본에 없다.

## LR — 관계 소실

| ID | 무엇이 끊기는가 | 확정 시점 | 인물은 살아 있는가 | 왜 복구되지 않는가 | 근거 |
|---|---|---|---|---|---|
| L002 | F0 지휘관·동료와의 관계 다수 | E025 F1 귀환 | F1 시민으로는 존재 | F1 시민을 유지하면서 관계만 되돌릴 수 없다 | `LOCK` L002, `V01` |
| L002-a | 에이든–다렌 모트 (C07)의 우정 | V02 이후 지속 | 다렌은 생존, F1 가족 보유 | 다렌 쪽에 공유 기억이 없고 현재 가족의 권리가 우선한다 | `CAST` C07, `CAST` §4 |
| L010 | Ria 세른의 F0 사적 관계 세부 — 이름·약속 | E297 인장화 → E299 확인 | Ria 생존, 공공증거는 보존 | 기록 열람은 증거를 돌려주지만 감정·관계를 돌려주지 않는다 | `LOCK` L010, `V12` E297, E299, `CAST` C02 |
| L010-a | Ria의 F0 관계 추가상실 | V14 | 생존 | 단일원본 포기 과정에서 사적 기록이 다시 깎인다 | `V14` Permanent Loss |
| L026 | 해방파와의 관계 일부 | V09 | 양측 생존 | 건설 허용 결정이 관계의 전제를 파기했다 | `V09` Permanent Loss |
| L039 | 에이든–동료들의 상호 인지 | E367 → E373 | 전원 생존 | 이름이 연결재로 소모되어 공적으로 기억할 근거 자체가 사라진다 | `V15` E367, E373, `NAME` §8-A |
| L040 | 에이든–젊은 에이든 (C08) | V11 종료 | 둘 다 생존 | 원인과 결과가 아니라 독립된 두 삶이므로 회복할 원본 관계가 없다 | `CAST` §4, `CAST` C08, `V11` E263 |
| L041 | 에이든–가족의 기억 속 인격 | E265 | 일부 생존 | 기억한 성격과 실제 인격이 다르며, 기억 쪽을 진짜로 우선하지 않는다 | `V11` E263 Scene 3, E265 |

## LI — 제도 소거

| ID | 소거 대상 | 확정 시점 | 소거 방식 | 기능은 어디로 갔는가 | 복구 금지 | 근거 |
|---|---|---|---|---|---|---|
| L017 | F1 구조대상 일부의 법적 존재 | V02 | 시간선 변경 후 등록 부재 | 없음. 미승인 상태로 잔존 | 소급 일괄등록 금지 | `V02` Permanent Loss |
| L018 | Ria 세른의 직위 안정성 | V02 | 본부 신뢰 단절 | 팔림프세스트 기록관 직무는 유지, 보호는 상실 | 직위 원상회복 금지 | `V02` Permanent Loss, `NAME` §5 C02 |
| L020 | F1 단일 국가의 정당성 | V03 | 진실 확정으로 서사 붕괴 | 이후 다자 협상 구조로 대체 | 단일 정통성 재구축 금지 | `V03` Permanent Loss |
| L004 | 옛 도시의 완전한 영토·지배권 | E092–E100 | 증언도시 절충 | 부분 권리·문화 반환만 | 과거 도시 통째 복원 금지 | `LOCK` L004, `V04` |
| L042 | 삭제된 공동체의 운영권 기관 | E281 | 후대 왕실이 정본연대기에서 삭제 | 실무를 이어 온 현지공동체가 기능계승 | 혈통·국가 근거의 원상복구 금지 | `V12` E281–E282 |
| L011 | 옛 소유권·가문 권리 일부 | E311–E312 | 시간선 상속 판결 | 사용·문화·접근·분해·보상 권리로 분리 | 전면 원상복구 금지 | `LOCK` L011, `V13` E308–E310 |
| L012 | 하나의 절대 정본 연대기 | E336–E349 | 복수원본·반론 병기 체제로 해체 | 이의제기형 공공기록 | 숨겨진 완전판 등장 금지 | `LOCK` L012, `V14` |
| L032 | 일부 지역의 협약 참여 | V14 | 독자중앙화·협약이탈 | 없음 | 강제 재편입 금지 | `V14` Permanent Loss |
| L043 | 중앙 연대개입·강제덮어쓰기·자동귀환 | E356 분리 → E368 폐쇄 | 물리·법적 분리 후 다중동의 잠금 | 생활안정 기능만 지역 분산망으로 | 광범위 다중동의·피해공개·지역거부 없이 재연결 금지 | `V15` E356, E368, `DEC` DEC-008, `CC` Ending |
| L044 | 중앙 귀환다리의 귀환 기능 | E368 | 에이든 주소를 연결재로 소모하며 폐쇄 | 없음 | 재가동 청원 수용 금지 | `V15` E367–E368 |
| L016 | 중앙 효율과 빠른 재난대응 능력 | Final | 기능분리의 구조적 결과 | 지역 수동망·상호지원·국제지원 | 모든 지역·기능의 완전 회복 금지 | `LOCK` L016, `V12` Permanent Loss, `V15` Final |
| L035 | 왕국의 비밀 군사우위 | V15 | 외부 상호감사 협정 수용 | 제한적 상호열람·피해청구 체계 | 일방적 비밀우위 회복 금지 | `V15` E360–E361, Final |
| L021 | 왕국 방어회랑·군사비밀 일부 | V04 | 증언도시 절충의 부수 비용 | 없음 | 회수 금지 | `V04` Permanent Loss |
| L027 | 농업기술 독점통제와 취약점 비공개 | V10 | 외부국 공개 교환 | 국제 지원·감사 접근권 | 재비밀화 금지 | `V10` Permanent Loss |
| L026-a | 시간장치 지식의 비확산 상태 | V09 | 공개 부담표·사후재판 도입의 부수효과 | F3 국가산업·시간전쟁 시장으로 발전 | 지식 회수 금지 | `V09` Volume Promise, Permanent Loss |
| L023 | 에이든의 안전한 귀환 보장 | V06 | 제도권 신뢰 단절 누적 | 없음 | 신분 복권 금지 | `V06` Permanent Loss, `V02` |
| L005 | 에이든 공적 신분의 누적 부식 | E111–E125 | 경계갑 사용의 누적 부채 | 없음 | 치료·장비로 초기화 금지 | `LOCK` L005, `V05`, `V11` E257–E258 |
| L014 | 에이든 공적 이름·역사주소·귀환권 | E367–E375 | 마지막 연결재로 자발 제공 | 이름 대신 공동체·피해·반론·무명증인의 분산기록 | 영웅 복귀·비밀 원상복구 금지 | `LOCK` L014, `V15` E365, E367, E373, `NAME` §8-A |
| L015 | F0 완전복원의 선택지 | Final | 새 미래 생존자 소거 위험으로 항구 폐기 | 없음 | 에필로그 리셋 금지 | `LOCK` L015, `CC` Ending, `DEC` DEC-008 |

## LM — 기억 손상

| ID | 손상 대상 | 확정 시점 | 손상 유형 | 잔존 형태 | 복구 시도가 막히는 지점 | 근거 |
|---|---|---|---|---|---|---|
| L010 | Ria의 F0 개인기억 | E297 → E299 | 자발적 인장화로 소모 | 검증된 좌표기억 일부만 사용, 공공증거는 보존 | 기록 열람으로 감정·관계 자동 복원 금지 | `LOCK` L010, `V12` E297, E299 |
| L008 | 에이든의 고향·유년·가족 기억 일부 | E263–E275 | 역사주소 붕괴에 동반된 소실 | 젊은 에이든의 독립 경로 | 젊은 에이든을 대체 기억으로 사용 금지 | `LOCK` L008, `V11` Permanent Loss |
| L008-a | 에이든의 시간요원 경력 기억 일부 | V11 | 법적 출생·귀환권 붕괴에 동반 | 장비마다 다른 이름으로 그를 인식 | 장비 재보정으로 이름 복원 금지 | `V11` E257–E258, Permanent Loss |
| L039-a | 동료 기록 속 에이든의 이름·역할 | E366 지연전 → E367 | 연결재 소모 중 점진 소실 | 선택의 결과만 남고 행위자는 남지 않음 | 새 성인·창립자 등록으로 되살리기 금지 | `V15` E366 Hook, E367, E373 |
| L025 | 증언자 한 명의 기억문 | E185 | 보관소 방화 | 분산보관된 나머지 증거 | 단일 완전본 회수 금지 | `V08` E185, `LOCK` L007 |
| L045 | 에르나 기억문의 무오류성 | E183 | 시간선 잔향·현재 기대·회복과정에 오염됨이 확정 | 날짜·감각·증언자 상태가 붙은 자료로 등록 | 몸기억을 정답으로 사용 금지 | `V08` E183, `CC` Memory Rule |
| L003 | 에이든의 면책 가능성 | E058–E075 | 기억이 아니라 책임의 소실 불가 | 첫 살인 책임 확정 | 기억상실·본부 명령으로 면책 금지 | `LOCK` L003, `CC` Prohibited |

## LG — 지역 소실

| ID | 지역 | 확정 시점 | 무엇이 사라지는가 | 주민은 어떻게 되는가 | 복구 금지 | 근거 |
|---|---|---|---|---|---|---|
| L006 | 변경도시 | E198–E200 | 장소·토지·건물과 일부 문화 | 생존자는 후대 왕조 중앙집권 세력에 합류 | 후대 복원 퀘스트로 회수 금지 | `LOCK` L006, `V08` Volume Promise, Permanent Loss |
| L006-a | 변경도시 일부 구조 | V07 | 건설 단계에서 선제 포기 | — | 재설계 회수 금지 | `V07` Permanent Loss |
| L007 | 건국 동맹 한 문화의 정본 기록 | E219–E225 | 단일 완전 기록 | 문화는 존속, 정본은 부재 | 단일 완전 기록 회수 금지, 잔흔만 가능 | `LOCK` L007 |
| L019 | 전체 원본 기록 일부 | V03 | 소각 | — | 완전 복원 금지 | `V03` Permanent Loss |
| L003-a | 도시 하나와 관련 관계·권리 일부 | V03 | 소거 | — | 통째 복원 금지 | `V03` Permanent Loss |
| L016-a | 아노르 백지권 일부 | E362 → E368 | 지역망 연결 자체 | 비참여를 선택한 쪽과 주소불안정으로 연결불가한 쪽이 다르다 | 강제 연결 금지, 완전 회복 금지 | `LOCK` L016, `V15` E362, E368, `NAME` §3 |
| L046 | 지역별 주소피해·기근피해 | V12 | 계절동기 붕괴로 수확·국경 주소 흔들림 | 실제 사망·기근 발생 | 중앙 부분재가동으로 취소 금지 | `V12` E290–E292, Permanent Loss |

### 제안되었으나 실행되지 않은 소거

거부된 소거도 대가를 남긴다. 이 표의 항목은 손실이 발생하지 않은 사례가 아니라, 손실이 다른 곳으로 이전된 사례다.

| 제안 | 제안 시점 | 대상 | 거부 근거 | 대신 발생한 영구비용 | 근거 |
|---|---|---|---|---|---|
| 백지권 인접 지방 주소·수확 소거 | E354 | 잿빛 변경 방면 지방 | 지방 대표 인장과 주민증언을 자동회로에 직접 연결 | 수도 방벽 안정치 급락, 수도 사상자, 복원파 재결집 | `V15` E354–E355 |
| 마르칸 베르 구출을 위한 중앙 부분재가동 | E291, E296 | 지방 한 곳의 주소·수확·주민 일부 | 부담이 특정 지방에 자동전가된다 | L009 지휘관 영구사망 | `V12` E291, E296, E298 |
| 아노르 백지권 전체를 완충재로 삼아 에이든 보존 | E363 | 백지권 주민의 얼굴·이름·통행·후손 권리 | 한 사람을 위해 익명집단을 희생하지 않는다 | L014 에이든 이름·주소·귀환권 소실 | `V15` E363–E364 |
| 가족 전원 생존 | E259 | — | 구호대 미창설로 환자·난민 대체사망 | L029 가족 일부 사망 수용 | `V11` E259–E260 |

## LA — 물질·유산 소실

| ID | 유산 | 확정 시점 | 원형 | 기능 | 어디로 갔는가 | 복구 금지 | 근거 |
|---|---|---|---|---|---|---|---|
| L013 | 절검 | E366 | 완전 파괴 | 회로차단에 소모 | 없음 | 재제작·과거 회수 금지 | `LOCK` L013, `V15` E366, Final Assets |
| L031 | 건국 모루 | V13 → E357 | 상실 | 전투기능 상실, 안정합금은 생활노드로 | 계절·의료·토지 노드 | 원형 복원 금지 | `V13` Permanent Loss, `V15` E357, Final Assets |
| L033 | 경계갑 | E111–E125 마모 → E357 재료화 | 상실 | 시간저항 기능 대부분 상실 | 지역노드 재료 | 재제작 금지 | `V05` Permanent Loss, `V11` E257, `V15` E357, Final Assets |
| L028 | 다른 에이든의 방패 | V10 봉인 → E366 소진 | 기억코어 봉인 | 외피기능 소진 | 없음 | 봉인 해제로 정답 획득 금지 | `V10` Permanent Loss, `V15` E366, Final Assets |
| L022 | F0 귀환패 | V05 서명 소실 → V15 기능종료 | 분산봉인 | 복원키가 아니라 잔류 센서였음이 확정 | 없음 | 복원키로 재해석 금지 | `V05` Permanent Loss, `V02` (F0 복구키 오해 차단), `V15` Final Assets |
| L047 | 장례보석 | E184 해석 확정 / E298 지휘관 기록 | 존속 | 죽음 순간의 시야·소리·공포만 재생 | — | 인격 복원·예언·부활 도구화 금지 | `V08` E184, `V12` E298, Final Assets |

## Recovery Failure Modes — 복구 시도는 어떻게 실패하는가

각 행은 작중에서 실제로 시도되거나 제안되는 복구 경로와, 그 경로가 막히는 정본 지점이다. 새 금지를 만들지 않고 기존 금지가 어떤 장면에서 작동하는지를 정리한다.

| 코드 | 복구 시도 | 시도 주체 | 표면적 기대 | 실제로 벌어지는 일 | 차단 근거 |
|---|---|---|---|---|---|
| RF-01 | 같은 시점으로 재파견해 다시 하기 | 미래 본부·모집팀 | 최적해를 찾을 때까지 반복 | 누적부채가 커지고 현지인이 실험변수가 된다. 반복 자체를 금지한다 | `CC` IMMUTABLE 1, `V11` E258, E262 |
| RF-02 | 다른 시간대 동일인으로 대체 | 유족·본부·독자기대 | 죽은 사람을 되찾음 | 다른 시간대 동일인은 독립 권리주체이며 원본의 귀환이 아니다 | `CC` IMMUTABLE 5, Death and Address Rule, `CAST` §6, `LOCK` L001·L009 |
| RF-03 | F0 완전복원 실행 | 복원파 | 원래 세계로 되돌림 | 새 미래의 생존자가 소거된다. 강제 덮어쓰기이지 복원이 아니다 | `LOCK` Principles 4, L015, `V12` E296–E299, `V15` E366 |
| RF-04 | 기록을 열람해 기억·관계 회복 | Ria·기록공동체 | 읽으면 돌아옴 | 공공증거는 돌아오지만 감정·약속·사적 세부는 돌아오지 않는다 | `LOCK` Principles 3, L010, `V12` E299 |
| RF-05 | 죽은 자에게 진실을 묻기 | 협상장·조사자 | 사망자 증언으로 사건 확정 | 장례보석은 마지막 감각만 재생하고, 그 장면조차 시간잔향이 겹쳐 있다 | `V08` E184, `V12` Final Assets |
| RF-06 | 기억상실을 근거로 면책 | 에이든·본부 | 몰랐으니 책임 없음 | 책임은 기억과 분리되어 확정된다 | `CC` Prohibited, `LOCK` L003 |
| RF-07 | 치료·장비로 신분 부식 초기화 | 중앙·의료기관 | 공적 기록 회복 | 부식은 장비 문제가 아니라 누적 역사부채다. 장비마다 그를 다른 이름으로 읽는다 | `LOCK` L005, `V11` E257 |
| RF-08 | 후대 복원 퀘스트로 소실 지역 회수 | 후대 세력·복원파 | 도시를 되찾음 | 옛 도시 통째 복원과 후대 회수를 모두 금지한다 | `LOCK` L004, L006 |
| RF-09 | 숨겨진 완전판 원본 발견 | 원본주의자 (C22) | 진짜 정본으로 분쟁 종결 | 가장 오래된 문서조차 후대 위조이며, 완벽한 원본이 정의를 선택해 주지 않는다 | `LOCK` L012, `V14` Volume Promise, E-level False Interpretation |
| RF-10 | 파괴·분해된 유산 재제작 | 공방·군부 | 무기·상징 회복 | 재료는 이미 생활노드로 소비되었고 재제작·과거 회수를 금지한다 | `LOCK` L013, `V15` E357, Final Assets |
| RF-11 | 시간여행 재가동 청원 | 대형 재난지역 시민 | 과거를 바꿔 수천 명을 살림 | 재가동은 강제덮어쓰기·주소소거·기술독점을 다시 연다. 현재 자원과 국제지원으로 처리하며 더 많은 단기사망을 감수한다 | `V15` E356, E372, `CC` Ending |
| RF-12 | 에이든을 성인·창립자·왕 없는 왕으로 등록 | 기념위·기록공동체 | 이름과 관계 회복 | 개인희생 신화가 다시 권력·혈통·정통성의 근거가 된다. 이름 대신 분산기록을 남긴다 | `LOCK` L014, `V15` E373 |
| RF-13 | 역사부채만 감수하면 전원 생존 | 에이든 | 비용을 혼자 지고 모두 구함 | 출발인장은 자기소거를 늦출 뿐 막지 못하며 부채를 타지역에 전가한다 | `V11` E259, E260 |
| RF-14 | 익명집단을 완충재로 삼아 주인공 보존 | Iris·검증위원회 | 성공률 높은 대안 | 지역 전체가 영구무명화된다. 안이 철회된다 | `V15` E363–E364 |
| RF-15 | 물리반환으로 옛 권리 전면회복 | 복원파·옛 주인 | 정의로운 원상회복 | 즉시 철거는 국경·피난로 방어를 붕괴시키고, 옛 법·현재 법 양쪽에서 지워지는 가족이 생긴다 | `LOCK` L011, `V13` E308–E310 |
| RF-16 | 중앙 부분재가동으로 특정 인물 구출 | 마르칸 베르·지지자 | 지휘관 생환 | 부분재가동도 부담을 특정 지방에 자동전가한다. 구출을 포기한다 | `LOCK` L009, `V12` E291, E296, E298 |
| RF-17 | 팔림프세스트 기억자를 정답자로 사용 | 협상장·신도 | 기억으로 진실 확정 | 기억은 자동 진실이 아니며 기억자를 예언자로 만들지 않는다 | `CC` Memory Rule, `V14` |
| RF-18 | 에필로그 리셋 | 작품 외부 압력 | 씁쓸함 상쇄 | 금지 | `LOCK` L015, `CC` IMMUTABLE 1 |
| RF-19 | 모든 시간요원 강제회수 | 본부·잔류자 반대파 | 아무도 남기지 않는 정의 | 현지 가족·책임·자율성을 파괴한다. 군사·장치 정보만 봉인하고 현지법에 맡긴다 | `V15` E352–E353, `CAST` C29 |
| RF-20 | 지역 자립망으로 중앙 부정의 해소 | 자립지역 | 분산화가 곧 정의 | 지역유력자가 감사를 포획하고 소수종족·환자·움브라에게 비용을 떠넘긴다 | `V15` E359 |

## Loss Transfer Ledger — 손실은 어디로 이전되는가

§Principles 1의 실행표다. 좌열의 손실을 막으면 우열이 반드시 발생한다.

| 막으려 한 손실 | 이전된 손실 | 이전 시점 | 근거 |
|---|---|---|---|
| 미래 멸망 | 세렌 바일 사망 + F0 관계 다수 소실 | E023–E025 (사망 E023, 관계소실 E025) | `V01`, `LOCK` L001, L002 |
| 옛 도시 완전 소멸 | 왕국 방어회랑·군사비밀 일부 | E092–E100 | `V04` |
| 후대 신화의 권력화 | 변경도시 영구소실 + 중앙대응 제한 사상자 | E198–E200 | `V08` |
| 후대 폭정 | 장치지식 확산과 F3 시간전쟁 시장 | E219–E225 | `V09` |
| 가족 전원 사망 | 구호대 미창설로 인한 환자·난민 대체사망 | V11 | `V11` E259 |
| 경쟁 시간개입 | 농업·의료·국경 붕괴와 기근 | E288–E293 | `V12` |
| 마르칸 베르 사망 | 지방 한 곳의 주소·수확·주민 소거 | E296 (거부됨) | `V12` |
| Ria 기억 보존 | 복원파의 F0 좌표 강제 실행 | E297 (거부됨) | `V12` |
| 지방 소거 | 수도 방벽 약화와 수도 사상자 | E354–E355 | `V15` |
| 중앙 효율 | 지역 기술격차와 빈곤지역 전환 불가 | E357–E358 | `V15` |
| 외국 봉쇄 | 왕국 단독비밀과 국제적 우선권 | E360–E361 | `V15` |
| 에이든의 생존 조건 | 백지권 전체 영구무명화 | E363 (거부됨) | `V15` |
| 백지권 희생 | 에이든 이름·역사주소·귀환권 | E367 | `V15`, `LOCK` L014 |
| 과거수정으로 얻는 즉시 구제 | 첫 재난의 추가 단기사망 | E372, E374 | `V15` |

## Loss Confirmation Gate — 손실이 비가역이 되는 4단계

`[ASSUMPTION]` 아래 4단계는 새 규칙이 아니라 `V08`·`V12`·`V15`에서 반복되는 동일 절차를 하나로 묶은 것이다. 개별 근거는 각 행에 표시했고, "4단계"라는 명명 자체는 정본 용어가 아니다.

| 단계 | 내용 | 이 단계에서 요구되는 것 | 이 단계 이후 금지되는 것 | 정본 사례 |
|---|---|---|---|---|
| G0 공개 | 무엇을 잃는지 표로 먼저 보인다 | 전환재료표, 피해표, 자동부담표, 공개 부담표 | 비밀 희생 | `V15` E354, E357, E364, `V12` E283 |
| G1 동의 | 당사자와 다중 거부권을 확인한다 | 권리자 동의, 검증위원회, 일곱 운영권 무거부 | 영웅 권한에 의한 일방 강탈·일방 희생 | `V12` E283, E297, `V15` E363, E365, E367 |
| G2 실행 | 물리·법적으로 분리하거나 손실이 발생한다 | — | 실행 중 우회 구조 | `V15` E356, E366–E368, `V12` E298–E299 |
| G3 기재 | 권 State Ledger의 Permanent Loss에 올린다 | 사망·기억·지역·유산 구분 기재 | 사후 축소·부인 | 각 권 `### Permanent Loss` |
| G4 잠금 | 재연결·재제작·재가동을 봉쇄한다 | 광범위 다중동의·피해공개·지역거부 없이는 불가 | 조용한 재가동 | `V15` E356 Scene 2, `LOCK` L001–L016 |

## Not a Loss — 오분류 금지 목록

아래는 손실처럼 보이지만 손실로 기재하면 안 되는 항목이다. 반대로 이를 손실로 처리하면 정본이 깨진다.

| 항목 | 실제 상태 | 왜 손실이 아닌가 | 근거 |
|---|---|---|---|
| 감사인장 | 존속 | 단독사용만 봉인되었고 일곱 운영권 절차로 계속 작동한다 | `V12` E287, `V15` Final Assets |
| 다렌 모트 (C07) 생존 여부 | P1 장부에 유지 | 미확정은 손실이 아니다 | `CAST` C07 |
| 이름 없는 여행자 (C30) | 의도적 익명 | 미완성이 아니라 결말의 익명성 정본이다. 에이든으로 확정해 관계를 회복하면 위반 | `CAST` §1, §6 |
| 아벨 네르 (C26)의 모순기억 | 병존 인정 | 손상이 아니라 모순기억과 현재 인격을 함께 인정받은 상태 | `CAST` C26 |
| 백지권의 자율적 비참여 | 권리 행사 | 비참여권과 지원·통행·의료·증언권은 분리되어 보장된다. 주소불안정으로 인한 연결불가만 손실 | `V15` E362 |
| 젊은 에이든 (C08) | 독립 인물 | C01의 기억·인생·관계의 보전물이 아니다 | `CAST` C08, §4, `LOCK` L008 |
| 유산의 기능 이전 | 재료화 | 기능이 지역노드로 옮겨진 것과 원형 소실은 별개로 기재한다 | `V15` E357, Final Assets |
| 에이든의 육체 | 생존 가능 | 죽음보다 넓은 희생이며, 사망과 역사주소 소거와 관계기억 소실은 구분한다 | `V15` E365, E368, Final Ledger |

## Ledger Coverage Check

| 권 | State Ledger에 Permanent Loss 기재 | §Locked Losses ID 존재 | 이 확장절에서 부여한 ID |
|---:|---|---|---|
| V01 | 있음 | L001, L002 | — |
| V02 | 있음 | 없음 | L017, L018 |
| V03 | 있음 | L003 | L019, L020, L003-a |
| V04 | 있음 | L004 | L021 |
| V05 | 있음 | L005 | L022, L033 |
| V06 | 있음 | 없음 | L023 |
| V07 | 있음 | 없음 | L006-a, L024 |
| V08 | 있음 | L006 | L025, L036, L045 |
| V09 | 있음 | L007 | L026, L026-a, L037 |
| V10 | 있음 | 없음 | L027, L028 |
| V11 | 있음 | L008 | L029, L040, L041, L008-a |
| V12 | 있음 | L009, L010 | L030, L042, L046 |
| V13 | 있음 | L011 | L031 |
| V14 | 있음 | L012 | L010-a, L032 |
| V15 | 있음 | L013–L016 | L035, L038, L039, L043, L044, L047 |

`[ASSUMPTION]` L017 이후의 ID는 이미 각 권 State Ledger에 기재된 손실을 이 원장에 승격하기 위한 번호이며, 새 사건을 만들지 않았다. L024는 `V07`의 "공방·연합 일부 분열"과 "왕도축 원형 고정"을 하나로 묶은 것이다. L030은 `V12`의 "중앙의 빠른 재난대응 능력 상실"이며 L016과 부분 중복이므로 L016의 선행 단계로 읽는다.

## Sources Read

- `docs/12_losses/permanent-loss-lock-v1.md` (기존 39행)
- `docs/00_project/canon-constitution-v1.md` — IMMUTABLE 1·2·5·8, Memory Rule, Death and Address Rule, Ending, Prohibited Convenient Solutions
- `docs/00_project/canon-naming-pack-v1.md` — §3 권역·장소, §5 인물, §6 기관, §8-A 어원(로엔·아노르)
- `docs/00_project/decision-log.md` — DEC-008 결말 기능과 Permanent Cost
- `docs/05_characters/cast-canon-index-v2.md` — C01–C30 최종상태, §3 아르덴 케르, §4 관계축, §6 금지
- `docs/10_story_architecture/detail/v01-scene-ready-design-v1.md` — Volume Promise, Permanent Loss
- `docs/10_story_architecture/detail/v02-scene-ready-design-v1.md` — Permanent Loss / Cost, F0 귀환패 오해 차단
- `docs/10_story_architecture/detail/v03-scene-ready-design-v1.md` — Permanent Loss
- `docs/10_story_architecture/detail/v04-scene-ready-design-v1.md` — Permanent Loss
- `docs/10_story_architecture/detail/v05-scene-ready-design-v1.md` — E103–E104, Permanent Loss
- `docs/10_story_architecture/detail/v06-scene-ready-design-v1.md` — Permanent Loss
- `docs/10_story_architecture/detail/v07-scene-ready-design-v1.md` — Permanent Loss
- `docs/10_story_architecture/detail/v08-scene-ready-design-v1.md` — Volume Promise, E183–E185, Permanent Loss
- `docs/10_story_architecture/detail/v09-scene-ready-design-v1.md` — Volume Promise, Permanent Loss
- `docs/10_story_architecture/detail/v10-scene-ready-design-v1.md` — Permanent Loss
- `docs/10_story_architecture/detail/v11-scene-ready-design-v1.md` — Volume Promise, E257–E267, Permanent Loss
- `docs/10_story_architecture/detail/v12-scene-ready-design-v1.md` — 전문, 특히 E281–E299, Volume Exit State Ledger
- `docs/10_story_architecture/detail/v13-scene-ready-design-v1.md` — Volume Promise, E308–E310, Permanent Loss
- `docs/10_story_architecture/detail/v14-scene-ready-design-v1.md` — Volume Promise, Permanent Loss
- `docs/10_story_architecture/detail/v15-scene-ready-design-v1.md` — 전문, 특히 E351–E375, Final State Ledger

### 근거 문서

- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/12_losses/permanent-loss-lock-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/00_project/canon-constitution-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/00_project/canon-naming-pack-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/00_project/decision-log.md (DEC-008 및 인접 항목)
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/05_characters/cast-canon-index-v2.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v01-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v02-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v03-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v04-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v05-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v06-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v07-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v08-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v09-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v10-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v11-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v12-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v13-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v14-scene-ready-design-v1.md
- C:/Users/Storm Credit/Desktop/Novel/너라는운율/project/ReturnToThePast/docs/10_story_architecture/detail/v15-scene-ready-design-v1.md

### 정본 근거가 없어 채우지 못한 항목

- ~~세렌 바일(C06) 사망의 정확한 화수~~ — **DEC-023으로 해소. E023 확정** (원고 E023에서 사망).
- 에이든 가족 구성원의 개별 이름, 인원, 사망자 수. V11은 '가족 일부 사망'까지만 규정한다.
- L006 변경도시의 정식 지명. canon-naming-pack-v1.md §3 주요 장소표에 해당 항목이 없어 '변경도시'로만 표기했다.
- L007 '건국 동맹 한 문화'가 P02–P05 중 어느 종족인지. 정본에 미지정.
- Ria 세른이 잃은 F0 기억의 구체 항목 목록(어떤 이름·어떤 약속인지). V12 E299는 '이름·약속·사적 세부'까지만 규정한다.
- 아노르 백지권 중 영구단절되는 구역의 범위·인구·지명. V15 E362·E368은 '일부'로만 규정한다.
- L036–L038 익명 사상자의 수치·지역·명단. 어느 권 State Ledger에도 숫자가 없다.
- 다렌 모트(C07)의 최종 생존 여부. cast-canon-index-v2.md가 'P1 장부에 유지'로 열어 두었다.
- L005 에이든 공적 신분 부식의 단계별 수치(어느 화에서 어느 정도 부식되는가). 이 문서 §Injury / Aging Rule이 '집필 전 상태 감사에서 확정'으로 미뤄 두었다.
- L013 절검의 물질 원형이 파괴된 뒤 남는 파편의 처분. V15 E357은 '절검 파편'을 전환재료표에 올리고 E366은 '완전히 부서진다'고 하는데, 두 서술의 선후·잔여량 관계가 정본에 없다.
- LB(육체 누적)의 배치별 상태표 실물. 참조되는 '배치별 상태표'와 '상태 감사' 문서를 저장소에서 찾지 못했다.
- 손실 확정 절차의 공식 명칭. G0–G4는 내가 묶은 일반화이며 정본에 절차명이 없다.
- L015 F0 완전복원 포기가 '누구의 어떤 선언으로' 최종 확정되는지의 장면 단위 근거. V15 Final State Ledger는 결과만 기재한다.
