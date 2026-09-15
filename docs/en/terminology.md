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
| Attacker | A person or group performing attack activity | Intent, attribution, and identity still require evidence |
| Threat actor | An analytical label for an actor creating cyber risk | It should not be equated automatically with a named group or state |

## Why hacker and cracker are not a simple pair

[RFC 1392](https://www.rfc-editor.org/rfc/rfc1392.html) and the Jargon File tradition associate *hacker* with curiosity and technical mastery, recommending *cracker* for a malicious or unauthorised intruder. The current [NIST glossary](https://csrc.nist.gov/glossary/term/hacker), however, also uses *hacker* in the sense of an unauthorised user.

The practical answer is not to declare one community universally correct. Professional writing should choose the more precise label: researcher, tester, attacker, incident responder, CTI analyst, or another actual role.

## A role is not authorization

A person may be a capable security researcher without being authorised to test somebody else's system. Conversely, a VDP or Bug Bounty policy may authorise only particular methods, assets, and time periods.

The precise formula is:

> Role describes function. Authorization defines permitted action. Intent describes motivation. None of them substitutes for the others.

The complete structured terminology set is in `data/terms.yaml`.
