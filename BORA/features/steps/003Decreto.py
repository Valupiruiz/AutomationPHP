from behave import given, when, then
from page_objects.ORGANISMOS.ABMSOrganismos import OrganismoSimple
from page_objects.COMMON.Menu.Menu import Menu
from config.parameters import Parameters
from page_objects.VERIFICACION_AVISO.Verificar_aviso import Verificacion
from page_objects.BANDEJA_TRAMITES.Bandeja_tramites import BandejaTramites
from generated_data.data_manager import DataManager


global tipo_aviso


@then("Verificar que el aviso este en estado {estado}")
def step_imp(context, estado):
    assert context.page.estado_aviso().upper().strip() == estado.upper().strip(),\
        "se esperaba{0} y fue {1}".format(estado.upper().strip(), context.page.estado_aviso().upper().strip())


@given("Obtengo el firmante  que no existe")
def step_imp(context):
    context.page = BandejaTramites(context.driver, DataManager.get_id_aviso(),
                                   context.data[DataManager.get_tipoAviso()+"Erroneo"],
                                   context.data[DataManager.get_tipoAviso()],
                                   DataManager.get_tipoAviso())
    context.page.firmante_inexistente()


@when("Activar organismo")
def step_imp(context):
    context.page.activar_organismo()
    context.page.guardar_organismo()


@when("Creo firmante")
def step_imp(context):
    context.page.nuevo_firmante()

@then("Creación exitosa firmante")
def step_imp(context):
    assert context.page.correcta_creacion_firmante() == "Creación exitosa"

@when("Reprocesar aviso")
def step_imp(context):
    context.page.reprocesar_aviso()


@then("Se reproceso correctamente")
def step_imp(context):
    assert context.page.reproceso_correctamente() == "Se reproceso con exito"


@then("Verificar orden de firmantes")
def step_imp(context):
    assert context.page.verificar_orden_firmantes()


@when("Cierro ventana")
def step_imp(context):
    context.page.cierro_ventana()

@when("Modifico {campo} erroneamente en estado {lugar}")
def step_imp(context, campo, lugar):
    if lugar == "Pendiente de publicación" or lugar == "Requiere Aprobación":
        context.page =BandejaTramites(context.driver, DataManager.get_id_aviso(),
                                      context.data[DataManager.get_tipoAviso() + "Erroneo"],
                                      context.data[DataManager.get_tipoAviso()], DataManager.get_tipoAviso())
    if lugar == "Pendiente de verificacion":
        context.page = Verificacion(context.driver, DataManager.get_id_aviso(),
                                    context.data[DataManager.get_tipoAviso() + "Erroneo"],
                                    context.data[DataManager.get_tipoAviso()], DataManager.get_tipoAviso())
    context.page.modificar_campo_error(campo)


@then("Verificar que existan anexos y documentos")
def step_imp(context):
    assert context.page.verificar_existencia_documentos()

@then("Verificar texto de documento de texto")
def step_imp(context):
    assert context.page.verificar_texto_pdf()

@then("Verificar titulo del documento de texto")
def step_imp(context):
    assert context.page.titulo_texto_organismo_sub(context.data["organismo"]["nombre_orga"],
                                               context.data["organismo"]["dep1_sub0_nombre"])


@when("Voy a descargar pdf del texto del aviso")
def step_imp(context):
    context.page.descargar_pdf_texto()

@when("Voy a descargar pdf del deocuemtno del texto del aviso")
def step_imp(context):
    context.page.descargar_pdf_documento()


@then("Verificar advertencia {campo}")
def step_imp(context, campo):
    assert context.page.verificar_advertencia(campo)


@given("Aprobar aviso en estado {estado}")
@then("Aprobar aviso en estado {estado}")
@when("Aprobar aviso en estado {estado}")
def step_imp(context, estado):
    if estado == "Pendiente de Verificacion":
        context.page = Verificacion(context.driver, DataManager.get_id_aviso(),
                                    context.data[DataManager.get_tipoAviso() + "Erroneo"],
                                    context.data[DataManager.get_tipoAviso()], DataManager.get_tipoAviso())
        context.page.aprobar_aviso_error()
    if estado == "Requiere aprobacion":
        context.page = BandejaTramites(context.driver, DataManager.get_id_aviso(),
                                       context.data[DataManager.get_tipoAviso() + "Erroneo"],
                                       context.data[DataManager.get_tipoAviso()],
                                       DataManager.get_tipoAviso())
        context.page.apruebo_req_aprobacion()
    if estado == "Pendiente Publicacion":
        context.page = BandejaTramites(context.driver, DataManager.get_id_aviso(),
                                       context.data[DataManager.get_tipoAviso() + "Erroneo"],
                                       context.data[DataManager.get_tipoAviso()],
                                       DataManager.get_tipoAviso())
        context.page.guardar_aviso()


@given("Apruebar aviso")
def step_imp(context):
    context.page = Verificacion(context.driver, DataManager.get_id_aviso(),
                                context.data[DataManager.get_tipoAviso() + "Erroneo"],
                                context.data[DataManager.get_tipoAviso()],
                                DataManager.get_tipoAviso())
    context.page.aprobar_aviso()


@then("Apruebar aviso")
def step_imp(context):
    context.page.aprobar_aviso()


@then("se aprobo con exito")
def step_imp(context):
    assert context.page.aprobo_exito() == "Se aprobo el aviso con exito"


@when("Modifico {campo} correctamente")
def step_imp(context, campo):
    context.page.modificar_campo_bien(campo)


@when("Guardo aviso en estado {estado}")
def step_imp(context, estado):
    if estado == "Pendiente de verificacion":
        context.page = Verificacion(context.driver,
                                    DataManager.get_id_aviso(),
                                    context.data[DataManager.get_tipoAviso() + "Erroneo"],
                                    context.data[DataManager.get_tipoAviso()],
                                    DataManager.get_tipoAviso())
    else:
        context.page = BandejaTramites(context.driver, DataManager.get_id_aviso(),
                                       context.data[DataManager.get_tipoAviso() + "Erroneo"],
                                       context.data[DataManager.get_tipoAviso()],
                                       DataManager.get_tipoAviso())
    if estado == "requiere aprobacion":
        context.page.apruebo_req_aprobacion()
    else:
        context.page.guardar_aviso()


@then("Se guardo correctamente")
def step_imp(context):
    context.page.guardo_correctamente()


@when("Publicar aviso")
def step_imp(context):
    context.page = Verificacion(context.driver, DataManager.get_id_aviso(),
                                context.data[DataManager.get_tipoAviso() + "Erroneo"],
                                context.data[DataManager.get_tipoAviso()],
                                DataManager.get_tipoAviso())
    context.status = context.page.informo_publicacion()

@then("Cerrar sesion")
def step_imp(context):
    context.page = Verificacion(context.driver,
                                DataManager.get_id_aviso(),
                                context.data[DataManager.get_tipoAviso() + "Erroneo"],
                                context.data[DataManager.get_tipoAviso()],
                                DataManager.get_tipoAviso())
    context.page.cerrar_sesion()

@given("Inicializo aviso {campo}")
def step_imp(context, campo):
    pass

@when("Descargar documento del aviso")
def step_imp(context):
    context.page = BandejaTramites(context.driver, DataManager.get_id_aviso(),
                                   context.data[DataManager.get_tipoAviso() + "Erroneo"],
                                   context.data[DataManager.get_tipoAviso()],
                                   DataManager.get_tipoAviso())
    context.page.descargar_pdf_documento()
    assert context.page.verificar_existencia_pdf_documento("República Argentina - Poder Ejecutivo Nacional")


