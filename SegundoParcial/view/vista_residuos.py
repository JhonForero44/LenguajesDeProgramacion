# vista/vista_residuos.py

def menu_residuos(control):
    sistema = control.obtener_subsistema("residuos")

    while True:
        print("\n=== GESTIÓN DE RESIDUOS ===")
        print("1. Agregar residuo")
        print("2. Evacuar residuos")
        print("3. Mostrar estado de residuos")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("Tipo de residuo: ")
            cantidad = int(input("Cantidad (kg): "))
            sistema.ejecutar("agregar", tipo, cantidad)
        elif opcion == "2":
            sistema.ejecutar("evacuar")
        elif opcion == "3":
            sistema.sistema.mostrar_estado()
        elif opcion == "0":
            break
        else:
            print("Opcion ingresada incorrecta!!!")