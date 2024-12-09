import numpy as np

def macierz_z_obramowaniem(size = 5):
    macierz = np.zeros((size, size), dtype = int)
    macierz[0, :] = 1
    macierz[-1, :] = 1
    macierz[:, 0] = 1
    macierz[:, -1] = 1
    return macierz

def inwert_macierz(macierz):
    return np.where(macierz == 0, 1, 0)

macierz1 = macierz_z_obramowaniem()
print("Macierz początkowa:\n", macierz1)

macierz_odwrocona = inwert_macierz(macierz1)
print("\nMacierz po zamieanie:\n", macierz_odwrocona)