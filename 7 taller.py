#7. Escribir un programa que determine si un número entero es positivo, negativo o cero. Después,
#modificar el programa para que reciba entradas de números enteros hasta que el número introducido
# sea 0. El programa debe dar el conteo de positivos y negativos y los respectivos promedios.

n = int(input("numero cualquiera: "))
c_p = 0
c_n = 0
promedio_p = 0
promedio_n = 0


while n != 0:
    if n > 0:
        print("el numero es positivo")
        c_p += 1
        promedio_p = promedio_p + n
    elif n < 0:
        print("el numero es negativo") 
        c_n += 1
        promedio_n = promedio_n + n
    n = int(input("numero cualquiera: "))

if c_p != 0:
    promedio_p = promedio_p //  c_p

if c_n != 0:
    promedio_n = promedio_n //  c_n
print(f"el numero de positivos fue: {c_p}, y su respectivo promedio aproximado es: {promedio_p}")
print(f"el numero de positivos fue: {c_n}, y su respectivo promedio aproximado es: {promedio_n}")
print("el numero es 0")