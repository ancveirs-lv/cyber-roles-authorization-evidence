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
    (ROOT / "data/claims.yaml", ROOT / "schemas/claims.schema.json"),
    (
        ROOT / "data/editorial_metaphors.yaml",
        ROOT / "schemas/editorial-metaphors.schema.json",
    ),
)

DOC_PAIRS = (
    ("lv/index.md", "en/index.md"),
    ("lv/terminology.md", "en/terminology.md"),
    ("lv/teams.md", "en/teams.md"),
    ("lv/vulnerability-programs.md", "en/vulnerability-programs.md"),
    ("lv/role-authorization-evidence.md", "en/role-authorization-evidence.md"),
    ("lv/public-claims-checklist.md", "en/public-claims-checklist.md"),
    ("lv/incident-commentary.md", "en/incident-commentary.md"),
    ("lv/quick-reference.md", "en/quick-reference.md"),
    ("lv/jargon.md", "en/jargon.md"),
    ("lv/methodology.md", "en/methodology.md"),
    ("lv/evidence-register.md", "en/evidence-register.md"),
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

MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


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


def validate_claim_source_fit(claims: list[dict], sources: list[dict]) -> list[str]:
    """Require every citation to support at least one term asserted by its claim."""
    errors: list[str] = []
    source_to_terms = {item["id"]: set(item["supports"]) for item in sources}
    for claim in claims:
        claim_terms = set(claim["term_ids"])
        for citation in claim["citations"]:
            source_id = citation["source_id"]
            supported_terms = source_to_terms.get(source_id)
            if supported_terms is not None and claim_terms.isdisjoint(supported_terms):
                errors.append(
                    f"claim/source mismatch: {claim['id']} cites {source_id} "
                    "without a supported claim term"
                )
    return errors


def validate_term_claim_coverage(terms: list[dict], claims: list[dict]) -> list[str]:
    """Require every canonical term record to be covered by the claim register."""
    covered = {term_id for claim in claims for term_id in claim["term_ids"]}
    return [
        f"term has no claim-level evidence: {term['id']}"
        for term in terms
        if term["id"] not in covered
    ]


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
    claims = load_yaml(ROOT / "data/claims.yaml")["claims"]
    metaphors = load_yaml(ROOT / "data/editorial_metaphors.yaml")[
        "editorial_metaphors"
    ]

    errors = unique_ids(terms, "term")
    errors.extend(unique_ids(sources, "source"))
    errors.extend(unique_ids(claims, "claim"))
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
        unknown_terms = set(term["not_synonymous_with"]) - term_ids
        if unknown_terms:
            errors.append(
                f"term {term['id']} has unknown not_synonymous_with ids: "
                + ", ".join(sorted(unknown_terms))
            )

    for source in sources:
        missing = set(source["supports"]) - term_ids
        if missing:
            errors.append(
                f"source {source['id']} supports unknown term ids: "
                + ", ".join(sorted(missing))
            )

    term_to_sources = {item["id"]: set(item["source_ids"]) for item in terms}
    source_to_terms = {item["id"]: set(item["supports"]) for item in sources}
    for term_id, referenced_sources in term_to_sources.items():
        for source_id in referenced_sources:
            if term_id not in source_to_terms[source_id]:
                errors.append(
                    f"term/source relation is one-way: {term_id} -> {source_id}"
                )
    for source_id, supported_terms in source_to_terms.items():
        for term_id in supported_terms:
            if source_id not in term_to_sources[term_id]:
                errors.append(
                    f"source/term relation is one-way: {source_id} -> {term_id}"
                )

    for claim in claims:
        missing_terms = set(claim["term_ids"]) - term_ids
        if missing_terms:
            errors.append(
                f"claim {claim['id']} has unknown term ids: "
                + ", ".join(sorted(missing_terms))
            )
        cited_sources = {citation["source_id"] for citation in claim["citations"]}
        missing_sources = cited_sources - source_ids
        if missing_sources:
            errors.append(
                f"claim {claim['id']} has unknown source ids: "
                + ", ".join(sorted(missing_sources))
            )

    errors.extend(validate_claim_source_fit(claims, sources))
    errors.extend(validate_term_claim_coverage(terms, claims))

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
        pair: list[Path] = []
        for relative in (lv_path, en_path):
            path = ROOT / "docs" / relative
            if not path.is_file():
                errors.append(f"missing language-pair document: docs/{relative}")
            else:
                pair.append(path)
        if len(pair) == 2:
            signatures = []
            for path in pair:
                lines = path.read_text(encoding="utf-8").splitlines()
                signatures.append(
                    (
                        sum(line.startswith("## ") for line in lines),
                        sum(line.startswith("|---") for line in lines),
                        sum(line.startswith("!!! ") for line in lines),
                    )
                )
            if signatures[0] != signatures[1]:
                errors.append(
                    "language-pair structure differs: "
                    f"docs/{lv_path} {signatures[0]} != docs/{en_path} {signatures[1]}"
                )
    return errors


def validate_page_metadata() -> list[str]:
    errors: list[str] = []
    for path in sorted((ROOT / "docs" / "en").glob("*.md")) + sorted(
        (ROOT / "docs" / "lv").glob("*.md")
    ):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n") or "\n---\n" not in text[4:]:
            errors.append(f"missing YAML front matter: {path.relative_to(ROOT)}")
            continue
        _, front_matter, _ = text.split("---", 2)
        metadata = yaml.safe_load(front_matter)
        if not isinstance(metadata, dict):
            errors.append(f"invalid YAML front matter: {path.relative_to(ROOT)}")
            continue
        for key in ("title", "description"):
            value = metadata.get(key)
            if not isinstance(value, str) or not value.strip():
                errors.append(
                    f"missing page {key}: {path.relative_to(ROOT)}"
                )
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
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(
                    f"local link escapes repository in {path.relative_to(ROOT)}: {target}"
                )
                continue
            if not resolved.is_file():
                errors.append(
                    f"broken local link in {path.relative_to(ROOT)}: {target}"
                )
    return errors


def validate_repository_configuration() -> list[str]:
    errors: list[str] = []
    mkdocs = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    if "site_url: https://" not in mkdocs:
        errors.append("mkdocs.yml must define an absolute HTTPS site_url")
    if "docs_structure: folder" not in mkdocs:
        errors.append("mkdocs.yml must use folder-based bilingual i18n")

    security = (ROOT / "SECURITY.md").read_text(encoding="utf-8").lower()
    if "replace this paragraph" in security or "before public launch" in security:
        errors.append("SECURITY.md contains an unresolved launch placeholder")
    return errors


def run_all() -> list[str]:
    errors: list[str] = []
    for data_path, schema_path in DATASETS:
        errors.extend(validate_schema(data_path, schema_path))
    errors.extend(validate_cross_references())
    errors.extend(validate_required_files())
    errors.extend(validate_language_pairs())
    errors.extend(validate_page_metadata())
    errors.extend(validate_local_links())
    errors.extend(validate_repository_configuration())
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
    claim_count = len(load_yaml(ROOT / "data/claims.yaml")["claims"])
    pair_count = len(DOC_PAIRS)
    print(
        f"Validation passed: {term_count} terms, {source_count} sources, "
        f"{claim_count} evidence claims, {pair_count} bilingual document pairs."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
