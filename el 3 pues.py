#3. Construir un programa que lea un entero positivo n y determine si dicho número es un cuadrado de otro
#entero, o sea, que tiene raíz cuadrada entera.
while True: 
    n = int(input("numero entero positivo: "))
    if n > 0:
        break
    else:
        print("un dato correcto")
        
if n ** 0.5 % 1 == 0:
    print("tiene raiz cuadrada")
else:
    print("no tiene raiz cuadrada")