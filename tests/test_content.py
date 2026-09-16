from pathlib import Path

from scripts.configure_repository import configure, detect_current_owner
from scripts.validate import run_all


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
