from model.subsistema_base import SubsistemaBase

class SistemaResiduos(SubsistemaBase):

    def __init__(self, limite_maximo=100):
        super().__init__("Control de Residuos")
        self.reciclables = 0
        self.no_reciclables = 0
        self.limite_maximo = limite_maximo

    def agregar_residuo(self, tipo: str, cantidad: int):
        tipo_normalizado = tipo.lower().replace(" ", "_")
        if tipo_normalizado == "reciclable":
            self.reciclables += cantidad
        elif tipo_normalizado == "no_reciclable":
            self.no_reciclables += cantidad
        else:
            print("Tipo de residuo desconocido.")
            return

        total = self.reciclables + self.no_reciclables
        if total > self.limite_maximo:
            self.alarma.activar("Exceso de residuos sin evacuar")
        print(f"Residuos totales: {total}/{self.limite_maximo}")

    def evacuar(self):
        self.reciclables = 0
        self.no_reciclables = 0
        print("Residuos evacuados.")

    def mostrar_estado(self):
        total = self.reciclables + self.no_reciclables
        print(f"Reciclables: {self.reciclables}")
        print(f"No reciclables: {self.no_reciclables}")
        print(f"Total: {total}/{self.limite_maximo}")
        print(f"Estado de la alarma: {self.alarma.estado()}")
