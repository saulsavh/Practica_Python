"""Escribir un programa que imprima los números pares entre el 0 y 200 de forma decreciente."""

#Formato tabla
Cadena_Vacio = ""
Caracter1 = "-"
Caracter_Vacio = " "

Mensaje_Saludo = "Hola, se imprimiran los numeros pares del 200 al 0"

#Inicio tabla
print(Cadena_Vacio.center(50,Caracter1))
print(Mensaje_Saludo.center(50,Caracter_Vacio))

#imprimir tabla de multiplicar
for i in range(200,-2,-2):
    print(i)

#fin de tabla
print(Cadena_Vacio.center(50,Caracter1))