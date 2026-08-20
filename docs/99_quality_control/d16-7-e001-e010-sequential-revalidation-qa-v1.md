# D16.7 E001–E010 Pack-Based Revalidation QA v1

Status: **PACK-BASED REVALIDATION COMPLETE / BATCH BLOCKED BY E007**  
Base Main: `da538974f8cfb200f359c0de797259f7885a9a03`  
Branch: `agent/d16-7-e001-e010-sequential-revalidation-20260820`  
Current Pack: `.agent/context-packs/episodes/E001-E010-current-context-pack-d16-7.md`

## 1. Method

Every episode was resolved in this order:

```text
Current Context Pack
→ historical CP / Craft provenance
→ actual manuscript
→ actual State Mutation
→ next episode Entry
→ current POV / Mystery / Visual locks
```

A historical CP existing on disk is not a PASS. A manuscript event being readable is also not enough if it conflicts with a later active architecture lock.

## 2. Final episode verdicts after pack-first correction

| EP | Canon/Event | Act/Subact | Handoff | POV | Mystery/Info | State/Visual | Next Cause | Final structural verdict | Prose |
|---|---|---|---|---|---|---|---|---|---|
| E001 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **GREEN — CURRENT-CLEAN** | AUTHOR REVIEW |
| E002 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **GREEN — CURRENT-CLEAN** | AUTHOR REVIEW |
| E003 | PASS | PASS | PASS | PASS | ACTIVE OVERLAY | PASS | PASS | **YELLOW-DOC — CURRENT-CLEAN WITH OVERLAY** | AUTHOR REVIEW |
| E004 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **GREEN — CURRENT-CLEAN** | AUTHOR REVIEW |
| E005 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **GREEN — CURRENT-CLEAN** | AUTHOR REVIEW |
| E006 | PASS | PASS | PASS | PASS | PASS | ACTIVE CHRONOLOGY OVERLAY | PASS | **YELLOW-DOC — CURRENT-CLEAN WITH OVERLAY** | AUTHOR REVIEW |
| E007 | PASS EVENT | PASS | PASS TARGET STATE | **FAIL** | PASS | PASS TARGET STATE | PASS TARGET STATE | **RED-ARCH — REPAIR REQUIRED** | NOT ELIGIBLE FOR FINAL REVIEW |
| E008 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **GREEN — CURRENT-CLEAN** | AUTHOR REVIEW |
| E009 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **GREEN — CURRENT-CLEAN** | AUTHOR REVIEW |
| E010 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **GREEN — CURRENT-CLEAN** | AUTHOR REVIEW |

Checksum:
- GREEN current-clean: **7**
- YELLOW-DOC current-clean with active overlay: **2**
- RED-ARCH repair required: **1**
- HUMAN PROSE PASS granted: **0**

## 3. E003 — current-clean with document overlay

Current Pack locks the witness death-date contradiction as already revealed in E003.

The later Mystery Ladder row repeating the same fact at E033 is stale production routing because current E032–E037 support defines E033 as `폐기될 나의 보고서`, with F0 mission-report metadata and Daren Mott registered as report author.

Result:
- E003 manuscript event remains.
- no manuscript rewrite needed for this issue.
- E033 must not replay the death-date contradiction as a first reveal.
- base Mystery Ladder can be consolidated separately without blocking E001–E010 manuscript use.

## 4. E006 — current-clean with chronology overlay

Current Pack hard-locks:

```text
F0 departure = CY 664 / 장야월 21일
N0 arrival   = CY 640 / 안개월 4일
```

The jump event, miss, equipment lock, invalid identity and bell/return-stone observation are compatible with the current pack.

Older uncertainty wording in historical CP/frontmatter is metadata debt. It does not invalidate the body event.

Result:
- no plot rewrite required.
- future reads use Current Pack chronology.
- metadata can be consolidated separately.

## 5. E007 — blocking architecture repair

Current Pack locks:

- POV: **C03 아이리스 네르 — P1**
- Iris knowledge ceiling: no Aiden mission purpose, no hidden internal equipment calculations.
- Iris function: local patient convoy / refusal-right / route choice / independent observation.
- Aiden: externally observed outsider only within Iris P1.
- next boundary: E008 receives the consequence of Iris's independent route/order action.

Historical manuscript/CP use Aiden close 3rd.

The event outcomes themselves are reusable:
- Aiden remains a misarrived undocumented outsider.
- hidden future equipment creates cost.
- gray bell/return-stone anomaly is only observed.
- Iris independently observes/tracks him.
- convoy/route conditions change through local agency.
- E008 begins from those consequences.

What cannot remain verbatim:
- Aiden-only interior calculations inside an Iris-P1 episode.
- direct access to Aiden's private equipment-state reasoning.
- scene construction that exists only to expose Aiden interior information unavailable to Iris.

Verdict: **REPAIR REQUIRED, EVENT PRESERVATION POSSIBLE.**

No full rewrite is performed by this QA document.

## 6. E008–E010 current-clean confirmation

### E008
- Aiden close 3rd + Meira Sol limited P3 matches Current Pack.
- Iris route/order intervention remains independent.
- Abel Ner is canonical C26.
- temporary registration is not citizenship.

### E009
- both birth certificates stay genuine-compatible.
- infection hypothesis is rationally tested and weakened, not replaced by omniscient truth.
- record/symptom correlation does not reveal final mechanism.

### E010
- Cathedral relief has real life-saving utility.
- coercive classification remains a simultaneous rights problem.
- Aiden accepts traceable registration rather than solving the institution through violence.
- E011 directly inherits transport duty, mission-time loss and unresolved trail.

## 7. Chain certificate

Episode-level reuse certificate:
- E001–E006: current-clean under Current Pack (E003/E006 via active overlays).
- E007: not current-clean.
- E008–E010: individually current-clean, but the continuous E001→E010 chain cannot be certified until E007 is repaired and E006→E007→E008 is rechecked.

Therefore:

**SEQUENTIAL CURRENT-CLEAN BOUNDARY = E006.**

This does not erase E008–E010 individual PASS; it only prevents claiming an unbroken certified chain across unresolved E007.

## 8. Human prose boundary

- No HUMAN PROSE PASS.
- GREEN/YELLOW here mean structural/current-context reuse only.
- Literary final review remains author-controlled.
- E007 prose finalization is blocked until architecture repair.

## 9. Next action

1. Prepare **E007 repair specification only** in project review format; preserve events and E008 Entry.
2. After repair authorization/implementation, rerun E006→E007→E008.
3. If PASS, move sequential current-clean boundary to E010.
4. Then compile E011–E020 Current Context Pack **before** manuscript revalidation of that batch.

**D16.7 Batch 01: PACK COMPLETE / REVALIDATION COMPLETE / ONE REPAIR BLOCKER.**
