#Declaro la lista de palabras a ordenar
palabras = ["perro", "gato", "cisne", "mono", "jirafa", "cerdo"]

#Creo una lista temporal donde almacenar las palabras
#a ordenar por la segunda letra
lista_segunda_letra = []

print("Lista sin ordenar: ")
print(palabras)

#uso un for para recorrer la lista de palabras
for i in range(len(palabras)):

    #Creo una variable llamada "palabra" que almacenara
    #la palabra con el indice 0 de la misma llevada al final
    #ej: gato -> atog
    palabra = palabras[i][1::] + palabras[i][0]

    #A medida que vamos consiguiendo las palabras las vamos agregando
    #a la lista provisoria
    lista_segunda_letra.append(palabra)

#Ordenamos la lista alfabeticamenta
lista_segunda_letra.sort()

#realizamos otra prueba de escritorio para ver el indice 0 de la palabra
#haya sido colocado al final de la misma
print("Lista con el indice[0] cambiado al final: ")
print(lista_segunda_letra)

#Creamos una lista final donde vamos a insertar y volver a ordenar
#la lista llevando en indice 0 luego de ser ordenada
#al principio
ordenado = []

#Recorremos la lista  de la segunda letra al final
for j in range(len(lista_segunda_letra)):

    #realizamos la inversa del ciclo for anterior ponemos la ultima letra
    #al principio
    palabra_final = lista_segunda_letra[j][-1] + lista_segunda_letra[j][:-1]

    #Agregamos la palabra a la lista
    ordenado.append(palabra_final)


#mostramos al usuario la lista final ordenada por la segunda letra
print("Lista final ordenada: ")
print(ordenado)

