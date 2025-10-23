from controller.controller import Controlado

def menu():
    sistema = Controlado()

    while True:
        print("AGENTE DE AUTOMATIZACION")
        print("Menu:")
        print("1 -> Agregar Agente")
        print("2 -> Listar Agente")
        print("3 -> Usar Agentes")
        print("4 -> Cargar Agentes")
        print("5 -> Salir")
        opcion = input("Ingresa una opcion: ")

        if opcion == "1":
            nombre = input ("Ingresa el nombre del agente: ")
            tipo = input ("Ingresa el tipo de agente (luz, residuos, temperatura): ")
            try:
                sistema.agregarAgente(nombre, tipo)
            except ValueError as e:
                print(e)            
        elif opcion == "2":
            sistema.listarAgente()
        elif opcion == "3":
            sistema.operarAgente()
        elif opcion == "4":
            sistema.cargarAgente()
        elif opcion == "5":
            print("Saliendo del sistema")
            break
        else:
            print("Ingresa una opcion valida!!!")