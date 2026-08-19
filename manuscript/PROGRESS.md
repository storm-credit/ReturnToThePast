# Manuscript Progress

Status: **MAIN VERIFIED THROUGH E088 / E089+ RECONCILIATION**  
Gate: ACTIVE — continuation requires latest-main reconciliation  
Target: E001–E375  
Verified Main SHA: `c3130ba8ccb095959d02d8bec8862e1a37e3e6cb`  
Protocol: latest main → episode/subact branch → validation → push → PR → author approval → merge

## Current Main Boundary

| Range | GitHub state | Notes |
|---|---|---|
| E001~E025 | MAIN | V1 surgical/canon edition reflected by PR #120 |
| E026~E050 | MAIN | V2 canon-standard retrofit reflected by PR #122 |
| E051~E056 | MAIN | PR #84 lineage |
| E057~E062 | MAIN | PR #85 lineage |
| E063~E069 | MAIN | PR #86 lineage |
| E070~E075 | MAIN | PR #87 lineage |
| E076~E081 | MAIN | PR #88 lineage |
| E082~E088 | MAIN | latest canon rewrite reflected by PR #121 |

The last manuscript file currently verified on `main` is:

`manuscript/volume-04/E088-가족관계가-바뀌는-의식.md`

`main` 존재 여부와 `HUMAN PROSE PASS`는 별도 상태다. AI는 작가 대신 Human Prose 최종승인을 부여하지 않는다.

## Unmerged Continuation Drafts

| Range | PR | Branch | Current use |
|---|---:|---|---|
| E089~E094 old draft | #90 | `agent/manuscript-e089-e094` | E089~E093 salvage candidate only; E094 superseded |
| E094~E100 | #114 | `agent/manuscript-e094-e100-v2` | current event-line candidate, but stale branch |
| E101~E106 | #115 | `agent/manuscript-e101-e106` | stale dependent draft |
| E107~E112 | #116 | `agent/manuscript-e107-e112` | stale dependent draft |
| E113~E118 | #117 | `agent/manuscript-e113-e118` | stale dependent draft |
| E119~E125 | #118 | `agent/manuscript-e119-e125` | stale dependent draft |

## Freshness Check — 2026-08-19

Latest `main`: `c3130ba8ccb095959d02d8bec8862e1a37e3e6cb`

- #90: **ahead 9 / behind 279 / diverged**
- #114: **ahead 10 / behind 279 / diverged**

The continuation chain was authored from the older `2717e3d...` main lineage. It must not be merged or extended in place without latest-main reconstruction and revalidation.

## Superseded Drafts

The repository still contains multiple historical OPEN/DRAFT branches for early episodes and replaced batches. They are not production truth when a newer merged or explicitly superseding branch exists.

Important examples:

- #89 E082~E088 → superseded by merged #121 rewrite
- #113 E095~E100 → CLOSED / NOT MERGED because of canon mismatch; #114 supersedes it
- #112 E025 → CLOSED / NOT MERGED because it conflicts with the canon card; merged #77 lineage is authoritative for manuscript state

## Human Prose Governance

- `AUTHOR REVIEW READY` is the highest AI-only prose verdict.
- `HUMAN PROSE PASS` requires explicit author approval after reading.
- Existing main manuscripts may still require later prose surgery even though they are GitHub-main verified.
- Prose revision must preserve approved events, numbers, mysteries, character intent, and canon unless the author explicitly changes canon.

## Required Recovery Sequence

1. Start from latest `main`.
2. Re-read E088 exit state and V4 E089~E093 Scene-Ready Design / CP / Craft / State requirements.
3. Compare PR #90 E089~E093 against current canon; salvage only still-valid prose/events.
4. Build a clean E089~E093 continuation branch with `behind_by=0`.
5. Validate manuscript, canon, information ceiling, scene density, state mutation, and human-prose risks.
6. Push and open PR. Do not merge without explicit author approval.
7. Reconstruct E094~E100 using #114 event line, not #90 E094.
8. Then revalidate #115~#118 sequentially because each depends on the previous batch state.

## Next Production Unit

**E089~E093 latest-main reconciliation.**

After that: E094~E100 → E101~E106 → E107~E112 → E113~E118 → E119~E125.
