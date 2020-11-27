from typing import List
from dominio.curso import Curso


class CicloLectivo:
    def __init__(self, nombre: str, periodos: List[str]):
        self.nombre = nombre
        self.periodos = periodos
        self.cursos = []  # List[Curso]

    def agregar_cursos(self, *cursos):
        for curso in cursos:
            self.cursos.append(curso)
