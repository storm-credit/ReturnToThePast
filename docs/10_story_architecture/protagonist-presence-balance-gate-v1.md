# Protagonist Presence Balance Gate v1

Status: ACTIVE QUANTITATIVE GOVERNANCE / NOT A CANON EVENT CHANGE
Owner: A08 Character / A12 Architecture / A13 Continuity / A14 Reader / A16 Red Team
Applies To: E001–E375
Depends On: `secondary-pov-and-offscreen-action-allocation-v1.md`, `parallel-plot-and-pov-governance-v1.md`, `faction-causal-track-v1.md`, D15 POV supplement

## 1. 목적

앙상블을 강화한다고 에이든을 작품 밖으로 밀어내거나, 반대로 모든 회차가 에이든의 관찰·판단을 기다리는 두 극단을 모두 막는다.

이 문서는 **POV 비율과 서사 중심 비율을 분리**한다.

- POV = 누구의 내면/관찰로 장면을 본다.
- Presence = 에이든이 실제 장면에 등장하는가.
- Narrative Center = 그 화의 비가역 선택·감정비용·다음 상태를 누가 주도하는가.

세 값을 혼용하지 않는다.

## 2. Locked Target Band

### Narrative Center
- AIDEN-CENTERED: **75–80%**
- 375화 기준: **281–300화**

### Physical Presence
- Aiden appears: **90–95%**
- 375화 기준: **338–356화**

### Full Absence
- Aiden fully absent: **5–10%**
- 375화 기준: **19–37화**
- 운영 권장 범위: **24–30화**

### Ensemble-Centered With Aiden Present
- 권장: **12–18%**
- 에이든이 등장하더라도 다른 인물/세력의 결정이 회차 상태를 바꾸는 화.

## 3. Existing Verified POV Distribution

Current verified allocation:

- P1 full secondary POV: **30 / 375 = 8.0%**
- P2 multi-POV: **15 episodes**
- P3 limited observer inserts: **8 inserts**

P1 30화는 이미 필요한 보조 POV 수준을 확보한다.

Therefore:

> **Do not increase P1 mechanically.**

앙상블 강화는 우선:
- F-Line independent move
- C-Line countermove
- offscreen material residue
- named faction face
- another actor's irreversible decision

로 해결한다.

## 4. Classification Rule

375화 전수 수치감사는 각 회차를 A/B/C 중 하나로만 분류한다.

### A — AIDEN-CENTERED
3개 기준 중 2개 이상:
1. 국소 비가역 선택의 주체가 에이든.
2. 이 화의 핵심 감정·관계·권리 비용이 에이든에게 귀속.
3. 에이든의 직접 행동이 없으면 Resolution 또는 Next Cause가 성립하지 않음.

POV가 에이든이라고 자동 A가 아니다.

### B — ENSEMBLE-CENTERED / AIDEN PRESENT
- 에이든은 등장한다.
- 그러나 다른 named face / community / institution이 먼저 움직인다.
- 그들의 선택이 물리·법·자원·동맹 상태를 변경한다.
- 에이든은 그 기정사실을 협상·수습·거부·책임지는 위치에 선다.

### C — AIDEN ABSENT
- 에이든이 물리적으로 등장하지 않는다.
- 독립행동이 실제 상태를 변경한다.
- 단순 설명·보고용 side story가 아니다.
- 1–3화 안에 주 플롯과 재합류하거나, 권말/결말처럼 의도된 handoff 근거가 있다.

## 5. Act-Level Recommended Shape

### GA I
- Aiden center: **80–85% 권장**
- 이유: 제한된 정보와 첫 오판을 독자가 에이든과 함께 믿어야 함.
- 부재/앙상블은 Ria/Iris/기관 증거가 독립적으로 움직인다는 정도로 제한.

### GA II
- Aiden center: **75–80% 권장**
- F0/F1/current residents/foreign actors 병렬화.

### GA III
- Aiden center: **72–78% 권장**
- Era O people must feel like a world that existed before Aiden.
- 단, 오르바드 중심 외전처럼 보이면 실패.

### GA IV
- Aiden center: **70–76% 권장**
- series maximum ensemble pressure.
- multiple missions and younger Aiden require independent agency.

### GA V
- E301–E368: **72–78% 권장**
- E369–E375: intentional post-Aiden public-address handoff.
- total GA V may therefore be lower than GA I without weakening the protagonist arc.

Series total remains **75–80%**.

## 6. Failure Conditions

### Too Aiden-Centric
Fail if:
- series A > 80% after deterministic classification;
- factions repeatedly wait for Aiden before acting;
- P1/P2 ends only reveal facts but change no state;
- a faction's goal is mostly `convince Aiden`;
- GA III–IV can be summarized as Aiden visiting one representative after another.

### Too Ensemble-Heavy
Fail if:
- A < 75%;
- absence episodes exceed 10% without explicit ending handoff reason;
- main emotional responsibility moves away from Aiden;
- readers could remove Aiden from the series without changing the major causal chain;
- secondary POV knows answers that should belong to Aiden's investigation.

## 7. Why 75–80% Fits This Project

This project needs a stronger protagonist center than a pure ensemble political saga because:
- first assassination guilt is Aiden's irreducible burden;
- changed-future returns are emotionally experienced through Aiden;
- younger-Aiden conflict requires continuity of self-responsibility;
- final historical-address sacrifice only works if readers have lived most of the series with him.

But it must stay below near-total protagonist monopoly because:
- F0/F1/current citizens have independent existence rights;
- Era O must not exist only to teach Aiden lore;
- foreign powers and regions must create irreversible facts offscreen;
- the final distributed order must already function before Aiden's last bridge is cut.

Therefore **75–80% center / 90–95% appearance / 5–10% absence** is the project-specific balance target.

## 8. Current Status

- Target: **LOCKED by current author instruction / project adaptation**
- POV base distribution: **VERIFIED**
- Exact 375-row A/B/C narrative-center ledger: **NOT YET GENERATED**

Do not claim an exact current protagonist-center percentage until that regression exists.

## 9. Next Quantitative Task

Generate `E001–E375 protagonist-center ledger` with fields:

`Episode | GA | Volume | POV type | Aiden present Y/N | Narrative Center A/B/C | Decisive Actor | Irreversible Cost Owner | State-Changing Independent Move | Verdict`

Then calculate:
- A count / 375
- A+B appearance count / 375
- C count / 375
- per-Grand-Act ratios
- longest absence streak
- longest A-centered streak

Any adjustment should preserve existing events and first try changing **scene emphasis / decisive actor visibility / offscreen residue**, not inventing new events.
