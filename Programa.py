from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()

raiz.geometry(f"{500}x{300}")

ventana=tk.PanedWindow(raiz,orient=tk.HORIZONTAL)
marco1=tk.Frame(ventana,background="yellow",width=250)
marco2=tk.Frame(ventana,background="orange",width=250)

ventana.add(marco1)
ventana.add(marco2)

ventana.pack(fill=tk.BOTH,expand=True)

raiz.mainloop()
 
