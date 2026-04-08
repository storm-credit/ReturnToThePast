# Model Routing Policy

This document defines the default model and effort for each orchestra role.

| Role | Default model | Effort | Why |
| --- | --- | --- | --- |
| `novel-orchestra-conductor` | `gpt-5.4` | `high` | Merge many specialist outputs and keep final authority coherent |
| `character-architect` | `gpt-5.4` | `high` | Character wounds, relationship logic, and emotional cost interact deeply |
| `faction-strategist` | `gpt-5.4` | `high` | Political pressure and institutional intent need long-range reasoning |
| `location-cartographer` | `gpt-5.4` | `medium` | Travel, staging, and local plausibility are narrower but still important |
| `world-rule-keeper` | `gpt-5.4` | `high` | Rule changes ripple into the whole series |
| `timeline-historian` | `gpt-5.4` | `high` | Fixed points, branch risk, and event order are core to this project |
| `foreshadow-bookkeeper` | `gpt-5.4` | `high` | Fair clue design and payoff debt require strong cross-volume synthesis |
| `structure-architect` | `gpt-5.4` | `high` | Ending-backsolve, act design, and volume promises set major constraints |
| `arc-psychologist` | `gpt-5.4` | `high` | Arc pressure, trust shifts, and identity cost are long-range craft problems |
| `reveal-choreographer` | `gpt-5.4` | `high` | Reveal order and misdirection fairness determine twist quality |
| `serial-tension-engineer` | `gpt-5.4` | `medium` | Cadence work is iterative, narrow, and benefits from fast repetition |
| `relic-curator` | `gpt-5.4` | `medium` | Item logic is bounded but can become a hidden continuity trap |
| `monster-ecologist` | `gpt-5.4` | `medium` | Ecology and outbreak pressure are domain-specific but systemic |
| `bestiary-warden` | `gpt-5.4-mini` | `medium` | Individual threat sheets are bounded and reward focused iteration |
| `building-cartographer` | `gpt-5.4-mini` | `medium` | Building-scale movement logic is narrow and map-specific |
| `ritual-liturgist` | `gpt-5.4` | `medium` | Rites and sacred procedures need conceptual coherence more than broad synthesis |
| `street-apothecary` | `gpt-5.4-mini` | `medium` | Everyday consumables and undercity remedy logic are bounded but texture-critical |
| `systems-chancellor` | `gpt-5.4` | `medium` | Social systems need coherent incentives more than maximal prose depth |
| `lore-forgemaster` | `gpt-5.4` | `high` | Canon repair and minimal-retcon design are high-leverage tasks |
| `plausibility-warden` | `gpt-5.4` | `medium` | Integration stress testing benefits from depth without always needing max effort |
| `scene-smith` | `gpt-5.4` | `high` | Voice, control, and scene-to-scene precision matter in prose |
| `hook-doctor` | `gpt-5.4-mini` | `medium` | Hook work is bounded and often benefits from quick iteration |
| `chapter-inspector` | `gpt-5.4` | `medium` | Final review is analytic but usually narrower than structural design |
| `chrono-weaver` | `gpt-5.4-mini` | `medium` | Helper analysis, lookups, and warning reports do not need the largest model |

## Escalation rules

- Use `gpt-5.4-mini` for simple spot checks, isolated chapter-end hook passes, and helper lookups.
- Use `gpt-5.4-mini` for building passes, item/consumable sheets, named-creature sheets, and other bounded field guides.
- Use `gpt-5.4` for any new canon, major retcon, endgame reveal work, or full-volume synthesis.
- Do not downgrade the conductor during a full lore audit or storycraft merge pass.
- Default to `medium` effort for bounded audits and `high` effort for cross-volume planning.
