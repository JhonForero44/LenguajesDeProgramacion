#Importar libreria
from abc import ABC, abstractmethod

#1. Implementa herrencia con clases abstractas (empleado -> tiempoCompleto, empleado -> contratista)
class Empleado(ABC):
    def __init__(self, nombre: str, salario: float):
        self.nombre = nombre
        self.salario = salario
        
    @abstractmethod
    def calcular_salario(this):
        pass
    
class EmpleadoTiempoCompleto(Empleado):
    def calcular_salario(this):
        return this.salario
    
class EmpleadoContratista(Empleado):
    def calcular_salario(this):
        return this.salario * 0.8 

#Imprimir resultados
Jhon = EmpleadoTiempoCompleto("Jhon", 2000000)
Arley = EmpleadoContratista("Arley", 2000000)  
print(f"El empleado de tiempo completo tiene un salario de {Jhon.calcular_salario()}")
print(f"El empleado  tiene un salario de {Arley.calcular_salario()}")    
    
#2. Implementar generalizacion ("herencia") con interfaces (notificaciones)
class Notificacion(ABC):
    @abstractmethod
    def enviar(this, mensaje: str):
        pass
    
class NotificacionEmail(Notificacion):
    def enviar(this, mensaje: str):
        return f"Enviando email con el mensaje: {mensaje}"

class NotificacionSMS(Notificacion):
    def enviar(this, mensaje: str):
        return f"Enviando SMS con el mensaje: {mensaje}"

email = NotificacionEmail()
sms = NotificacionSMS()
print(email.enviar("Hola, este es un email de prueba"))
print(sms.enviar("Hola, este es un SMS de prueba"))

#SINGLENTON Singlenton1.
# 1. Patrones Creacionales
# (a) - Singlenton
# Permite u obliga a que se use solo una instancia de clase como unico punto de acceso a una operacion logica
# del sistema

#Clase no singlenton:
class Persona():
    def __init__(self, nombre):
        self.nombre = nombre
        
class naive_singlento():
    #atributo de clase que almacena la instancia creada
    _instance = None
    
    #se va a lanzar error cuando se llame, para obligar a llamar el metodo create_instance
    def __init__(self):
        raise RuntimeError("use create_instance() method instead")
    
    #Se usa este metodo en vez de iniciarlizar para garantizar que se cree una sola instancia
    #@classmethod garantiza que el metodo sea estatico 
    #cls se usa aqui como el self
    @classmethod
    def create_instance(cls):
        #si no existe la instancia, se crea
        if cls._instance is None:
            #El metodo new tambien crea una instancia 
            cls._instance = cls.__new__(cls)
        #retorna la instancia
        return cls._instance

#Creamos objetos con el metodo que valida que no se crean mas instancias
object1 = naive_singlento.create_instance()
object2 = naive_singlento.create_instance()

Persona1 = Persona("Jhon")
Persona2 = Persona("Arley")

print(f"Son el mismo objeto?: {object1 is object2}")
print(f"Son el mismo objeto?: {Persona1 is Persona2}")

#Ejercicio: Usar el patron singlenton para simular el manejo de sesion de usuario de una plataforma de SW
# con la funcionalidad de autenticacion (simulado) con usuario y contraseña y (logout).

class naive_singlento_autenticacion():
    _instance = None
    usuario_actual = None
    
    def __init__(self):
        raise RuntimeError("use create_instance() method instead")
    
    @classmethod
    def create_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance
    
    def login(this, usuario: str, contrasena: str):
        #Simulacion de autenticacion
        if contrasena == "password123":
            this.usuario_actual = usuario
            return f"Usuario {usuario} ha iniciado sesion correctamente"
        else:
            return "Error de autenticacion"

    def logout(this):
        usuario = this.usuario_actual
        this.usuario_actual = None
        return f"Usuario {usuario} ha cerrado sesion correctamente"

usuario1 = naive_singlento_autenticacion.create_instance()
usuario2 = naive_singlento_autenticacion.create_instance()
print(f"Son el mismo objeto?: {usuario1 is usuario2}")
print(usuario1.login("Jhon", "password123"))
print(usuario2.login("Arley", "password123"))
print(usuario1.logout())
print(usuario2.logout())

#OPCION 2
print(f"----------------- OPCION 2 -----------------")


#AbstractFactorty
#(b) Factory Method: provee formas de crear objetos en una superclase (interfaz), pero son las subclases las que decidan como crearlos.

#Importar libreria
from abc import ABC, abstractmethod

#Producto (clase de  objetos) a crear 
class Itransporte(ABC):
    
    @abstractmethod
    def realizar_entrega(this):
        pass

#Las clases concretas quedan con la responsabilidad de definicir el comportamiento especifico
class Terrestre_Camion(Itransporte):
    def realizar_entrega(this):
        return "Entrega en Camion" 
    
class Terrestre_Motocicleta(Itransporte):
    def realizar_entrega(this):
        return "Entrega en Moto" 

class Aereo(Itransporte):    
    def realizar_entrega(this):
        return "Entrega Aerea" 

#Clase creadora - se le delega la creacion a esta clase (tiene el factory method)
class LogisticaEntregaBase(ABC):
    @abstractmethod
    def crear_metodoEntrega(self):
        pass
    
    #Se puede parametrizar la creacion de la subclases:
    def planificarEntrega(self):
        tipoTransporte = self.crear_metodoEntrega()
        return tipoTransporte.realizar_entrega()

#Uso de clases concretas
class entregaTesrrestre_Camion(LogisticaEntregaBase):
    def crear_metodoEntrega(self):
        return Terrestre_Camion()
    
class entregaTerrestre_Motocicleta(LogisticaEntregaBase):
    def crear_metodoEntrega(self):
        return super().crear_metodoEntrega()

#Uso
entrega_C = entregaTesrrestre_Camion() #La creacion de la clase concreta se delega a la clase creadora
print(entrega_C.planificarEntrega())
entrega_m = entregaTerrestre_Motocicleta()

#(c) Factory Method: Permite crear familias de objetos relacionados sin especificar sus clases concretas.


#Traer singlento hecho
#Repasar Factory Method