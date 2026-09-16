---
title: Terminoloģijas un pierādījumu metodoloģija
description: Divvalodu kiberdrošības atsauces avotu hierarhija, terminu statusi, izmaiņu noteikumi un juridiskās atrunas.
---

# Metodoloģija

## Avotu hierarhija

| Līmenis | Avotu veids | Kam to izmantojam |
|---|---|---|
| 1 | Normatīvi akti, oficiāli standarti un institucionālie ietvari | Juridiski vai formāli definēti procesi, lomas un pienākumi |
| 2 | CERT, CSIRT, NCSC, CISA, FIRST, MITRE un profesionālās institūcijas | Operacionāli termini, vadlīnijas un nozares prakse |
| 3 | Profesionālu programmu politikas un pakalpojumu ietvari | Reāls tvērums, safe harbor, atlīdzība un iesaistes noteikumi |
| 4 | Hakeru kultūras pirmavoti | Vēsturiska identitāte, ētika un žargona izcelsme |
| 5 | Mediji, mācību materiāli un komerciāli skaidrojumi | Lietojuma novērojumi; ne kanoniskas definīcijas, ja trūkst stiprāka avota |

## Termina statusi

- `established` — nostiprināts profesionāls vai tehnisks jēdziens;
- `established_with_context` — atzīts, bet tā robežas dažādos ietvaros atšķiras;
- `historical_or_community_jargon` — autentisks, bet ne formāls vai universāls;
- `common_but_contested` — joprojām izplatīts, bet tā formulējums vai robežas ir strīdīgas;
- `project_descriptive_category` — projekta skaidri radīta analītiska kategorija, ne nozares loma;
- `avoid_as_canonical` — sastopams, taču pārāk nekonsekvents kanoniskai vārdnīcai;
- `editorial_metaphor` — autora radīts tēls, glabājas atsevišķi no terminiem.

## Izmaiņu politika

Katrai definīcijas izmaiņai vajadzīgs:

1. konkrēts avots;
2. īss pamatojums;
3. abu valodu teksta pārbaude;
4. `last_reviewed` datuma atjauninājums;
5. skaidrojums, ja avoti savā starpā nesakrīt.

Negatīvs atradums — piemēram, “termins nav atrodams pārbaudītajos institucionālajos ietvaros” — nav absolūts pierādījums, ka terminu neviens nekad nelieto. Tas ir ierobežots secinājums par norādīto avotu kopu.

## Juridiskā piesardzība

Juridiskie secinājumi jāpiesaista konkrētai jurisdikcijai un politikas tekstam. Vispārīgais princips “labs nodoms nav automātiska atļauja” ir drošs, bet konkrēta VDP vai CVD programma var nepārprotami autorizēt noteikumiem atbilstošu testēšanu savā tvērumā.

Strukturētie avoti ir `data/sources.yaml`, terminu ieraksti — `data/terms.yaml`, bet apgalvojumu līmeņa atsauces un lokatori — `data/claims.yaml`. Rupjā `source.supports` saite palīdz navigācijai, bet nepierāda, ka avots pamato katru termina ieraksta lauku.
