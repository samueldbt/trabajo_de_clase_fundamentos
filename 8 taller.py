#8. Escribir un programa que lea un entero positivo y escriba el mismo número conformado por las cifras
#del número leído más 1. Si al sumar uno a una cifra da 10 se debe poner 0. Por ejemplo:
#12345 → 23456.
#987654 → 098765.

n = input("numero entero positivo: ")
l = len(n)

n_n = ""
for i in range(l):
    c = int(n[i])  + 1

    if c == 10:
        c = 0
    n_n = n_n + str(c)

print(n_n)
