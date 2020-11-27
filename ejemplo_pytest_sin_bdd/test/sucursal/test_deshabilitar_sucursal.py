import allure
import pytest

from src.actions.caja_actions import CierreTotalCajaAction
from src.actions.configuracion_actions import ModificarEstadoSucursalAction, IrEdicionSucursalAction, CrearCajaAction
from src.actions.login_actions import LoginAction
from src.actions.logout_actions import LogoutAction
from src.actions.operable_actions import AperturaOperableAction
from src.dominio.operaciones import Apertura, CierreTotal


# region Deshabilitar sucursal e intentar crear una caja
@allure.feature("Sucursal")
@allure.story("El usuario deshabilita una sucursal")
@allure.title("Al deshabilitar la sucursal, las cajas se deshabilitan y no se pueden generar nuevas")
@pytest.mark.usefixtures("generar_sucursal")
def test_deshabilitar_sucursal(context):
    modificar_estado_sucursal_action = ModificarEstadoSucursalAction(context)
    ir_edicion_sucursal_action = IrEdicionSucursalAction(context)
    crear_caja_action = CrearCajaAction(context)

    with allure.step("El usuario ingresa como Administrador"):
        LoginAction(context).verify_state().do(context.administrador).success("Dashboard")

    with allure.step("deshabilita la sucursal"):
        modificar_estado_sucursal_action.verify_state(context.sucursal)
        context.sucursal.desactivar()
        modificar_estado_sucursal_action.do(context.sucursal)

    with allure.step("Las cajas se deshabilitan"):
        modificar_estado_sucursal_action.success()

    with allure.step("el usuaro intenta crear una caja"):
        ir_edicion_sucursal_action.verify_state().do(context.sucursal).success()
        caja = context.sucursal.cajas[0]
        caja.codigo = "FF3343"
        crear_caja_action.verify_state(context.sucursal).do(caja)

    with allure.step("pero no puede porque la sucursal esta inactiva"):
        crear_caja_action.failure("Sucursal desactivada")

    LogoutAction(context).verify_state(context.administrador).do().success()


# endregion

# region Deshabilitar sucursal con cajas abiertas
@allure.feature("Sucursal")
@allure.story("El usuario deshabilita una sucursal")
@allure.title("Al deshabilitar la sucursal, no debe haber cajas abiertas")
@pytest.mark.usefixtures("generar_sucursal")
def test_deshabilitar_sucursal_caja_abierta(context):
    driver_cajero = context.driver_manager.main_driver
    caja = context.sucursal.cajas[0]
    cajero = context.cajeros[0]

    login_action = LoginAction(context)

    apertura = Apertura({moneda: 0 for moneda in caja.monedas_permitidas})
    apertura_action = AperturaOperableAction(context)

    modificar_estado_action = ModificarEstadoSucursalAction(context)

    with allure.step("Usuario A ingresa como Cajero"):
        login_action.verify_state().do(cajero, caja).success("Apertura Caja")

    with allure.step(f"Apertura la caja #{caja.codigo} con montos en 0"):
        apertura_action.fast_forward(cajero, caja, apertura)

    driver_administrador = context.driver_manager.new_driver()
    context.page.set_active_driver(driver_administrador)
    with allure.step("Usuario B ingresa como administrador"):
        login_action.verify_state().do(context.administrador).success("Dashboard")

    with allure.step("deshabilita la sucursal"):
        modificar_estado_action.verify_state(context.sucursal)
        context.sucursal.activa = False
        modificar_estado_action.do(context.sucursal)

    with allure.step("pero no puede porque Usuario B aperturo una caja"):
        modificar_estado_action.failure("abierta", context.sucursal, context.sucursal.cajas[0])

    logout_action = LogoutAction(context)
    for driver, usuario in [[driver_administrador, context.administrador], [driver_cajero, cajero]]:
        context.page.set_active_driver(driver)
        logout_action.verify_state(usuario).do().success()


# endregion

# region Deshabilitar sucursal con cajas con saldo
@allure.feature("Sucursal")
@allure.story("El usuario deshabilita una sucursal")
@allure.title("Al deshabilitar la sucursal, no debe haber cajas con saldo")
@pytest.mark.usefixtures("generar_sucursal")
def test_deshabilitar_sucursal_caja_con_saldo(context):
    caja = context.sucursal.cajas[0]
    cajero = context.cajeros[0]

    login_action = LoginAction(context)
    logout_action = LogoutAction(context)
    modificar_estado_action = ModificarEstadoSucursalAction(context)

    apertura = Apertura({moneda: 100 for moneda in caja.monedas_permitidas})
    apertura_action = AperturaOperableAction(context)

    cierre = CierreTotal({moneda: 100 for moneda in caja.monedas_permitidas})
    cierre_action = CierreTotalCajaAction(context)

    with allure.step("Usuario A ingresa como Cajero"):
        login_action.verify_state().do(cajero, caja).success("Apertura Caja")

    with allure.step(f"Apertura la caja {caja.codigo}"):
        apertura_action.fast_forward(cajero, caja, apertura, desbloquear=True)
        caja.agregar_operacion(apertura)

    with allure.step(f"Cierra totalmente la caja {caja.codigo}"):
        cierre_action.verify_state(caja, cierre).do(cajero.password).success()
        caja.agregar_operacion(cierre)
        logout_action.verify_state(cajero).do().success()

    with allure.step("Usuario B ingresa como administrador"):
        login_action.verify_state().do(context.administrador).success("Dashboard")

    with allure.step("deshabilita la sucursal"):
        modificar_estado_action.verify_state(context.sucursal)
        context.sucursal.activa = False
        modificar_estado_action.do(context.sucursal)

    with allure.step(f"pero no puede porque la caja {caja.codigo} tiene saldo"):
        modificar_estado_action.failure("con saldo", context.sucursal, caja)
        logout_action.verify_state(context.administrador).do().success()


# endregion

# region Habilitar sucursal
@allure.feature("Sucursal")
@allure.story("El usuario deshabilita una sucursal")
@allure.title("Al habilitar nuevamente la sucursal, las cajas permanecen deshabilitadas")
@pytest.mark.usefixtures("generar_sucursal")
def test_habilitar_sucursal(context):
    modificar_estado_sucursal_action = ModificarEstadoSucursalAction(context)
    ir_edicion_sucursal_action = IrEdicionSucursalAction(context)

    with allure.step("El usuario ingresa como Administrador"):
        LoginAction(context).verify_state().do(context.administrador).success("Dashboard")

    with allure.step("deshabilita la sucursal"):
        modificar_estado_sucursal_action.verify_state(context.sucursal)
        context.sucursal.desactivar()
        modificar_estado_sucursal_action.do(context.sucursal)

    with allure.step("Las cajas se deshabilitan"):
        modificar_estado_sucursal_action.success()

    with allure.step("habilita nuevamente la sucursal"):
        modificar_estado_sucursal_action.verify_state(context.sucursal)
        context.sucursal.activa = True
        modificar_estado_sucursal_action.do(context.sucursal).success()

    with allure.step("pero las cajas permanecen deshabilitadas"):
        ir_edicion_sucursal_action.verify_state().do(context.sucursal).success()

    LogoutAction(context).verify_state(context.administrador).do().success()

# endregion
