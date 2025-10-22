#Patrón de Diseño: Adapter (Adaptador)
#🧠 Idea principal

#Permite que dos clases con interfaces diferentes trabajen juntas.
#El adaptador actúa como un traductor entre ambas.

#💬 Ejemplo sencillo (vida real):

#Piensa en un enchufe europeo (dos clavijas) y un tomacorriente americano (tres orificios).
#Para conectarlos, necesitas un adaptador que haga compatibles ambos sistemas.

#💻 Ejemplo en código (Python):
#Supongamos que tenemos una clase que espera usar un reproductor de audio moderno, pero solo tenemos uno antiguo.

# Clase existente (interfaz esperada)
class ReproductorModerno:
    def reproducir_mp3(self, archivo):
        print(f"Reproduciendo archivo MP3: {archivo}")

# Clase incompatible (no tiene el mismo método)
class ReproductorAntiguo:
    def reproducir_cassette(self, cinta):
        print(f"Reproduciendo cinta: {cinta}")

# Adaptador: traduce la interfaz del antiguo al moderno
class AdaptadorCassetteA_MP3(ReproductorModerno):
    def __init__(self, reproductor_antiguo):
        self.reproductor_antiguo = reproductor_antiguo

    def reproducir_mp3(self, archivo):
        # convierte la llamada moderna en una acción antigua
        cinta = archivo.replace(".mp3", ".cassette")
        self.reproductor_antiguo.reproducir_cassette(cinta)

# Uso del adaptador
cassette = ReproductorAntiguo()
adaptador = AdaptadorCassetteA_MP3(cassette)

adaptador.reproducir_mp3("musica.mp3")
