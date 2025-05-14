'''
a code in where you get a string from the user, then ask for a number N with what
you make all the combinations posibles with the number N of items of the string at a
time, showing all this combinations to the user at the end
estoy desarrollando el siguiente problema de programación en Python, guíame en el 
desarrollo del código y hazme el acompañamiento como si fueras un profesor 
didactico/pedagogico y no me des el codigo puntualmente, a este debo llegar yo por mi cuenta con tu ayuda
'''
# get the string
string = input("cadena que combinar: ")

# clean the string
conjunto = set(string)
lista = list(conjunto)
lista.sort()

# get the number at a time
m = len(lista)
while True: 
    n = int(input("cuantos caracteres a la vez: "))
    if 0 <= n <= m:
        break
    else:
        print("ERROR 1")

#combinatione


def permutar(restantes, elegidos):
    if len(elegidos) == n:
        print("".join(elegidos))
        return
    else:
        for i in range(len(restantes)):
            char = restantes[i]
            nuevos_elegidos = elegidos + [char]
            nuevos_restantes = restantes[:i] + restantes[i+1:]
            permutar(nuevos_restantes, nuevos_elegidos)

permutar(lista, [])