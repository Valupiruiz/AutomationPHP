from src.dominio.operable import TiposOperable
from src.dominio.operaciones import TiposOperacion
from src.factory.page.listado_paginas import Paginas
from src.page_objects.default.default import DefaultPage
from src.page_objects.page_elements.properties.locators import NavBarLocators


class NavBarPageElement(DefaultPage):

    def __init__(self, driver, validar_pagina):
        self.__locators = NavBarLocators
        super().__init__(driver, validar_pagina)

    def ir_tipo_cierre(self, tipo_cierre, tipo_operable):
        self.find_element(self.__locators.BTN_CIERRES).click()
        self.find_element(self.__locators.LISTA)
        self.find_element(self._botones_por_tipo_cierre(tipo_cierre)).click()
        self.next_page = self._pages_por_tipo_cierre(tipo_cierre, tipo_operable)

    def ir_a_transf_salientes(self):
        self.find_element(self.__locators.NAV_BAR)
        self.find_element(self.__locators.BTN_TRANSFERENCIAS_SALIENTES).click()
        self.next_page = Paginas.TransferenciasSalientes

    def ir_a_transf_entrantes(self):
        self.find_element(self.__locators.NAV_BAR)
        self.find_element(self.__locators.BTN_TRANSFERENCIAS_ENTRANTES).click()
        self.next_page = Paginas.TransferenciasEntrantes

    def _pages_por_tipo_cierre(self, tipo_cierre, tipo_operable):
        return {
            TiposOperacion.CierreParcial: {TiposOperable.Caja: Paginas.CierreParcialCaja},
            TiposOperacion.CierreTotal: {TiposOperable.Caja: Paginas.CierreTotalCaja,
                                         TiposOperable.Boveda: Paginas.CierreTotalBoveda},
        }[tipo_cierre][tipo_operable]

    def _botones_por_tipo_cierre(self, tipo_cierre):
        return {
            TiposOperacion.CierreParcial: self.__locators.BTN_CIERRE_PARCIAL,
            TiposOperacion.CierreTotal: self.__locators.BTN_CIERRE_TOTAL,
        }[tipo_cierre]

    def _validar_pantalla(self):
        self.find_element(self.__locators.BTN_HOME)
        self.find_element(self.__locators.BTN_CIERRES)
        self.find_element(self.__locators.BTN_TRANSFERENCIAS_ENTRANTES)
        self.find_element(self.__locators.BTN_TRANSFERENCIAS_SALIENTES)
