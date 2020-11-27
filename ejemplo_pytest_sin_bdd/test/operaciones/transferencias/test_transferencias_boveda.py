from random import randint

import allure
import pytest

from src.actions.caja_actions import CierreTotalCajaAction
from src.actions.login_actions import LoginAction
from src.actions.logout_actions import LogoutAction
from src.actions.operable_actions import AperturaOperableAction, CierreOperableAction
from src.actions.transferencias_actions import SeleccionarDestinoTransferenciaAction, CompletarTransferenciaAction, \
    RecibirTransferenciaAction, RecepcionarTransferenciaAction, ConfirmarTransferenciaAction, \
    TransferenciaFinalizadaAction, CancelarTransferenciaAction, ReportarProblemaTranferenciaAction
from src.dominio.operaciones import Apertura, CierreTotal, Transferencia


# region Transferencia Caja -> Boveda
@allure.feature("Boveda General")
@allure.story("Transferencias entre boveda y caja")
@allure.title("Un cajero realiza una transferencia a la boveda general")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.usefixtures("lock_boveda")
@pytest.mark.parametrize('cant_cajas', [1])
@pytest.mark.parametrize('cant_cajeros', [1])
@pytest.mark.parametrize('cant_monedas', [2, 1])
def test_transferencia_caja_boveda(context):
    operador = context.operador_remesas
    boveda = context.boveda
    apertura_boveda = Apertura({m: 1000 for m in context.boveda.monedas_permitidas})

    driver_remesas = context.driver_manager.main_driver
    caja = context.sucursal.cajas[0]
    cajero = context.cajeros[0]
    apertura_caja = Apertura({moneda: 1000 for moneda in caja.monedas_permitidas})
    monedas_extraccion = caja.monedas_permitidas.intersection(context.boveda.monedas)

    transferencia = Transferencia(caja, context.boveda, {moneda: 165 for moneda in monedas_extraccion})

    login_action = LoginAction(context)
    logout_action = LogoutAction(context)
    apertura_action = AperturaOperableAction(context)
    cierre_caja_action = CierreTotalCajaAction(context)
    cierre_boveda_action = CierreOperableAction(context)
    completar_transferencia_action = CompletarTransferenciaAction(context)
    recibir_transferencia_action = RecibirTransferenciaAction(context)
    recepcionar_transferencia_action = RecepcionarTransferenciaAction(context)
    confirmar_transferencia_action = ConfirmarTransferenciaAction(context)
    transferencia_finalizada_action = TransferenciaFinalizadaAction(context)

    with allure.step("El operador de remesas apertura la boveda general"):
        login_action.verify_state().do(operador, boveda).success("Apertura Boveda")
        apertura_action.fast_forward(operador, boveda, apertura_boveda)
        boveda.agregar_operacion(apertura_boveda)

    driver_cajero = context.driver_manager.new_driver()
    context.page.set_active_driver(driver_cajero)
    with allure.step("El cajero apertura su caja"):
        login_action.verify_state().do(cajero, caja).success("Apertura Caja")
        apertura_action.fast_forward(cajero, caja, apertura_caja, desbloquear=True)
        caja.agregar_operacion(apertura_caja)

    with allure.step(f"El cajero genera un deposito en la boveda general"):
        SeleccionarDestinoTransferenciaAction(context).verify_state(caja).do(boveda).success()
        completar_transferencia_action.verify_state(transferencia).do(cajero.password)
        transferencia.codigo = completar_transferencia_action.success()
        caja.agregar_operacion(transferencia)

    context.page.set_active_driver(driver_remesas)
    with allure.step("Boveda general recepciona el deposito y luego confirma con montos correctos"):
        recibir_transferencia_action.verify_state(boveda).do(transferencia).success()
        recepcionar_transferencia_action.verify_state(boveda, transferencia).do()
        transferencia.estado = recepcionar_transferencia_action.success()
        confirmar_transferencia_action.verify_state(boveda, transferencia).do(operador.password)
        transferencia.estado = confirmar_transferencia_action.success()
        context.boveda.agregar_operacion(transferencia)

    context.page.set_active_driver(driver_cajero)
    with allure.step("La transferencia se contabiliza"):
        transferencia_finalizada_action.verify_state(caja).do(transferencia)
        transferencia.estado = transferencia_finalizada_action.success("Contabilizada")

    with allure.step("El cajero realiza un cierre total correctamente"):
        cierre_caja = CierreTotal(caja.balance())
        cierre_caja_action.fast_forward(cajero, caja, cierre_caja)
        caja.agregar_operacion(cierre_caja)
        logout_action.verify_state(cajero).do().success()

    context.page.set_active_driver(driver_remesas)
    with allure.step("El operador de remesas realiza un cierre total correctamente"):
        cierre_boveda = CierreTotal(boveda.balance())
        cierre_boveda_action.fast_forward(operador, boveda, cierre_boveda)
        context.boveda.agregar_operacion(cierre_boveda)
        logout_action.verify_state(operador).do().success()


# endregion

# region Transferencia Boveda -> Caja -> Boveda
@allure.feature("Boveda General")
@allure.story("Transferencias entre boveda y caja")
@allure.title("Un operador de remesas genera una extraccion desde su boveda a una caja")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.usefixtures("lock_boveda")
@pytest.mark.parametrize('cant_cajas', [1])
@pytest.mark.parametrize('cant_cajeros', [1])
@pytest.mark.parametrize('cant_monedas', [2, 1])
def test_transferencia_boveda_caja_boveda(context):
    driver_cajero = context.driver_manager.main_driver
    cajero = context.cajeros[0]
    caja = context.sucursal.cajas[0]
    monto_apertura_caja = 100
    apertura_caja = Apertura({moneda: monto_apertura_caja for moneda in caja.monedas_permitidas})

    operador = context.operador_remesas
    boveda = context.boveda
    monto_apertura_boveda = 1000
    apertura_boveda = Apertura({m: monto_apertura_boveda for m in context.boveda.monedas_permitidas})

    monedas = boveda.monedas_permitidas.intersection(caja.monedas_permitidas)
    transferencia = Transferencia(boveda, caja, {moneda: randint(1, 100) for moneda in monedas})

    login_action = LoginAction(context)
    logout_action = LogoutAction(context)
    apertura_action = AperturaOperableAction(context)
    cierre_caja_action = CierreTotalCajaAction(context)
    cierre_boveda_action = CierreOperableAction(context)
    completar_transferencia_action = CompletarTransferenciaAction(context)
    recepcionar_transferencia_action = RecepcionarTransferenciaAction(context)
    confirmar_transferencia_action = ConfirmarTransferenciaAction(context)
    transferencia_finalizada_action = TransferenciaFinalizadaAction(context)

    with allure.step("El cajero apertura su caja"):
        login_action.verify_state().do(cajero, caja).success("Apertura Caja")
        apertura_action.fast_forward(cajero, caja, apertura_caja, desbloquear=True)
        caja.agregar_operacion(apertura_caja)

    driver_remesas = context.driver_manager.new_driver()
    context.page.set_active_driver(driver_remesas)
    with allure.step("El operador de remesas apertura la boveda general"):
        login_action.verify_state().do(operador, boveda).success("Apertura Boveda")
        apertura_action.fast_forward(operador, boveda, apertura_boveda)
        boveda.agregar_operacion(apertura_boveda)

    with allure.step("El operador de remesas genera una transferencia de salida hacia caja destino"):
        SeleccionarDestinoTransferenciaAction(context).verify_state(boveda).do(caja).success()
        completar_transferencia_action.verify_state(transferencia).do(operador.password)
        transferencia.codigo = completar_transferencia_action.success()
        boveda.agregar_operacion(transferencia)

    context.page.set_active_driver(driver_cajero)
    with allure.step("El cajero de destino recibe la transferencia y confirma con montos correctos"):
        transferencia.estado = confirmar_transferencia_action.fast_forward(cajero, transferencia)
        caja.agregar_operacion(transferencia)

    context.page.set_active_driver(driver_remesas)
    with allure.step("la transferencia se contabiliza y ya no se muestra"):
        transferencia_finalizada_action.verify_state(boveda).do(transferencia)
        transferencia.estado = transferencia_finalizada_action.success("Contabilizada")

    context.page.set_active_driver(driver_cajero)
    transferencia2 = Transferencia(caja, boveda, {moneda: monto + monto_apertura_caja
                                                  for moneda, monto in transferencia.montos.items()})
    with allure.step("El cajero de destino genera una nueva transferencia hacia la boveda general"):
        transferencia2.codigo = completar_transferencia_action.fast_forward(cajero, transferencia2)
        caja.agregar_operacion(transferencia2)

    context.page.set_active_driver(driver_remesas)
    with allure.step("Boveda general recepciona el deposito y luego lo confirma con montos correctos"):
        transferencia2.estado = recepcionar_transferencia_action.fast_forward(operador, transferencia2)
        confirmar_transferencia_action.fast_forward(operador, transferencia2)

    context.page.set_active_driver(driver_cajero)
    with allure.step("la transferencia se contabiliza y ya no se muestra"):
        transferencia_finalizada_action.verify_state(caja).do(transferencia2)
        transferencia2.estado = transferencia_finalizada_action.fast_forward(transferencia2)
        boveda.agregar_operacion(transferencia2)

    with allure.step("El cajero realiza un cierre total"):
        cierre_caja = CierreTotal(caja.balance())
        cierre_caja_action.fast_forward(cajero, caja, cierre_caja)
        caja.agregar_operacion(cierre_caja)
        logout_action.verify_state(cajero).do().success()

    context.page.set_active_driver(driver_remesas)
    with allure.step("El operador de remesas realiza un cierre total correctamente"):
        cierre_boveda = CierreTotal(boveda.balance())
        cierre_boveda_action.fast_forward(operador, boveda, cierre_boveda)
        context.boveda.agregar_operacion(cierre_boveda)
        logout_action.verify_state(operador).do().success()


# endregion

# region Cerrar boveda con depositos pendientes de confirmacion

@allure.feature("Boveda General")
@allure.story("Transferencias entre boveda y caja")
@allure.title("La boveda puede cerrar con depositos pendiente de confirmacion")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.usefixtures("lock_boveda")
@pytest.mark.parametrize('cant_cajas', [1])
@pytest.mark.parametrize('cant_cajeros', [1])
@pytest.mark.parametrize('cant_monedas', [2, 1])
def test_cierre_boveda_con_depositos_pendiente_confirmacion(context):
    driver_cajero = context.driver_manager.main_driver
    caja = context.sucursal.cajas[0]
    monto_apretura_caja = 1000
    apertura_caja = Apertura({m: monto_apretura_caja for m in caja.monedas_permitidas})
    cajero = context.cajeros[0]

    apertura_boveda = 1000
    apertura_boveda = Apertura({m: apertura_boveda for m in context.boveda.monedas_permitidas})
    boveda = context.boveda
    operador = context.operador_remesas

    monedas = caja.monedas_permitidas.intersection(context.boveda.monedas)
    transferencia = Transferencia(caja, context.boveda, {moneda: randint(1, 100) for moneda in monedas})

    login_action = LoginAction(context)
    logout_action = LogoutAction(context)
    apertura_action = AperturaOperableAction(context)
    cierre_caja_action = CierreTotalCajaAction(context)
    cierre_boveda_action = CierreOperableAction(context)
    completar_transferencia_action = CompletarTransferenciaAction(context)
    recibir_transferencia_action = RecibirTransferenciaAction(context)
    recepcionar_transferencia_action = RecepcionarTransferenciaAction(context)

    with allure.step("El cajero apertura su caja"):
        login_action.verify_state().do(cajero, caja).success("Apertura Caja")
        apertura_action.fast_forward(cajero, caja, apertura_caja, desbloquear=True)
        caja.agregar_operacion(apertura_caja)

    driver_remesas = context.driver_manager.new_driver()
    context.page.set_active_driver(driver_remesas)
    with allure.step("El operador de remesas apertura la boveda general"):
        login_action.verify_state().do(operador, boveda).success("Apertura Boveda")
        apertura_action.fast_forward(operador, boveda, apertura_boveda)
        boveda.agregar_operacion(apertura_boveda)

    context.page.set_active_driver(driver_cajero)
    with allure.step(f"El cajero genera un deposito en la boveda general"):
        transferencia.codigo = completar_transferencia_action.fast_forward(cajero, transferencia)
        caja.agregar_operacion(transferencia)

    context.page.set_active_driver(driver_remesas)
    with allure.step("Boveda general recepciona el deposito"):
        transferencia.estado = recepcionar_transferencia_action.fast_forward(operador, transferencia)

    with allure.step("El operador de remesas realiza un cierre total correctamente"):
        cierre_boveda = CierreTotal(boveda.balance())
        cierre_boveda_action.fast_forward(operador, boveda, cierre_boveda)
        context.boveda.agregar_operacion(cierre_boveda)
        logout_action.verify_state(operador).do().success()

    context.page.set_active_driver(driver_cajero)
    with allure.step("El cajero realiza un cierre total correctamente"):
        cierre_caja = CierreTotal(caja.balance())
        cierre_caja_action.fast_forward(cajero, caja, cierre_caja)
        caja.agregar_operacion(cierre_caja)
        logout_action.verify_state(cajero).do().success()


# endregion

# region Cerrar boveda con depositos pendientes de recepcion

@allure.feature("Boveda General")
@allure.story("Transferencias entre boveda y caja")
@allure.title("La boveda no puede cerrar con depositos pendiente de recepcion")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.usefixtures("lock_boveda")
@pytest.mark.parametrize('cant_cajas', [1])
@pytest.mark.parametrize('cant_cajeros', [1])
@pytest.mark.parametrize('cant_monedas', [2, 1])
def test_cierre_boveda_con_depositos_pendiente_recepcion(context):
    driver_cajero = context.driver_manager.main_driver
    caja = context.sucursal.cajas[0]
    monto_apertura_caja = 1000
    apertura_caja = Apertura({m: monto_apertura_caja for m in caja.monedas_permitidas})

    cajero = context.cajeros[0]

    boveda = context.boveda
    operador = context.operador_remesas
    monto_apertura_boveda = 1000
    apertura_boveda = Apertura({m: monto_apertura_boveda for m in boveda.monedas_permitidas})

    monedas = caja.monedas_permitidas.intersection(context.boveda.monedas)
    transferencia = Transferencia(caja, context.boveda, {moneda: randint(1, 100) for moneda in monedas})

    login_action = LoginAction(context)
    logout_action = LogoutAction(context)
    apertura_action = AperturaOperableAction(context)
    cierre_caja_action = CierreTotalCajaAction(context)
    cierre_boveda_action = CierreOperableAction(context)
    completar_transferencia_action = CompletarTransferenciaAction(context)
    recibir_transferencia_action = RecibirTransferenciaAction(context)
    recepcionar_transferencia_action = RecepcionarTransferenciaAction(context)

    with allure.step("El cajero apertura su caja"):
        login_action.verify_state().do(cajero, caja).success("Apertura Caja")
        apertura_action.fast_forward(cajero, caja, apertura_caja, desbloquear=True)
        caja.agregar_operacion(apertura_caja)

    driver_remesas = context.driver_manager.new_driver()
    context.page.set_active_driver(driver_remesas)
    with allure.step("El operador de remesas apertura la boveda general"):
        login_action.verify_state().do(operador, boveda).success("Apertura Boveda")
        apertura_action.fast_forward(operador, boveda, apertura_boveda)
        boveda.agregar_operacion(apertura_boveda)

    context.page.set_active_driver(driver_cajero)
    with allure.step(f"El cajero genera un deposito en la boveda general"):
        transferencia.codigo = completar_transferencia_action.fast_forward(cajero, transferencia)
        caja.agregar_operacion(transferencia)

    context.page.set_active_driver(driver_remesas)
    with allure.step("Boveda general recibe la transferencia pero no la recepciona"):
        recibir_transferencia_action.verify_state(boveda).do(transferencia).success()

    with allure.step("El operador de remesas realiza un cierre total"):
        cierre_boveda = CierreTotal(boveda.balance())
        cierre_boveda_action.verify_state(boveda, cierre_boveda).do(operador.password, should_redirect=False)

    with allure.step("Pero no puede porque tiene operaciones pendientes"):
        cierre_boveda_action.failure("Operaciones Pendientes")

    # recepciono la operacion y cierro la boveda para que no quede bloqueada la boveda en los siguientes tests
    recibir_transferencia_action.verify_state(boveda).do(transferencia)
    recepcionar_transferencia_action.fast_forward(operador, transferencia)
    cierre_boveda = CierreTotal(boveda.balance())
    cierre_boveda_action.fast_forward(operador, boveda, cierre_boveda)
    logout_action.verify_state(operador).do().success()

    context.page.set_active_driver(driver_cajero)
    with allure.step("El cajero realiza un cierre total correctamente"):
        cierre_caja = CierreTotal(caja.balance())
        cierre_caja_action.fast_forward(cajero, caja, cierre_caja)
        caja.agregar_operacion(cierre_caja)
        logout_action.verify_state(cajero).do().success()


# endregion

# region Boveda cancela extraccion pendiente de recepcion
@allure.feature("Boveda General")
@allure.story("Transferencias entre boveda y caja")
@allure.title("La boveda puede cancelar extracciones pendientes de recepcion")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.usefixtures("lock_boveda")
@pytest.mark.parametrize('cant_cajas', [1])
@pytest.mark.parametrize('cant_cajeros', [1])
@pytest.mark.parametrize('cant_monedas', [2, 1])
def test_cancelar_transferencia_boveda_caja_pendiente_recepcion(context):
    driver_caja = context.driver_manager.main_driver
    cajero = context.cajeros[0]
    caja = context.sucursal.cajas[0]
    monto_apertura_caja = 100
    apertura_caja = Apertura({moneda: monto_apertura_caja for moneda in caja.monedas_permitidas})

    operador = context.operador_remesas
    boveda = context.boveda
    monto_apertura_boveda = 1000
    apertura_boveda = Apertura({moneda: monto_apertura_boveda for moneda in boveda.monedas_permitidas})

    monedas = boveda.monedas_permitidas.intersection(caja.monedas_permitidas)
    transferencia = Transferencia(boveda, caja, {moneda: randint(1, 100) for moneda in monedas})

    login_action = LoginAction(context)
    logout_action = LogoutAction(context)
    apertura_action = AperturaOperableAction(context)
    cierre_caja_action = CierreTotalCajaAction(context)
    cierre_boveda_action = CierreOperableAction(context)
    completar_transferencia_action = CompletarTransferenciaAction(context)
    recibir_transferencia_action = RecibirTransferenciaAction(context)
    cancelar_transferencia_action = CancelarTransferenciaAction(context)
    confirmar_transferencia_action = ConfirmarTransferenciaAction(context)
    transferencia_finalizada_action = TransferenciaFinalizadaAction(context)

    with allure.step("El cajero de destino apertura su caja"):
        login_action.verify_state().do(cajero, caja).success("Apertura Caja")
        apertura_action.fast_forward(cajero, caja, apertura_caja, desbloquear=True)
        caja.agregar_operacion(apertura_caja)

    driver_operador = context.driver_manager.new_driver()
    context.page.set_active_driver(driver_operador)
    with allure.step("El operador de remesas apertura la boveda general"):
        login_action.verify_state().do(operador, boveda).success("Apertura Boveda")
        apertura_action.fast_forward(operador, boveda, apertura_boveda)
        boveda.agregar_operacion(apertura_boveda)

    with allure.step("El operador de remesas genera una transferencia de salida hacia caja destino"):
        transferencia.codigo = completar_transferencia_action.fast_forward(operador, transferencia)
        boveda.agregar_operacion(transferencia)

    context.page.set_active_driver(driver_caja)
    with allure.step("La transferencia se muestra en los depositos pendientes del cajero"):
        recibir_transferencia_action.verify_state(caja).do(transferencia).success()

    context.page.set_active_driver(driver_operador)
    with allure.step("El operador cancela la transferencia"):
        cancelar_transferencia_action.verify_state(boveda, transferencia).do(operador.password).success()

    context.page.set_active_driver(driver_caja)
    with allure.step("El cajero no podra realizar ninguna accion con el deposito"):
        recibir_transferencia_action.success()
        confirmar_transferencia_action.verify_state(caja, transferencia).do(cajero.password).failure()

    with allure.step("y cuando refresque la pantalla ya no vera el deposito"):
        transferencia_finalizada_action.verify_state(caja).do(transferencia)
        transferencia.estado = transferencia_finalizada_action.success("Cancelada")

    with allure.step("El cajero de destino realiza un cierre total correctamente"):
        cierre_caja = CierreTotal(caja.balance())
        cierre_caja_action.fast_forward(cajero, caja, cierre_caja)
        caja.agregar_operacion(cierre_caja)
        logout_action.verify_state(cajero).do().success()

    context.page.set_active_driver(driver_operador)
    with allure.step("El operador de remesas realiza un cierre total correctamente"):
        cierre_boveda = CierreTotal(boveda.balance())
        cierre_boveda_action.fast_forward(operador, boveda, cierre_boveda)
        boveda.agregar_operacion(cierre_boveda)
        logout_action.verify_state(operador).do().success()


# endregion

# region Transferencia Caja -> Boveda (Boveda reporta un error)

@allure.feature("Boveda General")
@allure.story("Transferencias entre boveda y caja")
@allure.title("Un cajero realiza una transferencia a la boveda general y esta reporta un problema")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.usefixtures("lock_boveda")
@pytest.mark.parametrize('cant_cajas', [1])
@pytest.mark.parametrize('cant_cajeros', [1])
@pytest.mark.parametrize('cant_monedas', [2, 1])
def test_transferencia_caja_boveda_con_error(context):
    operador = context.operador_remesas
    boveda = context.boveda
    apertura_boveda = Apertura({m: 1000 for m in context.boveda.monedas_permitidas})

    driver_remesas = context.driver_manager.main_driver
    caja = context.sucursal.cajas[0]
    cajero = context.cajeros[0]
    apertura_caja = Apertura({moneda: 1000 for moneda in caja.monedas_permitidas})
    monedas_extraccion = caja.monedas_permitidas.intersection(context.boveda.monedas)

    transferencia = Transferencia(caja, context.boveda, {moneda: 165 for moneda in monedas_extraccion})

    login_action = LoginAction(context)
    logout_action = LogoutAction(context)
    apertura_action = AperturaOperableAction(context)
    cierre_caja_action = CierreTotalCajaAction(context)
    cierre_boveda_action = CierreOperableAction(context)
    completar_transferencia_action = CompletarTransferenciaAction(context)
    recibir_transferencia_action = RecibirTransferenciaAction(context)
    problema_transferencia_action = ReportarProblemaTranferenciaAction(context)
    transferencia_finalizada_action = TransferenciaFinalizadaAction(context)

    with allure.step("El operador de remesas apertura la boveda general"):
        login_action.verify_state().do(operador, boveda).success("Apertura Boveda")
        apertura_action.fast_forward(operador, boveda, apertura_boveda)
        boveda.agregar_operacion(apertura_boveda)

    driver_cajero = context.driver_manager.new_driver()
    context.page.set_active_driver(driver_cajero)
    with allure.step("El cajero apertura su caja"):
        login_action.verify_state().do(cajero, caja).success("Apertura Caja")
        apertura_action.fast_forward(cajero, caja, apertura_caja, desbloquear=True)
        caja.agregar_operacion(apertura_caja)

    with allure.step(f"El cajero genera un deposito en la boveda general"):
        transferencia.codigo = completar_transferencia_action.fast_forward(cajero, transferencia)
        caja.agregar_operacion(transferencia)

    context.page.set_active_driver(driver_remesas)
    with allure.step("Boveda general reporta un error en la transferencia"):
        recibir_transferencia_action.verify_state(boveda).do(transferencia).success()
        problema_transferencia_action.verify_state(boveda, transferencia).do("Reporte de Prueba", operador.password)
        problema_transferencia_action.success()
        boveda.agregar_operacion(transferencia)

    context.page.set_active_driver(driver_cajero)
    with allure.step("La transferencia se reporta con problemas"):
        transferencia_finalizada_action.verify_state(caja).do(transferencia)
        transferencia.estado = transferencia_finalizada_action.success("Hubo un Problema")

    with allure.step("El cajero realiza un cierre total correctamente"):
        cierre_caja = CierreTotal(caja.balance())
        cierre_caja_action.fast_forward(cajero, caja, cierre_caja)
        caja.agregar_operacion(cierre_caja)
        logout_action.verify_state(cajero).do().success()

    context.page.set_active_driver(driver_remesas)
    with allure.step("El operador de remesas realiza un cierre total correctamente"):
        cierre_boveda = CierreTotal(boveda.balance())
        cierre_boveda_action.fast_forward(operador, boveda, cierre_boveda)
        context.boveda.agregar_operacion(cierre_boveda)
        logout_action.verify_state(operador).do().success()

# endregion
