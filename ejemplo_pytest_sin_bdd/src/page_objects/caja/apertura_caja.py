from selenium.common.exceptions import TimeoutException

from src.dominio.operable import TiposOperable
from src.dominio.operaciones import TiposOperacion
from src.factory.page.listado_paginas import Paginas
from src.page_objects.caja.properties.locators import AperturaCajaLocators
from src.page_objects.default.default import DefaultPage
from src.page_objects.page_elements.ingresar_montos import IngresarMontosPageElement
from src.page_objects.page_elements.modales.confirmar_montos import ModalConfirmarMontosPageElement


class AperturaCajaPage(DefaultPage):

    def __init__(self, driver, validar_pantalla):
        self._locators = AperturaCajaLocators
        self._ingresar_montos = IngresarMontosPageElement(self, TiposOperacion.Apertura, TiposOperable.Caja)
        self._modal_confirmar = ModalConfirmarMontosPageElement(self, TiposOperacion.Apertura, TiposOperable.Caja)
        super().__init__(driver, validar_pantalla)
        self.wait_for_url('/cajas/apertura-caja')
        self._tipo_operacion = TiposOperacion.Apertura
        self._tipo_operable = TiposOperable.Caja

    def aperturar_operable(self, caja, montos):
        self._ingresar_montos.completar_montos_accion(caja.codigo, montos)
        self._modal_confirmar.confirmar_accion(caja, montos)

    def monedas_operables_apertura(self):
        return self._ingresar_montos.monedas_operables()

    def next(self, deberia_bloquearse):
        if deberia_bloquearse:
            self.next_page = Paginas.CajaBloqueada
        else:
            self.next_page = Paginas.OperacionesCaja

    def alerta_sin_operaciones(self):
        return self.get_element_text(self._locators.LBL_ALERTA_SIN_OPERACIONES)

    def mensaje_sin_operaciones(self):
        return self.get_element_text(self._locators.LBL_MENSAJE_SIN_OPERACIONES)

    def mensaje_habilitar_operaciones_caja(self):
        return self.get_element_text(self._locators.LBL_COMUNIQUESE_CON_EL_AREA)

    def titulo_apertura(self):
        return self.get_element_text(self._locators.LBL_TITULO)

    def _validar_pantalla(self):
        try:
            self._ingresar_montos.validar_pantalla()
        except TimeoutException:
            # si rompe, me fijo si se mostro la pantalla de alerta en lugar de la apertura
            self.find_element(self._locators.LBL_ALERTA_SIN_OPERACIONES)
            return
        else:
            elems = self.find_elements(self._locators.TXT_MONTOS)
            for e in elems:
                e.send_keys(1)
            self.find_element(self._locators.BTN_APERTURAR).click()
            self._modal_confirmar.validar_pantalla()
            self.driver.refresh()
            self.wait_for_url('/cajas/apertura-caja')
