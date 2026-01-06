#  Esta es la clase que gestiona las tareas
from models.tarea import Tarea
from utiles.logger import config_logger

logger = config_logger(__name__)

class GestorTareas:
    def __init__(self, db) -> None:
        self.db = db
        self.db.crear_tablas(Tarea)
        self.session = self.db.get_session()
        
        self.tareas_pendientes = []
        self.tareas_completadas = []

        logger.info("Va a cargar las tareas")
        self.cargar_desde_db()

    def crear_tarea(self, titulo, descripcion, prioridad, fecha):
        try:
            logger.debug(f"Intentando crear tarea: {titulo} con prioridad {prioridad}")
            nueva_tarea = Tarea(titulo=titulo, descripcion=descripcion, prioridad=prioridad, fecha_limite=fecha) 
            #  Agregar a la lista
            self.tareas_pendientes.append(nueva_tarea) 
            
            #  Agregar a la BD
            self.session.add(nueva_tarea)
            self.session.commit()
            logger.info(f"Tarea '{titulo}' creada exitosamente con ID: {nueva_tarea.id}")
        except Exception as e:
            logger.error(f"Error al crear la tarea '{titulo}': {e}", exc_info=True)
            raise e 

    def eliminar_tarea(self, tarea_obj):
        try:
            logger.debug(f"Intentando crear tarea: {tarea_obj.titulo}")
            if tarea_obj in self.tareas_pendientes:
                # Eliminar de la lista
                self.tareas_pendientes.remove(tarea_obj)

                # Eliminar de la BD
                self.session.delete(tarea_obj)
                self.session.commit()
                return True
            logger.warning(f"Intento de eliminar tarea inexistente: {tarea_obj}")
            return False
        except Exception as e:
            logger.error(f"Fallo crítico al eliminar tarea: {e}")
            raise e    

    def actualizar_tarea(self, tarea_obj, titulo, descripcion, prioridad, fecha):
        try:
            logger.debug(f"Intentando actualizar tarea: {tarea_obj.titulo}")
            tarea_obj.titulo = titulo
            tarea_obj.descripcion = descripcion
            tarea_obj.prioridad = prioridad
            tarea_obj.fecha_limite = fecha


            # Persistir
            logger.info(f"Tarea '{titulo}' actualizada exitosamente con ID: {tarea_obj.id}")
            self.session.commit()
            return True

        except Exception as e:
            logger.error(f"Error al actualizar la tarea '{titulo}': {e}", exc_info=True)
            raise e

    def alternar_estado_tarea(self, tarea_obj):
        try:
            logger.debug(f"Función completar tarea: {tarea_obj.titulo}")
            if tarea_obj.completada:
                logger.debug(f"Función Descompletar tarea: {tarea_obj.titulo}")
                tarea_obj.completada = False
                self.session.commit()
                self.tareas_pendientes.append(tarea_obj)
                self.tareas_completadas.remove(tarea_obj)
                logger.debug(f"Tarea: {tarea_obj.titulo}, se guardo como incompleta")
                return True
            tarea_obj.completada = True
            self.session.commit()
            self.tareas_pendientes.remove(tarea_obj)
            self.tareas_completadas.append(tarea_obj)
            logger.debug(f"Tarea: {tarea_obj.titulo}, se guardo como completada")
            return True

        except Exception as e:
            logger.error(f"Error al cabiar de estado la tarea '{tarea_obj.titulo}': {e}", exc_info=True)
            raise e

    def listar_tareas(self, tupla):
        self.ordenar_tareas()
        return self.tareas_pendientes if tupla == () else self.tareas_completadas

    def ordenar_tareas(self):
        self.tareas_pendientes.sort(key=lambda Tarea: Tarea.prioridad)
        self.tareas_completadas.sort(key=lambda Tarea: Tarea.prioridad)


    def cargar_desde_db(self):
        try:
            logger.debug(f"Cargando tareas desde la base de datos")
            todas = self.session.query(Tarea).all()
            self.tareas_pendientes = [t for t in todas if not t.completada]
            self.tareas_completadas = [t for t in todas if t.completada]
        except Exception as e:
            logger.error(f"Error al Cargaro tareas desde la base de datos: {e}", exc_info=True)
            raise e

    def obtener_prioridad(self):
        return Tarea.MAPA_PRIO

