#Es una clase base que NO se puede instanciar directamente.
#Sirve para decir: “todas las clases hijas deben implementar estos métodos”.

#Puede tener:
#Métodos abstractos (sin lógica, solo la firma).
#Métodos normales (con lógica ya escrita).
#Se usa con abc.ABC y @abstractmethod.

from abc import ABC, abstractmethod

class Animal(ABC):  # Clase abstracta
    @abstractmethod
    def sonido(self):
        pass  # las hijas deben implementarlo

    def dormir(self):  # método normal opcional
        print("Zzz...")

class Perro(Animal):
    def sonido(self):
        print("Guau!")

p = Perro()
p.sonido()   # Guau!
p.dormir()   # Zzz...
