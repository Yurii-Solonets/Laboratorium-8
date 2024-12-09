import matplotlib.pyplot as plt

kategoria = ["ELektronika", "Odzież", "Artukyły spożywcze", "Książki", "Sport"]
sprzedaż = [200, 250, 220, 150, 290]

plt.figure(figsize = (8, 5))
plt.bar(kategoria, sprzedaż, color = "Skyblue", edgecolor = "black")

plt.title("Ilość sprzedanych produktów w różnych kategoriach", fontsize = 14)
plt.xlabel("Kategoria", fontsize = 12)
plt.ylabel("Ilośc sprzedanych produktów", fontsize = 12)

plt.tight_layout()
plt.show()