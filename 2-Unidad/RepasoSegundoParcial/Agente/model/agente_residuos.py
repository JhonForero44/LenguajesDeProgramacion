from model.agente import Agente

class AgenteResiduos(Agente):
    def __init__(self, nombre, tipo = "residuos", bateria=100):
        super().__init__(nombre, tipo, bateria)

    def operar(self):
        if self._bateria >= 10:
            self._bateria -= 10
            print(f"El agente {self._nombre}, realizo la actividad de sacar los residuos, carga actual: {self._bateria}")
        else:
            print(f"El agente {self._nombre}, de tipo {self._tipo}, no puede trabajar sin antes ser cargado.")