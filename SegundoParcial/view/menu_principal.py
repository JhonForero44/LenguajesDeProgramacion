from controller.control_maestro import ControlMaestro
from view.vista_acceso import menu_acceso
from view.vista_luces import menu_luces
from view.vista_temperatura import menu_temperatura
from view.vista_residuos import menu_residuos

def menu_principal():
    control = ControlMaestro()

    while True:
        print("\n--- SISTEMA DOMÓTICO MAESTRO ---")
        print("1 -> Control de Acceso")
        print("2 -> Control de Luces")
        print("3 -> Control de Temperatura")
        print("4 -> Gestión de Residuos")
        print("5 -> Ver estado general")
        print("6 -> Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_acceso(control)
        elif opcion == "2":
            menu_luces(control)
        elif opcion == "3":
            menu_temperatura(control)
        elif opcion == "4":
            menu_residuos(control)
        elif opcion == "5":
            control.verificar_estado_general()
        elif opcion == "6":
            print("Saliendo del sistema :)")
            break
        else:
            print("Opcion ingresada incorrecta!!!")
