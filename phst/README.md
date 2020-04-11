# Paskeharens sikkerhetstjeneste 

# 1. Skjærtorsdag 

Det er noe mistenkelig med bildet. Vi vet at flaggformatet skal være på formen PHST{xxx..}. Med exiftool (https://en.wikipedia.org/wiki/ExifTool) kan vi se på metadata til png-bildet. Der finner vi noe som ligner på flagg-formatet, 

```
Image Description               : CUFG{Qrer_snatre_zrt_nyqev!!}
```

Men det ser ut som det er shiftet med en eller annen cipher. Prøver med ASCII-shift, med utgangspunkt i CUFG som bør bli PHST. Alle bokstavene er off med verdien 13. Sekvensen <+ - + +> fra CUFG passer ikke i neste "ord" da den går utenfor ASCII eller skifter caps, som er ulogisk da dette ser ut til å være en tekst-streng. 
Tester med Qrer som har gjentagende bokstaver, blir mønsteret <- + - +>. 

Det viser seg at algoritmen er å shifte hver bokstav med samme fortegn, helt til det ikke går opp (ut av ASCII eller bytter mellom liten/stor bokstav) så snu fortegn. shift er alltid 13 bokstaver. 

Fasit på shift:
<+ - + + ... - + - + ... - - - - - + ... - - - ... - - - + ->

Flagget blir da:
PHST{Dere_fanger_meg_aldri}

# 2. Langfredag

Bildet viser en kartong fargekodede påskeegg. Under kan man skimte en fargekode for motstand, hvor hvit begynner med 9 og man teller seg oppover til 
```
hvit = 9
grå = 8
lilla = 7
blå = 6
grønn = 5
gul = 4
orange = 3
rød = 2
Brun = 1
```
Ved å telle fra topp til bunn på hvert egg, venstre mot høyre får man følgende tallsekvens:
```
112 052 052 115 107 051
104 052 114 051 110 033
```
Med litt intuisjon ser man at dette ser ut som desimalverdi i ascii. Med litt substitusjon får vi i Leetspeak: 

p44sk3h4r3n!


# 3. Paskeaften
