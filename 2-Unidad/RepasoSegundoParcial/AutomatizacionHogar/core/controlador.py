from core.fabrica_agente import FabricaAgentes

class ControladorHogar:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.agentes = []
        return cls._instancia

    def agregar_agente(self, tipo, nombre):
        fabrica = FabricaAgentes()
        agente = fabrica.crear_agente(tipo, nombre)
        self.agentes.append(agente)
        print(f"✅ Agente '{nombre}' de tipo '{tipo}' agregado correctamente.")

    def listar_agentes(self):
        if not self.agentes:
            print("❌ No hay agentes registrados.")
        else:
            print("\n📋 Lista de agentes:")
            for a in self.agentes:
                print(f"- {a.nombre()} ({a.__class__.__name__}) - batería: {a.bateria()}%")

    def operar_agentes(self):
        if not self.agentes:
            print("❌ No hay agentes para operar.")
        else:
            for a in self.agentes:
                a.operar()

    def cargar_todos(self):
        for a in self.agentes:
            a.cargar_bateria()
