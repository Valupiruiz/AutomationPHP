class Materia:
    def __init__(self, nombre: str, opcion: str):
        self.nombre = nombre
        self.opcion = opcion
        self.alumnos = []
        self.evaluaciones = []

    def inscribir_alumnos(self, *alumnos):
        for alumno in alumnos:
            self.alumnos.append(alumno)

    def agendar_evaluaciones(self, *evaluaciones):
        for evaluacion in evaluaciones:
            self.evaluaciones.append(evaluacion)
