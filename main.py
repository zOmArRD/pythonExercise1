class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


# Creamos un objeto de la clase Rectangulo
mi_rectangulo = Rectangulo(5, 3)

# Calculamos el área y el perímetro utilizando los métodos de la clase
area_rectangulo = mi_rectangulo.area()
perimetro_rectangulo = mi_rectangulo.perimetro()

# Imprimimos los resultados
print("El área del rectángulo es:", area_rectangulo)
print("El perímetro del rectángulo es:", perimetro_rectangulo)