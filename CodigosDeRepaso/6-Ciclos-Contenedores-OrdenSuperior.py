#TALLER - CICLOS, CONTENEDORES, FUNCIONES DE ORDEN SUPERIOR
# 1.Escribir una función que reciba como parámetro una cadena de palabras separadas por espacios y devuelva, 
# como resultado, cuántas palabras de más de cinco letras tiene la cadena dada.
"""
def palabras(cadena):
      lista = []
      
      trozos_cadena = cadena.split()
      
      for i in trozos_cadena:
        lista.append(i)
      
      palabrasMayor5 = []
      
      for elemento in lista:
          if len(elemento) >= 5:
              palabrasMayor5.append(elemento)
      
      if palabrasMayor5 == [] :
          resultado = ("En la oracion no hay ninguna palabra con mas de cinco letras")
      else:
          resultado = (f"Las palabras con mas de cinco letras son: {palabrasMayor5}")

      return resultado 
  
print(palabras("Hola Soy Jhon Arley Forero Velasco"))
"""
# 2.Procesamiento de telegramas. Un oficial de correos decide optimizar el trabajo de su oficina cortando todas las palabras de más de 
# cinco letras a sólo cinco letras (e indicando que una palabra fue cortada con el agregado de una arroba).
# Además elimina todos los espacios en blanco de más.

#.Por ejemplo, el texto " Llego mañana alrededor del mediodía " se transcribe como "Llego mañan@ alred@ del medio@".
"""

def telegrama(oracion):
    oracionTranscrita = ""
    palabras = oracion.split()
    for i in palabras:
        if len(i) > 5:
            oracionTranscrita += i[:-1]
            oracionTranscrita += "@"
            oracionTranscrita += " "
            pass
        else:
            oracionTranscrita += i
            oracionTranscrita += " "
    return oracionTranscrita


oracion = "Llego mañana alrededor del mediodía"
print(telegrama(oracion))

"""
# 3.Escribir una función que indique si dos fichas de dominó encajan o no. 
# Las fichas son recibidas en dos tuplas, por ejemplo: (3,4) y (5,4).

#miTupla = 
"""
def domino(tupla1,tupla2):
    for numero in tupla1:
        if numero == tupla2[0] or numero == tupla2[1]:
            print(f"La ficha {numero} encajan con {tupla2}.")
        else:
            print(f"La ficha {numero} no encajan con {tupla2}.")
    pass
tupla1=(3,4)
tupla2=(5,4)
print(domino(tupla1,tupla2))
"""
# 4.Escribir una función que indique si dos fichas de dominó encajan o no. 
# Las fichas son recibidas en una cadena, por ejemplo: 3-4 2-5. Nota: utilizar la función split de las cadenas.
"""
def separar(cadena1, cadena2):
    numero1Cadena = cadena1.split("-")
    numero2Cadena = cadena2.split("-")
    return domino(numero1Cadena,numero2Cadena)
cadena1=("5-4")
cadena2=("2-5")
(separar(cadena1,cadena2))
"""
# 5.Escribir una función que reciba una tupla con nombres, y para cada nombre imprima el mensaje Estimado , vote por mí.
"""
def nombre(tuple):
    for nombre in tuple:
        print(f"Estimado {nombre}, vote por mi.")
    pass
nombre1 = ("Jhon","Arley","Forero","Velasco")
(nombre(nombre1))
"""

# 6.Escribir una función que reciba una tupla con nombres, una posición de origen p y una cantidad n, 
# e imprima el mensaje anterior para los n nombres que se encuentran a partir de la posición p.
"""
def funcion(variable):
    p = variable[-2]
    n = variable[-1]
    for elemento in variable:
        if p == elemento or n == elemento:
            pass
        else:
            nombre = variable[p:n]
            for nombre1 in nombre:            
                print(f"Estimado {nombre1}, vote por mi.")
            break
    pass

variable = ("Jhon","Arley","Forero","Velasco",2,4)
funcion(variable)
"""

# 7.Modificar las funciones anteriores para que tengan en cuenta el género del destinatario, 
# para ello, deberán recibir una tupla de tuplas, conteniendo el nombre y el género.
"""
def funcion(nombres):
    p = nombres[-2]
    n = nombres[-1]
    solucion = ""
    
    for elemento in nombres:
        if p == elemento or n == elemento:
            pass
        else:
            unionTuplas = list(zip(nombres[0],nombres[1])) 
            nombre = unionTuplas[p:n]
            for nombre1 in nombre:
                solucion += (f"Estimado {nombre1[0]}, de sexo {nombre1[1]}, vote por mi.\n")
            break
    return solucion

nombres = (
    ("Jhon","Arley","Forero","Velasco"),
    ("Masculino","Masculino","Masculino","Femenino"),2,4
    )
print(funcion(nombres))
"""

# 8.Dada una lista de números enteros, escribir una función que devuelva una lista con todos los que sean primos.
"""
def numeroPrimo(lista:list):
    nueva_lista = []
    for elemento in range(lista):
        if  % elemento == 0:
            
numeroPrimo(25)

numero = int(input("Ingrese un valor: "))    
esPrimo = True
for i in range (2,numero):
    if numero%i==0:
        esPrimo=False
        break
if esPrimo:
    print("Es numero primo.")
else:
    print("No es un numero primo.")    
"""

# 9.Dada una lista de números enteros, escribir una función que devuelva una lista con el factorial de cada uno de esos números.
"""
def factorial(lista_numero):
    producto = 1
    for elemento in int((1,lista_numero+1)):
        producto = producto * int(elemento)
    return producto 


print(factorial([25, 50, 13, 2]))
"""