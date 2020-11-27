import allure
import pytest

from src.actions.configuracion_actions import CompletarDatosNuevaSucursalAction, GuardarSucursalAction, \
    ModificarDatosSucursalAction, IrEdicionSucursalAction, CrearCajaAction
from src.actions.login_actions import LoginAction
from src.actions.logout_actions import LogoutAction
from src.dominio.sucursal import Sucursal


# region Crear sucursal


@allure.feature("Sucursal")
@allure.story("El usuario crea una sucursal")
@allure.title("El usuario crea una sucursal con una caja")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.parametrize('crear_sucursal', [False])
def test_crear_sucursal(context):

    with allure.step("El usuario ingresa como Administrador"):
        LoginAction(context).verify_state().do(context.administrador).success("Dashboard")

    with allure.step("crea una sucursal con una caja"):
        CompletarDatosNuevaSucursalAction(context).verify_state().do(context.sucursal).success()
        GuardarSucursalAction(context).verify_state(context.sucursal).do().success(True)
        IrEdicionSucursalAction(context).verify_state().do(context.sucursal)
        caja_action = CrearCajaAction(context)
        for c in context.cajas[0]:
            caja_action.verify_state(context.sucursal).do(c).success()
            context.sucursal.agregar_cajas(c)
        GuardarSucursalAction(context).verify_state(context.sucursal).do().success()
    LogoutAction(context).verify_state(context.administrador).do().success()


# endregion

# region Crear sucursal con codigo y nombre repetido
@allure.feature("Sucursal")
@allure.story("El usuario crea una sucursal")
@allure.title("El nombre y codigo de la sucursal deben ser unicos")
@pytest.mark.usefixtures("generar_sucursal")
def test_crear_sucursal_repetida(context):
    with allure.step("El usuario ingresa como Administrador"):
        LoginAction(context).verify_state().do(context.administrador).success("Dashboard")

    # No se si deberia hacer esto, pero es un caso muy especifico ¯\_(ツ)_/¯
    sucursal_repetida = Sucursal(context.sucursal.nombre, context.sucursal.codigo)

    with allure.step("crea una sucursal con un codigo y nombre repetido"):
        CompletarDatosNuevaSucursalAction(context).verify_state().do(sucursal_repetida).success()

    with allure.step("la sucursal no se crea porque el codigo ya esta en uso"):
        GuardarSucursalAction(context).verify_state(sucursal_repetida).do().failure("Nombre")

    with allure.step("el usuario modifica el nombre"):
        action = ModificarDatosSucursalAction(context)
        action.verify_state(sucursal_repetida)
        sucursal_repetida.nombre = "ARPER 123487"
        action.do(sucursal_repetida.nombre).success()

    with allure.step("la sucursal no se crea porque el codigo ya estaba en uso"):
        GuardarSucursalAction(context).verify_state(sucursal_repetida).do().failure("Codigo")
        LogoutAction(context).verify_state(context.administrador).do().success()


# endregion

# region Crear caja con codigo repetido

@allure.feature("Caja")
@allure.story("El codigo de la caja debe ser unico")
@allure.title("El codigo de la caja debe ser unico")
@pytest.mark.usefixtures("generar_sucursal")
def test_crear_caja_repetida(context):
    crear_caja_action = CrearCajaAction(context)

    with allure.step("El usuario ingresa como Administrador"):
        LoginAction(context).verify_state().do(context.administrador).success("Dashboard")

    with allure.step("Ingresa a editar una sucursal"):
        IrEdicionSucursalAction(context).do(context.sucursal).success()

    with allure.step("Crea una caja con un codigo repetido"):
        crear_caja_action.verify_state(context.sucursal).do(context.sucursal.cajas[0])

    with allure.step("El sistema le indica que el codigo debe ser unico"):
        crear_caja_action.failure("Codigo repetido")
        LogoutAction(context).verify_state(context.administrador).do().success()
# endregion
