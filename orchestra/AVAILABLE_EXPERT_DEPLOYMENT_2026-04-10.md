# 사용 가능 전문가 배치표

이 문서는 2026-04-10 기준으로 오케스트라가 실제로 꺼내 쓸 수 있는 전문가 층과,
현재 앱 세션에서 즉시 재호출 가능한 서브에이전트를 함께 정리한 운영표다.

핵심 원칙은 단순하다.

- 총괄은 항상 `novel-orchestra-conductor`
- 전문가는 필요할 때만 꺼내 쓴다
- 하네스는 전문가 없이 돌지 않는다
- 새 전문가 설치보다, 기존 전문가를 올바르게 매핑하는 것이 우선이다

## 1. 현재 세션에서 바로 쓸 수 있는 서브에이전트

| 이름 | 현재 역할 매핑 | 주 용도 |
| --- | --- | --- |
| `Aquinas` | 구조/패러독스/시간선 | 권 브리지, 고정점, 분기점, 후반 구조 점검 |
| `Confucius` | 감정선/톤 | 관계 압박, 감정 대가, 거리감, 문체 정조 |
| `Locke` | 오케스트라 운영/체크포인트 | 배치 순서, 하네스 분기, 체크포인트 운용 |
| `Ampere` | 시스템/큐 운용 | 재작성 큐, 병렬 레인, 체크포인트 묶음 |
| `Avicenna` | 의식/의학/오염/항체 | 강제 귀환술, 항체, 후영, 의식/정화/오염 구조 |
| `Erdos` | 논리/일관성/정합성 | 개연성, 충돌 탐지, 논리적 누수 점검 |

## 2. 저장된 스킬 기반 전문가

아래 스킬은 이미 설치되어 있고, 필요 시 오케스트라가 대응 전문가로 취급한다.

### 설정집 기본 전문가

- `character-architect`
- `faction-strategist`
- `location-cartographer`
- `world-rule-keeper`
- `timeline-historian`

### 엔진/작문법 기본 전문가

- `structure-architect`
- `arc-psychologist`
- `foreshadow-bookkeeper`
- `serial-tension-engineer`
- `scene-smith`
- `chapter-inspector`

### 세분화 전문가

- `chrono-weaver`
- `building-cartographer`
- `ritual-liturgist`
- `street-apothecary`
- `monster-ecologist`
- `bestiary-warden`
- `relic-curator`
- `systems-chancellor`
- `plausibility-warden`
- `hook-doctor`
- `reveal-choreographer`
- `lore-forgemaster`

## 3. 지금 문제에 필요한 전문가

현재 핵심 문제는 `드라마판 12 Monkeys 모티브 갭 감사`다.

즉, 아래를 점검해야 한다.

- 후반 구조가 닫힌 인과 고리로 읽히는가
- 미래 멸망선이 현재 선택을 되받아치는가
- 조직 기원/의식/기록/은폐 구조가 충분한가
- 가까운 인물과 적대의 위치 전환이 충분히 설계되었는가
- 다중 시점이나 동일 사건의 다른 이름 구조가 필요한가

이 문제에 필요한 기본 조합은 아래와 같다.

### 필수

- `novel-orchestra-conductor`
- `structure-architect`
- `timeline-historian`
- `chrono-weaver`
- `foreshadow-bookkeeper`
- `reveal-choreographer`
- `plausibility-warden`

### 보조

- `arc-psychologist`
- `world-rule-keeper`
- `faction-strategist`
- `character-architect`
- `ritual-liturgist`

## 4. 지금 바로 추가 설치가 필요한가

결론: `필수 아님`

이미 있는 전문가 조합만으로도 이번 감사는 충분히 처리 가능하다.

특히 다음 조합으로 현재 문제를 거의 다 커버할 수 있다.

- 구조선: `Aquinas` + `structure-architect` + `timeline-historian`
- 감정선: `Confucius` + `arc-psychologist`
- 의식/오염/후영: `Avicenna` + `ritual-liturgist` + `world-rule-keeper`
- 정합성 검수: `Erdos` + `plausibility-warden`
- 오케스트라 운영: `Locke` + `Ampere`

## 5. 선택적으로 나중에 만들 수 있는 전문가

지금 당장 필요하진 않지만, 후반부를 더 드라마판 12 Monkeys 쪽으로 끌어올리고 싶다면
아래처럼 `합성 역할`을 새 이름으로 빼는 것은 가능하다.

- `lineage-loop-architect`
  - 조직 기원 반전
  - 같은 사건의 다른 이름
  - 계보형 인과 고리

- `multi-viewpoint-weaver`
  - 현재/과거/미래 보조 시점 운용
  - 동일 사건의 다중 인식 배치

지금 단계에선 새 설치보다 기존 조합 재배치가 우선이다.

## 6. 초안 수정 원칙

현재 집필된 초안은 전면 재작성 대상이 아니다.

원칙은 아래와 같다.

- 먼저 `설정집 후반 구조 갭`을 잠근다
- 그다음 `해당 갭에 직접 걸리는 초안`만 좁게 환류한다
- 이미 통과한 권 전체를 다시 뜯지 않는다

즉 지금은 `설정집 보강 -> 영향 화수 선택 -> 좁은 수정` 순서가 맞다.
