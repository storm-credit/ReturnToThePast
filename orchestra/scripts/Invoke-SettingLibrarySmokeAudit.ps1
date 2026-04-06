param(
    [string]$RulesPath = "",
    [string]$OutputDir = ""
)

$ErrorActionPreference = "Stop"

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path

if ([string]::IsNullOrWhiteSpace($RulesPath)) {
    $RulesPath = Join-Path $PSScriptRoot "setting-audit-rules.json"
}

if (-not (Test-Path -LiteralPath $RulesPath)) {
    throw "Rules file not found: $RulesPath"
}

$rules = Get-Content -LiteralPath $RulesPath -Raw -Encoding utf8 | ConvertFrom-Json

function Normalize-RelPath {
    param([string]$Path)

    $normalizedRoot = $repoRoot.TrimEnd("\")
    if ($Path.StartsWith($normalizedRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
        return $Path.Substring($normalizedRoot.Length).TrimStart("\").Replace("\", "/")
    }

    return $Path.Replace("\", "/")
}

function Priority-Label {
    param([int]$Priority)

    switch ($Priority) {
        0 { return "P0" }
        1 { return "P1" }
        2 { return "P2" }
        default { return "P3" }
    }
}

function Test-AnyLike {
    param(
        [string]$Value,
        [object[]]$Patterns
    )

    foreach ($pattern in $Patterns) {
        if ($Value -like [string]$pattern) {
            return $true
        }
    }

    return $false
}

function Get-ScopedFiles {
    param(
        [object[]]$Include,
        [object[]]$Exclude
    )

    $results = New-Object System.Collections.Generic.List[string]

    foreach ($item in $Include) {
        $full = Join-Path $repoRoot ([string]$item)
        if (-not (Test-Path -LiteralPath $full)) {
            continue
        }

        $node = Get-Item -LiteralPath $full
        if ($node.PSIsContainer) {
            Get-ChildItem -LiteralPath $full -Recurse -File | ForEach-Object {
                $rel = Normalize-RelPath $_.FullName
                if (-not (Test-AnyLike -Value $rel -Patterns $Exclude)) {
                    $results.Add($_.FullName)
                }
            }
        }
        else {
            $rel = Normalize-RelPath $node.FullName
            if (-not (Test-AnyLike -Value $rel -Patterns $Exclude)) {
                $results.Add($node.FullName)
            }
        }
    }

    return $results | Sort-Object -Unique
}

function Search-Pattern {
    param(
        [string[]]$Files,
        [string]$Pattern
    )

    $matches = New-Object System.Collections.Generic.List[object]

    foreach ($file in $Files) {
        Select-String -LiteralPath $file -Pattern $Pattern -Encoding utf8 | ForEach-Object {
            $line = $_.Line.Trim()
            if ($line.Length -gt 120) {
                $line = $line.Substring(0, 117) + "..."
            }

            $matches.Add([pscustomobject]@{
                Path       = Normalize-RelPath $_.Path
                LineNumber = $_.LineNumber
                Line       = $line
            })
        }
    }

    return $matches
}

function Resolve-OverallStatus {
    param([string[]]$Statuses)

    if ($Statuses -contains "FAIL") { return "FAIL" }
    if ($Statuses -contains "WARNING") { return "WARNING" }
    return "PASS"
}

function Expand-VolumePath {
    param(
        [string]$Pattern,
        [int]$Volume
    )

    return $Pattern.Replace("{volume}", [string]$Volume)
}

$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
if ([string]::IsNullOrWhiteSpace($OutputDir)) {
    $OutputDir = "orchestra/runs/setting-smoke-$timestamp"
}

$outPath = Join-Path $repoRoot $OutputDir
New-Item -ItemType Directory -Path $outPath -Force | Out-Null

$checkSummaries = New-Object System.Collections.Generic.List[object]
$findings = New-Object System.Collections.Generic.List[object]

function Add-CheckSummary {
    param(
        [string]$CheckId,
        [string]$Status,
        [int]$Priority,
        [string]$Summary
    )

    $script:checkSummaries.Add([pscustomobject]@{
        CheckId  = $CheckId
        Status   = $Status
        Priority = $Priority
        Summary  = $Summary
    })
}

function Add-Finding {
    param(
        [string]$CheckId,
        [string]$Status,
        [int]$Priority,
        [string]$Title,
        [string]$Summary
    )

    $script:findings.Add([pscustomobject]@{
        CheckId  = $CheckId
        Status   = $Status
        Priority = $Priority
        Title    = $Title
        Summary  = $Summary
    })
}

function Invoke-MarkerChecks {
    param([object[]]$MarkerChecks)

    foreach ($marker in $MarkerChecks) {
        $checkId = [string]$marker.id
        $fileRel = [string]$marker.file
        $priority = [int]$marker.priority
        $title = if ($marker.title) { [string]$marker.title } else { $checkId }
        $passSummary = if ($marker.passSummary) { [string]$marker.passSummary } else { "All required markers are present." }

        $fileFull = Join-Path $repoRoot $fileRel
        if (-not (Test-Path -LiteralPath $fileFull)) {
            $summary = "Missing marker source file: $fileRel"
            Add-CheckSummary -CheckId $checkId -Status "FAIL" -Priority $priority -Summary $summary
            Add-Finding -CheckId $checkId -Status "FAIL" -Priority $priority -Title $title -Summary $summary
            continue
        }

        $raw = Get-Content -LiteralPath $fileFull -Raw -Encoding utf8
        $missingMarkers = @()

        foreach ($pattern in $marker.requiredPatterns) {
            if ($raw -notmatch [string]$pattern) {
                $missingMarkers += [string]$pattern
            }
        }

        if ($missingMarkers.Count -gt 0) {
            $summary = "$([string]$marker.description). Missing markers: " + ($missingMarkers -join ", ")
            Add-CheckSummary -CheckId $checkId -Status "FAIL" -Priority $priority -Summary $summary
            Add-Finding -CheckId $checkId -Status "FAIL" -Priority $priority -Title $title -Summary $summary
        }
        else {
            Add-CheckSummary -CheckId $checkId -Status "PASS" -Priority 3 -Summary $passSummary
        }
    }
}

$missingRequired = @()
foreach ($rel in $rules.requiredFiles) {
    $full = Join-Path $repoRoot ([string]$rel)
    if (-not (Test-Path -LiteralPath $full)) {
        $missingRequired += [string]$rel
    }
}

if ($missingRequired.Count -gt 0) {
    $summary = "Missing required source-of-truth files: " + ($missingRequired -join ", ")
    Add-CheckSummary -CheckId "required-files-check" -Status "FAIL" -Priority 0 -Summary $summary
    Add-Finding -CheckId "required-files-check" -Status "FAIL" -Priority 0 -Title "Required source bundle incomplete" -Summary $summary
}
else {
    Add-CheckSummary -CheckId "required-files-check" -Status "PASS" -Priority 3 -Summary "All required source-of-truth files are present."
}

$missingPairs = @()
for ($volume = 1; $volume -le [int]$rules.volumeCount; $volume++) {
    $outlineRel = Expand-VolumePath -Pattern ([string]$rules.outlinePattern) -Volume $volume
    $timelineRel = Expand-VolumePath -Pattern ([string]$rules.timelinePattern) -Volume $volume

    if (-not (Test-Path -LiteralPath (Join-Path $repoRoot $outlineRel))) {
        $missingPairs += $outlineRel
    }
    if (-not (Test-Path -LiteralPath (Join-Path $repoRoot $timelineRel))) {
        $missingPairs += $timelineRel
    }
}

if ($missingPairs.Count -gt 0) {
    $summary = "Missing volume pair files: " + ($missingPairs -join ", ")
    Add-CheckSummary -CheckId "volume-pair-check" -Status "FAIL" -Priority 0 -Summary $summary
    Add-Finding -CheckId "volume-pair-check" -Status "FAIL" -Priority 0 -Title "Outline/Timeline pair missing" -Summary $summary
}
else {
    Add-CheckSummary -CheckId "volume-pair-check" -Status "PASS" -Priority 3 -Summary "All 15 volume outline/timeline pairs exist."
}

$chapterMismatches = @()
for ($volume = 1; $volume -le [int]$rules.volumeCount; $volume++) {
    $outlineRel = Expand-VolumePath -Pattern ([string]$rules.outlinePattern) -Volume $volume
    $outlineFull = Join-Path $repoRoot $outlineRel
    if (-not (Test-Path -LiteralPath $outlineFull)) {
        continue
    }

    $count = (Select-String -LiteralPath $outlineFull -Pattern ([string]$rules.chapterRowPattern) -Encoding utf8).Count
    if ($count -ne [int]$rules.chaptersPerVolume) {
        $chapterMismatches += "$outlineRel ($count/$($rules.chaptersPerVolume))"
    }
}

if ($chapterMismatches.Count -gt 0) {
    $summary = "Outline chapter count mismatches: " + ($chapterMismatches -join ", ")
    Add-CheckSummary -CheckId "chapter-count-check" -Status "FAIL" -Priority 0 -Summary $summary
    Add-Finding -CheckId "chapter-count-check" -Status "FAIL" -Priority 0 -Title "25-chapter production rule broken" -Summary $summary
}
else {
    Add-CheckSummary -CheckId "chapter-count-check" -Status "PASS" -Priority 3 -Summary "Every outline file contains 25 chapter rows."
}

$canonFiles = Get-ScopedFiles -Include $rules.canonConflictScope.include -Exclude $rules.canonConflictScope.exclude
$canonFindings = 0
$canonHighestPriority = 3

foreach ($rule in $rules.canonConflicts) {
    $matches = Search-Pattern -Files $canonFiles -Pattern ([string]$rule.pattern)
    if ($matches.Count -eq 0) {
        continue
    }

    $canonFindings++
    $priority = [int]$rule.priority
    if ($priority -lt $canonHighestPriority) {
        $canonHighestPriority = $priority
    }

    $sample = $matches | Select-Object -First 5 | ForEach-Object { "$($_.Path):$($_.LineNumber)" }
    $summary = "$($rule.description). Matches: " + ($sample -join ", ")
    Add-Finding -CheckId "canon-conflict-check" -Status "FAIL" -Priority $priority -Title ([string]$rule.id) -Summary $summary
}

if ($canonFindings -gt 0) {
    Add-CheckSummary -CheckId "canon-conflict-check" -Status "FAIL" -Priority $canonHighestPriority -Summary "$canonFindings active canon conflict pattern(s) matched."
}
else {
    Add-CheckSummary -CheckId "canon-conflict-check" -Status "PASS" -Priority 3 -Summary "No locked canon conflict phrases were found in active canon files."
}

$styleFiles = Get-ScopedFiles -Include $rules.styleScope.include -Exclude $rules.styleScope.exclude
$styleFindings = 0
$styleHighestPriority = 3

foreach ($rule in $rules.styleTerms) {
    $matches = Search-Pattern -Files $styleFiles -Pattern ([string]$rule.pattern)
    if ($matches.Count -eq 0) {
        continue
    }

    $styleFindings++
    $priority = [int]$rule.priority
    if ($priority -lt $styleHighestPriority) {
        $styleHighestPriority = $priority
    }

    $sample = $matches | Select-Object -First 5 | ForEach-Object { "$($_.Path):$($_.LineNumber)" }
    $summary = "$($rule.description). Matches: " + ($sample -join ", ")
    Add-Finding -CheckId "banned-style-check" -Status "WARNING" -Priority $priority -Title ([string]$rule.id) -Summary $summary
}

if ($styleFindings -gt 0) {
    Add-CheckSummary -CheckId "banned-style-check" -Status "WARNING" -Priority $styleHighestPriority -Summary "$styleFindings style rule warning(s) matched."
}
else {
    Add-CheckSummary -CheckId "banned-style-check" -Status "PASS" -Priority 3 -Summary "No gore-forward diction was found in canon and planning docs."
}

$ledgerRel = [string]$rules.foreshadow.ledgerFile
$ledgerFull = Join-Path $repoRoot $ledgerRel
$foreshadowPriority = 3
$foreshadowHasProblem = $false

if (-not (Test-Path -LiteralPath $ledgerFull)) {
    $foreshadowHasProblem = $true
    $foreshadowPriority = 1
    Add-Finding -CheckId "foreshadow-ledger-check" -Status "FAIL" -Priority 1 -Title "Foreshadow ledger missing" -Summary "Missing required ledger file: $ledgerRel"
}
else {
    $ledgerText = Get-Content -LiteralPath $ledgerFull -Encoding utf8
    $ledgerRaw = Get-Content -LiteralPath $ledgerFull -Raw -Encoding utf8

    $missingIds = @()
    foreach ($id in $rules.foreshadow.requiredIds) {
        if ($ledgerRaw -notmatch [Regex]::Escape([string]$id)) {
            $missingIds += [string]$id
        }
    }

    if ($missingIds.Count -gt 0) {
        $foreshadowHasProblem = $true
        $foreshadowPriority = 1
        Add-Finding -CheckId "foreshadow-ledger-check" -Status "FAIL" -Priority 1 -Title "Required foreshadow IDs missing" -Summary ("Missing IDs: " + ($missingIds -join ", "))
    }

    $invalidStatusRows = @()
    $allowedStatuses = @($rules.foreshadow.allowedStatuses | ForEach-Object { [string]$_ })
    foreach ($line in $ledgerText) {
        if ($line -notmatch '^\|\s*F-\d{3}\s*\|') {
            continue
        }

        $cells = $line.Split('|') | ForEach-Object { $_.Trim() } | Where-Object { $_ -ne "" }
        if ($cells.Count -lt 2) {
            continue
        }

        $status = $cells[$cells.Count - 1]
        if ($allowedStatuses -notcontains $status) {
            $invalidStatusRows += $cells[0]
        }
    }

    if ($invalidStatusRows.Count -gt 0) {
        $foreshadowHasProblem = $true
        if ($foreshadowPriority -gt 2) {
            $foreshadowPriority = 2
        }
        Add-Finding -CheckId "foreshadow-ledger-check" -Status "WARNING" -Priority 2 -Title "Foreshadow ledger status drift" -Summary ("Invalid or missing status values on: " + ($invalidStatusRows -join ", "))
    }
}

$missingCompanions = @()
foreach ($rel in $rules.foreshadow.companionFiles) {
    $full = Join-Path $repoRoot ([string]$rel)
    if (-not (Test-Path -LiteralPath $full)) {
        $missingCompanions += [string]$rel
    }
}

if ($missingCompanions.Count -gt 0) {
    $foreshadowHasProblem = $true
    if ($foreshadowPriority -gt 1) {
        $foreshadowPriority = 1
    }
    Add-Finding -CheckId "foreshadow-ledger-check" -Status "FAIL" -Priority 1 -Title "Foreshadow companion files missing" -Summary ("Missing companion files: " + ($missingCompanions -join ", "))
}

if ($foreshadowHasProblem) {
    $statuses = @($findings | Where-Object { $_.CheckId -eq "foreshadow-ledger-check" } | Select-Object -ExpandProperty Status)
    $status = Resolve-OverallStatus -Statuses $statuses
    Add-CheckSummary -CheckId "foreshadow-ledger-check" -Status $status -Priority $foreshadowPriority -Summary "Foreshadow ledger requires follow-up."
}
else {
    Add-CheckSummary -CheckId "foreshadow-ledger-check" -Status "PASS" -Priority 3 -Summary "Foreshadow ledger, IDs, statuses, and companion files are aligned."
}

if ($rules.PSObject.Properties.Name -contains "markerChecks") {
    Invoke-MarkerChecks -MarkerChecks $rules.markerChecks
}

$overallStatus = Resolve-OverallStatus -Statuses ($checkSummaries | Select-Object -ExpandProperty Status)
$generatedAt = Get-Date -Format "yyyy-MM-dd HH:mm:ss zzz"
$sortedChecks = $checkSummaries | Sort-Object Priority, CheckId
$sortedFindings = $findings | Sort-Object Priority, CheckId, Title

$summaryLines = @(
    "# Setting Library Smoke Audit",
    "",
    "- Generated At: $generatedAt",
    "- Overall Status: $overallStatus",
    "- Rules File: $(Normalize-RelPath $RulesPath)",
    "- Output Directory: $($OutputDir.Replace('\', '/'))",
    "",
    "## Check Summary",
    "",
    "| Check | Status | Highest Priority | Summary |",
    "| --- | --- | --- | --- |"
)

foreach ($check in $sortedChecks) {
    $summaryLines += "| $($check.CheckId) | $($check.Status) | $(Priority-Label -Priority ([int]$check.Priority)) | $($check.Summary) |"
}

$summaryLines += ""
$summaryLines += "## Priority Queue"
$summaryLines += ""

if ($sortedFindings.Count -eq 0) {
    $summaryLines += "- No actionable findings."
}
else {
    foreach ($priority in 0..3) {
        $bucket = @($sortedFindings | Where-Object { $_.Priority -eq $priority })
        if ($bucket.Count -eq 0) {
            continue
        }

        $summaryLines += "### $(Priority-Label -Priority $priority)"
        foreach ($finding in $bucket) {
            $summaryLines += "- [$($finding.CheckId)] $($finding.Title): $($finding.Summary)"
        }
        $summaryLines += ""
    }
}

$summaryLines += "## Recommended Next Actions"
$summaryLines += ""

$recommended = @($sortedFindings | Select-Object -First 5)
if ($recommended.Count -eq 0) {
    $summaryLines += "1. Keep the smoke audit green while expanding outlines and timelines."
    $summaryLines += "2. Re-run the harness before major lore edits and before each drafting phase."
}
else {
    $index = 1
    foreach ($finding in $recommended) {
        $summaryLines += "$index. $($finding.Title) -> $($finding.Summary)"
        $index++
    }
}

Set-Content -LiteralPath (Join-Path $outPath "00_summary.md") -Value ($summaryLines -join "`r`n") -Encoding utf8

$jsonPayload = [pscustomobject]@{
    generated_at    = $generatedAt
    overall_status  = $overallStatus
    rules_file      = Normalize-RelPath $RulesPath
    output_dir      = $OutputDir.Replace("\", "/")
    checks          = $sortedChecks
    findings        = $sortedFindings
}

$jsonPayload | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath (Join-Path $outPath "results.json") -Encoding utf8

Write-Host "Setting library smoke audit complete."
Write-Host "Status: $overallStatus"
Write-Host "Report: $(Join-Path $outPath '00_summary.md')"
