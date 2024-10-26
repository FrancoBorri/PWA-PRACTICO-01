# Escribir un programa que tome dos números y muestre el mayor
# de ellos. Utilizando unicamente la sentencia If-else.

a = input("Ingrese el primer numero: ")
b = input("Ingrese el segundo numero: ")

if a > b:
    # formateo de strings
    print(f"El numero {a} es mayor que {b}")
else:
    print(f"El numero {b} es mayor que {a}")
