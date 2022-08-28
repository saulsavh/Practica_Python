"""Escribir un programa que pregunte el nombre y apellido del usuario. Luego de ser introducidos los datos muestre por pantalla la cadena ¡Hola {nombre} {apellido},
 gusto en conocerte!, donde: {nombre} y {apellido} son los valores introducidos."""

nombre = ""
apellido = ""

nombre = input("Ingresa tu nombre  ")
apellido = input("Ingresa tu apellido ")

# Metodo operador de Formato %
print("Hola!, %s %s"%(nombre, apellido))

#Metodo .format
print("Hola!, {0} {1}" .format(nombre, apellido))

# Metodo f-string
print(f"Hola!, {nombre} {apellido}")
