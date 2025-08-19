#Cuerpo de una funcion:
#def function_name():
#    cuerpo de la función

def hello(name):    # definiendo una función
    print("Hello,", name)    # cuerpo de la función
name = input("Ingresa tu nombre: ")
hello(name)    # invocación de la función

#1  ->  Un año bisiesto: escribiendo tus propias funciones 
"""
def is_year_leap(year):
    if year % 4 != 0:
        return False # no es divisible por 4
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")
"""

#Ejemplo triangulo y teorema de pitagoras
"""
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

a = float(input('Ingresa la longitud del primer lado: '))
b = float(input('Ingresa la longitud del segundo lado: '))
c = float(input('Ingresa la longitud del tercer lado: '))

if is_a_triangle(a, b, c):
    print('Si, si puede ser un triángulo.')
else:
    print('No, no puede ser un triángulo.')
"""