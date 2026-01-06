import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, scoped_session

class DatabaseConnection:
    def __init__(self, db_name: str = "Tarea.sqlite"):
        self.bd_url = f"sqlite:///{db_name}"
        try:
            #es el punto de entrada principal para interactuar con una base de datos en Python
            self.engine = create_engine(self.bd_url, connect_args={"check_same_thread": False}) # para SQLite y multihilo
            # Fabricante de Sesiones: Es un objeto que produce instancias de Session. No es la sesión en sí, sino la "fábrica" de donde se obtienen las sesiones.
            self._session_factory = sessionmaker(bind=self.engine, autocommit=False, autoflush=False)

            self.Session = scoped_session(self._session_factory)
        except SQLAlchemyError as e:
            print(f"Error al conectar la base de datos: {e}")

    def get_session(self):
        return self.Session

    def crear_tablas(self, Base):
        # Esto es lo que realmente crea el archivo .sqlite si no existe
        Base.metadata.create_all(self.engine)
        
        

        
