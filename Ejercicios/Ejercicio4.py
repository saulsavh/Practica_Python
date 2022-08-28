"""Escribir un programa que lea un entero positivo, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1. 
La suma de los primeros enteros positivos puede ser calculada de la siguiente forma: n(n+1)/2"""

iNumero = 0

iNumero = int(input("Digite un numero entero >>> "))

print(f"Su numero es {iNumero}, la suma de lo numeros dada por n(n+1)/2 es: \n")

for suma in range(0,iNumero+1):
    
    valor = (suma*(suma+1))/2
    print (f"Suma {suma} es: {valor}")

