# 👉 “Una clase debe tener una sola razón para cambiar.”
#🧠 Idea:
#Cada clase debe hacer una sola cosa, no muchas.

#Mal ejemplo
class Reporte:
    def generar(self):
        print("Generando reporte...")

    def guardar_en_bd(self):
        print("Guardando en la base de datos...")

#Buen ejemplo
class GeneradorReporte:
    def generar(self):
        print("Generando reporte...")

class GuardadorReporte:
    def guardar_en_bd(self):
        print("Guardando en la base de datos...")
