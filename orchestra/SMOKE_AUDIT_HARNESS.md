# 스모크 감사 하네스

대규모 설정 수선 전, 집필 시작 전, 최종 챕터 감수 전의 빠르고 반복 가능한 설정집 점검에 쓰는 하네스다.

## 점검 항목

- 필수 기준 문서가 모두 존재하는가
- 15권 전체에 `Outline`과 `Timeline`이 한 쌍으로 있는가
- 모든 아웃라인이 여전히 25화 행 구조를 유지하는가
- 잠근 캐논 충돌 문구가 다시 살아나지 않았는가
- 과장된 혈색 표현이 캐논 및 설계 문서에 스며들지 않았는가
- 복선 장부에 필수 ID와 유효 상태가 남아 있는가
- 전반부 복선, 측면 인물 목격, 엔딩 수렴 지도에 잠근 기준 레인이 유지되는가

## 관련 파일

- 스크립트: `orchestra/scripts/Invoke-SettingLibrarySmokeAudit.ps1`
- 규칙: `orchestra/scripts/setting-audit-rules.json`
- 산출물: `orchestra/runs/setting-smoke-<timestamp>/`

## 실행법

```powershell
powershell -ExecutionPolicy Bypass -File .\orchestra\scripts\Invoke-SettingLibrarySmokeAudit.ps1
```

지정 폴더에 쓰려면:

```powershell
powershell -ExecutionPolicy Bypass -File .\orchestra\scripts\Invoke-SettingLibrarySmokeAudit.ps1 -OutputDir "orchestra/runs/current-smoke"
```

## 우선순위 모델

- `P0`: 제작 구조가 깨져서 집필을 멈춰야 하는 상태
- `P1`: 여러 권을 오염시킬 수 있는 활성 캐논 충돌
- `P2`: 집필이 커지기 전에 정리해야 하는 톤, 이름, 장부 흔들림
- `P2`: 핵심 진실 공개나 목격 축이 얇아진 지도 흔들림
- `P3`: 참고용 통과 정보

## 언제 돌릴까

- 아웃라인이나 타임라인을 고친 뒤
- 캐논 규칙을 바꾼 뒤
- 복선, 목격, 엔딩 수렴 지도 같은 총괄 지도 문서를 추가하거나 뺀 뒤
- 권별 챕터 집필을 열기 직전
- 대형 설정 감사 병합 직전
