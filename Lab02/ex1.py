import numpy as np

p_B = 0.01
sens = 0.95 # P(+ | B)
spec = 0.90 # P(- | not B)
p_fals_poz = 1 - spec # P(+ | not B)

p_poz = (sens * p_B) + (p_fals_poz * (1 - p_B))
p_B_poz_teoretic = (sens * p_B) / p_poz

print(f"Probabilitate teoretica \t P(B|+) = {p_B_poz_teoretic:.6f} ({p_B_poz_teoretic * 100:.2f}%)")

N = 10_000_000
este_bolnav = np.random.rand(N) < p_B

rezultat_test = np.zeros(N, dtype=bool)

n_bolnavi = int(np.sum(este_bolnav))
n_sanatosi = int(np.sum(~este_bolnav))

rezultat_test[este_bolnav] = np.random.rand(n_bolnavi) < sens
rezultat_test[~este_bolnav] = np.random.rand(n_sanatosi) < p_fals_poz

pozitivi = rezultat_test
bolnavi_si_pozitivi = este_bolnav & pozitivi

p_B_poz_simulat = np.sum(bolnavi_si_pozitivi) / np.sum(pozitivi)

print(f"Probabilitate simulata \t\t P(B|+) = {p_B_poz_simulat:.6f} ({p_B_poz_simulat * 100:.2f}%)")
