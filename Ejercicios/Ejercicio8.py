"""Programa que solicite al usuario los datos para llevar Grados Farenheit a Grados Celcius. celcius = (fahrenheit - 32.0) * 5.0 / 9.0"""

farenheit = float(input("Digite el valor actual de temperatura en Farenheit >> "))

#Formula °f a °c

celcius = (farenheit - 32.0)*5.0/9.0

print("La temperatura actual en celcius es %0.2f" %(celcius))


