import tkinter as tk
from tkinter import messagebox
from datetime import datetime, date

def calcular():
    try:
        entrada = entry_fecha.get()
        fecha_nacimiento = datetime.strptime(entrada, "%d/%m/%Y").date()
        hoy = date.today()
        edad = hoy.year - fecha_nacimiento.year
        if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
            edad -= 1
        messagebox.showinfo("Resultado", f"Tienes {edad} años.")
    except ValueError:
        messagebox.showerror("Error", "Formato inválido. Usa dd/mm/aaaa.")

# Ventana principal
ventana = tk.Tk()
ventana.title("Formulario - Calculadora de Edad")
ventana.geometry("350x200")  # tamaño fijo
ventana.resizable(False, False)

# ===== FORMULARIO =====
lbl_titulo = tk.Label(ventana, text="Calculadora de Edad", font=("Arial", 14, "bold"))
lbl_titulo.grid(row=0, column=0, columnspan=2, pady=10)

lbl_fecha = tk.Label(ventana, text="Fecha de nacimiento (dd/mm/aaaa):")
lbl_fecha.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_fecha = tk.Entry(ventana, width=20)
entry_fecha.grid(row=1, column=1, padx=10, pady=5)

btn = tk.Button(ventana, text="Calcular Edad", width=15, command=calcular)
btn.grid(row=2, column=0, columnspan=2, pady=15)

ventana.mainloop()

