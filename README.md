# 📝 Tkinter Task Manager

Una aplicación de escritorio moderna y funcional para la gestión de tareas, construida con **Python** y **SQLite**. Este proyecto implementa un sistema de tarjetas con persistencia de datos y priorización visual.


## 🚀 Características principales

* **Gestión Completa (CRUD):** Crea, edita y elimina tareas de forma intuitiva.
* **Persistencia de Datos:** Integración con SQLite para que no pierdas tus tareas al cerrar la app.
* **Priorización Visual:** Sistema de colores inteligente basado en la importancia (de Rojo/Urgente a Verde/Baja).

## 🛠️ Stack Tecnológico

* **Lenguaje:** Python 3.x
* **Interfaz Gráfica:** Tkinter
* **Base de Datos:** SQLite3, SqlAlchemy
* **Arquitectura:** Modular (Separación de lógica de negocio, Vista y control)

## 📂 Estructura del Proyecto

```text
tkinter-tareas-app/
├── requirements.txt
└── src
    ├── control
    │   ├── GestorTareas.py
    ├── db
    │   ├── connection.py
    ├── main.py
    ├── models
    │   └── tarea.py
    ├── pyrightconfig.json
    └── vista
        ├── ventana_crear_tarea.py
        ├── ventana_principal.py
        └── ventana_tarea.py               
```

## ⚙️ Instalación y Uso
Sigue estos pasos para configurar el proyecto en tu entorno local:

1. **Clonar el repositorio:**
```bash
git clone https://github.com/Racsok/tareas-app.git
cd tareas-app
```

2. **Crear un entorno virtual (Recomendado):**
* en **Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```
* En **macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Instalar dependencias:** Una vez activado el entorno virtual, instala los paquetes necesarios:
```bash
pip install -r requirements.txt
```

4. **Ejecutar la aplicación:**
```bash
python3 src/main.py
```
### 2. Crea un archivo `.gitignore`
Para que tu repositorio sea impecable, crea un archivo llamado `.gitignore` en la carpeta raíz (al lado de `README.md`). Esto evitará que subas archivos "basura" o tu base de datos local. 

**Contenido recomendado para tu `.gitignore`:**
```tex
# Ignora cualquier carpeta llamada .venv en cualquier nivel de profundidad
**/.venv/
**/venv/
**/env/

# Ignora archivos de entorno de Python
**/*.py[cod]
**/__pycache__/

# Si usas Node.js en algunos proyectos
**/node_modules/

# Archivos de configuración de editores
.vscode/
.idea/

# Bases de datos SQLite
**/*.sqlite
**/*.db

pyrightconfig.json
```
















