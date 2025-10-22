#👉 “No obligues a una clase a implementar métodos que no usa.”
#🧠 Idea:
#Mejor tener interfaces pequeñas que una gigante con métodos inútiles.

#❌ Mal ejemplo:
class Trabajador:
    def trabajar(self): pass
    def comer(self): pass


#Si un robot implementa esta interfaz, no tiene sentido que “coma”.

#✅ Buen ejemplo:
class Trabajable:
    def trabajar(self): pass

class Comible:
    def comer(self): pass

class Humano(Trabajable, Comible):
    def trabajar(self): print("Trabajando...")
    def comer(self): print("Comiendo...")

class Robot(Trabajable):
    def trabajar(self): print("Trabajando sin comer...")