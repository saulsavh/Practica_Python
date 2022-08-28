"""Escribir un programa en el cual Dados 5 números enteros solicitados al usuario, determinar cuál de los 4 números enteros es más cercano al primero."""
#%%
#Variables
iNumComprar = 0
iNum1 = 0
iNum2 = 0
iNum3 = 0
iNum4 = 0
fRest1 = 0.0
fRest2 = 0.0
fRest3 = 0.0
fRest4 = 0.0
lNum3 =[]
#Formato tabla
Cadena_Vacio = ""
Caracter1 = "-"
Caracter_Vacio = " "

Mensaje_Saludo = "Ingrese 5 numero y te dire cual es el mar cercano al primero"
Mensaje_Primero = "Digite el numero a Comparar"
Mensaje_Segundo = "Digite el primer numero a comparar"
Mensaje_Tecero = "Digite el Segundo numero a comparar"
Mensaje_Cuarto = "Digite el Tercero numero a comparar"
Mensaje_Quinto = "Digite el Cuarto numero a comparar"
#%%
#Inicio tabla
print(Cadena_Vacio.center(50,Caracter1))
print(Mensaje_Saludo.center (50, Caracter_Vacio))
#Recolectar numeros
print(Mensaje_Primero.center(50,Caracter_Vacio))
iNumComprar = int(input(" >>> "))

print(Mensaje_Segundo.center(50,Caracter_Vacio))
iNum1 = int(input(" >>> "))

print(Mensaje_Tecero.center(50,Caracter_Vacio))
iNum2 = int(input(" >>> "))

print(Mensaje_Cuarto.center(50,Caracter_Vacio))
iNum3 = int(input(" >>> "))

print(Mensaje_Quinto.center(50,Caracter_Vacio))
iNum4 = int(input(" >>> "))

#%%
#Calculos
lNum1 = [iNum1, iNum2, iNum3, iNum4]
lNum2 = [abs(iNum1-iNumComprar), abs(iNum2-iNumComprar), abs(iNum3-iNumComprar), abs(iNum4-iNumComprar)]
lNum3 = [abs(iNum1-iNumComprar), abs(iNum2-iNumComprar), abs(iNum3-iNumComprar), abs(iNum4-iNumComprar)]
lNum3.sort()
print(lNum1)
print(lNum2)
print(lNum3)

res = lNum2.index(lNum3[0])
print("El numero mas cercano a %s es %s"%(iNumComprar, lNum1[res]))
print(Cadena_Vacio.center(50,Caracter1))
# %%
