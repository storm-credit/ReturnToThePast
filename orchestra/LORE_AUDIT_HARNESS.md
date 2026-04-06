# Lore Audit Harness

이 하네스는 설정집 전체를 인물, 세력, 장소, 세계 법칙, 타임라인으로 분해해 병렬 점검하고,
마지막에 총괄자가 다시 하나의 캐논으로 잠그기 위한 운영 규약이다.

## 목표

- 설정집 추가와 점검을 초안 집필과 분리한다.
- 도메인별 전문가가 자기 영역만 깊게 본다.
- 도메인 간 충돌은 총괄자만 최종 판정한다.
- 개연성 점검을 집필 이전의 게이트로 만든다.

## 권장 전문가 구성

- 총괄: `novel-orchestra-conductor`
- 인물: `character-architect`
- 세력: `faction-strategist`
- 장소: `location-cartographer`
- 세계 법칙: `world-rule-keeper`
- 타임라인: `timeline-historian`
- 선택 세부: `relic-curator`
- 선택 세부: `monster-ecologist`
- 선택 세부: `systems-chancellor`
- 보조 조회: `chrono-weaver`
- 보강: `lore-forgemaster`
- 통합 개연성: `plausibility-warden`

## 실행 순서

1. 총괄자가 master brief를 만든다.
2. 도메인 packet을 다섯 개로 분리한다.
3. 다섯 전문가를 병렬 투입한다.
4. `chrono-weaver`로 시간축/심리/인과 충돌을 별도 조회한다.
5. 총괄자가 도메인 간 충돌표를 만든다.
6. 필요 시 `lore-forgemaster`와 `plausibility-warden`로 재보강한다.
7. 확정 사항을 `REVISION_LEDGER`에 남기고, 이후 집필 라인으로 넘긴다.

## 동적 세분화 규칙

- 아이템/무기/유물 파일이 많이 걸리면 `relic-curator`를 추가한다.
- 괴물/역병/생태 압력이 핵심이면 `monster-ecologist`를 추가한다.
- 경제/길드/귀족/생존 시스템이 병목이면 `systems-chancellor`를 추가한다.
- 총괄자는 필요 시 기본 5도메인 위에 세부 전문가를 더 얹는다.

## 파일 소유권

- `character-architect`: `lore_bible/characters/**`, 관계 문서, 심리 관련 정리
- `faction-strategist`: `lore_bible/groups/**`, 조직 관련 `settings/**`
- `location-cartographer`: `lore_bible/locations/**`
- `world-rule-keeper`: `lore_bible/rules/**`, `magic/**`, `settings/**`, `items/**`, `monsters/**`
- `timeline-historian`: `outline/*Timeline*`, `lore_bible/history/**`, `lore_bible/Regression_Log.md`
- 총괄자: 병합 결정, 교차 참조, Source of Truth 유지

## 하네스 산출물

- master brief
- character packet
- faction packet
- location packet
- world packet
- timeline packet
- merge packet

## 모델 정책

자세한 매핑은 `.agent/skills/novel-orchestra-conductor/references/model-routing.md`를 따른다.
설정집 전체 감사처럼 비용이 큰 작업은 총괄과 핵심 도메인에 `gpt-5.4`를 유지한다.
