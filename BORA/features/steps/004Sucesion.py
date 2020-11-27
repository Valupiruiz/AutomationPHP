from behave import given, when, then
import time
from page_objects.JUDICIALES.Judiciales import OrganismoJudicial
from page_objects.BANDEJA_TRAMITES.Bandeja_tramites import BandejaTramites
from page_objects.COMMON.Login.Login import Login



@when("Crear organismo Judicial")
def step_imp(context):
    context.page.crear_organismo_judicial()
    context.page.crear_secretaria()
    context.page.crear_representante_secretaira()
    context.page.guardar_secretaria()

@when("Nueva pestania de judiciales")
def step_imp(context):
    context.driver.get("http://10.2.1.112:8083/admin/tramites")
    time.sleep(2)
    context.page = OrganismoJudicial(context.driver)
    context.page.login()

@when("Pagar aviso")
def step_imp(context):
    context.page.pagar_aviso()

@then("Se hizo el pago con exito")
def step_imp(context):
    assert context.page.pago_exitoso() == "El pago manual del aviso fue generado con éxito"

@when("Volver a BOW")
def step_imp(context):
    context.page = Login(context.driver)
    context.driver.get("http://10.2.1.112:8081")
    time.sleep(10)
