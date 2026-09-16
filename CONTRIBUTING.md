# Contributing / Līdzdalība

Contributions are welcome when they improve accuracy, sourcing, translation quality, or accessibility.

Ieguldījumi ir gaidīti, ja tie uzlabo precizitāti, avotu kvalitāti, tulkojumu vai pieejamību.

## Required for a terminology change

1. Identify the exact term and proposed status.
2. Link a primary or authoritative source.
3. Explain whether the source is normative, institutional, professional, academic, historical/community, or secondary.
4. Update both English and Latvian definitions.
5. Add or update the relevant claim in `data/claims.yaml`, including the
   source locator and support type.
6. Update `last_reviewed`.
7. Run all checks.

```bash
make check
```

## Source preference

Prefer sources in this order:

1. legislation and official standards;
2. institutional frameworks and guidance;
3. professional policies and service frameworks;
4. primary hacker-community sources for historical usage;
5. academic research;
6. secondary explainers only to document observed usage.

Conflicting authoritative definitions should be documented, not silently resolved in favour of one community.

## Bilingual rule

Visible explanations must be updated in both languages in the same pull request. The translations should preserve meaning and caveats, but they do not have to be word-for-word copies.

## Editorial metaphors

Author-created expressions belong in `data/editorial_metaphors.yaml`, not `data/terms.yaml`. They must be marked `standardised: false` and include a usage rule that prevents them from being represented as professional roles.

## Legal and personal claims

- Do not present this project as legal advice.
- Tie legal claims to a jurisdiction and source.
- Do not use an editorial metaphor to target a named or reasonably identifiable person or organisation based on style, clothing, follower count, self-description, workplace, imagery, or a recognisable incident.
- Claims about identifiable parties require documented facts, a fact/opinion distinction, proportionate public-interest justification, a correction route, and appropriate editorial or legal review.
- Critique documented claims and conduct with proportionate evidence.
- Do not submit secrets, personal data, exploit code targeting a live third party, or incident-sensitive artefacts.

## Commit and pull-request style

Use a short imperative subject, for example:

- `clarify purple teaming status`
- `add Latvian VDP source`
- `fix source cross-reference`

Use the included pull-request template and state which validation commands passed.
