#------------- CRUD CON TKINTER Y SQLITE3 --------#

# Importar las librerías necesarias

import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# En primer lugar voy a crear la interfaz gráfica

root=Tk()

miFrame=Frame()
miFrame.pack()
miFrame.config(bg="#B6B6D7")
miFrame.config(width=300, height=350)

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




root.mainloop()
