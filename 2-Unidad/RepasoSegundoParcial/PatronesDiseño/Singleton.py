#5. Singleton (Única Instancia)
#🧠 Idea:

#Asegura que solo exista una instancia de una clase en toda la aplicación, y ofrece un punto global de acceso a ella.

class Singleton:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            print("✅ Nueva instancia creada")
        return cls._instancia

# Uso
obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)  # True
