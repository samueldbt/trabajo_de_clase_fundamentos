#10. Construir un programa que muestre el siguiente término de la serie de Fibonacci respecto a un valor
#entero dado por el usuario.  


n = int(input("Introduce un número entero: "))
ultimo = 1
penultimo = 0

while ultimo <= n:
    ultimo = ultimo + penultimo 
    penultimo = ultimo - penultimo

print(ultimo)