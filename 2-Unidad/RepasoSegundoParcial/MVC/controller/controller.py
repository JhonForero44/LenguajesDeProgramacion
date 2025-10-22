from model.model import UsuarioModelo
from view.view import UsuarioVista

class UsuarioControlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def agregar_usuario(self, nombre):
        self.modelo.agregar_usuario(nombre)
        self.vista.mostrar_mensaje(f"✅ Usuario '{nombre}' agregado.")

    def mostrar_todos(self):
        usuarios = self.modelo.obtener_usuarios()
        self.vista.mostrar_usuarios(usuarios)
