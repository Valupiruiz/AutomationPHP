from page_objects.base_page import BasePage
from .locators import PrincipalDocenteLocators
from page_objects.menu.menu import Menu


class PrincipalDocente(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = PrincipalDocenteLocators()
        self._menu = Menu(driver)

    def me_dirijo(self, menues):
        self._menu.secuencial_click_menu(menues)

    def inscripcion_periodo(self):
        self.find_element(self.__locators.PERIODO_INSCR_BTN).click()




