from behave import given, when, then
from page_objects.COMMON.Menu.Menu import Menu
from page_objects.CREAR_AVISO.Nuevo_aviso_api import NuevoAvisoAPI
from generated_data.data_manager import DataManager
from page_objects.VERIFICACION_AVISO.Verificar_aviso import Verificacion


@when('Estoy logueado como usuario{usuario}')
@given('Estoy logueado como usuario{usuario}')
def step_imp(context, usuario):
    context.page = context.page.iniciar_sesion(usuario, '1234')


@then('Me dirijo a {menu1}, {menu2}')
@when('Me dirijo a {menu1}, {menu2}')
@given('Me dirijo a {menu1}, {menu2}')
def step_imp(context, menu1, menu2):
    context.page = Menu(context.driver)
    context.page = context.page.click_menu(menu1, menu2, context.data)


@when('ingresar datos de acta')
def step_imp(context):
    context.page.crear_aviso_acta()


@when('adjuntar archivo')
def step_imp(context):
    context.page.archivo()


@then('Creacion exitosa')
def step_imp(context):
    assert context.page.correcto() == 'Creación exitosa'


@when('Envio informacion del  aviso de tipo {tipo}')
def step_imp(context, tipo):
    context.page = NuevoAvisoAPI(tipo)
    context.status = context.page.envio_informacion()


@given('Envio documento')
def step_imp(context):
    context.status = context.page.creo_documento()


@given('Envio anexos')
def step_imp(context):
    context.status = context.page.creo_anexos()


@then('Documento creado exitosamente')
def step_imp(context):
    assert context.respuesta["dgfsdfs"]


@when('Apruebo aviso')
def step_imp(context):
    context.page = Verificacion(context.driver,
                                DataManager.get_id_aviso(),
                                context.data[DataManager.get_tipoAviso()+"Erroneo"],
                                context.data[DataManager.get_tipoAviso()],
                                DataManager.get_tipoAviso()),
    context.page.apruebo_aviso()


@when('Apruebo aviso manual')
def step_imp(context):
    context.page.apruebo_aviso_manual()


@then("Verificacion exitosa")
def step_imp(context):
    assert context.page.correcta_verificacion() == 'Se aprobo con exito'


@when("Informo publicacion")
def step_imp(context):
    context.page.informo_publicacion()


@when("Completar informacion")
def step_imp(context):
    context.page.crear_aviso_cuarta()


@given('Envio informacion del  aviso de tipo {tipo}')
def step_imp(context, tipo):
    context.page = NuevoAvisoAPI(tipo, context.data[tipo], context.data["ambiente"])
    DataManager.set_tipoAviso(tipo)
    context.status = context.page.envio_informacion()

@then("Informacion enviada exitosamente")
def step_imp(context):
    assert context.status == 0, "se esperaba{0} y fue {1}".format("0", context.status)


@when('Envio documento')
def step_imp(context):
    context.page = NuevoAvisoAPI(context.tipo_aviso, context.data[context.tipo_aviso], context.data["ambiente"])
    context.status = context.page.creo_documento()


@when('Envio anexos')
def step_imp(context):
    context.status = context.page.creo_anexos()

@when("Visualizar aviso")
@then("Visualizar aviso")
def step_imp(context):
    context.page.visualizar_aviso()

@when("Apruebo")
def step_imp(context):
    context.page.apruebo_req_aprobacion()


@when("Agregar aviso a OA de suplementos")
def step_imp(context):
    context.page = NuevoAvisoAPI(DataManager.get_tipoAviso(), context.data[DataManager.get_tipoAviso()], context.data["ambiente"])
    context.page = context.page.agregar_aviso_oa_sup()

@when("Creo OA suplementos")
def step_imp(context):
    context.page.crear_orden()
    # context.page.cambio_nro_edicion()
    # assert context.page.guardar_orden() == 'La orden de armado se ha guardado correctamente', \
    #     "se esperaba{0} y fue {1}".format("0", context.page.guardar_orden())

@when("Agrego avisos a suplemento")
def step_imp(context):
    context.page.agrego_avisos_oa(context.data["oa_sup"])


# Esto se hizo especificamente para un flujo de un dia lo ideal seria hacer generico el date picker
@when("Cambio fecha y Agrego aviso a {suplemento}")
def step_imp(context, suplemento):
    context.page.click_fecha()
    context.page.modificar_fecha()
    context.page.agrego_aviso_oa(suplemento)

@when("Cambio de rubro a {rubro}")
def step_imp(context, rubro):
    context.page.cambio_rubro(rubro)
# 

@when("Cambio numero de edicion")
def step_imp(context):
    context.page.visualizar_orden_sup()
    context.page.cambio_nro_edicion()
    assert context.page.guardar_orden() == 'La orden de armado se ha guardado correctamente', \
         "se esperaba{0} y fue {1}".format("0", context.page.guardar_orden())

@then("Verificar avisos en el pdf de la orden")
def step_imp(context):
    context.page.descargar_pdf_oa()
    context.page.verificar_contenido_oa()


