class AdaptadorResiduos:
    def __init__(self, sistema_residuos):
        self.sistema = sistema_residuos

    def ejecutar(self, accion, *args):
        if accion == "agregar":
            self.sistema.agregar_residuo(*args)
        elif accion == "evacuar":
            self.sistema.evacuar()
        else:
            print("Acción desconocida para residuos.")

    def mostrar_estado(self):
        self.sistema.mostrar_estado()