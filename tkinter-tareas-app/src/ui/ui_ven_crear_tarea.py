#Crea los diseños de la ventana crear tarea
from tkinter import ttk

class UiVistaCrearTarea():
    def __init__(self) -> None:
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        # Configuración de estilos
        self.style.configure("Form.TFrame", background="#ffffff")
        self.style.configure("Header.TLabel", font=("Arial", 10, "bold"), background="#ffffff", foreground="#333333")

        # Estilo para el botón (verde)
        self.style.configure("Success.TButton", font=("Arial", 11, "bold"), foreground="white", background="#4CAF50")
        self.style.map("Success.TButton", background=[('active', '#45a049')])
