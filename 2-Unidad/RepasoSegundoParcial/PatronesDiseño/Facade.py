#Facade (Fachada)
#🧠 Idea:
#Simplifica el acceso a un sistema complejo, ofreciendo una interfaz única y fácil de usar.

# Subsistemas
class CPU:
    def encender(self): print("CPU encendida")
class Memoria:
    def cargar(self): print("Memoria cargada")
class DiscoDuro:
    def leer(self): print("Disco duro leído")

# Fachada
class Computadora:
    def iniciar(self):
        print("Iniciando sistema...")
        cpu = CPU()
        memoria = Memoria()
        disco = DiscoDuro()
        cpu.encender()
        memoria.cargar()
        disco.leer()
        print("Sistema iniciado ✅")

# Uso
pc = Computadora()
pc.iniciar()
