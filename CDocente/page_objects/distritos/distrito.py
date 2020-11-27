from page_objects.base_page import BasePage
from .locators import DistritoLocators
import time


class Distrito(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = DistritoLocators()

    def editar_area(self, area):
        self.find_select(self.__locators.AREA_SEL).select_by_visible_text(area)
        _locator = self.__locators.AREA_TEMP.formatear_locator({"area": area})
        self.find_element(_locator).click()

    def seleccionar_distrito(self, distritos):
        for x in distritos:
            _locator = self.__locators.DISTRITO_TEMP.formatear_locator({"distrito": x})
            self.find_element(_locator).click()

    def guardar(self):
        self.find_element(self.__locators.GUARDAR_BTN).click()

    def se_guardo_correctamente(self):
        return self.find_element(self.__locators.ALERT_LBL).text
