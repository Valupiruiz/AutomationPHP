from datetime import datetime

from src.actions.base.base_action import BaseAction
from src.dominio.operaciones import EstadosTransferencia
from src.utils.others import seconds_before_now, today


class CompletarSolicitudFondosAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)
        self._solicitud = None
        self._time = None

    def verify_state(self, operable):
        self._assert.that(f"{operable.tipo} {operable.codigo}").equals(self.page.codigo_operable())
        self.page.ir_a_transf_entrantes()
        self.page.pill_solicitud_fondos()
        self.page.nueva_solicitud()
        monedas_esperadas = [moneda.codigo for moneda in operable.monedas_permitidas]
        monedas_obtenidas = self.page.monedas_modal_entrante()
        self._assert.that(set(monedas_esperadas)).equals(set(monedas_obtenidas))
        self._assert.that(len(monedas_esperadas)).equals(len(monedas_obtenidas))
        return self

    def do(self, solicitud, password):
        self._time = datetime.utcnow()
        self.page.generar_solicitud(solicitud.montos, solicitud.observaciones, password)
        self._solicitud = solicitud
        return self

    def success(self):
        self._assert.that("Solicitud creada con éxito.").equals(self.page.get_toast())
        self.page.dismiss_toast()
        transf = self.db.get_transferencia(self._solicitud)
        self._assert.that(transf["fecha"]).greater_than(self._time)
        codigo = f"{transf['tipo_de_transaccion_id']}-{transf['numero_transaccion']}"
        tabla_obtenida = self.page.tabla_solicitud_fondos(codigo)
        detalle_obtenido = self.page.detalle_solicitud_fondos(codigo)
        self._assert.that(_tabla_solicitud_fondos(self._solicitud)).equals(tabla_obtenida)
        self._assert.that(_detalle_solicitud(self._solicitud, codigo)).equals(detalle_obtenido)
        return codigo

    def failure(self, caja):
        # tfs#1660
        self._assert.that(f"No se puede crear la solicitud de fondos porque la bóveda {caja.codigo} "
                          f"no se encuentra abierta").equals(self.page.get_toast())
        self.page.dismiss_toast()
        self.page.cerrar_modal()


class RecibirSolicitudFondosAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)
        self._solicitud = None

    def verify_state(self, boveda):
        self._assert.that(f"{boveda.tipo} {boveda.codigo}").equals(self.page.codigo_operable())
        return self

    def do(self, solicitud):
        self.page.ir_a_transf_salientes()
        self.page.pill_solicitud_fondos()
        self._solicitud = solicitud
        return self

    def success(self):
        tabla_obtenida = self.page.tabla_solicitud_entrante(self._solicitud.codigo)
        detalle_obtenido = self.page.detalle_solicitud_fondos(self._solicitud.codigo)
        self._assert.that(_tabla_solicitud_entrante(self._solicitud)).equals(tabla_obtenida)
        self._assert.that(_detalle_solicitud(self._solicitud)).equals(detalle_obtenido)

    def failure(self):
        pass


class AceptarSolicitudFondosAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)
        self._solicitud = None

    def verify_state(self, boveda, solicitud):
        self._assert.that(f"{boveda.tipo} {boveda.codigo}").equals(self.page.codigo_operable())
        self._assert.that(_tabla_solicitud_entrante(solicitud)).equals(
            self.page.tabla_solicitud_entrante(solicitud.codigo))
        self._assert.that(_detalle_solicitud(solicitud)).equals(self.page.detalle_solicitud_fondos(solicitud.codigo))

        self.page.nueva_autorizacion_solicitud(solicitud.codigo)

        montos = {moneda.codigo: str(monto) for moneda, monto in solicitud.montos.items()}
        self._assert.that(montos).equals(self.page.montos_autorizacion_solicitud())
        self._solicitud = solicitud
        return self

    def do(self, password, montos=None):
        if montos is not None:  # Si le envio montos, significa que son distintos de lo solicitado
            self.page.modificar_montos_autorizacion_solicitud(montos)
        self.page.autorizar_solicitud(str(self._solicitud.observaciones), password)
        return self

    def success(self, transferencia):
        self._assert.that("Se autorizó con éxito la solicitud").equals(self.page.get_toast())
        self.page.dismiss_toast()
        self.page.solicitud_stale(self._solicitud.codigo, False)

        self.page.ir_a_transf_entrantes()
        self.page.ir_a_transf_salientes()
        self.page.pill_extracciones_en_curso()
        tabla_esperada = {
            "Estado": transferencia.estado['front'],
            "Destino": transferencia.destino.codigo,
            "Montos": {moneda.codigo: str(monto) for moneda, monto in transferencia.montos.items()},
            "Fecha": today(),
            "Medio": transferencia.medio
        }
        tabla_obtenida = self.page.tabla_transferencia_saliente(transferencia.codigo)
        self._assert.that(tabla_esperada).equals(tabla_obtenida)

        detalle_esperado = {
            "Titulo": f"Detalle de extracción\n{transferencia.codigo} - {today()}",
            "Medio": transferencia.medio,
            "Destino": transferencia.destino.codigo,
            "Montos": {moneda.codigo: str(monto) for moneda, monto in transferencia.montos.items()},
            "Observacion": transferencia.observaciones.get_label_text()
        }
        detalle_obtenido = self.page.detalle_transferencia_saliente(transferencia.codigo)
        self._assert.that(detalle_esperado).equals(detalle_obtenido)

    def failure(self):
        self._assert.that("No cuenta con fondos suficientes para realizar la operación").equals(self.page.get_toast())
        self.page.dismiss_toast()
        self.page.cerrar_modal()


class RechazarSolicitudFondosAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)
        self._solicitud = None

    def verify_state(self, boveda, solicitud):
        self._assert.that(f"{boveda.tipo} {boveda.codigo}").equals(self.page.codigo_operable())
        self._assert.that(_tabla_solicitud_entrante(solicitud)).equals(
            self.page.tabla_solicitud_entrante(solicitud.codigo))
        self._assert.that(_detalle_solicitud(solicitud)).equals(self.page.detalle_solicitud_fondos(solicitud.codigo))

        self.page.nuevo_rechazo(solicitud.codigo)
        self._solicitud = solicitud
        return self

    def do(self, password):
        self.page.rechazar_solicitud(str(self._solicitud.observaciones), password)
        return self

    def success(self):
        self._assert.that("Se rechazó con éxito la solicitud.").equals(self.page.get_toast())
        self.page.dismiss_toast()
        self.page.solicitud_stale(self._solicitud.codigo, False)

    def failure(self):
        pass


class CancelarSolicitudFondosAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)
        self._solicitud = None

    def verify_state(self, solicitante, solicitud):
        self._assert.that(f"{solicitante.tipo} {solicitante.codigo}").equals(self.page.codigo_operable())
        self.page.ir_a_transf_entrantes()
        self.page.pill_solicitud_fondos()
        tabla_obtenida = self.page.tabla_solicitud_fondos(solicitud.codigo)
        detalle_obtenido = self.page.detalle_solicitud_fondos(solicitud.codigo)
        self._assert.that(_tabla_solicitud_fondos(solicitud)).equals(tabla_obtenida)
        self._assert.that(_detalle_solicitud(solicitud)).equals(detalle_obtenido)
        self._solicitud = solicitud
        return self

    def do(self, password):
        self.page.nueva_cancelacion_solicitud(self._solicitud.codigo)
        detalle_esperado = {
            "Montos": {moneda.codigo: str(monto) for moneda, monto in self._solicitud.montos.items()},
            "Observacion": self._solicitud.observaciones.get_label_text()
        }
        self._assert.that(detalle_esperado).equals(self.page.detalle_cancelacion_solicitud())
        self.page.confirmar_cancelacion_solicitud_fondos(password)
        return self

    def success(self):
        pass

    def failure(self):
        pass


class SolicitudFinalizadaAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)
        self._solicitud = None

    def verify_state(self, solicitante):
        self._assert.that(f"{solicitante.tipo} {solicitante.codigo}").equals(self.page.codigo_operable())
        return self

    def do(self, solicitud, refresh=True):
        self.page.solicitud_stale(solicitud.codigo, refresh)
        self._solicitud = solicitud
        return self

    def success(self, success_type):
        estado = {
            "Aceptada": EstadosTransferencia.PENDIENTE_RECEPCION['db'],
            "Rechazada": "SolicitudRechazada"
        }[success_type]
        self._assert.that(estado).equals(self.db.transferencia_por_numero(self._solicitud.numero)['estado_de_transferencia_id'])

    def failure(self):
        pass


def _tabla_solicitud_entrante(solicitud):
    return {
        "Estado": solicitud.estado,
        "Montos": {moneda.codigo: str(monto) for moneda, monto in solicitud.montos.items()},
        "Fecha": today(),
        "Origen": solicitud.origen.codigo,
    }


def _detalle_solicitud(solicitud, codigo=None):
    if codigo is None:
        codigo = solicitud.codigo

    return {
        "Titulo": f"Detalle de solicitud\n{codigo} - {today()}",
        # "Info Text": "Se ha solicitado depósito de los siguientes montos:",
        "Montos": {moneda.codigo: str(monto) for moneda, monto in solicitud.montos.items()},
        "Observacion": solicitud.observaciones.get_label_text()
    }


def _tabla_solicitud_fondos(solicitud):
    return {
        "Fecha": today(),
        "Montos": {moneda.codigo: str(monto) for moneda, monto in solicitud.montos.items()},
        "Estado": solicitud.estado
    }
