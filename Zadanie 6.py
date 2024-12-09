import numpy as np

#A
tablica_A = np.zeros((3,3), dtype = int)
tablica_A [2, :] = 1
print("Tablica A:\n", tablica_A)

#B
tablica_B = np.zeros((3, 3), dtype = int)
tablica_B[1:, 1] = 1
print("\nTablica B:\n", tablica_B)

#C
tablica_C = np.ones((3, 3), dtype = int)
tablica_C [0, :] = 0
print("\nTablica C:\n", tablica_C)

#D
tablica_D = np.ones((3, 3), dtype = int)
tablica_D[:, 1] = 0
tablica_D[2:, :] = 0
print("\nTablica D:\n", tablica_D)

#E
tablica_E = np.zeros((3, 3), dtype=int)
tablica_E[1:, 1:] = 1
print("\nTablica E:\n", tablica_E)