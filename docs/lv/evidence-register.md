---
title: Kiberdrošības terminoloģijas pierādījumu reģistrs
description: Apgalvojumu līmeņa pierādījumi pilnvarojuma robežām, lomu nošķīrumiem un strīdīgai kiberdrošības terminoloģijai.
---

# Pierādījumu reģistrs

Reģistrs nošķir projekta apgalvojumu no precīzas avota vietas, kas to pamato, ierobežo vai ievieto kontekstā. Avots var terminu definēt, tikai pieminēt, dokumentēt vēsturisku lietojumu vai ierobežot pilnvarojuma apgalvojumu. Tie nav līdzvērtīgi pierādījumu veidi.

Mašīnlasāmais reģistrs ir [`data/claims.yaml`](https://github.com/ancveirs-lv/cyber-roles-authorization-evidence/blob/main/data/claims.yaml). Tā shēma ir [`schemas/claims.schema.json`](https://github.com/ancveirs-lv/cyber-roles-authorization-evidence/blob/main/schemas/claims.schema.json).

| Apgalvojums | Pierādījumu robeža |
|---|---|
| Terminam hakeris ir konfliktējošas nozīmes | Vēsturiskās/kopienas un pašreizējās institucionālās definīcijas ir reģistrētas atsevišķi. |
| Citētajā definīcijā uzbrucējs nav automatizēts process | Tiešais NIST ieraksts definē personu. |
| Ētisks nolūks nav pilnvarojums | Joprojām vajadzīga konkrētam mērķim dota atļauja, tvērums un noteikumi. |
| Red Team vajag autorizētus noteikumus | Tā ir novērtēšanas funkcija, ne atļauja nesaskaņotai ielaušanai. |
| VDP politika un programma atšķiras | Politika ir dokuments; programma ir plašāka organizācijas spēja. |
| `security.txt` nav atļauja | RFC 9116 5.5. sadaļa tieši nošķir atrašanu no atļaujas. |
| CVD nav universāla testēšanas atļauja | Autorizētu pētniecību nosaka konkrēta programma vai politika. |
| Programmas safe harbour ir ierobežots | Tas automātiski neaptver trešo pušu sistēmas vai darbību ārpus noteikumiem. |
| White hat nav tvērums | Krāsas apzīmējums nepierāda atļauju konkrētam mērķim. |
| Haktīvists ir aktora motivācijas apzīmējums | Pašreizējie apdraudējumu pārskati to nepadara par profesijas lomu. |
| Incidentu komentētājs ir projekta kategorija | NCSC vadlīnijas pamato komunikācijas robežas, ne standartizētu profesiju. |
| Responsible disclosure ir izplatīts, bet strīdīgs | Šeit priekšroka dota CVD, jo tas apraksta koordināciju bez morāla apzīmējuma. |

## Kā lasīt atsauci

Katra atsauce norāda:

- avotu un precīzu vietu;
- vai avots definē, pamato, ierobežo, piemin vai dokumentē lietojumu;
- jurisdikciju vai kontekstu;
- normatīvo statusu;
- iegūšanas un pārskatīšanas datumu.

Avota autoritāte ir ierobežota ar to, ko avots faktiski pasaka. Pirmavots pierāda, ka tā autors ir izteicis apgalvojumu; paša notikuma pierādīšanai joprojām var būt vajadzīgs neatkarīgs apstiprinājums.
