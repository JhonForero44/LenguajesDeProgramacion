from model.agente import Agente

class AgenteLuz(Agente):
    def __init__(self, nombre, tipo = "luz", bateria=100):
        super().__init__(nombre, tipo, bateria)

    def operar(self):
        if self._bateria >= 15:
            self._bateria -= 15
            print(f"El agente {self._nombre}, realizo la actividad de apagar la luz, carga actual: {self._bateria}")
        else:
            print(f"El agente {self._nombre}, de tipo {self._tipo}, no puede trabajar sin antes ser cargado.")
