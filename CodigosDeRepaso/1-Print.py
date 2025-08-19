texto = "Hola Mundo"
print(texto)

#Metodos, funcion incluida dentro de un objeto
print(texto.upper()) #Texto todo en mayuscula
print(texto.lower()) #Texto todo en minuscula
print(texto.find("Mundo")) #Donde esta Mundo, -1 si no encuentra nada
print(texto.replace("Mundo", "Paisano")) #Cambiar cadena de texto por otra
nuevoTexto = texto.replace("Mundo", "Paisano")
print(nuevoTexto)
print("Mundo" in texto) #Buscar si la palabra esta o no     

#Ejemplos Con Operaciones:
z, y = 9, 8
suma = z + y	
print("La suma es: " + str(suma))  # Convertir a cadena para concatenar
print(f"El modulo es : {suma}")