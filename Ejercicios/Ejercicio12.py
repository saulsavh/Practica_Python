"""
Escribir un Programa que solicite al usuario la edad de 2 personas, y diga cuál es mayor. Ejemplo:

- La Primera persona es mayor!

Si la edad de ambos es igual se muestra el siguiente mensaje:

- Ambos tienen la misma edad!
"""

#Variables
Edad1 = 0
Edad2 = 0
Nombre1 = ""
Nombre2 = ""

#formato tabla
Caracter1 = "-"
Caracter_Vacio = " "
Cadena_Vacio = ""
Mensaje_Saludo = "Hola, veremos quien de los dos es mas viejo"
Mensaje_Nombre = "Ingrese el %s Nombre >>>"
Posicion1 = "Primer"
Posicion2 = "Segundo"
Mensaje_Resultado = "Parece que %s es mayor que %s"
Mensaje_Igual = "Ambos tienen la misma edad"

#Inicio Tabla
print(Cadena_Vacio.center(50,Caracter1))
print(Mensaje_Saludo.center(50,Caracter_Vacio))
print(Cadena_Vacio.center(50,Caracter1))

#Captura de Nombres y Edades
print(Mensaje_Nombre.center(50,Caracter_Vacio)%(Posicion1))
Nombre1 = input(" >>> ")
print("Deme su edad".center(50,Caracter_Vacio))
Edad1 = int(input(" >>> "))
print(Cadena_Vacio.center(50,Caracter1))
print(Mensaje_Nombre.center(50,Caracter_Vacio)%(Posicion2))
Nombre2 = input(" >>> ")
print("Deme su edad".center(50,Caracter_Vacio))
Edad2 = int(input(" >>> "))
print(Cadena_Vacio.center(50,Caracter1))

#resultado condiciones
if Edad1 == Edad2 :
    print(Mensaje_Igual.center(50, Caracter_Vacio))
elif Edad1 > Edad2 : 
    print(Mensaje_Resultado.center(50,Caracter_Vacio)%(Nombre1, Nombre2))
else :
    print(Mensaje_Resultado.center(50,Caracter_Vacio)%(Nombre2, Nombre1))
print(Cadena_Vacio.center(50,Caracter1))