class VerificacionBateria:


    def __init__(self, subsistema):
        self._subsistema = subsistema

    def __getattr__(self, nombre):
        return getattr(self._subsistema, nombre)

    def ejecutar_accion(self, funcion, *args, **kwargs):

        if not self._subsistema.verificar_baterias():
            self._subsistema.alarma.activar("Nivel de batería bajo en " + self._subsistema.nombre)
            print("Acción no ejecutada por batería baja.")
            return
        funcion(*args, **kwargs)
