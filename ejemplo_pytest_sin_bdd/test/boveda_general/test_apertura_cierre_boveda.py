import allure
import pytest

from src.actions.login_actions import LoginAction
from src.actions.logout_actions import LogoutAction
from src.actions.operable_actions import AperturaOperableAction, CierreOperableAction
from src.dominio.operaciones import Apertura, CierreTotal


# Region Aperturar y cerrar Boveda en 0
@pytest.mark.usefixtures("lock_boveda")
@allure.feature("Boveda General")
@allure.story("El usuario apertura una boveda y luego la cierra")
@allure.title("Aperturar y cerrar boveda")
def test_aperturar_cerrar_boveda(context):
    boveda = context.boveda
    operador = context.operador_remesas

    apertura = Apertura({moneda: 0 for moneda in boveda.monedas_permitidas})
    apertura_action = AperturaOperableAction(context)

    cierre = CierreTotal({moneda: 0 for moneda in boveda.monedas_permitidas})
    cierre_action = CierreOperableAction(context)

    with allure.step("Un usuario ingresa como operador de boveda"):
        LoginAction(context).verify_state().do(operador, boveda).success("Apertura Boveda")

    with allure.step(f"Apertura la caja {boveda.codigo} con montos en 0"):
        apertura_action.verify_state(boveda).do(apertura)

    with allure.step("la caja se apertura"):
        apertura_action.success()

    with allure.step("Realiza un cierre total con montos correctos"):
        cierre_action.verify_state(boveda, cierre).do(operador.password)

    with allure.step("La boveda se cierra totalmente"):
        cierre_action.success()

    LogoutAction(context).verify_state(operador).do().success()
# endregion
