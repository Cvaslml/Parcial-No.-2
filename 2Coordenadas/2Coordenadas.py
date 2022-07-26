"""Herramienta: Plano cartesiano con 2 coordenadas"""

# importo la libreria tkinter, con el alias tk
from cgitb import text
from pydoc import plain
import tkinter as tk
from tkinter import TkVersion, messagebox


#---------------------------
# Funciones operaciones
# --------------------------
def graficar():
    messagebox.showinfo("Plano cartesiano", "Hizo click en el boton Calcular")

def borrar():
    messagebox.showinfo("Plano cartesiano", "Hizo click en el boton Borrar")
    x1.set(0)
    y1.set(0)
    x2.set(0)
    y2.set(0)
    at_resultados.delete("1.0","end")
   
def salir():
    messagebox.showinfo("Plano cartesiano", "La app se cerrará")
    ventana_principal.destroy()

def pendiente():
    messagebox.showinfo("Plano cartesiano", "Pendiente")
    m = (y2 - y1) / (x2 - x1)
    at_resultados(str(m))
    

# -----------------------------
# VENTANA PRINCIPAL
# -----------------------------

# creacion objeto Tk (ventana principal)
ventana_principal = tk.Tk()

# Titulo ventana principal
ventana_principal.title("Plano cartesiano")

# dimensiones de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton maximizar
ventana_principal.resizable(0,0)

# color de fondo ventana principal
ventana_principal.config(bg="black")

# icono de la ventana
ventana_principal.iconbitmap('Per.ico')

# -----------------------------
# FRAME ENTRADA DATOS
# -----------------------------
frame_entrada = tk.Frame(ventana_principal)
frame_entrada.config(bg="pink", width=480, height=40)
frame_entrada.place(x=10,y=10)

# etiqueta para el titulo
titulo = tk.Label(frame_entrada,text="PLANO CARTESIANO")
titulo.config(bg="pink", fg="black", font=("Arial, 12"))
titulo.place(x=150, y=10)

# -----------------------------
# FRAME OPERACIONES
# -----------------------------
frame_operaciones = tk.Frame(ventana_principal)
frame_operaciones.config(bg="pink", width=480, height=120)
frame_operaciones.place(x=10,y=380)

# boton Graficar
boton_calcular = tk.Button(frame_operaciones, text="Graficar", command=graficar)
boton_calcular.place(x=350, y=12)

# boton Pendiente
boton_pendiente = tk.Button(frame_operaciones, text="Pendiente", command= pendiente)
boton_pendiente.place(x=350, y=52)

# boton borrar
boton_borrar = tk.Button(frame_operaciones, text="Borrar", command=borrar)
boton_borrar.place(x=200, y=90)

# boton salir
boton_salir = tk.Button(frame_operaciones, text="Salir", command=salir)
boton_salir.place(x=430, y=90)

# -----------------------------
# Def de variables
# -----------------------------
#x1= tk()
#x2= tk()
#y1= tk()
#y2= tk()

# etiqueta X1
label_x1 = tk.Label(frame_operaciones, text = "X1 =")
label_x1.config(bg = "pink", fg="black", font=("Arial", 14))
label_x1.place(x=40, y=10)

# caja de texto para X1
entry_x1 = tk.Entry(frame_operaciones)
entry_x1.config(font=("Arial", 12))
entry_x1.focus_set()
entry_x1.place(x=90, y=12, width=70, height=25)

# etiqueta X2
label_x2 = tk.Label(frame_operaciones, text = "X2 =")
label_x2.config(bg = "pink", fg="black", font=("Arial", 14))
label_x2.place(x=200, y=10)

# caja de texto para X2
entry_x2 = tk.Entry(frame_operaciones)
entry_x2.config(font=("Arial", 12))
entry_x2.focus_set()
entry_x2.place(x=250, y=12, width=70, height=25)

# etiqueta Y1
label_y1 = tk.Label(frame_operaciones, text = "Y1 =")
label_y1.config(bg = "pink", fg="black", font=("Arial", 14))
label_y1.place(x=40, y=60)

# caja de texto para Y1
entry_y1 = tk.Entry(frame_operaciones)
entry_y1.config(font=("Arial", 12))
entry_y1.place(x=90, y=62, width=70, height=25)

# etiqueta Y2
label_y2 = tk.Label(frame_operaciones, text = "Y2 =")
label_y2.config(bg = "pink", fg="black", font=("Arial", 14))
label_y2.place(x=200, y=60)

# caja de texto para Y2
entry_y2 = tk.Entry(frame_operaciones)
entry_y2.config(font=("Arial", 12))
entry_y2.place(x=250, y=62, width=70, height=25)

# -----------------------------
# FRAME RESULTADOS
# -----------------------------
frame_resultados = tk.Frame(ventana_principal)
frame_resultados.config(bg="pink", width=300, height=300)
frame_resultados.place(x=100,y=60)

# area de texto de resultados
at_resultados = tk.Text(frame_resultados)
at_resultados.config(width=10, height=2)
at_resultados.place(x=210,y=255)

# desplegar ventana principal y queda a la espera de eventos del usuario
ventana_principal.mainloop()