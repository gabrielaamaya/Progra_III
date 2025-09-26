import tkinter as tk
from tkinter import messagebox

def calcular_promedio():
    try:
        lab1 = float(entry_lab1.get())
        lab2 = float(entry_lab2.get())
        parcial = float(entry_parcial.get())

        # Validación de rango
        if not (0 <= lab1 <= 10 and 0 <= lab2 <= 10 and 0 <= parcial <= 10):
            messagebox.showerror("Error", "Todas las notas deben estar entre 0 y 10")
            return

        # Cálculo del promedio ponderado
        nota_final = (lab1 * 0.3) + (lab2 * 0.3) + (parcial * 0.4)

        # Mostrar resultado en la etiqueta
        resultado.set(f"Nota final: {nota_final:.2f} - {'Aprobado ' if nota_final >= 6 else 'Reprobado '}")

    except ValueError:
        messagebox.showerror("Error", "Ingrese solo números válidos.")

# ===== Ventana principal =====
ventana = tk.Tk()
ventana.title("Formulario - Cálculo de Nota Final")
ventana.geometry("400x250")
ventana.resizable(False, False)

# ===== Formulario =====
tk.Label(ventana, text="Laboratorio 1 (30%):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_lab1 = tk.Entry(ventana)
entry_lab1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(ventana, text="Laboratorio 2 (30%):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_lab2 = tk.Entry(ventana)
entry_lab2.grid(row=1, column=1, padx=10, pady=5)

tk.Label(ventana, text="Parcial (40%):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_parcial = tk.Entry(ventana)
entry_parcial.grid(row=2, column=1, padx=10, pady=5)

# Botón de calcular
btn = tk.Button(ventana, text="Calcular Promedio", command=calcular_promedio)
btn.grid(row=3, column=0, columnspan=2, pady=15)

# Etiqueta de resultado
resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, font=("Arial", 12, "bold")).grid(row=4, column=0, columnspan=2, pady=10)

ventana.mainloop()