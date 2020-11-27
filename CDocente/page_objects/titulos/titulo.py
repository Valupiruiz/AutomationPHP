from page_objects.base_page import BasePage
from .locators import TitulosLocators
import time


class Titulo(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = TitulosLocators()

    def abrir_buscador_titulos(self):
        self.find_element(self.__locators.BUSCADOR_BTN).click()

    def buscar_por_titulo(self, titulo, sin_secundario):
        if sin_secundario:
            time.sleep(1)
            self.find_element(self.__locators.SIN_SECUNDARIO_CHK).click()
            self.find_element(self.__locators.ACEPTAR_SIN_SEC_BTN, 30).click()
        self.find_element(self.__locators.TITULO_INP).send_keys(titulo)
        self.find_element(self.__locators.BUSCAR_BTN).click()

    def agregar_titulo(self, titulo):
        _locator = self.__locators.AGREGAR_TEMP_BTN.formatear_locator({"titulo": titulo})
        self.find_element(_locator).click()

    def se_cargo_exitosamente(self):
        return self.find_element(self.__locators.ALERT_SPAN).text


