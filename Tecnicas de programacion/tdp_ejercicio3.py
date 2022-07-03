"""
Ejercicio 4.6.5. Escribir funciones que resuelvan los siguientes problemas:
a) Dado un año indicar si es bisiesto.
Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100,
"""

anio = int(input("Ingrese el año: "))

if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
    print("El año", anio, "es bisiesto")
else:
    print("No es bisiesto")




