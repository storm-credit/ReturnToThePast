# 엔진 데이터 레이어 정책

이 문서는 설정집 안의 JSON 및 엔진 친화 데이터층을 어떻게 다룰지 잠그는 기준이다.

## 결론

- 엔진용 JSON 키는 억지로 한국어로 바꾸지 않는다.
- 대신 사람이 읽는 설명층을 별도 문서로 붙인다.
- 즉, `엔진 키는 안정성`, `설명 문서는 가독성`을 맡는다.

## 왜 이렇게 하는가

- `character_id`, `name`, `beliefs`, `ideal`, `tension_triggers` 같은 키는
  후속 스크립트, 검색, 구조 비교에 유리하다.
- 이 키를 지금 한국어로 전면 교체하면,
  엔진/자동화/재사용 코어 쪽에서 오히려 유지 비용이 커진다.
- 반대로 설명 문서가 없으면 사람 입장에선 JSON이 차갑고 불친절하게 읽힌다.

그래서 현재 프로젝트는:

1. JSON 키는 유지
2. 한국어 설명 문서를 옆에 둠
3. 필요한 경우 표시용 별도 필드만 추가

이 순서를 기본 원칙으로 삼는다.

## 현재 적용 범위

- `lore_bible/rules.json`
- `lore_bible/temporal_facts.json`
- `lore_bible/characters/Kael_psych.json`
- `lore_bible/characters/Ria_psych.json`
- `lore_bible/characters/Protagonist_psych.json`

## 허용되는 변경

- 값 보정
- 긴 설명을 한국어 문서로 분리
- 표시용 메타 필드 추가
  예: `display_name_ko`, `notes_ko`

## 피해야 할 변경

- 기존 핵심 키를 일괄 한국어로 바꾸기
- 사람용 설명을 JSON 안에 장문으로 밀어 넣기
- 캐논 문서를 JSON 기준으로 다시 쓰기

## 연결 문서

- `lore_bible/characters/Psych_Profile_Data_Guide.md`
- `lore_bible/Rules_Data_Guide.md`
- `lore_bible/Temporal_Facts_Guide.md`
- `lore_bible/characters/Protagonist_Psych_Legacy_Guide.md`
- `orchestra/CORE_LAYER_MAP.md`
- `orchestra/ENGINE_DATA_LAYER_POLICY.md`
