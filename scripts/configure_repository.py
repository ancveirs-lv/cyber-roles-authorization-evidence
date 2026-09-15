#!/usr/bin/env python3
"""Replace GitHub-owner placeholders in the repository template."""

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


def configure(root: Path, github_user: str, dry_run: bool = False) -> list[Path]:
    if not VALID_OWNER.fullmatch(github_user):
        raise ValueError(
            "GitHub owner must contain 1–39 letters, digits, or hyphens and "
            "must not start or end with a hyphen."
        )

    changed: list[Path] = []
    for relative in TARGETS:
        path = root / relative
        original = path.read_text(encoding="utf-8")
        updated = original
        for placeholder in PLACEHOLDERS:
            updated = updated.replace(placeholder, github_user)
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
    parser.add_argument("--dry-run", action="store_true", help="List files without changing them")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    changed = configure(ROOT, args.github_user, args.dry_run)
    action = "Would update" if args.dry_run else "Updated"
    if changed:
        print(f"{action} {len(changed)} file(s):")
        for path in changed:
            print(f"- {path.relative_to(ROOT)}")
    else:
        print("No placeholders found; no files changed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
