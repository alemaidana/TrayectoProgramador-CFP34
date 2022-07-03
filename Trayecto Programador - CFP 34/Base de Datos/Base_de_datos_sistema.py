import tkinter
from tkinter import *
# ttk = treeview
from tkinter import ttk
import sqlite3
 
# Colores Interfaz Grafica
color = "#44475a"
color_texto = "#f8f8f2"
color_boton = "#8be9fd"
color_boton2 = "#ffb86c"  #
 
# creamos la conexion
conn = sqlite3.connect('elementos.db')
 
# Crear un cursor
c = conn.cursor()
 
ventana = Tk()
ventana.title("Ejemplo de arboles")
ventana.geometry("1000x400")
ventana['bg'] = color
 
 
# Funcion para mostrar todos los registros del producto
def mostrar():
    conn = sqlite3.connect('elementos.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Producto")
    elementos = c.fetchall()
    for i in arbol.get_children():
        arbol.delete(i)
    for elemento in elementos:
        arbol.insert("", END, text=elemento[0], values=(elemento[1], elemento[2], elemento[3]))
 
    conn.commit()
    conn.close()
 
 
#funcion propia de la ventana eliminar
def borrar_registro():
    conn = sqlite3.connect("elementos.db")
    c = conn.cursor()
    c.execute("DELETE FROM Producto WHERE ID = " + campo_eliminar.get())
    conn.commit()
    conn.close()
    campo_eliminar.delete(0, END)
 
 
 
#funcion propia de ventana agregar
def agregar_front():
    conn = sqlite3.connect("elementos.db")
    c = conn.cursor()
 
    c.execute("INSERT INTO Producto (Nombre, Precio, Cantidad) VALUES (:Producto, :Precio, :Cantidad)",
 
              {"Producto": entrada_producto.get(),
               "Precio": entrada_precio.get(),
               "Cantidad": entrada_cantidad.get()
 
               }
 
              )
 
    conn.commit()
    conn.close()
 
    entrada_producto.delete(0, END)
    entrada_precio.delete(0, END)
    entrada_cantidad.delete(0, END)
    mostrar()
 
#Creamos una segunda funcion para pasar los datos al front
def agregar():
    global entrada_producto
    global entrada_precio
    global entrada_cantidad
    #creamos una ventana nueva
    ventana_agregar = Tk()
    ventana_agregar.title("Agregar Registro")
    ventana_agregar.geometry('300x200')
    ventana_agregar['bg'] = color
    #establecemos la conexion
    conn = sqlite3.connect('elementos.db')
    c = conn.cursor()
    #etiquetas de la ventana
    producto = Label(ventana_agregar, text= "Nombre", bg=color, fg=color_texto)
    producto.grid(row=0, column=0)
    precio = Label(ventana_agregar, text="Precio", bg=color, fg=color_texto)
    precio.grid(row=1, column=0)
    cantidad = Label(ventana_agregar, text="Cantidad", bg=color, fg=color_texto)
    cantidad.grid(row=2, column=0)
    #inputs de texto
    entrada_producto = Entry(ventana_agregar, width=30)
    entrada_producto.grid(row=0, column=1)
    entrada_precio = Entry(ventana_agregar, width=30)
    entrada_precio.grid(row=1, column=1)
    entrada_cantidad = Entry(ventana_agregar, width=30)
    entrada_cantidad.grid(row=2, column=1)
    #botones de accion
    btn_ok = Button(ventana_agregar, text="Agregar", command=agregar_front, bg=color_boton2, fg=color_texto)
    btn_ok.grid(row=3, column=1, columnspan=2)
 
    #comiteamos los cambios y cerramos conexion
    conn.commit()
    conn.close()
 
 
def eliminar():
    global campo_eliminar
    #creamos una ventana para eliminar los registros
    ventana_eliminar = Tk()
    ventana_eliminar.title("Eliminar Registro")
    ventana_eliminar.geometry("300x200")
    ventana_eliminar['bg'] = color
    #creamos las conexiones con la base de datos
    conn = sqlite3.connect("elementos.db")
    c = conn.cursor()
    #etiquetas , inputs texto y botones
    etiqueta_eliminar = Label(ventana_eliminar, text="ID a eliminar", bg=color, fg=color_texto)
    etiqueta_eliminar.grid(row=0, column=0)
    campo_eliminar = Entry(ventana_eliminar, width=30)
    campo_eliminar.grid(row=0, column=1)
    btn_borrar = Button(ventana_eliminar, text="Eliminar", command=borrar_registro, bg=color_boton2, fg=color_texto)
    btn_borrar.grid(row=1, column=1, columnspan=2)
 
#Funcion para editar registro
def modificar():
    #creamos la ventana para modificar los registros
    ventana_modificar = Tk()
    ventana_modificar.title("Modificar registro")
    ventana_modificar.geometry("300x300")
    ventana_modificar['bg'] = color
    #creamos las conexiones con la base de datos
    conn = sqlite3.connect('elementos.db')
    c = conn.cursor()
    #etiquetas, inputs, textos y botones
 
    buscar_codigo = Label(ventana_modificar, text="Ingrese el ID", bg=color, fg=color_texto)
    buscar_codigo.grid(row=0, column=0)
    input_codigo = Entry(ventana_modificar, width=30)
    input_codigo.grid(row=0, column=1)
 
    btn_buscar = Button(ventana_modificar, text="Buscar", command=None, bg=color_boton2, fg=color_texto)
    btn_buscar.grid(row=1, column=1, columnspan=2)
 
    etiqueta_act_producto = Label(ventana_modificar, text="Producto", bg=color, fg=color_texto)
    etiqueta_act_producto.grid(row=2, column=0)
    etiqueta_act_precio = Label(ventana_modificar, text="Precio", bg=color, fg=color_texto)
    etiqueta_act_precio.grid(row=3, column=0)
    etiqueta_act_cantidad = Label(ventana_modificar, text="Cantidad", bg=color, fg=color_texto)
    etiqueta_act_cantidad.grid(row=4, column=0)
    campo_act_producto = Entry(ventana_modificar, width=30)
    campo_act_producto.grid(row=2, column=1)
    campo_act_precio = Entry(ventana_modificar, width=30)
    campo_act_precio.grid(row=3, column=1)
    campo_act_cantidad = Entry(ventana_modificar, width=30)
    campo_act_cantidad.grid(row=4, column=1)
 
    btn_actualizar_reg = Button(ventana_modificar, text="Actualizar", command=None, bg=color_boton2, fg=color_texto)
    btn_actualizar_reg.grid(row=5, column=1, columnspan=2)
 
 
 
# titulo
titulo = Label(ventana, text="Inventario almacen", bg=color, fg=color_texto, font=("Verdana", 24))
titulo.grid(row=0, column=2, columnspan=2)
 
# botones
boton_agregar = Button(ventana, text="Agregar", command=agregar, bg=color_boton2, fg=color_texto)
boton_agregar.grid(row=1, column=0, columnspan=2, padx=20, pady=20, ipadx=50)
 
boton_modificar = Button(ventana, text="Modificar", command= modificar, bg=color_boton2, fg=color_texto)
boton_modificar.grid(row=2, column=0, columnspan=2, padx=20, pady=20, ipadx=50)
 
boton_consultar = Button(ventana, text="Consultar", command= mostrar, bg=color_boton2, fg=color_texto)
boton_consultar.grid(row=3, column=0, columnspan=2, padx=20, pady=20, ipadx=50)
 
boton_eliminar = Button(ventana, text="Eliminar", command=eliminar, bg=color_boton2, fg=color_texto)
boton_eliminar.grid(row=4, column=0, columnspan=2, padx=20, pady=20, ipadx=50)
 
# widget treeview muestra una coleccion en arbol de elementos, tiene enbezado
# y es una forma prolija de mostrar la informacion en una bdd
# mediante nodos e hijos
# admite desplazamiento horizontal y vertical
 
# Arbol
arbol = ttk.Treeview(ventana, columns=("c1", "c2", "c3"))
 
# Configuracion columnas
arbol.column("#0", width=200, anchor=CENTER)
arbol.column("c1", width=200, anchor=CENTER)
arbol.column("c2", width=200, anchor=CENTER)
arbol.column("c3", width=150, anchor=CENTER)
 
# encabezados columnas
arbol.heading("#0", text="ID", anchor=CENTER)
arbol.heading("c1", text="Producto", anchor=CENTER)
arbol.heading("c2", text="Precio", anchor=CENTER)
arbol.heading("c3", text="Cantidad", anchor=CENTER)
 
arbol.grid(row=1, column=2, columnspan=20, rowspan=4)
 
# comiteamos los cambios
conn.commit()
# cerramos la conexion
conn.close()
 
ventana.mainloop()