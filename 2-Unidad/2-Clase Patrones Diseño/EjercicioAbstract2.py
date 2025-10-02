#Ejercicio 4: Animales
#Define una clase abstracta Animal con:
from abc import ABC, abstractmethod
class Animal(ABC):

    @abstractmethod
    def hacer_sonido(self):
        pass

#método abstracto hacer_sonido()
#Implementa:
#Perro → “Guau”
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"
    
#Gato → “Miau”
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"
    
#Vaca → “Muuu”
class Vaca(Animal):
    def hacer_sonido(self):
        return "Muuu"
    
#Recorre una lista de animales y haz que todos hagan su sonido.
animales = [Perro(), Gato(), Vaca()]
for animal in animales:
    print(animal.hacer_sonido())