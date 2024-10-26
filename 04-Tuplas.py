# Crear un script que contenga una tupla mi_tupla con tres tipos
# diferentes de datos.
# Crea una tupla con un solo elemento e imprimir su tipo de
# dato.


mi_tupla = (1, "Franco", True)  # Number, String, Boolean
# En python todo es un objeto.
# En este caso al crear la tupla se crea una instancia de la clase tuple


tupla_dos = ("Borri")
# En este caso python detecta que tupla_dos es un string


# Para que python reconozca que tupla_dos es una tupla se debe agregar una coma al final.
tupla_dos = ("Borri",)


# Tambien se puede utilizar el metodo tuple()
print(tuple(tupla_dos))
# En este caso python transforma tupla_dos en una tupla
# Toma cada uno de los valores de tupla_dos y los transforma en tupla
# La salida seria ('B', 'o', 'r', 'r', 'i')

print(type(mi_tupla))  # <class 'tuple'>
print(type(tupla_dos))   # <class 'tuple'>
