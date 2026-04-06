from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[4]
SCAN_ROOTS = [
    ROOT / "Start_Here.md",
    ROOT / "Guidelines",
    ROOT / "orchestra",
    ROOT / ".agent" / "skills",
]
ALIASES = {
    "Series_Roadmap.md": "outline/Series_Roadmap.md",
}
IGNORED_REFS = {
    "lore_bible/monsters/Bestiary.md",
    "lore_bible/magic/Magic_System.md",
    "lore_bible/items/Four_Kings_Weapons.md",
    "lore_bible/SciFi_Elements_in_Fantasy.md",
}

MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
INLINE_PATH_RE = re.compile(r"`([^`]+\.(?:md|json|py|bat))`")


def iter_files() -> list[Path]:
    files: list[Path] = []
    for root in SCAN_ROOTS:
        if root.is_file():
            files.append(root)
            continue
        files.extend(sorted(root.rglob("*.md")))
    return files


def extract_refs(text: str) -> list[str]:
    refs: list[str] = []
    for value in MARKDOWN_LINK_RE.findall(text):
        if "://" in value or value.startswith("#"):
            continue
        refs.append(value.split("#", 1)[0])
    for value in INLINE_PATH_RE.findall(text):
        if "://" in value:
            continue
        refs.append(value.split("#", 1)[0])
    return refs


def should_skip(ref: str) -> bool:
    if ref in IGNORED_REFS:
        return True
    if "[" in ref or "]" in ref:
        return True
    if "*" in ref:
        return True
    if "Vol_N" in ref or "Vol_X" in ref:
        return True
    return False


def main() -> int:
    missing: list[tuple[str, str]] = []

    for file_path in iter_files():
        text = file_path.read_text(encoding="utf-8")
        for ref in extract_refs(text):
            if should_skip(ref):
                continue
            ref = ALIASES.get(ref, ref)
            local_candidate = (file_path.parent / ref).resolve()
            repo_candidate = (ROOT / ref).resolve()
            if not local_candidate.exists() and not repo_candidate.exists():
                missing.append((str(file_path.relative_to(ROOT)).replace("\\", "/"), ref))

    if not missing:
        print("PASS: active orchestration docs reference only existing files.")
        return 0

    print("FAIL: missing references detected.")
    for owner, ref in missing:
        print(f"- {owner} -> {ref}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
