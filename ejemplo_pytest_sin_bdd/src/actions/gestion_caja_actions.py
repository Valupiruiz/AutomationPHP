import datetime

from src.actions.base.base_action import BaseAction
from random import choice

from src.utils.others import today, parse_iso_date


class AsignarCajeroCajaAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)
        self._caja = None
        self._oficina = None
        self._cajero = None

    def verify_state(self, caja, oficina, nombre_cajero):
        _buscar_caja(self, caja, oficina)
        if nombre_cajero is None:
            estado_esperado = "No asignada"
            usuario_detalle = "Sin asignacion"
            usuario_tabla = "No asignada"
        else:
            estado_esperado = "Operativa"
            usuario_tabla = nombre_cajero
            usuario_detalle = nombre_cajero
        _validar_tabla(self, caja, oficina, usuario_tabla, estado_esperado)

        self.page.nueva_asignacion(caja.codigo)
        detalles_esperado = {
            "Codigo": caja.codigo,
            "Oficina": oficina.nombre,
            "Usuario": usuario_detalle
        }
        self._assert.that(detalles_esperado).equals(self.page.detalle_asignar_usuario())
        self._caja = caja
        self._oficina = oficina
        return self

    def do(self, cajero):
        if cajero is None:
            self.page.confirmar_desasignacion()
        else:
            self.page.confirmar_asignacion(cajero)
            self._cajero = cajero
        return self

    # region success
    def success(self, success_type):
        {
            "Usuario asignado": self._usuario_asignado_correctamente,
            "Usuario desasignado": self._usuario_desasignado_correctamente
        }[success_type]()

    def _usuario_desasignado_correctamente(self):
        self._assert.that("Se ha desasignado el usuario a la caja con éxito").equals(self.page.get_toast())
        self.page.dismiss_toast()
        tabla_obtenida = self.page.tabla_caja(self._caja.codigo)
        tabla_esperada = {
            "Codigo": self._caja.codigo,
            "Usuario": "No asignada",
            "Oficina": self._oficina.nombre,
            "Estado": "No asignada"
        }
        self._assert.that(tabla_obtenida).equals(tabla_esperada)

    def _usuario_asignado_correctamente(self):
        self._assert.that("Se ha asignado el usuario a la caja con éxito").equals(self.page.get_toast())
        self.page.dismiss_toast()
        tabla_obtenida = self.page.tabla_caja(self._caja.codigo)
        tabla_esperada = {
            "Codigo": self._caja.codigo,
            "Usuario": self._cajero.nombre_completo(),
            "Oficina": self._oficina.nombre,
            "Estado": "Operativa"
        }
        self._assert.that(tabla_obtenida).equals(tabla_esperada)

    # endregion

    # region failure
    def failure(self, failure_type):
        {
            "Asignar caja abierta": self._error_asignar_caja_abierta,
            "Desasignar caja abierta": self._error_desasignar_caja_abierta,
        }[failure_type]()

    def _message_error_failure_type(self, toast_text):
        self._assert.that(toast_text).equals(self.page.get_toast())
        self.page.dismiss_toast()
        self.page.cerrar_modal()

    def _error_desasignar_caja_abierta(self):
        self._message_error_failure_type(
            f'No se puede desasignar al cajero de la caja {self._caja.codigo} porque no se '
            f'encuentra cerrada totalmente')

    def _error_asignar_caja_abierta(self):
        self._message_error_failure_type(f'No se puede asignar al cajero a la caja {self._caja.codigo} '
                                         f''f'porque no se encuentra cerrada totalmente')
    # endregion


class DesbloquearCajaAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)
        self._oficina = None
        self._bloqueo = None

    def verify_state(self, bloqueo, oficina):
        _buscar_caja(self, bloqueo.caja, oficina)
        _validar_tabla(self, bloqueo.caja, oficina, bloqueo.cajero.nombre_completo(), "Bloqueada")
        self.page.nuevo_desbloqueo(bloqueo.caja.codigo, oficina.nombre)
        self._validar_nuevo_desbloqueo(bloqueo, self.page.detalle_bloqueo(), self.page.diferencias_monto_bloqueo())
        self._oficina = oficina
        self._bloqueo = bloqueo
        return self

    def do(self, resolucion):
        self.page.desbloquear_caja(resolucion)
        return self

    def success(self):
        self._assert.that("Se ha desbloqueado la caja con éxito").equals(self.page.get_toast())
        self.page.dismiss_toast()
        _validar_tabla(self, self._bloqueo.caja, self._oficina, self._bloqueo.cajero.nombre_completo(), "Operativa")
        self._assert.that("CerradoTotalmente").equals(self.db.get_estado_caja(self._bloqueo.caja.codigo))

    def failure(self):
        pass

    def fast_forward(self, operador, bloqueo, resolucion):
        self.api.login(operador)
        response = self.api.gestion_caja(bloqueo.caja)
        assert response.ok
        # todo: utilizar algun tipo de mapeo para que no sea tan feo
        informacion = response.json()['items'][0]
        detalle = {
            "Usuario": informacion['nombreUsuario'],
            "Fecha": parse_iso_date(informacion['bloqueo']['fecha']),
            "Situacion": informacion['bloqueo']['situacion']
        }
        diferencias = {
            "Logicos": {l['moneda']: str(l['cantidad']) for l in informacion['montos']['logicos']},
            "Reales": {l['moneda']: str(l['cantidad']) for l in informacion['montos']['reales']},
            "Diferencias": {l['moneda']: str(l['cantidad']) for l in informacion['montos']['diferencias']}
        }
        self._validar_nuevo_desbloqueo(bloqueo, detalle, diferencias)
        response = self.api.desbloquear_caja(bloqueo.caja, resolucion)
        assert response.ok

    def _validar_nuevo_desbloqueo(self, bloqueo, detalle, diferencias):
        detalle_esperado = {
            "Usuario": bloqueo.cajero.nombre_completo(),
            "Fecha": today(),
            "Situacion": bloqueo.situacion
        }
        self._assert.that(detalle_esperado).equals(detalle)
        tabla_diferencias_esperada = {
            "Logicos": bloqueo.logico,
            "Reales": bloqueo.reales,
            "Diferencias": bloqueo.diferencias
        }
        self._assert.that(tabla_diferencias_esperada).equals(diferencias)


def _buscar_caja(self, caja, oficina):
    filtros = {
        "Codigo": caja.codigo,
        "Oficina": choice([oficina.nombre, None])
    }
    self.page.buscar_caja(filtros)


def _validar_tabla(self, caja, oficina, nombre_cajero, estado):
    tabla_obtenida = self.page.tabla_caja(caja.codigo)
    tabla_esperada = {
        "Codigo": caja.codigo,
        "Usuario": nombre_cajero,
        "Oficina": oficina.nombre,
        "Estado": estado,
    }
    self._assert.that(tabla_obtenida).equals(tabla_esperada)
