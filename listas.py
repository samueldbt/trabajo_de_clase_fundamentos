A = []
print(A)
n = int(input("Numero de elementos: "))
for i in range(n):
    A.append(float(input(f"Elemento {i}: ")))
    
print(A)

suma = 0
for i in range(len(A)):
    print(A[i])
    suma = suma + A[i]

print(suma)
if len(A) > 0 :
    print(f"Promedio es {suma/len(A)}")
    
suma = 0
for x in A:
    print(x)
    suma = suma + x
