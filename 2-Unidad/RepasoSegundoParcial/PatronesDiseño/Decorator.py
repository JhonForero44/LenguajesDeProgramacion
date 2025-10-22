#Decorator (Decorador)
#🧠 Idea:

#Permite añadir funcionalidades extra a un objeto sin modificar su estructura original.

# Clase base
class Cafe:
    def costo(self):
        return 5

# Decorador base
class DecoradorCafe:
    def __init__(self, cafe):
        self._cafe = cafe
    def costo(self):
        return self._cafe.costo()

# Decoradores concretos
class Leche(DecoradorCafe):
    def costo(self):
        return self._cafe.costo() + 2

class Chocolate(DecoradorCafe):
    def costo(self):
        return self._cafe.costo() + 3

# Uso
cafe = Cafe()
cafe_con_leche = Leche(cafe)
cafe_choco_leche = Chocolate(cafe_con_leche)

print(f"Costo total: {cafe_choco_leche.costo()} USD")
