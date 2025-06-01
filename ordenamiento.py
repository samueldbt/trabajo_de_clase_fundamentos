import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter_ns

def insertion_sort(L):
    i = 1
    operaciones = 0
    while i < len(L):
        j = i
        while j > 0 and L[j - 1] > L[j]:
            operaciones += 1
            L[j], L[j - 1] = L[j - 1], L[j]
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
        operaciones += 1
    return L, operaciones
def bubble_sort(L):
    n = len(L)
    comparaciones = 0
    for i in range(n - 1):
        for j in range(n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
               
            comparaciones += 1
    return L, comparaciones



num_elements = np.arange(10, 101, 10)
print(num_elements)
size = num_elements.size
print(size)

cm = np.zeros(size)
cm2 = np.zeros(size)
cm3 = np.zeros(size)

t_bubble = np.zeros(size)
t_selection = np.zeros(size)
t_insertion = np.zeros(size)
t_quick_sort = np.zeros(size)

for i, n in enumerate(num_elements) :
    vector = np.random.randint(0, 100, n, dtype=np.int16) 
    vector_ord = vector.copy()
    A,cm[i] = bubble_sort(vector_ord)
    vector_ord = vector.copy() 
    A,cm2[i] = selection_sort(vector_ord)
    vector_ord = vector.copy() 
    A,cm3[i] = insertion_sort(vector_ord)
    
    
    print(A)


plt.plot(num_elements,cm, "g-", num_elements,cm2,"b-",num_elements,cm3,"r-")
plt.show()
