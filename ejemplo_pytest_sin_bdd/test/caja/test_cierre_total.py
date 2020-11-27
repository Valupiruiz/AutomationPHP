import allure
import pytest

from src.actions.caja_actions import CierreTotalCajaAction
from src.actions.gestion_caja_actions import DesbloquearCajaAction
from src.actions.login_actions import LoginAction
from src.actions.logout_actions import LogoutAction
from src.actions.operable_actions import AperturaOperableAction
from src.dominio.operaciones import Apertura, CierreTotal, Bloqueo


# region Cierre total en 0
@allure.feature("Caja")
@allure.story("El usuario realiza un cierre total")
@allure.title("El usuario realiza un cierre total")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.parametrize('cant_monedas', [2, 1])
def test_cierre_total(context):
    caja = context.sucursal.cajas[0]
    cajero = context.cajeros[0]

    apertura = Apertura({moneda: 0 for moneda in caja.monedas_permitidas})
    apertura_action = AperturaOperableAction(context)

    cierre = CierreTotal({moneda: 0 for moneda in caja.monedas_permitidas})
    cierre_action = CierreTotalCajaAction(context)

    with allure.step("Un usuario ingresa como cajero"):
        LoginAction(context).verify_state().do(cajero, caja).success("Apertura Caja")

    with allure.step(f"Apertura la caja {caja.codigo} con montos en 0"):
        apertura_action.fast_forward(cajero, caja, apertura)

    with allure.step("Realiza un cierre total con montos correctos"):
        cierre_action.verify_state(caja, cierre).do(cierre)

    with allure.step("La caja se cierra totalmente"):
        cierre_action.success()

    LogoutAction(context).verify_state(cajero).do().success()


# endregion

# region Cierre total con montos mayores al margen

@allure.feature("Caja")
@allure.story("El usuario realiza un cierre total")
@allure.title("Al realizar un cierre total con una diferencia de montos mayor al permitido, la caja se bloquea")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.parametrize('cant_monedas', [2, 1])
@pytest.mark.parametrize('diferencia', [51, -51])
def test_cierre_total_con_bloqueo(context, diferencia):
    caja = context.sucursal.cajas[0]
    cajero = context.cajeros[0]
    monto_apertura = 100

    apertura = Apertura({moneda: monto_apertura for moneda in caja.monedas_permitidas})
    apertura_action = AperturaOperableAction(context)

    cierre = CierreTotal({moneda: monto_apertura + diferencia for moneda in caja.monedas_permitidas})
    cierre_action = CierreTotalCajaAction(context)

    bloqueo = Bloqueo(caja, cajero, "Cierre total", logico=apertura.montos, reales=cierre.montos,
                      diferencia={moneda: diferencia for moneda in caja.monedas_permitidas})
    desbloqueo_action = DesbloquearCajaAction(context)

    with allure.step("Un usuario ingresa como cajero"):
        LoginAction(context).verify_state().do(cajero, caja).success("Apertura Caja")

    with allure.step(f"Apertura la caja {caja.codigo}"):
        apertura_action.fast_forward(cajero, caja, apertura, desbloquear=True)

    with allure.step("Realiza un cierre total con montos fuera del margen de diferencia"):
        cierre_action.verify_state(caja, cierre).do(cajero.password)

    with allure.step("la caja se bloquea"):
        cierre_action.failure("Bloqueo")
        LogoutAction(context).verify_state(cajero).do().success()

    with allure.step("El area de operaciones puede ver correctamente la razon de bloqueo y desbloquear la caja"):
        desbloqueo_action.fast_forward(context.operaciones, bloqueo, "Desbloqueo de prueba")


# endregion

# region Cierre total con montos dentro del margen

@allure.feature("Caja")
@allure.story("El usuario realiza un cierre total")
@allure.title("Al realizar un cierre total con una diferencia de montos permitida, la caja se cierra correctamente")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.parametrize('cant_monedas', [2])
@pytest.mark.parametrize('diferencia', [50, -50])
def test_cierre_total_con_diferencia(context, diferencia):
    caja = context.sucursal.cajas[0]
    cajero = context.cajeros[0]
    monto = 100

    apertura = Apertura({moneda: monto for moneda in caja.monedas_permitidas})
    apertura_action = AperturaOperableAction(context)

    cierre = CierreTotal({moneda: monto + diferencia for moneda in caja.monedas_permitidas})
    cierre_action = CierreTotalCajaAction(context)

    with allure.step("Un usuario ingresa como cajero"):
        LoginAction(context).verify_state().do(cajero, caja).success("Apertura Caja")

    with allure.step(f"Apertura la caja {caja.codigo}"):
        apertura_action.fast_forward(cajero, caja, apertura, desbloquear=True)

    with allure.step("Realiza un cierre total con montos dentro del margen"):
        cierre_action.verify_state(caja, cierre).do(cajero.password)

    with allure.step("La caja se cierra correctamente"):
        cierre_action.success()
    LogoutAction(context).verify_state(cajero).do().success()


# endregion

# region cierre total con ARS en 0 y PEN fuera del margen

@allure.feature("Caja")
@allure.story("El usuario realiza un cierre total")
@allure.title("Al realizar un cierre total con una moneda correcta y la otra no, la caja se bloquea")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.parametrize('cant_monedas', [2])
def test_cierre_total_con_bloqueo_multimoneda(context):
    caja = context.sucursal.cajas[0]
    cajero = context.cajeros[0]

    apertura = Apertura({moneda: 0 for moneda in caja.monedas_permitidas})
    apertura_action = AperturaOperableAction(context)

    cierre = CierreTotal(dict(zip(caja.monedas_permitidas, [0, 100])))
    cierre_action = CierreTotalCajaAction(context)

    bloqueo = Bloqueo(caja, cajero, "Cierre total", logico=apertura.montos, reales=cierre.montos,
                      diferencia=cierre.montos)
    desbloqueo_action = DesbloquearCajaAction(context)

    with allure.step("Un usuario ingresa como cajero"):
        LoginAction(context).verify_state().do(cajero, caja).success("Apertura Caja")

    with allure.step(f"Apertura la caja {caja.codigo} con montos en 0"):
        apertura_action.fast_forward(cajero, caja, apertura)

    with allure.step("Realiza un cierre total con montos fuera del margen de diferencia"):
        cierre_action.verify_state(caja, cierre).do(cajero.password)

    with allure.step("la caja se bloquea"):
        cierre_action.failure("Bloqueo")
        LogoutAction(context).verify_state(cajero).do().success()

    with allure.step("El area de operaciones puede ver correctamente la razon de bloqueo y desbloquear la caja"):
        desbloqueo_action.fast_forward(context.operaciones, bloqueo, "Desbloqueo de prueba")
# endregion
