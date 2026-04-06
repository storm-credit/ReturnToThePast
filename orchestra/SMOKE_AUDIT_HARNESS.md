# Smoke Audit Harness

Use this harness for fast, repeatable setting-library checks before major lore surgery, before drafting, and before final chapter inspection.

## What it checks

- required source-of-truth files exist
- all 15 volumes have both `Outline` and `Timeline`
- every outline still has 25 chapter rows
- locked canon conflict phrases do not reappear
- gore-forward diction does not leak into canon/planning docs
- the foreshadow ledger still contains required IDs and valid statuses
- front-half clue, supporting-witness, and ending-convergence marker docs still contain their locked anchor lanes

## Files

- Script: `orchestra/scripts/Invoke-SettingLibrarySmokeAudit.ps1`
- Rules: `orchestra/scripts/setting-audit-rules.json`
- Output: `orchestra/runs/setting-smoke-<timestamp>/`

## Usage

```powershell
powershell -ExecutionPolicy Bypass -File .\orchestra\scripts\Invoke-SettingLibrarySmokeAudit.ps1
```

To write into a named folder:

```powershell
powershell -ExecutionPolicy Bypass -File .\orchestra\scripts\Invoke-SettingLibrarySmokeAudit.ps1 -OutputDir "orchestra/runs/current-smoke"
```

## Priority Model

- `P0`: production structure is broken and drafting should stop
- `P1`: active canon conflicts that can poison multiple volumes
- `P2`: tone, naming, or ledger drift that should be cleaned before prose expands
- `P2`: marker-map drift where key reveal or witness anchors have silently thinned out
- `P3`: informational pass state

## When to run it

- after outline or timeline edits
- after canon rule changes
- after adding or removing any conductor map such as foreshadow, witness, or ending-convergence docs
- before chapter drafting begins for a volume
- before a full lore audit merge
