import tkinter 
from tkinter import *
#ttk = treeview
from tkinter import ttk



#widget treeview muestra una coleccion en arbol de elementos, tiene enbezado
#y es una forma prolija de mostrar la informacion en una bdd
#mediante nodos e hijos
#admite desplazamiento horizontal y vertical


ventana = Tk()
ventana.title("Ejemplo de arboles")
ventana.geometry("400x300")
ventana['bg'] = '#fb0'

#creamos el arbol
tv = ttk.Treeview(ventana)

#creamos el primer nodo padre
item1 = tv.insert("",END, text="Dias")

#nodos hijos de item1
tv.insert( item1,END, text="Lunes")
tv.insert( item1,END, text="Martes")
tv.insert( item1,END, text="Miercoles")
tv.insert( item1,END, text="Jueves")
tv.insert( item1,END, text="Viernes")
tv.insert( item1,END, text="Sabado")
tv.insert( item1,END, text="Domingo")

#creamos el segundo nodo padre
item2 = tv.insert("",END, text="Colores")

#nodos hijos de item2
tv.insert( item2 ,END, text="Rojo")
tv.insert( item2 ,END, text="Amarillo")
tv.insert( item2 ,END, text="Verde")
tv.insert( item2 ,END, text="Violeta")
tv.insert( item2 ,END, text="Negro")

#---------Metodos----------

#imprimimos el nodo
#print(tv.item(item1))
#imprmimos los hijos
#print(tv.get_children(item1))

#vista de nodo padre -> hijos
for x in tv.get_children():
	print(x)
	print(tv.get_children(x))



tv.pack()

ventana.mainloop()