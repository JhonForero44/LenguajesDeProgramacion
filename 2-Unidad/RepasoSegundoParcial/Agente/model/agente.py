class Agente():
    def __init__(self, nombre, tipo="Generico", bateria = 100):
        self._nombre = nombre
        self._bateria = bateria
        self._tipo = tipo

    def nombre(self):
        return self._nombre

    def bateria(self):
        return self._bateria

    def tipo(self):
        return self._tipo

    def cargar_bateria(self):
        self._bateria = 100
        print(f"Agente {self._nombre}, tipo {self._tipo}, cargado al 100%")

    def operar(self):
        pass