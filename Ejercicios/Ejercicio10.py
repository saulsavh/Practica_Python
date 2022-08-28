"""
Un Freelancer desea saber cuánto puede cobrar por su trabajo semanal y mensualmente, para ello solo necesita establecer el precio de su trabajo por hora.

Se estiman 40 horas de trabajo a la semana.

Las Fórmulas para calcular el pago Semanal y Mensual son:

1) Pago_Semanal = (DolaresPorHora x 40)

2) Pago_Mensual = (DolaresPorHora x 160)
"""

#variables 
Pago_Hora = 10

Pago_Semanal = 0
Pago_Mensual = 0

#Formato de tabla

Caracter1 = "-"
Caracter_Vacio = " "
Cadena_Vacio = ""
Mensaje_Saludo = "Hola, Calcularemos cuanto ganas"
Mensaje_Phora = "Cuanto ganas por Hora?"
Mensaje_Psemanal = " >>> Pago a la semana es de %s"
Mensaje_Pmensual = " >>> Pago Mensual es de %s"

#inicio Tabla
print(Cadena_Vacio.center(60, Caracter1))
print(Mensaje_Saludo.center(60, Caracter_Vacio))
print(Mensaje_Phora.center(60,Caracter_Vacio))
Pago_Hora = float(input(" >>> "))
print(Cadena_Vacio.center(60, Caracter1))

#Calculo pagos 
Pago_Semanal = Pago_Hora * 40
Pago_Mensual = Pago_Hora * 40 * 4

#Resultados en tabla
print(Cadena_Vacio.center(60, Caracter1))
print(Mensaje_Psemanal%(Pago_Semanal))
print(Cadena_Vacio.center(60, Caracter1))
print(Mensaje_Pmensual%(Pago_Mensual))
print(Cadena_Vacio.center(60, Caracter1))