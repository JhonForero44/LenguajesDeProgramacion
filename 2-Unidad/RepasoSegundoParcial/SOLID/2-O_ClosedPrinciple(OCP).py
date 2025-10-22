#👉 “El código debe estar abierto para extenderse, pero cerrado para modificarse.”
#🧠 Idea:
#Si necesitas agregar funciones nuevas, no modifiques el código existente, crea nuevas clases o métodos que lo extiendan.

#❌ Mal ejemplo:
def calcular_area(figura):
    if figura["tipo"] == "circulo":
        return 3.14 * figura["radio"]**2
    elif figura["tipo"] == "cuadrado":
        return figura["lado"]**2


#Cada vez que se agregue una nueva figura, hay que modificar la función.

#✅ Buen ejemplo:
class Figura:
    def area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return 3.14 * self.radio**2

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado**2