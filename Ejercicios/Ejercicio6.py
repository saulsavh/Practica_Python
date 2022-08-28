"""Programa que solicite al usuario los datos para calcular el área de un Triángulo (▲), finalmente mostrar el resultado en pantalla."""

fBase = 0.0
fAltura = 0.0

fBase = float(input("Ingrese la base del triangulo >> "))
fAltura = float(input("Ingrese la Altura del triangulo >> "))
fArea = (fBase*fAltura)/2

print (f"El area del triangulo es de {fArea}")
