import allure
import pytest

from src.actions.caja_actions import CierreParcialCajaAction
from src.actions.login_actions import LoginAction
from src.actions.logout_actions import LogoutAction
from src.actions.operable_actions import AperturaOperableAction
from src.dominio.operaciones import Apertura, CierreParcial


# region Cerrar parcialmente en 0
@allure.feature("Caja")
@allure.story("El usuario realiza un cierre parcial")
@allure.title("El usuario realiza un cierre parcial")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.parametrize('cant_monedas', [2, 1])
def test_cierre_parcial(context):
    caja = context.sucursal.cajas[0]
    cajero = context.cajeros[0]

    apertura = Apertura({moneda: 0 for moneda in caja.monedas_permitidas})
    apertura_action = AperturaOperableAction(context)

    cierre = CierreParcial({moneda: 0 for moneda in caja.monedas_permitidas})
    cierre_action = CierreParcialCajaAction(context)

    with allure.step("Un usuario ingresa como cajero"):
        LoginAction(context).verify_state().do(cajero, caja).success("Apertura Caja")

    with allure.step(f"Apertura la caja {caja.codigo} con montos en 0"):
        apertura_action.fast_forward(cajero, caja, apertura)

    with allure.step("Realiza un cierre parcial con montos correctos"):
        cierre_action.verify_state(caja, cierre).do(cajero.password)

    with allure.step("La caja se cierra parcialmente"):
        cierre_action.success()

    LogoutAction(context).verify_state(cajero).do().success()


# endregion

# region realizar cierre parcial fuera del margen
@allure.feature("Caja")
@allure.story("El usuario realiza un cierre parcial")
@allure.title("Al realizar un cierre parcial, no importa la diferencia de montos")
@pytest.mark.usefixtures("generar_sucursal")
def test_cierre_parcial_con_diferencia(context):
    caja = context.sucursal.cajas[0]
    cajero = context.cajeros[0]

    apertura = Apertura({moneda: 0 for moneda in caja.monedas_permitidas})
    apertura_action = AperturaOperableAction(context)

    cierre_parcial = CierreParcial({moneda: 5000 for moneda in caja.monedas_permitidas})
    cierre_action = CierreParcialCajaAction(context)

    with allure.step("Un usuario ingresa como cajero"):
        LoginAction(context).verify_state().do(cajero, caja).success("Apertura Caja")

    with allure.step(f"Apertura la caja {caja.codigo} con montos en 0"):
        apertura_action.fast_forward(cajero, caja, apertura)

    with allure.step("Realiza un cierre parcial con montos fuera del margen de diferencia"):
        cierre_action.verify_state(caja, cierre_parcial).do(cajero.password)

    with allure.step("La caja se cierra parcialmente de todas maneras"):
        cierre_action.success()

    LogoutAction(context).verify_state(cajero).do().success()


# endregion


# region aperturar parcialmente con montos fuera del margen
@allure.feature("Caja")
@allure.story("El usuario realiza un cierre parcial")
@allure.title("Al realizar una apertura parcial, no importa la diferencia de montos")
@pytest.mark.usefixtures("generar_sucursal")
def test_apertura_parcial_con_diferencia(context):
    caja = context.sucursal.cajas[0]
    cajero = context.cajeros[0]

    apertura = Apertura({moneda: 0 for moneda in caja.monedas_permitidas})
    apertura2 = Apertura({moneda: 1000 for moneda in caja.monedas_permitidas})
    apertura_action = AperturaOperableAction(context)

    cierre = CierreParcial({moneda: 0 for moneda in caja.monedas_permitidas})
    cierre_action = CierreParcialCajaAction(context)

    with allure.step("Un usuario ingresa como cajero"):
        LoginAction(context).verify_state().do(cajero, caja).success("Apertura Caja")

    with allure.step(f"Apertura la caja {caja.codigo} con montos en 0"):
        apertura_action.fast_forward(cajero, caja, apertura)

    with allure.step("Realiza un cierre parcial con montos correctos"):
        cierre_action.fast_forward(cajero, caja, cierre)

    with allure.step(f"Apertura la caja {caja.codigo} con montos fuera del rango"):
        apertura_action.verify_state(caja).do(apertura2)

    with allure.step("La caja se apertura correctamente"):
        apertura_action.success()

    LogoutAction(context).verify_state(cajero).do().success()
# endregion
