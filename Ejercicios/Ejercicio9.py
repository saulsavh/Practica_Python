"""Un radar común de detección de velocidad de la policía de caminos emite un rayo de microondas a una frecuencia f0. 
El rayo es reflejado por un automóvil que se aproxima y el rayo reflejado es captado y analizado por la unidad de radar.
 La frecuencia del rayo reflejado es cambiada ligeramente de f0 a f1 debido al movimiento del automóvil."""

#Imprimir tabla
Caracter1 = "*"
Caracter_vacio = " "
Cadena_vacia = ""

#Formato salida
FormatoSalida = "El resultado es %0.1f"

#Datos problema
f0 = 2e10
f1 = 2.0000004e10

#formula
resultado = ((6.685e8)*(f1-f0))/(f0+f1)

#Imprimir tabla y resultado
print(Cadena_vacia.center(50,Caracter1))
print("Ejercicio 9".center(50,Caracter_vacio))
print(Cadena_vacia.center(50,Caracter1))
print(FormatoSalida.center(50,Caracter_vacio)%(resultado))
print(Cadena_vacia.center(50,Caracter1))