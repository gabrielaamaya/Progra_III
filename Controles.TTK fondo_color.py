# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

main = tk.Tk()
main.title("Controles TTK")
main.config(bg="#E4E2E2")
main.geometry("600x400")

contador = tk.IntVar(value=0)  # variable para el número

style = ttk.Style(main)
style.theme_use("clam")

# ===== LABEL =====
style.configure("label.TLabel", background="#E4E2E2", foreground="#000", font=("Arial", 14, "bold"))
label = ttk.Label(master=main, textvariable=contador, style="label.TLabel", anchor="center")
label.place(x=271, y=75, width=80, height=40)

# ===== FUNCIONES =====
def aumentar():
    contador.set(contador.get() + 1)

def disminuir():
    contador.set(contador.get() - 1)

def salir():
    main.destroy()

def cambiar_fondo():
    if radio_button_var.get() == 0:
        main.config(bg="red")   # rojo
    elif radio_button_var.get() == 1:
        main.config(bg="turquoise2")      # turquoise2
    elif radio_button_var.get() == 2:
        main.config(bg="violet")      # Morado

# ===== BOTONES =====
style.configure("buttob.TButton", background="#E4E2E2", foreground="#000")
buttob = ttk.Button(master=main, text="Aumentar", style="buttob.TButton", command=aumentar)
buttob.place(x=271, y=157, width=80, height=40)

style.configure("button.TButton", background="#E4E2E2", foreground="#000")
button = ttk.Button(master=main, text="Disminuir", style="button.TButton", command=disminuir)
button.place(x=272, y=216, width=80, height=40)

style.configure("button1.TButton", background="#E4E2E2", foreground="#000")
button1 = ttk.Button(master=main, text="Salir", style="button1.TButton", command=salir)
button1.place(x=275, y=288, width=80, height=40)

# ===== RADIO BUTTONS =====
radio_button_var = tk.IntVar()

style.configure("radio_button.TRadiobutton", background="#E4E2E2", foreground="#000")

radio_button_0 = ttk.Radiobutton(
    master=main, variable=radio_button_var, text="red", value=0,
    style="radio_button.TRadiobutton", command=cambiar_fondo
)
radio_button_0.place(x=80, y=136)

radio_button_1 = ttk.Radiobutton(
    master=main, variable=radio_button_var, text="turquoise2", value=1,
    style="radio_button.TRadiobutton", command=cambiar_fondo
)
radio_button_1.place(x=80, y=160)

radio_button_2 = ttk.Radiobutton(
    master=main, variable=radio_button_var, text="violet", value=2,
    style="radio_button.TRadiobutton", command=cambiar_fondo
)
radio_button_2.place(x=80, y=184)

main.mainloop()