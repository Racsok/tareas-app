import tkinter as tk
from tkinter import ttk

from ui.ui_ventana_principal import UiVentanaPrincipla
from vista.ventana_crear_tarea import VistaCrearTarea
from vista.ventana_tarea import VistaTarea

class Ventana(tk.Tk):
    def __init__(self, control) -> None:
        super().__init__()
        self.title("Flujo de trabajo")
        self.geometry("500x500")
        self.configure(bg="#f0f0f0")
        self.control = control

        # Frame de botones superiores
        frame_menu = tk.Frame(self, bg="#ffffff", borderwidth=1, relief="groove", pady=15, padx=15)
        frame_menu.pack(fill="x")

        # Frame para botones de navegación
        ttk.Button(frame_menu, text="Pendientes", command=self.mostrar_tareas).grid(column=0, row=0, padx=5)
        ttk.Button(frame_menu, text="Completadas", command=lambda :self.mostrar_tareas("completada")).grid(column=1, row=0, padx=5)
        ttk.Button(frame_menu, text="+ Nueva Tarea", command=self.crear_tarea).grid(column=2, row=0, padx=20)


        # Crear un contenedor principal para el área de scroll
        self.main_container = tk.Frame(self, bg="#f0f0f0")
        self.main_container.pack(fill="both", expand=True)
        # Crear el Canvas y # 3. Crear el Scrollbar vinculado al Canvas
        self.canvas = tk.Canvas(self.main_container, bg="#f0f0f0", highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar = ttk.Scrollbar(self.main_container, orient="vertical", command=self.canvas.yview)
        scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        #Contenedor Tareas
        self.contenedor_tareas = tk.Frame(self.canvas, bg="#f0f0f0", padx=10, pady=10)
        self.contenedor_tareas.pack(fill="both", expand=True)

        # Meter el frame dentro del canvas
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.contenedor_tareas, anchor="nw")
        # Configurar que el frame interno se estire al ancho del canvas
        self.contenedor_tareas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig(self.canvas_frame, width=e.width))
        # self.canvas.bind_all("<MouseWheel>", lambda e: self.canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

        #primera carga de tareas
        self.mostrar_tareas()


    def crear_tarea(self):
        crear_tarea = VistaCrearTarea(self, self.control)
        crear_tarea.grab_set() # bloquea la ventana principal
        self.wait_window(crear_tarea)
        data = crear_tarea.data
        if not data:
            return
        self.control.crear_tarea(data.get("titulo"), data.get("descripcion"), data.get("prioridad"), data.get("ent_fecha"))
        self.mostrar_tareas()

    def ver_tarea(self, Tarea):
        ventana_tarea = VistaTarea(self, Tarea)
        ventana_tarea.update_idletasks() # pide esperar a que termine de cargar la ventana
        ventana_tarea.grab_set()
        self.wait_window(ventana_tarea)
        cambio = False
        if ventana_tarea.data != None and ventana_tarea.data.get("evento") == "eliminar":
            tarea = ventana_tarea.data.get("tarea")
            cambio = self.control.eliminar_tarea(tarea)
        
        if ventana_tarea.data != None and ventana_tarea.data.get("evento") == "actualizar":
            data = ventana_tarea.data
            cambio = self.control.actualizar_tarea(data.get("tarea"), data.get("titulo"), data.get("descripcion"), data.get("prioridad"), data.get("ent_fecha"))

        if ventana_tarea.data != None and ventana_tarea.data.get("evento") == "alternar_estado":
            tarea = ventana_tarea.data.get("tarea")
            cambio = self.control.alternar_estado_tarea(tarea)
             
        if cambio:
            self.mostrar_tareas()
        
    def mostrar_tareas(self, *args):
        #limpiar widget contenedor
        for widget in self.contenedor_tareas.winfo_children():
            widget.destroy()
        #lista actualizada de tareas
        lista_tareas = self.control.listar_tareas(args)
        ui = UiVentanaPrincipla()
        

        self.contenedor_tareas.columnconfigure(0, weight=1)
        self.contenedor_tareas.columnconfigure(1, weight=1)

        for i, Tarea in enumerate(lista_tareas):
            # Creamos la tarjeta
            tarjeta = ui.crear_tarjeta(self.contenedor_tareas, i, Tarea)

            # agregar funcionalidad con bind para click
            for hijo in tarjeta.winfo_children():
                hijo.bind("<Button-1>", lambda _, tarea=Tarea, t=tarjeta: self.ver_tarea(tarea))
            #agreagr resaltado Usamos t=tarjeta para "congelar" la variable en el lambda
            tarjeta.bind("<Button-1>", lambda _, tarea=Tarea, t=tarjeta: self.ver_tarea(tarea))
            tarjeta.bind("<Enter>", lambda _, t=tarjeta: t.state(['active']))
            tarjeta.bind("<Leave>", lambda _, t=tarjeta: t.state(['!active']))

