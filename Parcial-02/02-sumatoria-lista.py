# Crear un script de python que contenga una función con el
# nombre “sumar_lista”, reciba como único parámetros una lista de
# números y retorne la sumatoria de todos los números de la lista.


# Utilizando sum() que es una funcion incorporada de python para sumar elementos de un iterable.
def sumar_lista(lista):
    return sum(lista)


print(sumar_lista([1, 2, 3, 4, 5]))  # Salida -> 15


# Utilizando un bucle for para sumar todos los elementos de la lista
def sumar(numeros):
    sumatoria = 0
    for i in numeros:
        sumatoria = i + sumatoria
    return sumatoria


print(sumar([1, 2, 3, 4, 5]))  # Salida -> 15
