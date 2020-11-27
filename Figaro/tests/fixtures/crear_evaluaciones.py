import pytest
from dominio.evaluacion import Evaluacion, TipoEvaluacion, Ponderacion


@pytest.mark.usefixtures('hc_docente_vacuna', 'vgdia_docente_mrgarnero', 'ak_docente_medina', 'hc_crear_evaluaciones',
                         'vgdia_crear_evaluaciones', 'ak_crear_evaluaciones')
@pytest.fixture
def crear_evaluaciones(driver, hc_docente_vacuna, vgdia_docente_mrgarnero, hc_evaluaciones,
                       vgdia_evaluaciones, ak_docente_medina,ak_evaluaciones):
    hc_docente_vacuna.inscribir_en_institucion(hc_evaluaciones)
    vgdia_docente_mrgarnero.inscribir_en_institucion(vgdia_evaluaciones)
    ak_docente_medina.inscribir_en_institucion(ak_evaluaciones)
    driver['usuarios'] = [hc_docente_vacuna, vgdia_docente_mrgarnero,ak_docente_medina]
    return driver

@pytest.fixture
def hc_evaluaciones(hc_crear_evaluaciones):
    materia = get_materia(hc_crear_evaluaciones)
    periodos = get_periodos(hc_crear_evaluaciones)
    evtrim_1_1 = Evaluacion(f'{materia.nombre} {periodos[0]} Ev.1', periodos[0], TipoEvaluacion.NUMERICA, '06/03/2020', Ponderacion.AUTOMATICA)
    evtrim_1_2 = Evaluacion(f'{materia.nombre} {periodos[0]} Ev.2', periodos[0], TipoEvaluacion.NUMERICA, '06/04/2020', Ponderacion.AUTOMATICA)
    evtrim_1_3 = Evaluacion(f'{materia.nombre} {periodos[0]} Ev.3', periodos[0], TipoEvaluacion.NUMERICA, '06/05/2020', Ponderacion.AUTOMATICA)
    evtrim_2_1 = Evaluacion(f'{materia.nombre} {periodos[1]} Ev.1', periodos[1], TipoEvaluacion.NUMERICA, '06/06/2020', Ponderacion.AUTOMATICA)
    evtrim_2_2 = Evaluacion(f'{materia.nombre} {periodos[1]} Ev.2', periodos[1], TipoEvaluacion.NUMERICA, '06/07/2020', Ponderacion.AUTOMATICA)
    evtrim_2_3 = Evaluacion(f'{materia.nombre} {periodos[1]} Ev.3', periodos[1], TipoEvaluacion.NUMERICA, '06/08/2020', Ponderacion.AUTOMATICA)
    evtrim_3_1 = Evaluacion(f'{materia.nombre} {periodos[2]} Ev.1', periodos[2], TipoEvaluacion.NUMERICA, '08/09/2020', Ponderacion.AUTOMATICA)
    evtrim_3_2 = Evaluacion(f'{materia.nombre} {periodos[2]} Ev.2', periodos[2], TipoEvaluacion.NUMERICA, '06/10/2020', Ponderacion.AUTOMATICA)
    evtrim_3_3 = Evaluacion(f'{materia.nombre} {periodos[2]} Ev.3', periodos[2], TipoEvaluacion.NUMERICA, '06/11/2020', Ponderacion.MANUAL, 10)
    materia.agendar_evaluaciones(evtrim_1_1, evtrim_1_2, evtrim_1_3, evtrim_2_1, evtrim_2_2, evtrim_2_3, evtrim_3_1, evtrim_3_2, evtrim_3_3)
    return hc_crear_evaluaciones


@pytest.fixture
def vgdia_evaluaciones(vgdia_crear_evaluaciones):
    materia = get_materia(vgdia_crear_evaluaciones)
    periodos = get_periodos(vgdia_crear_evaluaciones)
    evtrim_1_1 = Evaluacion(f'{materia.nombre} {periodos[0]} Ev.1', periodos[0], TipoEvaluacion.NUMERICA, '07/03/2020', Ponderacion.MANUAL, 30)
    evtrim_1_2 = Evaluacion(f'{materia.nombre} {periodos[0]} Ev.2', periodos[0], TipoEvaluacion.NUMERICA, '07/04/2020', Ponderacion.AUTOMATICA)
    evtrim_1_3 = Evaluacion(f'{materia.nombre} {periodos[0]} Ev.3', periodos[0], TipoEvaluacion.NUMERICA, '07/05/2020', Ponderacion.AUTOMATICA)
    evtrim_2_1 = Evaluacion(f'{materia.nombre} {periodos[1]} Ev.1', periodos[1], TipoEvaluacion.NUMERICA, '09/06/2020', Ponderacion.AUTOMATICA)
    evtrim_2_2 = Evaluacion(f'{materia.nombre} {periodos[1]} Ev.2', periodos[1], TipoEvaluacion.NUMERICA, '07/07/2020', Ponderacion.AUTOMATICA)
    evtrim_2_3 = Evaluacion(f'{materia.nombre} {periodos[1]} Ev.3', periodos[1], TipoEvaluacion.NUMERICA, '07/08/2020', Ponderacion.AUTOMATICA)
    evtrim_3_1 = Evaluacion(f'{materia.nombre} {periodos[2]} Ev.1', periodos[2], TipoEvaluacion.NUMERICA, '15/09/2020', Ponderacion.MANUAL, 70)
    evtrim_3_2 = Evaluacion(f'{materia.nombre} {periodos[2]} Ev.2', periodos[2], TipoEvaluacion.NUMERICA, '07/10/2020', Ponderacion.MANUAL, 20)
    evtrim_3_3 = Evaluacion(f'{materia.nombre} {periodos[2]} Ev.3', periodos[2], TipoEvaluacion.NUMERICA, '07/11/2020', Ponderacion.MANUAL, 10)
    materia.agendar_evaluaciones(evtrim_1_1, evtrim_1_2, evtrim_1_3, evtrim_2_1, evtrim_2_2, evtrim_2_3, evtrim_3_1, evtrim_3_2, evtrim_3_3)
    return vgdia_crear_evaluaciones

@pytest.fixture
def ak_evaluaciones(ak_crear_evaluaciones):
    materia = get_materia(ak_crear_evaluaciones)
    periodos = get_periodos(ak_crear_evaluaciones)
    evtrim_1_1 = Evaluacion(f'{materia.nombre} {periodos[0]} Ev.1', periodos[0], TipoEvaluacion.NUMERICA, '07/03/2020', Ponderacion.AUTOMATICA)
    evtrim_1_2 = Evaluacion(f'{materia.nombre} {periodos[0]} Ev.2', periodos[0], TipoEvaluacion.NUMERICA, '07/04/2020', Ponderacion.AUTOMATICA)
    evtrim_1_3 = Evaluacion(f'{materia.nombre} {periodos[0]} Ev.3', periodos[0], TipoEvaluacion.NUMERICA, '07/05/2020', Ponderacion.AUTOMATICA)
    evtrim_2_1 = Evaluacion(f'{materia.nombre} {periodos[1]} Ev.1', periodos[1], TipoEvaluacion.NUMERICA, '09/06/2020', Ponderacion.AUTOMATICA)
    evtrim_2_2 = Evaluacion(f'{materia.nombre} {periodos[1]} Ev.2', periodos[1], TipoEvaluacion.NUMERICA, '07/07/2020', Ponderacion.AUTOMATICA)
    evtrim_2_3 = Evaluacion(f'{materia.nombre} {periodos[1]} Ev.3', periodos[1], TipoEvaluacion.NUMERICA, '07/08/2020', Ponderacion.AUTOMATICA)
    evtrim_3_1 = Evaluacion(f'{materia.nombre} {periodos[2]} Ev.1', periodos[2], TipoEvaluacion.NUMERICA, '15/09/2020', Ponderacion.AUTOMATICA)
    evtrim_3_2 = Evaluacion(f'{materia.nombre} {periodos[2]} Ev.2', periodos[2], TipoEvaluacion.NUMERICA, '07/10/2020', Ponderacion.AUTOMATICA)
    evtrim_3_3 = Evaluacion(f'{materia.nombre} {periodos[2]} Ev.3', periodos[2], TipoEvaluacion.NUMERICA, '07/11/2020', Ponderacion.MANUAL, 10)
    materia.agendar_evaluaciones(evtrim_1_1, evtrim_1_2, evtrim_1_3, evtrim_2_1, evtrim_2_2, evtrim_2_3, evtrim_3_1, evtrim_3_2, evtrim_3_3)
    return ak_crear_evaluaciones


@pytest.fixture
def evaluacion_a_modificar():
    return 1


def get_materia(institucion):
    return institucion.ciclo_lectivo.cursos[0].materias[0]


def get_periodos(institucion):
    return institucion.ciclo_lectivo.periodos
