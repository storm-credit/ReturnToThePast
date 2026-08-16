# E038–E043 Canon / Information Ceiling / Anti-Padding Audit

Status: IN PROGRESS — AUTHOR REVIEW REQUIRED

## Scope
- E038 `두 번째 표적의 얼굴`
- E039 `주소를 주지 않는 기록관`
- E040 `진짜 배신 기록`
- E041 `취소할 수 없는 피해표`
- E042 `더 위험한 구조`
- E043 `새 정족수`

## Canon Locks
- 두 번째 표적의 정식 이름/ID는 현 정본에서 미확정이므로 임의 고유명 추가 금지.
- 왕실 접촉 사실과 배신 동기 해석을 분리.
- 리아 세른의 역사주소 거부권을 우회하거나 무효화하지 않음.
- 마르칸 베르의 지연 피해예측은 실제 비용으로 유지.
- 아벨 네르는 증거가 아니라 의료 취약 아동 환자로 우선 구조.
- 아이리스 네르의 현지 대피 거부권과 조건을 유지.
- 본부 감시요원은 즉시 악역/흑막으로 확정하지 않음.

## Manual Findings Before Revision
- 독자용 본문에 `F0`, `F1`, `Era N`, `E0xx` 등 제작용 표기가 반복 노출됨.
- E038에 `정본 설계에서 말한 구조` 메타서술 노출.
- E039에 `정본 인물표` 메타서술 노출.
- E041에 `E042에서 계산한다` 및 `회차 번호처럼 말하지 마십시오` 메타 대사 노출.
- E042에 `E055에서 아직 오지 않은 선택` 메타서술 노출.
- E043에 `E044에서 그 비용을...` 메타서술 노출.

## Gate
- 각 화 공백 포함 최소 7,000자.
- `validate_manuscript.py` 전 화 PASS.
- 제작용 메타표기 독자 본문에서 제거.
- Canon / Information Ceiling 수동 PASS.
- Anti-Padding 수동 PASS.
- HUMAN PROSE PASS는 작가 승인 전 부여하지 않음.
- main 병합은 작가의 명시적 승인 전 금지.
