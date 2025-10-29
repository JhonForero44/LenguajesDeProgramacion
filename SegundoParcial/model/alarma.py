class Alarma:
    def __init__(self):
        self.activa = False
        self.mensaje = ""

    def activar(self, mensaje: str):
        self.activa = True
        self.mensaje = mensaje
        print(f" ALARMA ACTIVADA: {mensaje}")

    def desactivar(self):
        self.activa = False
        self.mensaje = ""
        print(" Alarma desactivada")

    def estado(self):
        return "Activa" if self.activa else "Inactiva"