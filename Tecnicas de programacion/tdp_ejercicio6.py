"""
Ejercicio 3.9.3. Escribir una función que, dados cuatro números, devuelva el mayor producto
de dos de ellos. Por ejemplo, si recibe los números 1, 5, -2, -4 debe devolver 8, que es el producto
más grande que se puede obtener entre ellos (8 = −2 × −4).
"""

#Definimos la funcion para obtener el numero de elementos que deseamos ingresar
def dame_numero_de_elementos():

    #Preguntamos al usuario cuantos numeros desea ingresar
    numero_elementos = int(input("Ingrese la cantidad de elementos que desea ingresar: "))

    #En caso que sea negativo el numero ingresado se le solicitara de nuevo el mismo
    while numero_elementos < 0:
        #mensaje de error al usuario por introducir numero negativo
        print("ERROR ! El numero de elementos no puede ser negativo. Por favor intentelo de nuevo.")
        #volvemos a pedir el numero hasta que este sea postivo
        numero_elementos = int(input("Ingrese la cantidad de elementos que desea ingresar"))

    #devolvemos el numero de elementos de la lista
    return numero_elementos

#Definimos la funcion para agregar los numeros a la lista
def agregar_valores(cantidad):

    #creamos una lista vacia para almacenar los numeros
    numeros = []

    #vamos agregando elementos a la lista desde 0 hasta la cantidad de elementos que se desea
    for elemento in range(0, cantidad):
        numero = int(input("Ingrese el " + str(elemento + 1) + " numero: "))
        numeros.append(numero)

    #devolvemos la lista con los valores cargados
    return numeros



#Definimos la funcion para encontrar el maximo producto
def maximo_producto(lista_de_numeros):

    #guardamos en una variable el tamaño de la lista
    cantidad_numeros = len(lista_de_numeros)

    #creamos la variable que almacenara el valor maximo
    valor_maximo = 0

    #exploramos la lista realizando la busqueda del maximo producto de la lista
    for filas in range(0, cantidad_numeros):

        for columnas in range(1, cantidad_numeros):

            if (lista_de_numeros[filas] * lista_de_numeros[columnas] > valor_maximo) and (filas != columnas):

                valor_maximo = lista_de_numeros[filas] * lista_de_numeros[columnas]

    #devolvemos el valor maximo
    return valor_maximo




#LLamamos a la funcion con los valores a buscar el maximo producto

#almacenamos en x el numero de elementos
x = dame_numero_de_elementos()

#en valores guardamos la lista con los numeros
valores = agregar_valores(x)

#mostramos por pantalla al usuario cual fue el maximo producto encontrado en los valores de la lista
print("\nEl mayor producto de los numeros ingresados es: " + str(maximo_producto(valores)))


