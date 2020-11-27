from random import choice

import allure
import pytest

from src.actions.caja_actions import CierreTotalCajaAction
from src.actions.login_actions import LoginAction
from src.actions.logout_actions import LogoutAction
from src.actions.operable_actions import AperturaOperableAction, CierreOperableAction
from src.actions.solicitud_fondo_actions import CompletarSolicitudFondosAction, RecibirSolicitudFondosAction, \
    AceptarSolicitudFondosAction, SolicitudFinalizadaAction, RechazarSolicitudFondosAction, \
    CancelarSolicitudFondosAction
from src.actions.transferencias_actions import RecibirTransferenciaAction, \
    ConfirmarTransferenciaAction, TransferenciaFinalizadaAction
from src.dominio.operaciones import Apertura, CierreTotal, SolicitudFondo, Transferencia


# region Solicitud fondos Caja -> Boveda general (Caja sugiere montos y boveda transfiere lo solicitado)
@allure.feature("Caja")
@allure.story("Solicitar fondos")
@allure.title("Un cajero solicita fondos y la boveda envia los montos solicitados")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.usefixtures("lock_boveda")
@pytest.mark.parametrize('cant_cajas', [2])
@pytest.mark.parametrize('cant_cajeros', [1])
@pytest.mark.parametrize('cant_monedas', [2, 1])
def test_solicitar_fondos_montos_solicitados(context):
    cajero = context.cajeros[0]
    caja = context.sucursal.cajas[0]
    monto_apertura_caja = 0
    apertura_caja = Apertura({m: monto_apertura_caja for m in caja.monedas_permitidas})

    driver_operador = context.driver_manager.main_driver
    operador = context.operador_remesas
    boveda = context.boveda
    monto_apertura_boveda = 1000
    apertura_boveda = Apertura({m: monto_apertura_boveda for m in boveda.monedas_permitidas})

    monedas = caja.monedas_permitidas.intersection(context.boveda.monedas)
    solicitud = SolicitudFondo(caja, boveda, {m: choice([20, 50]) for m in monedas})
    transferencia = Transferencia(boveda, caja, solicitud.montos, solicitud.observaciones)

    login_action = LoginAction(context)
    logout_action = LogoutAction(context)
    apertura_action = AperturaOperableAction(context)
    cierre_caja_action = CierreTotalCajaAction(context)
    cierre_boveda_action = CierreOperableAction(context)
    completar_solicitud_action = CompletarSolicitudFondosAction(context)
    recibir_solicitud_action = RecibirSolicitudFondosAction(context)
    aceptar_solicitud_action = AceptarSolicitudFondosAction(context)
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
        apertura_action.fast_forward(cajero, caja, apertura_caja)
        caja.agregar_operacion(apertura_caja)

    with allure.step("El cajero genera una solicitud de fondos con montos sugeridos"):
        completar_solicitud_action.verify_state(caja).do(solicitud, cajero.password)

    with allure.step("La solicitud se genera correctamnete"):
        solicitud.codigo = completar_solicitud_action.success()

    context.page.set_active_driver(driver_operador)
    with allure.step("Boveda recibe la solicitud y la acepta con los montos sugeridos"):
        recibir_solicitud_action.verify_state(boveda).do(solicitud).success()
        aceptar_solicitud_action.verify_state(boveda, solicitud).do(operador.password)

    with allure.step("La solicitud se confirma y se genera la transferencia"):
        transferencia.codigo = solicitud.codigo
        aceptar_solicitud_action.success(transferencia)
        boveda.agregar_operacion(transferencia)

    context.page.set_active_driver(driver_cajero)
    with allure.step("El cajero recibe la transferencia y confirma con montos correctos"):
        SolicitudFinalizadaAction(context).verify_state(caja).do(solicitud).success("Aceptada")
        transferencia.estado = confirmar_transferencia_action.fast_forward(cajero, transferencia)

    context.page.set_active_driver(driver_operador)
    with allure.step("la transferencia se contabiliza y ya no se muestra"):
        transferencia.estado = transferencia_finalizada_action.fast_forward(transferencia)
        caja.agregar_operacion(transferencia)

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

# region Solicitud fondos Caja -> Boveda Central (Caja sugiere montos y boveda transfiere +- de lo solicitado)
@allure.feature("Caja")
@allure.story("Solicitar fondos")
@allure.title("Un cajero solicita fondos y la boveda envia una cantidad distinta de la solicitada")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.usefixtures("lock_boveda")
@pytest.mark.parametrize('cant_cajas', [2])
@pytest.mark.parametrize('cant_cajeros', [1])
@pytest.mark.parametrize('cant_monedas', [2, 1])
@pytest.mark.parametrize('diferencia', [10, -10])
def test_solicitar_fondos_montos_distintos(context, diferencia):
    cajero = context.cajeros[0]
    caja = context.sucursal.cajas[0]
    monto_apertura_caja = 0
    apertura_caja = Apertura({m: monto_apertura_caja for m in caja.monedas_permitidas})

    driver_operador = context.driver_manager.main_driver
    operador = context.operador_remesas
    boveda = context.boveda
    monto_apertura_boveda = 1000
    apertura_boveda = Apertura({m: monto_apertura_boveda for m in boveda.monedas_permitidas})

    monedas = caja.monedas_permitidas.intersection(context.boveda.monedas)
    solicitud = SolicitudFondo(caja, boveda, {m: choice([20, 50]) for m in monedas})
    transferencia = Transferencia(boveda, caja,
                                  {moneda: monto + diferencia for moneda, monto in solicitud.montos.items()},
                                  solicitud.observaciones)

    login_action = LoginAction(context)
    logout_action = LogoutAction(context)
    apertura_action = AperturaOperableAction(context)
    cierre_caja_action = CierreTotalCajaAction(context)
    cierre_boveda_action = CierreOperableAction(context)
    completar_solicitud_action = CompletarSolicitudFondosAction(context)
    recibir_solicitud_action = RecibirSolicitudFondosAction(context)
    aceptar_solicitud_action = AceptarSolicitudFondosAction(context)
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
        apertura_action.fast_forward(cajero, caja, apertura_caja)
        caja.agregar_operacion(apertura_caja)

    with allure.step("El cajero genera una solicitud de fondos con montos sugeridos"):
        completar_solicitud_action.verify_state(caja).do(solicitud, cajero.password)

    with allure.step("La solicitud se genera correctamnete"):
        solicitud.codigo = completar_solicitud_action.success()

    context.page.set_active_driver(driver_operador)
    with allure.step("Boveda recibe la solicitud y la acepta con menos dinero del sugerido"):
        recibir_solicitud_action.verify_state(boveda).do(solicitud).success()
        aceptar_solicitud_action.verify_state(boveda, solicitud).do(operador.password, transferencia.montos)

    with allure.step("La solicitud se confirma y se genera la transferencia"):
        transferencia.codigo = solicitud.codigo
        aceptar_solicitud_action.success(transferencia)
        boveda.agregar_operacion(transferencia)

    context.page.set_active_driver(driver_cajero)
    with allure.step("El cajero recibe la transferencia y confirma con montos correctos"):
        SolicitudFinalizadaAction(context).verify_state(caja).do(solicitud).success("Aceptada")
        transferencia.estado = confirmar_transferencia_action.fast_forward(cajero, transferencia)

    context.page.set_active_driver(driver_operador)
    with allure.step("la transferencia se contabiliza y ya no se muestra"):
        transferencia.estado = transferencia_finalizada_action.fast_forward(transferencia)
        caja.agregar_operacion(transferencia)

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


# region Solicitud fondos Caja -> Boveda Central (Boveda rechaza la solicitud)
@allure.feature("Caja")
@allure.story("Solicitar fondos")
@allure.title("Un cajero solicita fondos y la boveda rechaza")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.usefixtures("lock_boveda")
@pytest.mark.parametrize('cant_cajas', [2])
@pytest.mark.parametrize('cant_cajeros', [1])
@pytest.mark.parametrize('cant_monedas', [2, 1])
@pytest.mark.parametrize('monto_apertura_caja', [0, 150])
def test_solicitud_fondos_rechazada(context, monto_apertura_caja):
    cajero = context.cajeros[0]
    caja = context.sucursal.cajas[0]
    apertura_caja = Apertura({m: monto_apertura_caja for m in caja.monedas_permitidas})

    driver_operador = context.driver_manager.main_driver
    operador = context.operador_remesas
    boveda = context.boveda
    monto_apertura_boveda = 1000
    apertura_boveda = Apertura({m: monto_apertura_boveda for m in boveda.monedas_permitidas})

    monedas = caja.monedas_permitidas.intersection(context.boveda.monedas)
    solicitud = SolicitudFondo(caja, boveda, {m: choice([20, 50]) for m in monedas})

    login_action = LoginAction(context)
    logout_action = LogoutAction(context)
    apertura_action = AperturaOperableAction(context)
    cierre_caja_action = CierreTotalCajaAction(context)
    cierre_boveda_action = CierreOperableAction(context)
    completar_solicitud_action = CompletarSolicitudFondosAction(context)
    recibir_solicitud_action = RecibirSolicitudFondosAction(context)
    rechazar_solicitud_action = RechazarSolicitudFondosAction(context)

    with allure.step("El operador de remesas apertura la boveda general"):
        login_action.verify_state().do(operador, boveda).success("Apertura Boveda")
        apertura_action.fast_forward(operador, boveda, apertura_boveda)
        boveda.agregar_operacion(apertura_boveda)

    driver_cajero = context.driver_manager.new_driver()
    context.page.set_active_driver(driver_cajero)
    with allure.step("El cajero apertura su caja"):
        login_action.verify_state().do(cajero, caja).success("Apertura Caja")
        apertura_action.fast_forward(cajero, caja, apertura_caja, desbloquear=monto_apertura_caja > 0)
        caja.agregar_operacion(apertura_caja)

    with allure.step("El cajero genera una solicitud de fondos con montos sugeridos"):
        completar_solicitud_action.verify_state(caja).do(solicitud, cajero.password)

    with allure.step("La solicitud se genera correctamnete"):
        solicitud.codigo = completar_solicitud_action.success()

    context.page.set_active_driver(driver_operador)
    with allure.step("Boveda recibe la solicitud y la rechaza"):
        recibir_solicitud_action.verify_state(boveda).do(solicitud).success()
        rechazar_solicitud_action.verify_state(boveda, solicitud).do(operador.password)

    context.page.set_active_driver(driver_cajero)
    with allure.step("La solicitud se rechaza"):
        SolicitudFinalizadaAction(context).verify_state(caja).do(solicitud).success("Rechazada")

    context.page.set_active_driver(driver_operador)
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

# region region Solicitud fondos Caja -> Boveda Central (Boveda no cuenta con fondos para aceptar)

@allure.feature("Caja")
@allure.story("Solicitar fondos")
@allure.title("Un cajero solicita fondos y la boveda no cuenta con fondos para aceptar")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.usefixtures("lock_boveda")
@pytest.mark.parametrize('cant_cajas', [2])
@pytest.mark.parametrize('cant_cajeros', [1])
@pytest.mark.parametrize('cant_monedas', [2, 1])
@pytest.mark.parametrize('monto_apertura_caja', [0, 150])
def test_solicitud_fondos_boveda_sin_fondos(context, monto_apertura_caja):
    cajero = context.cajeros[0]
    caja = context.sucursal.cajas[0]
    apertura_caja = Apertura({m: monto_apertura_caja for m in caja.monedas_permitidas})

    driver_operador = context.driver_manager.main_driver
    operador = context.operador_remesas
    boveda = context.boveda
    monto_apertura_boveda = 0
    apertura_boveda = Apertura({m: monto_apertura_boveda for m in boveda.monedas_permitidas})

    monedas = caja.monedas_permitidas.intersection(context.boveda.monedas)
    solicitud = SolicitudFondo(caja, boveda, {m: choice([20, 50]) for m in monedas})

    login_action = LoginAction(context)
    logout_action = LogoutAction(context)
    apertura_action = AperturaOperableAction(context)
    cierre_caja_action = CierreTotalCajaAction(context)
    cierre_boveda_action = CierreOperableAction(context)
    completar_solicitud_action = CompletarSolicitudFondosAction(context)
    recibir_solicitud_action = RecibirSolicitudFondosAction(context)
    aceptar_solicitud_action = AceptarSolicitudFondosAction(context)

    with allure.step("El operador de remesas apertura la boveda general"):
        login_action.verify_state().do(operador, boveda).success("Apertura Boveda")
        apertura_action.fast_forward(operador, boveda, apertura_boveda)
        boveda.agregar_operacion(apertura_boveda)

    driver_cajero = context.driver_manager.new_driver()
    context.page.set_active_driver(driver_cajero)
    with allure.step("El cajero apertura su caja"):
        login_action.verify_state().do(cajero, caja).success("Apertura Caja")
        apertura_action.fast_forward(cajero, caja, apertura_caja, desbloquear=monto_apertura_caja > 0)
        caja.agregar_operacion(apertura_caja)

    with allure.step("El cajero genera una solicitud de fondos con montos sugeridos"):
        completar_solicitud_action.verify_state(caja).do(solicitud, cajero.password)

    with allure.step("La solicitud se genera correctamnete"):
        solicitud.codigo = completar_solicitud_action.success()

    context.page.set_active_driver(driver_operador)
    with allure.step("Boveda recibe la solicitud y la intenta aceptar pero no cuenta con fondos"):
        recibir_solicitud_action.verify_state(boveda).do(solicitud).success()
        aceptar_solicitud_action.verify_state(boveda, solicitud).do(operador.password).failure()
        recibir_solicitud_action.success()

    context.page.set_active_driver(driver_cajero)
    with allure.step("La solicitud permanece pendiente"):
        CancelarSolicitudFondosAction(context).verify_state(caja, solicitud)

    context.page.set_active_driver(driver_operador)
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

# region Caja solicita fondos pero la boveda esta cerrada
@allure.feature("Caja")
@allure.story("Solicitar fondos")
@allure.title("Solo se pueden solicitar fondos si la boveda esta abierta")
@pytest.mark.usefixtures("generar_sucursal")
@pytest.mark.usefixtures("lock_boveda")
@pytest.mark.parametrize('cant_cajas', [2])
@pytest.mark.parametrize('cant_cajeros', [1])
@pytest.mark.parametrize('cant_monedas', [2, 1])
def test_solicitar_fondos_boveda_cerrada(context):
    cajero = context.cajeros[0]
    caja = context.sucursal.cajas[0]
    monto_apertura_caja = 0
    apertura_caja = Apertura({m: monto_apertura_caja for m in caja.monedas_permitidas})

    monedas = caja.monedas_permitidas.intersection(context.boveda.monedas)
    solicitud = SolicitudFondo(caja, context.boveda, {m: choice([20, 50]) for m in monedas})

    login_action = LoginAction(context)
    logout_action = LogoutAction(context)
    apertura_action = AperturaOperableAction(context)
    completar_solicitud_action = CompletarSolicitudFondosAction(context)

    with allure.step("El cajero apertura su caja"):
        login_action.verify_state().do(cajero, caja).success("Apertura Caja")
        apertura_action.fast_forward(cajero, caja, apertura_caja)
        caja.agregar_operacion(apertura_caja)

    with allure.step("El cajero genera una solicitud de fondos con montos sugeridos"):
        completar_solicitud_action.verify_state(caja).do(solicitud, cajero.password)

    with allure.step("El sistema le indica que la boveda se encuentra cerrada"):
        completar_solicitud_action.failure(caja)
        logout_action.verify_state(cajero).do().success()
# endregion
