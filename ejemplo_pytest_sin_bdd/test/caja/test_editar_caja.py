from random import choice

import allure
import pytest

from src.actions.configuracion_actions import IrEdicionSucursalAction, EditarCajaAction, GuardarSucursalAction
from src.actions.login_actions import LoginAction, OperadorSinAccionesLoginAction
from src.actions.logout_actions import LogoutAction
from src.actions.operable_actions import AperturaOperableAction


# region Deshabilitar envio y recibo de giros
@allure.feature("Caja")
@allure.story("El usuario edita una caja")
@allure.title("El usuario deshabilita el envio y recibo de giros de una caja")
@pytest.mark.usefixtures("generar_sucursal")
def test_deshabilitar_envio_recibo_giros(context):
    caja = context.sucursal.cajas[0]
    editar_caja_action = EditarCajaAction(context)
    operador_sin_operaciones_action = OperadorSinAccionesLoginAction(context)

    with allure.step("El usuario ingresa como Administrador"):
        LoginAction(context).do(context.administrador).success("Dashboard")

    with allure.step("deshabilita el envio de giros de la caja"):
        IrEdicionSucursalAction(context).do(context.sucursal).success()
        editar_caja_action.verify_state(caja)
        caja.envia_giros = False
        editar_caja_action.do(caja)

    with allure.step("el envio de giros se deshabilita correctamente"):
        editar_caja_action.success()

    with allure.step("deshabilita el recibo de giros de la caja"):
        editar_caja_action.verify_state(caja)
        caja.recibe_giros = False
        editar_caja_action.do(caja)

    with allure.step("el recibo de giros se deshabilita correctamente"):
        editar_caja_action.success()
        LogoutAction(context).verify_state(context.administrador).do().success()

    with allure.step("El cajero asignado intenta aperturar la caja"):
        operador_sin_operaciones_action.verify_state(caja).do(context.cajeros[0])

    with allure.step("Pero no puede porque la caja no tiene operaciones activas"):
        operador_sin_operaciones_action.success()

    LogoutAction(context).verify_state(context.cajeros[0]).do().success()
# endregion

# region deshabilitar moneda del recibo de giros


@allure.feature("Caja")
@allure.story("El usuario edita una caja")
@allure.title("El usuario deshabilita una moneda")
@pytest.mark.usefixtures("generar_sucursal")
def test_deshabilitar_moneda_apertura(context):
    caja = context.sucursal.cajas[0]
    editar_caja_action = EditarCajaAction(context)

    with allure.step("El usuario ingresa como Administrador"):
        LoginAction(context).verify_state().do(context.administrador).success("Dashboard")

    moneda_eliminada = choice(tuple(caja.monedas_permitidas))
    with allure.step(f"deshabilita la moneda {moneda_eliminada.codigo}"):
        IrEdicionSucursalAction(context).verify_state().do(context.sucursal).success()
        editar_caja_action.verify_state(caja)
        caja.deshabilitar_moneda_giro("Ambos", moneda_eliminada)
        editar_caja_action.do(caja).success()
        GuardarSucursalAction(context).verify_state(context.sucursal).do().success()
        LogoutAction(context).verify_state(context.administrador).do().success()

    with allure.step("El cajero asignado ingresa al sistema"):
        LoginAction(context).verify_state().do(context.cajeros[0], caja).success("Apertura Caja")

    with allure.step("Solo se muestra una moneda operable"):
        AperturaOperableAction(context).verify_state(caja)

    LogoutAction(context).verify_state(context.cajeros[0]).do().success()
# endregion
