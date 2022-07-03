import tkinter 
from tkinter import *
#ttk = treeview
from tkinter import ttk


ventana = Tk()
ventana.title("Ejemplo de arboles")
ventana.geometry("400x300")
ventana['bg'] = '#fb0'

#creamos el arbol
#widget treeview muestra una coleccion en arbol de elementos, tiene enbezado
#y es una forma prolija de mostrar la informacion en una bdd
#mediante nodos e hijos
#admite desplazamiento horizontal y vertical
tv = ttk.Treeview(ventana, columns= ("c1", "c2"))

#Configuracion columnas
tv.column("#0", width= 80)
tv.column("c1", width= 80, anchor=CENTER)
tv.column("c2", width= 80, anchor=CENTER)

#encabezados columnas
tv.heading("#0", text= "ID", anchor=CENTER)
tv.heading("c1", text= "Producto", anchor=CENTER)
tv.heading("c2", text= "Precio", anchor=CENTER)

#insertar valores en la columna
tv.insert("", END, text= "Azucar", values=("28", "2"))
tv.insert("", END, text= "Refresco", values=("23", "4"))
tv.insert("", END, text= "Aceite", values=("11", "6"))

tv.pack()

ventana.mainloop()