class Bateria:

    def __init__(self, nivel_carga: int = 100):
        self.nivel_carga = nivel_carga

    def verificar_bateria(self):
        return self.nivel_carga == 100

    def descargar(self, cantidad: int):
        self.nivel_carga = max(0, self.nivel_carga - cantidad)

    def cargar(self):
        self.nivel_carga = 100

    def nivel(self):
        return f"Batería: {self.nivel_carga}%"