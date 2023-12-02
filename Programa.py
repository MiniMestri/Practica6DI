from bs4 import BeautifulSoup
import tkinter as tk

raiz = tk.Tk()

archivo = open("instruccion.xml","r")
contenido = archivo.read()
xml = BeautifulSoup(contenido,"xml")
for campo in xml.find_all("campo"):
    tipo = campo.get("tipo")
    if tipo == "entrada":
        tk.Entry(raiz).pack(padx=20,pady=20)
    elif tipo== "etiqueta":
        tk.Label(raiz,text="hola").pack(padx=20,pady=20)
    elif tipo == "boton":
        tkButton(raiz,text="hola").pack(padx=20,pady=20)

tk.mainloop()
 
