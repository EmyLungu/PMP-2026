1.
X = rezultat primul zar
Y = rezultat al doilea zar
P(X+Y>=10 | X = Par) = ?

---


1.1 Calculaţi probabilitatea ca suma să fie cel puţin 10, ştiind că primul zar indică un număr par.

P(X+Y>=10 | X = Par) = P(X+Y>=10 ∩ X = Par) / P(X = Par)

P(X = Par) = 3/6 = 1/2  (Presupunem echiprobabilitate)

X + Y >= 10 => (x, y) <=> {(4, 6), (6,4),
                           (5, 5),
                           (5, 6), (6, 5)
                           (6, 6)}
X+Y>=10 ∩ X = Par => (x, y) <=> {(4, 6), (6,4), (6, 5), (6, 6)}
P(X+Y>=10 ∩ X = Par) = 4/36 = 1/9


P(X+Y>=10 | X = Par) = P(X+Y>=10 ∩ X = Par) / P(X = Par)
                     = 1/9  /  1/2
                     = 1/9  *  2
                     = 2/9

1.2 Calculaţi probabilitatea ca suma să fie cel puţin 10, ştiind că cel puţin unul dintre zaruri indică un număr par.

P(X = Par ∪ Y = Par) = 1 - P(X = Impar ∩ Y = Impar)    (Presupunem ca sunt independente)
                     = 1 - 1/2 * 1/2
                     = 1 - 1/4
                     = 3/4

X+Y>=10 ∩ (X = Par ∪ Y = Par) => (x, y) <=> {(4, 6), (6,4), (5, 6), (6, 5), (6, 6)}
P(X+Y>=10 ∩ (X = Par ∪ Y = Par)) = 5/36


P(X+Y>=10 | (X = Par ∪ Y = Par)) = P(X+Y>=10 ∩ (X = Par ∪ Y = Par)) / P(X = Par ∪ Y = Par)
                     = 5/36  /  3/4
                     = 5/36  *  4/3
                     = 5/27

1.3 Calculaţi probabilitatea ca ambele zaruri să indice numere pare, ştiind că suma lor este 8.

X + Y = 8 => (x, y) <=> {(2, 6), (6, 2),
                         (3, 5), (5, 3),
                         (4, 4)}
P(X+Y=8) = 5/36

X + Y = 8 ∩ (X = Par ∩ Y = Par) => (x, y) <=> {(2, 6), (6, 2), (4, 4)}
P(X + Y = 8 ∩ (X = Par ∪ Y = Par)) = 3/36 = 1/12

Folosim T.H. Bayes:
P((X = Par ∪ Y = Par) | X+Y=8) = P(X+Y=8 ∩ (X = Par ∪ Y = Par)) / P(X+Y=8)
                               = 1/12  /  5/36
                               = 1/12  *  36/5
                               = 3/5

1.4. Sunt evenimentele A = {X + Y >= 10} şi B = {X este par} independente?

A, B - independente <=> P(A ∩ B) = P(A) * P(B)

De la 1.1 avem ca: P(A ∩ B) = 1/9
P(A) = 5/36
P(B) = 1/2

P(A ∩ B) = P(A) * P(B)
<=> 1/9 = 1/6  *  1/2
<=> 1/9 = 1/12      (FALS) => A, B nu sunt independente


---

2.

30% mesaje sunt spam
"oferta" in 80% din spam
"oferta" in 15% din non-spam

---

2.1. Care este probabilitatea ca un mesaj care conţine cuvântul „ofertă” să fie spam?

Probabilitatea Totala:
P(oferta) = P(oferta | spam) * P(spam) + P(oferta | ¬spam) * P(¬spam)
          = 80/010 * 30/100 + 15/100 * 70/100
          = (2400 + 1050) / 10000
          = (2400 + 1050) / 10000
          = 345 / 1000
          = 0.345

T.H. Bayes
P(spam | oferta) = P(oferta | spam) * P(spam) / P(oferta)
                 = 80/100 * 30/100   /   345 / 10000
                 = 80 * 30 / 3450
                 = 240 / 345
                 = 0.695652173913

2.2. Presupunem că termenul „gratuit” apare în 60% dintre mesajele spam şi în 10% dintre mesajele legitime. Consid-
erând independenţa condiţionată a apariţiei celor două cuvinte, calculaţi probabilitatea ca un mesaj care conţine

P(gratuit | spam) = 60%
P(gratuit | ¬spam) = 10%

P(spam | oferta ∩ gratuit) = P(oferta ∩ gratuit | spam) * P(spam) / P(oferta ∩ gratuit)
                           = 48/100 * 30/100   /   1545/10000
                           = 1440 / 1545
                           = 0.932038835

P(oferta ∩ gratuit | spam) = P(oferta | spam) * P(gratuit | spam)
                           = 80/100 * 60/100
                           = 48/100

P(oferta ∩ gratuit | ¬spam) = P(oferta | ¬spam) * P(gratuit | ¬spam)
                           = 15/100 * 10/100
                           = 15/1000

Prob totala
P(oferta ∩ gratuit) = P(oferta ∩ gratuit | spam) * P(spam) + P(oferta ∩ gratuit | ¬spam) * P(¬spam)
                    = 48/100 * 30/100 + 15/1000 * 70/100
                    = 1545/10000


ambele cuvinte să fie spam.
2.3. Explicaţi de ce ipoteza independenţei condiţionate poate fi nerealistă.

Ipoteza este nerealistă deoarece cuvintele din limbajul natural nu sunt independente.
Cuvinte precum "ofertă” și "gratuit” apar frecvent împreună în anunțuri

2.4. Propuneţi o regulă de clasificare bazată pe probabilitatea condiţionată.

Mesajul este etichetat drept spam dacă:

P(spam | X) = 1 - P(¬spam | X)

P(spam | X) > 0.5
putem creste limita de 0.5 daca nu vrem riscul de a clasifica gresit (ex: 0.8)


---

3.1. Calculaţi rata de promovare la fiecare disciplină, separat pentru fiecare program.
P(P1, A) = 81/90
         = 9/10
         = 90%

P(P2, A) = 1/10
         = 10%

P(P1, B) = 19/20
         = 95/100
         = 95%

P(P2, B) = 72/80
         = 9/10
         = 90%

3.2. Care disciplină are o rată de promovare mai mare în fiecare program?
Program 1: Disciplina B
Program 2: Disciplina B

3.3. Calculaţi rata globală de promovare pentru cele două discipline.
A_global = (81 + 1) / (90 + 10)
         = 82 / 100
         = 82%

B_global = (19 + 72) / (20 + 80)
         = 91 / 100
         = 91%

3.4. Explicaţi de ce ordinea disciplinelor se inversează atunci când agregăm datele.

Nu avem un paradox Simpson, pentru că ordinea rămâne aceeași și după agregare: B este mai bună atât separat, cât și global.

3.5. Formulaţi fenomenul în termeni de probabilităţi condiţionate.

P(promovare | A) = P(promovare | A, P1) * P(P1 | A) + P(promovare | A, P2) * P(P2 | A)
P(promovare | B) = P(promovare | B, P1) * P(P1 | B) + P(promovare | B, P2) * P(P2 | B)

P(promovare | A) = 90% * 90% + 10% * 10% = 81% + 1% = 82%
P(promovare | B) = 95% * 20% + 90% * 80% = 19% + 72% = 91%
