def graficar(peores_individuos, mejores_individuos, medias):
    generacion = range(len(peores_individuos))
    plt.plot(generacion, peores_individuos, label="Peor Individuo")
    plt.plot(generacion, mejores_individuos, label="Mejor Individuo")
    plt.plot(generacion, medias, label="Media")

    plt.xlabel("Generación")
    plt.ylabel("Fitness")
    plt.title("Evolución del Fitness")
    plt.legend()
    plt.show()
    
def mostrar_tabla_alimentos(datos):
    ventana = tk.Tk()
    ventana.title("Tabla de Alimentos")

    tabla = ttk.Treeview(ventana)
    tabla["columns"] = ["Nombre", "Categoría", "Energía", "Proteína", "Grasa", "Calcio", "Hierro", "Vitamina A", "Tiamina", "Riboflavina", "Niacina", "Folato", "Vitamina C", "Objetivo"]

    # Ajustar el ancho de las columnas
    tabla.column("#0", width=0)  # Columna de índices
    for columna in tabla["columns"]:
        tabla.column(columna, width=80)  # Ajustar el ancho de las columnas de datos

    tabla.heading("#0", text="")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Categoría", text="Categoría")
    tabla.heading("Energía", text="Energía")
    tabla.heading("Proteína", text="Proteína")
    tabla.heading("Grasa", text="Grasa")
    tabla.heading("Calcio", text="Calcio")
    tabla.heading("Hierro", text="Hierro")
    tabla.heading("Vitamina A", text="Vitamina A")
    tabla.heading("Tiamina", text="Tiamina")
    tabla.heading("Riboflavina", text="Riboflavina")
    tabla.heading("Niacina", text="Niacina")
    tabla.heading("Folato", text="Folato")
    tabla.heading("Vitamina C", text="Vitamina C")
    tabla.heading("Objetivo", text="Objetivo")

    tabla.grid(row=0, column=0)

    for i, dato in enumerate(datos, start=1):
        tabla.insert("", "end", text=str(i), values=dato)

    ventana.mainloop()
