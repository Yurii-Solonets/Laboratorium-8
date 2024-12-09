import matplotlib.pyplot as plt
import numpy as np

czas = np.linspace(0, 20, 21)
szybkość = [0, 5, 10, 15, 20, 25, 30, 32, 34, 35, 36, 35, 34, 32, 30, 25, 20, 15, 10, 5, 0]

plt.figure(figsize = (8, 5))
plt.scatter(czas, szybkość, color = "blue", label = "Przędkość chwilowa")

plt.title("Przędkość chwilowa pojazdu w czasie", fontsize = 14)
plt.xlabel("Czas (s)", fontsize = 12)
plt.ylabel("Przędkość (m/s)", fontsize = 12)

plt.legend()

plt.tight_layout()
plt.show()