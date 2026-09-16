---
title: Cybersecurity terminology
description: Source-backed distinctions between hackers, attackers, security researchers, ethical hackers and penetration testers.
---

# Terminology

## The safest default

Name a person by a verifiable action and context, not merely by a self-description or hat colour.

| Term | Recommended use | Essential caveat |
|---|---|---|
| Hacker | A broad cultural or technical label | Not a precise job or legal status; authoritative sources differ |
| Cracker | Historical/community label for someone who defeats controls | “Attacker” or “threat actor” is often more precise today |
| Security researcher | A person researching system security properties or vulnerabilities | The title does not itself authorize testing a specific system |
| Ethical hacker | A widely recognised professional label | “Ethical” is not legal permission or a uniform qualification |
| Penetration tester | Performs a planned assessment within scope and rules of engagement | Not every penetration test is a Red Team exercise |
| Attacker | In the cited NIST entry, a person attempting to exploit vulnerabilities | Broader actor taxonomies may separately cover groups; automated tooling is an attack mechanism, not automatically the actor |
| Threat actor | An analytical label for an actor creating cyber risk | It should not be equated automatically with a named group or state |

## Why hacker and cracker are not a simple pair

[RFC 1392](https://www.rfc-editor.org/rfc/rfc1392.html) and the Jargon File tradition associate *hacker* with curiosity and technical mastery, recommending *cracker* for a malicious or unauthorised intruder. The current [NIST glossary](https://csrc.nist.gov/glossary/term/hacker), however, also uses *hacker* in the sense of an unauthorised user.

The practical answer is not to declare one community universally correct. Professional writing should choose the more precise label: researcher, tester, attacker, incident responder, CTI analyst, or another actual role.

## A role is not authorization

A person may be a capable security researcher without being authorised to test somebody else's system. Conversely, a VDP or Bug Bounty policy may authorise only particular methods, assets, and time periods.

The precise formula is:

> Role describes function. Authorization defines permitted action. Intent describes motivation. None of them substitutes for the others.

The complete structured terminology set is in [`data/terms.yaml`](https://github.com/ancveirs-lv/cyber-roles-authorization-evidence/blob/main/data/terms.yaml). Claim-level support and exact locators are in the [evidence register](evidence-register.md).
