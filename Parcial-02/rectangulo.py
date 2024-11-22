# Crear una clase `Rectangulo` que tenga los atributos `ancho` y
# `alto`. Además, debe tener dos métodos: `area` que calcule el área
# del rectángulo, y `perimetro` que calcule el perímetro.


class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)


rectangulo = Rectangulo(10, 5)
print(rectangulo.area())  # Salida -> 50
print(rectangulo.perimetro())  # Salida -> 30
