import numpy as np

n = int(input("filas: "))
m = int(input("columnas: "))
matriz = np.random.randint(1, 10, (n, m))
transpuesta = np.zeros((m, n), dtype=int)

for i in range(n):
    for j in range(m):
        transpuesta[j][i] = matriz[i][j]

print(matriz)
print(transpuesta)
