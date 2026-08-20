# D16.7 — E001–E010 Sequential Revalidation

Status: **BATCH 01 AUDITED / ONE BLOCKING MANUSCRIPT-ARCHITECTURE CONFLICT**  
Date: 2026-08-20  
Base Main: `da538974f8cfb200f359c0de797259f7885a9a03`  
Scope: E001–E010 actual manuscript + existing Context Pack + State Mutation + current Canon/Architecture/POV/Mystery/Visual overlays  
Authority: production-validation overlay only; 사건·설정·결말을 새로 만들지 않는다.

## 1. Why D16.7 exists

D16.6 proved that E001–E088 has structural Context/State coverage and no broken handoff in the historical production chain. It did **not** prove that every old Context Pack and manuscript still matches later D11–D16.6 overlays.

D16.7 therefore revalidates the existing manuscript sequentially from E001.

Required chain:

`current Canon → Act → Volume → Subact → D6 Card → existing CP → previous Exit → actual manuscript → State Mutation → next Entry → current POV/Mystery/Visual overlays`

A Context Pack existing on disk is not itself a PASS.

## 2. Verdict codes

- `GREEN` — current Canon/Architecture/State can use the manuscript without structural rewrite. Human prose remains author review unless separately approved.
- `YELLOW-DOC` — manuscript event is usable, but a supporting document/metadata statement is stale and must be overridden or corrected.
- `RED-ARCH` — actual manuscript conflicts with a later active architecture/POV lock. Do not declare the episode current-clean until repaired and reaudited.

## 3. Batch 01 result

| Episode | Subact | Current POV lock | Structural verdict | Human prose | Required action |
|---|---|---|---|---|---|
| E001 | V01-1A | 에이든 로엔 close 3rd | GREEN | AUTHOR REVIEW | latest overlay used on reuse |
| E002 | V01-1A | 에이든 로엔 close 3rd | GREEN | AUTHOR REVIEW | none |
| E003 | V01-1A | 에이든 로엔 close 3rd | YELLOW-DOC | AUTHOR REVIEW | stale M02 E033 duplicate rung overridden |
| E004 | V01-1A | 에이든 로엔 close 3rd | GREEN | AUTHOR REVIEW | none |
| E005 | V01-1A | 에이든 로엔 close 3rd | GREEN | AUTHOR REVIEW | none |
| E006 | V01-1A | 에이든 로엔 close 3rd | YELLOW-DOC | AUTHOR REVIEW | old CP/frontmatter date wording overridden by master chronology |
| E007 | V01-1B | **아이리스 네르 P1** | **RED-ARCH** | NOT ELIGIBLE FOR FINAL PASS | current manuscript/old CP use Aiden POV; requires repair |
| E008 | V01-1B | 에이든 close 3rd + 메이라 솔 P3 | GREEN | AUTHOR REVIEW | none |
| E009 | V01-1B | 에이든 로엔 close 3rd | GREEN | AUTHOR REVIEW | none |
| E010 | V01-1B | 에이든 로엔 close 3rd | GREEN | AUTHOR REVIEW | none |

Checksum:
- GREEN = 7
- YELLOW-DOC = 2
- RED-ARCH = 1
- HUMAN PROSE PASS = 0 granted by D16.7

**Batch current-clean verdict: BLOCKED BY E007.**

## 4. E003 — M02 duplicate-rung correction

Actual E003 already reveals that a deleted witness death date precedes the attributed Seren offense date. The current `mystery-reinforcement-ladder-v1.md` still assigns the same fact to E033.

But current E032–E037 production support defines E033 as `폐기될 나의 보고서`: official joint access, F0 mission-report metadata, and the hook that the report author is Daren Mott. Therefore the old E033 M02 death-date rung is stale.

D16.7 routing rule:
- E003 existing clue remains valid.
- Do not repeat the same death-date reveal in E033.
- For production routing, treat M02 ladder as `E003 early contradiction → E014 왕실 보고서/금지의식 → E061 날짜층 위조 ...` until the base ladder is formally consolidated.
- This changes no E003 manuscript event.

## 5. E006 — chronology metadata correction

Current master chronology J01 locks:
- departure: F0 / CY 664 / 장야월 21일
- arrival: N0 / CY 640 / 안개월 4일

Historical E006 CP and manuscript frontmatter still contain older wording that departure is `장야월 18일 또는 그 직후` and/or arrival date is unconfirmed.

The E006 State Mutation already carries the current exact J01 dates, and the manuscript body does not build a conflicting plot event around the obsolete metadata.

D16.7 routing rule:
- current chronology wins;
- old E006 CP date-warning is stale;
- old E006 manuscript frontmatter calendar line is metadata debt, not a prose-event conflict;
- do not alter the jump event, 18km-class miss, identity failure, return-window cost, or gray-bell resonance.

## 6. E007 — blocking POV conflict

Active global POV allocation locks E007 as:
- `C03 아이리스 네르 — P1`
- independent function: patient convoy / local refusal-right / route decision without knowing Aiden's mission purpose
- result rejoins Aiden in E008.

D15 POV supplement explicitly states that unlisted older POV rows remain unchanged; E007 is not overridden.

However:
- E007 old CP selects Aiden close 3rd despite acknowledging the Iris P1 row.
- E007 Storycraft Manifest is built around Aiden internal concealment-resource management and labels POV conditional.
- actual E007 manuscript frontmatter and prose are Aiden close 3rd.
- E007 State Mutation preserves Iris's offscreen independent tracking, so the causal event layer is salvageable.

Verdict: **RED-ARCH / POV implementation conflict, not event-canon collapse.**

Repair constraints:
- preserve the existing E007 event outcomes and E008 entry state;
- do not turn Iris into a destined guide;
- Iris must not know Aiden's mission purpose;
- Aiden internal equipment calculations that cannot be known from Iris POV must not be head-hopped into the P1 episode;
- E008 remains Aiden close 3rd + Meira P3 and should receive the route consequence from Iris's E007 action;
- any full E007 prose replacement remains AUTHOR REVIEW and requires author approval before HUMAN PROSE PASS.

## 7. E008–E010 continuity

### E008
Current manuscript correctly implements:
- Aiden close 3rd
- Meira Sol limited P3
- Iris independently changes convoy order
- Abel Ner as C26 patient witness
- no mana-fever final answer

### E009
Current manuscript correctly preserves:
- both birth certificates as genuine-compatible evidence
- Aiden's infection hypothesis as a rational but failing interpretation
- symptom/record coupling without final mechanism disclosure
- Iris and Meira as independent checks, not answer machines

### E010
Current manuscript correctly preserves:
- Cathedral relief order's real life-saving utility
- coercive classification as a simultaneous rights problem
- Aiden accepting traceable medical-assistant registration
- patient-family agency
- target-organization mark as unresolved evidence
- direct E010 → E011 cause: registered transport role + lost mission time → bridge rescue choice

## 8. Visual current-state locks for E001–E010

D16.4/D16.5 is a production overlay; it does not add people to scenes.

Current allowed visual states:
- C01 Aiden Roen: `F0 FIELD` throughout this batch. Era N arrival does not automatically promote him to later `ALTERED/WORN` or `ADDRESS-LOSS` variants.
- C02 Ria Seorn: `PRIVATE+OFFICIAL MIX` where actually present.
- C03 Iris Ner: `WESTERN FIELD`.
- C10 Meira Sol: `FIELD MEDICAL`.
- C26 Abel Ner: `PATIENT WITNESS`.
- R01 gray bell: community/shared evidence object; never Aiden's personal equipment or prophecy device.

Do not advance:
- C01 later address-loss visual grammar
- C03 later council/audit variants
- C10 final civic-medical-network state
- C26 later rights-recognized state
- R01 later audit-tool final interpretation

## 9. Human prose boundary

D16.7 structural/canon verdict does not grant HUMAN PROSE PASS.

For E001–E010:
- existing author-review prose stays author-review prose;
- no episode is promoted to final merely because its structural verdict is GREEN;
- E007 is not eligible for prose-final consideration before the POV architecture conflict is repaired.

## 10. Sequential stop rule

D16.7 is deliberately sequential.

Before declaring E001–E010 fully current-clean:
1. resolve E003 document debt via active overlay/base-document consolidation;
2. resolve E006 chronology metadata debt;
3. repair E007 POV architecture conflict;
4. re-run E006→E007→E008 handoff after repair.

Only after that should Batch 02 (E011–E020) be given a final current-clean chain certification.

This does not prevent read-only inspection of later episodes; it prevents falsely declaring the earlier chain fully validated.
