from model.agente import Agente

class AgenteLuz(Agente):
    def operar(self):
        if self._bateria > 10:
            self._bateria -= 10
            print(f"💡 {self._nombre}: luces encendidas. Batería al {self._bateria}%")
        else:
            print(f"⚠️ {self._nombre}: batería baja, recarga necesaria.")