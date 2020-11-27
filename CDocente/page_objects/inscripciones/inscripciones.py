from page_objects.base_page import BasePage
from .locators import InscripcionesLocators


class Inscripciones(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = InscripcionesLocators()

    def inscribirse(self):
        self.find_element(self.__locators.NUEVA_INSC_BTN).click()

