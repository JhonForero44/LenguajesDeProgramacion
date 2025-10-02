#Interfaz
#En Python no existe la palabra reservada "interface" (como en Java o C#).
#Se simula creando una clase abstracta solo con métodos abstractos, sin lógica dentro.
#Sirve para definir un contrato: “si una clase implementa esta interfaz, debe tener estos métodos”.

from abc import ABC, abstractmethod

class INotificacion(ABC):  # Interfaz
    @abstractmethod
    def enviar(self, mensaje):
        pass

class EmailNotificacion(INotificacion):
    def enviar(self, mensaje):
        print(f"Enviando Email: {mensaje}")

class SMSNotificacion(INotificacion):
    def enviar(self, mensaje):
        print(f"Enviando SMS: {mensaje}")

e = EmailNotificacion()
e.enviar("Hola!")   # Enviando Email: Hola!
