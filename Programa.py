from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()

raiz.geometry(f"{670}x{300}")

ventana=tk.PanedWindow(raiz,orient=tk.HORIZONTAL)
marco1=tk.Frame(ventana,background="yellow")
marco2=tk.Frame(ventana,background="orange")

ventana.add(marco1)
ventana.add(marco2)

ventana.pack(fill=tk.BOTH,expand=True)

archivo=open("instruccion.xml","r")
contenido=archivo.read()
xml=BeautifulSoup(contenido,"xml")

for opcion in xml.find_all("opcion"):
    tipo=opcion.get("tipo")
    texto=opcion.get("text")
    if(tipo=="check1"):
        ttk.Label(marco1,text=texto,background="yellow").grid(row=0,column=0,padx=75,pady=20)
        ttk.Checkbutton(marco1).grid(row=0,column=1,padx=10)
    elif(tipo=="check2"):
        ttk.Label(marco2,text=texto,background="orange").grid(row=0,column=0,padx=75,pady=20)
        ttk.Checkbutton(marco2).grid(row=0,column=1,padx=10)

for texto in xml.find_all("texto"):
    tipo=texto.get("tipo")
    if(tipo=="label"):
        ttk.Label(marco1,text="Elige un numero",background="yellow").grid(row=1,column=0,padx=75,pady=20)
        ttk.Label(marco2,text="Elige el numero",background="orange").grid(row=1,column=0,padx=75,pady=20)

for eleccion in xml.find_all("eleccion"):
    tipo=eleccion.get("tipo")
    if(tipo=="entry"):
        ttk.Spinbox(marco1,from_=0,to=10).grid(row=2,column=0,padx=75,pady=20)
        ttk.Spinbox(marco2,from_=0,to=10).grid(row=2,column=0,padx=75,pady=20)
        
for eleccion in xml.find_all("resultado"):
    tipo=eleccion.get("tipo")
    if(tipo=="label"):
        ttk.Label(marco1,text="El resultado ha sido ",background="yellow").grid(row=4,column=0,padx=75,pady=20)
        ttk.Label(marco2,text="GANADOR ",background="orange").grid(row=4,column=0,padx=75,pady=20) 


raiz.mainloop()
 
