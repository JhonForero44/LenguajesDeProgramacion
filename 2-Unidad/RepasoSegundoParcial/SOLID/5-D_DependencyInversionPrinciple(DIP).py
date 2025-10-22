#👉 “Depende de abstracciones, no de cosas concretas.”
#🧠 Idea:
#Las clases grandes no deben depender directamente de detalles o implementaciones específicas.

#❌ Mal ejemplo:
class MotorGasolina:
    def arrancar(self):
        print("Motor de gasolina encendido")

class Coche:
    def __init__(self):
        self.motor = MotorGasolina()  # depende directamente

    def encender(self):
        self.motor.arrancar()

#➡️ Si quieres cambiar a un motor eléctrico, toca modificar Coche.

#✅ Buen ejemplo:
class Motor:
    def arrancar(self):
        pass

class MotorGasolina(Motor):
    def arrancar(self):
        print("Motor de gasolina encendido")

class MotorElectrico(Motor):
    def arrancar(self):
        print("Motor eléctrico encendido")

class Coche:
    def __init__(self, motor: Motor):
        self.motor = motor

    def encender(self):
        self.motor.arrancar()

# Uso
coche1 = Coche(MotorGasolina())
coche2 = Coche(MotorElectrico())