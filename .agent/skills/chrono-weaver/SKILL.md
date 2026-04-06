---
name: chrono-weaver
description: 시간축, 인과율, 심리 상태를 빠르게 조회하는 저수준 보조 스킬입니다. 오케스트라의 기초 컨텍스트 레이어로 사용합니다.
---

# Chrono-Weaver Protocol

이 스킬은 단독 총괄자가 아니라, `novel-orchestra-conductor`, `plausibility-warden`, `chapter-inspector`가 호출하는 공용 분석 도구다.

## 1. Timeline Query
- `scripts/get_temporal_context.py`로 특정 연도에 유효한 사실만 조회한다.
- 미래 사실이 현재 시점 캐릭터에게 새지 않도록, 반드시 요청 연도 기준으로만 해석한다.

## 2. Psychology Query
- `scripts/analyze_psych.py`로 긴장도를 계산한다.
- 심리 데이터가 깨졌거나 누락되면 그 사실을 경고로 남기고, 없는 데이터를 지어내지 않는다.
- 심리 분석은 행동 가능성 제안까지만 담당한다. 플롯 확정은 오케스트레이터가 한다.

## 3. Causality Query
- `scripts/validate_causality.py`로 제안된 행동이 설정집의 금지 규칙과 직접 충돌하는지 검사한다.
- 통과 여부만 말하지 말고, 어떤 제약에 걸렸는지 짧게 요약한다.

## 4. Output Contract
- 이 스킬의 결과는 최종 원고가 아니라 근거 자료다.
- 항상 아래 세 줄을 포함한 짧은 보고 형태로 반환한다.

```text
[TIMELINE] ...
[PSYCH] ...
[CAUSALITY] ...
```

## 5. Usage Notes
- 새 설정을 추가할 때는 먼저 기존 설정과 충돌하지 않는지 확인한다.
- 챕터 집필 전에 먼저 조회하고, 집필 후에는 검수 스킬이 다시 확인한다.
- 결론이 불충분하면 "근거 부족"으로 멈추고 상위 오케스트레이터에 되돌린다.
