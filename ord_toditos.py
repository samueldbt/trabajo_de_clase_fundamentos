import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter_ns

def bubble_sort(L):
    n = len(L)
    operaciones = 0
    #intercambios = 0
    for i in range(n - 1):
        for j in range(n - i - 1):
            operaciones += 1
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                #intercambios += 1
        #print(f"paso {i + 1}: {L}")

    return L, operaciones

def insertion_sort(L):
    operaciones = 0
    i = 1
    while i < len(L):
        j = i
        while j > 0 and L[j - 1] > L[j]:
            operaciones += 1
            L[j], L[j - 1] = L[j - 1], L[j]
            #intercambios += 1
            j -= 1
        i += 1
    return L, operaciones

def selection_sort(L):
    operaciones = 0
    for i in range(len(L) - 1):
        min = i
        for j in range(i + 1, len(L)):
            operaciones += 1
            if (L[min] > L[j]):
                min = j
        if min != i:
            L[min], L[i] = L[i], L[min]
            #intercambios += 1
            operaciones += 1


    return L, operaciones
    #t1_fin = perf_counter_ns()
    #print(f"Número de operaciones realizadas: {operaciones}.  Número de intercambios: {intercambios}")
    #print(f"Tiempo utilizado (ns): { t1_fin - t1_inicio }")
    
    
num_elements = np.arange(10, 101, 10)

print(num_elements)
size = num_elements.size
print(size)
#print(num_elements)
op = np.zeros(size)
op2 = np.zeros(size)
op3 = np.zeros(size)

t_bubble = np.zeros(size)
t_selection = np.zeros(size)
t_insertion = np.zeros(size)
t_quick_sort = np.zeros(size)
# como se cancela ? 
# mi mama su me 

for i, n in enumerate(num_elements) :
    vector = np.random.randint(0, 100, n, dtype=np.int16) # se crea el vector a ordenar
    # acá se hace una copia de ese vector, para preservar el vector con números aleatorios.
    vector_ord = vector.copy()
    # acá viene la estructura para tomar el tiempo
    t_inicio = perf_counter_ns()
    A, op[i] = bubble_sort(vector_ord) # se ejecuta el método burbuja con el vector copia
    t_final = perf_counter_ns()
    t_bubble[i] = t_final - t_inicio # se guarda el tiempo para n elementos, para crear una gráfica.
    print(f"Vector ordenado: \n{A}")
    vector_ord = vector.copy() # volvemos a copiar el vector aleatorio original sobre el vector copia para
    # que el siguiente método trabaje sobre los mismos datos
    print(f"Vector sin ordenar: \n{vector_ord}")
    t_inicio = perf_counter_ns()
    A, op2[i] = insertion_sort(vector_ord)
    t_final = perf_counter_ns()
    t_insertion[i] = t_final - t_inicio
    print(A)
    #uwu
    t_inicio = perf_counter_ns()
    A, op3[i] = selection_sort(vector_ord)
    t_final = perf_counter_ns()
    t_selection[i] = t_final - t_inicio
    print(A)
    

z = True
while z == True:
    print("que quieres hacer papu")
    r = int(input("operaciones en funcion de algo o lo otro o nada(1/2/3): "))
    if r == 1:
        #valores de booleanos del menu
        #aqui mostramos el operaciones en funcion de lo otro    
        plt.plot(num_elements, op, "g-", num_elements, op2, "b-", num_elements, op3, "r-")
        plt.show()
        #z = False
    elif r == 2: 
        #aqui mostramos la cantidad de tiempo en funcion de lo otro
        plt.plot(num_elements, t_bubble, "g-", num_elements, t_insertion, "b-", num_elements, t_selection, "r-")
        plt.show()
        #z = False    
    elif r == 3:
        print("chao papu")
        z = False
    else:
        print("ponlo bien papu")
        #z = False