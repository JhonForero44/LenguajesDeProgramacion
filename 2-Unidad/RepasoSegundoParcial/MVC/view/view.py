class UsuarioVista:
    def mostrar_usuarios(self, usuarios):
        print("👥 Lista de usuarios:")
        for u in usuarios:
            print(f"- {u}")

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
