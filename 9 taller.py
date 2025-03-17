#9. Construir un programa que muestre los términos de la serie de Fibonacci que sean menores o iguales a
#un valor entero dado por el usuario.

#se muestran n numeros de fibonacci, los cuales son menores que l
penultimo = 0
ultimo = 1
suma = 0
i = 1
n = int(input())
l = int(input())
print(penultimo)
print(ultimo)
while i <= n:
    suma = penultimo + ultimo
    penultimo = ultimo
    ultimo = suma
    if ultimo < l:
        print(ultimo)
    i = i + 1
