class Evaluacion:
    def __init__(self, nombre: str, periodo: str, tipo: "TipoEvaluacion", fecha: str, ponderacion: "Ponderacion",
                 porcentaje: int = 0, excluida: bool = False):
        self.nombre = nombre
        self.periodo = periodo
        self.fecha = fecha
        self.tipo = tipo
        self.ponderacion = ponderacion
        self.excluida = excluida
        if ponderacion == Ponderacion.MANUAL and porcentaje > 0:
            self.porcentaje = porcentaje


class TipoEvaluacion:
    NUMERICA = "Numérica"
    CONCEPTUAL = "Conceptual"


class Ponderacion:
    AUTOMATICA = "Automatica"
    MANUAL = "Manual"
