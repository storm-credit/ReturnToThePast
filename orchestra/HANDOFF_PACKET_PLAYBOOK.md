# 총괄 핸드오프 패킷 플레이북

이 플레이북은 총괄자가 가장 먼저 꺼내 써야 할 짧고 재사용 가능한 패킷 종류를 정리한다.

사용자가 흔히 요청하는 소설 작업을 빠르게 시작해야 하고, 그때마다 새 패킷을 처음부터 설계할 필요가 없을 때 이 문서를 쓴다.

---

## 빠른 시작 체크리스트

패킷을 보내기 전에 아래 다섯 가지를 먼저 잠근다.

1. 진짜 병목이 설정, 브리지 논리, 산문, 복선, 감사 중 무엇인가
2. 이번 패스의 기준 문서는 무엇인가
3. 바뀔 수 있는 파일은 무엇인가
4. 바뀌면 안 되는 파일은 무엇인가
5. 어떤 출력 모양으로 돌아와야 하는가

이 다섯 가지가 흐리면 아직 위임하지 않는다.

---

## 추천 패킷 계열

| 패킷 | 쓰는 상황 | 주 레인 | 기본 전문가 순서 | 템플릿 |
| --- | --- | --- | --- | --- |
| `lore-repair` | 캐논 파일끼리 충돌하거나 설정 블록이 너무 얇아 안전하게 집필할 수 없을 때 | `lore` | conductor -> lore -> chrono -> plausibility | `templates/HANDOFF_LORE_REPAIR.md` |
| `bridge-reinforcement` | 인접 화나 권의 논리와 감정 연결이 약할 때 | `plausibility` | conductor -> structure -> arc -> plausibility -> foreshadow | `templates/HANDOFF_BRIDGE_REINFORCEMENT.md` |
| `foreshadow-repair` | 진실 공개가 덜 심겨 있거나 불공정하거나 너무 늦게 느껴질 때 | `lore` | conductor -> foreshadow -> timeline -> world-rule -> plausibility | `templates/HANDOFF_FORESHADOW_REPAIR.md` |

`chapter-draft`는 이후를 위한 패킷이며, 지금은 `SETTING_FIRST_MODE.md`가 활성이라 중지 상태다.

---

## 빌더 사용법

Python이 가능하면 먼저 패킷 빌더로 초안을 뽑고, 그다음 수동으로 조인다.

예시:

```text
python .agent/skills/novel-orchestra-conductor/scripts/build_work_packet.py --preset lore-repair --entity Iris --mission "Repair Iris canon and debt continuity"
python .agent/skills/novel-orchestra-conductor/scripts/build_work_packet.py --preset bridge-reinforcement --volume 6 --mission "Reinforce the Vol. 6 -> Vol. 7 handoff"
```

Python을 쓸 수 없으면 `orchestra/templates/`에서 가장 가까운 템플릿을 복사해 수동으로 채운다.

---

## 패킷 설계 메모

### 설정 수선

- 다른 방법으로 닫을 수 없는 공백이 아니라면, 세계 확장을 충돌 수선과 섞지 않는다.
- 설정 수선 패킷에는 무엇이 충돌인지 한 문장으로 적는다.
- 한 개 권 이상을 건드리는 수선이면 `Blocking Decisions`에 표시한다.

### 브리지 보강

- 브리지는 논리와 감정을 같이 본다.
- 이전 권 마감과 다음 권 시작을 둘 다 읽는다.
- 억지 반전보다 압력 수선을 우선한다.

### 복선 수선

- 패킷 안에서 단서가 심기는 지점과 회수되는 미래 지점을 둘 다 잠근다.
- 첫 단서와 회수가 같은 권에 있으면, 특별한 근거가 없는 한 아직 얕다고 본다.

---

## 좋은 패킷이 피해야 할 것

- `더 좋게 해줘` 같은 모호한 동사
- 충돌 대상 없이 세계관만 늘리는 열린 설정 발명
- 캐논 막힘이 풀리기 전에 산문 작업을 보내는 일
- `설정 우선 모드`가 켜져 있는데 산문 작업을 보내는 일
- 모든 일을 모든 레인으로 돌리는 습관
- 진짜 결정 지점을 숨긴 채 전문가에게 넘기는 방식
