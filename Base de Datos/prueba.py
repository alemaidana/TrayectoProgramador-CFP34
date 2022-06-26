import tkinter 
from tkinter import *
#ttk = treeview
from tkinter import ttk
import sqlite3

#Colores Interfaz Grafica
color = "#44475a"
color_texto = "#f8f8f2" 
color_boton = "#8be9fd"
color_boton2 = "#ffb86c" #

#creamos la conexion
conn = sqlite3.connect('elementos.db')
    
#Crear un cursor
c = conn.cursor()
    
ventana = Tk()
ventana.title("Ejemplo de arboles")
ventana.geometry("1000x400")
ventana['bg'] = color

#Funcion para mostrar todos los registros del producto
def mostrar():
	conn = sqlite3.connect('elementos.db')
	c = conn.cursor()
	c.execute("SELECT * FROM Producto")
	elementos = c.fetchall()
	for elemento in elementos:
		arbol.insert("", END, text = elemento[0],  values=(elemento[1], elemento[2], elemento[3]))
		
	conn.commit()
	conn.close()

#titulo
titulo = Label(ventana, text= "Crud Base de datos", bg = color, fg= color_texto, font=("Verdana",24))
titulo.grid(row = 0, column = 2, columnspan= 2)

#botones
boton_agregar = Button(ventana, text= "Agregar", command = None, bg = color_boton2, fg = color_texto)
boton_agregar.grid(row= 1, column = 0, columnspan= 2, padx= 20, pady = 20, ipadx= 50)

boton_modificar = Button(ventana, text= "Modificar", command = None, bg = color_boton2, fg = color_texto)
boton_modificar.grid(row= 2, column = 0, columnspan= 2, padx= 20, pady = 20, ipadx= 50)

boton_consultar = Button(ventana, text= "Consultar", command = mostrar, bg = color_boton2, fg = color_texto)
boton_consultar.grid(row= 3, column = 0, columnspan= 2, padx= 20, pady = 20, ipadx= 50)

boton_eliminar = Button(ventana, text= "Eliminar", command = None, bg = color_boton2, fg = color_texto)
boton_eliminar.grid(row= 4, column = 0, columnspan= 2, padx= 20, pady = 20, ipadx= 50)


#widget treeview muestra una coleccion en arbol de elementos, tiene enbezado
#y es una forma prolija de mostrar la informacion en una bdd
#mediante nodos e hijos
#admite desplazamiento horizontal y vertical

#Arbol
arbol = ttk.Treeview(ventana, columns=("c1", "c2", "c3"))

#Configuracion columnas
arbol.column("#0", width= 200, anchor=CENTER)
arbol.column("c1", width= 200, anchor=CENTER)
arbol.column("c2", width= 200, anchor=CENTER)
arbol.column("c3", width= 150, anchor=CENTER)

#encabezados columnas
arbol.heading("#0", text= "ID", anchor=CENTER)
arbol.heading("c1", text= "Producto", anchor=CENTER)
arbol.heading("c2", text= "Precio", anchor=CENTER)
arbol.heading("c3", text= "Cantidad", anchor=CENTER)


arbol.grid(row=1, column= 2, columnspan = 20, rowspan = 4) 


#comiteamos los cambios
conn.commit()
#cerramos la conexion
conn.close()


ventana.mainloop()