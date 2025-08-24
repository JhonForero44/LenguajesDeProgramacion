#Recibe como parametras una operación y realiza la operación correspondiente
#Funciones Anonimas

def calculadora_1 (operacion):
    if operacion == "+":
        return lambda a, b : a + b
    elif operacion == "-":
        return lambda a, b : a - b
    elif operacion == "*":
        return lambda a, b : a * b
    elif operacion == "/":
        return lambda a, b : a / b
        
