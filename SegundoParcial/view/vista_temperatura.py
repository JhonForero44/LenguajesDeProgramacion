# vista/vista_temperatura.py

def menu_temperatura(control):
    sistema = control.obtener_subsistema("temperatura")

    while True:
        print("\n=== CONTROL DE TEMPERATURA ===")
        print("1. Subir temperatura")
        print("2. Bajar temperatura")
        print("3. Mostrar temperaturas")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            hab = input("Habitación: ")
            sistema.ejecutar_accion(sistema.subir_temperatura, int(hab))
        elif opcion == "2":
            hab = input("Habitación: ")
            sistema.ejecutar_accion(sistema.bajar_temperatura, int(hab))
        elif opcion == "3":
            sistema.mostrar_estado()
        elif opcion == "0":
            break
        else:
            print("Opcion ingresada incorrecta!!!")