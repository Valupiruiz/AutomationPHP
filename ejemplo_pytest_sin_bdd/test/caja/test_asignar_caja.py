import allure
import pytest

from src.actions.caja_actions import CierreParcialCajaAction, CierreTotalCajaAction
from src.actions.gestion_caja_actions import AsignarCajeroCajaAction
from src.actions.login_actions import LoginAction, OperadorSinOperableLoginAction
from src.actions.logout_actions import LogoutAction
from src.actions.operable_actions import AperturaOperableAction
from src.dominio.operaciones import Apertura, CierreParcial, CierreTotal


# region Asignar cajero

@allure.feature("Gestion de caja")
@allure.story("Asignar cajero")
@allure.title("Operaciones asigna un cajero a una caja")
@pytest.mark.usefixtures("generar_sucursal")
def test_asignar_caja(context):
    driver_cajero = context.driver_manager.main_driver
    caja = context.sucursal.cajas[0]
    cajero = context.cajeros[0]

    apertura_action = AperturaOperableAction(context)

    with allure.step("El cajero no tiene una caja asignada"):
        OperadorSinOperableLoginAction(context).verify_state().do(cajero).success()

    driver_operaciones = context.driver_manager.new_driver()
    context.page.set_active_driver(driver_operaciones)
    with allure.step("Operaciones le asigna una caja"):
        LoginAction(context).verify_state().do(context.operaciones).success("Gestion de caja")
        AsignarCajeroCajaAction(context).verify_state(caja, context.sucursal, None).do(cajero) \
            .success("Usuario asignado")

    context.page.set_active_driver(driver_cajero)
    with allure.step(f"el cajero es asignado y puede aperturar la caja"):
        LogoutAction(context).verify_state(cajero).do().success()
        LoginAction(context).verify_state().do(cajero).success("Apertura Caja")
        apertura_action.verify_state(caja)


@allure.feature("Gestion de caja")
@allure.story("Asignar cajero")
@allure.title("Operaciones cambia el cajero de una caja cerrada totalmente")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.parametrize('cant_cajeros', [2])
def test_cambiar_cajero_caja_cerrada_totalmente(context):
    driver_cajero_a = context.driver_manager.main_driver
    cajero_a = context.cajeros[0]
    cajero_b = context.cajeros[1]
    caja = context.sucursal.cajas[0]

    apertura_action = AperturaOperableAction(context)

    with allure.step("El cajero A no tiene una caja asignada"):
        OperadorSinOperableLoginAction(context).verify_state().do(cajero_a).success()

    driver_cajero_b = context.driver_manager.new_driver()
    context.page.set_active_driver(driver_cajero_b)
    with allure.step("El cajero B tiene una caja asignada"):
        LoginAction(context).verify_state().do(cajero_b, caja).success("Apertura Caja")
        apertura_action.verify_state(caja)

    driver_operaciones = context.driver_manager.new_driver()
    context.page.set_active_driver(driver_operaciones)
    with allure.step("Operaciones le asigna la caja del cajero b al cajero a"):
        LoginAction(context).verify_state().do(context.operaciones).success("Gestion de caja")
        AsignarCajeroCajaAction(context).verify_state(caja, context.sucursal, cajero_b.nombre_completo()).do(cajero_a) \
            .success("Usuario asignado")

    context.page.set_active_driver(driver_cajero_a)
    with allure.step("El cajero A es asignado y puede aperturar la caja"):
        LogoutAction(context).verify_state(cajero_a).do().success()
        LoginAction(context).verify_state().do(cajero_a).success("Apertura Caja")
        apertura_action.verify_state(caja)

    context.page.set_active_driver(driver_cajero_b)
    with allure.step("El cajero B ya no tiene una caja asignada"):
        LogoutAction(context).verify_state(cajero_b).do().success()
        OperadorSinOperableLoginAction(context).verify_state().do(cajero_b).success()

    for driver, usuario in [[driver_cajero_a, cajero_a], [driver_cajero_b, cajero_b]]:
        context.page.set_active_driver(driver)
        LogoutAction(context).verify_state(usuario).do().success()


@allure.feature("Gestion de caja")
@allure.story("Asignar cajero")
@allure.title("No se puede cambiar el cajero de una caja abierta")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.parametrize('cant_cajeros', [2])
def test_cambiar_cajero_caja_abierta(context):
    driver_cajero_a = context.driver_manager.main_driver
    cajero_a = context.cajeros[0]
    cajero_b = context.cajeros[1]
    caja = context.sucursal.cajas[0]

    apertura = Apertura({moneda: 0 for moneda in caja.monedas_permitidas})
    cierre = CierreTotal({moneda: 0 for moneda in caja.monedas_permitidas})
    apertura_action = AperturaOperableAction(context)
    asignar_caja_action = AsignarCajeroCajaAction(context)

    with allure.step("El cajero A no tiene una caja asignada"):
        OperadorSinOperableLoginAction(context).verify_state().do(cajero_a).success()

    driver_cajero_b = context.driver_manager.new_driver()
    context.page.set_active_driver(driver_cajero_b)
    with allure.step("El cajero B tiene una caja abierta"):
        LoginAction(context).verify_state().do(cajero_b, caja).success("Apertura Caja")
        apertura_action.fast_forward(cajero_b, caja, apertura)

    driver_operaciones = context.driver_manager.new_driver()
    context.page.set_active_driver(driver_operaciones)
    with allure.step("Operaciones le asigna la caja del cajero A al cajero B"):
        LoginAction(context).verify_state().do(context.operaciones).success("Gestion de caja")
        asignar_caja_action.verify_state(caja, context.sucursal, cajero_b.nombre_completo()).do(cajero_a)

    with allure.step("Pero no puede porque la caja esta abierta"):
        asignar_caja_action.failure("Asignar caja abierta")

    context.page.set_active_driver(driver_cajero_b)
    with allure.step("El cajero B aun tiene la caja asignada"):
        CierreTotalCajaAction(context).verify_state(caja, cierre)

    context.page.set_active_driver(driver_cajero_a)
    with allure.step("El cajero A sigue sin una asignacion"):
        LogoutAction(context).verify_state(cajero_a).do().success()
        OperadorSinOperableLoginAction(context).verify_state().do(cajero_a).success()

    logout_action = LogoutAction(context)
    for driver, usuario in [[driver_operaciones, context.operaciones],
                            [driver_cajero_a, cajero_a],
                            [driver_cajero_b, cajero_b]]:
        context.page.set_active_driver(driver)
        logout_action.verify_state(usuario).do().success()


@allure.feature("Gestion de caja")
@allure.story("Asignar cajero")
@allure.title("No se puede cambiar el cajero de una caja cerrada parcialmente")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.parametrize('cant_cajeros', [2])
def test_cambiar_cajero_caja_cerrada_parcialmente(context):
    driver_cajero_a = context.driver_manager.main_driver
    cajero_a = context.cajeros[0]
    cajero_b = context.cajeros[1]
    caja = context.sucursal.cajas[0]

    cierre = CierreParcial({moneda: 0 for moneda in caja.monedas_permitidas})
    apertura = Apertura({moneda: 0 for moneda in caja.monedas_permitidas})
    apertura_action = AperturaOperableAction(context)

    asignar_caja_action = AsignarCajeroCajaAction(context)

    with allure.step("El cajero A no tiene una caja asignada"):
        OperadorSinOperableLoginAction(context).verify_state().do(cajero_a).success()

    driver_cajero_b = context.driver_manager.new_driver()
    context.page.set_active_driver(driver_cajero_b)
    with allure.step("El cajero B tiene una caja cerrada parcialmente"):
        LoginAction(context).verify_state().do(cajero_b, caja).success("Apertura Caja")
        apertura_action.fast_forward(cajero_b, caja, apertura)
        CierreParcialCajaAction(context).fast_forward(cajero_b, caja, cierre)

    driver_operaciones = context.driver_manager.new_driver()
    context.page.set_active_driver(driver_operaciones)
    with allure.step("Operaciones le asigna la caja del cajero b al cajero a"):
        LoginAction(context).verify_state().do(context.operaciones).success("Gestion de caja")
        asignar_caja_action.verify_state(caja, context.sucursal, cajero_b.nombre_completo()).do(cajero_a)

    with allure.step("Pero no puede porque la caja esta cerrada parcialmente"):
        asignar_caja_action.failure("Asignar caja abierta")

    context.page.set_active_driver(driver_cajero_b)
    with allure.step("El cajero B aun esta asignado a la caja"):
        LogoutAction(context).verify_state(cajero_b).do().success()
        LoginAction(context).verify_state().do(cajero_b).success("Apertura Caja")
        apertura_action.verify_state(caja)

    context.page.set_active_driver(driver_cajero_a)
    with allure.step("El cajero A sigue sin una asignacion"):
        LogoutAction(context).verify_state(cajero_a).do().success()
        OperadorSinOperableLoginAction(context).verify_state().do(cajero_a).success()

    for driver, usuario in [[driver_operaciones, context.operaciones],
                            [driver_cajero_a, cajero_a],
                            [driver_cajero_b, cajero_b]]:
        context.page.set_active_driver(driver)
        LogoutAction(context).verify_state(usuario).do().success()


@allure.feature("Gestion de caja")
@allure.story("Asignar cajero")
@allure.title("Operaciones desasigna un cajero de una caja")
@pytest.mark.usefixtures("generar_sucursal")
def test_desasignar_cajero(context):
    driver_cajero = context.driver_manager.main_driver
    caja = context.sucursal.cajas[0]
    cajero = context.cajeros[0]

    apertura_action = AperturaOperableAction(context)

    with allure.step("El cajero tiene una caja asignada"):
        LoginAction(context).verify_state().do(cajero, caja).success("Apertura Caja")
        apertura_action.verify_state(caja)

    driver_operaciones = context.driver_manager.new_driver()
    context.page.set_active_driver(driver_operaciones)
    with allure.step("Operaciones le desasigna su caja"):
        LoginAction(context).verify_state().do(context.operaciones).success("Gestion de caja")
        AsignarCajeroCajaAction(context).verify_state(caja, context.sucursal, cajero.nombre_completo()).do(None) \
            .success("Usuario desasignado")

    context.page.set_active_driver(driver_cajero)
    with allure.step(f"el cajero es desasignado y no puede operar"):
        LogoutAction(context).verify_state(cajero).do().success()
        OperadorSinOperableLoginAction(context).verify_state().do(cajero, desasignar_cajero=False).success()


@allure.feature("Gestion de caja")
@allure.story("Asignar cajero")
@allure.title("No se puede desasignar un cajero si la caja esta abierta")
@pytest.mark.usefixtures("generar_sucursal")
def test_desasignar_cajero_caja_abierta(context):
    driver_cajero = context.driver_manager.main_driver
    caja = context.sucursal.cajas[0]
    cajero = context.cajeros[0]

    apertura = Apertura({moneda: 0 for moneda in caja.monedas_permitidas})
    apertura_action = AperturaOperableAction(context)
    asignar_cajero_action = AsignarCajeroCajaAction(context)

    with allure.step("El cajero tiene una caja abierta"):
        LoginAction(context).verify_state().do(cajero, caja).success("Apertura Caja")
        apertura_action.fast_forward(cajero, caja, apertura)

    driver_operaciones = context.driver_manager.new_driver()
    context.page.set_active_driver(driver_operaciones)
    with allure.step("Operaciones le desasigna su caja"):
        LoginAction(context).verify_state().do(context.operaciones).success("Gestion de caja")
        asignar_cajero_action.verify_state(caja, context.sucursal, cajero.nombre_completo()).do(None)

    with allure.step("Pero no puede porque la caja esta abierta"):
        asignar_cajero_action.failure('Desasignar caja abierta')

    for driver, usuario in [[driver_cajero, cajero], [driver_operaciones, context.operaciones]]:
        context.page.set_active_driver(driver)
        LogoutAction(context).verify_state(usuario).do().success()


@allure.feature("Gestion de caja")
@allure.story("Asignar cajero")
@allure.title("No se puede desasignar un cajero si la caja esta cerrada parcialmente")
@pytest.mark.usefixtures("generar_sucursal")
def test_desasignar_cajero_caja_cerrada_parcialmente(context):
    driver_cajero = context.driver_manager.main_driver
    caja = context.sucursal.cajas[0]
    cajero = context.cajeros[0]

    cierre = CierreParcial({moneda: 100 for moneda in caja.monedas_permitidas})
    apertura = Apertura({moneda: 100 for moneda in caja.monedas_permitidas})
    apertura_action = AperturaOperableAction(context)

    asignar_cajero_action = AsignarCajeroCajaAction(context)

    with allure.step("El cajero tiene una caja cerrada parcialmente"):
        LoginAction(context).verify_state().do(cajero, caja).success("Apertura Caja")
        apertura_action.fast_forward(cajero, caja, apertura, desbloquear=True)
        CierreParcialCajaAction(context).fast_forward(cajero, caja, cierre)

    driver_operaciones = context.driver_manager.new_driver()
    context.page.set_active_driver(driver_operaciones)
    with allure.step("Operaciones le desasigna su caja"):
        LoginAction(context).verify_state().do(context.operaciones).success("Gestion de caja")
        asignar_cajero_action.verify_state(caja, context.sucursal, cajero.nombre_completo()).do(None)

    with allure.step("Pero no puede porque la caja esta cerrada parcialmente"):
        asignar_cajero_action.failure('Desasignar caja abierta')

    for driver, usuario in [[driver_cajero, cajero], [driver_operaciones, context.operaciones]]:
        context.page.set_active_driver(driver)
        LogoutAction(context).verify_state(usuario).do().success()

# endregion
