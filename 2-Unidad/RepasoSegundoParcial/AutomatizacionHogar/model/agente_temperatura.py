from model.agente import Agente

class AgenteTemp(Agente):
    def operar(self):
        if self._bateria > 15:
            self._bateria -= 15
            print(f"🌡️ {self._nombre}: ajustando temperatura... batería al {self._bateria}%")
        else:
            print(f"⚠️ {self._nombre}: batería insuficiente para ajustar temperatura.")
