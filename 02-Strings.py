# Crear un script de python que contenga una variable mi_nombre
# y asignarle tu nombre como string. Luego mostrar el tipo de datos
# de la variable.
# Intentar acceder a la primera y última letra de mi_nombre
# utilizando índices y mostrándolos en pantalla.
# Utilizar la función len() para calcular la longitud de
# mi_nombre y mostrarlo.
# Imprimir en pantalla el contenido de la variable mi_nombre,
# todo en mayusculas y todo en minúsculas.

mi_nombre = "Franco"

print(type(mi_nombre))  # Imprime el tipo de dato
print(mi_nombre[0])   # 0 -> Accedo al primer valor.
print(mi_nombre[-1])  # -1 -> Cuenta hacia atras, accedo al ultimo valor.
print(len(mi_nombre))  # Imprime la longitud
print(mi_nombre.upper())  # Imprime todo en mayusculas
print(mi_nombre.lower())  # Imprime todo en minusculas
