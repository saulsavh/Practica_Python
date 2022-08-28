"""Programa que solicite al usuario los datos para calcular el área de un Círculo (●), finalmente mostrar el resultado en pantalla."""

PI = 3.1416

fRadio = float(input("Ingrese el radio del circulo >> "))

#Area del circulo
fArea = PI*(fRadio**2)

print("El area del circulo es: %0.1f"%(fArea))