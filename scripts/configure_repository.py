#!/usr/bin/env python3
"""Update GitHub-owner references in a clone or fork."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGETS = (
    "README.md",
    "README.lv.md",
    "INSTALL.md",
    "INSTALL.lv.md",
    "mkdocs.yml",
    "CITATION.cff",
)
PLACEHOLDERS = ("YOUR-USERNAME", "TAVS-LIETOTAJVARDS")
VALID_OWNER = re.compile(r"^(?!-)[A-Za-z0-9-]{1,39}(?<!-)$")
REPOSITORY_OWNER = re.compile(
    r"github\.com/(?P<owner>[A-Za-z0-9-]{1,39})/cyber-roles-authorization-evidence"
)


def detect_current_owner(root: Path) -> str | None:
    """Read the currently configured owner from mkdocs.yml."""
    match = REPOSITORY_OWNER.search((root / "mkdocs.yml").read_text(encoding="utf-8"))
    return match.group("owner") if match else None


def configure(
    root: Path,
    github_user: str,
    dry_run: bool = False,
    current_owner: str | None = None,
) -> list[Path]:
    if not VALID_OWNER.fullmatch(github_user):
        raise ValueError(
            "GitHub owner must contain 1–39 letters, digits, or hyphens and "
            "must not start or end with a hyphen."
        )

    owner_to_replace = current_owner or detect_current_owner(root)
    replacements = set(PLACEHOLDERS)
    if owner_to_replace and owner_to_replace != github_user:
        replacements.add(owner_to_replace)

    changed: list[Path] = []
    for relative in TARGETS:
        path = root / relative
        original = path.read_text(encoding="utf-8")
        updated = original
        for value in replacements:
            updated = updated.replace(value, github_user)
        if updated != original:
            changed.append(path)
            if not dry_run:
                path.write_text(updated, encoding="utf-8")
    return changed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Configure GitHub URLs in the repository template."
    )
    parser.add_argument("--github-user", required=True, help="GitHub account or organisation")
    parser.add_argument(
        "--current-owner",
        help="Owner currently present in repository URLs; detected from mkdocs.yml by default",
    )
    parser.add_argument("--dry-run", action="store_true", help="List files without changing them")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    changed = configure(ROOT, args.github_user, args.dry_run, args.current_owner)
    action = "Would update" if args.dry_run else "Updated"
    if changed:
        print(f"{action} {len(changed)} file(s):")
        for path in changed:
            print(f"- {path.relative_to(ROOT)}")
    else:
        print("Repository already uses the requested owner; no files changed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
