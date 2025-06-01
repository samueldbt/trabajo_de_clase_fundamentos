import random as rnd

n = int(input("n: "))
lista = []
for i in range(n):
    lista.append(rnd.randint(0, 100))

max = lista[0]
posmax = 0

for i in range(len(lista)):
    if lista[i] > max:
        max = lista[i]
        posmax = i
    
print(lista)
print(f"El maximo es {max}, en la posicion {posmax}")    

min = lista[0]
posmin = 0
for i, x in enumerate(lista):
    if x < min:
        min = x
        posmin = i
    
print(f"EL minimo es {min}, en la posición {posmin}")

for j in range(len(lista)):
    for i in range(len(lista)-1):
        if lista[i] > lista[i + 1] :
            '''temp = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = temp '''
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            print(lista)
            
print(lista)
