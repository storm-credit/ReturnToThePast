# E008 품질 보고서 — 이름 없는 검문

Status: AUTHOR REVIEW — FIRST DRAFT / NOT HUMAN-PROSE APPROVED  
Episode: E008  
Branch: `agent/manuscript-e008-draft`

## 설계 대조
- E형 4장면: 검문선 / 파손 수레 / 아벨 네르 발작 / 아이리스 네르의 순번 재배치.
- 검문은 신원 확인보다 책임 귀속 절차로 구현. 잘못된 미래 문서는 `위조`가 아니라 `처리 불가` 판정.
- 미래 도구 없이 현지 목재·밧줄·쐐기로 수레를 임시 수리하고, 그 대가로 임시 노역표·호송 조건 획득.
- 아이리스 네르, 메이라 솔, 아벨 네르 첫 핵심 등장 시 전체 이름 명시.
- 같은 가구의 유사 증상과 존재하지 않는 가족 기억을 함께 배치하되 원인 확정 없음.
- 메이라 솔은 이름→날짜→장소 순으로 확인하고 병명을 확정하지 않음.
- 마지막에 아벨이 에이든에게 `두 번째로 늦게 왔다`고 말하는 훅 구현.

## 정보상한 / 금지
- 마나열병 기전 미공개.
- 아벨의 두 번째 출생기록 미공개(E009 소관).
- 아이리스를 안내자·미래 임무 이해자로 만들지 않음.
- 뇌물·무력·미래 도구로 검문 돌파하지 않음.
- 회색 종은 이 화에서 울리지 않음.

## 문체
- 에이든 로엔 단일 근접 3인칭 중심, 메이라 솔 제한 관찰은 실무 묘사 수준으로 제한.
- 신규 비정본 가족 이름은 직접 생성하지 않음.
- 최소 7,000자 기준을 넘기는 장편 초고로 작성.

`validate_manuscript.py`는 connector-only 환경에서 실행하지 않았으므로 PASS로 기록하지 않는다.

## 판정
Structural/Craft: PASS (manual)  
Canon/Information Ceiling: PASS (manual)  
Human Prose: AUTHOR REVIEW REQUIRED  
Final: DRAFT ONLY
