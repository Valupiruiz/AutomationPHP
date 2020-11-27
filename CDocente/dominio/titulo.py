from utils.custom_types import RutaArchivo
from typing import List


class Titulo:
    def __init__(self, nombre: str, fecha_emision: str, nivel: "Nivel", resolucion: str = None, legajo: bool = False, procedencia: str = "SIN RESOLUCION ESPECIFICA",
                 anio_presentacion: str = None, imagenes: List[RutaArchivo] = None, sin_secundario: bool = False):
        self.nombre = nombre
        self.fecha_emision = fecha_emision
        self.nivel = nivel
        self.resolucion = resolucion
        self.legajo = legajo
        self.procedencia = procedencia
        self.anio_presentacion = anio_presentacion
        self.imagenes = [] if imagenes is None else imagenes
        self.sin_secundario = sin_secundario



class Nivel:
    SECUNDARIO = "Secundario"
    TERCIARIO_UNIVERSITARIO = "Terciario o Universitario"
    POSGRADO = "Posgrado"
    MAESTRIA_DOCTORADO = "Maestría y Doctorado"



