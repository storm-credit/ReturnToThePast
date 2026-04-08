# Foreshadow Harness

이 하네스는 "무슨 복선을 심고, 독자가 무엇으로 오해하며, 어디서 어떤 방식으로 회수할지"를 총괄자가 역산 관리하기 위한 규약이다.

## 목표

- 핵심 반전과 결말을 먼저 잠근다.
- 복선을 분위기용 떡밥이 아니라 회수 가능한 장치로 관리한다.
- 독자 지식, 주인공 지식, 세계의 진실을 따로 관리한다.
- 설정집, 아웃라인, 원고가 같은 복선 장부를 바라보게 만든다.

## 필수 참조 문서

- `lore_bible/Ending_A_Canon.md`
- `lore_bible/Ending_B_Alternate.md`
- `lore_bible/Secrets_Activation.md`
- `lore_bible/Mandatory_Events.md`
- `lore_bible/Foreshadow_Payoff_Ledger.md`
- `Guidelines/Foreshadow_Payoff_Checklist.md`
- `outline/Series_Roadmap.md`

## 권장 역할

- 총괄: `novel-orchestra-conductor`
- 복선 장부: `foreshadow-bookkeeper`
- 시간 진실 검증: `timeline-historian`
- 세계 진실 검증: `world-rule-keeper`
- 레드 헤링/공정성 검증: `plausibility-warden`

## 체크 축

1. 무엇을 숨기고 있나
2. 독자는 무엇으로 오해해야 하나
3. 주인공은 무엇을 언제 모르는가
4. 첫 씨앗은 어디에 심나
5. 중간 강화는 어디에 두나
6. 회수는 어디서 어떻게 하나
7. 회수 뒤 앞 장면 의미가 재해석되는가

## 불합격 조건

- 복선은 있는데 회수 시점이 없다
- 회수는 있는데 씨앗이 없다
- 레드 헤링만 있고 진짜 단서가 없다
- 결말 정서와 복선 방향이 다르다

## 기본 훅

- `seed-payoff-hook`
- `reveal-fairness-hook`
- `ending-convergence-hook`
