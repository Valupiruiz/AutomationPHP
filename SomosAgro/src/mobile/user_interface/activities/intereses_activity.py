from src.mobile.user_interface.mother_screen import MotherScreen
from src.mobile.user_interface.locators.intereses_locators import InteresesLocators
from selenium.common.exceptions import TimeoutException
from typing import List
from src.domain.interes import Interes
from src.mobile.user_interface.activities.zonas_activity import ZonasActivity


class InteresesActivity(MotherScreen):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = InteresesLocators()

    def tocar_interes(self, nombre_interes: str):
        locator = self.__locators.INTERES_TEMP_VIEW.format_locator({"texto": nombre_interes})
        try:
            self.find_element(locator).click()
        except TimeoutException:
            self.scroll_until_element_appears(locator).click()

    def tocar_subinteres(self, nombre_subinteres: str):
        locator = self.__locators.INTERES_SUBCATEGORIA_TEMP.format_locator({"texto": nombre_subinteres})
        self.find_element(locator).click()

    def tocar_intereses_y_subintereses(self, intereses: List[Interes]):
        for interes in intereses:
            self.tocar_interes(interes.nombre)
            subintereses = interes.subintereses
            for subinteres in subintereses:
                self.tocar_subinteres(subinteres)
            self.find_element(self.__locators.ACEPTAR_BTN).click()

    def aceptar_subinteres(self):
        self.t_single_tap(self.__locators.ACEPTAR_BTN)

    def continuar(self):
        super().continuar()
        return ZonasActivity(self.driver)
    #
    # def deseleccionar_interes_elegido(self):
    #     self.t_single_tap(self.__locators.INTERES_SELECCIONADO)
