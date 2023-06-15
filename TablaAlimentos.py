import tkinter as tk
import tkinter.ttk as ttk

class TablaAlimentos:
    def __init__(self, datos):
        self.datos = datos
        self.ventana = tk.Tk()
        self.ventana.title("Tabla de Alimentos")

        self.tabla = ttk.Treeview(self.ventana)
        self.tabla["columns"] = ["Nombre", "Categoría", "Energía", "Proteína", "Grasa", "Calcio", "Hierro", "Vitamina A", "Tiamina", "Riboflavina", "Niacina", "Folato", "Vitamina C", "Objetivo", "Fitness"]
        self.tabla.grid(row=0, column=0)

        # Ajustar el ancho de las columnas
        self.tabla.column("#0", width=0)  # Columna de índices
        for columna in self.tabla["columns"]:
            self.tabla.column(columna, width=100)  # Ajustar el ancho de las columnas de datos

        for i, dato in enumerate(self.datos, start=1):
            if len(dato) >= 15:
                self.tabla.insert("", "end", text=str(i), values=dato[:13] + dato[14:])  # Excluye el elemento de índice 13
            else:
                # Si los datos no tienen suficientes elementos, puedes realizar alguna acción aquí, como omitir los datos o mostrar un mensaje de error
                pass

    def mostrar(self):
        self.ventana.mainloop()