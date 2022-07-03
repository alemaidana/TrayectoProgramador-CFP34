"""
Ejercicio 5.7.3. Manejo de contraseñas

a) Escribir un programa que contenga una contraseña inventada, que le pregunte al usua-
rio la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.

b) Modificar el programa anterior para que solamente permita una cantidad fija de inten-
tos.

c) Modificar el programa anterior para que después de cada intento agregue una pausa
cada vez mayor, utilizando la función sleep del módulo time.

d) Modificar el programa anterior para que sea una función que devuelva si el usuario
ingresó o no la contraseña correctamente, mediante un valor booleano (True o False).

************ IMPORTANTE ************

NOTA_ALUMNO: AQUI CONTEMPLAREMOS LAS 3 PRIMERAS PARTES PARA UNA MEJOR LECTURA DE
CODIGO LA PARTE D SERA HECHA EN OTRO ARCHIVO
"""

#importamos la clase time para usar sus funciones
import time

#Declaramos la variable Contraseña donde le pediremos al usuario que ingrese el dato
password = None

#Definimos una cantidad de intentos fijos
intentos = 3

#Definimos una cantidad de delay en segundos que tendra la respuesta del programa
delay_segundos = 2

#Definimos una variable para saber si puede entrar al sistema o es bloqueado
entrada_sistema = False

#variable de ciclo
salida = False

#Creamos el ciclo while con la condicion a cumplir
while not salida:

    #Le mostramos al usuario la cantidad de intentos que tiene disponible
    print("Dispones de " + str(intentos) + " intentos")

    #Pedimos al usuario que ingrese la contraseña para ingresar al sistema
    password = input("Ingrese la contraseña para ingresar al sistema: ").lower()

    #Imprimimos un mensaje de carga
    print("Cargando...")

    #De la clase time usamos la funcion sleep para retrasar el mensaje
    #la cantidad de segundos que la variable delay_segundos propone
    time.sleep(delay_segundos)

    if password == "rataalada":
        entrada_sistema = True
        salida = True
    else:
    #Si la contraseña no es la indicada se procedera a restar un intento
        intentos -= 1

    #A pedido del ejercicio incrementamos el delay de la funcion sleep en cada vuelta del ciclo
        delay_segundos += 2

    #Si nos quedamos sin intentos entrada sera False lo que hara que salgamos
    #del bucle y nos evalue en la condicion fuera del while
    if intentos == 0:
            entrada_sistema = False
            salida = True



#Si hemos adivinado entraremos al sistema  de lo contrario con entrada como False seremos bloqueados por el sistema
if entrada_sistema:
    print("Haz entrado satisfactoriamente al sistema en:", intentos, "intentos")
else:
    print("Ya no puedes ingresar al sistema, haz sido bloqueado")