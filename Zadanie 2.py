import matplotlib.pyplot as plt

kategoria = ["Elektronika", "Odzież", "Artukuły spożywcze", "Książki", "Sport"]
sprzedaż = [200, 250, 220, 150, 290]

plt.figure(figsize = (8, 8))
plt.pie(sprzedaż, labels = kategoria, autopct = "%1.1f%%", startangle= 140,
colors= ['lightcoral', 'gold', 'lightgreen', 'lightskyblue', 'red'])

plt.title("Procentowy udział różnych kategorii w całkowitej sprzedaży", fontsize = 14)

plt.tight_layout()
plt.show()