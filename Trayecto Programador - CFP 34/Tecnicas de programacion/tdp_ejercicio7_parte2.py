"""

Ejercicio 5.7.3. Manejo de contraseñas

************ PARTE d) ************

d) Modificar el programa anterior para que sea una función que devuelva si el usuario
ingresó o no la contraseña correctamente, mediante un valor booleano (True o False).

"""
#importamos la clase time
import time

#definimos la funcion que nos devuelva si ingreso o no
def validar_password(respuesta):

    #Definimos la contraseña del sistema
    contra = "rataalada"

    #preguntamos si el argumento de la funcion es igual a la contraseña
    if respuesta == contra:
        #coincide
        return True

    else:
        #no coincide
        return False

#definimos cantidad de intentos
intentos = 3

#definimos el delay de la respuesta
delay = 2

#bandera de salida
entrada_sistema = False

#variable de ciclo
salida = False

#Creamos el ciclo while con la condicion a cumplir
while not salida:

    #Le mostramos al usuario la cantidad de intentos que tiene disponible
    print("Dispones de " + str(intentos) + " intentos")

    #Pedimos al usuario que ingrese la contraseña para ingresar al sistema
    passw = input("Ingrese la contraseña: ")

    print("Cargando...")

    #Se ejecuta la pausa propuesta en el ejercicio
    time.sleep(delay)

    #evaluamos la validacion del password
    if validar_password(passw):

        #el password es correcto
        entrada_sistema = True

        print("Haz entrado satisfactoriamente al sistema en:", intentos, "intentos")

        #salimos con exito del ciclo
        salida = True

    else:

        #Si la contraseña no es la indicada se procedera a restar un intento
        intentos -= 1

        #A pedido del ejercicio incrementamos el delay de la funcion sleep en cada vuelta del ciclo
        delay += 1

        print("Contraseña incorrecta")

        if intentos == 0:
            salida = True


#Si hemos adivinado entraremos al sistema: de lo contrario con entrada como False seremos bloqueados por el sistema
if entrada_sistema:
#print("Haz entrado satisfactoriamente al sistema en:", intentos, "intentos")
    print("Sigue el ciclo y el programa con normalidad")
else:
    print("Ha sido bloqueado del sistema")