# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

main = tk.Tk()
main.title("Controles TTK")
main.config(bg="#E4E2E2")
main.geometry("600x400")

contador = tk.IntVar(value=0)  # variable para guardar el número

style = ttk.Style(main)
style.theme_use("clam")

# ===== LABEL =====
style.configure("label.TLabel", background="#E4E2E2", foreground="yellow", font=("Arial", 14, "bold"))
label = ttk.Label(master=main, textvariable=contador, style="label.TLabel", anchor="center")
label.place(x=271, y=75, width=80, height=40)

# ===== FUNCIONES =====
def aumentar():
    contador.set(contador.get() + 1)

def disminuir():
    contador.set(contador.get() - 1)

def salir():
    main.destroy()

# ===== BOTONES =====
style.configure("buttob.TButton", background="#E4E2E2", foreground="#000")
style.map("buttob.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

buttob = ttk.Button(master=main, text="Aumentar", style="buttob.TButton", command=aumentar)
buttob.place(x=271, y=157, width=80, height=40)

style.configure("button.TButton", background="#E4E2E2", foreground="#000")
style.map("button.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button = ttk.Button(master=main, text="Disminuir", style="button.TButton", command=disminuir)
button.place(x=272, y=216, width=80, height=40)

style.configure("button1.TButton", background="#E4E2E2", foreground="#000")
style.map("button1.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button1 = ttk.Button(master=main, text="Salir", style="button1.TButton", command=salir)
button1.place(x=275, y=288, width=80, height=40)

main.mainloop()
