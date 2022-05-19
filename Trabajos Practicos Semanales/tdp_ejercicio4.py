"""
Ejercicio 7.6. Dada una lista de números enteros y un entero k, escribir una función que:
a) Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a
k.
b) Devuelva una lista con aquellos que son múltiplos de k.
"""

#Recibimos el numero entero
entero = int(input("Ingrese un numero entero: "))

#Podemos pedir al usuario que ingrese la cantidad de numeros que quiera en su lista
tamanio = int(input("ingrese la cantidad de numeros que quiera en su lista: "))

#Creamos las listas
iguales = []
mayores = []
menores = []
coleccion_1 =[]
multiplos = []


#Ingresa el usuario los numeros que quiere

for valor in range(0, tamanio):
    print("ingrese el valor", (valor+1), ":")
    numero = int(input())
    coleccion_1.append(numero)
    if numero > entero:
        mayores.append(numero)
    elif numero < entero:
        menores.append(numero)
    else:
        iguales.append(numero)

    if coleccion_1[valor] % entero == 0:
        multiplos.append(numero)



#Imprime al usuario la coleccion que ingreso
print("\n--------INFORME DE DATOS--------")
print("Numero ingresado:", entero)
print("Lista de numeros ingresada:", coleccion_1)
print("Numeros Mayores", mayores)
print("Numeros Menores", menores)
print("Numeros Iguales", iguales)
print(f"Numeros Multiplos de {entero}:", multiplos )