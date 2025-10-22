class UsuarioModelo:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, nombre):
        self.usuarios.append(nombre)

    def obtener_usuarios(self):
        return self.usuarios
