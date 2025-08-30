#------------- CRUD CON TKINTER Y SQLITE3 --------#

# Importar las librerías necesarias

import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# En primer lugar voy a crear la interfaz gráfica

root=Tk()
root.config(width=400, height=300)

miFrame=Frame(root)
miFrame.pack()
#miFrame.config(bg="#B6B6D7")


frameDatos= Frame(miFrame, width=500)
frameDatos.grid(row=1, column=0)

frameBotones=Frame(miFrame)
frameBotones.grid(row=2, column=0)

#---------- Barra de menú ------------------------

barraMenu=Menu(miFrame)
root.config(menu=barraMenu)

menuBBDD=Menu(barraMenu)
menuBBDD.config(tearoff=0)
menuBBDD.add_command(label="Conectar")
menuBBDD.add_command(label="Salir")

menuBorrar=Menu(barraMenu)
menuBorrar.config(tearoff=0)
menuBorrar.add_command(label="Borrar")

menuCRUD=Menu(barraMenu)
menuCRUD.config(tearoff=0)
menuCRUD.add_command(label="Nuevo")
menuCRUD.add_command(label="Mostrar")
menuCRUD.add_command(label="Actualizar")
menuCRUD.add_command(label="Eliminar")

menuAyuda=Menu(barraMenu)
menuAyuda.config(tearoff=0)
menuAyuda.add_command(label="Licencia")
menuAyuda.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=menuBBDD)
barraMenu.add_cascade(label="Borrar", menu=menuBorrar)
barraMenu.add_cascade(label="CRUD", menu=menuCRUD)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)

#----------- Etiquetas de los campos ----------------------

etiquetaId=Label(frameDatos, text="Id")
etiquetaId.grid(row=0, column=0, sticky="e")

etiquetaNombre=Label(frameDatos, text="Nombre")
etiquetaNombre.grid(row=1, column=0, sticky="e")

etiquetaApellidos=Label(frameDatos, text="Apellidos")
etiquetaApellidos.grid(row=2, column=0, sticky="e")

etiquetaContra=Label(frameDatos, text="Contraseña")
etiquetaContra.grid(row=3, column=0, sticky="e")

etiquetaDireccion=Label(frameDatos, text="Dirección")
etiquetaDireccion.grid(row=4, column=0, sticky="e")

etiquetaComentarios=Label(frameDatos, text="Comentarios")
etiquetaComentarios.grid(row=5, column=0, sticky="e")

#-------------- Campos para introducir datos -------

campoId=Entry(frameDatos)
campoId.grid(row=0, column=1)

campoNombre=Entry(frameDatos)
campoNombre.grid(row=1, column=1)

campoApellidos=Entry(frameDatos)
campoApellidos.grid(row=2, column=1)

campoContra=Entry(frameDatos)
campoContra.grid(row=3, column=1)

campoDireccion=Entry(frameDatos)
campoDireccion.grid(row=4, column=1)

campoComentarios=Text(frameDatos)
campoComentarios.config(width=15, height=6)
campoComentarios.grid(row=5, column=1)

scroll=Scrollbar(frameDatos, command=campoComentarios.yview)
scroll.grid(row=5, column=2, sticky="nsew")
campoComentarios.config(yscrollcommand=scroll.set)

#-------------- Botones -------------------

botonNuevo=Button(frameBotones, text="Nuevo", width=7)
botonNuevo.grid(row=0, column=0)
botonLeer=Button(frameBotones, text="Leer", width=7)
botonLeer.grid(row=0, column=1)
botonActualizar=Button(frameBotones, text="Actualizar", width=7)
botonActualizar.grid(row=0, column=2)
botonEliminar=Button(frameBotones, text="Eliminar", width=7)
botonEliminar.grid(row=0, column=3)





root.mainloop()
