import numpy as np
import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

N_esantioane = 10000
lambdas = [3.0, 6.0, 4.0]
probabilitati = [3/13, 6/13, 4/13]

frizeri_alesi = np.random.choice([0, 1, 2], size=N_esantioane, p=probabilitati)
X = np.array([np.random.exponential(scale=1/lambdas[f]) for f in frizeri_alesi])

media_X = np.mean(X)
std_X = np.std(X)

print(f"Media estimata a lui X: {media_X:.4f} ore ({media_X * 60:.2f} minute)")
print(f"Deviatia standard estimata a lui X: {std_X:.4f} ore")

kde = gaussian_kde(X)
x_grid = np.linspace(0, np.max(X), 1000)

plt.plot(x_grid, kde(x_grid), label="Densitate estimata a lui X (KDE)", color="crimson", lw=2)
plt.xlabel("Timpul de servire X (ore)")
plt.ylabel("Densitate")
plt.title("Estimarea densitatii distributiei timpului de servire X")
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()
