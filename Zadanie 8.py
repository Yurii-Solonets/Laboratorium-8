import numpy as np

macierz  = np.random.randint(0, 1010, size = (5, 5))
print("Macierz losowa:\n", macierz)

elementy_większe_20 = macierz[macierz > 20]
liczba_elementów = len(elementy_większe_20)

średnia_tablicy = macierz.mean()

print("\nLiczba elementów większych niż 20: ", liczba_elementów)
print("\nŚrendia dla całej tablicy: ", round(średnia_tablicy, 2))