import numpy as np
import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt

def simuleaza_un_joc(p=0.5):
    n_pasi = 0
    while True:
        n_pasi += 1
        aruncare_moneda = np.random.choice([1, 0], p=[p, 1-p])
        
        if aruncare_moneda == 1:
            zar = np.random.randint(1, 7)
            castig_zar = zar - 3
            S = castig_zar - 0.5 * (n_pasi - 1)
            return n_pasi, S

def simuleaza_jocuri(numar_jocuri=100000, p=0.5):
    S_valori = []
    for _ in range(numar_jocuri):
        _, S = simuleaza_un_joc(p)
        S_valori.append(S)
    return np.array(S_valori)

numar_simulari = 100000
S_p_05 = simuleaza_jocuri(numar_simulari, p=0.5)
S_p_03 = simuleaza_jocuri(numar_simulari, p=0.3)
S_p_07 = simuleaza_jocuri(numar_simulari, p=0.7)

print(f"p = 0.5 -> Media aproximată a lui S: {np.mean(S_p_05):.4f} $")
print(f"p = 0.3 -> Media aproximată a lui S: {np.mean(S_p_03):.4f} $")
print(f"p = 0.7 -> Media aproximată a lui S: {np.mean(S_p_07):.4f} $")

fig, axes = plt.subplots(1, 3, figsize=(16, 4), sharey=True)

axes[0].hist(S_p_05, bins=30, color='skyblue', edgecolor='black', density=True)
axes[0].set_title(f"Moneda echilibrata (p=0.5)\nMedia S = {np.mean(S_p_05):.2f}$")
axes[0].set_xlabel("Suma S ($)")
axes[0].set_ylabel("Densitate")

axes[1].hist(S_p_03, bins=30, color='salmon', edgecolor='black', density=True)
axes[1].set_title(f"Moneda masluita (p=0.3)\nMedia S = {np.mean(S_p_03):.2f}$")
axes[1].set_xlabel("Suma S ($)")

axes[2].hist(S_p_07, bins=30, color='lightgreen', edgecolor='black', density=True)
axes[2].set_title(f"Moneda masluita (p=0.7)\nMedia S = {np.mean(S_p_07):.2f}$")
axes[2].set_xlabel("Suma S ($)")

plt.tight_layout()
plt.show()
