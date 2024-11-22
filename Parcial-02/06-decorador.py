# Crear un decorador con el nombre “decorador_mensaje” que
# imprima un mensaje antes y después de la ejecución de la función
# decorada.


def decorador_mensaje(funcion):
    def nueva_funcion():
        print("Mensaje antes del decorador")
        funcion()
        print("Mensaje despues del decorador")
    return nueva_funcion


@decorador_mensaje
def funcion_principal():
    print("Esta es la fucion principal")


funcion_principal()
# Salida -> Mensaje antes del decorador
# Salida -> Esta es la fucion principal
# Salida -> Mensaje despues del decorador
