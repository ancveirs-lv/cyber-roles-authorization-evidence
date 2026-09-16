from pathlib import Path

from scripts.configure_repository import configure, detect_current_owner
from scripts.validate import (
    run_all,
    validate_claim_source_fit,
    validate_term_claim_coverage,
)


def test_repository_content_is_valid() -> None:
    assert run_all() == []


def test_repository_configuration_replaces_both_placeholders(tmp_path: Path) -> None:
    for filename in ("README.md", "README.lv.md", "INSTALL.md", "INSTALL.lv.md", "mkdocs.yml", "CITATION.cff"):
        (tmp_path / filename).write_text(
            "YOUR-USERNAME TAVS-LIETOTAJVARDS", encoding="utf-8"
        )

    changed = configure(tmp_path, "example-owner")

    assert len(changed) == 6
    for path in changed:
        assert path.read_text(encoding="utf-8") == "example-owner example-owner"


def test_repository_configuration_replaces_existing_owner(tmp_path: Path) -> None:
    for filename in ("README.md", "README.lv.md", "INSTALL.md", "INSTALL.lv.md", "CITATION.cff"):
        (tmp_path / filename).write_text(
            "https://github.com/ancveirs-lv/cyber-roles-authorization-evidence",
            encoding="utf-8",
        )
    (tmp_path / "mkdocs.yml").write_text(
        "repo_url: https://github.com/ancveirs-lv/cyber-roles-authorization-evidence\n",
        encoding="utf-8",
    )

    assert detect_current_owner(tmp_path) == "ancveirs-lv"
    changed = configure(tmp_path, "example-owner")

    assert len(changed) == 6
    for path in changed:
        assert "ancveirs-lv" not in path.read_text(encoding="utf-8")
        assert "example-owner" in path.read_text(encoding="utf-8")


def test_claim_source_fit_rejects_unrelated_source() -> None:
    claims = [
        {
            "id": "claim_one",
            "term_ids": ["red_team"],
            "citations": [{"source_id": "source_one"}],
        }
    ]
    sources = [{"id": "source_one", "supports": ["blue_team"]}]

    assert validate_claim_source_fit(claims, sources) == [
        "claim/source mismatch: claim_one cites source_one without a supported claim term"
    ]


def test_term_claim_coverage_rejects_uncovered_term() -> None:
    terms = [{"id": "red_team"}, {"id": "blue_team"}]
    claims = [{"term_ids": ["red_team"]}]

    assert validate_term_claim_coverage(terms, claims) == [
        "term has no claim-level evidence: blue_team"
    ]
