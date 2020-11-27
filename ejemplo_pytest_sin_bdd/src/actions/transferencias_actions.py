from datetime import datetime

from src.actions.base.base_action import BaseAction
from src.dominio.operable import TiposOperable
from src.dominio.operaciones import EstadosTransferencia
from src.utils.others import today, seconds_before_now


# region Salientes
class SeleccionarDestinoTransferenciaAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)
        self._origen = None
        self._destino = None

    def verify_state(self, origen):
        _validar_operable_activo(self, origen)
        self._origen = origen
        return self

    def do(self, destino):
        self.page.ir_a_transf_salientes()
        self.page.nueva_extraccion()
        self.page.seleccionar_destinatario(destino.codigo)
        self._destino = destino
        return self

    def success(self):
        monedas_esperadas = [moneda.codigo for moneda in self._origen.monedas_permitidas
                             if moneda in self._destino.monedas_permitidas]
        monedas_obtenidas = self.page.monedas_disponibles_deposito()
        self._assert.that(len(monedas_esperadas)).equals(len(monedas_obtenidas))
        self._assert.that(set(monedas_esperadas)).equals(set(monedas_obtenidas))

    def failure(self, *args):
        self.page.mensaje_extraccion_sin_monedas()
        self.page.cerrar_modal()


class CompletarTransferenciaAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)
        self._transferencia = None
        self._time = None

    def verify_state(self, transferencia):
        self._assert.that(transferencia.destino.codigo).equals(self.page.destino_seleccionado())
        self._transferencia = transferencia
        return self

    def do(self, password):
        self._time = datetime.utcnow()
        self.page.generar_extraccion(self._transferencia.montos, str(self._transferencia.observaciones), password)
        return self

    def success(self):
        self._assert.that("Extracción creada con éxito.").equals(self.page.get_toast())
        self.page.dismiss_toast()
        self._get_codigo(self._transferencia, self._time)
        transf = self.db.get_transferencia(self._transferencia)
        self._assert.that(transf["fecha"]).greater_than(self._time)
        codigo = f"{transf['tipo_de_transaccion_id']}-{transf['numero_transaccion']}"

        self._assert.that(_tabla_saliente(self._transferencia)) \
            .equals(self.page.tabla_transferencia_saliente(codigo))
        self._assert.that(_detalle_saliente(self._transferencia, codigo=codigo)) \
            .equals(self.page.detalle_transferencia_saliente(codigo))
        return codigo

    def _get_codigo(self, transferencia, tiempo):
        transf = self.db.get_transferencia(transferencia)
        self._assert.that(transf["fecha"]).greater_than(tiempo)
        return f"{transf['tipo_de_transaccion_id']}-{transf['numero_transaccion']}"

    def failure(self, failure_type):
        mensajes = {
            "Sin Saldo": "No cuenta con fondos suficientes para realizar la operación"
        }
        self._assert.that(mensajes[failure_type]).equals(self.page.get_toast())
        self.page.dismiss_toast()
        self.page.cerrar_modal()

    def fast_forward(self, cajero, transferencia):
        self.api.login(cajero)
        tiempo = datetime.utcnow()
        response = self.api.generar_transferencia(transferencia, cajero)
        assert response.ok
        self.page.ir_a_transf_salientes()
        return self._get_codigo(transferencia, tiempo)



class CancelarTransferenciaAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)
        self._transferencia = None

    def verify_state(self, operable, transferencia):
        _validar_operable_activo(self, operable)
        self._assert.that(_tabla_saliente(transferencia)).equals(
            self.page.tabla_transferencia_saliente(transferencia.codigo))
        self._assert.that(transferencia.estado).equals(EstadosTransferencia.PENDIENTE_RECEPCION)

        self.page.nueva_cancelacion_transferencia(transferencia.codigo)
        esperado = {
            "Titulo": f"Cancelar extracción\n{transferencia.codigo} - {today()}",
            "Info Text": "¿Está seguro que desea cancelar esta extracción?",
            "Destino": transferencia.destino.codigo,
            "Montos": {moneda.codigo: str(monto) for moneda, monto in transferencia.montos.items()},
            "Observacion": transferencia.observaciones.get_label_text(),
            "Medio": transferencia.medio
        }
        obtenido = self.page.detalle_cancelacion_transferencia()
        self._assert.that(esperado).equals(obtenido)

        self._transferencia = transferencia
        return self

    def do(self, password):
        self.page.cancelar_transferencia(password)
        return self

    def success(self):
        self._assert.that("Se ha cancelado la extracción correctamente").equals(self.page.get_toast())
        self.page.dismiss_toast()
        self.page.transferencia_stale(self._transferencia.codigo, False)
        return EstadosTransferencia.CANCELADA

    def failure(self, *args):
        pass


# endregion

# region Entrantes

class RecibirTransferenciaAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)
        self._transferencia = None
        self._operable = None

    def verify_state(self, operable):
        _validar_operable_activo(self, operable)
        self._operable = operable
        return self

    def do(self, transferencia):
        self.page.ir_a_transf_salientes()
        self.page.ir_a_transf_entrantes()
        self._transferencia = transferencia
        return self

    def success(self):
        tabla_obtenida = self.page.tabla_transferencia_entrante(self._transferencia.codigo)
        detalle_obtenido = self.page.detalle_transferencia_entrante(self._transferencia.codigo)

        self._assert.that(_tabla_entrante(self._transferencia, self._operable)).equals(tabla_obtenida)
        self._assert.that(_detalle_entrante(self._transferencia)).equals(detalle_obtenido)

    def failure(self, *args):
        pass


class RecepcionarTransferenciaAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)
        self._operable = None
        self._transferencia = None

    def verify_state(self, operable, transferencia):
        _validar_operable_activo(self, operable)
        self._assert.that(_tabla_entrante(transferencia, operable)).equals(
            self.page.tabla_transferencia_entrante(transferencia.codigo))

        self._operable = operable
        self._transferencia = transferencia
        return self

    def do(self):
        self.page.recepcionar_deposito(self._transferencia.codigo)
        return self

    def success(self):
        self._assert.that("El depósito fue recibido por la oficina").equals(self.page.get_toast())
        self.page.dismiss_toast()
        esperado = _tabla_entrante(self._transferencia, self._operable)
        esperado['Estado'] = EstadosTransferencia.PENDIENTE_CONFIRMACION['front']
        self._assert.that(esperado).equals(self.page.tabla_transferencia_entrante(self._transferencia.codigo))
        self._assert.that(EstadosTransferencia.PENDIENTE_CONFIRMACION['db']) \
            .equals(self.db.transferencia_por_numero(self._transferencia.numero)['estado_de_transferencia_id'])
        return EstadosTransferencia.PENDIENTE_CONFIRMACION

    def failure(self, *args):
        pass

    def fast_forward(self, operador, transferencia):
        id_transf = self.db.transferencia_por_numero(transferencia.numero)['id']
        self.api.login(operador)
        response = self.api.recepcionar_transferencia(id_transf)
        assert response.ok
        return EstadosTransferencia.PENDIENTE_CONFIRMACION


class ConfirmarTransferenciaAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)
        self._operable = None
        self._transferencia = None

    def verify_state(self, operable, transferencia):
        _validar_operable_activo(self, operable)

        esperado = _tabla_entrante(transferencia, operable)
        self._assert.that(esperado).equals(self.page.tabla_transferencia_entrante(transferencia.codigo))

        self.page.validar_modales(transferencia.codigo)
        self.page.nueva_confirmacion(transferencia.codigo)
        monedas_esperadas = [moneda.codigo for moneda in transferencia.montos]
        monedas_obtenidas = self.page.monedas_modal_entrante()
        self._assert.that(set(monedas_esperadas)).equals(set(monedas_obtenidas))
        self._assert.that(len(monedas_esperadas)).equals(len(monedas_obtenidas))
        self._transferencia = transferencia
        self._operable = operable
        return self

    def do(self, password):
        self.page.confirmar_deposito(self._transferencia.montos, password)
        return self

    def success(self):
        self._assert.that("Depósito confirmado con éxito.").equals(self.page.get_toast())
        self.page.dismiss_toast()
        # No deberia refrescar porque el sistema elimina la fila
        self.page.transferencia_stale(self._transferencia.codigo, False)

    def failure(self):
        self._assert.that(f"No se puede confirmar la transferencia {self._transferencia.codigo} "
                          f"porque no se encuentra pendiente de confirmación o recepción") \
            .equals(self.page.get_toast())
        self.page.dismiss_toast()
        self.page.cerrar_modal()

    def fast_forward(self, cajero, transferencia):
        id_transf = self.db.transferencia_por_numero(transferencia.numero)['id']
        self.api.login(cajero)
        response = self.api.confirmar_transferencia(id_transf, transferencia, cajero)
        assert response.ok


class ReportarProblemaTranferenciaAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)
        self._transferencia = None

    def verify_state(self, operable, transferencia):
        _validar_operable_activo(self, operable)
        esperado = _tabla_entrante(transferencia, operable)
        self._assert.that(esperado).equals(self.page.tabla_transferencia_entrante(transferencia.codigo))
        self._transferencia = transferencia
        return self

    def do(self, observacion, password):
        self.page.nuevo_reporte_problema(self._transferencia.codigo)
        self.page.confirmar_reporte_problema(observacion, password)
        return self

    def success(self):
        self._assert.that("Se ha reportado el problema con el depósito").equals(self.page.get_toast())
        self.page.dismiss_toast()
        self.page.transferencia_stale(self._transferencia.codigo, False)

    def failure(self):
        pass


# endregion

# region General

class TransferenciaFinalizadaAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)
        self._transferencia = None

    def verify_state(self, operable):
        _validar_operable_activo(self, operable)
        return self

    def do(self, transferencia, refresh=True):
        self.page.transferencia_stale(transferencia.codigo, refresh)
        self._transferencia = transferencia
        return self

    def success(self, success_type):
        estado = {
            "Contabilizada": EstadosTransferencia.CONTABILIZADA,
            "Cancelada": EstadosTransferencia.CANCELADA,
            "Hubo un Problema": EstadosTransferencia.ERROR_REPORTADO
        }[success_type]
        self._assert\
            .that(estado)\
            .equals(self.db.transferencia_por_numero(self._transferencia.numero)['estado_de_transferencia_id'])
        return estado

    def failure(self):
        pass

    def fast_forward(self, transferencia):
        self._assert\
            .that(EstadosTransferencia.CONTABILIZADA)\
            .equals(self.db.transferencia_por_numero(transferencia.numero)['estado_de_transferencia_id'])
        return EstadosTransferencia.CONTABILIZADA


# todo: ver donde meter este tipo de metodos :thinking:
def _tabla_entrante(transferencia, operable):
    esperado = {
        "Origen": transferencia.origen.codigo,
        "Estado": transferencia.estado['front'],
        "Medio": transferencia.medio,
        "Fecha": today(),
    }

    if operable.tipo == TiposOperable.Boveda:
        esperado["Montos"] = {moneda.codigo: str(monto) for moneda, monto in transferencia.montos.items()}
    return esperado


def _detalle_entrante(transferencia, codigo=None):
    if codigo is None:
        codigo = transferencia.codigo
    return {
        "Titulo": f"Detalle del depósito\n{codigo} - {today()}",
        "Medio": transferencia.medio,
        "Origen": transferencia.origen.codigo,
        "Observacion": transferencia.observaciones.get_label_text()
    }


def _tabla_saliente(transferencia):
    return {
        "Estado": transferencia.estado['front'],
        "Destino": transferencia.destino.codigo,
        "Montos": {moneda.codigo: str(monto) for moneda, monto in transferencia.montos.items()},
        "Fecha": today(),
        "Medio": transferencia.medio
    }


def _detalle_saliente(transferencia, codigo=None):
    if codigo is None:
        codigo = transferencia.codigo

    return {
        "Titulo": f"Detalle de extracción\n{codigo} - {today()}",
        "Medio": transferencia.medio,
        "Destino": transferencia.destino.codigo,
        "Montos": {moneda.codigo: str(monto) for moneda, monto in transferencia.montos.items()},
        "Observacion": transferencia.observaciones.get_label_text()
    }


def _validar_operable_activo(self, operable):
    self._assert.that(f"{operable.tipo} {operable.codigo}").equals(self.page.codigo_operable())

# endregion
