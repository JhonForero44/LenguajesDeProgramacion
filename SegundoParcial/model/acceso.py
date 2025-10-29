from model.subsistema_base import SubsistemaBase

class SistemaAcceso(SubsistemaBase):

    def __init__(self):
        super().__init__("Control de acceso")
        self.usuarios = {} 
        self.intentos_fallidos = 0
        self.personas_adentro = 0

    def agregar_usuario(self, nombre: str, codigo: int):
        if nombre in self.usuarios:
            print(f"El usuario {nombre} ya existe.")
        else:
            self.usuarios[nombre] = codigo
            print(f"Usuario {nombre} agregado correctamente.")

    def verificar_acceso(self, codigo: int):
 
        if codigo in self.usuarios.values():
            print("Acceso permitido. Bienvenido.")
            self.personas_adentro += 1
            self.intentos_fallidos = 0
        else:
            self.intentos_fallidos += 1
            print("Acceso denegado. Código incorrecto.")

            if self.intentos_fallidos >= 3:
                self.alarma.activar("Demasiados intentos fallidos de ingreso")

    def mostrar_estado(self):
        print("\n Estado del sistema de acceso:")
        print(f"Usuarios registrados: {list(self.usuarios.keys())}")
        print(f"Personas dentro: {self.personas_adentro}")
        print(f"Intentos fallidos: {self.intentos_fallidos}")
        print(f"Estado de alarma: {self.alarma.estado()}")
