---
name: progress-ledger
description: Keep the ReturnToThePast orchestra moving during active work and leave a durable progress log. Use when the user says `진행`, asks to continue without stopping, wants current/next task status, or asks which conductor, specialists, MCP, skills, hooks, and harnesses were used in a pass.
---

# Progress Ledger

Keep one pass moving until it reaches a real checkpoint, and leave enough trace that the next pass can resume without guessing.

## Required Reads

Read these before logging or resuming work:

1. `orchestra/SESSION_STATE.md`
2. `orchestra/WORKFLOW.md`
3. `orchestra/RTTP_ENGINE_EXECUTION_PROTOCOL.md`
4. `orchestra/MCP_SKILLS_AGENTS_HOOKS_HARNESS_MAP.md`
5. `orchestra/EXECUTION_PROGRESS_LEDGER.md`
6. `orchestra/SETTING_PROGRESS_TRACKER.md` or `orchestra/DRAFTING_PROGRESS_TRACKER.md`

## Use This Skill For

- User says `진행`, `계속`, or asks not to stop until they stop the run
- User asks what is active now, what is next, or what remains
- User asks which conductor, specialists, MCP, skills, hooks, or harnesses are in play
- A pass changes lane, target chapter/volume, or checkpoint state
- A pass finishes and needs a durable resume point

## Logging Workflow

1. Read the active state and tracker files.
2. Identify the current bottleneck in one line.
3. State `현재 작업 / 다음 작업 / 실행 방식` before substantial work.
4. Do not stop at analysis if the pass has an executable next step.
5. Update `orchestra/EXECUTION_PROGRESS_LEDGER.md` after any meaningful pass with:
   - date/time
   - mode and bottleneck
   - conductor
   - specialists actually used
   - MCP actually used, or `none`
   - skills actually used
   - hooks/harnesses selected
   - files touched
   - result
   - next queue
6. If the active objective or target batch changed, also update `orchestra/SESSION_STATE.md`.
7. If progress counts changed, also update the relevant tracker.

## Runtime Rules

- Treat `EXECUTION_PROGRESS_LEDGER.md` as the pass-by-pass log.
- Treat `SESSION_STATE.md` as the current resume snapshot.
- Treat `SETTING_PROGRESS_TRACKER.md` and `DRAFTING_PROGRESS_TRACKER.md` as aggregate meters, not detailed logs.
- Log only tools actually used in the pass. Do not list unused experts or hooks.
- If no specialist, MCP, or hook was used, write `none` explicitly.
- Keep entries short and factual so the next conductor can scan them fast.
- When the user says `진행`, prefer continuing the current queue over reopening solved planning.

## Stop Conditions

- Stop only at a real checkpoint, blocker, or user interruption.
- If blocked, log the blocker and the exact next restart step.
- If the user presses stop or redirects scope, record the handoff point before exiting.
