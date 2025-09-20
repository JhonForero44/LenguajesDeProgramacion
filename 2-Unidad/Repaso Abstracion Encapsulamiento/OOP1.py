#Conceptos basicos de POO en Python
#Abstraccion, Encapsulamiento, 
#Atributos de clase (estaticos) vs atributos instancia (requieren creacion)
class estudiante:
    
    #Atributo de clase (estatico)
    universidad = "Universidad Santiago de Cali"
    
    #Metodo de instancia (crea objetos)
    #Recibe como primer parametro self (hace referencia al objeto), referencia a la instancia
    #Se puede usar el this tambien o self
    def __init__(this, nombre: str, ciudad: str, carrera: str):
        this.nombre = nombre
        this.ciudad = ciudad
        this.carrera = carrera
        this.curso = []
        
    #Metodo de instancias (al usar this o self, se refiere a la instancia) 
    def matricularCurso(this, curso: str):
        this.curso.append(curso)
    
    #Metodos de clase
    @classmethod
    def cambiarRazonSocial(cls, nuevaRazonSocial):
        cls.universidad = nuevaRazonSocial
        
e1 = estudiante("Diego", "Cali", "Ingenieria de Sistemas")
e2 = estudiante("Carolina", "Cali", "Ingenieria Electronica")

print(f"El estudiante {e1.nombre} de la {e1.universidad} es de {e1.ciudad}")
e1.cambiarRazonSocial("Excelentisima Universidad Santiago de Cali - USC")
print(f"El estudiante {e2.nombre} de la {e2.universidad} es de {e2.ciudad}")
print(f"El estudiante {e1.nombre} de la {e1.universidad} es de {e1.ciudad}")

#Abstraccion + Encapsulamiento
#Importar libreria
from abc import ABC, abstractmethod

#CLASE ABSTRACTA
class Cuenta(ABC):
    def __init__(self, titular: str, numcuenta: int, saldo: float):
        self.titular = titular
        self.numcuenta = numcuenta
        self.saldo = saldo
        
    #Los metodos abstractos no tienen implementacion
    #La implementacion la tiene las subclases:
    @abstractmethod
    def calcular_rendimiento(this):
        #NO hacer nada
        pass
    
    def calcular_saldo(this):
        return f"El saldo de la cuenta es: {this.saldo}"   
    
    def depositar(this, monto: float):
        this.saldo = this.saldo + monto
        
    def retirar(this, monto: float):
        this.saldo = this.saldo - monto

class cuentaAhorros(Cuenta):
    
    por_rend = 0.1
    
    def calcular_rendimiento(this):
        #Ejercicio: implementar de acuerdo al atributo de clase propio de la cuenta de ahorros:
        this.saldo = this.saldo + (1.0 + this.por_rend)
        #return this.saldo * this.por_rend

class cuentaCorriente(Cuenta):
    
    cupo_sobregiro = 5000000
    
    def calcular_rendimiento(this):
        #Ejercicio: implementar de acuerdo al atributo de clase propio de la cuenta corriente.
        return "La cuenta corriente no genera rendimiento"
    
    def consultar_saldo(this):
        #Se sobre escribe el metodo de la clase padre
        return super().calcular_saldo() 

cuenta1 = cuentaAhorros("Diego Loaiza", 777, 150000000.0)
cuenta2 = cuentaCorriente("Diana Loaiza", 888, 50000000.0)

cuenta1.depositar(80000.0)
cuenta2.depositar(45000.0)

# ----------------- OJO: -----------------
# Una interfaz es una clase abstracta (Abstract base class en python) que solo tiene metodos abstractos (@abstractmethod)
#           (ES UN "CONTRATO") -> LAS SUBCLASES "IMPLEMENTAN"
# Una clase abstracta es un abstract base class que puede tener ciertas implementacion que pueden sobreescribirse o sobrecargadas
#           (ES UNA "GENERALIZACION") -> LAS SUBCLASES "EXTIENDEN")