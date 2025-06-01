import numpy as np
from time import perf_counter_ns


A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]

print(A)
print(B)

filasA = len(A)
colsA = len(A[0])
filasB = len(B)
colsB = len(B[0])

C = []



inicio = perf_counter_ns()
for i in range(filasA):
    temp = []
    for j in range(colsB):
        temp.append(0)
    C.append(temp)

if filasB == colsA :
    for i in range(filasA):
        for j in range(colsB):
            c = 0
            for k in range(filasB):
                c = c + A[i][k] * B[k][j]
                print(f"fila {i}, col {j}, celda {k} - C[{i}][{j}] = {c}")
            C[i][j] = c
    
    print(C)
fin = perf_counter_ns()

print(f"Se demoro {fin - inicio} ns")
    
A2 = np.array(A)
B2 = np.array(B)

filasA, colsA = A2.shape
filasB, colsB = B2.shape

inicio = perf_counter_ns()

C = np.zeros( (filasA, colsB))
print(C)

if filasB ==  colsA :
    for i in range(filasA):
        for j in range(colsB):
            for k in range(colsA):
                C[i, j] = C[i, j] + A2[i, k] * B2[k, j]
            
    print(C)

fin = perf_counter_ns()

print(f"Se demoro {fin - inicio} ns")

C = np.zeros( (filasA, colsB))
if filasB ==  colsA :
    for i in range(filasA):
        for j in range(colsB):
            C[i, j] = sum(A2[i,:]*B2[:, j])
            
    print(C)
    
D = A2 @ B2
print(D)

E = A2*B2
print(E)
