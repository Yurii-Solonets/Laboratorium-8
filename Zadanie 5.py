import numpy as np
import matplotlib.pyplot as plt

tab4_2d = np.random.randint(1, 101, size = (5, 5))

największy_element = tab4_2d.max()
najmniejszy_element = tab4_2d.min()

największe_w_wierszach = tab4_2d.max(axis = 1)
największe_w_kolumnach = tab4_2d.max(axis = 0)

suma_wierzy = tab4_2d.sum(axis = 1)

table_dane = [
    ["Macierz"] + [f"Kol {i + 1}" for i in range (5) ]
]
table_dane += [[f"wiersz {i + 1}"] + list(tab4_2d[i]) for i in range (5)]
table_dane += [
    ["Największe w wierszach"] + list(największe_w_wierszach),
    ["Największe w kolumnach"] + list(największe_w_kolumnach),
    ["Suma w wierszach"] + list(suma_wierzy),
    ["Maks", największy_element, "", "", "", ""],
    ["Min", najmniejszy_element, "", "", "", ""],
]

max_cols = max(len(row) for row in table_dane)
for row in table_dane:
    while len(row) < max_cols:
        row.append("")

fig, ax = plt.subplots(figsize = (8, 6))
ax.axis = ("tight")
ax.axis = ("off")

table = ax.table(cellText = table_dane, cellLoc = "center", loc = "center")

plt.title("Analiza losowej macierzy", fontsize = 14)
plt.show()