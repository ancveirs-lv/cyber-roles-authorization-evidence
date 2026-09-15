# Kiberdrošības lomas, pilnvarojums un pierādījumi

Latviski · [English](README.md)

Atvērts divvalodu atsauču projekts par kiberdrošības lomām, atļautas testēšanas robežām, ievainojamību paziņošanas mehānismiem un atšķirību starp pierādījumiem un publisku ekspertīzes performanci.

Projekta pamatā ir četri jautājumi:

1. **Loma:** kādu funkciju persona vai komanda faktiski pilda?
2. **Pilnvarojums:** ko, kur un pēc kādiem noteikumiem tā drīkst darīt?
3. **Pierādījumi:** kāda informācija un artefakti pamato apgalvojumu?
4. **Atbildība:** kurš atbild par lēmumu, kļūdas labošanu, ievainojamības novēršanu vai rezultātu?

Projekts nepasniedz katru internetā sastopamo “cepures krāsu” kā nozares standartu. Nostiprināti termini, vēsturisks/kopienas žargons un autora metaforas ir marķēti atsevišķi.

## Kas atrodams repozitorijā

- paralēla dokumentācija latviešu un angļu valodā;
- avotos balstīta YAML terminoloģijas datu kopa;
- lomu, pilnvarojuma, pierādījumu un ievainojamību programmu matricas;
- publisku kiberdrošības apgalvojumu novērtēšanas kontrolsaraksts;
- incidentu komentēšanas risku skaidrojums;
- atsevišķa vēsturiskā žargona un redakcionālo metaforu uzskaite;
- JSON shēmas un validācijas skripts;
- automatizētas pārbaudes un GitHub Pages publicēšanas darbplūsmas.

## Ātrais sākums

Nepieciešams Git, Python 3.11 vai jaunāks un interneta savienojums pirmajai atkarību instalēšanai.

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

Windows PowerShell vidē virtuālo vidi aktivizē ar:

```powershell
.venv\Scripts\Activate.ps1
```

`ancveirs-lv` vietā ieraksti sava GitHub konta nosaukumu. Pēc lokālā servera palaišanas atver `http://127.0.0.1:8000/`. Pilns lokālās uzstādīšanas, GitHub publicēšanas un GitHub Pages ceļš ir aprakstīts [INSTALL.lv.md](INSTALL.lv.md).

## Redakcionālā robeža

`Red Team`, `Blue Team`, `White Team`, CVD, VDP, `security.txt`, Bug Bounty un penetrācijas tests ir dokumentēti profesionāli vai tehniski jēdzieni. `Purple Team` ir plaši lietots apzīmējums, bieži sadarbības prakse, ne obligāti pastāvīga organizācijas vienība.

`Red Hat hacker` ir nekonsekvents nišas žargons. `Red Cap Team`, `Cyber Hype Team` un `Post-Factum Team` ir komentāriem radītas autora metaforas; tās nav kanoniskas kiberdrošības lomas un nav iekļautas kanoniskajā terminu datu kopā.

## Atkārtota izmantošana un citēšana

- kods un automatizācija: [MIT licence](LICENSE-CODE);
- teksts un dati: [CC BY 4.0](LICENSE-CONTENT);
- citēšanas metadati: [CITATION.cff](CITATION.cff).

Šis ir izglītojošs terminoloģijas projekts. Tas nav juridisks atzinums, atļauja testēt sistēmas vai operacionāla incidentu reaģēšanas procedūra.
