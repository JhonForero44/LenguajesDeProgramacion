#Importar libreria
from abc import ABC, abstractmethod

class Empleado(ABC):
    
    def __init__(self, identificacion: int, nombre: str, salario: float, horasTrabajadas: int):
        self.identificacion = identificacion
        self.nombre = nombre
        self.salario = salario
        self.horasTrabajadas = horasTrabajadas
    
    def mostrarInfo(self):
        return f"ID: {self.identificacion}, Nombre: {self.nombre}, Horas Trabajadas: {self.horasTrabajadas}"

    @abstractmethod
    def calcularSalario(this):
        pass
    
class tiempoCompleto(Empleado):
    
    def calcularSalario(self):
        return self.salario * self.horasTrabajadas

class medioTiempo(Empleado):
    
    def calcularSalario(self):
        return (self.salario * self.horasTrabajadas) / 2

class prestacionServicios(Empleado):
    valorHora = 3000
    
    def __init__(self, identificacion, nombre, horasTrabajadas):
        # aquí no pedimos salario base, se usa valorHora
        super().__init__(identificacion, nombre, self.valorHora, horasTrabajadas)
    
    def calcularSalario(self):
        return (self.horasTrabajadas * self.valorHora) 
    
# 🔹 Lista de empleados mezclados
empleados = [
    tiempoCompleto(1111, "Jhon", 10000, 8),
    medioTiempo(1112, "Arley", 10000, 8),
    prestacionServicios(1113, "Forero", 8)
]

# 🔹 Recorrer con polimorfismo
for e in empleados:
    print(e.mostrarInfo())
    print("  Salario calculado:", e.calcularSalario())
    print("-" * 50)