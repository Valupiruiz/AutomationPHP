from dominio.redondeo import Redondeo
from dominio.ciclo_lectivo import CicloLectivo


class Institucion:
    def __init__(self, nombre: str, nombre_sistema: str, sub_colegio: str, redondeo: Redondeo, promedio_final: Redondeo, apodo: str):
        self.nombre = nombre
        self.nombre_sistema = nombre_sistema
        self.sub_colegio = sub_colegio
        self.redondeo = redondeo
        self.promedio_final = promedio_final
        self.ciclo_lectivo = None
        self.apodo = apodo

    def adjuntar_ciclo_lectivo(self, ciclo: CicloLectivo):
        self.ciclo_lectivo = ciclo
