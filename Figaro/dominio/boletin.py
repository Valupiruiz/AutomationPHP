from dominio.curso import Curso
from dominio.usuario import Alumno
from dominio.redondeo import Redondeo
from enum import Enum


class Boletin:
    def __init__(self, curso: Curso):
        self.curso = curso

    def calcular_promedio_alumno(self, alumno: Alumno, periodo: str, redondeo: Redondeo, tipo_promedio: "Promedio"):
        pass


class Promedio(Enum):
    EXACTO = 0
    EV = 1
    FINAL = 2
    DEFINITIVO = 3
