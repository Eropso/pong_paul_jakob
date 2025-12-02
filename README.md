# Pong – Planlegging

## Beskrivelse
Vi skal gjenskape spillet **Pong** med **Pygame** og ved bruk av **objektorientert programmering**.

---

## Funksjonalitet
- Ball som beveger automatisk  
- To plattformer/paddles  
- Ball spretter når den treffer:
  - Plattform/paddle  
  - Tak  
  - Gulv  
- Poeng til motspiller hvis ballen går ut på sin egen side  

---

## Bevegelse
- **Venstre spiller**
  - Opp: `W`
  - Ned: `S`
- **Høyre spiller**
  - Opp: `Pil opp`
  - Ned: `Pil ned`

---

## Poengsystem
- Vis poeng for begge spillerne  
- Oppdater poeng når ballen går ut  
- Når ballen går ut:
  - Reset ballen til midten  
- Spiller vinner etter **11 poeng**  
- Poeng resettes etter seier  

---

## Utviklingsmetode
Smidig utvikling gjør at vi kan teste spillet etter at hver ny funksjon er lagt til, og gir rask oversikt over når noe ikke fungerer og hva som må fikses.  
I tillegg kan vi gjøre justeringer underveis, og det passer bra ved samarbeid fordi arbeidet kan deles opp i små deler.  

Fossefallmetoden derimot gjør at man må gå flere steg tilbake hvis man oppdager feil.

---

## Fremtidig arbeid

### Paul
- Paddle  
- Opp & ned-bevegelse  
- Paddle beveger seg riktig  

### Jakob
- Ball  
- Ballen spretter riktig  
- Kollisjon med paddle og vegger  
- Reset av ball etter poeng  

### Felles – Spillklassen
Kan deles opp i mindre deler.  
Paul kan lage objektene, og Jakob kan fikse poengsystemet og reset-funksjonen.

---

## Klassediagram
*(Legges til senere)*
