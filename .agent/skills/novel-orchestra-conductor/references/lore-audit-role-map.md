# Lore Audit Role Map

| Domain | Specialist | Core responsibility | Required reads | Default model |
| --- | --- | --- | --- | --- |
| `character` | `character-architect` | 인물 상태, 상처, 감정 대가, 관계, 동기 | `lore_bible/characters/**`, `lore_bible/characters/Relationship_Map.md`, 관련 아웃라인/타임라인 | `gpt-5.4` / `high` |
| `faction` | `faction-strategist` | 세력 목적, 정치 압력, 동맹/배신, 조직 간 충돌 | `lore_bible/groups/**`, 관련 `settings/**`, 관련 아웃라인 | `gpt-5.4` / `high` |
| `location` | `location-cartographer` | 도시/지형/동선/여행 시간/장소 분위기 | `lore_bible/locations/**`, 타임라인, 이동 관련 장면 | `gpt-5.4` / `medium` |
| `world` | `world-rule-keeper` | 마법, 대가의 법칙, 귀환 구조, 역병, 아이템, 괴물, 사회 시스템 | `lore_bible/rules/**`, `magic/**`, `settings/**`, `items/**`, `monsters/**` | `gpt-5.4` / `high` |
| `timeline` | `timeline-historian` | 사건 순서, 고정점, 분기점, 역사와 여파 | `outline/*Timeline*`, `lore_bible/history/**`, `lore_bible/Regression_Log.md` | `gpt-5.4` / `high` |
| `items-detail` | `relic-curator` | 무기, 유물, 저주받은 이물의 비용과 소유 정합성 | `lore_bible/items/**`, 관련 규칙/캐릭터/타임라인 | `gpt-5.4` / `medium` |
| `monsters-detail` | `monster-ecologist` | 괴물, 변이, 역병, 생태 공포 구조 | `lore_bible/monsters/**`, `rules/**`, 관련 장소/타임라인 | `gpt-5.4` / `medium` |
| `systems-detail` | `systems-chancellor` | 경제, 길드, 귀족, 해결사, 마약 카르텔 같은 사회 장치 | `lore_bible/settings/**`, 관련 세력/장소/아웃라인 | `gpt-5.4` / `medium` |
| `cross-check` | `chrono-weaver` | 시간축/심리/인과 보조 조회 | `lore_bible/temporal_facts.json`, psych profiles, rules | `gpt-5.4-mini` / `medium` |
| `merge` | `novel-orchestra-conductor` | 도메인 결과 병합, 충돌 해결, 최종 우선순위 판정 | 모든 domain report + source-of-truth docs | `gpt-5.4` / `high` |

## Default lore audit sequence

1. `novel-orchestra-conductor`가 master brief와 domain packet을 만든다.
2. `character`, `faction`, `location`, `world`, `timeline` 전문가를 병렬 투입한다.
3. `chrono-weaver`가 시간/심리/인과율 쟁점만 별도 조회한다.
4. 총괄자가 도메인 간 충돌표를 만든다.
5. 필요 시 `lore-forgemaster`와 `plausibility-warden`로 재보강한다.
6. 최종 확정사항을 `REVISION_LEDGER`에 남긴다.

## Optional micro-split triggers

- 아이템 파일이 5개 이상 직접 영향을 받으면 `relic-curator`를 추가한다.
- 괴물/역병/변이체가 권 핵심 갈등이면 `monster-ecologist`를 추가한다.
- 경제, 길드, 귀족, 해결사 구조가 플롯 병목이면 `systems-chancellor`를 추가한다.
- 총괄자는 필요 시 `world-rule-keeper`를 유지한 채 세부 역할을 병렬로 더 태운다.
