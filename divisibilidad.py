n = int(input("cuantos numeros se mostraran en la lista: ")) #se motraran n numeros en pantalla

for i in range(n + 1): #en cada condicional checamos que sea divisible por algunos de los valores dados
    if (i % 2) == 0:
        print(i)
    elif (i % 3) == 0:
        print(i)
    elif (i % 5) == 0:
        print(i)

#luego de recorrer n numero en la recta numerica termina el programa