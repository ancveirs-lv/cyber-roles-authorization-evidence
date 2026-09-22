---
title: Evaluating public cybersecurity claims
description: A checklist for distinguishing direct observation, party statements, corroborated findings, inference, hypothesis and opinion.
---

# Evaluating public claims

Use this checklist before sharing a video, interview, post, or “rapid incident analysis”.

## Five core questions

1. **Role:** In what capacity is the person speaking — investigator, researcher, organisational representative, journalist, or external commentator?
2. **Access:** Did they have system logs and artefacts, or only public information?
3. **Source:** What did they establish directly, what comes from a primary source, and what is retelling?
4. **Certainty:** Are fact, inference, and hypothesis separated clearly?
5. **Accountability:** Are errors corrected publicly, and is the original post updated?

## Claim labels

These six labels are a project-defined editorial model for classifying claims, not an industry standard or a NIST/FIRST taxonomy.

| Label | Meaning | Example wording |
|---|---|---|
| Directly observed | Recorded in a verifiable artefact or observed through a stated method | “The public service returned HTTP 503 at 14:32 UTC; the response was preserved.” |
| Party statement | What an organisation, authority, researcher, or attacker says; primary evidence of the statement, not necessarily of the event | “The organisation reports service unavailability; no independent telemetry is available.” |
| Corroborated finding | Supported by independent evidence or multiple sources whose access and methods are stated | “Status data and two independent measurements show the outage began before 14:30 UTC.” |
| Inference | A reasoned assessment whose supporting observations and alternatives are disclosed | “The public timeline suggests that...” |
| Hypothesis | A testable but unconfirmed explanation | “One possibility is..., but log evidence is unavailable.” |
| Opinion | A personal or normative judgement | “In my view, the communication was late.” |

A primary source is not automatically a confirmed fact. It may be authoritative evidence of what that party said while the underlying technical claim still requires corroboration.

## Warning signs

- categorical attribution without explaining the evidence;
- an “obvious” cause before an incident timeline is available;
- terminal screens or certificate lists used as substitutes for competence;
- an attacker's statement republished as fact;
- failure to disclose that the commentator had no access to internal data;
- an original error silently deleted instead of corrected;
- views or follower counts treated as equivalent to technical evidence.

A good commentator is not less valuable than a practitioner; it is simply a different role with a different evidence base.
