from model.agente import Agente

class AgenteResiduos(Agente):
    def operar(self):
        if self._bateria > 20:
            self._bateria -= 20
            print(f"🗑️ {self._nombre}: gestionando residuos... batería al {self._bateria}%")
        else:
            print(f"⚠️ {self._nombre}: batería baja, recarga necesaria.")
