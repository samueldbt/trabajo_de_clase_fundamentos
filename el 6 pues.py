#6. Escribir un programa que reciba una entrada n, que es un número entero. El programa devolverá una
#lista de números enteros hasta n, incluyéndolo, y especificando si el número es divisible por 2, 3 o por
#5, o si es divisible por ambos. 

n = int(input("Un numero entero: "))

for i in range(n + 1): #lista de numeros hasta n
    #es el numero i divisible por 2?
    div2 = False
    div3 = False
    div5 = False
    if i % 2 == 0:
        div2 = True
        
    #es divisible por 3? 
    if i % 3 == 0:
        div3 = True
        
    #es divisible por 5?
    if i % 5 == 0:
        div5 = True
    
    #si el numero es divisible por alguno, imprimir por cual o si es por 2 imprimir esos 2
    if div2 == True and div3 == True and div5 == True: #divisible por los 3
        print(f"{i} es divisible por 2,3 y 5")
    elif div2 == True and div3 == True: #divisible por 2 y 3
        print(f"{i} es divisible por 2 y 3")
    elif div3 == True and div5 == True: #divisible por 3 y 5
        print(f"{i} es divisible por 3 y 5")
    elif div2 == True and div5 == True: #divisible por 2 y 5
        print(f"{i} es divisible por 3 y 5")
    elif div2 == True: #por 2
        print(f"{i} divisible por 2")
    elif div3 == True: #por 3
        print(f"{i} divisible por 3")
    elif div5 == True: #por 5
        print(f"{i} divisible por 5")
    else:
        print(f"{i} que numero es ese wtf")
       
        