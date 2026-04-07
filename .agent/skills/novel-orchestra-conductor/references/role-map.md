# Role Map

| Lane | Skill | Trigger | Required reads | Default output |
| --- | --- | --- | --- | --- |
| `lore` | `lore-forgemaster` | Missing canon, thin lore, entity design, contradiction repair | `Start_Here.md`, `outline/Series_Roadmap.md`, target lore files, nearby rule files | `Lore Delta` |
| `plausibility` | `plausibility-warden` | Timeline stress, motivation gaps, power ceiling, payment logic, recovery time | roadmap, target outline, target timeline, relevant lore | `Plausibility Report` |
| `draft` | `scene-smith` | Suspended by default while setting-first mode is active; use only after prose is reopened | roadmap, target outline, target timeline, core character files | draft body plus continuity notes |
| `hook` | `hook-doctor` | Suspended by default while setting-first mode is active; use only after a real draft exists | target outline, next beat from outline | opening and ending revisions |
| `audit` | `chapter-inspector` | Suspended by default while setting-first mode is active; use for final prose validation after drafting resumes | checklist, target outline, target timeline, relevant lore | pass / fail audit report |
| `foreshadow` | `foreshadow-bookkeeper` | Missing payoff map, weak twist fairness, unclear clue trail, unrecovered setup | endings, `lore_bible/Secrets_Activation.md`, `lore_bible/Mandatory_Events.md`, roadmap, relevant outlines | foreshadow/payoff report |
| `structure` | `structure-architect` | Ending lock, volume design, act-turn repair, midpoint design, backsolve planning | endings, roadmap, target outlines, mandatory events | structure report or beat map |
| `arc` | `arc-psychologist` | Character arc drift, weak emotional progression, trust-shift design, wound/need mapping | protagonist file, key character files, relevant outline, mandatory events if arc-critical | arc pressure report |
| `reveal` | `reveal-choreographer` | Reveal ladder design, misdirection fairness, secret staging, truth release pacing | endings, `lore_bible/Secrets_Activation.md`, foreshadow ledger, roadmap, relevant outlines | reveal ladder report |
| `cadence` | `serial-tension-engineer` | Suspended by default while setting-first mode is active; use later for prose pacing | target outline, checklist, hook notes if present | cadence report |

## Routing rules

- Route to `lore-forgemaster` first if missing canon would force downstream guesswork.
- Route to `plausibility-warden` before any major drafting pass.
- While `setting-first mode` is active, do not route into `draft`, `hook`, `audit`, or `cadence` unless the user explicitly reopens prose work.
- Route to `hook-doctor` only after a coherent draft exists.
- Route to `foreshadow-bookkeeper` when a reveal, twist, or endgame clue path is unclear.
- Route to `structure-architect` before drafting when the volume promise, midpoint, or ending-backsolve is still unstable.
- Route to `arc-psychologist` when character behavior works locally but the longer emotional path feels thin or repetitive.
- Route to `reveal-choreographer` when the truth is interesting but the release order is weak.
- Route to `serial-tension-engineer` when the prose is acceptable but chapters do not pull the reader forward.
- End with `chapter-inspector` unless the user explicitly wants raw planning only.
