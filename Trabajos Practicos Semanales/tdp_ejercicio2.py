"""
Ejercicio 2:
Se le va a pedir al usuario el radio y se va a calcular el area de la circunferencia
"""
import math

#Solicitamos datos de entrada
radio = int(input("Ingrese el valor del radio: "))

#Proceso -> operacion

area_circulo = math.pi * (math.pow(radio, 2))

#Salida: mostramos al usuario los datos por pantalla

print("El area del circulo es:", area_circulo)


