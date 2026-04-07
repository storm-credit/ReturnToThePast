# Work Packet Contract

Use one packet per mission. Specialists should receive a packet, not a vague prompt.

## Required packet fields

- `Mission`: one sentence describing the job.
- `Lane`: `lore`, `plausibility`, `draft`, `hook`, or `audit`.
- `Target`: entity, volume, chapter, or file cluster.
- `State Snapshot`: current bottleneck, adjacent dependency, and active risk.
- `Required Reads`: files that must be read before acting.
- `Optional Reads`: nearby canon that may be pulled in if contradiction risk is high.
- `Locked Facts`: facts the specialist may not override.
- `Editable Targets`: files the conductor may patch after review.
- `No-Touch Files`: files that must not change in this pass.
- `Requested Expert Order`: ideal lane sequence when the mission spans more than one specialist.
- `Deliverable`: exact output shape expected from the specialist.
- `Blocking Decisions`: decisions the conductor has not locked yet and may need escalation.
- `Stop Conditions`: blockers that require escalation back to the conductor.

## Shared output shape

Every specialist response should use these headings:

```markdown
## Decision
## Findings
## Required Changes
## Assumptions
## Handoff
```

Keep findings concrete and file-scoped when possible.

## Packet families

For repeatable novelist-side tasks, prefer the repo-local handoff playbook instead of drafting packets from scratch every time:

- `orchestra/HANDOFF_PACKET_PLAYBOOK.md`
- `orchestra/templates/HANDOFF_CHAPTER_DRAFT.md`
- `orchestra/templates/HANDOFF_LORE_REPAIR.md`
- `orchestra/templates/HANDOFF_BRIDGE_REINFORCEMENT.md`
- `orchestra/templates/HANDOFF_FORESHADOW_REPAIR.md`

## Lane-specific deliverables

### Lore lane

- Decide missing or contradictory canon.
- Output a `Lore Delta`:
  - canon decision
  - new facts
  - conflicts checked
  - files to patch
  - knock-on risks

### Plausibility lane

- Stress-test time, motivation, causality, and equal-exchange weight.
- Output a `Plausibility Report`:
  - verdict
  - failures
  - required fixes
  - suggested lore deltas
  - safe-to-draft yes or no

### Draft lane

- Write or rewrite prose within locked canon.
- Output:
  - draft body
  - assumptions used
  - continuity notes for the next lane

### Hook lane

- Improve only the opening, ending, and chapter-turn pressure.
- Output:
  - hook goal
  - revised opening
  - revised ending or cliffhanger
  - delta summary

### Audit lane

- Grade the draft against checklist, timeline, and canon.
- Output:
  - pass / conditional / fail
  - blocking issues
  - warnings
  - exact fixes
  - re-audit scope

## Stop conditions

Escalate to the conductor instead of guessing when any of these happen:

- roadmap and timeline disagree
- a required file is missing
- a new lore fact would alter more than one volume
- the previous chapter contradicts the target chapter in a way that cannot be resolved locally
- a requested rewrite would require a new outline beat
