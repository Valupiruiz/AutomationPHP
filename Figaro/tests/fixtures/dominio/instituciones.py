import pytest
from tests.fixtures import *


# region Holy Cross fixtures
@pytest.fixture
def hc_institucion():
    return Institucion('Holy Cross', 'Holy Cross', 'Secundario Varones', CincuentaArriba(), CincuentaArriba(), 'hcs')

@pytest.fixture
def hc_ciclo_2020():
    return CicloLectivo('2020', ['Trim. 1', 'Trim. 2', 'Trim. 3'])

@pytest.fixture
def hc_curso_2do_u():
    return Curso('2do. Secundaria', 'U',)


@pytest.fixture
def hc_materia_biologia_u():
    return Materia('BIOLOGÍA', 'U')


@pytest.fixture
def hc_crear_evaluaciones(hc_institucion, hc_ciclo_2020, hc_curso_2do_u, hc_materia_biologia_u):
    hc_curso_2do_u.agregar_materias(hc_materia_biologia_u)
    hc_ciclo_2020.agregar_cursos(hc_curso_2do_u)
    hc_institucion.adjuntar_ciclo_lectivo(hc_ciclo_2020)
    return hc_institucion

# endregion

# region Instituto de Vanguardia fixtures
@pytest.fixture
def vgdia_institucion():
    return Institucion('Instituto de Vanguardia', 'Instituto Vanguardia- Secundaria', 'Secundario',
                       CuarentaNueveArriba(), CuarentaNueveArriba(),'vgds')


@pytest.fixture
def vgdia_ciclo_2020():
    return CicloLectivo('Ciclo Lectivo 2020', ['Primer Trimestre', 'Segundo Trimestre', 'Tercer Trimestre'])


@pytest.fixture
def vgdia_curso_1ero_a():
    return Curso('1°', 'A')


@pytest.fixture
def vgdia_materia_ciencias_naturales_a():
    return Materia('CIENCIAS NATURALES', 'A')


@pytest.fixture
def vgdia_crear_evaluaciones(vgdia_institucion, vgdia_ciclo_2020, vgdia_curso_1ero_a, vgdia_materia_ciencias_naturales_a):
    vgdia_curso_1ero_a.agregar_materias(vgdia_materia_ciencias_naturales_a)
    vgdia_ciclo_2020.agregar_cursos(vgdia_curso_1ero_a)
    vgdia_institucion.adjuntar_ciclo_lectivo(vgdia_ciclo_2020)
    return vgdia_institucion

@pytest.fixture
def hc_crear_calificaciones(hc_alumno_armagnif,hc_crear_evaluaciones):
    hc_curso_2do_u.matricular_alumnos(hc_alumno_armagnif)
    return vgdia_institucion

# endregion

# region Adolfo Kolping

@pytest.fixture
def ak_institucion():
    return Institucion('Instituto Superior Adolfo Kolping Nivel Secundario',
                       'Instituto Superior Adolfo Kolping', 'Secundario',
                       Truncar(), CuarentaNueveArriba(),'aks')

@pytest.fixture
def ak_ciclo_2020():
    return CicloLectivo('2020', ['1º Trimestre', '2º Trimestre', '3º Trimestre'])

@pytest.fixture
def ak_curso_1anio_a():
    return Curso('1º Año', 'A')

@pytest.fixture
def ak_materia_lenguaex_a():
    return Materia('Lengua Extranjera', 'A')

@pytest.fixture
def ak_crear_evaluaciones(ak_institucion, ak_ciclo_2020, ak_curso_1anio_a, ak_materia_lenguaex_a):
    ak_curso_1anio_a.agregar_materias(ak_materia_lenguaex_a)
    ak_ciclo_2020.agregar_cursos(ak_curso_1anio_a)
    ak_institucion.adjuntar_ciclo_lectivo(ak_ciclo_2020)
    return ak_institucion


# end region

