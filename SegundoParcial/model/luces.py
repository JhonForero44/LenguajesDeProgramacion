from model.subsistema_base import SubsistemaBase

class SistemaLuces(SubsistemaBase):

    def __init__(self, habitaciones=3, luces_por_habitacion=2):
        super().__init__("Control de Luces")
        self.habitaciones = habitaciones
        self.luces_por_habitacion = luces_por_habitacion
        self.luces = []  
        for h in range(habitaciones):
            luces_habitacion = []
            for l in range(luces_por_habitacion):
                luces_habitacion.append(False)
            self.luces.append(luces_habitacion)

    def encender(self, habitacion, luz):
        try:
            self.luces[habitacion-1][luz-1] = True
            print(f"Luz {luz} de habitación {habitacion} encendida.")
        except IndexError:
            self.alarma.activar("Intento de encender una luz inexistente")

    def apagar(self, habitacion, luz):
        try:
            self.luces[habitacion-1][luz-1] = False
            print(f"Luz {luz} de habitación {habitacion} apagada.")
        except IndexError:
            self.alarma.activar("Intento de apagar una luz inexistente")

    def mostrar_estado(self):
        print(f"Habitaciones: {self.habitaciones}")
        for i, luces_hab in enumerate(self.luces):
            print(f"  Habitación {i + 1}: ", end="")
            for l in luces_hab:
                if l:
                    print("ON", end=" ")
                else:
                    print("OFF", end=" ")
            print()
        print(f"Estado de la alarma: {self.alarma.estado()}")
