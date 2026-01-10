#!/usr/bin/env python3
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, scoped_session
import os
import sys

from utiles.logger import config_logger

logger = config_logger(__name__)

class DatabaseConnection:
    def __init__(self, db_name: str = "Tarea.sqlite"):
        # 1. Determinar una carpeta persistente
        if getattr(sys, 'frozen', False):
            # Si es un ejecutable, usamos la carpeta del usuario
            # En Windows: C:/Users/Nombre/AppData/Roaming/TuApp
            home_dir = os.path.expanduser("~")
            base_dir = os.path.join(home_dir, ".mi_app_tareas")
        else:
            # Si es desarrollo, usamos la carpeta src/db/ como ya tienes
            base_dir = os.path.dirname(os.path.abspath(__file__))

        # 2. Crear la carpeta si no existe
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)

        ruta_db = os.path.join(base_dir, db_name)
        self.bd_url = f"sqlite:///{ruta_db}"
        try:
            #es el punto de entrada principal para interactuar con una base de datos en Python
            self.engine = create_engine(self.bd_url, connect_args={"check_same_thread": False}) # para SQLite y multihilo
            # Fabricante de Sesiones: Es un objeto que produce instancias de Session. No es la sesión en sí, sino la "fábrica" de donde se obtienen las sesiones.
            self._session_factory = sessionmaker(bind=self.engine, autocommit=False, autoflush=False)

            self.Session = scoped_session(self._session_factory)
        except SQLAlchemyError as e:
            logger.error(f"Error al conectar la base de datos: {e}")

    def get_session(self):
        return self.Session

    def crear_tablas(self, Base):
        # Esto es lo que realmente crea el archivo .sqlite si no existe
        Base.metadata.create_all(self.engine)
        
        

        
