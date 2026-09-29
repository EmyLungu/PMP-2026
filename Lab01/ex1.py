import random


def a(afisare: bool = False) -> bool:
    urna = ["r"] * 3 + ["a"] * 4 + ["n"] * 2

    zar = random.randint(1, 6)
    if zar in [2, 3, 5]:
        urna.append("n")
    elif zar == 6:
        urna.append("r")
    else:
        urna.append("a")

    [bila] = random.sample(urna, 1)
    urna.remove(bila)

    if afisare:
        print("urna =", urna, "bila =", bila)

    return bila == "r"


def b() -> None:
    n_simulari = 1_000_000
    succese = sum(a() for _ in range(n_simulari))
    prob_estimata = succese / n_simulari
    print(prob_estimata)


"""
c)
6 cazuri
I.      2, 3, 5 (3 cazuri)  -> 3 rosii
II.     6       (1 caz)     -> 4 rosii
III.    1, 4    (2 cazuri)  -> 3 rosii

3/6 * 3/10 +
1/6 * 4/10 +
2/6 * 3/10
= 0.31666666666

b) 0.316493 | 0.316836 | 0.316892
"""

if __name__ == "__main__":
    a(afisare=True)
    b()
