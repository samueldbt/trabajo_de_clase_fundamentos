n = int(input("Numero para convertir: ")) #se pide el numero para convertir a la base x
m = 0
factor = 1


while True: # este while True hace las veces de un do-while, para pedir un valor y checar su correctitud
    b = int(input("base a la que lo convertiras: ")) # un valor: 2 <= x < 10
    if b >= 2 and b < 10:
        break #con el break sale forzosamente del while True, asi no se queda en bucle infinito

while n > 0: #conversion del numero a la base indicada
    r = n % b
    n = float(n) // b
    m = m + factor * r
    factor = factor * 10

print(int(m)) # imprime el numero en su version de la base x
