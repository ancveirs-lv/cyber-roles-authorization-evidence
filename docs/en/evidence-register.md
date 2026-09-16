---
title: Evidence register for cybersecurity terminology
description: Claim-level evidence for authorization boundaries, role distinctions, and contested cybersecurity terminology.
---

# Evidence register

This register separates a project statement from the exact source passage used to support, limit, or contextualise it. A source may define a term, merely mention it, document historical usage, or constrain an authorization claim. Those are not equivalent forms of evidence.

The machine-readable record is [`data/claims.yaml`](https://github.com/ancveirs-lv/cyber-roles-authorization-evidence/blob/main/data/claims.yaml). Its schema is [`schemas/claims.schema.json`](https://github.com/ancveirs-lv/cyber-roles-authorization-evidence/blob/main/schemas/claims.schema.json).

| Claim | Evidence boundary |
|---|---|
| Hacker has conflicting meanings | Historical/community and current institutional definitions are recorded separately. |
| Attacker is not an automated process in the cited definition | The direct NIST entry defines an individual. |
| Ethical intent is not authorization | Target-specific permission, scope, and rules still control. |
| Red Team requires authorized rules | Red Team is an assessment function, not a licence for unsanctioned intrusion. |
| VDP policy and programme are distinct | The policy is a document; the programme is the wider organisational capability. |
| `security.txt` is not permission | RFC 9116 section 5.5 expressly separates discovery from permission. |
| CVD is not universal test permission | A programme or policy must define any authorized research. |
| Programme safe harbour has limits | It cannot automatically authorize third-party systems or activity outside its terms. |
| White hat is not scope | A colour label does not prove permission for a particular target. |
| Hacktivist is an actor-motivation label | Current threat reporting does not make it a workforce role. |
| Incident commentator is a project category | NCSC guidance supports communication boundaries, not a standardised profession. |
| Responsible disclosure is common but contested | CVD is preferred here because it describes coordination without a moral label. |

## How to read a citation

Each citation records:

- the source and exact locator;
- whether it defines, supports, limits, mentions, or documents usage;
- its jurisdiction or context;
- its normative status;
- the retrieval and review date.

The source's authority is limited to what it actually says. A primary source proves that its author made a statement; independent corroboration may still be needed to prove the underlying event.
