# Uzstādīšanas un publicēšanas ceļvedis

Ceļvedis aptver trīs variantus: darbu ar lejupielādēto ZIP paku, klonēšanu no GitHub un savas GitHub Pages vietnes publicēšanu.

## 1. Priekšnosacījumi

Uzstādi:

- Git 2.40 vai jaunāku;
- Python 3.11 vai jaunāku;
- GitHub kontu;
- pēc izvēles GitHub CLI (`gh`) repozitorija izveidei terminālī.

Pārbaudi instalāciju:

```bash
git --version
python3 --version
```

Windows vidē `python3` vietā var būt jālieto `python`.

## 2. Sāc ar ZIP paku

Atarhivē failu un atver projekta direktoriju:

```bash
unzip cyber-roles-authorization-evidence-v0.1.0.zip
cd cyber-roles-authorization-evidence
```

Izveido lokālu Git repozitoriju:

```bash
git init
git add .
git commit -m "Initial bilingual terminology reference"
git branch -M main
```

## 3. Uzstādi lokālo dokumentācijas vidi

macOS un Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Konfigurē repozitorija adreses veidnē:

```bash
python scripts/configure_repository.py --github-user ancveirs-lv
```

Komanda aizstāj GitHub īpašnieka vietturus failos `mkdocs.yml`, `CITATION.cff` un uzstādīšanas dokumentācijā. Lai tikai apskatītu maināmo failu sarakstu, neko nepārrakstot, pievieno `--dry-run`.

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Pārbaudi datu kopas un dokumentācijas saites:

```bash
python scripts/validate.py
pytest
```

Palaid vietni lokāli:

```bash
mkdocs serve
```

Pēc tam atver `http://127.0.0.1:8000/`.

Izveido produkcijas būvi lokāli:

```bash
mkdocs build --strict
```

Gatavā vietne tiek izveidota direktorijā `site/`, kura apzināti nav iekļauta Git vēsturē.

## 4. Izveido GitHub repozitoriju

### A variants — GitHub tīmekļa saskarne

1. Atver GitHub un izvēlies **New repository**.
2. Nosaukums: `cyber-roles-authorization-evidence`.
3. Nepievieno README, licenci vai `.gitignore`; tie jau ir pakā.
4. Izveido repozitoriju.
5. Nokopē repozitorija adresi un izpildi:

```bash
git remote add origin https://github.com/ancveirs-lv/cyber-roles-authorization-evidence.git
git push -u origin main
```

### B variants — GitHub CLI

Vienreiz autorizējies:

```bash
gh auth login
```

Izveido un publicē publisku repozitoriju:

```bash
gh repo create cyber-roles-authorization-evidence --public --source=. --remote=origin --push
```

Ja sākumā repozitorijam jābūt privātam, `--public` vietā izmanto `--private`.

## 5. Ieslēdz GitHub Pages

`.github/workflows/pages.yml` darbplūsma uzbūvē un publicē vietni.

1. Atver repozitoriju GitHub.
2. Ej uz **Settings → Pages**.
3. Sadaļā **Build and deployment** kā avotu izvēlies **GitHub Actions**.
4. Atver **Actions** un pārliecinies, ka **Deploy documentation to GitHub Pages** izpildās sekmīgi.
5. Vietnes adrese parasti būs `https://ancveirs-lv.github.io/cyber-roles-authorization-evidence/`.

Privātam repozitorijam GitHub Pages pieejamība ir atkarīga no konta plāna un organizācijas politikas.

## 6. Aizsargā galveno zaru

Ieteicamie iestatījumi:

1. Atver **Settings → Rules → Rulesets**.
2. Izveido noteikumu kopu zarā `main`.
3. Pieprasi pull request pirms apvienošanas.
4. Pieprasi sekmīgu `validate-and-build` pārbaudi.
5. Aizliedz piespiedu pārrakstīšanu un zara dzēšanu.

Ja repozitoriju uztur viena persona, viena apstiprinājuma prasība nav obligāta; automatizētā pārbaude tik un tā ir vērtīga.

## 7. Droši atjaunini terminoloģiju

1. Izveido zaru: `git switch -c term/<iss-nosaukums>`.
2. Labo `data/terms.yaml` un, ja vajag, `data/sources.yaml`.
3. Ja mainās publiskais skaidrojums, izlabo abu valodu lapas.
4. Laukā `last_reviewed` ieraksti pārskatīšanas datumu.
5. Palaid `python scripts/validate.py`, `pytest` un `mkdocs build --strict`.
6. Izveido commit un pull request ar komplektā iekļauto veidni.

Redakcionālu metaforu nepievieno `data/terms.yaml`. Ievieto to `data/editorial_metaphors.yaml` un nepārprotami norādi, ka tā nav nozares standarta loma.

## 8. Izveido laidienu

Pēc pirmās pārskatītās publikācijas:

```bash
git tag -a v0.1.0 -m "Initial bilingual release"
git push origin v0.1.0
gh release create v0.1.0 --generate-notes
```

Pirms nākamajiem laidieniem atjaunini `CITATION.cff`, `CHANGELOG.md` un versiju ZIP faila nosaukumā.

## 9. Biežākās problēmas

- **`python3` nav atrasts:** izmēģini `python`; ja nedarbojas abi, instalē Python no python.org.
- **PowerShell bloķē aktivizēšanu:** pēc savas organizācijas politikas pārbaudes izmanto `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.
- **YAML validācija neizdodas:** pārbaudi atkāpes un to, vai katrs `source_id` ir atrodams `data/sources.yaml`.
- **GitHub Pages rāda 404:** pārbaudi, vai Pages avots ir GitHub Actions un darbplūsma ir pabeigta.
- **Stingrā MkDocs būve neizdodas:** izlabo norādīto iekšējo saiti vai navigācijas ceļu; neizslēdz stingro režīmu tikai kļūdas paslēpšanai.
