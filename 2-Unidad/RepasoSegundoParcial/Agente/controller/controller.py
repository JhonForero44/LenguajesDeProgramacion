from controller.crear_agente import CrearAgente

class Controlado:
    _instancia = None

    def __new__(cls):
        if cls._instancia  is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.agentes = []
        return cls._instancia
    
    def agregarAgente(self, tipo, nombre):
        crear = CrearAgente()
        agente = crear.crearAgente(tipo, nombre)
        self.agentes.append(agente)
        print(f"Agente {nombre}, tipo: {tipo}, fue agregado correctamente.")
        pass

    def listarAgente(self):
        if not self.agentes:
            print("No se han agregado agentes!!!")
        else:
            print("Lista de agentes:")
            for a in self.agentes:
                print(f"- {a.nombre()} ({a.tipo()}) - batería: {a.bateria()}%")

    def operarAgente(self):
        if not self.agentes:
            print("No hay agentes para operar!!!")
        else:
            for a in self.agentes:
                a.operar()

    def cargarAgente(self):
        for a in self.agentes:
            a.cargar_bateria()
