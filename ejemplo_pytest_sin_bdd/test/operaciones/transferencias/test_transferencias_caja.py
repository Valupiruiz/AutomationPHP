from random import randint

import allure
import pytest

from src.actions.caja_actions import CierreTotalCajaAction
from src.actions.configuracion_actions import IrEdicionSucursalAction, EditarCajaAction
from src.actions.login_actions import LoginAction
from src.actions.logout_actions import LogoutAction
from src.actions.operable_actions import AperturaOperableAction
from src.actions.transferencias_actions import SeleccionarDestinoTransferenciaAction, CompletarTransferenciaAction, \
    RecibirTransferenciaAction, ConfirmarTransferenciaAction, TransferenciaFinalizadaAction, \
    ReportarProblemaTranferenciaAction
from src.dominio.operaciones import Apertura, CierreTotal, Transferencia


# region Transferencia Caja -> Caja

@allure.feature("Caja")
@allure.story("Un cajero genera una extraccion desde su caja a otra")
@allure.title("Un cajero genera una extraccion desde su caja a otra")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.parametrize('cant_cajas', [2])
@pytest.mark.parametrize('cant_cajeros', [2])
@pytest.mark.parametrize('cant_monedas', [2, 1])
def test_transferencia_caja_caja(context):
    driver_origen = context.driver_manager.main_driver
    caja_origen = context.sucursal.cajas[0]
    cajero_origen = context.cajeros[0]
    apertura_origen = Apertura({m: 1000 for m in caja_origen.monedas_permitidas})

    caja_destino = context.sucursal.cajas[1]
    cajero_destino = context.cajeros[1]
    apertura_destino = Apertura({m: 0 for m in caja_origen.monedas_permitidas})

    monedas = caja_origen.monedas_permitidas.intersection(caja_destino.monedas_permitidas)
    transferencia = Transferencia(caja_origen, caja_destino,
                                  {moneda: randint(1, 150) for moneda in monedas})

    login_action = LoginAction(context)
    logout_action = LogoutAction(context)
    apertura_action = AperturaOperableAction(context)
    cierre_caja_action = CierreTotalCajaAction(context)
    completar_transferencia_action = CompletarTransferenciaAction(context)
    recibir_transferencia_action = RecibirTransferenciaAction(context)
    confirmar_transferencia_action = ConfirmarTransferenciaAction(context)
    transferencia_finalizada_action = TransferenciaFinalizadaAction(context)

    with allure.step("El cajero de origen apertura su caja"):
        login_action.verify_state().do(cajero_origen, caja_origen).success("Apertura Caja")
        apertura_action.fast_forward(cajero_origen, caja_origen, apertura_origen, desbloquear=True)
        caja_origen.agregar_operacion(apertura_origen)

    driver_destino = context.driver_manager.new_driver()
    context.page.set_active_driver(driver_destino)
    with allure.step("El cajero de destino apertura su caja"):
        login_action.verify_state().do(cajero_destino, caja_destino).success("Apertura Caja")
        apertura_action.fast_forward(cajero_destino, caja_destino, apertura_destino)
        caja_destino.agregar_operacion(apertura_destino)

    context.page.set_active_driver(driver_origen)
    with allure.step(f"El cajero de origen genera un deposito en la caja destino"):
        SeleccionarDestinoTransferenciaAction(context).verify_state(caja_origen).do(caja_destino).success()
        completar_transferencia_action.verify_state(transferencia).do(cajero_origen.password)
        transferencia.codigo = completar_transferencia_action.success()
        caja_origen.agregar_operacion(transferencia)

    context.page.set_active_driver(driver_destino)
    with allure.step("El cajero de destino recibe la transferencia y la confirma con montos correctos"):
        recibir_transferencia_action.verify_state(caja_destino).do(transferencia).success()
        confirmar_transferencia_action.verify_state(caja_destino, transferencia).do(cajero_destino.password).success()
        caja_destino.agregar_operacion(transferencia)

    context.page.set_active_driver(driver_origen)
    with allure.step("La transferencia se contabiliza"):
        transferencia_finalizada_action.verify_state(caja_origen).do(transferencia)
        transferencia.estado = transferencia_finalizada_action.success("Contabilizada")

    with allure.step("El cajero de origen realiza un cierre total correctamente"):
        cierre_caja_origen = CierreTotal(caja_origen.balance())
        cierre_caja_action.fast_forward(cajero_origen, caja_origen, cierre_caja_origen)
        caja_origen.agregar_operacion(cierre_caja_origen)
        logout_action.verify_state(cajero_origen).do().success()

    context.page.set_active_driver(driver_destino)
    with allure.step("El cajero de destino realiza un cierre total correctamente"):
        cierre_caja_destino = CierreTotal(caja_destino.balance())
        cierre_caja_action.fast_forward(cajero_destino, caja_destino, cierre_caja_destino)
        logout_action.verify_state(cajero_destino).do().success()


# endregion

# region Transferencia Caja A -> Caja B -> Caja A

@allure.feature("Caja")
@allure.story("Un cajero genera una extraccion desde su caja a otra")
@allure.title("Un cajero recibe una extraccion y genera otra")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.parametrize('cant_cajas', [2])
@pytest.mark.parametrize('cant_cajeros', [2])
@pytest.mark.parametrize('cant_monedas', [2, 1])
@pytest.mark.parametrize('monto_apertura_destino', [150, 0])
def test_transferencia_caja_caja_caja(context, monto_apertura_destino):
    cajero_origen = context.cajeros[0]
    caja_origen = context.sucursal.cajas[0]
    monto_apertura_origen = 1000
    apertura_origen = Apertura({m: monto_apertura_origen for m in caja_origen.monedas_permitidas})

    driver_destino = context.driver_manager.main_driver
    cajero_destino = context.cajeros[1]
    caja_destino = context.sucursal.cajas[1]
    apertura_destino = Apertura({m: monto_apertura_destino for m in caja_destino.monedas_permitidas})

    monedas = caja_origen.monedas_permitidas.intersection(caja_destino.monedas_permitidas)
    transferencia = Transferencia(caja_origen, caja_destino,
                                  {moneda: randint(1, monto_apertura_origen) for moneda in monedas})

    login_action = LoginAction(context)
    logout_action = LogoutAction(context)
    apertura_action = AperturaOperableAction(context)
    cierre_caja_action = CierreTotalCajaAction(context)
    completar_transferencia_action = CompletarTransferenciaAction(context)
    confirmar_transferencia_action = ConfirmarTransferenciaAction(context)
    transferencia_finalizada_action = TransferenciaFinalizadaAction(context)

    with allure.step("El cajero de destino apertura su caja"):
        login_action.verify_state().do(cajero_destino, caja_destino).success("Apertura Caja")
        apertura_action.fast_forward(cajero_destino, caja_destino,
                                     apertura_destino, desbloquear=monto_apertura_destino > 0)
        caja_destino.agregar_operacion(apertura_destino)

    driver_origen = context.driver_manager.new_driver()
    context.page.set_active_driver(driver_origen)
    with allure.step("El cajero de origen apertura su caja"):
        login_action.verify_state().do(cajero_origen, caja_origen).success("Apertura Caja")
        apertura_action.fast_forward(cajero_origen, caja_origen, apertura_origen, desbloquear=True)
        caja_origen.agregar_operacion(apertura_origen)

    with allure.step("El cajero de origen genera una transferencia de salida hacia caja destino"):
        transferencia.codigo = completar_transferencia_action.fast_forward(cajero_origen, transferencia)
        caja_origen.agregar_operacion(transferencia)

    context.page.set_active_driver(driver_destino)
    with allure.step("El cajero de destino recibe la transferencia y la confirma con montos correctos"):
        confirmar_transferencia_action.fast_forward(cajero_destino, transferencia)
        caja_destino.agregar_operacion(transferencia)

    context.page.set_active_driver(driver_origen)
    with allure.step("La transferencia se contabiliza"):
        transferencia.estado = transferencia_finalizada_action.fast_forward(transferencia)

    context.page.set_active_driver(driver_destino)
    transferencia2 = Transferencia(caja_destino, caja_origen,
                                   {moneda: monto + monto_apertura_destino
                                    for moneda, monto in transferencia.montos.items()})
    with allure.step("El cajero de destino genera una nueva transferencia hacia origen"):
        transferencia2.codigo = completar_transferencia_action.fast_forward(cajero_destino, transferencia2)
        caja_destino.agregar_operacion(transferencia2)

    context.page.set_active_driver(driver_origen)
    with allure.step("El cajero de origen recibe el deposito y lo confirma"):
        confirmar_transferencia_action.fast_forward(cajero_destino, transferencia2)

    context.page.set_active_driver(driver_destino)
    with allure.step("La transferencia se contabiliza"):
        transferencia2.estado = transferencia_finalizada_action.fast_forward(transferencia2)
        caja_origen.agregar_operacion(transferencia2)

    with allure.step("El cajero de destino realiza un cierre total correctamente"):
        cierre_caja_destino = CierreTotal(caja_destino.balance())
        cierre_caja_action.fast_forward(cajero_destino, caja_destino, cierre_caja_destino)
        logout_action.verify_state(cajero_destino).do().success()

    context.page.set_active_driver(driver_origen)
    with allure.step("El cajero de origen realiza un cierre total correctamente"):
        cierre_caja_origen = CierreTotal(caja_origen.balance())
        cierre_caja_action.fast_forward(cajero_origen, caja_origen, cierre_caja_origen)
        caja_origen.agregar_operacion(cierre_caja_origen)
        logout_action.verify_state(cajero_origen).do().success()


# endregion

# region Transferencia Caja A -> Caja B -> Caja A (Caja B sin saldo)
@allure.feature("Caja")
@allure.story("Un cajero genera una extraccion desde su caja a otra")
@allure.title("Un cajero recibe una extraccion e intenta generar otra pero no cuenta con el saldo suficiente")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.parametrize('cant_cajas', [2])
@pytest.mark.parametrize('cant_cajeros', [2])
@pytest.mark.parametrize('cant_monedas', [2, 1])
@pytest.mark.parametrize('monto_apertura_destino', [150, 0])
def test_transferencia_caja_caja_caja_sin_saldo(context, monto_apertura_destino):
    cajero_origen = context.cajeros[0]
    caja_origen = context.sucursal.cajas[0]
    monto_apertura_origen = 1000
    apertura_origen = Apertura({m: monto_apertura_origen for m in caja_origen.monedas_permitidas})

    caja_destino = context.sucursal.cajas[1]
    driver_destino = context.driver_manager.main_driver
    cajero_destino = context.cajeros[1]
    apertura_destino = Apertura({m: monto_apertura_destino for m in caja_destino.monedas_permitidas})

    monedas = caja_origen.monedas_permitidas.intersection(caja_destino.monedas_permitidas)
    transferencia = Transferencia(caja_origen, caja_destino,
                                  {moneda: randint(1, 100) for moneda in monedas})

    login_action = LoginAction(context)
    logout_action = LogoutAction(context)
    apertura_action = AperturaOperableAction(context)
    completar_transferencia_action = CompletarTransferenciaAction(context)
    confirmar_transferencia_action = ConfirmarTransferenciaAction(context)
    transferencia_finalizada_action = TransferenciaFinalizadaAction(context)

    with allure.step("El cajero de destino apertura su caja"):
        login_action.verify_state().do(cajero_destino, caja_destino).success("Apertura Caja")
        apertura_action.fast_forward(cajero_destino, caja_destino,
                                     apertura_destino, desbloquear=monto_apertura_destino > 0)
        caja_destino.agregar_operacion(apertura_destino)

    driver_origen = context.driver_manager.new_driver()
    context.page.set_active_driver(driver_origen)
    with allure.step("El cajero de origen apertura su caja"):
        login_action.verify_state().do(cajero_origen, caja_origen).success("Apertura Caja")
        apertura_action.fast_forward(cajero_origen, caja_origen, apertura_origen, desbloquear=True)
        caja_origen.agregar_operacion(apertura_origen)

    with allure.step("El cajero de origen genera una transferencia de salida hacia caja destino"):
        transferencia.codigo = completar_transferencia_action.fast_forward(cajero_origen, transferencia)
        caja_origen.agregar_operacion(transferencia)

    context.page.set_active_driver(driver_destino)
    with allure.step("El cajero de destino recibe la transferencia y la confirma con montos correctos"):
        confirmar_transferencia_action.fast_forward(cajero_destino, transferencia)
        caja_destino.agregar_operacion(transferencia)

    context.page.set_active_driver(driver_origen)
    with allure.step("La transferencia se contabiliza"):
        transferencia.estado = transferencia_finalizada_action.fast_forward(transferencia)

    context.page.set_active_driver(driver_destino)
    transferencia2 = Transferencia(caja_destino, caja_origen,
                                   {moneda: monto + monto_apertura_destino + 1
                                    for moneda, monto in transferencia.montos.items()})
    with allure.step("El cajero de destino intenta generar una nueva transferencia hacia origen"):
        SeleccionarDestinoTransferenciaAction(context).verify_state(caja_destino).do(caja_origen).success()
        completar_transferencia_action.verify_state(transferencia2).do(cajero_destino.password)

    with allure.step("Pero no puede porque no cuenta con saldo"):
        completar_transferencia_action.failure("Sin Saldo")

    for driver, usuario in [[driver_origen, cajero_origen], [driver_destino, cajero_destino]]:
        context.page.set_active_driver(driver)
        logout_action.verify_state(usuario).do().success()


# endregion

# region Transferencia  Caja A -> Caja B (No hay monedas en comun entre Caja A y Caja B)
@allure.feature("Caja")
@allure.story("Un cajero genera una extraccion desde su caja a otra")
@allure.title("Al no haber monedas en comun entre las cajas, no se puede transferir")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.parametrize('cant_cajas', [2])
@pytest.mark.parametrize('cant_cajeros', [2])
def test_transferencia_caja_caja_sin_monedas(context):
    driver_origen = context.driver_manager.main_driver
    cajero_origen = context.cajeros[0]
    cajero_destino = context.cajeros[1]

    caja_origen = context.sucursal.cajas[0]
    caja_destino = context.sucursal.cajas[1]
    moneda_origen = 'ARS'
    moneda_destino = 'PEN'
    monedas_eliminada_origen = [moneda for moneda in caja_origen.monedas if moneda.codigo != moneda_origen]
    monedas_eliminada_destino = [moneda for moneda in caja_destino.monedas if moneda.codigo != moneda_destino]

    login_action = LoginAction(context)
    logout_action = LogoutAction(context)
    apertura_action = AperturaOperableAction(context)
    seleccionar_destinatario_action = SeleccionarDestinoTransferenciaAction(context)
    editar_caja_action = EditarCajaAction(context)

    with allure.step("El usuario ingresa como Administrador"):
        LoginAction(context).verify_state().do(context.administrador).success("Dashboard")

    IrEdicionSucursalAction(context).verify_state().do(context.sucursal).success()
    for c, monedas in [[caja_origen, monedas_eliminada_origen], [caja_destino, monedas_eliminada_destino]]:
            editar_caja_action.verify_state(c)
            [c.deshabilitar_moneda_giro("Ambos", moneda) for moneda in monedas]
            editar_caja_action.do(c).success()
    logout_action.verify_state(context.administrador).do().success()

    apertura_origen = Apertura({m: 0 for m in caja_origen.monedas_permitidas})
    apertura_destino = Apertura({m: 0 for m in caja_destino.monedas_permitidas})

    with allure.step("El cajero de origen apertura su caja"):
        login_action.verify_state().do(cajero_origen, caja_origen).success("Apertura Caja")
        apertura_action.fast_forward(cajero_origen, caja_origen, apertura_origen)
        caja_origen.agregar_operacion(apertura_origen)

    driver_destino = context.driver_manager.new_driver()
    context.page.set_active_driver(driver_destino)
    with allure.step("El cajero de destino apertura su caja"):
        login_action.verify_state().do(cajero_destino, caja_destino).success("Apertura Caja")
        apertura_action.fast_forward(cajero_destino, caja_destino, apertura_destino)
        caja_destino.agregar_operacion(apertura_destino)

    context.page.set_active_driver(driver_origen)
    with allure.step("El cajero de origen intenta generar una transferencia de salida hacia caja destino"):
        seleccionar_destinatario_action.verify_state(caja_origen).do(caja_destino)

    with allure.step("Pero no puede porque no hay monedas en comun entre las cajas"):
        seleccionar_destinatario_action.failure()

    for driver, usuario in [[driver_destino, cajero_destino], [driver_origen, cajero_origen]]:
        context.page.set_active_driver(driver)
        logout_action.verify_state(usuario).do().success()


# endregion

# region Transferencia Caja A -> Caja B (Caja B Reporta un error)

@allure.feature("Caja")
@allure.story("Un cajero genera una extraccion desde su caja a otra")
@allure.title("Un cajero genera una extraccion, destino indica que hubo un error")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.parametrize('cant_cajas', [2])
@pytest.mark.parametrize('cant_cajeros', [2])
@pytest.mark.parametrize('cant_monedas', [2, 1])
@pytest.mark.parametrize('monto_apertura_destino', [0, 150])
def test_transferencia_caja_caja_con_error(context, monto_apertura_destino):
    driver_origen = context.driver_manager.main_driver
    caja_origen = context.sucursal.cajas[0]
    cajero_origen = context.cajeros[0]
    apertura_origen = Apertura({m: 1000 for m in caja_origen.monedas_permitidas})

    caja_destino = context.sucursal.cajas[1]
    cajero_destino = context.cajeros[1]
    apertura_destino = Apertura({m: monto_apertura_destino for m in caja_origen.monedas_permitidas})

    monedas = caja_origen.monedas_permitidas.intersection(caja_destino.monedas_permitidas)
    transferencia = Transferencia(caja_origen, caja_destino,
                                  {moneda: randint(1, 150) for moneda in monedas})

    login_action = LoginAction(context)
    logout_action = LogoutAction(context)
    apertura_action = AperturaOperableAction(context)
    cierre_caja_action = CierreTotalCajaAction(context)
    completar_transferencia_action = CompletarTransferenciaAction(context)
    recibir_transferencia_action = RecibirTransferenciaAction(context)
    problema_transferencia_action = ReportarProblemaTranferenciaAction(context)
    transferencia_finalizada_action = TransferenciaFinalizadaAction(context)

    with allure.step("El cajero de origen apertura su caja"):
        login_action.verify_state().do(cajero_origen, caja_origen).success("Apertura Caja")
        apertura_action.fast_forward(cajero_origen, caja_origen, apertura_origen, desbloquear=True)
        caja_origen.agregar_operacion(apertura_origen)

    driver_destino = context.driver_manager.new_driver()
    context.page.set_active_driver(driver_destino)
    with allure.step("El cajero de destino apertura su caja"):
        login_action.verify_state().do(cajero_destino, caja_destino).success("Apertura Caja")
        apertura_action.fast_forward(cajero_destino, caja_destino, apertura_destino, desbloquear=monto_apertura_destino > 0)
        caja_destino.agregar_operacion(apertura_destino)

    context.page.set_active_driver(driver_origen)
    with allure.step(f"El cajero de origen genera un deposito en la caja destino"):
        transferencia.codigo = completar_transferencia_action.fast_forward(cajero_origen, transferencia)
        caja_origen.agregar_operacion(transferencia)

    context.page.set_active_driver(driver_destino)
    with allure.step("El cajero de destino reporta un error en la transferencia"):
        recibir_transferencia_action.verify_state(caja_destino).do(transferencia).success()
        problema_transferencia_action.verify_state(caja_destino, transferencia).do("Reporte de Prueba",
                                                                                   cajero_destino.password)
        problema_transferencia_action.success()
        caja_destino.agregar_operacion(transferencia)

    context.page.set_active_driver(driver_origen)
    with allure.step("La transferencia se marca con errores"):
        transferencia_finalizada_action.verify_state(caja_origen).do(transferencia)
        transferencia.estado = transferencia_finalizada_action.success("Hubo un Problema")

    with allure.step("El cajero de origen realiza un cierre total correctamente"):
        cierre_caja_origen = CierreTotal(caja_origen.balance())
        cierre_caja_action.fast_forward(cajero_origen, caja_origen, cierre_caja_origen)
        caja_origen.agregar_operacion(cierre_caja_origen)
        logout_action.verify_state(cajero_origen).do().success()

    context.page.set_active_driver(driver_destino)
    with allure.step("El cajero de destino realiza un cierre total correctamente"):
        cierre_caja_destino = CierreTotal(caja_destino.balance())
        cierre_caja_action.fast_forward(cajero_destino, caja_destino, cierre_caja_destino)
        logout_action.verify_state(cajero_destino).do().success()


# endregion

# Region transferencia Caja A -> Caja B (Ambas cajas tienen 2 monedas habilitadas pero solo se utiliza 1)
@allure.feature("Caja")
@allure.story("Un cajero genera una extraccion desde su caja a otra")
@allure.title("Un cajero genera una extraccion con menos monedas de las disponibles con destino")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.parametrize('cant_cajas', [2])
@pytest.mark.parametrize('cant_cajeros', [2])
@pytest.mark.parametrize('cant_monedas', [2])
@pytest.mark.parametrize('monto_apertura_destino', [0, 100])
def test_transferencia_caja_caja_una_moneda_de_dos(context, monto_apertura_destino):
    driver_origen = context.driver_manager.main_driver
    caja_origen = context.sucursal.cajas[0]
    cajero_origen = context.cajeros[0]
    apertura_origen = Apertura({m: 1000 for m in caja_origen.monedas_permitidas})

    caja_destino = context.sucursal.cajas[1]
    cajero_destino = context.cajeros[1]
    apertura_destino = Apertura({m: monto_apertura_destino for m in caja_origen.monedas_permitidas})

    monedas = caja_origen.monedas_permitidas.intersection(caja_destino.monedas_permitidas)
    transferencia = Transferencia(caja_origen, caja_destino, {next(iter(monedas)): randint(1, 150)})

    login_action = LoginAction(context)
    logout_action = LogoutAction(context)
    apertura_action = AperturaOperableAction(context)
    cierre_caja_action = CierreTotalCajaAction(context)
    completar_transferencia_action = CompletarTransferenciaAction(context)
    confirmar_transferencia_action = ConfirmarTransferenciaAction(context)
    transferencia_finalizada_action = TransferenciaFinalizadaAction(context)

    with allure.step("El cajero de origen apertura su caja"):
        login_action.verify_state().do(cajero_origen, caja_origen).success("Apertura Caja")
        apertura_action.fast_forward(cajero_origen, caja_origen, apertura_origen, desbloquear=True)
        caja_origen.agregar_operacion(apertura_origen)

    driver_destino = context.driver_manager.new_driver()
    context.page.set_active_driver(driver_destino)
    with allure.step("El cajero de destino apertura su caja"):
        login_action.verify_state().do(cajero_destino, caja_destino).success("Apertura Caja")
        apertura_action.fast_forward(cajero_destino, caja_destino,
                                     apertura_destino, desbloquear=monto_apertura_destino > 0)
        caja_destino.agregar_operacion(apertura_destino)

    context.page.set_active_driver(driver_origen)
    with allure.step(f"El cajero de origen genera un deposito en la caja destino"):
        transferencia.codigo = completar_transferencia_action.fast_forward(cajero_origen, transferencia)
        caja_origen.agregar_operacion(transferencia)

    context.page.set_active_driver(driver_destino)
    with allure.step("El cajero de destino recibe la transferencia y la confirma con montos correctos"):
        transferencia.estado = confirmar_transferencia_action.fast_forward(cajero_destino, transferencia)
        caja_destino.agregar_operacion(transferencia)

    context.page.set_active_driver(driver_origen)
    with allure.step("La transferencia se contabiliza"):
        transferencia_finalizada_action.verify_state(caja_origen).do(transferencia)
        transferencia.estado = transferencia_finalizada_action.success("Contabilizada")

    with allure.step("El cajero de origen realiza un cierre total correctamente"):
        cierre_caja_origen = CierreTotal(caja_origen.balance())
        cierre_caja_action.fast_forward(cajero_origen, caja_origen, cierre_caja_origen)
        caja_origen.agregar_operacion(cierre_caja_origen)
        logout_action.verify_state(cajero_origen).do().success()

    context.page.set_active_driver(driver_destino)
    with allure.step("El cajero de destino realiza un cierre total correctamente"):
        cierre_caja_destino = CierreTotal(caja_destino.balance())
        cierre_caja_action.fast_forward(cajero_destino, caja_destino, cierre_caja_destino)
        logout_action.verify_state(cajero_destino).do().success()
