from model.subsistema_base import SubsistemaBase

class SistemaTemperatura(SubsistemaBase):

    def __init__(self, habitaciones=3, temp_min=18, temp_max=28):
        super().__init__("Control de Temperatura")
        self.habitaciones = habitaciones
        self.temp_actual = [22 for _ in range(habitaciones)]
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.termostato_encendido = True

    def subir_temperatura(self, habitacion):
        if not self.termostato_encendido:
            print("Termostato apagado.")
            return
        self.temp_actual[habitacion] += 1
        if self.temp_actual[habitacion] > self.temp_max:
            self.alarma.activar("Temperatura demasiado alta")
        print(f"Habitación {habitacion+1}: {self.temp_actual[habitacion]}°C")

    def bajar_temperatura(self, habitacion):
        if not self.termostato_encendido:
            print("Termostato apagado.")
            return
        self.temp_actual[habitacion] -= 1
        if self.temp_actual[habitacion] < self.temp_min:
            self.alarma.activar("Temperatura demasiado baja")
        print(f"Habitación {habitacion+1}: {self.temp_actual[habitacion]}°C")

    def mostrar_estado(self):
        for i, t in enumerate(self.temp_actual):
            print(f"Habitación {i+1}: {t}°C")
        print(f"Termostato: {'Encendido' if self.termostato_encendido else 'Apagado'}")
        print(f"Estado de la alarma: {self.alarma.estado()}")
