# Production / Pre-Writing Gate Status

Status: **DESIGN RECONCILIATION ACTIVE — NEW MANUSCRIPT BLOCKED**  
Effective: 2026-08-20  
Main Verified: `0a2e5204233723829f97167d744e2e89c187d90c`  
Main Manuscript Boundary: **E001–E088 present**  
Current Production Unit: **D12-based E089–E093 preparation only (Context Pack / Craft / Continuity), no manuscript**

## 1. Why This File Was Resynced

이 문서는 오래도록 `E001 AUTHOR PROSE REVIEW / E003+ STOP` 상태에 머물렀지만 실제 GitHub main에는 이후 E001–E088 원고가 병합되었다.

따라서 과거 상태문구를 현재 생산 경계로 사용하면 안 된다.

현재 사실은 다음 두 가지를 동시에 보존한다.

1. **파일 존재 상태**: main 원고는 E001–E088까지 존재한다.
2. **품질 승인 상태**: 파일이 main에 있다는 사실은 각 회차의 `HUMAN PROSE PASS`를 의미하지 않는다. 최종 인간문체 승인은 작가만 부여한다.

## 2. Current Canon / Architecture State

- Canon Constitution: ACTIVE
- D11 Story Architecture Amendment: MAIN MERGED
  - 마나열병 = 회색 재앙
  - 에이든은 중심 주인공이지만 세계의 유일한 인과 주체가 아님
- D12 Ensemble Resolution Amendment: MAIN MERGED
  - V12 Era O 대표 = C21 레오르 세르바
  - V10→V12 세 시대 협상 연속성 해소
  - V4 E089–E093 병렬세력·POV·권리절차 보강
- 5 Grand Acts / 15권 / 60 Subact 사건 골격: 유지
- 결말·영구손실: 유지

## 3. Main Manuscript Boundary

현재 main의 연속 원고 경계는 **E088**이다.

V4 main:
- E076–E088 존재 확인
- E088 `가족관계가 바뀌는 의식`이 현재 마지막 원고
- E089 이후 원고는 main에 없음

### Important

`main에 있음`과 `최종 문체 승인`을 구분한다.

- HUMAN PROSE 최종 승인: AUTHOR ONLY
- 자동 validator 통과: HUMAN PROSE PASS가 아님
- AUTHOR REVIEW / FIRST DRAFT 원고가 main에 존재할 수 있음

## 4. E089+ Production Gate

D11/D12 이후 E089부터는 과거 초안을 그대로 이어 쓰지 않는다.

### E089–E093 before manuscript

필수:
1. E088 실제 원고 Exit 재확인
2. V4 D6
3. D11 Amendment
4. D12 Amendment
5. `v04-e089-e093-d11-ensemble-overlay-v1.md`
6. `v04-witness-zone-consent-protocol-v1.md`
7. Secondary POV table
8. 새 Context Pack
9. 새 Craft Manifest
10. Continuity / Red Team PASS

이 준비가 끝나기 전 **새 E089 원고 작성/병합 금지**.

### E089 hard correction

- POV: **리아 세른 P1**
- 기존 에이든 POV 초안은 superseded reference
- B05 백지사슴: 보조증거, 진실판독기 금지
- 나하 아노르: 주소상실 주민 독립행동 축

## 5. Stale Manuscript PR Safety

D11/D12 이전 연쇄 초고는 직접 병합하지 않는다.

### Closed / Not Merged / Reference Only

- #90 E089–E094 — superseded
- #114 E094–E100 — stale chain
- #115 E101–E106 — stale chain
- #116 E107–E112 — stale chain
- #117 E113–E118 — stale chain
- #118 E119–E125 — stale chain
- #125 E089–E093 v2 — D11/D12 POV/ensemble mismatch

브랜치는 보존하며 사건·문장 재사용 여부는 최신 main 정본과 대조 후 결정한다.

## 6. Operational PRs

- #126 D11 deep world/faction architecture — MERGED
- #127 D12 ensemble resolution — MERGED
- #124 Minimum Action Agent OS adoption — OPEN / NOT MERGED / 별도 운영 작업
- #123 old production-state sync — SUPERSEDED by this D12 sync; 직접 병합 금지

## 7. Human Prose Hard Stops

기존 작가 피드백은 계속 유효한 품질 규칙이다.

- 짧은 격언형 마감 과다
- `A가 아니라 B`, `A가 아니었다. B였다.` 기계적 반복
- 대사 직후 의미 재해설
- 모든 단락을 훅·주제문으로 마감
- 모든 인물이 같은 수준으로 짧고 정확하게 말함
- 설정어가 감각·행동보다 먼저 나옴
- 감정을 행동 뒤 추상어로 다시 설명
- 생활 마찰·우연·머뭇거림 부재

이 규칙은 E089 이후 재구성에도 적용한다.

## 8. Current Gate Verdict

### Allowed now
- 세계관·설정집·설계도 심화
- 맹점/Red Team
- 최신 main 기준 상태 동기화
- E089+ Context Pack / Craft Manifest / continuity preparation
- 구식 PR 정리

### Blocked now
- D11/D12를 반영하지 않은 기존 E089+ 초안 병합
- E089 새 원고를 준비문서 없이 작성
- HUMAN PROSE PASS 자동 선언

## 9. Resume Condition for New Manuscript

1. E089–E093 D12 Context Pack/Craft/Continuity 준비 완료
2. Canon/POV/Faction/Information Ceiling 검증 PASS
3. 실제 원고 작성 단계 진입 시 Human Prose Audit 적용
4. HUMAN PROSE PASS는 작가 승인만으로 확정

현재 다음 단위는 **원고가 아니라 E089–E093 D12 집필 준비문서 재생성**이다.
