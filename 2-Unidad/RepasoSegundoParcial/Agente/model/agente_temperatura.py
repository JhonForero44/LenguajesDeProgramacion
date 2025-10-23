from model.agente import Agente

class AgenteTemperatura(Agente):

    def __init__(self, nombre, tipo = "temperatura", bateria=100):
        super().__init__(nombre, tipo, bateria)

    def operar(self):
        if self._bateria >= 5:
            self._bateria -= 5
            print(f"El agente {self._nombre}, realizo la actividad de ajustar la temperatura, carga actual: {self._bateria}")
        else:
            print(f"El agente {self._nombre}, de tipo {self._tipo}, no puede trabajar sin antes ser cargado.")