import random as rnd

A = []
n = 10
for i in range(n):
    A.append(rnd.randint(0, 100))

print(A)

suma = 0
for i in range(len(A)):
    suma += A[i]

media = suma/len(A)
print(media)

Max = A[0]
pMax = 0
for i in range(len(A)):
    if A[i] > Max :
        Max = A[i]
        pMax = i
        
print(max)
print(Max)
print(pMax)
print(max(A))
