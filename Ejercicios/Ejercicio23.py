"""Escribir un programa que imprima los números pares entre 0 y 200 de forma creciente."""

#Formato tabla
Cadena_Vacio = ""
Caracter1 = "-"
Caracter_Vacio = " "

Mensaje_Saludo = "Hola, se imprimiran los numeros pares del 0 al 200"

#Inicio tabla
print(Cadena_Vacio.center(50,Caracter1))
print(Mensaje_Saludo.center(50,Caracter_Vacio))

#imprimir tabla de multiplicar
for i in range(0,202,2):
    print(i)

#fin de tabla
print(Cadena_Vacio.center(50,Caracter1))