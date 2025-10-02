#Ejercicio
#Interfaz -> Clase abstracta solo con metodos abstractos

#Importar libreria de abstraccion
from abc import ABC, abstractmethod

class INotificacion(ABC):
    
    def __init__(self, usuario: str, numeroNotificacion: int):
        self.usuario = usuario
        self.numeroNotificacion = numeroNotificacion
    
    @abstractmethod
    def enviarNotificacion(this):
        pass

class NotificacionEmail(INotificacion):
    
    def enviarNotificacion(self):
        return f"[EMAIL] Enviando notificación a {self.usuario} con número {self.numeroNotificacion}"

class NotificacionSMS(INotificacion):
    
    def enviarNotificacion(self):
        return f"[SMS] Enviando notificación a {self.usuario} con número {self.numeroNotificacion}"
    
notificacion1 = NotificacionEmail("Jhon", 777)
print(notificacion1.enviarNotificacion())

notificacion2 = NotificacionSMS("Ana", 888)
print(notificacion2.enviarNotificacion())