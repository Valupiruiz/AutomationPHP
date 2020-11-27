from pytest_bdd import given, when, then, scenario
from pytest_bdd import parsers
from page_objects.datos_personales.datos_personales import DatosPersonales
from page_objects.titulos.titulo import Titulo
import pytest_check as check
from page_objects.certificados.certificado import Certificado
from page_objects.usuarios_bue.usuarios_bue import UsuariosBue
from page_objects.buscador_docentes.buscador_docentes import BuscadorDocente
from page_objects.buscador_docentes.docentes.datos_docentes import DatosDocentes
from page_objects.inscripciones.nueva_inscripcion.nueva_inscripcion import NuevaInscripcion
from page_objects.inscripciones.inscripciones import Inscripciones
from page_objects.cursos.cursos import Curso
from page_objects.distritos.distrito import Distrito


@scenario("../features/02-carga_documentacion.feature", "Cargo datos faltantes")
def test_cargo_datos_faltantes():
    pass

@scenario("../features/02-carga_documentacion.feature", "Cargo titulo")
def test_cargo_titulo():
    pass


@scenario("../features/02-carga_documentacion.feature", "Aprobar documentacion")
def test_aprobar_documentacion():
    pass

@scenario("../features/02-carga_documentacion.feature", "Inscripcion a cargo")
def test_inscripcion_cargo():
    pass

@scenario("../features/02-carga_documentacion.feature", "Cargo curso")
def test_cargo_curso():
    pass


# @scenario("../features/02-carga_documentacion.feature", "Deshabilitar usuario")
# def test_deshabilitar():
#     pass


@when('completo datos faltantes')
def completo_faltantes(context, docente_test5):
    context["page"] = DatosPersonales(context["driver"])
    context["page"].cargar_info_faltante(docente_test5)
    context["page"].guardar()
    check.equal(context["page"].se_guardo_correctamente(), "×\nLos datos personales se guardaron correctamente.", f'obtuve {context["page"].se_guardo_correctamente()}')


@when("cargo titulo")
def cargo_titulo(context, docente_test5):
    context["page"] = Titulo(context["driver"])
    context["page"].abrir_buscador_titulos()
    context["page"].buscar_por_titulo(docente_test5.titulos[0].nombre, docente_test5.titulos[0].sin_secundario)
    context["page"].agregar_titulo(docente_test5.titulos[0].nombre)
    context["page"] = Certificado(context["driver"])
    context["page"].completar_info_basica(docente_test5.titulos[0].imagenes[0],
                                          docente_test5.titulos[0].fecha_emision)


@then("se cargo exitosamente el titulo")
def titulo_cargado(context):
    context["page"] = Titulo(context["driver"])
    check.equal(context["page"].se_cargo_exitosamente(), "×\nEl título se guardó correctamente.", f'obtuve {context["page"].se_cargo_exitosamente()}')


@when("Deshabilito usuario")
def deshabilitar_usuario(context, docente_test5):
    context["page"] = UsuariosBue(context["driver"])
    context["page"].deshabilitar_usuario(docente_test5.nro_dni)
    check.equal(context["page"].cambio_correcto(), "×\nEl Usuario Temporal se habilitó correctamente.",
                f'obtuve {context["page"].cambio_correcto()}')


@when("deshabilito y cambio mail")
def cambio_mail(context, docente_test5):
    context["page"] = UsuariosBue(context["driver"])
    context["page"].cambio_mail_definitivo(docente_test5.mail)
    context["page"].guardar()
    check.equal(context["page"].cambio_correcto(), "×\nEl Usuario se guardó correctamente.",
                f'obtuve {context["page"].cambio_correcto()}')

@when("aprobar documentacion de titulo")
def aprobar_doc(context, docente_test5):
    context["page"] = BuscadorDocente(context["driver"])
    context["page"].buscar_por_mail(docente_test5.mail)
    context["page"] = DatosDocentes(context["driver"])
    context["page"].ir_a_solapa('Documentación')
    context["page"].aprobar_titulo(docente_test5.titulos[0].nombre)
    estado_page = context["page"].estado_titulo(docente_test5.titulos[0].nombre)
    check.equal(estado_page, "Aprobado", f'obtuve {estado_page} y esperaba "Aprobado"')

@when("nueva inscripcion")
def nueva_insc(context, docente_test5):
    context["page"].inscripcion_periodo()
    context["page"] = Inscripciones(context["driver"])
    context["page"].inscribirse()
    context["page"] = NuevaInscripcion(context["driver"])
    context["page"].buscar_inscripcion(docente_test5.inscripciones[0].area,
                                       docente_test5.inscripciones[0].cargo,
                                       docente_test5.inscripciones[0].asignatura,
                                       docente_test5.inscripciones[0].especialidad)
    estado_page = context["page"].inscripcion_correcta()
    check.is_in("Se pudo inscribir correctamente al cargo", estado_page, f'obtuve {estado_page}"')


@when("agrego curso")
def agrego_curso(context, docente_test5):
    context["page"] = Curso(context["driver"])
    context["page"].abrir_buscador()
    context["page"].buscar(docente_test5.cursos[0].nombre)
    context["page"].agregar_curso(docente_test5.cursos[0].nombre)
    context["page"] = Certificado(context["driver"])
    context["page"].completar_info_basica(docente_test5.cursos[0].imagenes[0],
                                          docente_test5.cursos[0].fecha_egreso)

@then("se aprobo exitosamente el curso")
def se_aprobo_curso(context):
    context["page"] = Curso(context["driver"])
    estado_page = context["page"].curso_agregado_correctamente()
    check.is_in("El curso se guardó correctamente.", estado_page, f'obtuve {estado_page}"')

@when("cargo distritos")
def cargo_distritos(context, docente_test5):
    context["page"] = Distrito(context["driver"])
    context["page"].editar_area(docente_test5.inscripciones[0].area)
    context["page"].seleccionar_distrito(docente_test5.inscripciones[0].distrito)
    context["page"].guardar()
    estado_page = context["page"].se_guardo_correctamente()
    check.is_in("La Selección de Configuración de Distritos se guardó correctamente", estado_page, f'obtuve {estado_page}"')





