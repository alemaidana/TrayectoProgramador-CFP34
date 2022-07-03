from random import *


def juego_barco(barco, nave_mayor, nave_menor, mercante, long_mapa):
    # este es el mapa maestro que solo veo yo con todas las ubicaciones
    mapa = [["-" for row in range(long_mapa)] for column in range(long_mapa)]
    # este es el map que solo ve el usuario
    oceano = [["-" for row in range(long_mapa)] for column in range(long_mapa)]

    # definimos cabeceras para los mapas
    lista_letras = [" ", " A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    lista_numeros = [" ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "10"]

    # las agregamos al mapa
    for i in range(0, len(lista_letras)):
        mapa[0][i] = lista_letras[i]

    for i in range(0, len(lista_numeros)):
        mapa[i][0] = lista_numeros[i]

    # mapa que vera el usuario
    for i in range(0, len(lista_letras)):
        oceano[0][i] = lista_letras[i]

    for i in range(0, len(lista_numeros)):
        oceano[i][0] = lista_numeros[i]

    # establecemos las coordenadas de los barcos con un valor inicial
    xa = 1
    ya = 1

    xb = 1
    yb = 1

    xc = 1
    yc = 1

    xd = 1
    yd = 1

    # seteamos los posiciones
    xa = randint(1, 5)
    ya = randint(1, 2)
    for i in range(5):
        mapa[xa][ya + i] = barco

    xb = xa + 5
    yb = ya + 4
    for i in range(4):
        mapa[xb][yb + i] = nave_mayor

    xc = randint(7, 8)
    yc = randint(1, 3)
    for i in range(3):
        mapa[xc + i][yc] = nave_menor

    xd = randint(1, 4)
    yd = randint(8, 10)
    for i in range(2):
        mapa[xd + i][yd] = mercante

    #DESCOMENTA LAS DOS SIGUIENTES LINEAS SI QUIERES VER EL MAPA MAESTRO
    #for row in mapa:
    #    print(" ".join(str(casillero) for casillero in row))

    # Creamos un diccionario para lanzar los disparos
    ubicaciones = {
        "": 0, "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10
    }

    # variables de intentos y corte
    barcos_restantes = 14
    # variables de barcos
    total_barco = 0
    total_nave = 0
    total_mercante = 0
    total_velero = 0

    print("****BATALLA NAVAL****\n")
    # imprimimos el mapa
    for row in oceano:
        print(" ".join(str(casillero) for casillero in row))

    # creamos un ciclo while para lanzar los disparos
    while barcos_restantes != 0:

        print("--Donde deseas disparar?--")
        fila = int(input("Ingresa la fila: "))
        columna = input("Ingresa la columna: ")

        # pasando la columna a mayuscula nos ahorramos un problema de may/min
        if mapa[fila][ubicaciones[columna.upper()]] == "B":
            print("TOCADO")
            oceano[fila][ubicaciones[columna.upper()]] = "X"
            barcos_restantes -= 1
            total_barco += 1
        elif mapa[fila][ubicaciones[columna.upper()]] == "N":
            print("TOCADO")
            oceano[fila][ubicaciones[columna.upper()]] = "X"
            barcos_restantes -= 1
            total_nave += 1
        elif mapa[fila][ubicaciones[columna.upper()]] == "M":
            print("TOCADO")
            oceano[fila][ubicaciones[columna.upper()]] = "X"
            barcos_restantes -= 1
            total_mercante += 1
        elif mapa[fila][ubicaciones[columna.upper()]] == "V":
            print("TOCADO")
            oceano[fila][ubicaciones[columna.upper()]] = "X"
            barcos_restantes -= 1
            total_velero += 1
        else:
            print("AGUA")
            oceano[fila][ubicaciones[columna.upper()]] = "~"

        #mostramos estados de los barcos al usuario a medida que los va hundiendo
        if total_barco == 5:
            print("BARCO --> HUNDIDO")
        if total_nave == 4:
            print("NAVE --> HUNDIDO")
        if total_mercante == 3:
            print("MERCANTE --> HUNDIDO")
        if total_velero == 2:
            print("VELERO --> HUNDIDO")

        # imprimimos el mapa
        for row in oceano:
            print(" ".join(str(casillero) for casillero in row))

    print("\n")
    print("Ganaste !!! ")
    print("Hundiste todos los barcos")
    print(".--------------------.")
    print("|  G A M E  O V E R  | ")
    print(".--------------------.")


juego_barco("B", "N", "M", "V", 11)
