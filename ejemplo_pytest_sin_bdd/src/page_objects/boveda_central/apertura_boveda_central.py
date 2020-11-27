from selenium.common.exceptions import TimeoutException

from src.dominio.operable import TiposOperable
from src.dominio.operaciones import TiposOperacion
from src.factory.page.listado_paginas import Paginas
from src.page_objects.caja.properties.locators import AperturaCajaLocators
from src.page_objects.default.default import DefaultPage
from src.page_objects.page_elements.ingresar_montos import IngresarMontosPageElement
from src.page_objects.page_elements.modales.confirmar_montos import ModalConfirmarMontosPageElement


class AperturaBovedaPage(DefaultPage):

    def __init__(self, driver, validar_pantalla):
        self._ingresar_montos = IngresarMontosPageElement(self, TiposOperacion.Apertura, TiposOperable.Boveda)
        self._modal_confirmar = ModalConfirmarMontosPageElement(self, TiposOperacion.Apertura, TiposOperable.Boveda)
        self._locators = AperturaCajaLocators
        super().__init__(driver, validar_pantalla)
        self.wait_for_url('/boveda-central/apertura-boveda-central')

    def aperturar_operable(self, boveda, montos):
        self._ingresar_montos.completar_montos_accion(boveda.codigo, montos)
        self._modal_confirmar.confirmar_accion(boveda, montos)

    def monedas_operables_apertura(self):
        return self._ingresar_montos.monedas_operables()

    def next(self, deberia_bloquearse):
        if deberia_bloquearse:
            self.next_page = Paginas.CajaBloqueada
        else:
            self.next_page = Paginas.OperacionesCaja

    def titulo_apertura(self):
        return self.find_element(self._locators.LBL_TITULO).text

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
            self.wait_for_url('/boveda-central/apertura-boveda-central')
