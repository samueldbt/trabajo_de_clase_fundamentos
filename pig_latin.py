#reglas del pig latin
#si la palabra con una vocal se le agrega "ay" al final
#si la palabra empieza con una consonante o varias, estas consonantes iniciales se mueven al final
#y se le añade "ay" al final de la palabra

w = input("palabra para convertir: ")
r = 0

for i in w: #se itera por cada digito de la palabra w

    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u": # en caso de que empiece en vocal
        print(w + "ay")
        break
    
    while True:
        if i != "a" and i != "e" and i != "i" and i != "o" and i != "u": #mientras no sea vocal
            w = w + i
            w = w[r + 1:] # esto es el slicing de python, que use para poder modificiar la cadena

        elif i == "a" or i == "e" or i == "i" or i == "o" or i == "u": #el momento en que la palaba que empieza con consonantes llega a la vocal
            print(w + "ay")
            break
        break #los breaks son para salir de todos los bucles y finalizar el algoritmo.