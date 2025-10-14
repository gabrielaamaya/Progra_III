import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import articulos

class FormularioArticulo:
    def __init__(self):
        self.articulo1 = articulos.Articulos()
        self.ventana1 = tk.Tk()
        self.ventana1.title("Inventario")

        self.cuaderno1 = ttk.Notebook(self.ventana1)
        self.carga_articulo()
        self.consulta_por_codigo()
        self.modificar()
        self.borrado()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)

        self.ventana1.mainloop()


    # Pestaña 1: Insertar

    def carga_articulo(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Insertar")
        self.labelframe1 = ttk.LabelFrame(self.pagina1, text="Producto")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        ttk.Label(self.labelframe1, text="Nombre:").grid(column=0, row=0, padx=4, pady=4)
        self.descripcioncarga = tk.StringVar()
        ttk.Entry(self.labelframe1, textvariable=self.descripcioncarga).grid(column=1, row=0, padx=4, pady=4)

        ttk.Label(self.labelframe1, text="Precio:").grid(column=0, row=1, padx=4, pady=4)
        self.preciocarga = tk.StringVar()
        ttk.Entry(self.labelframe1, textvariable=self.preciocarga).grid(column=1, row=1, padx=4, pady=4)

        ttk.Button(self.labelframe1, text="Guardar", command=self.agregar).grid(column=1, row=2, padx=4, pady=4)

    def agregar(self):
        datos = (self.descripcioncarga.get(), self.preciocarga.get())
        self.articulo1.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados correctamente.")
        self.descripcioncarga.set("")
        self.preciocarga.set("")


    # Pestaña 2: Consulta por código

    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por código")

        self.labelframe2 = ttk.LabelFrame(self.pagina2, text="Artículo")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)

        ttk.Label(self.labelframe2, text="Código:").grid(column=0, row=0, padx=4, pady=4)
        self.codigo = tk.StringVar()
        ttk.Entry(self.labelframe2, textvariable=self.codigo).grid(column=1, row=0, padx=4, pady=4)

        ttk.Label(self.labelframe2, text="Descripción:").grid(column=0, row=1, padx=4, pady=4)
        self.descripcion = tk.StringVar()
        ttk.Entry(self.labelframe2, textvariable=self.descripcion, state="readonly").grid(column=1, row=1, padx=4, pady=4)

        ttk.Label(self.labelframe2, text="Precio:").grid(column=0, row=2, padx=4, pady=4)
        self.precio = tk.StringVar()
        ttk.Entry(self.labelframe2, textvariable=self.precio, state="readonly").grid(column=1, row=2, padx=4, pady=4)

        ttk.Button(self.labelframe2, text="Consultar", command=self.consultar).grid(column=1, row=3, padx=4, pady=4)

    def consultar(self):
        datos = (self.codigo.get(), )
        respuesta = self.articulo1.consulta(datos)
        if len(respuesta) > 0:
            self.descripcion.set(respuesta[0][0])
            self.precio.set(respuesta[0][1])
        else:
            self.descripcion.set('')
            self.precio.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código.")

    # Pestaña 3: Modificar artículo

    def modificar(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Modificar artículos")

        self.labelframe5 = ttk.LabelFrame(self.pagina4, text="Artículo")
        self.labelframe5.grid(column=0, row=0, padx=5, pady=10)

        # Código
        ttk.Label(self.labelframe5, text="Código:").grid(column=0, row=0, padx=4, pady=4)
        self.codigomod = tk.StringVar()
        ttk.Entry(self.labelframe5, textvariable=self.codigomod).grid(column=1, row=0, padx=4, pady=4)

        # Descripción
        ttk.Label(self.labelframe5, text="Nueva descripción:").grid(column=0, row=1, padx=4, pady=4)
        self.nuevadesc = tk.StringVar()
        ttk.Entry(self.labelframe5, textvariable=self.nuevadesc).grid(column=1, row=1, padx=4, pady=4)

        # Precio
        ttk.Label(self.labelframe5, text="Nuevo precio:").grid(column=0, row=2, padx=4, pady=4)
        self.nuevoprecio = tk.StringVar()
        ttk.Entry(self.labelframe5, textvariable=self.nuevoprecio).grid(column=1, row=2, padx=4, pady=4)

        # Botones
        ttk.Button(self.labelframe5, text="Consultar", command=self.consultar_mod).grid(column=0, row=3, padx=4, pady=4)
        ttk.Button(self.labelframe5, text="Modificar", command=self.actualizar).grid(column=1, row=3, padx=4, pady=4)

    def consultar_mod(self):
        codigo = self.codigomod.get().strip()
        if codigo == "":
            mb.showwarning("Atención", "Debe ingresar un código para consultar.")
            return

        datos = (codigo,)
        respuesta = self.articulo1.consulta(datos)
        if len(respuesta) > 0:
            self.nuevadesc.set(respuesta[0][0])
            self.nuevoprecio.set(respuesta[0][1])
        else:
            self.nuevadesc.set("")
            self.nuevoprecio.set("")
            mb.showinfo("Información", "No existe un artículo con dicho código.")

    def actualizar(self):
        codigo = self.codigomod.get().strip()
        descripcion = self.nuevadesc.get().strip()
        precio = self.nuevoprecio.get().strip()

        if codigo == "" or descripcion == "" or precio == "":
            mb.showwarning("Atención", "Todos los campos son obligatorios.")
            return

        try:
            float(precio)  # Validamos que el precio sea numérico
        except ValueError:
            mb.showerror("Error", "El precio debe ser un número.")
            return

        datos = (descripcion, precio, codigo)
        cantidad = self.articulo1.modificacion(datos)

        if cantidad == 1:
            mb.showinfo("Información", "El artículo se modificó correctamente.")
            self.codigomod.set("")
            self.nuevadesc.set("")
            self.nuevoprecio.set("")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código.")



    # Pestaña 4: Borrado

    def borrado(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Borrado de artículos")

        self.labelframe4 = ttk.LabelFrame(self.pagina3, text="Artículo")
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)

        ttk.Label(self.labelframe4, text="Código:").grid(column=0, row=0, padx=4, pady=4)
        self.codigoborra = tk.StringVar()
        ttk.Entry(self.labelframe4, textvariable=self.codigoborra).grid(column=1, row=0, padx=4, pady=4)

        ttk.Button(self.labelframe4, text="Borrar", command=self.borrar).grid(column=1, row=1, padx=4, pady=4)

    def borrar(self):
        datos = (self.codigoborra.get(), )
        cantidad = self.articulo1.baja(datos)
        if cantidad == 1:
            mb.showinfo("Información", "Se borró el artículo con dicho código.")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código.")



aplicacion1 = FormularioArticulo()