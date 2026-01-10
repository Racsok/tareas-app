#!/usr/bin/env python3
# Interfaz para crear tarea
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from ui.ui_ven_crear_tarea import UiVistaCrearTarea

class VistaCrearTarea(tk.Toplevel):
    def __init__(self, parent, control):
        super().__init__(parent)
        self.prio = control.obtener_prioridad()
        self.data = {}
        self.ui = UiVistaCrearTarea()
        self.title("Crear Tarea")
        self.geometry("350x450")
        self.configure(padx=25, pady=20)

        
        # Titulo
        ttk.Label(self, text="Título", style="Header.TLabel").pack(anchor="w", pady=(0, 5))
        self.titulo = ttk.Entry(self, font=("Arial", 11))
        self.titulo.pack(fill="x", pady=5)

        # Descripción
        ttk.Label(self, text="Descripción", style="Header.TLabel").pack(anchor="w", pady=(0, 5))
        self.descripcion = tk.Text(self, height=5, font=("Arial", 11))
        self.descripcion.pack(fill="x", pady=5)

        # Prioridad
        ttk.Label(self, text="Prioridad", style="Header.TLabel").pack(anchor="w", pady=(0, 5))
        self.prioridad = ttk.Combobox(self, values=list(self.prio.keys()), state="readonly")
        self.prioridad.set("Media (2)") # Valor por defecto
        self.prioridad.pack(fill="x", pady=(0, 15))
        
        # Fecha Limite
        ttk.Label(self, text="Fecha límite", style="Header.TLabel").pack(anchor="w", pady=(0, 5))
        self.ent_fecha = DateEntry(self, width=12, background='darkblue', foreground='white', borderwidth=2, font=("Arial", 10))
        self.ent_fecha.pack(fill="x", pady=(0, 25))

        # Boton Crear
        btn_crear = ttk.Button(self, text="＋ Crear Tarea", style="Success.TButton", command=self.guardar_datos)
        btn_crear.pack(fill="x", ipady=5)

    def guardar_datos(self):
        try:
            if not self.titulo.get():
                messagebox.showinfo("!ups", "No se puede crear una tarea con el tirulo vacio")
            else:
                self.data = {
                        "titulo":  self.titulo.get(),
                        "descripcion": self.descripcion.get("1.0", "end-1c"),
                        "prioridad": self.prio[f"{self.prioridad.get()}"],
                        "ent_fecha":  self.ent_fecha.get_date(), 
                        "evento": "guardar",
                        }
                self.destroy()
        finally:
            pass




