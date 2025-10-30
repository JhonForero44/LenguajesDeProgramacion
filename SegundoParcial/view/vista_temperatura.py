# vista/vista_temperatura.py

def menu_temperatura(control):
    sistema = control.obtener_subsistema("temperatura")

    while True:
        print("\n--- CONTROL DE TEMPERATURA ---")
        print("1 -> Subir temperatura")
        print("2 -> Bajar temperatura")
        print("3 -> Mostrar temperaturas")
        print("4 -> Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            hab = int(input("Habitación: ")) - 1
            sistema.subir_temperatura(hab) 
        elif opcion == "2":
            hab = int(input("Habitación: ")) - 1
            sistema.bajar_temperatura(hab)
        elif opcion == "3":
            sistema.mostrar_estado()
        elif opcion == "4":
            break
        else:
            print("Opcion ingresada incorrecta!!!")