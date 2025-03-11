#4. Construir un programa que lea dos números y si son ambos pares o ambos impares, halle el máximo
#común divisor de dos números; si uno es par y el otro impar, el programa debe hallar el mínimo común
#múltiplo.

n = int(input("primer numero: "))
m = int(input("segundo numero: "))

if n % 2 == 0 and m % 2 == 0: 
    if n < m:
        for i in range(1, n + 1, 1):
            if n % i == 0 and m % i == 0:
                mcd = i
    else:
        if n > m:
            i = 1
            while i <= m:
                if n % i == 0 and m % i == 0:
                    mcd = i
                i = i + 1
        else:
            mcd = n
    print(mcd)
    


if n % 2 == 0 and m % 2 != 0:
    
    n = int(input())
    m = int(input())
    if n > m:
        for i in range(n * m, n - 1, -1):
            if i % n == 0 and i % m == 0:
                mcm = i
    else:
        if n < m:
            for i in range(n * m, m - 1, -1):
                if i % n == 0 and i % m == 0:
                    mcm = i
        else:
            mcm = m
    print(mcm)
