class TiposOperacion:
    Apertura = 'Apertura'
    CierreParcial = 'Cierre Parcial'
    CierreTotal = 'Cierre Total'
    Transferencia = 'Transferencia'
    Solicitud = "Solicitud de Fondos"


class EstadosTransferencia:
    PENDIENTE_RECEPCION = {"front": "Pendiente de recepción", "db": 2}
    PENDIENTE_CONFIRMACION = {"front": "Pendiente de confirmación", "db": 3}
    # A partir de esta instancia, ya no se muestran por interface asique no es necesario un dict
    CONTABILIZADA = 4
    CANCELADA = 6
    ERROR_REPORTADO = 7


class BaseOperacion:

    # valor relativo a como debe contabilizarse en el balance
    def relative_value(self, operable):
        raise NotImplementedError()


class Apertura(BaseOperacion):

    def __init__(self, montos, observaciones=None):
        self.tipo = TiposOperacion.Apertura
        self.montos = montos
        self.observaciones = ObservacionOperacion(observaciones)

    def relative_value(self, operable):
        return self.montos


class CierreParcial(BaseOperacion):

    def __init__(self, montos, observaciones=None):
        self.tipo = TiposOperacion.CierreParcial
        self.montos = montos
        self.observaciones = ObservacionOperacion(observaciones)

    # los cierres no se contabilizan contra el balance
    def relative_value(self, operable):
        return {moneda: 0 for moneda in self.montos}


class CierreTotal(BaseOperacion):

    def __init__(self, montos, observaciones=None):
        self.tipo = TiposOperacion.CierreTotal
        self.montos = montos
        self.observaciones = ObservacionOperacion(observaciones)

    # los cierres no se contabilizan contra el balance
    def relative_value(self, operable):
        return {moneda: 0 for moneda in self.montos}


class Transferencia(BaseOperacion):

    def __init__(self, origen, destino, montos, observacion=None):
        self.origen = origen
        self.destino = destino
        self.montos = montos
        self.estado = EstadosTransferencia.PENDIENTE_RECEPCION
        if observacion is None:  # fixme
            self.observaciones = ObservacionOperacion(self.__get_obs())
        else:
            self.observaciones = observacion
        self.tipo = TiposOperacion.Transferencia
        self.codigo = None
        self.medio = "Transferencia logística"

    @property
    def numero(self):
        numero = None
        if self.codigo is not None:
            _, numero = self.codigo.split('-')
        return numero

    def __get_obs(self):
        # todo: sacar esto de aca, la transferencia deberia recibir las observaciones en lugar de generarlas
        from random import choice
        if choice([True, False]):
            return f"Extraccion de {self.origen.codigo} hacia {self.destino.codigo}"
        return None

    def relative_value(self, operable):
        if self.origen == operable:  # en origen, la resta se realiza solo si no esta cancelada
            if self.estado != EstadosTransferencia.CANCELADA:
                return {moneda: -monto for moneda, monto in self.montos.items()}

        if self.destino == operable:  # en destino, la suma se realiza cuando se contabiliza
            if self.estado == EstadosTransferencia.CONTABILIZADA:
                return self.montos

        return {moneda: 0 for moneda in self.montos}


class ObservacionOperacion(object):

    def __init__(self, observacion):
        self.observacion = observacion

    def get_label_text(self):
        # Si la transferencia no tiene observacion, se muestra como "Sin Observacion"
        if self.observacion is None:
            return "Sin observación"
        return self.observacion

    def __str__(self):
        return self.observacion or ''

    def __bool__(self):
        return self.observacion is not None

    def __eq__(self, other):
        return self.observacion == other


class SolicitudFondo:

    def __init__(self, origen, destino, montos):
        self.codigo = None
        self.tipo = TiposOperacion.Solicitud
        self.estado = "Esperando confirmación"
        self.montos = montos
        self.origen = origen
        self.destino = destino
        self.observaciones = ObservacionOperacion(self._get_obs())

    @property
    def numero(self):
        numero = None
        if self.codigo is not None:
            _, numero = self.codigo.split('-')
        return numero

    def _get_obs(self):
        from random import choice
        if choice([True, False]):
            return f"Solicitud de fondos de {self.origen.codigo} hacia {self.destino.codigo}"
        return None


class Bloqueo:

    def __init__(self, caja, cajero, situacion, logico, reales, diferencia):
        self.caja = caja
        self.cajero = cajero
        self.logico = {moneda.codigo: str(monto) for moneda, monto in logico.items()}
        self.reales = {moneda.codigo: str(monto) for moneda, monto in reales.items()}
        self.diferencias = {moneda.codigo: str(monto) for moneda, monto in diferencia.items()}
        self.situacion = situacion
