param(
    [string]$Mission = "Full lore audit",
    [int]$Volume = 0,
    [string]$Focus = "setting consistency and plausibility",
    [string]$OutputDir = "",
    [switch]$IncludeDetailLanes
)

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\\..")).Path

function ExistingRelPaths {
    param([string[]]$Paths)
    $results = @()
    foreach ($rel in $Paths) {
        if ([string]::IsNullOrWhiteSpace($rel)) { continue }
        $full = Join-Path $repoRoot $rel
        if (Test-Path -LiteralPath $full) {
            $results += $rel.Replace("\", "/")
        }
    }
    return $results
}

function CollectDomainFiles {
    param(
        [string]$RelativeRoot,
        [string]$Filter = "*"
    )
    $fullRoot = Join-Path $repoRoot $RelativeRoot
    if (-not (Test-Path -LiteralPath $fullRoot)) { return @() }
    return @(Get-ChildItem -LiteralPath $fullRoot -Recurse -File -Filter $Filter |
        ForEach-Object { $_.FullName.Replace($repoRoot + "\", "").Replace("\", "/") } |
        Sort-Object)
}

function WritePacket {
    param(
        [string]$FileName,
        [string]$Specialist,
        [string]$Model,
        [string]$Domain,
        [string[]]$RequiredReads,
        [string[]]$OptionalReads,
        [string[]]$EditableTargets,
        [string[]]$LockedFacts,
        [string[]]$StopConditions,
        [string]$Deliverable
    )

    $path = Join-Path $outPath $FileName
    $lines = @(
        "# Lore Audit Packet",
        "",
        "- Mission: $Mission",
        "- Specialist: $Specialist",
        "- Recommended Model: $Model",
        "- Domain: $Domain",
        "- Focus: $Focus",
        ""
    )

    $lines += "## Required Reads"
    foreach ($item in $RequiredReads | Select-Object -Unique) { $lines += "- $item" }
    $lines += ""
    $lines += "## Optional Reads"
    foreach ($item in $OptionalReads | Select-Object -Unique) { $lines += "- $item" }
    $lines += ""
    $lines += "## Locked Facts"
    foreach ($item in $LockedFacts | Select-Object -Unique) { $lines += "- $item" }
    $lines += ""
    $lines += "## Editable Targets"
    foreach ($item in $EditableTargets | Select-Object -Unique) { $lines += "- $item" }
    $lines += ""
    $lines += "## No-Touch Files"
    $lines += "- 00_CANON.md"
    $lines += "- Start_Here.md"
    $lines += "- outline/Series_Roadmap.md"
    $lines += ""
    $lines += "## Deliverable"
    $lines += "- $Deliverable"
    $lines += ""
    $lines += "## Stop Conditions"
    foreach ($item in $StopConditions | Select-Object -Unique) { $lines += "- $item" }

    Set-Content -LiteralPath $path -Value ($lines -join "`r`n") -Encoding utf8
}

$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
if ([string]::IsNullOrWhiteSpace($OutputDir)) {
    $OutputDir = "orchestra/runs/lore-audit-$timestamp"
}

$outPath = Join-Path $repoRoot $OutputDir
New-Item -ItemType Directory -Path $outPath -Force | Out-Null

$core = ExistingRelPaths @(
    "00_CANON.md",
    "Start_Here.md",
    "orchestra/SOURCE_OF_TRUTH.md",
    "orchestra/WORKFLOW.md",
    "orchestra/LORE_AUDIT_HARNESS.md",
    "outline/Series_Roadmap.md",
    "lore_bible/rules/Equivalent_Exchange.md",
    "lore_bible/Regression_Constraints.md",
    "lore_bible/Time_Travel_Laws.md"
)

$volumeFiles = @()
if ($Volume -gt 0) {
    $volumeFiles = ExistingRelPaths @(
        "outline/Vol_${Volume}_Outline.md",
        "outline/Vol_${Volume}_Timeline.md"
    )
}

$lockedFacts = @(
    "Treat Drafts as downstream output, not canon source.",
    "Do not weaken roadmap stakes with convenient lore.",
    "Equivalent exchange must stay costly and visible.",
    "Do not expose explicit regression counts in chapter prose.",
    "Honor orchestra/SOURCE_OF_TRUTH.md ordering."
)

$stopConditions = @(
    "A required file is missing.",
    "Roadmap and timeline disagree.",
    "A domain change would retcon multiple volumes.",
    "A specialist needs to invent canon outside its domain."
)

$characterFiles = CollectDomainFiles "lore_bible/characters"
$groupFiles = CollectDomainFiles "lore_bible/groups"
$locationFiles = CollectDomainFiles "lore_bible/locations"
$worldFiles = @(
    (CollectDomainFiles "lore_bible/rules"),
    (CollectDomainFiles "lore_bible/magic"),
    (CollectDomainFiles "lore_bible/settings"),
    (CollectDomainFiles "lore_bible/items"),
    (CollectDomainFiles "lore_bible/monsters")
) | ForEach-Object { $_ }
$timelineFiles = @(
    (CollectDomainFiles "lore_bible/history"),
    (ExistingRelPaths @("lore_bible/Regression_Log.md", "lore_bible/temporal_facts.json"))
) | ForEach-Object { $_ }

$master = @(
    "# Lore Audit Master Brief",
    "",
    "- Mission: $Mission",
    "- Focus: $Focus",
    "- Output Directory: $($OutputDir.Replace('\','/'))",
    "- Recommended Conductor Model: gpt-5.4 / high",
    ""
)
$master += "## Domain Order"
$master += "1. character-architect"
$master += "2. faction-strategist"
$master += "3. location-cartographer"
$master += "4. world-rule-keeper"
$master += "5. timeline-historian"
$master += "6. chrono-weaver"
$master += "7. lore-forgemaster (only if fixes are needed)"
$master += "8. plausibility-warden (merge-level stress test)"
if ($IncludeDetailLanes) {
    $master += "9. relic-curator"
    $master += "10. monster-ecologist"
    $master += "11. systems-chancellor"
}
$master += ""
$master += "## Core Reads"
foreach ($item in ($core + $volumeFiles | Select-Object -Unique)) { $master += "- $item" }
$master += ""
$master += "## Global Locked Facts"
foreach ($item in $lockedFacts) { $master += "- $item" }
$master += ""
$master += "## Merge Goal"
$master += "- Produce one canon-consistent repair list with domain conflicts resolved by the conductor."
Set-Content -LiteralPath (Join-Path $outPath "00_master_brief.md") -Value ($master -join "`r`n") -Encoding utf8

WritePacket -FileName "10_character_packet.md" `
    -Specialist "character-architect" `
    -Model "gpt-5.4 / high" `
    -Domain "character" `
    -RequiredReads ($core + $volumeFiles + (ExistingRelPaths @("lore_bible/characters/Protagonist.md", "lore_bible/characters/Relationship_Map.md"))) `
    -OptionalReads $characterFiles `
    -EditableTargets ($characterFiles + (ExistingRelPaths @("lore_bible/Regression_Log.md"))) `
    -LockedFacts $lockedFacts `
    -StopConditions $stopConditions `
    -Deliverable "Character continuity report covering wounds, memory loss, emotional cost, relationships, and required canon deltas."

WritePacket -FileName "20_faction_packet.md" `
    -Specialist "faction-strategist" `
    -Model "gpt-5.4 / high" `
    -Domain "faction" `
    -RequiredReads ($core + $volumeFiles + $groupFiles) `
    -OptionalReads (CollectDomainFiles "lore_bible/settings") `
    -EditableTargets ($groupFiles + (CollectDomainFiles "lore_bible/settings")) `
    -LockedFacts $lockedFacts `
    -StopConditions $stopConditions `
    -Deliverable "Faction logic report covering power balance, motives, alliance logic, vulnerabilities, and political knock-on effects."

WritePacket -FileName "30_location_packet.md" `
    -Specialist "location-cartographer" `
    -Model "gpt-5.4 / medium" `
    -Domain "location" `
    -RequiredReads ($core + $volumeFiles + $locationFiles) `
    -OptionalReads (ExistingRelPaths @("lore_bible/Calendar_Conversion.md")) `
    -EditableTargets $locationFiles `
    -LockedFacts $lockedFacts `
    -StopConditions $stopConditions `
    -Deliverable "Location coherence report covering travel pressure, map identity, district clarity, and atmospheric function."

WritePacket -FileName "40_world_packet.md" `
    -Specialist "world-rule-keeper" `
    -Model "gpt-5.4 / high" `
    -Domain "world" `
    -RequiredReads ($core + $volumeFiles + $worldFiles) `
    -OptionalReads (ExistingRelPaths @("lore_bible/Mandatory_Events.md", "lore_bible/Secrets_Activation.md")) `
    -EditableTargets $worldFiles `
    -LockedFacts $lockedFacts `
    -StopConditions $stopConditions `
    -Deliverable "World-rule report covering clarity, loopholes, debt, noir pressure, and required rule tightening."

if ($IncludeDetailLanes) {
    WritePacket -FileName "41_relic_packet.md" `
        -Specialist "relic-curator" `
        -Model "gpt-5.4 / medium" `
        -Domain "items-detail" `
        -RequiredReads ($core + $volumeFiles + (CollectDomainFiles "lore_bible/items")) `
        -OptionalReads (ExistingRelPaths @("lore_bible/rules/Equivalent_Exchange.md")) `
        -EditableTargets (CollectDomainFiles "lore_bible/items") `
        -LockedFacts $lockedFacts `
        -StopConditions $stopConditions `
        -Deliverable "Item and artifact continuity report covering possession, activation cost, side effects, and cursed burden."

    WritePacket -FileName "42_monster_packet.md" `
        -Specialist "monster-ecologist" `
        -Model "gpt-5.4 / medium" `
        -Domain "monsters-detail" `
        -RequiredReads ($core + $volumeFiles + (CollectDomainFiles "lore_bible/monsters") + (ExistingRelPaths @("lore_bible/rules/Infection_Levels.md"))) `
        -OptionalReads (CollectDomainFiles "lore_bible/locations") `
        -EditableTargets ((CollectDomainFiles "lore_bible/monsters") + (ExistingRelPaths @("lore_bible/rules/Infection_Levels.md"))) `
        -LockedFacts $lockedFacts `
        -StopConditions $stopConditions `
        -Deliverable "Monster ecology report covering threat role, outbreak logic, infection pressure, and habitat fit."

    WritePacket -FileName "43_systems_packet.md" `
        -Specialist "systems-chancellor" `
        -Model "gpt-5.4 / medium" `
        -Domain "systems-detail" `
        -RequiredReads ($core + $volumeFiles + (CollectDomainFiles "lore_bible/settings")) `
        -OptionalReads ($groupFiles + $locationFiles) `
        -EditableTargets (CollectDomainFiles "lore_bible/settings") `
        -LockedFacts $lockedFacts `
        -StopConditions $stopConditions `
        -Deliverable "Social-system report covering scarcity, leverage, institutions, guild logic, and noir survival pressure."
}

WritePacket -FileName "50_timeline_packet.md" `
    -Specialist "timeline-historian" `
    -Model "gpt-5.4 / high" `
    -Domain "timeline" `
    -RequiredReads ($core + $volumeFiles + $timelineFiles) `
    -OptionalReads (ExistingRelPaths @("lore_bible/Regression_Log.md", "lore_bible/Secrets_Activation.md")) `
    -EditableTargets ($timelineFiles + $volumeFiles) `
    -LockedFacts $lockedFacts `
    -StopConditions $stopConditions `
    -Deliverable "Timeline report covering event order, fixed points, consequence chains, spoiler leakage, and date repairs."

WritePacket -FileName "90_merge_packet.md" `
    -Specialist "novel-orchestra-conductor" `
    -Model "gpt-5.4 / high" `
    -Domain "merge" `
    -RequiredReads ($core + $volumeFiles) `
    -OptionalReads (ExistingRelPaths @("orchestra/templates/REVISION_LEDGER.md")) `
    -EditableTargets (ExistingRelPaths @("orchestra/SESSION_STATE.md")) `
    -LockedFacts $lockedFacts `
    -StopConditions $stopConditions `
    -Deliverable "Merged canon repair order with conflicts resolved, priorities assigned, and downstream patch order."

Write-Output "Lore audit packets created at $($OutputDir.Replace('\','/'))"
