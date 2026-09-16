#!/usr/bin/env python3
"""Verify SEO and localization invariants in the built MkDocs site."""

from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin

import yaml


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"


def configured_base_url() -> str:
    config = yaml.safe_load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
    value = config.get("site_url") if isinstance(config, dict) else None
    if not isinstance(value, str) or not value.startswith("https://"):
        raise ValueError("mkdocs.yml must define an absolute HTTPS site_url")
    return value.rstrip("/") + "/"


BASE_URL = configured_base_url()
PAGES = (
    "index",
    "terminology",
    "teams",
    "vulnerability-programs",
    "role-authorization-evidence",
    "public-claims-checklist",
    "incident-commentary",
    "quick-reference",
    "jargon",
    "evidence-register",
    "methodology",
)


class HeadParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.language: str | None = None
        self.canonical: str | None = None
        self.alternates: dict[str, str] = {}
        self.description: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "html":
            self.language = values.get("lang")
        elif tag == "link" and values.get("rel") == "canonical":
            self.canonical = values.get("href")
        elif tag == "link" and values.get("rel") == "alternate":
            if values.get("hreflang") and values.get("href"):
                self.alternates[values["hreflang"]] = values["href"]
        elif tag == "meta" and values.get("name") == "description":
            self.description = values.get("content")


def page_path(locale: str, page: str) -> Path:
    prefix = Path() if locale == "en" else Path("lv")
    return SITE / prefix / ("index.html" if page == "index" else f"{page}/index.html")


def page_url(locale: str, page: str) -> str:
    locale_part = "" if locale == "en" else "lv/"
    page_part = "" if page == "index" else f"{page}/"
    return BASE_URL + locale_part + page_part


def verify() -> list[str]:
    errors: list[str] = []
    descriptions: set[str] = set()
    expected_urls: set[str] = set()

    for locale in ("en", "lv"):
        for page in PAGES:
            path = page_path(locale, page)
            expected = page_url(locale, page)
            expected_urls.add(expected)
            if not path.is_file():
                errors.append(f"missing built page: {path.relative_to(ROOT)}")
                continue

            parser = HeadParser()
            parser.feed(path.read_text(encoding="utf-8"))
            if parser.language != locale:
                errors.append(
                    f"wrong html lang for {path.relative_to(ROOT)}: {parser.language!r}"
                )
            if parser.canonical != expected:
                errors.append(
                    f"wrong canonical for {path.relative_to(ROOT)}: {parser.canonical!r}"
                )
            for alternate_locale in ("en", "lv"):
                alternate_expected = page_url(alternate_locale, page)
                alternate_actual = parser.alternates.get(alternate_locale)
                if (
                    alternate_actual is None
                    or urljoin(expected, alternate_actual) != alternate_expected
                ):
                    errors.append(
                        f"missing/wrong {alternate_locale} alternate for "
                        f"{path.relative_to(ROOT)}"
                    )
            if not parser.description:
                errors.append(f"missing meta description: {path.relative_to(ROOT)}")
            elif parser.description in descriptions:
                errors.append(f"duplicate meta description: {path.relative_to(ROOT)}")
            else:
                descriptions.add(parser.description)

    sitemap = SITE / "sitemap.xml"
    if not sitemap.is_file():
        errors.append("missing site/sitemap.xml")
    else:
        root = ET.parse(sitemap).getroot()
        namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        actual_urls = {
            element.text for element in root.findall("sm:url/sm:loc", namespace) if element.text
        }
        missing_urls = expected_urls - actual_urls
        if missing_urls:
            errors.append("sitemap missing: " + ", ".join(sorted(missing_urls)))

    return errors


def main() -> int:
    errors = verify()
    if errors:
        print(f"Built-site verification failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Built-site verification passed: {len(PAGES) * 2} localized pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
