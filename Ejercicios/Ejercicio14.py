"""Introducir un número por teclado y que se muestre un mensaje indicando si es múltiplo de 3."""

#Variables
iNum1 = 0
fRes = 0

#formato tabla
Caracter1 = "-"
Caracter_Vacio = " "
Cadena_Vacio = ""
Mensaje_Saludo = "Hola, veremos si tu numero es Multiplo de 3"
Mensaje_Numero = "Ingrese su Numero >>>"
Mensaje_Multiplo = "Su numero es Multiplo de 3"
Mensaje_Nomultiplo = "Su numero no es Multiplo de 3"

#Inicio de tabla
print(Cadena_Vacio.center(50,Caracter1))
print(Mensaje_Saludo.center(50,Caracter_Vacio))
print(Mensaje_Numero)
iNum1 = int(input(" >>> "))
print(Cadena_Vacio.center(50,Caracter1))

#Calculo
fRes = iNum1%3

#Condicion resultado


if fRes != 0: print(Mensaje_Nomultiplo.center(50,Caracter_Vacio))
else : print(Mensaje_Multiplo.center(50, Caracter_Vacio))
#Fin tabla
print(Cadena_Vacio.center(50,Caracter1))