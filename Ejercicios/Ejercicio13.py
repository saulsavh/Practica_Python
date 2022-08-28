"""Introducir un número por teclado y que se muestre un mensaje indicando si es par o impar."""

#Variables
iNum1 = 0
fRes = 0

#formato tabla
Caracter1 = "-"
Caracter_Vacio = " "
Cadena_Vacio = ""
Mensaje_Saludo = "Hola, veremos si tu numero es par o impar"
Mensaje_Numero = "Ingrese su Numero >>>"
Mensaje_Par = "Su numero es Par"
Mensaje_Impar = "Su numero es Impar"

#Inicio de tabla
print(Cadena_Vacio.center(50,Caracter1))
print(Mensaje_Saludo.center(50,Caracter_Vacio))
print(Mensaje_Numero)
iNum1 = int(input(" >>> "))
print(Cadena_Vacio.center(50,Caracter1))

#Calculo
fRes = iNum1%2

#Condicion resultado


if fRes != 0: print(Mensaje_Impar.center(50,Caracter_Vacio))
else : print(Mensaje_Par.center(50, Caracter_Vacio))
#Fin tabla
print(Cadena_Vacio.center(50,Caracter1))