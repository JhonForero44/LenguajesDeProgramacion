#Ejercicio: Usar el patron singlenton para simular el manejo de sesion de usuario de una plataforma de SW
# con la funcionalidad de autenticacion (simulado) con usuario y contraseña y (logout).

class sesion_singlento():
    
    #Atributo de clases que almacena la instancia unica
    _instance = None
    
    #Mensaje de error si se intenta crear una instancia directamente
    def __init__(self):
        raise RuntimeError("use create_instance() method instead")
    
    @classmethod
    def create_instance(cls):
        #si no existe la instancia, se crea
        if cls._instance is None:
            #El metodo new tambien crea una instancia 
            cls._instance = cls.__new__(cls)
        #retorna la instancia
        return cls._instance
    
    def login(this, usuario: str, contrasena: str):
        if contrasena == "password123":
            this.usuario_actual = usuario
            return f"Usuario {usuario} ha iniciado sesion correctamente"
        else:
            return "Error de autenticacion"
    
    def logout(this):
        usuario = this.usuario_actual
        this.usuario_actual = None
        return f"Usuario {usuario} ha cerrado sesion correctamente"

#Creamos dos objetos
sesion1 = sesion_singlento.create_instance()
sesion2 = sesion_singlento.create_instance()
print("---"*20)
#Comparamos si son el mismo objeto
print(f"Son el mismo objeto?: {sesion1 is sesion2}")
print("---"*20)

#Iniciamos sesion con el primer objeto
print(sesion1.login("Jhon", "password123"))
#Intentamos iniciar sesion con el segundo objeto
print(sesion2.login("Arley", "password123"))
#Cerramos sesion con el primer objeto
print(sesion1.logout())
#Intentamos cerrar sesion con el segundo objeto
print(sesion2.logout())
print("---"*20)