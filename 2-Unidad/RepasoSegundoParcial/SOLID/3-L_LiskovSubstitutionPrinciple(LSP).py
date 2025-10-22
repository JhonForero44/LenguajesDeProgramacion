#👉 “Las subclases deben poder reemplazar a su clase padre sin problemas.”
#🧠 Idea:
#Una clase hija debe comportarse como su padre, sin romper la lógica.

#❌ Mal ejemplo:
class Ave:
    def volar(self):
        print("Volando...")

class Pinguino(Ave):
    def volar(self):
        raise Exception("¡No puedo volar!")

#✅ Buen ejemplo:
class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        print("Volando...")

class Pinguino(Ave):
    def nadar(self):
        print("Nadando...")