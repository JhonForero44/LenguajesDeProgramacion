from model.model import UsuarioModelo
from view.view import UsuarioVista
from controller.controller import UsuarioControlador

# Crear las partes del MVC
modelo = UsuarioModelo()
vista = UsuarioVista()
controlador = UsuarioControlador(modelo, vista)

# Simular acciones del usuario
controlador.agregar_usuario("Ana")
controlador.agregar_usuario("Carlos")
controlador.mostrar_todos()
