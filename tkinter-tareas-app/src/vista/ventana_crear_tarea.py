#!/usr/bin/env python3
# Interfaz para crear tarea
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

class VistaCrearTarea(tk.Toplevel):
    def __init__(self, parent, control):
        super().__init__(parent)
        self.prio = control.obtener_prioridad()
        self.data = {}
        self.title("Crear Tarea")
        self.geometry("350x450")
        self.configure(padx=25, pady=20)

        
        # Titulo
        tk.Label(self, text="Título", font=("Arial", 10, "bold")).pack(anchor="w", pady=(0, 5))
        self.titulo = ttk.Entry(self, font=("Arial", 11))
        self.titulo.pack(fill="x", pady=5)

        # Descripción
        tk.Label(self, text="Descripción", font=("Arial", 10, "bold")).pack(anchor="w", pady=(0, 5))
        self.descripcion = ttk.Entry(self, font=("Arial", 11))
        self.descripcion.pack(fill="x", pady=5)

        # Prioridad
        tk.Label(self, text="Prioridad", font=("Arial", 10, "bold")).pack(anchor="w", pady=(0, 5))
        self.prioridad = ttk.Combobox(self, values=list(self.prio.keys()), state="readonly")
        self.prioridad.set("Media (2)") # Valor por defecto
        self.prioridad.pack(fill="x", pady=(0, 15))
        
        # Fecha Limite
        tk.Label(self, text="Fecha límite", font=("Arial", 10, "bold")).pack(anchor="w", pady=(0, 5))
        self.ent_fecha = DateEntry(self, width=12, background='darkblue', foreground='white', borderwidth=2, font=("Arial", 10))
        self.ent_fecha.pack(fill="x", pady=(0, 25))

        # Boton Crear
        btn_crear = tk.Button(self, text="＋ Crear Tarea", bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), relief="flat", padx=10, pady=8, command=self.guardar_datos)
        btn_crear.pack(fill="x")

    def guardar_datos(self):
        try:
            self.data = {
                    "titulo":  self.titulo.get(),
                    "descripcion": self.descripcion.get(),
                    "prioridad": self.prio[f"{self.prioridad.get()}"],
                    "ent_fecha":  self.ent_fecha.get_date(), 
                    "evento": "guardar",
                    }
            self.destroy()
        finally:
            pass




