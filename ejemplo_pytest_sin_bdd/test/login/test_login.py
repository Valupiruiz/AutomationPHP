import allure
import pytest
from allure_commons.types import LinkType

from src.actions.login_actions import OperadorSinOperableLoginAction, LoginIncorrectoAction
from src.actions.logout_actions import LogoutAction

# region Validacion de campos de login


@allure.feature("Login")
@allure.title("Los campos obligatorios para ingresar al sistema son DNI, Maill y contraseña")
def test_campos_login(context):
    LoginIncorrectoAction(context).verify_state().do().success()


# endregion

# region Loguearse como cajero sin caja asignada

@allure.feature("Login")
@allure.title("Al ingresar como cajero sin una caja asignada, se muestra un mensaje indicandolo")
def test_cajero_sin_caja(context):
    OperadorSinOperableLoginAction(context).verify_state().do(context.cajeros[0]).success()
    LogoutAction(context).verify_state(context.cajeros[0]).do().success()

# endregion

# region Loguearse como operador de boveda sin boveda asignada
@pytest.mark.usefixtures("lock_boveda")
@allure.feature("Login")
@allure.title("Al ingresar como operador de boveda sin una asignada, se muestra un mensaje indicandolo")
def test_operador_sin_boveda(context):
    OperadorSinOperableLoginAction(context).verify_state().do(context.operador_remesas).success()
    LogoutAction(context).verify_state(context.operador_remesas).do().success()
# endregion
