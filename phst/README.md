# Paskeharens sikkerhetstjeneste 

# 1. Skjærtorsdag 

Det er noe mistenkelig med bildet. Vi vet at flaggformatet skal være på formen PHST{xxx..}. Med exiftool (https://en.wikipedia.org/wiki/ExifTool) kan vi se på metadata til png-bildet. Der finner vi noe som ligner på flagg-formatet, 
'''
Image Description               : CUFG{Qrer_snatre_zrt_nyqev!!}
'''
Men det ser ut som det er shiftet med en eller annen cipher. Prøver med ASCII-shift, med utgangspunkt i CUFG som bør bli PHST. Alle bokstavene er off med verdien 13. Sekvensen <+ - + +> fra CUFG passer ikke i neste "ord" da den går utenfor ASCII eller skifter caps, som er ulogisk da dette ser ut til å være en tekst-streng. 
Tester med Qrer som har gjentagende bokstaver, blir mønsteret <- + - +>. 

Det viser seg at algoritmen er å shifte hver bokstav med samme fortegn, helt til det ikke går opp (ut av ASCII eller bytter mellom liten/stor bokstav) så snu fortegn. shift er alltid 13 bokstaver. 

Fasit på shift:
<+ - + + ... - + - + ... - - - - - + ... - - - ... - - - + ->
Flagget blir da:
PHST{Dere_fanger_meg_aldri}

# 2. Langfredag
