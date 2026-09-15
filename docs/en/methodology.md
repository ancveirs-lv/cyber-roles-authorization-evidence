# Methodology

## Source hierarchy

| Level | Source type | How it is used |
|---|---|---|
| 1 | Legislation, official standards, and institutional frameworks | Legally or formally defined processes, roles, and duties |
| 2 | CERTs, CSIRTs, NCSCs, CISA, FIRST, MITRE, and professional bodies | Operational terminology, guidance, and industry practice |
| 3 | Professional programme policies and service frameworks | Real scope, safe harbour, rewards, and rules of engagement |
| 4 | Primary hacker-culture sources | Historical identity, ethics, and jargon origins |
| 5 | Media, training material, and commercial explainers | Evidence of usage, not canonical definitions where stronger sources are absent |

## Term statuses

- `established` — an established professional or technical concept;
- `established_with_context` — recognised, but with boundaries that vary between frameworks;
- `historical_or_community_jargon` — authentic, but neither formal nor universal;
- `avoid_as_canonical` — found in use, but too inconsistent for the canonical glossary;
- `editorial_metaphor` — author-created imagery stored separately from the terminology dataset.

## Change policy

Every definition change requires:

1. a specific source;
2. a short rationale;
3. review of both language texts;
4. an updated `last_reviewed` date;
5. an explanation when sources conflict.

A negative finding — for example, “the term does not appear in the reviewed institutional frameworks” — is not absolute proof that nobody has ever used the term. It is a bounded conclusion about the stated source set.

## Legal caution

Legal conclusions must be tied to a jurisdiction and policy text. The general principle “good intent is not automatic permission” is sound, but a specific VDP or CVD programme may explicitly authorise policy-compliant testing within its scope.

Structured sources are in `data/sources.yaml`; term records are in `data/terms.yaml`.
