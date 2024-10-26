# Crear un script con un diccionario mi_diccionario con tres
# pares de clave:valor, de 3 tipos diferentes
# Imprimir el valor de la primer clave.
# Añade un nuevo par clave:valor al diccionario.
# Intenta cambiar el valor de la segunda clave existente.
# Imprimir el contenido del diccionario en pantalla.


mi_diccionario = {
    "nombre": "Franco",
    "documento": 12345678,
    "activo": True
}

print(mi_diccionario["nombre"])

mi_diccionario["ciudad"] = "Viedma"

# Los diccionarios en python son mutables
mi_diccionario["documento"] = 1234


print(mi_diccionario)
