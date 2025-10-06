#Importar librerias
from abc import ABC, abstractmethod

#1. abstract 
#Una clase abstracta es una clase que no se puede instanciar directamente (no puedes hacer new de ella).
#Puede tener métodos abstractos (sin implementación, solo firma) y también métodos normales con código.
#Se usa cuando quieres dar una plantilla común para que las subclases la completen.
#Clase abstracta
class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass  # método abstracto (sin implementación)

    def dormir(self):
        print("Zzz...")  # método normal

#2. interface (Interfaz)
#Una interfaz es un contrato: define qué métodos deben implementarse, pero no tiene código dentro (en algunos lenguajes modernos ya puede tener default o static methods).
#Una clase puede implementar varias interfaces (múltiple herencia de comportamiento).
#Se usa cuando quieres garantizar que todas las clases que la implementen tengan los mismos métodos, sin importar su jerarquía.
# 🔹 Interfaz simulada (usando ABC)
class Volador(ABC):
    @abstractmethod
    def volar(self):
        pass

#3. extends (Herencia)
#extends significa que una clase hereda de otra.
#Se usa con clases (y también con interfaces en algunos casos).
#Cuando una clase extiende otra, hereda sus atributos y métodos, y puede sobreescribirlos (override).
#Clase que hereda de Animal (extends) e implementa Volador (interface)
class Pajaro(Animal, Volador):
    def hacer_sonido(self):
        print("Pío Pío 🐦")

    def volar(self):
        print("El pájaro vuela alto 🚀")

#Uso
p = Pajaro()
p.hacer_sonido()  # Implementación propia
p.volar()         # Cumple la "interfaz"
p.dormir()        # Método heredado de Animal