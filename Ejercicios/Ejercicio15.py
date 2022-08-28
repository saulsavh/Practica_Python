"""Escribir un programa que solicite al usuario una letra y diga si esta es MAYÚSCULA o minúscula."""
#%%
#formato tabla
Cadena_Vacio = ""
Caracter1 = "-"
Caracter_Vacio = " "

Mensaje_Saludo = "Hola, Ingrese una letra y te dire si es Mayuscula o no"
Mensaje_Mayuscula = "%s está en Mayuscula"
Mensaje_Minuscila = "%s es Minuscula"
Mensaje_Error = """Digite un valor Valido, recuerde solo usar letras sin caracteres especiales"""
#%%
#inicio tabla
print(Cadena_Vacio.center(50, Caracter1))
print(Mensaje_Saludo.center(50,Caracter_Vacio))
Letra = ord(input(" >>> "))
print(Cadena_Vacio.center(50,Caracter1))
#%%
#Condiciones Mayusculas
if Letra > 64 and Letra < 91 :
    print(Mensaje_Mayuscula%(chr(Letra)))
elif Letra > 96 and Letra < 124 :
    print(Mensaje_Minuscila%(chr(Letra)))
else : 
    print(Mensaje_Error)

#Final de tabla
print(Cadena_Vacio.center(50,Caracter1))


# %%
