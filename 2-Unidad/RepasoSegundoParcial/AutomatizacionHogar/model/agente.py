class Agente:
    def __init__(self, nombre, bateria=100):
        self._nombre = nombre
        self._bateria = bateria
        
    @property
    def nombre(self):
        return self._nombre

    @property
    def bateria(self):
        return self._bateria

    def cargar_bateria(self):
        self._bateria = 100
        print(f"🔋 {self._nombre}: batería cargada al 100%")

    def operar(self):
        """Método abstracto: cada agente define su propio comportamiento"""
        raise NotImplementedError("Este método debe implementarse en la subclase.")