from src.page_objects.caja.properties.locators import OperacionesLocators
from src.page_objects.page_elements.nav_bar import NavBarPageElement


class OperacionesPage(NavBarPageElement):

    def __init__(self, driver, validar_pagina):
        self._locators = OperacionesLocators
        super().__init__(driver, validar_pagina)
        self.wait_for_url('/operaciones')

    def _validar_pantalla(self):
        pass
