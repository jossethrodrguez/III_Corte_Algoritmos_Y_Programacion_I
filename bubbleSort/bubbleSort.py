# 3/6/2022 | Algoritmos y Programacion I | Josseth Rodriguez 30.502.713

array = [12, 4, 6, 13, 15, 0, 4, 15, 25, 22, 8, 10, 23, 13, 12, 11, 3, 15, 14, 23, 7, 13, 9, 8, 20, 26, 6, 1, 18, 0];
longitud = len(array);

def bubbleSort(array):
    
    # Esta bucle repitara el procesor hasta que el ultimo elemento del Array
    for i in range(longitud):

        # Este bucle se encargara de realizar la comparacion entre elementos
        for j in range(0, longitud-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]; # Esta linea realiza la sustitucion


print("asi es como estaba el array : ", array);

bubbleSort(array);
print("ahora el array ordenado de forma ascendente es: ", array);




    








    