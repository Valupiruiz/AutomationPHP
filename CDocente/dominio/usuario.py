from typing import List
from utils.custom_types import RutaArchivo, T
from .inscripcion import Inscripcion
from dominio.titulo import Titulo
from .curso import Curso


class Usuario:
    def __init__(self, nombre: str, apellido: str, mail: str = "test5.cys@bue.edu.ar", contrasenia: str = "pruebascys",
                 perfil: str = ""):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.contrasenia = contrasenia
        self.perfil = perfil


class Docente(Usuario):
    def __init__(self, nombre: str, apellido: str, mail: str = "test5.cys@bue.edu.ar", contrasenia: str = "pruebascys",
                 fecha_nacimiento: str = None, sexo: str = None, tipo_dni: str = None, nro_dni: str = None, cuil: str = None,
                 provincia: str = None, localidad: str = None, calle: str = None, piso: str = None, departamento: str = None,
                 cod_postal: str = None, mail_temportal: str = None, contrasenia_temporal: str = None,
                 imagenes_dni: List[RutaArchivo] = None, imagen_cuil: RutaArchivo = None,
                 inscripciones: List[Inscripcion] = None, titulos: List[Titulo] = None, cursos: List[Curso] = None,
                 antecedentes: List[T] = None, otros=None, servicios=None, celular = None):
        super().__init__(nombre, apellido, mail, contrasenia, perfil=Perfil.DOCENTE)
        # region datos personales
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.tipo_dni = tipo_dni
        self.nro_dni = nro_dni
        self.imagenes_dni = [] if imagenes_dni is None else imagenes_dni
        self.cuil = cuil
        self.imagen_cuil = "" if imagen_cuil is None else imagen_cuil
        # endregion
        # region Direccion personal
        self.provincia = provincia
        self.localidad = localidad
        self.calle = calle
        self.piso = piso
        self.departamento = departamento
        self.cod_postal = cod_postal
        self.celular = celular
        # endregion
        # region Email y contrasenia
        self.mail_temportal = mail_temportal
        self.contrasenia_temporal = contrasenia_temporal
        #region inscripciones
        self.inscripciones = inscripciones
        self.titulos = titulos
        self.cursos = cursos
        self.antecedentes = [] if antecedentes is None else antecedentes
        self.otros = [] if otros is None else otros
        self.servicios = [] if servicios is None else servicios
        # endregion

class Perfil:
    DOCENTE = "Docente"
    ADMINISTRADOR = "Administrador"
    VALIDADOR = "Validador"