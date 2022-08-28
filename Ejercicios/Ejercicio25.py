"""Escribir un programa que imprima los números pares de 
forma creciente hasta un número introducido por el usuario."""

#Formato tabla
Cadena_Vacio = ""
Caracter1 = "-"
Caracter_Vacio = " "

Mensaje_Saludo = "Hola, se imprimiran los numeros pares del 0 al 200"
iNum = int(input(""" >>> ingrese hasta que numero quiere que haga la serie
 >>> """))

#Inicio tabla
print(Cadena_Vacio.center(50,Caracter1))
print(Mensaje_Saludo.center(50,Caracter_Vacio))

#imprimir tabla de multiplicar
for i in range(0,iNum+2,2):
    print(i)

#fin de tabla
print(Cadena_Vacio.center(50,Caracter1))