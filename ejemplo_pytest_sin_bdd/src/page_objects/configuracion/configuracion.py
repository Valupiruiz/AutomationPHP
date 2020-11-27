from src.factory.page.listado_paginas import Paginas
from src.page_objects.configuracion.properties.locators import ConfiguracionLocators
from src.page_objects.default.default import DefaultPage


class Configuracion(DefaultPage):

    def __init__(self, driver, validar_pantalla):
        self._locators = ConfiguracionLocators
        super().__init__(driver, validar_pantalla)
        self.wait_for_url("/configuration")

    def configurar_sucursales(self):
        self.find_element(self._locators.ConfigSucursal).click()
        self.next_page = Paginas.Sucursal

    def _validar_pantalla(self):
        pass