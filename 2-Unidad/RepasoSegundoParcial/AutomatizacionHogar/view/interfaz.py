from core.controlador import ControladorHogar

def menu():
    sistema = ControladorHogar()

    while True:
        print("\n=== 🌐 SISTEMA DE AUTOMATIZACIÓN DEL HOGAR ===")
        print("1. Agregar nuevo agente")
        print("2. Listar agentes")
        print("3. Operar todos los agentes")
        print("4. Cargar todas las baterías")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("Ingrese el tipo de agente (luz, temperatura, residuos, agua): ")
            nombre = input("Ingrese el nombre del agente: ")
            try:
                sistema.agregar_agente(tipo, nombre)
            except ValueError as e:
                print(e)
        elif opcion == "2":
            sistema.listar_agentes()
        elif opcion == "3":
            sistema.operar_agentes()
        elif opcion == "4":
            sistema.cargar_todos()
        elif opcion == "5":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida, intente de nuevo.")
