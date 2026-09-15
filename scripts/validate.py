#!/usr/bin/env python3
"""Validate bilingual documentation, schemas, references, and local links."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]

DATASETS = (
    (ROOT / "data/terms.yaml", ROOT / "schemas/terms.schema.json"),
    (ROOT / "data/sources.yaml", ROOT / "schemas/sources.schema.json"),
    (
        ROOT / "data/editorial_metaphors.yaml",
        ROOT / "schemas/editorial-metaphors.schema.json",
    ),
)

DOC_PAIRS = (
    ("lv/index.md", "en/index.md"),
    ("lv/termini.md", "en/terminology.md"),
    ("lv/komandas.md", "en/teams.md"),
    ("lv/ievainojamibu-programmas.md", "en/vulnerability-programs.md"),
    (
        "lv/lomu-pilnvarojuma-pieradijumu-matrica.md",
        "en/role-authorization-evidence.md",
    ),
    (
        "lv/publisku-apgalvojumu-kontrolsaraksts.md",
        "en/public-claims-checklist.md",
    ),
    ("lv/incidentu-komentari.md", "en/incident-commentary.md"),
    ("lv/isa-atsauce.md", "en/quick-reference.md"),
    ("lv/zargons.md", "en/jargon.md"),
    ("lv/metodologija.md", "en/methodology.md"),
)

REQUIRED_FILES = (
    "README.md",
    "README.lv.md",
    "INSTALL.md",
    "INSTALL.lv.md",
    "LICENSE-CODE",
    "LICENSE-CONTENT",
    "CITATION.cff",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "mkdocs.yml",
)

MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        value = yaml.safe_load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path.relative_to(ROOT)} must contain a mapping")
    return value


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def unique_ids(items: list[dict], label: str) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for item in items:
        item_id = item["id"]
        if item_id in seen:
            errors.append(f"duplicate {label} id: {item_id}")
        seen.add(item_id)
    return errors


def validate_schema(data_path: Path, schema_path: Path) -> list[str]:
    data = load_yaml(data_path)
    schema = load_json(schema_path)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors: list[str] = []
    for error in sorted(validator.iter_errors(data), key=lambda value: list(value.path)):
        location = ".".join(str(part) for part in error.path) or "<root>"
        errors.append(
            f"{data_path.relative_to(ROOT)}:{location}: {error.message}"
        )
    return errors


def validate_cross_references() -> list[str]:
    terms = load_yaml(ROOT / "data/terms.yaml")["terms"]
    sources = load_yaml(ROOT / "data/sources.yaml")["sources"]
    metaphors = load_yaml(ROOT / "data/editorial_metaphors.yaml")[
        "editorial_metaphors"
    ]

    errors = unique_ids(terms, "term")
    errors.extend(unique_ids(sources, "source"))
    errors.extend(unique_ids(metaphors, "editorial metaphor"))

    term_ids = {item["id"] for item in terms}
    source_ids = {item["id"] for item in sources}
    metaphor_ids = {item["id"] for item in metaphors}

    overlap = term_ids & metaphor_ids
    if overlap:
        errors.append(
            "editorial metaphors must not occur in canonical terms: "
            + ", ".join(sorted(overlap))
        )

    for term in terms:
        missing = set(term["source_ids"]) - source_ids
        if missing:
            errors.append(
                f"term {term['id']} has unknown source ids: {', '.join(sorted(missing))}"
            )
        unknown_terms = set(term["not_equivalent_to"]) - term_ids
        if unknown_terms:
            errors.append(
                f"term {term['id']} has unknown not_equivalent_to ids: "
                + ", ".join(sorted(unknown_terms))
            )

    for source in sources:
        missing = set(source["supports"]) - term_ids
        if missing:
            errors.append(
                f"source {source['id']} supports unknown term ids: "
                + ", ".join(sorted(missing))
            )

    return errors


def validate_required_files() -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")
    return errors


def validate_language_pairs() -> list[str]:
    errors: list[str] = []
    for lv_path, en_path in DOC_PAIRS:
        for relative in (lv_path, en_path):
            path = ROOT / "docs" / relative
            if not path.is_file():
                errors.append(f"missing language-pair document: docs/{relative}")
    return errors


def markdown_files() -> list[Path]:
    files = list(ROOT.glob("*.md"))
    files.extend((ROOT / "docs").rglob("*.md"))
    return sorted(files)


def validate_local_links() -> list[str]:
    errors: list[str] = []
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith(("#", "mailto:")):
                continue
            relative_path = unquote(parsed.path)
            if not relative_path:
                continue
            resolved = (path.parent / relative_path).resolve()
            if not resolved.exists():
                errors.append(
                    f"broken local link in {path.relative_to(ROOT)}: {target}"
                )
    return errors


def run_all() -> list[str]:
    errors: list[str] = []
    for data_path, schema_path in DATASETS:
        errors.extend(validate_schema(data_path, schema_path))
    errors.extend(validate_cross_references())
    errors.extend(validate_required_files())
    errors.extend(validate_language_pairs())
    errors.extend(validate_local_links())
    return errors


def main() -> int:
    errors = run_all()
    if errors:
        print(f"Validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    term_count = len(load_yaml(ROOT / "data/terms.yaml")["terms"])
    source_count = len(load_yaml(ROOT / "data/sources.yaml")["sources"])
    pair_count = len(DOC_PAIRS)
    print(
        f"Validation passed: {term_count} terms, {source_count} sources, "
        f"{pair_count} bilingual document pairs."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
