import numpy as np
import matplotlib.pyplot as plt

potęgi_dwa = [128, 64, 32, 16, 8, 4, 2, 1]

wagi = np.array(potęgi_dwa)

liczba_bin = np.random.randint(0, 2, size = 8)

def wartość_liczby_bin (wagi, liczba_bin):
    return np.sum(wagi * liczba_bin)

wartość = wartość_liczby_bin(wagi, liczba_bin)

nagłówki = ["Wagi", "Liczba bin"]
dane = list(zip(wagi, liczba_bin))

fig, ax = plt.subplots(figsize = (6, 3))
ax.axis("tight")
ax.axis("off")
table = ax.table(cellText= dane, colLabels = nagłówki, cellLoc = "center", loc = "center")

plt.title(f"Wartość liczby binarnej {wartość}", fontsize = 14)

plt.show()