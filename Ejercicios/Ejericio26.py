"""Escribir un programa que imprima todos los números 
primos hasta un número introducido por el usuario."""
#%%
#Ver si es primo
iNumMax = 45
"""
for i in range(2,iNumMax):
    for a in range(2,i):
        if i != a:
            if i%a != 0:
                print(i)
"""
#ejemplo de 1 solo valor

for i in range (2,iNumMax):
    if iNumMax % i == 0:
         