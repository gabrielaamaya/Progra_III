import tkinter as tk
from tkinter import ttk, messagebox as mb, scrolledtext as st
import mysql.connector


class Libros:

    # CONEXIÓN A LA BASE DE DATOS

    def abrir(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="holamundo1"
        )

    # INSERTAR REGISTRO

    def alta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = """INSERT INTO libros (BookID, Title, Author, Publication, Price)
                 VALUES (%s,%s,%s,%s,%s)"""
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    # CONSULTAR REGISTRO POR ID

    def consulta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "SELECT * FROM libros WHERE BookID = %s"
        cursor.execute(sql, datos)
        registros = cursor.fetchall()
        cone.close()
        return registros

    # MODIFICAR REGISTRO

    def modificacion(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = """UPDATE libros
                 SET Title=%s, Author=%s, Publication=%s, Price=%s
                 WHERE BookID=%s"""
        cursor.execute(sql, datos)
        cone.commit()
        filas = cursor.rowcount
        cone.close()
        return filas

    # ELIMINAR REGISTRO

    def baja(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "DELETE FROM libros WHERE BookID = %s"
        cursor.execute(sql, datos)
        cone.commit()
        filas = cursor.rowcount
        cone.close()
        return filas

    # MOSTRAR TODOS LOS REGISTROS

    def recuperar_todos(self):
        cone = self.abrir()
        cursor = cone.cursor()
        cursor.execute("SELECT * FROM libros")
        registros = cursor.fetchall()
        cone.close()
        return registros


class FormularioLibros:
    def __init__(self):
        self.libro = Libros()
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Libros")
        self.ventana.geometry("800x600")
        self.ventana.configure(bg="#F0F4F8")

        self.cuaderno = ttk.Notebook(self.ventana)
        self.cuaderno.pack(fill="both", expand=True)

        # Pestañas
        self.frame_alta = ttk.Frame(self.cuaderno)
        self.frame_consulta = ttk.Frame(self.cuaderno)
        self.frame_modificacion = ttk.Frame(self.cuaderno)
        self.frame_baja = ttk.Frame(self.cuaderno)
        self.frame_listado = ttk.Frame(self.cuaderno)

        self.cuaderno.add(self.frame_alta, text="Registrar Libro")
        self.cuaderno.add(self.frame_consulta, text="Consultar Libro")
        self.cuaderno.add(self.frame_modificacion, text="Modificar Libro")
        self.cuaderno.add(self.frame_baja, text="Eliminar Libro")
        self.cuaderno.add(self.frame_listado, text="Listado General")

        self.form_alta()
        self.form_consulta()
        self.form_modificacion()
        self.form_baja()
        self.form_listado()

        self.ventana.mainloop()

    # FORMULARIO DE ALTA

    def form_alta(self):
        self.id = tk.StringVar()
        self.titulo = tk.StringVar()
        self.autor = tk.StringVar()
        self.publicacion = tk.StringVar()
        self.precio = tk.StringVar()

        ttk.Label(self.frame_alta, text="Book ID:").grid(column=0, row=0, padx=10, pady=10, sticky="w")
        ttk.Entry(self.frame_alta, textvariable=self.id).grid(column=1, row=0)

        ttk.Label(self.frame_alta, text="Título:").grid(column=0, row=1, padx=10, pady=10, sticky="w")
        ttk.Entry(self.frame_alta, textvariable=self.titulo).grid(column=1, row=1)

        ttk.Label(self.frame_alta, text="Autor:").grid(column=0, row=2, padx=10, pady=10, sticky="w")
        ttk.Entry(self.frame_alta, textvariable=self.autor).grid(column=1, row=2)

        ttk.Label(self.frame_alta, text="Año de Publicación:").grid(column=0, row=3, padx=10, pady=10, sticky="w")
        ttk.Entry(self.frame_alta, textvariable=self.publicacion).grid(column=1, row=3)

        ttk.Label(self.frame_alta, text="Precio:").grid(column=0, row=4, padx=10, pady=10, sticky="w")
        ttk.Entry(self.frame_alta, textvariable=self.precio).grid(column=1, row=4)

        ttk.Button(self.frame_alta, text="Registrar", command=self.agregar_libro).grid(column=1, row=5, pady=15)

    def agregar_libro(self):
        try:
            datos = (
                self.id.get().strip(),
                self.titulo.get().strip(),
                self.autor.get().strip(),
                self.publicacion.get().strip(),
                self.precio.get().strip()
            )

            if any(campo == "" for campo in datos):
                mb.showwarning("Campos vacíos", "Todos los campos son obligatorios.")
                return

            self.libro.alta(datos)
            mb.showinfo("Éxito", f"Libro registrado correctamente.")
            self.limpiar_formulario_alta()

        except Exception as e:
            mb.showerror("Error", f"No se pudo registrar el libro.\n{e}")

    def limpiar_formulario_alta(self):
        self.id.set("")
        self.titulo.set("")
        self.autor.set("")
        self.publicacion.set("")
        self.precio.set("")

    # FORMULARIO DE CONSULTA

    def form_consulta(self):
        self.id_consulta = tk.StringVar()

        ttk.Label(self.frame_consulta, text="Book ID:").grid(column=0, row=0, padx=10, pady=10)
        ttk.Entry(self.frame_consulta, textvariable=self.id_consulta).grid(column=1, row=0)
        ttk.Button(self.frame_consulta, text="Consultar", command=self.consultar_libro).grid(column=1, row=1, pady=10)

        self.txt_resultado = st.ScrolledText(self.frame_consulta, width=60, height=15)
        self.txt_resultado.grid(column=0, row=2, columnspan=2, pady=10)

    def consultar_libro(self):
        datos = (self.id_consulta.get(),)
        registros = self.libro.consulta(datos)
        self.txt_resultado.delete("1.0", tk.END)
        if len(registros) > 0:
            for fila in registros:
                self.txt_resultado.insert(
                    tk.END,
                    f"ID: {fila[0]}\nTítulo: {fila[1]}\nAutor: {fila[2]}\nPublicación: {fila[3]}\nPrecio: ${fila[4]}\n\n"
                )
        else:
            mb.showinfo("Sin resultados", "No se encontró ningún libro con ese ID.")
        self.id_consulta.set("")

    # FORMULARIO DE MODIFICACIÓN

    def form_modificacion(self):
        self.id_mod = tk.StringVar()
        self.titulo_mod = tk.StringVar()
        self.autor_mod = tk.StringVar()
        self.publicacion_mod = tk.StringVar()
        self.precio_mod = tk.StringVar()

        etiquetas = ["Book ID:", "Título:", "Autor:", "Año de Publicación:", "Precio:"]
        for i, texto in enumerate(etiquetas):
            ttk.Label(self.frame_modificacion, text=texto).grid(column=0, row=i, padx=10, pady=10, sticky="w")

        ttk.Entry(self.frame_modificacion, textvariable=self.id_mod).grid(column=1, row=0)
        ttk.Entry(self.frame_modificacion, textvariable=self.titulo_mod).grid(column=1, row=1)
        ttk.Entry(self.frame_modificacion, textvariable=self.autor_mod).grid(column=1, row=2)
        ttk.Entry(self.frame_modificacion, textvariable=self.publicacion_mod).grid(column=1, row=3)
        ttk.Entry(self.frame_modificacion, textvariable=self.precio_mod).grid(column=1, row=4)

        ttk.Button(self.frame_modificacion, text="Modificar", command=self.modificar_libro).grid(column=1, row=5, pady=15)

    def modificar_libro(self):
        datos = (
            self.titulo_mod.get(),
            self.autor_mod.get(),
            self.publicacion_mod.get(),
            self.precio_mod.get(),
            self.id_mod.get()
        )
        try:
            filas = self.libro.modificacion(datos)
            if filas > 0:
                mb.showinfo("Éxito", "Libro modificado correctamente.")
                self.limpiar_formulario_mod()
            else:
                mb.showwarning("Aviso", "No se encontró el libro con ese ID.")
        except Exception as e:
            mb.showerror("Error", f"No se pudo modificar el libro.\n{e}")

    def limpiar_formulario_mod(self):
        self.id_mod.set("")
        self.titulo_mod.set("")
        self.autor_mod.set("")
        self.publicacion_mod.set("")
        self.precio_mod.set("")

    # FORMULARIO DE BAJA

    def form_baja(self):
        self.id_baja = tk.StringVar()
        ttk.Label(self.frame_baja, text="Book ID:").grid(column=0, row=0, padx=10, pady=10)
        ttk.Entry(self.frame_baja, textvariable=self.id_baja).grid(column=1, row=0)
        ttk.Button(self.frame_baja, text="Eliminar", command=self.eliminar_libro).grid(column=1, row=1, pady=10)

    def eliminar_libro(self):
        datos = (self.id_baja.get(),)
        try:
            filas = self.libro.baja(datos)
            if filas > 0:
                mb.showinfo("Éxito", "Libro eliminado correctamente.")
                self.id_baja.set("")
            else:
                mb.showwarning("Aviso", "No se encontró ningún libro con ese ID.")
        except Exception as e:
            mb.showerror("Error", f"No se pudo eliminar el libro.\n{e}")

    # LISTADO GENERAL

    def form_listado(self):
        ttk.Button(self.frame_listado, text="Actualizar Listado", command=self.mostrar_todos).pack(pady=10)
        self.txt_listado = st.ScrolledText(self.frame_listado, width=80, height=25)
        self.txt_listado.pack(pady=10)

    def mostrar_todos(self):
        registros = self.libro.recuperar_todos()
        self.txt_listado.delete("1.0", tk.END)
        if len(registros) > 0:
            for fila in registros:
                self.txt_listado.insert(
                    tk.END,
                    f"ID: {fila[0]} | Título: {fila[1]} | Autor: {fila[2]} | Publicación: {fila[3]} | Precio: ${fila[4]}\n{'-'*80}\n"
                )
        else:
            self.txt_listado.insert(tk.END, "No hay libros registrados.\n")


if __name__ == "__main__":
    FormularioLibros()