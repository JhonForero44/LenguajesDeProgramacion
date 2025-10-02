#Ejercicio 1: Figuras geométricas
from abc import ABC, abstractmethod
#Crea una clase abstracta Figura que tenga:
class Figura(ABC):
    def __init__(self, lado):
        self.lado = lado
    
#un método abstracto area()
    @abstractmethod
    def area(self):
        pass

#un método abstracto perimetro()
    @abstractmethod
    def perimtero(self):
        pass

#Implementa las clases hijas:
#Cuadrado (con atributo lado)
class cuadrado(Figura):    
    
    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return self.lado * 4
    
#Circulo (con atributo radio)
class circulo(Figura):
    def area(self):
        return 3.14 * (self.lado ** 2)

    def perimetro(self):
        return 2 * 3.14 * self.lado


#Muestra el área y perímetro de cada figura.
cuadrado1 = cuadrado(4)
print("Área del cuadrado:", cuadrado1.area())
print("Perímetro del cuadrado:", cuadrado1.perimetro())

circulo1 = circulo(5)
print("Área del círculo:", circulo1.area())
print("Perímetro del círculo:", circulo1.perimetro())