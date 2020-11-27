import allure
import pytest

from src.actions.caja_actions import CierreTotalCajaAction, CierreParcialCajaAction
from src.actions.configuracion_actions import IrEdicionSucursalAction, EditarCajaAction, GuardarSucursalAction
from src.actions.login_actions import LoginAction
from src.actions.logout_actions import LogoutAction
from src.actions.operable_actions import AperturaOperableAction
from src.dominio.operaciones import Apertura, CierreTotal, CierreParcial


# region Deshabilitar caja
@allure.feature("Caja")
@allure.story("El usuario deshabilita una caja")
@allure.title("Deshabilitar caja")
@pytest.mark.usefixtures("generar_sucursal")
def test_deshabilitar_caja(context):
    caja = context.sucursal.cajas[0]
    editar_caja_action = EditarCajaAction(context)
    guardar_sucursal_action = GuardarSucursalAction(context)

    with allure.step("El usuario ingresa como Administrador"):
        LoginAction(context).verify_state().do(context.administrador).success("Dashboard")

    with allure.step("deshabilita la caja de una sucursal"):
        IrEdicionSucursalAction(context).do(context.sucursal).success()
        editar_caja_action.verify_state(caja)
        caja.desactivar()
        editar_caja_action.do(caja)

    with allure.step("La caja se deshabilitar correctamente"):
        editar_caja_action.success()
        guardar_sucursal_action.verify_state(context.sucursal).do().success()

    LogoutAction(context).verify_state(context.administrador).do().success()


# endregion

# region Habilitar caja

@allure.feature("Caja")
@allure.story("El usuario deshabilita una caja")
@allure.title("Habilitar caja")
@pytest.mark.usefixtures("generar_sucursal")
def test_habilitar_caja(context):
    caja = context.sucursal.cajas[0]
    ir_edicion_sucursal_action = IrEdicionSucursalAction(context)
    editar_caja_action = EditarCajaAction(context)
    guardar_sucursal_action = GuardarSucursalAction(context)

    with allure.step("El usuario ingresa como Administrador"):
        LoginAction(context).verify_state().do(context.administrador).success("Dashboard")

    with allure.step("deshabilita la caja de la sucursal"):
        ir_edicion_sucursal_action.do(context.sucursal).success()
        editar_caja_action.verify_state(caja)
        caja.desactivar()
        editar_caja_action.do(caja).success()
        guardar_sucursal_action.verify_state(context.sucursal)

    with allure.step("Habilita la caja de la sucursal"):
        editar_caja_action.verify_state(caja)
        caja.activar()
        editar_caja_action.do(caja).success()
        guardar_sucursal_action.verify_state(context.sucursal)

    LogoutAction(context).verify_state(context.administrador).do().success()


# endregion

# region Deshabilitar caja abierta

@allure.feature("Caja")
@allure.story("El usuario deshabilita una caja")
@allure.title("Solo se puede deshabilitar una caja si no esta abierta")
@pytest.mark.usefixtures("generar_sucursal")
def test_deshabilitar_caja_abierta(context):
    driver_cajero = context.driver_manager.main_driver
    caja = context.sucursal.cajas[0]
    cajero = context.cajeros[0]
    editar_caja_action = EditarCajaAction(context)

    apertura = Apertura({moneda: 0 for moneda in caja.monedas_permitidas})
    apertura_action = AperturaOperableAction(context)

    with allure.step("Usuario A ingresa como Cajero"):
        LoginAction(context).verify_state().do(cajero, caja).success("Apertura Caja")

    with allure.step("Apertura la caja"):
        apertura_action.fast_forward(cajero, caja, apertura)

    driver_administrador = context.driver_manager.new_driver()
    context.page.set_active_driver(driver_administrador)
    with allure.step("Usuario B ingresa como administrador"):
        LoginAction(context).verify_state().do(context.administrador).success("Dashboard")

    with allure.step("deshabilita la caja"):
        IrEdicionSucursalAction(context).do(context.sucursal).success()
        editar_caja_action.verify_state(caja)
        caja.desactivar()
        editar_caja_action.do(caja)

    with allure.step("pero no puede porque se encuentra abierta por Usuario B"):
        editar_caja_action.failure(caja, "abierta")
        caja.activar()
        GuardarSucursalAction(context).verify_state(context.sucursal)

    logout_action = LogoutAction(context)
    for driver, usuario in [[driver_administrador, context.administrador], [driver_cajero, cajero]]:
        context.page.set_active_driver(driver)
        logout_action.verify_state(usuario).do().success()


# endregion

# region Deshabilitar caja con saldo

@allure.feature("Caja")
@allure.story("El usuario deshabilita una caja")
@allure.title("Solo se puede deshabilitar una caja si no tiene saldo")
@pytest.mark.usefixtures("generar_sucursal")
def test_deshabilitar_caja_con_saldo(context):
    caja = context.sucursal.cajas[0]
    cajero = context.cajeros[0]

    apertura = Apertura({moneda: 100 for moneda in caja.monedas_permitidas})
    apertura_action = AperturaOperableAction(context)

    cierre = CierreTotal({moneda: 100 for moneda in caja.monedas_permitidas})
    cierre_action = CierreTotalCajaAction(context)

    editar_caja_action = EditarCajaAction(context)

    with allure.step("El usuario cuenta con una caja con saldo"):
        apertura_action.fast_forward(cajero, caja, apertura, desbloquear=True, asignar_operador=True,
                                     redireccionar=False)
        caja.agregar_operacion(apertura)
        cierre_action.fast_forward(cajero, caja, cierre, redirect=False)
        caja.agregar_operacion(cierre)

    with allure.step("Ingresa como administrador"):
        LoginAction(context).verify_state().do(context.administrador).success("Dashboard")

    with allure.step("Intenta deshabilita la caja"):
        IrEdicionSucursalAction(context).verify_state().do(context.sucursal).success()
        editar_caja_action.verify_state(caja)
        caja.desactivar()
        editar_caja_action.do(caja)

    with allure.step("Pero no puede porque su saldo es mayor a 0"):
        editar_caja_action.failure(caja, "con saldo")
        caja.activar()
        GuardarSucursalAction(context).verify_state(context.sucursal)
        LogoutAction(context).verify_state(context.administrador).do().success()


# endregion

# region Deshabilitar caja cerrada parcialmente
@allure.feature("Caja")
@allure.story("El usuario deshabilita una caja")
@allure.title("Solo se puede deshabilitar una caja si no esta cerrada parcialmente")
@pytest.mark.usefixtures("generar_sucursal")
def test_deshabilitar_caja_cerrada_parcialmente(context):
    caja = context.sucursal.cajas[0]
    cajero = context.cajeros[0]

    apertura = Apertura({moneda: 0 for moneda in caja.monedas_permitidas})
    apertura_action = AperturaOperableAction(context)

    cierre = CierreParcial({moneda: 0 for moneda in caja.monedas_permitidas})
    cierre_action = CierreParcialCajaAction(context)

    login_action = LoginAction(context)
    editar_caja_action = EditarCajaAction(context)

    with allure.step("El usuario cuenta con una caja cerrada parcialmente"):
        apertura_action.fast_forward(cajero, caja, apertura, asignar_operador=True,
                                     redireccionar=False)
        caja.agregar_operacion(apertura)
        cierre_action.fast_forward(cajero, caja, cierre, redirect=False)
        caja.agregar_operacion(cierre)

    with allure.step("el usuario ingresa como administrador"):
        login_action.verify_state().do(context.administrador).success("Dashboard")

    with allure.step("e intenta deshabilita la caja"):
        IrEdicionSucursalAction(context).verify_state().do(context.sucursal).success()
        editar_caja_action.verify_state(caja)
        caja.desactivar()
        editar_caja_action.do(caja)

    with allure.step("pero no puede porque se encuentra cerrada parcialmente"):
        editar_caja_action.failure(caja, "abierta")

# endregion
