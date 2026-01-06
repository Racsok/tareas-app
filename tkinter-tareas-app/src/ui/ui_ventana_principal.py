#Crea los diseños de la ventana principal
from tkinter import ttk

class UiVentanaPrincipla():
    def __init__(self) -> None:
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # 1. Configuración de los tres estilos para tarjetas según prioridad
        # Prioridad Alta (Rojo suave)
        # Prioridad Media (Amarillo/Naranja suave)
        # Prioridad Baja (Azul suave)
        self.style.configure("alta.tarjeta.TFrame", background="#ffebee", relief="flat", borderwidth=1, padding=10)
        self.style.configure("media.tarjeta.TFrame", background="#fff9c4", relief="flat", borderwidth=1, padding=10)
        self.style.configure("baja.tarjeta.TFrame", background="#e3f2fd", relief="flat", borderwidth=1, padding=10)


        # self.style.configure("tarjeta.TFrame", background = "white", relief="flat", borderwidth=1, padding=10)
        self.style.map("tarjeta.TFrame",background=[('active', '#eeeeee'), ('pressed', '#e0e0e0')],relief=[('pressed', 'sunken')])

        self.style.configure("titulo.TLabel", font=("Arial", 9, "bold"),  foreground="#333333")
        self.style.configure("descripcion.TLabel", font=("Arial", 8), foreground="#666666")

    def crear_tarjeta(self, contenedor, i, tarea_obj):
        if tarea_obj.prioridad == 1:
            estilo_prioridad = "alta.tarjeta.TFrame"
            color_fondo = "#ffebee"
        elif tarea_obj.prioridad == 2:
            estilo_prioridad = "media.tarjeta.TFrame"
            color_fondo = "#fff9c4"
        else:
            estilo_prioridad = "baja.tarjeta.TFrame"
            color_fondo = "#e3f2fd"


        tarjeta = ttk.Frame(contenedor, style=estilo_prioridad)
        tarjeta.grid(row=i // 2, column=i % 2, padx=10, pady=10, sticky="nsew")

        # Dentro de la tarjeta
        ttk.Label(tarjeta, text=tarea_obj.titulo.upper(), style="titulo.TLabel", background=color_fondo).pack(anchor="w", padx=15, pady=(15, 5))
        ttk.Label(tarjeta, text=tarea_obj.descripcion, style="descripcion.TLabel", background=color_fondo).pack(anchor="w", padx=15, pady=(0, 15))
        return tarjeta


