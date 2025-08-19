vacaciones = True  
dia_descanso = False
disposicion = False

if (vacaciones and disposicion) or dia_descanso:
    print("Vayase de paseo")
else:
    print("Quede en casa")    

if not(vacaciones or dia_descanso):
    print("No salgas")
else:
    print("Ok puedes salir")
