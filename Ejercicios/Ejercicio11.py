"""
Escribir un programa que solicite al usuario un número entero y muestre en pantalla si el número es Positivo (+) o Negativo (-). 
En caso de que el número sea igual a cero (0) se debe mostrar en pantalla: El número no es Positivo ni Negativo.
"""

#Formato tabla
Caracter1 = "-"
Caracter_Vacio = " "
Cadena_Vacio = ""
Mensaje_Saludo = "Hola, ingrese un numero entero"
Mensaje_Numero = " >>> Tu numero es %s"
Mensaje_Positivo = " >>> Tu numero es Positivo"
Mesaje_Negativo = " >>> Tu numero es negativo"
Mensaje_Zero = " >>> El numero no es Positivo ni Negativo"

#inicio tabla
print(Cadena_Vacio.center(50, Caracter1))
print(Mensaje_Saludo.center(50, Caracter_Vacio))
iNumero = int(input(" >>> "))
print(Cadena_Vacio.center(50, Caracter1))
print(Mensaje_Numero%(iNumero))

#Condicional Positivo negativo
if iNumero > 0:
    print(Mensaje_Positivo)

elif iNumero < 0:
    print (Mesaje_Negativo)
else:
    print(Mensaje_Zero)

#fin de tabla
print(Cadena_Vacio.center(50,Caracter1))
