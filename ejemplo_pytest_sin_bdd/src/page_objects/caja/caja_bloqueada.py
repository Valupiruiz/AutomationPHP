from src.page_objects.caja.properties.locators import CajaBloqueadaLocators
from src.page_objects.default.default import DefaultPage


class CajaBloqueadaPage(DefaultPage):

    def __init__(self, driver, validar_pagina):
        self._locators = CajaBloqueadaLocators
        super().__init__(driver, validar_pagina)
        self.wait_for_url('/cajas/bloqueada')

    def titulo_bloqueo(self):
        return self.find_element(self._locators.LBL_TITULO).text

    def subtitulo_bloqueo(self):
        return self.find_element(self._locators.LBL_SUBTITULO).text

    def _validar_pantalla(self):
        pass
