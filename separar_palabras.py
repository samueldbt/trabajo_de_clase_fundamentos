entrada = input("dame una frase: ")
longitud = len(entrada)
separador = " "
palabra = ""

for i in range(longitud):
    if entrada[i] == " ":
        print(palabra)
        palabra = ""
    else:
        palabra = palabra + entrada[i]
        
print(palabra)
