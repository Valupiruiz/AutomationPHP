import pytest
from dominio.calificacion import Calificacion
from decimal import Decimal, ROUND_UP


@pytest.mark.usefixtures('hc_alumno_armagnif', 'vgdia_alumno_abdalaf', 'ak_alumno_lazzarom') #fixtures que se van a usar
@pytest.fixture
def crear_calificaciones(crear_evaluaciones, hc_alumno_armagnif, vgdia_alumno_abdalaf, ak_alumno_lazzarom):
    crear_evaluaciones['usuarios'][0].institucion.ciclo_lectivo.cursos[0].matricular_alumnos(hc_alumno_armagnif)
    crear_evaluaciones['usuarios'][1].institucion.ciclo_lectivo.cursos[0].matricular_alumnos(vgdia_alumno_abdalaf)
    crear_evaluaciones['usuarios'][2].institucion.ciclo_lectivo.cursos[0].matricular_alumnos(ak_alumno_lazzarom)
    return crear_evaluaciones

@pytest.fixture
def hc_calificaciones(crear_calificaciones):
    curso = get_curso(crear_calificaciones['usuarios'][0])
    evtrim_1_1_af = Calificacion(curso.materias[0].evaluaciones[0], Decimal("7.00"), curso.alumnos[0])
    evtrim_1_2_af = Calificacion(curso.materias[0].evaluaciones[1], Decimal("3.00"), curso.alumnos[0])
    evtrim_1_3_af = Calificacion(curso.materias[0].evaluaciones[2], Decimal("10.00"), curso.alumnos[0])
    evtrim_2_1_af = Calificacion(curso.materias[0].evaluaciones[3], Decimal("7.00"), curso.alumnos[0])
    evtrim_2_2_af = Calificacion(curso.materias[0].evaluaciones[4], Decimal("2.00"), curso.alumnos[0])
    evtrim_2_3_af = Calificacion(curso.materias[0].evaluaciones[5], Decimal("10.00"), curso.alumnos[0])
    evtrim_3_1_af = Calificacion(curso.materias[0].evaluaciones[6], Decimal("10.00"), curso.alumnos[0])
    evtrim_3_2_af = Calificacion(curso.materias[0].evaluaciones[7], Decimal("2.00"), curso.alumnos[0])
    evtrim_3_3_af = Calificacion(curso.materias[0].evaluaciones[8], Decimal("1.76"), curso.alumnos[0])
    return [evtrim_1_1_af, evtrim_1_2_af, evtrim_1_3_af, evtrim_2_1_af, evtrim_2_2_af, evtrim_2_3_af, evtrim_3_1_af,
            evtrim_3_2_af, evtrim_3_3_af]

@pytest.fixture
def vgdia_calificaciones(crear_calificaciones):
    curso = get_curso(crear_calificaciones['usuarios'][1])
    evtrim_1_1_abf = Calificacion(curso.materias[0].evaluaciones[0], Decimal("7.00"), curso.alumnos[0])
    evtrim_1_2_abf = Calificacion(curso.materias[0].evaluaciones[1], Decimal("3.00"), curso.alumnos[0])
    evtrim_1_3_abf = Calificacion(curso.materias[0].evaluaciones[2], Decimal("10.00"), curso.alumnos[0])
    evtrim_2_1_abf = Calificacion(curso.materias[0].evaluaciones[3], Decimal("7.00"), curso.alumnos[0])
    evtrim_2_2_abf = Calificacion(curso.materias[0].evaluaciones[4], Decimal("2.00"), curso.alumnos[0])
    evtrim_2_3_abf = Calificacion(curso.materias[0].evaluaciones[5], Decimal("10.00"), curso.alumnos[0])
    evtrim_3_1_abf = Calificacion(curso.materias[0].evaluaciones[6], Decimal("10.00"), curso.alumnos[0])
    evtrim_3_2_abf = Calificacion(curso.materias[0].evaluaciones[7], Decimal("2.00"), curso.alumnos[0])
    evtrim_3_3_abf = Calificacion(curso.materias[0].evaluaciones[8], Decimal("1.76"), curso.alumnos[0])
    return [evtrim_1_1_abf, evtrim_1_2_abf, evtrim_1_3_abf, evtrim_2_1_abf, evtrim_2_2_abf, evtrim_2_3_abf,
            evtrim_3_1_abf, evtrim_3_2_abf, evtrim_3_3_abf]

@pytest.fixture
def ak_calificaciones(crear_calificaciones):
    curso = get_curso(crear_calificaciones['usuarios'][2])
    evtrim_1_1_abf = Calificacion(curso.materias[0].evaluaciones[0], Decimal("7.00"), curso.alumnos[0])
    evtrim_1_2_abf = Calificacion(curso.materias[0].evaluaciones[1], Decimal("3.00"), curso.alumnos[0])
    evtrim_1_3_abf = Calificacion(curso.materias[0].evaluaciones[2], Decimal("10.00"), curso.alumnos[0])
    evtrim_2_1_abf = Calificacion(curso.materias[0].evaluaciones[3], Decimal("7.00"), curso.alumnos[0])
    evtrim_2_2_abf = Calificacion(curso.materias[0].evaluaciones[4], Decimal("2.00"), curso.alumnos[0])
    evtrim_2_3_abf = Calificacion(curso.materias[0].evaluaciones[5], Decimal("10.00"), curso.alumnos[0])
    evtrim_3_1_abf = Calificacion(curso.materias[0].evaluaciones[6], Decimal("10.00"), curso.alumnos[0])
    evtrim_3_2_abf = Calificacion(curso.materias[0].evaluaciones[7], Decimal("2.00"), curso.alumnos[0])
    evtrim_3_3_abf = Calificacion(curso.materias[0].evaluaciones[8], Decimal("5.00"), curso.alumnos[0])
    return [evtrim_1_1_abf, evtrim_1_2_abf, evtrim_1_3_abf, evtrim_2_1_abf, evtrim_2_2_abf, evtrim_2_3_abf,
            evtrim_3_1_abf, evtrim_3_2_abf, evtrim_3_3_abf]

def get_curso(usuario):
    return usuario.institucion.ciclo_lectivo.cursos[0]


@pytest.fixture()
def cp_calificaciones(ak_calificaciones, vgdia_calificaciones, hc_calificaciones):
    return {
        "hcs": hc_calificaciones,
        "vgds": vgdia_calificaciones,
        "aks": ak_calificaciones
    }
