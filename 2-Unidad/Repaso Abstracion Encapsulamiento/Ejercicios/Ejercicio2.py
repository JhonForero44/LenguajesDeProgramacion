#Importar libreria
from abc import ABC, abstractmethod

class Empleado(ABC):
    
    def __init__(self, identificacion: int, nombre: str, salario: float, horasTrabajadas: int, anioIngreso: int, bonificaciones: float = 0, deducciones: float = 0):
        self.identificacion = identificacion
        self.nombre = nombre
        self.salario = salario
        self.horasTrabajadas = horasTrabajadas
        self.anioIngreso = anioIngreso
        self.bonificaciones = bonificaciones
        self.deducciones = deducciones

    
    def mostrarInfo(self):
        return f"ID: {self.identificacion}, Nombre: {self.nombre}, Hotas Trabajadas: {self.horasTrabajadas}"

    def calcularAntiguedad(self, anioActual: int):
        return 2025 - self.anioIngreso

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
    
    def __init__(self, identificacion, nombre, horasTrabajadas, anioIngreso):
        # aquí no pedimos salario base, se usa valorHora
        super().__init__(identificacion, nombre, self.valorHora, horasTrabajadas, anioIngreso)
    
    def calcularSalario(self):
        return (self.horasTrabajadas * self.valorHora) 
    
# 🔹 Lista de empleados mezclados
empleados = [
    tiempoCompleto(1111, "Ana", 10000, 8, 2020, bonificaciones=5000, deducciones=2000),
    medioTiempo(1112, "Luis", 12000, 6, 2022, bonificaciones=2000),
    prestacionServicios(1113, "Carolina", 10, 2024)
]

# 🔹 Recorrer con polimorfismo
for e in empleados:
    print(e.mostrarInfo())
    print("  Salario calculado:", e.calcularSalario())
    print("-" * 50)