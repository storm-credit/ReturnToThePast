# Branch and Checkpoint Policy

## 목적

- 작업을 도메인별로 분기한다.
- 중간 커밋과 주간 푸시를 습관으로 고정한다.
- 큰 설정 변경이 섞여 흐려지는 것을 막는다.

## 기본 브랜치

- integration branch: `codex/orchestra-setting-sync`

이 브랜치는 설정집과 오케스트라의 `통합 진행 상황`을 모으는 기본선이다.

## 작업 브랜치 규칙

도메인이 크거나 위험할 때는 integration에서 파생 브랜치를 만든다.

- `codex/lore-<scope>`
- `codex/maps-<scope>`
- `codex/naming-<scope>`
- `codex/orchestra-core-<scope>`
- `codex/packet-<scope>`

## 커밋 규칙

한 커밋에는 한 가지 self-contained pass만 넣는다.

좋은 묶음 예:

- 이름 충돌 정리
- 적대축 밀도 보강
- 배경지도 확장
- 코어 모듈 분리
- packet template 추가

피해야 할 묶음 예:

- 이름 정리 + 지도 추가 + 문체 정책 + 엔딩 구조 수정

## 체크포인트 규칙

### 중간 체크포인트

- 최소 기준: `작업 1패스 완료 + smoke PASS + 감사 메모 갱신`
- 권장 시점: 매주 수요일 21:00 KST
- 동작: integration branch에 커밋 후 push

### 주간 체크포인트

- 최소 기준: `그 주의 주요 pass 정리 + queue 갱신 + smoke PASS`
- 권장 시점: 매주 일요일 21:00 KST
- 동작: integration branch에 summary 성격 커밋 후 push

## 병합 규칙

- smoke PASS 없는 변경은 integration에 올리지 않는다.
- 진입 문서나 index를 깨는 rename은 단독 pass로 다룬다.
- `.obsidian`과 `orchestra/runs`는 기본적으로 커밋 범위에서 제외한다.

## 총괄자 규칙

- 총괄자는 pass 시작 전에 목표 파일군을 잠근다.
- specialist가 제안한 변경은 병합 전에 한 번 더 문맥 검토한다.
- branch를 많이 만드는 것보다, `경계가 분명한 pass`를 만드는 쪽이 우선이다.
