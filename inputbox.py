import tkinter as tk
from tkinter import StringVar

class Aplicacion:
    def __init__(self):
        # formulario
        self.formulario01 = tk.Tk()
        self.formulario01.title("Operaciones")
        self.formulario01.geometry("600x400")

        # etiqueta
        self.label01 = tk.Label(self.formulario01, text="Ingrese el primer número:")
        self.label01.grid(column=0, row=0, padx=10, pady=5)

        # caja de texto num1
        self.dato01 = StringVar()
        self.entry01 = tk.Entry(self.formulario01, width=10, textvariable=self.dato01)
        self.entry01.grid(column=1, row=0, padx=10, pady=5)

        # etiqueta segundo número
        self.label02 = tk.Label(self.formulario01, text="Ingrese el segundo número:")
        self.label02.grid(column=0, row=1, padx=10, pady=5)

        # caja de texto num2
        self.dato02 = StringVar()
        self.entry02 = tk.Entry(self.formulario01, width=10, textvariable=self.dato02)
        self.entry02.grid(column=1, row=1, padx=10, pady=5)

        # Botones de operaciones
        self.boton_suma = tk.Button(self.formulario01, text="Sumar", command=self.sumar)
        self.boton_resta = tk.Button(self.formulario01, text="Restar", command=self.restar)
        self.boton_multi = tk.Button(self.formulario01, text="Multiplicar", command=self.multiplicar)
        self.boton_div = tk.Button(self.formulario01, text="Dividir", command=self.dividir)

        # colocamos botones centrados
        self.boton_suma.grid(column=0, row=2, padx=10, pady=10, columnspan=2, sticky="nsew")
        self.boton_resta.grid(column=0, row=3, padx=10, pady=10, columnspan=2, sticky="nsew")
        self.boton_multi.grid(column=0, row=4, padx=10, pady=10, columnspan=2, sticky="nsew")
        self.boton_div.grid(column=0, row=5, padx=10, pady=10, columnspan=2, sticky="nsew")

        # Etiqueta de resultado
        self.label_resultado = tk.Label(self.formulario01, text="Resultado:")
        self.label_resultado.grid(column=0, row=6, columnspan=2, pady=20)

        self.formulario01.mainloop()

    def obtener_valores(self):
        """ Obtiene los valores de las cajas de texto """
        try:
            num1 = float(self.dato01.get())
            num2 = float(self.dato02.get())
            return num1, num2
        except ValueError:
            self.label_resultado.configure(text="Por favor, ingrese números válidos.")
            return None, None

    def sumar(self):
        num1, num2 = self.obtener_valores()
        if num1 is not None:
            self.label_resultado.configure(text=f"Resultado: {num1 + num2}")

    def restar(self):
        num1, num2 = self.obtener_valores()
        if num1 is not None:
            self.label_resultado.configure(text=f"Resultado: {num1 - num2}")

    def multiplicar(self):
        num1, num2 = self.obtener_valores()
        if num1 is not None:
            self.label_resultado.configure(text=f"Resultado: {num1 * num2}")

    def dividir(self):
        num1, num2 = self.obtener_valores()
        if num1 is not None:
            if num2 != 0:
                self.label_resultado.configure(text=f"Resultado: {num1 / num2}")
            else:
                self.label_resultado.configure(text="Error: División entre cero")

# Ejecutar la aplicación
app = Aplicacion()