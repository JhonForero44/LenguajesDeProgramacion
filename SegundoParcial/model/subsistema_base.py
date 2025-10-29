from model.bateria import Bateria
from model.alarma import Alarma

class SubsistemaBase:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.baterias = [Bateria(100), Bateria(80), Bateria(60)]
        self.alarma = Alarma()

    def verificar_baterias(self):
        for b in self.baterias:
            if b.verificar_bateria():  
                return True            
        return False                   

    def estado_baterias(self):
        niveles = []
        for b in self.baterias:
            niveles.append(b.nivel_carga)
        return niveles
