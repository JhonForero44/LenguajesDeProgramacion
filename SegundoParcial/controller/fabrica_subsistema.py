from model.acceso import SistemaAcceso
from model.luces import SistemaLuces
from model.temperatura import SistemaTemperatura
from model.residuos import SistemaResiduos

class FabricaSubsistemas:

    def crear_subsistema(tipo: str):
        tipo = tipo.lower()

        if tipo == "acceso":
            return SistemaAcceso()
        elif tipo == "luces":
            return SistemaLuces()
        elif tipo == "temperatura":
            return SistemaTemperatura()
        elif tipo == "residuos":
            return SistemaResiduos()
        else:
            raise ValueError("Tipo de subsistema no reconocido.")