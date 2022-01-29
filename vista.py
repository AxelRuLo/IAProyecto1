from tkinter import *
from tkinter import ttk
import tkinter as tk

window = Tk()
window.title("Pedidos")
window.geometry("650x500")
window.resizable(False, False)
window.config(bg="#DEB887")

tv = ttk.Treeview(window)
tv.insert("",END,text="Generar mapa")
tv.pack()



def abrirVentana():
    window2= Tk()
    window2.title("Ordenar")
    window2.geometry("500x500")
    window2.resizable(True, True)
    window2.config(bg="#DEB887")

    idPedido=tk.IntVar()
    numeroGarrafones=tk.IntVar()
    ubicacion=tk.IntVar()
    beneficioEntrega=tk.IntVar()

    tk.Label(window2,text="Identificador del Pedido",font=('Calibri', 14),background="#DEB887").place(x=100,y=30)
    tk.Label(window2,text="Numero de Garrafones",font=('Calibri', 14),background="#DEB887").place(x=100,y=90)
    tk.Label(window2,text="Ubicacion",font=('Calibri', 14),background="#DEB887").place(x=100,y=150)
    tk.Label(window2,text="Beneficio de Entrega",font=('Calibri', 14),background="#DEB887").place(x=100,y=210)

    tk.Entry(window2,textvariable=idPedido,font=('Calibri', 14),width=15).place(x=100,y=60)
    tk.Entry(window2,textvariable=numeroGarrafones,font=('Calibri', 14),width=15).place(x=100,y=120)
    tk.Entry(window2,textvariable=ubicacion,font=('Calibri', 14),width=15).place(x=100,y=180)
    tk.Entry(window2,textvariable=beneficioEntrega,font=('Calibri', 14),width=15).place(x=100,y=250)
    tk.Button(window2,font=('Calibri', 14),text="Hacer pedido").place(x=130,y=400)

tk.Label(window,text="Se mostrara la mejor solucion para la distribucion de garrafones",font=('Calibri', 16),background="#DEB887").place(x=20,y=0)
tk.Button(window,font=('Calibri', 14),text="Pedidos aleatorios").place(x=450,y=400)
tk.Button(window,font=('Calibri', 14),text="Ordenar",command=abrirVentana,).place(x=50,y=400)

window.mainloop()