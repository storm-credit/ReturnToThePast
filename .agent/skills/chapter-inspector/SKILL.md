---
name: chapter-inspector
description: Perform final chapter audit for ReturnToThePast. Use when Codex must review a chapter against the checklist, timeline, lore, continuity, banned terms, equal-exchange burden, and chapter-level readability before sign-off or targeted repair.
---

# Chapter Inspector

- Read `../novel-orchestra-conductor/references/packet-contract.md` before acting.
- Default to a review mindset: findings first, summary second.
- Read the checklist, target draft, previous chapter, target outline, target timeline, and relevant lore files before judging.

## Output contract

Use these headings:

```markdown
## Decision
## Findings
## Required Changes
## Assumptions
## Handoff
```

Within `Findings`, separate:

- blocking issues
- warnings
- exact file or scene references when possible

## Rules

- Prefer targeted fixes over whole-chapter rewrites.
- Check banned modern terms, explicit regression counts, continuity drift, injury drift, and soft equal-exchange chapters.
- If the chapter passes, say so plainly and note residual risk only.
- If it fails, identify the smallest patch set that would make it re-auditable.
