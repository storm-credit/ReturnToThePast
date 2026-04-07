# 규칙 데이터 가이드

이 문서는 `lore_bible/rules.json`을 사람이 읽기 쉽게 풀어 둔 설명층이다.

## 이 파일이 하는 일

- 설정집 금지어를 엔진이 빠르게 잡을 수 있게 한다.
- 특정 서술 습관을 자동감사와 보조 엔진이 판별할 수 있게 한다.
- 판타지 결을 해치는 현대어, 게임어, 과장된 표현이 되살아나는지 확인한다.

## 핵심 키 뜻

- `setting_name`: 현재 프로젝트의 세계 이름
- `genre`: 장르 표면
- `forbidden_terms`: 설정집과 운영 문서에서 경계할 표현 목록
- `magic_system.resource`: 마력 자원의 표면 표현
- `magic_system.cost_logic`: 마법이 어떤 대가 문법을 따르는지
- `constraints[].trigger`: 엔진이 주목할 촉발 구문
- `constraints[].message`: 그 촉발 구문이 잡혔을 때 돌려줄 안내 문장

## 운용 원칙

- JSON 키 이름은 바꾸지 않는다.
- 금지어를 더 넣을 때는 바로 문서 전체 금지로 보지 말고, 실제로 반복적으로 문제를 일으킨 표현만 넣는다.
- `constraints`는 작가를 과하게 묶는 법전이 아니라, 자주 무너지는 문법을 빠르게 잡는 안전장치다.

## 수정할 때 주의할 점

- `forbidden_terms`, `constraints[].trigger`, `constraints[].message`는 엔진이 직접 읽는다.
- 키를 바꾸면 감사 엔진과 보조 자동화가 깨질 수 있다.
- 같은 뜻의 표현을 너무 넓게 잡으면 오탐이 늘어난다.

## 같이 읽을 문서

- `Guidelines/Prompt_Quick_Reference.md`
- `Guidelines/Chapter_Audit_Checklist.md`
- `orchestra/ENGINE_DATA_LAYER_POLICY.md`
