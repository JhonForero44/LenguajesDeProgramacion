from model.agente_luz import AgenteLuz
from model.agente_residuos import AgenteResiduos
from model.agente_temperatura import AgenteTemperatura

class CrearAgente():
    def crearAgente(self, nombre, tipo):
        tipo = tipo.lower()
        if tipo == "luz":
            return AgenteLuz(nombre)
        elif tipo == "residuos":
            return AgenteResiduos(nombre)
        elif tipo == "temperatura":
            return AgenteTemperatura(nombre)
        else:
            return f"Tipo {tipo} de agente desconocido.!!!"