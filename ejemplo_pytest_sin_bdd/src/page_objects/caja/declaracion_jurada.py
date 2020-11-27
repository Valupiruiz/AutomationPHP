from selenium.common.exceptions import TimeoutException

from src.factory.page.listado_paginas import Paginas
from src.page_objects.caja.properties.locators import DeclaracionJuradaLocators
from src.page_objects.default.default import DefaultPage


class DeclaracionJuradaPage(DefaultPage):

    def __init__(self, driver, validar_pantalla):
        self._locators = DeclaracionJuradaLocators
        super().__init__(driver, validar_pantalla)
        # self.wait_for_url('/cajas/declaracion-jurada-caja')

    def ir_home_dj(self, deberia_bloquearse):
        # url = self.driver.current_url.replace('/cajas/declaracion-jurada-caja', '/login')
        # self.driver.get(url)
        # self.find_element(self._locators.BTN_DESCARGAR)
        # self.find_element(self._locators.BTN_HOME).click()
        if deberia_bloquearse:
            self.next_page = Paginas.CajaBloqueada
        else:
            self.next_page = Paginas.AperturaCaja


    def _validar_pantalla(self):
        pass
