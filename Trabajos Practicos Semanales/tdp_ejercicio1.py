"""
Ejercicio 1:
Considerando el problema del rectangulo calcular la hipotenusa del triangulo rectangulo
"""
import math

#Solicitamos datos de entrada
b = int(input("Ingrese el valor de la base: "))
h = int(input("Ingrese el valor de la altura: "))

#Proceso -> operacion

hipotenusa = math.sqrt((math.pow(b, 2)) + (math.pow(h, 2)))

#Salida: mostramos al usuario los datos por pantalla

print("La hipotenusa del triangulo rectangulo es:", hipotenusa)

