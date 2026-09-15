# Cyber Roles, Authorization & Evidence

[Latviski](README.lv.md) · English

An open, bilingual reference for explaining cybersecurity roles, authorization boundaries, vulnerability-disclosure mechanisms, and the difference between evidence and public performance.

This repository is built around four questions:

1. **Role:** What function is the person or team actually performing?
2. **Authorization:** What are they permitted to do, to which systems, and under which rules?
3. **Evidence:** What information and artefacts support the claim?
4. **Accountability:** Who owns the decision, correction, remediation, or outcome?

It deliberately avoids presenting every online “hat colour” as an industry standard. Established terms, historical/community jargon, and editorial metaphors are labelled separately.

## What is included

- paired Latvian and English documentation;
- a source-backed terminology dataset in YAML;
- matrices for roles, authorization, evidence, and disclosure mechanisms;
- a checklist for evaluating public cyber claims;
- guidance on incident commentary risks;
- separate treatment of historical jargon and editorial metaphors;
- JSON Schemas and a validation script;
- automated checks and GitHub Pages deployment workflows.

## Quick start

Requirements: Git, Python 3.11 or newer, and internet access for the first dependency install.

```bash
git clone https://github.com/ancveirs-lv/cyber-roles-authorization-evidence.git
cd cyber-roles-authorization-evidence
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python scripts/configure_repository.py --github-user ancveirs-lv
python scripts/validate.py
mkdocs serve
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

Replace `ancveirs-lv` with your GitHub account name. Open `http://127.0.0.1:8000/` after the local server starts. See [INSTALL.md](INSTALL.md) for the full local, GitHub, and GitHub Pages path.

## Editorial boundary

`Red Team`, `Blue Team`, `White Team`, CVD, VDP, `security.txt`, Bug Bounty, and penetration testing are documented professional or technical concepts. `Purple Team` is widely used, often as a collaborative practice rather than a permanent organisational unit.

`Red Hat hacker` is inconsistent niche jargon. `Red Cap Team`, `Cyber Hype Team`, and `Post-Factum Team` are editorial metaphors created for commentary; they are not canonical cybersecurity roles and are excluded from the canonical term dataset.

## Reuse and citation

- Code and automation: [MIT License](LICENSE-CODE)
- Written content and data: [CC BY 4.0](LICENSE-CONTENT)
- Citation metadata: [CITATION.cff](CITATION.cff)

This project is educational and terminological. It is not legal advice, an authorization to test systems, or an operational incident-response procedure.
