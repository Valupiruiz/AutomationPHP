from time import sleep

from src.actions.base.base_action import BaseAction
from src.dominio.operable import TiposOperable, Operable
from src.factory.page.listado_paginas import Paginas
from src.dominio.operable import EstadosOperable


class AperturaOperableAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)
        self._operable = None
        self._apertura = None

    def verify_state(self, operable):
        # Solo se puede operar si la cantidad de monedas es correcta
        self._operable = operable
        monedas_disponibles_esperadas = [moneda.codigo for moneda in self._operable.monedas_permitidas]
        monedas_disponibles_obtenidas = self.page.monedas_operables_apertura()
        self._assert.that(len(monedas_disponibles_obtenidas)).equals(len(monedas_disponibles_esperadas))
        self._assert.that(set(monedas_disponibles_obtenidas)).equals(set(monedas_disponibles_esperadas))
        self._assert.that(operable.codigo).contains(self.page.titulo_apertura())
        return self

    def do(self, apertura, deberia_desbloquearla=False, deberia_bloquearse=False):
        self._apertura = apertura

        self.page.aperturar_operable(self._operable, apertura.montos)
        self._desbloquear_si_deberia(deberia_desbloquearla)
        self.page.next(deberia_bloquearse)
        return self

    def _cambiar_estado(self, nuevo_estado, estado_anterior):
        self.page.wait.until(
            lambda x: self.db.get_estado_caja(self._operable.codigo) == estado_anterior)
        self.db.modificar_estado_caja(self._operable.codigo, nuevo_estado)
        self.page.wait.until(lambda x: self.db.get_estado_caja(self._operable.codigo) == nuevo_estado)
        self.page.driver.refresh()

    def _desbloquear_si_deberia(self, deberia):
        sleep(1)
        if deberia:
            self._cambiar_estado(EstadosOperable.ABIERTA, EstadosOperable.BLOQUEADA)
        self.page.driver.refresh()

    def success(self):
        self._assert.that(f"{self._operable.tipo} {self._operable.codigo}").equals(self.page.codigo_operable())

    def failure(self):
        _validar_bloqueo(self)

    def fast_forward(self, operador, operable, apertura, desbloquear=False, asignar_operador=False, redireccionar=True):
        if asignar_operador:
            self.db.asignar_operador(operador, operable.codigo)
        self._operable = operable
        metodo = {
            TiposOperable.Caja: self.api.aperturar_caja,
            TiposOperable.Boveda: self.api.aperturar_boveda,
        }[operable.tipo]
        self.api.login(operador)
        response = metodo(operable, apertura, operador)
        assert response.ok
        self._desbloquear_si_deberia(desbloquear)
        if redireccionar:
            self.page.create_with_name(Paginas.OperacionesCaja, refresh=not desbloquear)


class CierreOperableAction(BaseAction):

    def __init__(self, context):
        super().__init__(context)
        self._operable = None
        self._operacion = None
        self._failure_types = {
            "Operaciones Pendientes": self._operaciones_pendientes,
            "Bloqueo": self._bloqueo
        }

    def verify_state(self, operable, operacion):
        self._operacion = operacion
        self._operable = operable
        self.page.ir_tipo_cierre(self._operacion.tipo, self._operable.tipo)
        monedas_disponibles_esperadas = [moneda.codigo for moneda in self._operable.monedas_permitidas]
        monedas_disponibles_obtenidas = self.page.monedas_operables_cierre()
        self._assert.that(len(monedas_disponibles_obtenidas)).equals(len(monedas_disponibles_esperadas))
        self._assert.that(set(monedas_disponibles_obtenidas)).equals(set(monedas_disponibles_esperadas))
        return self

    def do(self, password, should_redirect=True):
        # todo: utilizar pw
        self.page.realizar_cierre(self._operable, self._operacion.montos, should_redirect)
        return self

    def success(self):
        self._assert.that(f"Apertura de {self._operable.tipo.lower()} {self._operable.codigo}").equals(
            self.page.titulo_apertura())

    def failure(self, failure_type):
        self._failure_types[failure_type]()

    def fast_forward(self, operador, operable, cierre, redirect=True):
        metodo, target_page = {
            TiposOperable.Caja: [self.api.cerrar_totalmente_caja, Paginas.AperturaCaja],
            TiposOperable.Boveda: [self.api.cerrar_boveda, Paginas.AperturaBoveda]
        }[operable.tipo]
        self.api.login(operador)
        response = metodo(operable, cierre, operador)
        assert response.ok
        assert self.db.get_estado_caja(operable.codigo) == EstadosOperable.CERRADA_TOTALMENTE
        if redirect:
            self.page.create_with_name(target_page, refresh=True)

    def _operaciones_pendientes(self):
        self._assert.that(f"La {self._operable.tipo.lower()} ({self._operable.codigo}) no puede cerrarse por que "
                          f"tiene operaciones pendientes").equals(self.page.get_toast())
        self.page.dismiss_toast()
        self.page.cerrar_modal_confirmacion()

    def _bloqueo(self):
        _validar_bloqueo(self)


def _validar_bloqueo(self):
    # Lleva un espacio adelante porque :shrug:
    self._assert.that(f" La caja {self._operable.codigo} se ha bloqueado").equals(self.page.titulo_bloqueo())
    self._assert.that("No podrá operar con esta caja.").equals(self.page.subtitulo_bloqueo())
