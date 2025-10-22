#1. Command (Comando)
#🧠 Idea:
#Convierte una acción (comando) en un objeto, para poder ejecutarla, deshacerla o almacenarla fácilmente.

# Receptor: quien realiza la acción real
class Luz:
    def encender(self):
        print("💡 La luz está encendida")
    def apagar(self):
        print("💡 La luz está apagada")

# Comando abstracto
class Comando:
    def ejecutar(self):
        pass

# Comandos concretos
class EncenderLuz(Comando):
    def __init__(self, luz):
        self.luz = luz
    def ejecutar(self):
        self.luz.encender()

class ApagarLuz(Comando):
    def __init__(self, luz):
        self.luz = luz
    def ejecutar(self):
        self.luz.apagar()

# Invocador: quien da la orden
class ControlRemoto:
    def __init__(self, comando):
        self.comando = comando
    def presionar_boton(self):
        self.comando.ejecutar()

# Uso
luz = Luz()
control = ControlRemoto(EncenderLuz(luz))
control.presionar_boton()
