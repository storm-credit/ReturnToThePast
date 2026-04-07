# Conductor Handoff Packet Playbook

This playbook defines the short, reusable packet types the conductor should reach for first.

Use these when the user asks for common novelist-side tasks and speed matters more than inventing a custom packet from scratch.

---

## Fast-start checklist

Before dispatching any packet, lock these five things:

1. What is the real bottleneck: lore, bridge logic, prose, foreshadow, or audit?
2. Which files are truth sources for this pass?
3. Which files may change?
4. Which files must not change?
5. What exact output shape should come back?

If those five are unclear, do not delegate yet.

---

## Recommended packet families

| Packet | Use when | Primary lane | Default expert order | Template |
| --- | --- | --- | --- | --- |
| `chapter-draft` | A chapter needs fresh prose or a clean rewrite inside locked canon | `draft` | conductor -> chrono -> plausibility -> scene -> hook -> audit | `templates/HANDOFF_CHAPTER_DRAFT.md` |
| `lore-repair` | Canon files disagree or a setting block is too thin to draft safely | `lore` | conductor -> lore -> chrono -> plausibility | `templates/HANDOFF_LORE_REPAIR.md` |
| `bridge-reinforcement` | Adjacent chapters or volumes connect weakly in logic or emotion | `plausibility` | conductor -> structure -> arc -> plausibility -> foreshadow | `templates/HANDOFF_BRIDGE_REINFORCEMENT.md` |
| `foreshadow-repair` | A reveal feels under-seeded, unfair, or too late | `lore` | conductor -> foreshadow -> timeline -> world-rule -> plausibility | `templates/HANDOFF_FORESHADOW_REPAIR.md` |

---

## Builder usage

When Python is available, use the packet builder for a first draft and then tighten the packet manually.

Examples:

```text
python .agent/skills/novel-orchestra-conductor/scripts/build_work_packet.py --preset chapter-draft --volume 1 --chapter 3 --mission "Draft Vol. 1 Ch. 3 inside locked canon"
python .agent/skills/novel-orchestra-conductor/scripts/build_work_packet.py --preset lore-repair --entity Iris --mission "Repair Iris canon and debt continuity"
python .agent/skills/novel-orchestra-conductor/scripts/build_work_packet.py --preset bridge-reinforcement --volume 6 --mission "Reinforce the Vol. 6 -> Vol. 7 handoff"
```

If Python is unavailable, copy the closest template from `orchestra/templates/` and fill it manually.

---

## Packet design notes

### Chapter draft

- Keep the packet narrow to one chapter unless a bridge is the real blocker.
- Always include the previous chapter tail if continuity matters.
- Lock the chapter exit style before prose starts if the hook lane is likely.

### Lore repair

- Do not mix world expansion with contradiction repair unless the gap cannot be closed any other way.
- A lore repair packet should name the contradiction in one sentence.
- If the fix would touch more than one volume, flag that in `Blocking Decisions`.

### Bridge reinforcement

- Treat the handoff as both logical and emotional.
- Read both sides of the bridge: previous volume close and next volume open.
- Prefer pressure repair over twist injection.

### Foreshadow repair

- Lock both the clue seed and the future payoff in the packet.
- If the first clue and the payoff land in the same volume, assume the setup is still too shallow until proven otherwise.

---

## What good packets avoid

- vague verbs like "make it better"
- open-ended lore invention without a contradiction target
- sending prose work before canon blockers are resolved
- routing every task through every lane
- hiding the real decision from the specialist
