#codigo que da un menu con + - * / y debera funcionar hasta escoger la opcion salir
while True:

    while True: 
        n = input ("escribe la operaion que deseas hacer (+, -, /, * o 'salir'): ")

        if n == "+" or n == "-" or n == "*" or n == "/" or "salir":
            break

    if n == "+":
        a = float(input("digita un numero para sumar: "))
        b = float(input("digita otro: /"))
        print(f"el resultado de la suma es {a + b}")

    if n == "-":
        a = float(input("digita un numero para restar: "))
        b = float(input("digita otro: "))
        print(f"la diferencia es {a - b}")

    if n == "*":
        a = float(input("digita un numero para mutiplicar: "))
        b = float(input("digita otro: "))
        print(f"el producto es {a * b}")

    if n == "/":
        a = float(input("digita un numero para dividir: "))
        while True:
            b = float(input("digita otro: "))
            if b != 0:
                break
            else:
                print("uno distinto de 0 po")

        print(f"el cociente es {a / b}")

    if n == "salir":
        print("fin de la operacion.")
        break
