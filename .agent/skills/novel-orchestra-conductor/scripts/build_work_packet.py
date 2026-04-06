from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable, List


ROOT = Path(__file__).resolve().parents[4]


def existing(paths: Iterable[Path]) -> List[Path]:
    return [path for path in paths if path.exists()]


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
    lane = args.task
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

    target = "repository"
    mission = args.mission

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
            required_reads.extend(
                existing(
                    [
                        ROOT / "Guidelines" / "Writing_Prompt_Template.md",
                    ]
                )
            )
        if lane == "audit":
            required_reads.extend(
                existing(
                    [
                        ROOT / "Guidelines" / "Chapter_Audit_Checklist.md",
                    ]
                )
            )
            locked_facts.append("Audit findings should prefer targeted fixes over whole-chapter rewrites.")

    elif lane == "plausibility":
        require(volume, "--volume is required for plausibility")
        target = f"Vol_{volume}" if not chapter else f"Vol_{volume} Chapter_{chapter}"
        required_reads.extend(existing([outline_path(volume), timeline_path(volume)]))
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
        mission = f"{lane} pass for {target}"

    deliverables = {
        "lore": "Return a Lore Delta with canon decision, new facts, conflicts checked, files to patch, and risks.",
        "plausibility": "Return a Plausibility Report with verdict, failures, required fixes, suggested lore deltas, and safe-to-draft status.",
        "draft": "Return chapter prose plus assumptions and continuity notes.",
        "hook": "Return revised opening and ending sections plus a short delta summary.",
        "audit": "Return pass/fail findings, blocking issues, warnings, exact fixes, and re-audit scope.",
    }

    lines = [
        "# Work Packet",
        "",
        f"- Mission: {mission}",
        f"- Lane: {lane}",
        f"- Target: {target}",
        "",
        "## Required Reads",
    ]
    lines.extend(f"- {item}" for item in fmt(required_reads))
    lines.extend(
        [
            "",
            "## Optional Reads",
        ]
    )
    lines.extend(f"- {item}" for item in fmt(optional_reads))
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
            "## Deliverable",
            f"- {deliverables[lane]}",
            "",
            "## Stop Conditions",
        ]
    )
    lines.extend(f"- {item}" for item in stop_conditions)

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a work packet for the novel orchestra lanes.")
    parser.add_argument("--task", choices=["lore", "plausibility", "draft", "hook", "audit"], required=True)
    parser.add_argument("--volume", type=int)
    parser.add_argument("--chapter", type=int)
    parser.add_argument("--entity")
    parser.add_argument("--mission")
    args = parser.parse_args()
    print(build_packet(args))


if __name__ == "__main__":
    main()
