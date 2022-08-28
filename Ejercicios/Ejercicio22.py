"""Escribir un programa en el cual se solicite al usuario un número y 
se imprima la tabla de potencias del 1 al 10 del valor introducido."""

#Formato tabla
Cadena_Vacio = ""
Caracter1 = "-"
Caracter_Vacio = " "

Mensaje_Saludo = "Hola ingresa un numero para Elevarlo"

#Inicio tabla
print(Cadena_Vacio.center(50,Caracter1))
print(Mensaje_Saludo.center(50,Caracter_Vacio))
iNum = int(input(" >>> "))
print(Cadena_Vacio.center(50,Caracter1))

#imprimir tabla de multiplicar
for i in range(0,11):
    print("%s elevado a %s = %s"%(iNum, i, iNum**i))

#fin de tabla
print(Cadena_Vacio.center(50,Caracter1))