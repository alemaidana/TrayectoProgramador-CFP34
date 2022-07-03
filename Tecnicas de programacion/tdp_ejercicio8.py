"""
Ejercicio 5.7.4. Utilizando la función randrange del módulo random, escribir un programa que
obtenga un número aleatorio secreto, y luego permita al usuario ingresar números y le indique
si son menores o mayores que el número a adivinar, hasta que el usuario ingrese el número
correcto.
"""
import random
import time

#Constantes de cada dificultad
DIFICULTAD_FACIL = 50
DIFICULTAD_MEDIA = 500
DIFICULTAD_DIFICIL = 100
#opciones para inicializar el menu
opcion = 0


#creamos una funcion para salir
def salir():
    print("Gracias por jugar. Salimos con exito del programa")

#creamos una funcion que nos devuelve un mensaje cuando ganamos o perdemos
def final_mensaje(intentos, gano):
    if intentos == 0 and not gano:
        print("\n*** TE HAZ QUEDADO SIN INTENTOS, HAZ PERDIDO INTENTALO DE NUEVO ***\n")
    else:
        print("FELICITACIONES!!\n")

#creamos una funcion para el primer nivel sin intentos, solo adivinar el numero
def nivel_facil():
    print("NIVEL FACIL:")
    print("Tienes una cantidad ilimitada de intentos y debes adivinar un numero del 0 al", DIFICULTAD_FACIL)

    #creamos el numero aleatorio correspondiente a la dificultad facil
    numero_aleatorio_facil = random.randint(0, DIFICULTAD_FACIL)

    #ver el numero (para prueba de escritorio)
    #print(numero_aleatorio_facil)

    #inicializamos numero en 0
    numero = 0

    #iniciamos el ciclo del juego modo facil
    while numero != numero_aleatorio_facil:

        # pedimos un numero al usuario
        numero = int(input("Ingrese un numero: "))

        # evaluamos las condiciones
        if numero > numero_aleatorio_facil:
            print("El numero ingresado es mayor al numero secreto")
        elif numero < numero_aleatorio_facil:
            print("El numero ingresado es menor al numero secreto")
        else:
            print("\n*****BINGO HAZ ACERTADO!!!***** \n")


#creamos una funcion para el segundo nivel con limite de intentos para adivinar el numero
def nivel_medio():
    print("NIVEL MEDIO:")
    print("Tienes una cantidad de 30 intentos y debes adivinar un numero del 0 al", DIFICULTAD_MEDIA)

    #inicializamos la varible ganar como false como parte del mensaje final
    ganar = False

    #creamos el numero aleatorio correspondiente a la dificultad media
    numero_aleatorio_medio = random.randint(0, DIFICULTAD_MEDIA)

    #inicializamos la variable intentos del nivel con 30
    intentos = 30

    #ver el numero (para prueba de escritorio)
    #print(numero_aleatorio_medio)

    #iniciamos el ciclo del juego modo medio
    while intentos != 0:

        #mostramos cantidad de intentos
        print("INTENTOS DISPONIBLES:", intentos)

        #pedimos un numero al usuario
        numero = int(input("\nIngrese un numero: "))

        #evaluamos las condiciones
        if numero > numero_aleatorio_medio:
            print("El numero ingresado es mayor al numero secreto")
            intentos -= 1
        elif numero < numero_aleatorio_medio:
            print("El numero ingresado es menor al numero secreto")
            intentos -= 1
        elif numero == numero_aleatorio_medio:
            #cumplio el objetivo, gano, por lo tanto salimos del ciclo
            ganar = True
            print("\n*****BINGO HAZ ACERTADO EN", intentos, "INTENTOS!!!***** \n")
            intentos = 0
        else:
            print("Opcion invalida. Intentelo de nuevo")

    #mensaje final al usuario
    final_mensaje(0, ganar)


#creamos una funcion para el tercer nivel con limite de intentos y tiempo para adivinar el numero
def nivel_dificil():
    print("NIVEL DIFICIL:")
    print("Tienes una cantidad de 5 intentos y debes adivinar un numero del 0 al", DIFICULTAD_DIFICIL)
    print("PERO DEBES LOGRARLO ANTES DE 4 SEGUNDOS, SINO SE RESTARA UN INTENTO")

    #creamos el numero aleatorio correspondiente a la dificultad dificil
    numero_aleatorio_dificil = random.randint(0, DIFICULTAD_DIFICIL)

    #inicializamos la varible ganar como false como parte del mensaje final
    ganar = False

    #inicializamos la variable intentos del nivel con 5
    intentos = 5

    #ver el numero (para prueba de escritorio)
    #print(numero_aleatorio_dificil)

    #iniciamos el ciclo del juego modo dificil
    while intentos != 0:
        #mostramos cantidad de intentos
        print("INTENTOS DISPONIBLES:", intentos)

        #inicializamos el reloj
        tiempo_inicial = time.time()

        #pedimos un numero al usuario
        numero = int(input("\nIngrese un numero: "))

        #evaluamos las condiciones
        if numero > numero_aleatorio_dificil:
            print("El numero ingresado es mayor al numero secreto")
            intentos -= 1
        elif numero < numero_aleatorio_dificil:
            print("El numero ingresado es menor al numero secreto")
            intentos -= 1
        elif numero == numero_aleatorio_dificil:
            #en caso de acertar se toma el tiempo final
            tiempo_final = time.time()

            #se busca el tiempo total que tomo la respuesta
            tiempo_total = round(tiempo_final - tiempo_inicial)

            #si es menor al tiempo requerido gana el juego
            if tiempo_total < 5:
                ganar = True
                print("\n*****BINGO HAZ ACERTADO!! EN SOLO " + str(tiempo_total) + " SEGUNDOS*****\n")
                intentos = 0
            else:
                #en caso que haya acertado pero no el tiempo perdido se le muestra un mensaje al usuario
                print("TU RESPUESTA HA SIDO CORRECTA PERO EL TIEMPO NO LE HA ALCANZADO")
                intentos = 0
        else:
            print("OPCION NO VALIDA")

    #mensaje final al usuario
    final_mensaje(0, ganar)


#Creamos un menu para elegir el nivel de juego
while opcion != 4:
    print("Adivina el numero:")
    print("1 - Dificultad Facil")
    print("2 - Dificultad Media")
    print("3 - Dificultad Dificil")
    print("4 - Salir")

    #pedimos al usuario la opcion
    opcion = int(input("\nElige tu opcion: "))

    #creamos una lista con los metodos
    niveles = [nivel_facil, nivel_medio, nivel_dificil, salir]

    #llamamos a la opcion deseada
    niveles[opcion - 1]()


