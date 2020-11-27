from src.page_objects.boveda_central.properties.locators import BovedaNoAsociadaLocators
from src.page_objects.default.default import DefaultPage


class BovedaNoAsociadaPage(DefaultPage):

    def __init__(self, driver, validar_pagina):
        self._locators = BovedaNoAsociadaLocators
        super().__init__(driver, validar_pagina)
        self.wait_for_url("/boveda-central/no-asociada")

    def titulo_operable_sin_asignar(self):
        return self.find_element(self._locators.LBL_MENSAJE).text

    def _validar_pantalla(self):
        pass
