# 하네스-훅 매트릭스

이 문서는 각 하네스가 어떤 훅을 기본으로 태우는지 빠르게 보여주는 운영표다.

## 1. Lore Audit

- 공통: `preflight`, `dispatch`, `merge`, `verify`, `checkpoint`
- 전용: `lore-gap-hook`, `canon-conflict-hook`, `naming-conflict-hook`, `setting-first-hook`

## 2. Foreshadow

- 공통: `preflight`, `dispatch`, `merge`, `verify`, `checkpoint`
- 전용: `seed-payoff-hook`, `reveal-fairness-hook`, `ending-convergence-hook`

## 3. Storycraft

- 공통: `preflight`, `dispatch`, `merge`, `verify`, `checkpoint`
- 전용: `arc-pressure-hook`, `bridge-gap-hook`, `tone-guard-hook`, `serial-retention-hook`

## 4. Smoke

- 공통: `preflight`, `verify`, `checkpoint`
- 전용: `marker-hook`, `link-integrity-hook`, `banned-surface-hook`, `volume-structure-hook`

## 5. 총괄 규칙

- 어떤 훅을 실제로 켤지는 총괄이 병목에 맞춰 고른다.
- 모든 훅을 항상 다 켜지 않는다.
- 설정집 단계에선 `setting-first-hook`과 `marker-hook`의 우선순위가 높다.
- 집필 직전에는 `serial-retention-hook`보다 `canon-conflict-hook`과 `volume-structure-hook`이 먼저다.
