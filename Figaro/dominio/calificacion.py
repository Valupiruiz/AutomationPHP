from dominio.evaluacion import Evaluacion
from dominio.usuario import Alumno
from decimal import Decimal


class Calificacion:
    def __init__(self, evaluacion: Evaluacion, nota: Decimal, alumno: Alumno, observaciones: str = '',
                 ausente: bool = False):
        self.evaluacion = evaluacion
        self.nota = nota
        self.alumno = alumno
        self.observaciones = observaciones
        self.ausente = ausente
