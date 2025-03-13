n = int(input("Numero para convertir: ")) #se pide el numero para convertir a la base x
z = n

factor = 1
m1 = 0
m2 = 0
m3 = 0
m4 = 0
a = 2
b = 4
c = 8
d = 16
hex = "ABCDEF"

while n > 0: #conversion del numero a la base 2
    r = n % a
    n = float(n) // a
    m1 = m1 + factor * r
    factor = factor * 10

factor = 1
n = z
while n > 0: #conversion del numero a la base 4
    r = n % b
    n = float(n) // b
    m2 = m2 + factor * r
    factor = factor * 10

factor = 1
n = z
while n > 0: #conversion del numero a la base 8
    r = n % c
    n = float(n) // c
    m3 = m3 + factor * r
    factor = factor * 10

factor = 1
n = z  
while n > 0: #conversion del numero a la base 16
    r = n % d
    #posicion IGUAL A LA r MAS 1
    
    n = float(n) // d
    m4 = m4 + factor * r
    factor = factor * 10
    # n = n (qque es el cociente) concatenado con la posicion en el arreglo


print(f"En base 2: {int(m1)}. En base 4: {int(m2)}. En base 8: {int(m3)}. En base 16: {int(m4)}") # imprime el numero en su version de la base x