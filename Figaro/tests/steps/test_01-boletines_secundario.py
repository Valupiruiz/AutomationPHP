from pytest_bdd import given, when, then, scenario
from pytest_bdd import parsers
from page_objects.common.navbar.navbar import Navbar
from page_objects.common.menu.menu import Menu
import pytest
from utils.math_utils import *
import pytest_check as check


# es una lista de strings separada por comas
docentes_a_usar = ['mrgarnero', 'vacuna@holycross.edu.ar', 'mmedina13']


@pytest.mark.parametrize('usuario', docentes_a_usar)
@scenario('../features/01-boletines_secundario.feature', 'Crear evaluaciones')
def test_crear_evaluaciones(usuario):
    pass


@given(parsers.parse('me encuentro en la pantalla principal de {tipo_institucion}'))
def ingreso_pantalla_principal(crear_evaluaciones, tipo_institucion):
    crear_evaluaciones["nivel"] = tipo_institucion
    crear_evaluaciones["driver"].get('https://figaro-auto.cysonline.com.ar/')


@given('verifico ciclo y sub-colegio')
def verifico_ciclo_sub_colegio(crear_evaluaciones):
    crear_evaluaciones["page"] = Navbar(crear_evaluaciones["driver"])
    crear_evaluaciones["page"].verificar_sub_colegio(crear_evaluaciones["user_actual"])
    crear_evaluaciones["page"].verificar_ciclo(crear_evaluaciones["user_actual"].institucion.ciclo_lectivo)


@given(parsers.parse('Me dirijo a solapa {nombre}'))
def dirigirse_a_solapa(crear_evaluaciones, nombre):
    crear_evaluaciones["page"] = Menu(crear_evaluaciones["driver"])
    crear_evaluaciones["solapa"] = crear_evaluaciones["page"].dirigirse_a_solapa(nombre)
    crear_evaluaciones["page"] = crear_evaluaciones["solapa"].inicializar(crear_evaluaciones["nivel"], crear_evaluaciones["driver"])


@given("selecciono una materia")
def selecciono_materia(crear_evaluaciones):
    curso_actual = crear_evaluaciones["user_actual"].institucion.ciclo_lectivo.cursos[0]
    crear_evaluaciones["page"].seleccionar_materia(curso_actual)


@given(parsers.parse("cambio a vista de {vista}"))
def cambio_solapa(crear_evaluaciones, vista):
    crear_evaluaciones["page"] = crear_evaluaciones["page"].dirigirse_solapa(vista)


@when("creo las evaluaciones")
def crear_evaluaciones_(crear_evaluaciones):
    materias = crear_evaluaciones["user_actual"].institucion.ciclo_lectivo.cursos[0].materias[0].evaluaciones
    apodo = crear_evaluaciones["user_actual"].institucion.apodo
    crear_evaluaciones["page"].crear_todas_las_evaluaciones(materias, apodo)


@when("Solicito la planilla de evaluaciones")
def planilla_evaluaciones(crear_evaluaciones):
    crear_evaluaciones["page"] = crear_evaluaciones["page"].planilla_evaluaciones()


@pytest.mark.parametrize('usuario', docentes_a_usar)
@scenario('../features/01-boletines_secundario.feature', 'Calificar evaluaciones')
def test_calificar_evaluaciones(usuario):
    pass


@when("Califico evaluaciones")
def califico_evaluaciones(crear_evaluaciones, cp_calificaciones):
    print("estoy en Califico Evaluaciones")
    crear_evaluaciones["calificar"] = cp_calificaciones
    crear_evaluaciones["driver"].switch_to_window(crear_evaluaciones["driver"].window_handles[-1])
    crear_evaluaciones["page"].calificar_evaluaciones(crear_evaluaciones["calificar"][crear_evaluaciones["user_actual"].institucion.apodo])


@then("verifico promedios")
def verifico_promedios(crear_evaluaciones, cp_calificaciones):
    periodos = crear_evaluaciones["user_actual"].institucion.ciclo_lectivo.periodos
    calificaciones = cp_calificaciones[crear_evaluaciones["user_actual"].institucion.apodo]
    prom_calculado = []
    prom_planilla = []
    ev_calculado = []
    ev_planilla = []
    for periodo in periodos:
        promedio = Decimal(crear_evaluaciones["page"].obtengo_promedio_exacto(calificaciones, periodo))
        prom_planilla.append(promedio)
        promedio = calcular_promedio_exacto(calificaciones, periodo)
        prom_calculado.append(promedio)
        ev = Decimal(crear_evaluaciones["page"].obtener_nota_boletin_periodo(calificaciones, periodo))
        ev_planilla.append(ev)
        ev = calcular_ev(promedio, crear_evaluaciones["user_actual"].institucion.redondeo)
        ev_calculado.append(ev)

    check.equal(prom_calculado, prom_planilla, f'Se esperaba {prom_calculado} obtuve {prom_planilla}')
    check.equal(ev_calculado, ev_planilla, f'Se esperaba {ev_calculado} obtuve {ev_planilla}')


@then("vuelvo a pestaña principal")
def volver_pestania_ppal(crear_evaluaciones):
    crear_evaluaciones["driver"].switch_to_window(crear_evaluaciones["driver"].window_handles[0])
    crear_evaluaciones["page"].cerrar_modal_planilla()


@pytest.mark.parametrize('usuario', docentes_a_usar)
@scenario('../features/01-boletines_secundario.feature', 'Verificar ausencias')
def test_ausentar_alumno(usuario):
    pass


@when(parsers.parse('marco alumno como {estado} y verifico promedios'))
@then(parsers.parse('marco alumno como {estado} y verifico promedios'))
def marcar_alumno_ausente(crear_evaluaciones, evaluacion_a_modificar, cp_calificaciones, estado):
    institucion = crear_evaluaciones['user_actual'].institucion
    evaluacion = institucion.ciclo_lectivo.cursos[0].materias[0].evaluaciones[evaluacion_a_modificar]
    calificacion = next(c for c in cp_calificaciones[institucion.apodo] if c.evaluacion.nombre == evaluacion.nombre)
    calificacion.ausente = True if estado == "ausente" else False
    crear_evaluaciones["driver"].switch_to_window(crear_evaluaciones["driver"].window_handles[-1])
    crear_evaluaciones["page"].manejar_ausencia(calificacion)
    verifico_promedios(crear_evaluaciones, cp_calificaciones)
