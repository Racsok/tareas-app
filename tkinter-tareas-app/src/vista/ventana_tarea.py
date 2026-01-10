#!/usr/bin/env python3
# Ventana para ver una tarea
import tkinter as tk 
from tkinter import ttk

from tkcalendar import DateEntry
from ui.ui_ventana_tarea import UiVentanaTarea

class VistaTarea(tk.Toplevel):
    def __init__(self, parent, Tarea):
        super().__init__(parent)
        self.tarea = Tarea
        self.data = None
        invr = Tarea.MAPA_PRIO_INVERTIDO
        self.ui = UiVentanaTarea()


        self.title("Tarea")
        self.configure(padx=20, pady=20)

        # --- TÍTULO ---
        ttk.Label(self, text="Título de la Tarea", style="Header.TLabel").pack(anchor="w")
        self.titulo = tk.Entry(self, font=("Arial", 11))
        self.titulo.insert(0, self.tarea.titulo)
        self.titulo.pack(fill="x", pady=(0, 15))

        # --- DESCRIPCIÓN ---
        ttk.Label(self, text="Descripción", style="Header.TLabel").pack(anchor="w")
        self.descripcion = tk.Text(self, height=5, font=("Arial", 11))
        self.descripcion.insert("1.0", self.tarea.descripcion)
        self.descripcion.pack(fill="x", pady=(0, 15))

        # --- FILA PARA PRIORIDAD Y FECHA ---
        meta_frame = ttk.Frame(self)
        meta_frame.pack(fill="x", pady=(0, 20))

        # Prioridad
        prioridad_frame = ttk.Frame(meta_frame)
        prioridad_frame.pack(side="left", fill="x", expand=True)
        ttk.Label(prioridad_frame, text="Prioridad", style="Header.TLabel").pack(anchor="w")
        self.prioridad = ttk.Combobox(prioridad_frame, values=list(self.tarea.MAPA_PRIO.keys()), state="readonly")
        self.prioridad.set(invr[self.tarea.prioridad])
        self.prioridad.pack(anchor="w", padx=(0, 10))

        # Fecha Límite
        fecha_frame = ttk.Frame(meta_frame)
        fecha_frame.pack(side="left", fill="x", expand=True)
        ttk.Label(fecha_frame, text="Fecha Límite", style="Header.TLabel").pack(anchor="w")
        self.ent_fecha = DateEntry(fecha_frame)
        self.ent_fecha.insert(0, self.tarea.fecha_limite)
        self.ent_fecha.pack(anchor="w")

        # --- BOTONES DE ACCIÓN ---
        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill="x", side="bottom", pady=10)

        # Botón Cerrar (Gris)
        self.btn_cerrar = ttk.Button(btn_frame, text="Cerrar", command=self.destroy)
        self.btn_cerrar.pack(side="right", padx=5)

        if not self.tarea.completada:

            # Botón Eliminar (Rojo)
            self.btn_eliminar = ttk.Button(btn_frame, text="Eliminar", style="Danger.TButton", command=self.eliminar)
            self.btn_eliminar.pack(side="left")


            # Botón Actualizar (Azul/Principal)
            self.btn_actualizar = ttk.Button(btn_frame, text="Actualizar Tarea", style="Action.TButton", command=self.actualizar)
            self.btn_actualizar.pack(side="right", padx=5)
            
            # Botón Completar (Verde)
            self.btn_completar = ttk.Button(btn_frame, text="Completar Tarea", style="Success.TButton", command=self.completar)
            self.btn_completar.pack(side="right", padx=5)
        else:

            # Botón Descompletar (Verde)
            self.btn_completar = ttk.Button(btn_frame, text="Completar Tarea", style="Success.TButton", command=self.completar)
            self.btn_completar.pack(side="right", padx=5)


    def eliminar(self):
        self.data = {
                "tarea": self.tarea,
                "evento": "eliminar"
                }
        self.destroy()
    
    def actualizar(self):
        t = self.tarea
        try:
            self.data = {
                    "tarea": self.tarea,
                    "titulo":  self.titulo.get(),
                    "descripcion": self.descripcion.get("1.0", "end-1c"),
                    "prioridad": self.tarea.MAPA_PRIO[f"{self.prioridad.get()}"],
                    "ent_fecha":  self.ent_fecha.get_date(),
                    "evento": "actualizar"
                    }
            if t.titulo != self.data.get("titulo") or t.descripcion != self.data.get("descripcion") or t.prioridad != self.data.get("prioridad") or t.fecha_limite != self.data.get("ent_fecha"):
                self.destroy()
        finally:
            pass
    
    def completar(self):
        self.data = {
                "tarea": self.tarea,
                "evento": "alternar_estado"
                }
        self.destroy()



