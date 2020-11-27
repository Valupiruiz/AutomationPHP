from src.dominio.operable import TiposOperable
from src.dominio.operaciones import TiposOperacion
from src.factory.page.listado_paginas import Paginas
from src.page_objects.default.default import DefaultPage
from src.page_objects.page_elements.ingresar_montos import IngresarMontosPageElement
from src.page_objects.page_elements.modales.confirmar_montos import ModalConfirmarMontosPageElement


class CierreTotalCajaPage(DefaultPage):

    def __init__(self, driver, validar_pantalla):
        self._ingresar_montos = IngresarMontosPageElement(self, TiposOperacion.CierreTotal, TiposOperable.Caja)
        self._modal_confirmar = ModalConfirmarMontosPageElement(self, TiposOperacion.CierreTotal, TiposOperable.Caja)
        super().__init__(driver, validar_pantalla)
        self.wait_for_url('/cajas/operaciones/cierre-total')

    def realizar_cierre(self, caja, montos, should_redirect):
        self._ingresar_montos.completar_montos_accion(caja.codigo, montos)
        self._modal_confirmar.confirmar_accion(caja, montos)
        if should_redirect:
            self.next_page = Paginas.DeclaracionJurada

    def monedas_operables_cierre(self):
        return self._ingresar_montos.monedas_operables()

    def cerrar_modal_confirmacion(self):
        self._modal_confirmar.cerrar()

    def _validar_pantalla(self):
        pass
