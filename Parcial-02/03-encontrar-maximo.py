# Crear un script de python que contenga una función con el
# nombre “encontrar_maximo”, reciba como único parámetros una lista
# de números y retorne el numero máximo encontrado en la lista.

# Utilizando max() funcion incorporada de python
def encontrar_maximo(numeros):
    return max(numeros)


print(encontrar_maximo([1, 2, 5, 3, 4]))  # Salida -> 5


# Utilizando un bucle for para encontrar el numero maximo de la lista
def encontrar_max(numeros):
    maximo = 0
    for i in numeros:
        if i > maximo:
            maximo = i
    return maximo


print(encontrar_max([1, 2, 5, 4]))  # Salida -> 5
