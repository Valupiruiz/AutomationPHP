class Curso:
    def __init__(self, nombre: str, division: str):
        self.nombre = nombre
        self.division = division
        self.materias = []
        self.alumnos = []

    def agregar_materias(self, *materias):
        for materia in materias:
            self.materias.append(materia)

    def matricular_alumnos(self, *alumnos):
        for alumno in alumnos:
            self.alumnos.append(alumno)
