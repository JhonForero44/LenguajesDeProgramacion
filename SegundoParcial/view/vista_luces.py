# vista/vista_luces.py

def menu_luces(control):
    sistema = control.obtener_subsistema("luces")

    while True:
        print("\n--- CONTROL DE LUCES ---")
        print("1 -> Encender luz")
        print("2 -> Apagar luz")
        print("3 -> Mostrar estado de luces")
        print("4 -> Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            hab = input("Habitación: ")
            luz = input("Nombre de la luz: ")
            sistema.encender (int(hab), int(luz))
        elif opcion == "2":
            hab = input("Habitación: ")
            luz = input("Nombre de la luz: ")
            sistema.apagar (int(hab), int(luz))
        elif opcion == "3":
            sistema.mostrar_estado()
        elif opcion == "4":
            break
        else:
            print("Opcion ingresada incorrecta!!!")