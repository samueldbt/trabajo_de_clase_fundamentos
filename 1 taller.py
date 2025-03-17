#1. Construir un programa que lea un número variable de valores enteros. El resultado que entregara el
#programa es la media de los números pares de entre los leídos, es decir, la suma de todos los valores
#pares dividida por el número de estos. 

c = int(input("Cantidad de numeros:"))
m = 0
p = 0

for i in range(c):
    t = int(input("numero uwu: "))
    if t % 2 == 0:    
        m = m + t
        p = p + 1 
    
print(m/p)
    
    