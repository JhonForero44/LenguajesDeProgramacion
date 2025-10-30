class Comando:
    def ejecutar(self):
        pass

class ComandoEncenderLuz(Comando):
    def __init__(self, sistema, habitacion, luz):
        self.sistema = sistema
        self.habitacion = habitacion
        self.luz = luz

    def ejecutar(self):
        self.sistema.encender(self.habitacion, self.luz)

class ComandoApagarLuz(Comando):
    def __init__(self, sistema, habitacion, luz):
        self.sistema = sistema
        self.habitacion = habitacion
        self.luz = luz

    def ejecutar(self):
        self.sistema.apagar(self.habitacion, self.luz)

class ComandoSubirTemperatura(Comando):
    def __init__(self, sistema, habitacion):
        self.sistema = sistema
        self.habitacion = habitacion

    def ejecutar(self):
        self.sistema.subir_temperatura(self.habitacion)

class ComandoEvacuarResiduos(Comando):
    def __init__(self, sistema):
        self.sistema = sistema

    def ejecutar(self):
        self.sistema.evacuar()