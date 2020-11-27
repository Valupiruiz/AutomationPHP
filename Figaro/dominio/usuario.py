from dominio.institucion import Institucion
from typing import List


class Usuario(object):
    def __init__(self, username: str, nombre: str, apellido: str, perfil=None, password: str = "BNyl7e"):
        self.username = username
        self.password = password
        self.nombre = nombre
        self.apellido = apellido
        self._perfil = perfil
        self.institucion = None

    @property
    def perfil(self):
        return self._perfil

    @perfil.setter
    def perfil(self, valor):
        self._perfil = valor

    def get_sub_colegio_select(self):
        return f"{self.perfil} - {self.institucion.nombre_sistema} - {self.institucion.sub_colegio}"

    def inscribir_en_institucion(self, institucion: Institucion):
        self.institucion = institucion


class Administrador(Usuario):
    def __init__(self, username, nombre, apellido):
        super().__init__(username, nombre, apellido, perfil=Perfiles.ADMINISTRADOR)


class Docente(Usuario):
    def __init__(self, username, nombre, apellido):
        super().__init__(username, nombre, apellido, perfil=Perfiles.DOCENTE)


class Alumno(Usuario):
    def __init__(self, username, nombre, apellido):
        super().__init__(username, nombre, apellido, perfil=Perfiles.ALUMNO)


class Padre(Usuario):
    def __init__(self, username, nombre, apellido):
        super().__init__(username, nombre, apellido, perfil=Perfiles.PADRE)


class Perfiles:
    ADMINISTRADOR = "Administrador"
    DOCENTE = "Docente"
    ALUMNO = "Alumno"
    PADRE = "Padre"
