# Installation and publication guide

This guide covers three paths: using the downloaded ZIP, cloning from GitHub, and publishing your own GitHub Pages site.

## 1. Prerequisites

Install:

- Git 2.40 or newer;
- Python 3.11 or newer;
- a GitHub account;
- optionally, GitHub CLI (`gh`) for command-line repository creation.

Check your installation:

```bash
git --version
python3 --version
```

On Windows, `python` may be used instead of `python3`.

## 2. Start from the ZIP package

Extract the archive and enter the project directory:

```bash
unzip cyber-roles-authorization-evidence-v0.1.0.zip
cd cyber-roles-authorization-evidence
```

Create a local Git repository:

```bash
git init
git add .
git commit -m "Initial bilingual terminology reference"
git branch -M main
```

## 3. Install the local documentation environment

macOS and Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Configure repository URLs in the template:

```bash
python scripts/configure_repository.py --github-user ancveirs-lv
```

The command replaces the GitHub-owner placeholders in `mkdocs.yml`, `CITATION.cff`, and the setup documentation. Preview the affected files without changing them by adding `--dry-run`.

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Validate the datasets and documentation links:

```bash
python scripts/validate.py
pytest
```

Run the local site:

```bash
mkdocs serve
```

Then open `http://127.0.0.1:8000/`.

Build production files locally:

```bash
mkdocs build --strict
```

The generated site is written to `site/`, which is intentionally ignored by Git.

## 4. Create the GitHub repository

### Option A — GitHub web interface

1. Open GitHub and select **New repository**.
2. Use the name `cyber-roles-authorization-evidence`.
3. Do not add a README, licence, or `.gitignore`; the package already contains them.
4. Create the repository.
5. Copy the repository URL and run:

```bash
git remote add origin https://github.com/ancveirs-lv/cyber-roles-authorization-evidence.git
git push -u origin main
```

### Option B — GitHub CLI

Authenticate once:

```bash
gh auth login
```

Create and push a public repository:

```bash
gh repo create cyber-roles-authorization-evidence --public --source=. --remote=origin --push
```

Replace `--public` with `--private` if the repository should initially remain private.

## 5. Enable GitHub Pages

The workflow in `.github/workflows/pages.yml` builds and deploys the site.

1. Open the repository on GitHub.
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, choose **GitHub Actions** as the source.
4. Open **Actions** and confirm that **Deploy documentation to GitHub Pages** succeeds.
5. The site URL will normally be `https://ancveirs-lv.github.io/cyber-roles-authorization-evidence/`.

If the repository is private, GitHub Pages availability depends on the account plan and organisation policy.

## 6. Configure repository protection

Recommended settings:

1. Go to **Settings → Rules → Rulesets**.
2. Create a branch ruleset targeting `main`.
3. Require a pull request before merging.
4. Require the `validate-and-build` status check.
5. Block force pushes and branch deletion.

For a single-maintainer repository, requiring one approval is optional; requiring the automated check is still useful.

## 7. Update terminology safely

1. Create a branch: `git switch -c term/<short-name>`.
2. Update `data/terms.yaml` and, when needed, `data/sources.yaml`.
3. Update both language pages if the visible explanation changes.
4. Set `last_reviewed` to the review date.
5. Run `python scripts/validate.py`, `pytest`, and `mkdocs build --strict`.
6. Commit and open a pull request using the included template.

Do not add an editorial metaphor to `data/terms.yaml`. Put it in `data/editorial_metaphors.yaml` and state explicitly that it is not an industry-standard role.

## 8. Create a release

After the first reviewed publication:

```bash
git tag -a v0.1.0 -m "Initial bilingual release"
git push origin v0.1.0
gh release create v0.1.0 --generate-notes
```

Update `CITATION.cff`, `CHANGELOG.md`, and the version in the ZIP filename before later releases.

## 9. Common problems

- **`python3` not found:** try `python`; install Python from python.org if neither works.
- **PowerShell blocks activation:** use `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, after reviewing your organisation's policy.
- **YAML validation fails:** check indentation and ensure every `source_id` exists in `data/sources.yaml`.
- **GitHub Pages returns 404:** confirm the Pages source is GitHub Actions and the deployment workflow completed.
- **Strict MkDocs build fails:** fix the reported internal link or navigation path; do not disable strict mode to hide it.
