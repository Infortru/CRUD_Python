#------------- CRUD CON TKINTER Y SQLITE3 --------#

# Importar las librerías necesarias

from tkinter import *
from tkinter import messagebox
import sqlite3
#------------------ Variables --------------------------


#------------------ Funciones --------------------------

def crearBD():
    conexion=sqlite3.connect("Base usuarios")
    cursor=conexion.cursor()
    try:
        cursor.execute('''CREATE TABLE usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre VARCHAR(25), 
                    apellidos VARCHAR(50), 
                    contra INTEGER, 
                    dirección VARCHAR(50), 
                    comentarios VARCHAR(150)
                    )''')
        messagebox.showinfo(title=None, message="Base de datos creada")
    except Exception:
        messagebox.showwarning(title=None, message="La base de datos ya existe")
    conexion.close()

def borrarCampos():
    campoId.delete(0, END)
    campoNombre.delete(0, END)
    campoApellidos.delete(0, END)
    campoContra.delete(0, END)
    campoDireccion.delete(0, END)
    campoComentarios.delete(1.0, END)

def nuevoUsuario(nombre, apellidos, contra, direccion, comentarios):
    try:
        if nombre=="" or apellidos=="" or direccion=="" or contra=="":
            messagebox.showwarning(message="Falta algun dato")
        else:
            conexion=sqlite3.connect("Base usuarios")
            cursor=conexion.cursor()
            cursor.execute('''INSERT INTO usuarios (nombre, apellidos, contra, dirección, comentarios) 
                            VALUES(?,?,?,?,?)''',
                            (nombre, apellidos, contra, direccion, comentarios)
                            )
            conexion.commit()
            cursor.close()

            messagebox.showinfo("CRUD", "Nuevo usuario creado con éxito")

    except Exception:
        messagebox.showwarning(message="Ha ocurrido un error")

    borrarCampos()

def buscarUsuario(id):
    conexion=sqlite3.connect("Base usuarios")
    cursor=conexion.cursor()

    try:
        cursor.execute("SELECT * FROM usuarios WHERE id=" + id)
        datos=cursor.fetchall()

        for usuario in datos:
            nombre.set(usuario[1])
            apellidos.set(usuario[2])
            contrasena.set(usuario[3])
            direccion.set(usuario[4])
            campoComentarios.delete(1.0, END)
            if type(usuario[5])!=str:
                messagebox.showwarning(message="No hay comentarios")
            else:
                campoComentarios.insert(1.0, usuario[5])
        
    except Exception:
        messagebox.showwarning(message="Ha ocurrido un problema")
    conexion.close()

def actualizarUsuario(id, nombre, apellidos, contra, direccion, comentarios):
    
    conexion=sqlite3.connect("Base usuarios")
    cursor=conexion.cursor()
    actualizar='''UPDATE usuarios 
                SET nombre = ?,
                apellidos = ?,
                contra = ?,
                dirección = ?,
                comentarios = ?
                
                WHERE id= ?'''
    try:
        cursor.execute(actualizar, (nombre, apellidos, contra, direccion, comentarios, id))
        conexion.commit()
        cursor.close()

        messagebox.showinfo("CRUD", "Usuario actualizado correctamente")
    except Exception:
        messagebox.showwarning(message="Ha ocurrido un problema")
    conexion.close()

def eliminarUsuario(id):
    conexion=sqlite3.connect("Base usuarios")
    cursor=conexion.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id=" + id)
    conexion.commit()

    messagebox.showinfo("CRUD", "Registro eliminado con éxito")

    borrarCampos()
  
def salir():
    confirmar=messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")

    if(confirmar=="yes"):
        root.destroy()

def licencia():

    messagebox.showinfo("CRUD", "Aplicación de libre uso\n Versión: 1.0\n 2025")

def acercade():
    messagebox.showinfo("CRUD", "Aplicación de escritorio para la gestión de bases de datos")
# En primer lugar voy a crear la interfaz gráfica

root=Tk()

nombre=StringVar()
apellidos=StringVar()
contrasena=StringVar()
direccion=StringVar()

frameDatos= Frame(root, width=500)
frameDatos.grid(row=1, column=0)

frameBotones=Frame(root)
frameBotones.grid(row=2, column=0)

#---------- Barra de menú ------------------------

barraMenu=Menu(root)
root.config(menu=barraMenu, width=600, height=600)

menuBBDD=Menu(barraMenu)
menuBBDD.config(tearoff=0)
menuBBDD.add_command(label="Conectar", command=crearBD)
menuBBDD.add_command(label="Salir", command=salir)

menuBorrar=Menu(barraMenu)
menuBorrar.config(tearoff=0)
menuBorrar.add_command(label="Borrar", command=borrarCampos)

menuCRUD=Menu(barraMenu)
menuCRUD.config(tearoff=0)
menuCRUD.add_command(label="Nuevo", command=lambda:nuevoUsuario(campoNombre.get(), 
                                                                campoApellidos.get(), 
                                                                campoContra.get(), 
                                                                campoDireccion.get(), 
                                                                campoComentarios.get("1.0", END)))
                                                        
menuCRUD.add_command(label="Mostrar", command=lambda:buscarUsuario(campoId.get()))
menuCRUD.add_command(label="Actualizar", command=lambda:actualizarUsuario(campoId.get(),
                                                                        campoNombre.get(), 
                                                                        campoApellidos.get(), 
                                                                        campoContra.get(), 
                                                                        campoDireccion.get(), 
                                                                        campoComentarios.get("1.0", END)))
menuCRUD.add_command(label="Eliminar", command=lambda:eliminarUsuario(campoId.get()))

menuAyuda=Menu(barraMenu)
menuAyuda.config(tearoff=0)
menuAyuda.add_command(label="Licencia", command=licencia)
menuAyuda.add_command(label="Acerca de...", command=acercade)

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
campoId.grid(row=0, column=1, padx=10, pady=5)

campoNombre=Entry(frameDatos, textvariable=nombre)
campoNombre.grid(row=1, column=1, padx=10, pady=5)

campoApellidos=Entry(frameDatos, textvariable=apellidos)
campoApellidos.grid(row=2, column=1, padx=10, pady=5)

campoContra=Entry(frameDatos, textvariable=contrasena)
campoContra.grid(row=3, column=1, padx=10, pady=5)

campoDireccion=Entry(frameDatos, textvariable=direccion)
campoDireccion.grid(row=4, column=1, padx=10, pady=5)

campoComentarios=Text(frameDatos)
campoComentarios.config(width=15, height=6)
campoComentarios.grid(row=5, column=1, padx=10, pady=5)

scroll=Scrollbar(frameDatos, command=campoComentarios.yview)
scroll.grid(row=5, column=2, sticky="nsew")
campoComentarios.config(yscrollcommand=scroll.set)

#-------------- Botones -------------------

botonNuevo=Button(frameBotones, text="Nuevo", width=7, command=lambda:nuevoUsuario(campoNombre.get(), 
                                                                campoApellidos.get(), 
                                                                campoContra.get(), 
                                                                campoDireccion.get(), 
                                                                campoComentarios.get("1.0", END)))
botonNuevo.grid(row=0, column=0)
botonLeer=Button(frameBotones, text="Leer", width=7, command=lambda:buscarUsuario(campoId.get()))
botonLeer.grid(row=0, column=1)
botonActualizar=Button(frameBotones, text="Actualizar", width=7, command=lambda:actualizarUsuario(campoId.get(),
                                                                        campoNombre.get(), 
                                                                        campoApellidos.get(), 
                                                                        campoContra.get(), 
                                                                        campoDireccion.get(), 
                                                                        campoComentarios.get("1.0", END)))
botonActualizar.grid(row=0, column=2)
botonEliminar=Button(frameBotones, text="Eliminar", width=7, command=lambda:eliminarUsuario(campoId.get()))
botonEliminar.grid(row=0, column=3)





root.mainloop()
