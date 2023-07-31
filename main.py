#  Created by PyCharm
#
#  User: zOmArRD
#  Date: 30/7/2023
#
#  Copyright (c) 2023. zOmArRD <dev@zomarrd.me>

from abc import ABC, abstractmethod


class Figura(ABC):
    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimetro(self):
        pass


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self._base = base
        self._altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        self._base = value

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, value):
        self._altura = value

    @property
    def area(self):
        return self.base * self.altura

    @property
    def perimetro(self):
        return 2 * (self.base + self.altura)


# Creamos un objeto de la clase Rectangulo
rectangulo = Rectangulo(10, 20)

# Modificamos los atributos usando las propiedades (getters y setters)
rectangulo.base = 7
rectangulo.altura = 4

# Calculamos el área y el perímetro utilizando los métodos de la clase
area_rectangulo = rectangulo.area
perimetro_rectangulo = rectangulo.perimetro

# Imprimimos los resultados
print("El área del rectángulo es:", area_rectangulo)
print("El perímetro del rectángulo es:", perimetro_rectangulo)
