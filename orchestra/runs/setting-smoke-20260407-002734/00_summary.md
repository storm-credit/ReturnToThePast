# Setting Library Smoke Audit

- Generated At: 2026-04-07 00:27:34 +09:00
- Overall Status: FAIL
- Rules File: orchestra/scripts/setting-audit-rules.json
- Output Directory: orchestra/runs/setting-smoke-20260407-002734

## Check Summary

| Check | Status | Highest Priority | Summary |
| --- | --- | --- | --- |
| canon-conflict-check | FAIL | P1 | 1 active canon conflict pattern(s) matched. |
| banned-style-check | WARNING | P2 | 1 style rule warning(s) matched. |
| chapter-count-check | PASS | P3 | Every outline file contains 25 chapter rows. |
| foreshadow-ledger-check | PASS | P3 | Foreshadow ledger, IDs, statuses, and companion files are aligned. |
| required-files-check | PASS | P3 | All required source-of-truth files are present. |
| volume-pair-check | PASS | P3 | All 15 volume outline/timeline pairs exist. |

## Priority Queue

### P1
- [canon-conflict-check] C-002: The blink technique must not be described as a one-second or half-second stop. Matches: lore_bible/locations/Ancient_Labyrinth.md:20

### P2
- [banned-style-check] S-001: Avoid gore-forward diction in canon and planning docs. Matches: lore_bible/characters/Thomas.md:12

## Recommended Next Actions

1. C-002 -> The blink technique must not be described as a one-second or half-second stop. Matches: lore_bible/locations/Ancient_Labyrinth.md:20
2. S-001 -> Avoid gore-forward diction in canon and planning docs. Matches: lore_bible/characters/Thomas.md:12
