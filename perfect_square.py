#perfect squares cases
def es_primo(n):
    divisores = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisores += 1
    return divisores == 2


while True: 
    cantidad_casos = int(input("cantidad de casos: "))
    if cantidad_casos > 0:
        break


for i in range(cantidad_casos): #realiza el bucle el numero de veces que dijo el usuario, o sea el numero de casos
    x = int(input("numero: "))
    base = x
    factores = {}
    for j in range(2, x + 1):
        if x % j == 0 and es_primo(j):
            contador = 0
            while x % j == 0:
                contador += 1
                x = x// j
            factores[j] = contador  
    y = 1
    for p, e in factores.items():
        if e % 2 != 0:
            y *= p          

    print(f"el valor para el caso {base} es {y}")     
        
    
