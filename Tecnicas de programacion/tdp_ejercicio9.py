"""
a) Crear una funcion que nos devuelva un numero aleatorio
b) Crear una funcion que nos devuelva TRUE si el numero es par o FALSE si es impar
c) Crear una funcion que nos devuelva la tabla de multiplicar
d) TAREA: AGREGAR UNA FUNCION EXTRA QUE REALICE ALGUNA OPERACION CON UN NUMERO, ES A ELECCION
"""

import random

#Creamos la primer funcion para regresar al usuario un numero al azar
def obtener_numero_aleatorio(limite):
    #usamos la funcion radint de la clase random que parte desde 0 hasta el limite que el usuario quiera
    return random.randint(0, limite)

#Creamos la segunda funcion que nos devuelve True si el numero es par o False si es impar
def es_par(numero):

    return numero % 2 == 0

#Creamos la tercer funcion que nos devuelve una lista con la tabla de multiplicar de cualquier numero
def tabla_de_multiplicar(valor):

    #creamos una lista para almacenar las tablas
    tabla_numeros = []

    #preguntamos al usuario el limite de la tabla
    limite = int(input("Hasta que numero deseas saber la tabla???: "))

    #usamos un ciclo for para generar las tablas de multiplicar del valor en el rango que el usuario quiera
    for i in range(0, limite + 1):
        tabla = str(valor) + " x " + str(i) + " = " + str(valor * i)
        tabla_numeros.append(tabla)

    #retornamos la lista con las tablas
    return tabla_numeros

#Creamos la cuarta funcion que nos devuelve un numero y su pasaje a hexadecimal, binario y octal
def conversion_sistemas_digitales(numero):

    #Creamos un menu para las opciones

    salir = False

    while not salir:
        print("MENU CONVERSION NUMERICA: ")
        print("1 - Conversion a sistema Hexadecimal")
        print("2 - Conversion a sistema Octal")
        print("3 - Conversion a sistema Binario")
        print("4 - Salir")
        # Pedimos al usuario que ingrese una opcion
        eleccion = int(input("Elija su opcion: "))
        #Segun su eleccion el usuario podra elegir el numero en el sistema que desee
        if eleccion == 1:
            #usamos la funcion hex para devolver el valor en hexadecimal
            return hex(numero)
        elif eleccion == 2:
            #usamos la funcion oct para devolver el valor en octal
            return oct(numero)
        elif eleccion == 3:
            #usamos la funcion bin para devolver el valor en bin
            return bin(numero)
        elif eleccion == 4:
            salir = True
            return "Gracias por operar"
        else:
            print("Opcion no valida intentelo de nuevo")


#creamos una funcion para salir
def salir(numero):
    return "Gracias por jugar"


#creamos una variable opcion para manejar el menu principal
opcion = 0

#Creamos un menu principal
while opcion != 5:
    
    print("MENU PRINCIPAL:")
    print("1 - Obtener numero al azar")
    print("2 - Saber si el numero es par")
    print("3 - Ver la tabla de multiplicar de un numero")
    print("4 - Conversion de numeros")
    print("5 - Salir")

    #Diccionario de funciones
    menu = {1: obtener_numero_aleatorio, 2: es_par, 3: tabla_de_multiplicar, 4: conversion_sistemas_digitales, 5: salir}

    #Pedimos al usuario que ingrese una opcion
    opcion = int(input("Ingrese una opcion: "))

    #con este simple if evitamos que nos aparezca el input en la opcion 5
    if opcion < 5:
        n = int(input("Ingrese un valor para operar: "))
    else:
        n = 5

    #mostramos la opcion elegida por el usuario
    print(menu[opcion](n))

