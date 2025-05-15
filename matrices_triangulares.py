#saber si una matriz es triangular o no

n = int(input("size of the matrix: "))
matriz = []     

for i in range(n):
    fila = list(map(int, input().split())) #bof con eso me ahorro como 5 lineas de codigo  
    matriz.append(fila)

for fila in matriz:
    print(" ".join(map(str, fila)))

es_triangular_superior = True
es_triangular_inferior = True
for i in range(n):
    for j in range(n):
        if i > j and matriz[i][j] != 0:
            es_triangular_superior = False

for i in range(n):
    for j in range(n):
        if i < j and matriz[i][j] != 0:
            es_triangular_inferior = False

if es_triangular_superior == True:
    print("es triangular superior")
elif es_triangular_inferior == True:
    print("es triangular inferior")
else:
    print("no es triangular")