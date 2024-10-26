# Escribir un programa que le solicite al usuario ingresar una
# calificación del 0 al 100, la asigne a una variable y muestre la
# calificación alfabética correspondiente (A, B, C, D, F) según el
# numero ingresado. Correspondiendo cada letra con valores de 20 en
# 20. Es decir: 0 a 19 = A, de 20 a 39 = B, etc

calificacion = int(input("Ingrese la calificación de 0 a 100 : "))

if calificacion <= 19:
    print("Calificación A")
elif calificacion <= 39:
    print("Calificación B")
elif calificacion <= 59:
    print("Calificación C")
elif calificacion <= 79:
    print("Calificación D")
else:
    print("Calificación F")
