from pathlib import Path
from typing import Iterable, Optional, Union


PathLike = Union[str, Path]
ROOT_MARKERS: Iterable[str] = ("Start_Here.md", "lore_bible", "outline", ".agent")


def find_repo_root(start: Optional[PathLike] = None) -> Path:
    current = Path(start or __file__).resolve()
    if current.is_file():
        current = current.parent

    for candidate in (current, *current.parents):
        if all((candidate / marker).exists() for marker in ROOT_MARKERS):
            return candidate

    raise FileNotFoundError(
        "Could not locate the story repository root. "
        "Expected Start_Here.md, lore_bible/, outline/, and .agent/."
    )


def resolve_project_path(*parts: str, start: Optional[PathLike] = None) -> Path:
    return find_repo_root(start=start).joinpath(*parts)
