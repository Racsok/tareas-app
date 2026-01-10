#Crea los diseños de la ventana tarea
from tkinter import ttk

class UiVentanaTarea():
    def __init__(self) -> None:
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Estilo para etiquetas de encabezado
        self.style.configure("Header.TLabel", font=("Arial", 10, "bold"), pady=5)

        # Botón Actualizar (Azul)
        self.style.configure("Action.TButton", font=("Arial", 10, "bold"), background="#2196F3", foreground="white")
        self.style.map("Action.TButton", background=[('active', '#1976D2')])

        # Botón Completar/Descompletar (Verde)
        self.style.configure("Success.TButton", font=("Arial", 10, "bold"), background="#4CAF50", foreground="white")
        self.style.map("Success.TButton", background=[('active', '#45a049')])

        # Botón Eliminar (Rojo)
        self.style.configure("Danger.TButton", font=("Arial", 10, "bold"), background="#f44336", foreground="white")
        self.style.map("Danger.TButton", background=[('active', '#d32f2f')])
