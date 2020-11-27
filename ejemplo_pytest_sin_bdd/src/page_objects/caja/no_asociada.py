from src.page_objects.caja.properties.locators import CajaNoAsociadaLocators
from src.page_objects.default.default import DefaultPage


class CajaNoAsociadaPage(DefaultPage):

    def __init__(self, driver, validar_pagina):
        self._locators = CajaNoAsociadaLocators
        super().__init__(driver, validar_pagina)
        self.wait_for_url("/cajas/no-asociada")

    def titulo_operable_sin_asignar(self):
        return self.find_element(self._locators.LBL_MENSAJE).text

    def _validar_pantalla(self):
        pass
