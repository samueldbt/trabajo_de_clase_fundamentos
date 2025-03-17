#2. Construir un programa que lea un número entero mayor que 2 y devuelva como resultado el
#número primo de valor más cercano, en este caso menor o igual, al número leído.
while True:
    m = int(input("numero: "))
    if m >= 2:
        break
    else:
        print("no")

for n in range(2, m+1):
    divisores = 0
    i = 2
    while i < n :
        if n % i == 0 :
            divisores = divisores + 1
        i = i + 1
        
    if divisores <= 0 :
        p = n
print(p)
        
