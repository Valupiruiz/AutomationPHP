from behave import when, then
import time


@when("Creo un organismo")
def step_imp(context):
    context.page.agregar_organismo()
    context.page.datos_organismo()
    context.page.direccion_organismo()
    context.page.publicador_uno_organismo()
    context.page.facturador_uno_organismo()
    context.page.guardar_organismo()

@when("Agrego dependencia")
def step_imp(context):
    context.page.dependencia_uno()
    context.page.publicador_uno_dependencia_uno()
    context.page.facturador_uno_dependencia_uno()
    context.page.guardar_dependencia()

@when("Agrego subdepdendencia")
def step_imp(context):
    context.page.subdependencia_uno_dependencia_uno()
    context.page.publicador_subdependencia_uno_dependencia_uno()
    context.page.facturador_subdependencia_uno_dependencia_uno()
    context.page.guardar_dependencia()

@then("La dependencia se agrego exitosamente")
def step_imp(context):
    assert context.page.correcto_organismo('Se creo dependencia con exito')

@then("La subdependencia se agrego exitosamente")
def step_imp(context):
    assert context.page.correcto_organismo('Se creo sub-dependencia con exito')


@then("El organismo se crea existosamente")
def step_imp(context):
    assert context.page.correcto_organismo('El organismo se creo con éxito')

@then("El organismo judicial se crea existosamente")
def step_imp(context):
    assert context.page.correcto_organismo('Creación exitosa')


@when("Voy a modificar el organismo")
def step_imp(context):
    context.page.modifico_organismo()
    context.page.dependencia_dos()
    context.page.publicador_dependencia_dos()
    context.page.facturador_dependencia_dos()
    context.page.subdependencia_uno_dependencia_dos()
    time.sleep(10)
    context.page.guardar_organismo()



@then("El organismo se modifico existosamente")
def step_imp(context):
    assert context.page.se_modifico_correctamente() == 'El organismo se edito con éxito'


