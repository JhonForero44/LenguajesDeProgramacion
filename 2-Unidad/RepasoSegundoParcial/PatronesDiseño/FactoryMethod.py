#Factory Method (Método de Fábrica)
#🧠 Idea:

#Permite crear objetos sin especificar la clase exacta que se va a crear.
#La decisión se delega a las subclases.

# Producto base
class Animal:
    def hablar(self):
        pass

# Productos concretos
class Perro(Animal):
    def hablar(self):
        return "Guau!"

class Gato(Animal):
    def hablar(self):
        return "Miau!"

# Creador (Fábrica)
class FabricaAnimales:
    def crear_animal(self, tipo):
        if tipo == "perro":
            return Perro()
        elif tipo == "gato":
            return Gato()
        else:
            return None

# Uso
fabrica = FabricaAnimales()
animal = fabrica.crear_animal("gato")
print(animal.hablar())
