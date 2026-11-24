# Laborator 8 — Efectul lui Y și θ asupra distribuției a posteriori

Avem un număr a priori de clienți $n \sim \text{Poisson}(10)$ și $Y \sim \text{Binomial}(n, \theta)$ cumpărători.

## Efectul lui Y (câți clienți au cumpărat)
- **Stabilește minimul:** $n$ nu poate fi mai mic decât $Y$ ($n \ge Y$).
- **Mută graficul spre dreapta:** Cu cât $Y$ e mai mare ($0 \rightarrow 5 \rightarrow 10$), cu atât ne așteptăm la mai mulți clienți în total.
- **Nu schimbă împrăștierea:** Forma/lățimea distribuției rămâne la fel pentru un $\theta$ dat, doar se deplasează.

## Efectul lui θ (probabilitatea de cumpărare)
- **Scade media estimată când θ crește:** Dacă oamenii cumpără mai ușor ($\theta = 0.5$ față de $0.2$), e nevoie de mai puțini clienți în total pentru a obține același număr $Y$ de vânzări.
- **Face graficul mai îngust:** Un $\theta$ mai mare înseamnă mai puțină incertitudine în jurul estimării.

## Pe scurt (pentru a priori Poisson(10))
- **Media a posteriori:** $Y + 10(1 - \theta)$
- **Exemplu la $Y = 10$:** media este **18** la $\theta = 0.2$, dar scade la **15** la $\theta = 0.5$.