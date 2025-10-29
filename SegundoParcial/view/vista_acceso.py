# vista/vista_acceso.py

def menu_acceso(control):
    sistema = control.obtener_subsistema("acceso")

    while True:
        print("\n=== CONTROL DE ACCESO ===")
        print("1. Agregar usuario")
        print("2. Verificar acceso")
        print("3. Mostrar usuarios")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del usuario: ")
            codigo = input("Código de acceso: ")
            sistema.agregar_usuario(nombre, int(codigo))
        elif opcion == "2":
            codigo = input("Ingrese el código: ")
            sistema.verificar_acceso(int(codigo))
        elif opcion == "3":
            sistema.mostrar_estado()
        elif opcion == "0":
            break
        else:
            print("Opcion ingresada incorrecta!!!")