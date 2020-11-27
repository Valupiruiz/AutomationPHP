from utils.custom_types import RutaArchivo, T
from typing import List

class Curso:
    def __init__(self, nombre: str, fecha_egreso: str, resolucion: str = None, legajo: bool = False, institucion: str = "SIN RESOLUCION ESPECIFICA",
                 anio_presentacion: str = None, imagenes: List[RutaArchivo] = None):
        self.nombre = nombre
        self.fecha_egreso = fecha_egreso
        self.resolucion = resolucion
        self.legajo = legajo
        self.institucion = institucion
        self.anio_presentacion = anio_presentacion
        self.imagenes = [] if imagenes is None else imagenes

