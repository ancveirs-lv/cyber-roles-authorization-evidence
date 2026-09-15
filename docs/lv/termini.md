# Terminoloģija

## Drošākais pamatprincips

Nosauc cilvēku pēc pārbaudāmas darbības un konteksta, nevis tikai pēc pašnosaukuma vai cepures krāsas.

| Termins | Ieteicamais lietojums | Būtiskā atruna |
|---|---|---|
| Hakeris | Plašs kultūras vai tehnisks apzīmējums | Nav precīzs amats vai juridisks statuss; avoti nav vienoti |
| Krekeris | Vēsturisks/kopienas apzīmējums aizsardzības pārvarētājam | Mūsdienās bieži precīzāks ir “uzbrucējs” vai “apdraudējuma aktors” |
| Drošības pētnieks | Persona, kas pēta sistēmu drošības īpašības vai ievainojamības | Nosaukums pats par sevi nedod tiesības testēt konkrētu sistēmu |
| Ētiskais hakeris | Plaši atpazīstams profesionāls apzīmējums | “Ētisks” nav juridiska atļauja vai vienota kvalifikācija |
| Penetrācijas testētājs | Veic plānotu pārbaudi noteiktā tvērumā un pēc iesaistes noteikumiem | Ne katrs pentests ir Red Team vingrinājums |
| Uzbrucējs | Persona vai grupa, kas veic uzbrukuma darbības | Nolūks, piesaiste un identitāte jāpamato ar pierādījumiem |
| Apdraudējuma aktors | Analītisks apzīmējums aktoram, kas rada kiberapdraudējumu | Nevajag automātiski pielīdzināt konkrētai valstij vai grupējumam |

## Kāpēc “hakeris” un “krekeris” nav vienkāršs pretstats

[RFC 1392](https://www.rfc-editor.org/rfc/rfc1392.html) un Jargon File tradīcija vārdu *hacker* saista ar zinātkāri un tehnisku meistarību, bet ļaunprātīgam vai neatļautam pārkāpējam iesaka *cracker*. Savukārt [NIST pašreizējā vārdnīca](https://csrc.nist.gov/glossary/term/hacker) vārdu *hacker* lieto arī neatļauta lietotāja nozīmē.

Secinājums nav izvēlēties vienu nometni par absolūti pareizu. Profesionālā tekstā jāizvēlas precīzāks apzīmējums: pētnieks, testētājs, uzbrucējs, incidentu reaģētājs, CTI analītiķis vai cita faktiskā loma.

## Loma nav atļauja

Persona var būt kompetents drošības pētnieks, taču bez konkrētas politikas, līguma vai cita pilnvarojuma tā vēl nav tiesīga aktīvi testēt svešu sistēmu. Savukārt VDP vai Bug Bounty noteikumi var atļaut tikai noteiktas metodes konkrētiem aktīviem un noteiktā laikā.

Precīza formula:

> Loma apraksta funkciju. Pilnvarojums nosaka atļauto rīcību. Nolūks raksturo motivāciju. Neviens no tiem viens pats neaizstāj pārējos.

Pilnā strukturētā terminu kopa atrodas `data/terms.yaml`.
