#Ejercicio 1: Asignación de funciones
#Define una función saludar(nombre) que retorne "Hola, {nombre}".
def saludar(nombre):
    return print(f"Hola, {nombre}")

#Asigna esa función a otra variable llamada f.
f = saludar
#Usa f para saludar a 3 nombres diferentes.
f("Juan")
f("Pedro")
f("Mordelon")

#Ejercicio 2: Función como argumento
#Crea una función aplicar_funcion(funcion, lista) que reciba una función y una lista.
def aplicar_funcion(funcion, lista):
    listaResultados = []
    for i in lista:
        nuevo = funcion(i)
        listaResultados.append(nuevo)
    return listaResultados

#Haz que la función aplique la operación recibida a todos los elementos de la lista.
#Prueba con:
#lambda x: x**2 sobre [1,2,3,4,5].
#lambda x: x+10 sobre [10,20,30].
print(aplicar_funcion(lambda x: x**2, [1,2,3,4,5]))
print(aplicar_funcion(lambda x: x+10, [10,20,30]))

#Ejercicio 3: Función que retorna funciones
#Crea una función multiplicador(n) que devuelva otra función que multiplica cualquier número por n.
def multiplicador(n):
    def funcion_interna(x):
        return x * n
    return funcion_interna

#Usa doble = multiplicador(2) y triple = multiplicador(3).
doble = multiplicador(2)
triple = multiplicador(3)

#Verifica:
#doble(5) debe dar 10.
#triple(7) debe dar 21.
print(doble(5))   
print(triple(7))  
