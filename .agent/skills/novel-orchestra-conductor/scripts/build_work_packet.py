from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable, List


ROOT = Path(__file__).resolve().parents[4]

PRESETS = {
    "bridge-reinforcement": {
        "lane": "plausibility",
        "expert_order": [
            "novel-orchestra-conductor",
            "structure-architect",
            "arc-psychologist",
            "plausibility-warden",
            "foreshadow-bookkeeper",
        ],
        "required": [
            ROOT / "Guidelines" / "Prompt_Quick_Reference.md",
        ],
        "locked_facts": [
            "Strengthen the handoff with pressure, cost, logistics, or emotion before adding spectacle.",
            "Do not invent a brand-new arc to hide a weak bridge.",
        ],
    },
    "chapter-audit": {
        "lane": "audit",
        "expert_order": [
            "novel-orchestra-conductor",
            "chapter-inspector",
        ],
        "required": [
            ROOT / "Guidelines" / "Prompt_Quick_Reference.md",
            ROOT / "Guidelines" / "Chapter_Audit_Checklist.md",
        ],
        "locked_facts": [
            "Prefer targeted fixes over whole-chapter rewrites unless the structure is broken.",
        ],
    },
    "chapter-draft": {
        "lane": "draft",
        "expert_order": [
            "novel-orchestra-conductor",
            "chrono-weaver",
            "plausibility-warden",
            "scene-smith",
            "hook-doctor",
            "chapter-inspector",
        ],
        "required": [
            ROOT / "Guidelines" / "Prompt_Quick_Reference.md",
            ROOT / "Guidelines" / "Writing_Prompt_Template.md",
            ROOT / "Guidelines" / "Chapter_Audit_Checklist.md",
        ],
        "locked_facts": [
            "Keep the target chapter inside the current outline beat order.",
            "Preserve chapter-exit pressure without adding a grand epilogue.",
        ],
    },
    "lore-repair": {
        "lane": "lore",
        "expert_order": [
            "novel-orchestra-conductor",
            "lore-forgemaster",
            "chrono-weaver",
            "plausibility-warden",
        ],
        "required": [
            ROOT / "Guidelines" / "Prompt_Quick_Reference.md",
            ROOT / "Guidelines" / "Setting_Audit_Scope.md",
        ],
        "locked_facts": [
            "Favor contradiction repair over ornamental world expansion.",
            "New lore must reinforce existing roadmap pressure instead of weakening it.",
        ],
    },
}

DEFAULT_EXPERT_ORDER = {
    "audit": [
        "novel-orchestra-conductor",
        "chapter-inspector",
    ],
    "draft": [
        "novel-orchestra-conductor",
        "chrono-weaver",
        "plausibility-warden",
        "scene-smith",
        "chapter-inspector",
    ],
    "hook": [
        "novel-orchestra-conductor",
        "scene-smith",
        "hook-doctor",
        "chapter-inspector",
    ],
    "lore": [
        "novel-orchestra-conductor",
        "lore-forgemaster",
        "chrono-weaver",
        "plausibility-warden",
    ],
    "plausibility": [
        "novel-orchestra-conductor",
        "plausibility-warden",
    ],
}


def existing(paths: Iterable[Path]) -> List[Path]:
    return [path for path in paths if path.exists()]


def unique_paths(paths: Iterable[Path]) -> List[Path]:
    seen = set()
    ordered = []
    for path in paths:
        if path in seen:
            continue
        seen.add(path)
        ordered.append(path)
    return ordered


def chapter_path(volume: int, chapter: int) -> Path:
    return ROOT / "Drafts" / f"Vol_{volume}" / f"Vol_{volume}_Chapter_{chapter}.md"


def outline_path(volume: int) -> Path:
    return ROOT / "outline" / f"Vol_{volume}_Outline.md"


def timeline_path(volume: int) -> Path:
    return ROOT / "outline" / f"Vol_{volume}_Timeline.md"


def lore_matches(entity: str) -> List[Path]:
    lowered = entity.lower()
    matches = []
    for path in ROOT.joinpath("lore_bible").rglob("*.md"):
        if lowered in path.stem.lower():
            matches.append(path)
    return sorted(matches)


def fmt(paths: Iterable[Path]) -> List[str]:
    return [str(path.relative_to(ROOT)).replace("\\", "/") for path in paths]


def require(value: object, message: str) -> None:
    if not value:
        raise SystemExit(message)


def build_packet(args: argparse.Namespace) -> str:
    preset = PRESETS.get(args.preset) if args.preset else None
    lane = args.task or (preset["lane"] if preset else None)
    require(lane, "--task is required unless --preset provides a lane")

    volume = args.volume
    chapter = args.chapter
    entity = args.entity

    shared_required = existing(
        [
            ROOT / "00_CANON.md",
            ROOT / "Start_Here.md",
            ROOT / "orchestra" / "SOURCE_OF_TRUTH.md",
            ROOT / "orchestra" / "WORKFLOW.md",
            ROOT / "outline" / "Series_Roadmap.md",
        ]
    )
    shared_optional = existing(
        [
            ROOT / "Guidelines" / "Writing_Prompt_Template.md",
            ROOT / "Guidelines" / "Chapter_Audit_Checklist.md",
            ROOT / "lore_bible" / "Regression_Log.md",
            ROOT / "lore_bible" / "Time_Travel_Laws.md",
            ROOT / "lore_bible" / "characters" / "Protagonist.md",
        ]
    )

    required_reads: List[Path] = list(shared_required)
    optional_reads: List[Path] = list(shared_optional)
    editable_targets: List[str] = []
    no_touch_files = ["00_CANON.md", "Start_Here.md", "outline/Series_Roadmap.md"]
    expert_order = list(DEFAULT_EXPERT_ORDER[lane])
    locked_facts = [
        "Preserve roadmap beats unless the user explicitly asks for roadmap surgery.",
        "Preserve timeline order and dates unless the packet is for a timeline repair.",
        "Preserve equal-exchange cost; gains require a narrative payment.",
        "Do not expose explicit regression counts in chapter prose.",
        "Treat Drafts as downstream output, not canon source.",
    ]
    stop_conditions = [
        "A required file is missing.",
        "Roadmap and timeline disagree.",
        "The task would force a new multi-volume canon branch.",
    ]
    blocking_decisions = list(args.blocking_decision or ["None locked at packet creation."])

    target = "repository"
    mission = args.mission

    if preset:
        required_reads.extend(existing(preset.get("required", [])))
        optional_reads.extend(existing(preset.get("optional", [])))
        locked_facts.extend(preset.get("locked_facts", []))
        stop_conditions.extend(preset.get("stop_conditions", []))
        expert_order = list(preset.get("expert_order", expert_order))

    if lane in {"draft", "hook", "audit"}:
        require(volume, "--volume is required for draft/hook/audit")
        require(chapter, "--chapter is required for draft/hook/audit")
        target = f"Vol_{volume} Chapter_{chapter}"
        chapter_reads = [outline_path(volume), timeline_path(volume), chapter_path(volume, chapter)]
        if chapter > 1:
            chapter_reads.append(chapter_path(volume, chapter - 1))
        required_reads.extend(existing(chapter_reads))
        editable_targets.append(f"Drafts/Vol_{volume}/Vol_{volume}_Chapter_{chapter}.md")
        if lane == "hook":
            optional_reads.extend(existing([chapter_path(volume, chapter + 1)]))
        if lane == "draft":
            required_reads.extend(existing([ROOT / "Guidelines" / "Writing_Prompt_Template.md"]))
        if lane == "audit":
            required_reads.extend(existing([ROOT / "Guidelines" / "Chapter_Audit_Checklist.md"]))
            locked_facts.append("Audit findings should prefer targeted fixes over whole-chapter rewrites.")

    elif lane == "plausibility":
        require(volume, "--volume is required for plausibility")
        target = f"Vol_{volume}" if not chapter else f"Vol_{volume} Chapter_{chapter}"
        required_reads.extend(existing([outline_path(volume), timeline_path(volume)]))
        if args.preset == "bridge-reinforcement":
            required_reads.extend(existing([outline_path(volume + 1), timeline_path(volume + 1)]))
            editable_targets.extend(
                [
                    f"outline/Vol_{volume + 1}_Outline.md",
                    f"outline/Vol_{volume + 1}_Timeline.md",
                ]
            )
        if chapter:
            optional_reads.extend(existing([chapter_path(volume, chapter - 1), chapter_path(volume, chapter)]))
        editable_targets.extend(
            [
                f"outline/Vol_{volume}_Outline.md",
                f"outline/Vol_{volume}_Timeline.md",
            ]
        )

    elif lane == "lore":
        require(entity, "--entity is required for lore")
        target = entity
        matches = lore_matches(entity)
        required_reads.extend(matches[:5])
        editable_targets.extend(fmt(matches[:5]))
        if not editable_targets:
            editable_targets.append("lore_bible/<category>/<new-file>.md")
        locked_facts.append("New lore must support existing roadmap pressure instead of dissolving it.")
        stop_conditions.append("A lore change would retcon published draft chapters.")

    else:
        raise SystemExit(f"Unsupported lane: {lane}")

    if not mission:
        mission = f"{args.preset or lane} pass for {target}"

    deliverables = {
        "audit": "Return pass/fail findings, blocking issues, warnings, exact fixes, and re-audit scope.",
        "draft": "Return chapter prose plus assumptions and continuity notes.",
        "hook": "Return revised opening and ending sections plus a short delta summary.",
        "lore": "Return a Lore Delta with canon decision, new facts, conflicts checked, files to patch, and risks.",
        "plausibility": "Return a Plausibility Report with verdict, failures, required fixes, suggested lore deltas, and safe-to-draft status.",
    }

    state_snapshot = []
    if args.preset:
        state_snapshot.append(f"Preset: {args.preset}")
    if volume:
        state_snapshot.append(f"Volume: {volume}")
    if chapter:
        state_snapshot.append(f"Chapter: {chapter}")
    if entity:
        state_snapshot.append(f"Entity: {entity}")
    if args.preset == "bridge-reinforcement" and volume:
        state_snapshot.append(f"Bridge span: Vol_{volume} -> Vol_{volume + 1}")
    if not state_snapshot:
        state_snapshot.append("Repository-wide target")

    lines = [
        "# Work Packet",
        "",
        f"- Mission: {mission}",
        f"- Lane: {lane}",
        f"- Target: {target}",
        "",
        "## State Snapshot",
    ]
    lines.extend(f"- {item}" for item in state_snapshot)
    lines.extend(
        [
            "",
            "## Required Reads",
        ]
    )
    lines.extend(f"- {item}" for item in fmt(unique_paths(required_reads)))
    lines.extend(
        [
            "",
            "## Optional Reads",
        ]
    )
    lines.extend(f"- {item}" for item in fmt(unique_paths(optional_reads)))
    lines.extend(
        [
            "",
            "## Locked Facts",
        ]
    )
    lines.extend(f"- {item}" for item in locked_facts)
    lines.extend(
        [
            "",
            "## Editable Targets",
        ]
    )
    lines.extend(f"- {item}" for item in editable_targets)
    lines.extend(
        [
            "",
            "## No-Touch Files",
        ]
    )
    lines.extend(f"- {item}" for item in no_touch_files)
    lines.extend(
        [
            "",
            "## Requested Expert Order",
        ]
    )
    lines.extend(f"{idx}. {item}" for idx, item in enumerate(expert_order, start=1))
    lines.extend(
        [
            "",
            "## Deliverable",
            f"- {deliverables[lane]}",
            "",
            "## Blocking Decisions",
        ]
    )
    lines.extend(f"- {item}" for item in blocking_decisions)
    lines.extend(
        [
            "",
            "## Stop Conditions",
        ]
    )
    lines.extend(f"- {item}" for item in stop_conditions)

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a work packet for the novel orchestra lanes.")
    parser.add_argument("--task", choices=["lore", "plausibility", "draft", "hook", "audit"])
    parser.add_argument("--preset", choices=sorted(PRESETS))
    parser.add_argument("--volume", type=int)
    parser.add_argument("--chapter", type=int)
    parser.add_argument("--entity")
    parser.add_argument("--mission")
    parser.add_argument("--blocking-decision", action="append")
    args = parser.parse_args()
    print(build_packet(args))


if __name__ == "__main__":
    main()
