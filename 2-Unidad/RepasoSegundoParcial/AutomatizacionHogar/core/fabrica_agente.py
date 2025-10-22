from model.agente_luz import AgenteLuz
from model.agente_temperatura import AgenteTemp
from model.agente_residuos import AgenteResiduos

class FabricaAgentes:
    def crear_agente(self, tipo, nombre):
        tipo = tipo.lower()
        if tipo == "luz":
            return AgenteLuz(nombre)
        elif tipo == "temperatura":
            return AgenteTemp(nombre)
        elif tipo == "residuos":
            return AgenteResiduos(nombre)
        else:
            raise ValueError(f"Tipo de agente desconocido: {tipo}")
