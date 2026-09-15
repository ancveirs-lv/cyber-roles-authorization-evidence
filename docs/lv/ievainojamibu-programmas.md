# CVD, VDP, Bug Bounty un pentests

Šie jēdzieni ir saistīti, bet risina atšķirīgas problēmas.

| Mehānisms | Galvenais mērķis | Vai var atļaut testēšanu? | Atlīdzība | Tipiskais rezultāts |
|---|---|---|---|---|
| CVD | Koordinēt ievainojamības saņemšanu, analīzi, novēršanu un publiskošanu | Process pats par sevi nav universāla atļauja; konkrēta programma var noteikt autorizētu tvērumu | Nav obligāta | Koordinēts labojums un paziņošana |
| VDP | Publicēt organizācijas noteikumus un ziņošanas kanālu | Jā, ja politikā nepārprotami aprakstīta labticīga, tvērumā ietverta pētniecība | Parasti nav | Paredzams ziņošanas un apstrādes process |
| `security.txt` | Padarīt atrodamu drošības kontaktu un politikas saiti | Nē, faila esamība pati par sevi nav atļauja | Nē | Kontaktinformācijas atrašana |
| Bug Bounty | Stimulēt noteikumiem atbilstošu ievainojamību atrašanu | Jā, programmas noteiktajā tvērumā un ar atļautajām metodēm | Var būt nauda, atzinība vai cita balva | Derīgs ziņojums un iespējamā atlīdzība |
| Pentests | Pasūtīta sistēmu vai kontroļu pārbaude pēc līguma un iesaistes noteikumiem | Jā, līgumā noteiktajā tvērumā | Pakalpojuma samaksa, ne atraduma balva | Ziņojums par pārbaudēm, risku un labojumiem |

## Trīs robežas, kuras nedrīkst sajaukt

### Kontakts nav atļauja

[RFC 9116](https://www.rfc-editor.org/rfc/rfc9116.html) standartizē `security.txt` kā veidu drošības kontaktu un politikas atrašanai. Fails viens pats neapstiprina tiesības aktīvi testēt sistēmu.

### Labs nolūks nav viss tvērums

Konkrēta VDP vai Bug Bounty politika var atzīt noteikumiem atbilstošu pētniecību par autorizētu. Tas attiecas tikai uz politikā norādītajiem aktīviem, metodēm un nosacījumiem. Vienmēr jāņem vērā jurisdikcija un noteikumu teksts.

### Atlīdzība nav garantēta

Bug Bounty nenozīmē, ka par katru iesniegumu pienākas samaksa. Programma var prasīt, lai ievainojamība būtu derīga, ietekmīga, iepriekš neziņota, tvērumā un iegūta ar atļautām metodēm.

## Latvijas konteksts

[CERT.LV CVD platforma](https://cvd.cert.lv/faq/answers/100) nodrošina koordinētu ievainojamību ziņošanas ceļu un skaidro, ka CVD ziņošana nav pilnvērtīgs pentests. Atlīdzība ir atkarīga no konkrētas programmas noteikumiem.

## Terminoloģijas izvēle

Starptautiskajā profesionālajā vidē ieteicams lietot *coordinated vulnerability disclosure* (CVD). *Responsible disclosure* ir vēsturiski lietots, bet var radīt nevajadzīgu morālu vērtējumu par to, kura puse rīkojusies “atbildīgi”.
