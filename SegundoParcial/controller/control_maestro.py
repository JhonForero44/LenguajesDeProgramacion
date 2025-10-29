from controller.fabrica_subsistema import FabricaSubsistemas
from controller.decoradores import VerificacionBateria
from controller.adaptadores import AdaptadorResiduos

class ControlMaestro:
    _instancia = None 

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(ControlMaestro, cls).__new__(cls)
        return cls._instancia

    def __init__(self):
        if not hasattr(self, "subsistemas"):
            self.subsistemas = {
                "acceso": FabricaSubsistemas.crear_subsistema("acceso"),
                "luces": FabricaSubsistemas.crear_subsistema("luces"),
                "temperatura": FabricaSubsistemas.crear_subsistema("temperatura"),
                "residuos": AdaptadorResiduos(FabricaSubsistemas.crear_subsistema("residuos")),
            }

            # Aplicamos el decorador de batería a todos los subsistemas menos residuos
            for clave, subsistema in self.subsistemas.items():
                if clave != "residuos":
                    self.subsistemas[clave] = VerificacionBateria(subsistema)

    def obtener_subsistema(self, nombre):
        return self.subsistemas.get(nombre)

    def verificar_estado_general(self):
        print("\nEstado general del sistema:")
        for nombre, subsistema in self.subsistemas.items():
            print(f"{nombre.upper()}:")
            if hasattr(subsistema, "mostrar_estado"):
                subsistema.mostrar_estado()
            else:
                print("Sin método de estado disponible.")
            print("-" * 40)
