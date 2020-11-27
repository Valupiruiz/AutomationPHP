from src.page_objects.dashboard.properties.locators import DashboardLocators
from src.page_objects.default.default import DefaultPage


class DashboardPage(DefaultPage):

    def __init__(self, driver, validar_pagina):
        self._locators = DashboardLocators
        super().__init__(driver, validar_pagina)
        # self.wait_for_url("/dashboard") por alguna razon ahora redireccionan a config

    def _validar_pantalla(self):
        pass