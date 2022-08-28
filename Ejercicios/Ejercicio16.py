"""Escribir un programa que solicite al usuario 3 números, compararlos y decir cual es mayor."""
#%%
#Formato tabla 
Cadena_Vacio = ""
Caracter1 = "-"
Caracter_Vacio = " "
iNum = []

Mensaje_Saludo = "Hola, ingresa 3 numeros"
Mensaje_Primero = "Ingresa el primer numero"
Mensaje_segundo = "Ingresa el segundo numero"
Mensaje_tercero = "Ingresa el tercer numero"
#%%
#inicio tabla
print(Cadena_Vacio.center(50,Caracter1))
print(Mensaje_Saludo.center(50,Caracter_Vacio))
print(Mensaje_Primero.center(50,Caracter_Vacio))
#iNum1 = int(input(" >>> "))
iNum.append(int(input(" >>> ")))
print(Mensaje_segundo.center(50,Caracter_Vacio))
#iNum2 = int(input(" >>> "))
iNum.append(int(input(" >>> ")))
print(Mensaje_tercero.center(50,Caracter_Vacio))
#iNum3 = int(input(" >>> "))
iNum.append(int(input(" >>> ")))
print(Cadena_Vacio.center(50,Caracter1))
print(iNum)
#ordenar lista
print(iNum.sort())
print("Tu el numero mayor es %s"%(iNum[2]))


# %%
