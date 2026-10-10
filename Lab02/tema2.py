import numpy as np
import pandas as pd


def ex1() -> None:
    N = 100_000

    x = np.random.randint(1, 7, size=N)
    y = np.random.randint(1, 7, size=N)

    x_par = x % 2 == 0
    y_par = y % 2 == 0
    sum_min_10 = x + y >= 10
    sum_8 = x + y == 8

    prob_1 = np.sum(sum_min_10 & x_par) / np.sum(x_par)
    print("1.1.\t", prob_1)

    prob_2 = np.sum(sum_min_10 & (x_par | y_par)) / np.sum(x_par | y_par)
    print("1.2.\t", prob_2)

    prob_3 = np.sum((x_par & y_par) & sum_8) / np.sum(sum_8)
    print("1.3.\t", prob_3)


def ex2() -> None:
    df = pd.DataFrame(
        {
            "Program": ["P1", "P1", "P2", "P2"],
            "Disciplina": ["A", "B", "A", "B"],
            "Promovati": [9, 8, 1, 0],
            "Total": [10, 10, 10, 1],
        }
    )

    df["Rata"] = df["Promovati"] / df["Total"]
    print(df)

    print("\n Local")
    print(df.pivot(index="Program", columns="Disciplina", values="Rata"))

    print("\n Global")
    global_df = pd.DataFrame(
        {
            "Promovati": df.groupby("Disciplina")["Promovati"].sum(),
            "Total": df.groupby("Disciplina")["Total"].sum(),
        }
    )
    global_df["Rata"] = global_df["Promovati"] / global_df["Total"]
    # A: (9+1)/(10 + 10) = 10/20 = 50%
    # B: (8+0)/(10 + 1) = 8/11 = 72%
    print(global_df)


if __name__ == "__main__":
    # ex1()
    ex2()
