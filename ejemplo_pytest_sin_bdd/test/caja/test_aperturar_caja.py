import allure
import pytest

from src.actions.caja_actions import CierreTotalCajaAction
from src.actions.gestion_caja_actions import DesbloquearCajaAction
from src.actions.login_actions import LoginAction
from src.actions.logout_actions import LogoutAction
from src.actions.operable_actions import AperturaOperableAction
from src.dominio.operaciones import Apertura, CierreTotal, Bloqueo


# region Aperturar caja en 0
@allure.feature("Caja")
@allure.story("El usuario apertura una caja")
@allure.title("Aperturar caja en 0")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.parametrize('cant_monedas', [2, 1])
def test_aperturar_caja(context):
    caja = context.sucursal.cajas[0]
    cajero = context.cajeros[0]

    apertura = Apertura({moneda: 0 for moneda in caja.monedas_permitidas})
    apertura_action = AperturaOperableAction(context)

    with allure.step("Un usuario ingresa como cajero"):
        LoginAction(context).verify_state().do(cajero, caja).success("Apertura Caja")

    with allure.step(f"Apertura la caja #{caja.codigo} con montos en 0"):
        apertura_action.verify_state(caja).do(apertura)

    with allure.step("la caja se apertura"):
        apertura_action.success()

    LogoutAction(context).verify_state(cajero).do().success()


# endregion
# region Aperturar caja con montos fuera del margen
@allure.feature("Caja")
@allure.story("El usuario apertura una caja")
@allure.title("Al aperturar con montos fuera del margen, la caja se bloquea")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.parametrize('cant_monedas', [2, 1])
@pytest.mark.parametrize('diferencia', [51, -51])
def test_aperturar_caja_con_bloqueo(context, diferencia):
    caja = context.sucursal.cajas[0]
    cajero = context.cajeros[0]
    monto_apertura = 100

    apertura1 = Apertura({moneda: monto_apertura for moneda in caja.monedas_permitidas})
    apertura2 = Apertura({moneda: monto_apertura + diferencia for moneda in caja.monedas_permitidas})
    apertura_action = AperturaOperableAction(context)

    bloqueo = Bloqueo(caja, cajero, "Apertura", logico=apertura1.montos, reales=apertura2.montos,
                      diferencia={moneda: diferencia for moneda in caja.monedas_permitidas})
    desbloqueo_action = DesbloquearCajaAction(context)

    cierre1 = CierreTotal({moneda: monto_apertura for moneda in caja.monedas_permitidas})
    cierre_action = CierreTotalCajaAction(context)

    with allure.step("Un usuario ingresa como cajero"):
        LoginAction(context).verify_state().do(cajero, caja).success("Apertura Caja")

    # Abro y cierro la caja para inyectarle balance
    apertura_action.fast_forward(cajero, caja, apertura1, desbloquear=True)
    caja.agregar_operacion(apertura1)

    cierre_action.fast_forward(cajero, caja, cierre1)
    caja.agregar_operacion(cierre1)

    with allure.step(f"Apertura la caja {caja.codigo} con montos incorrectos"):
        apertura_action.verify_state(caja).do(apertura2, deberia_bloquearse=True)

    with allure.step("la caja se bloquea"):
        apertura_action.failure()
        LogoutAction(context).verify_state(cajero).do().success()

    with allure.step("El area de operaciones puede ver correctamente la razon de bloqueo y desbloquear la caja"):
        desbloqueo_action.fast_forward(context.operaciones, bloqueo, "Desbloqueo de prueba")


# endregion
# region Aperturar caja con montos dentro del margen
@allure.feature("Caja")
@allure.story("El usuario apertura una caja")
@allure.title("Al aperturar con montos dentro del margen de diferencia, la caja no se bloquea")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.parametrize('cant_monedas', [2, 1])
@pytest.mark.parametrize('diferencia', [50, -50])
def test_aperturar_caja_con_margen(context, diferencia):
    caja = context.sucursal.cajas[0]
    cajero = context.cajeros[0]
    monto_apertura = 100

    apertura1 = Apertura({moneda: monto_apertura for moneda in caja.monedas_permitidas})
    apertura_action = AperturaOperableAction(context)

    cierre1 = CierreTotal({moneda: monto_apertura for moneda in caja.monedas_permitidas})

    apertura2 = Apertura({moneda: monto_apertura + diferencia for moneda in caja.monedas_permitidas})

    with allure.step("Un usuario ingresa como cajero"):
        LoginAction(context).verify_state().do(cajero, caja).success("Apertura Caja")

    # Las cajas se crean en 0, Abro y cierro para que tenga 100
    apertura_action.fast_forward(cajero, caja, apertura1, desbloquear=True)
    caja.agregar_operacion(apertura1)

    CierreTotalCajaAction(context).fast_forward(cajero, caja, cierre1)
    caja.agregar_operacion(cierre1)

    with allure.step(f"Apertura la caja {caja.codigo} con montos dentro del margen"):
        apertura_action.verify_state(caja).do(apertura2)

    with allure.step("la caja se apertura"):
        apertura_action.success()

    LogoutAction(context).verify_state(cajero).do().success()


# endregion
# region Aperturar caja con ARS dentro del margen y PEN fuera del margen
# Le seteo cant monedas en 2 a pesar de que es el default ya que este test solo funciona con 2,
# si eventualmente el default cambia, no me rompe el test
@allure.feature("Caja")
@allure.story("El usuario apertura una caja")
@allure.title("Al aperturar con una moneda dentro del margen de diferencia y otra no, la caja se bloquea")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.parametrize('cant_monedas', [2])
def test_aperturar_caja_con_bloqueo_multimoneda(context):
    caja = context.sucursal.cajas[0]
    cajero = context.cajeros[0]

    apertura = Apertura(dict(zip(caja.monedas_permitidas, [0, 100])))
    bloqueo = Bloqueo(caja, cajero, "Apertura", logico=caja.balance(), reales=apertura.montos,
                      diferencia=apertura.montos)
    desbloqueo_action = DesbloquearCajaAction(context)
    apertura_action = AperturaOperableAction(context)

    with allure.step("Un usuario ingresa como cajero"):
        LoginAction(context).verify_state().do(cajero, caja).success("Apertura Caja")

    with allure.step(f"Apertura la caja {caja.codigo} con una moneda correcta y otra no"):
        apertura_action.verify_state(caja).do(apertura, deberia_bloquearse=True)

    with allure.step("la caja se bloquea"):
        apertura_action.failure()
        LogoutAction(context).verify_state(cajero).do().success()

    with allure.step("El area de operaciones puede ver correctamente la razon de bloqueo y desbloquear la caja"):
        desbloqueo_action.fast_forward(context.operaciones, bloqueo, "Desbloqueo de prueba")

# endregion
