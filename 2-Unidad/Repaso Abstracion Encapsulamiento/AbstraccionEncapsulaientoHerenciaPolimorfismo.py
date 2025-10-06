#Explicación
#Abstracción → La clase Vehiculo es abstracta y define métodos que todas las subclases deben implementar (arrancar()).
#Encapsulamiento → La variable __velocidad está oculta (es privada) y solo puede modificarse mediante métodos de la clase.
#Herencia → Carro y Moto heredan de Vehiculo.
#Polimorfismo → El método arrancar() se comporta distinto en Carro y en Moto, pero se invoca de la misma manera.

from abc import ABC, abstractmethod

# 🔹 Abstracción: Clase abstracta que define el "qué" deben hacer los vehículos
class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.__velocidad = 0  # 🔹 Encapsulamiento: atributo privado

    @abstractmethod
    def arrancar(self):
        pass

    def acelerar(self, cantidad):
        self.__velocidad += cantidad
        print(f"{self.marca} {self.modelo} acelera a {self.__velocidad} km/h")

    def frenar(self):
        self.__velocidad = 0
        print(f"{self.marca} {self.modelo} se detuvo.")

# 🔹 Herencia: Carro y Moto heredan de Vehiculo
class Carro(Vehiculo):
    def arrancar(self):
        print(f"🚗 El carro {self.marca} {self.modelo} ha arrancado.")

class Moto(Vehiculo):
    def arrancar(self):
        print(f"🏍️ La moto {self.marca} {self.modelo} ha arrancado.")

# 🔹 Polimorfismo: distintos comportamientos para el mismo método arrancar()
def iniciar_vehiculo(vehiculo: Vehiculo):
    vehiculo.arrancar()
    vehiculo.acelerar(50)

# ---------------------------
# Uso del programa
# ---------------------------

carro1 = Carro("Toyota", "Corolla")
moto1 = Moto("Yamaha", "R6")

iniciar_vehiculo(carro1)   # llama arrancar() de Carro
iniciar_vehiculo(moto1)    # llama arrancar() de Moto
carro1.acelerar(30)
carro1.frenar()