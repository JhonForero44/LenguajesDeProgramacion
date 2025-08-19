lenguajes = ["Python", "Ruby", "PHP", "JavaScript", "Java"]
print(lenguajes)
print(lenguajes[1])
lenguajes[1] = "Go" #Cambiar Ruby por Go
print(lenguajes)
print(lenguajes[-1])#Ultimo elemento
print(lenguajes[-2])#Penultimo elemento
print(lenguajes[1:3])#Seleccionar rango de elementos
print(lenguajes[:3])
print(lenguajes[1:])

#Metodos de listas
lenguajes = ["Python", "Ruby", "PHP", "JavaScript", "Java"]
lenguajes.insert(3, "Go") #Insertar elemento en la lista
lenguajes.insert(3, "C")#Insertar elemento al comienzo
print(lenguajes)
lenguajes.remove("Ruby") #Eliminar elemento
print(lenguajes)
print("PHP" in lenguajes)#Preguntar si esta en la lista
print(len(lenguajes)) #Cantidad de datos dentro de la lista
lenguajes.clear()#Limpiar lista
