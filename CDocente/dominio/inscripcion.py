from typing import List


class Inscripcion:
    def __init__(self, listado: ["Listado"], area: str, cargo: str, asignatura: str, especialidad: str, periodo: str = "Período Ordinario",
                 distrito: List[str] = None):
        self.listado = listado
        self.area = area
        self.cargo = cargo
        self.asignatura = asignatura
        self.especialidad = especialidad
        self.periodo = periodo
        self.distrito = distrito


class Listado:
    INGRESO = "Inscripciones para Ingreso"
    SUPLENCIAS = "Inscripciones para Interinatos y suplencias"
    TITULARES = "Inscripciones para Titulares"
    ASCENSO = "Voluntad de ascenso"







