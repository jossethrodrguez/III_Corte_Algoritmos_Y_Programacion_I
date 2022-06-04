# 3/6/2022 | Algoritmos y Programacion I | Josseth Rodriguez 30.502.713

import sys
array = [12, 4, 6, 13, 15, 0, 4, 15, 25, 22, 8, 10, 23, 13, 12, 11, 3, 15, 14, 23, 7, 13, 9, 8, 20, 26, 6, 1, 18, 0];
longitud = len(array);

def selectionSort(array):
   

    # este bucle recorre todo el array
    for i in range(longitud):
            
            indice = i; 
            # este bucle evaluara en cada espacio buscando el valor minimo
            for j in range(i + 1, longitud):
                if array[indice] > array[j]:
                    indice = j;

             
            array[i], array[indice] = array[indice], array[i];

print("asi es como estaba el array : ", array);

selectionSort(array);
print("ahora el array ordenado de forma ascendente es: ", array);
