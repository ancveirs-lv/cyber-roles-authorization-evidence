# Changelog

All notable changes are recorded here. The project follows [Semantic Versioning](https://semver.org/) for published releases.

## [Unreleased]

- Narrowed terminology claims to what their registered sources support.
- Removed absolute VDP authorisation language and added issuer-authority, third-party, contract, and applicable-law limits.
- Reframed the incident-update list as an editorial rather than compliance checklist.
- Strengthened safeguards against applying editorial metaphors to identifiable parties.
- Added semantic claim-to-source cross-reference validation and regression coverage.
- Added claim-level coverage for all 29 canonical term records and a build gate that rejects uncovered terms.
- Made repository-owner configuration cover all tracked text configuration and documentation locations.
- Derived built-site verification URLs from `mkdocs.yml` instead of a hard-coded GitHub owner.
- Added fork-portability and invalid-owner regression tests.
- Added one substantive generated glossary per language with stable anchors for all 29 terms.
- Added `DefinedTermSet`/`DefinedTerm` structured data and controlled Open Graph metadata.
- Made HTML language alternates absolute, added `x-default`, and enforced both in built-site verification.
- Added manual CI dispatch and generated-content drift checks.

## [0.2.0] — 2026-09-16

- Added claim-level evidence records with exact source locators and support types.
- Separated Vulnerability Disclosure Policy from Vulnerability Disclosure Program.
- Corrected ENISA, NIST, community-jargon, and project-defined category mappings.
- Added real bilingual builds with correct language metadata, canonical URLs, hreflang, and sitemap verification.
- Added page-specific metadata and a public evidence register.
- Hardened GitHub Actions permissions, pinned actions to full commit SHAs, and locked Python dependencies with hashes.
- Added Dependabot, CODEOWNERS, source-health checks, and a private vulnerability-reporting route.
- Expanded validation for bilateral source relations, claims, bilingual structure, metadata, and repository configuration.

## [0.1.0] — 2026-09-15

- Added paired Latvian and English documentation.
- Added canonical terminology and source datasets.
- Separated editorial metaphors from canonical terms.
- Added schema validation, tests, CI, and GitHub Pages deployment.
