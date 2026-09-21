#!/usr/bin/env python3
"""Generate the substantive bilingual glossary from canonical term/source data."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DOMAIN_ORDER = (
    "actor_identity",
    "professional_role",
    "team_function",
    "organisational_function",
    "authorization",
    "vulnerability_process",
    "community_jargon",
    "communication_role",
)
DOMAIN_LABELS = {
    "en": {
        "actor_identity": "Actors and identity labels",
        "professional_role": "Professional roles",
        "team_function": "Team functions",
        "organisational_function": "Organisational functions",
        "authorization": "Authorization",
        "vulnerability_process": "Vulnerability processes",
        "community_jargon": "Community jargon",
        "communication_role": "Communication roles",
    },
    "lv": {
        "actor_identity": "Aktori un identitātes apzīmējumi",
        "professional_role": "Profesionālās lomas",
        "team_function": "Komandu funkcijas",
        "organisational_function": "Organizatoriskās funkcijas",
        "authorization": "Atļauja un pilnvarojums",
        "vulnerability_process": "Ievainojamību procesi",
        "community_jargon": "Kopienas žargons",
        "communication_role": "Komunikācijas lomas",
    },
}


def load_data() -> tuple[list[dict], dict[str, dict], str]:
    terms = yaml.safe_load((ROOT / "data/terms.yaml").read_text(encoding="utf-8"))["terms"]
    sources = yaml.safe_load((ROOT / "data/sources.yaml").read_text(encoding="utf-8"))["sources"]
    config = yaml.safe_load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
    return terms, {source["id"]: source for source in sources}, config["site_url"].rstrip("/") + "/"


def json_ld(terms: list[dict], locale: str, page_url: str) -> str:
    items = [
        {
            "@type": "DefinedTerm",
            "@id": f"{page_url}#term-{term['id']}",
            "name": term[f"label_{locale}"],
            "description": term[f"definition_{locale}"],
            "inDefinedTermSet": page_url,
        }
        for term in terms
    ]
    value = {
        "@context": "https://schema.org",
        "@type": "DefinedTermSet",
        "@id": page_url,
        "name": "Cybersecurity terminology reference" if locale == "en" else "Kiberdrošības terminoloģijas atsauce",
        "inLanguage": locale,
        "hasDefinedTerm": items,
    }
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def render(locale: str, terms: list[dict], sources: dict[str, dict], base_url: str) -> str:
    is_en = locale == "en"
    page_url = base_url + ("glossary/" if is_en else "lv/glossary/")
    title = "Complete cybersecurity glossary" if is_en else "Pilnā kiberdrošības vārdnīca"
    description = (
        "Definitions, authorization boundaries and sources for all canonical terms in the project."
        if is_en
        else "Definīcijas, atļaujas robežas un avoti visiem projekta kanoniskajiem terminiem."
    )
    intro = (
        "This page renders every canonical term from the machine-readable dataset. Status labels describe how the term is used; they do not rank people or grant permission."
        if is_en
        else "Šajā lapā attēloti visi mašīnlasāmās datu kopas kanoniskie termini. Statuss raksturo termina lietojumu; tas nevērtē cilvēkus un nedod atļauju testēt."
    )
    lines = [
        "---",
        f"title: {title}",
        f"description: {description}",
        "---",
        "",
        f"# {title}",
        "",
        intro,
        "",
    ]
    for domain in DOMAIN_ORDER:
        members = [term for term in terms if term["domain"] == domain]
        if not members:
            continue
        lines.extend([f"## {DOMAIN_LABELS[locale][domain]}", ""])
        for term in members:
            label = term[f"label_{locale}"]
            definition = term[f"definition_{locale}"]
            boundary = term[f"authorization_note_{locale}"]
            citations = ", ".join(
                f"[{sources[source_id]['title']}]({sources[source_id]['url']})"
                for source_id in term["source_ids"]
            )
            lines.extend(
                [
                    f'<a id="term-{term["id"]}"></a>',
                    f"### {label}",
                    "",
                    f'<span class="term-status">{term["status"]}</span>',
                    "",
                    definition,
                    "",
                    f"**{'Authorization boundary' if is_en else 'Atļaujas robeža'}:** {boundary}",
                    "",
                    f"**{'Sources' if is_en else 'Avoti'}:** {citations}",
                    "",
                ]
            )
    lines.extend(
        [
            '<script type="application/ld+json">',
            json_ld(terms, locale, page_url),
            "</script>",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    terms, sources, base_url = load_data()
    stale: list[str] = []
    for locale in ("en", "lv"):
        path = ROOT / "docs" / locale / "glossary.md"
        expected = render(locale, terms, sources, base_url)
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != expected:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.write_text(expected, encoding="utf-8")
    if stale:
        print("Generated glossary is stale: " + ", ".join(stale))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
