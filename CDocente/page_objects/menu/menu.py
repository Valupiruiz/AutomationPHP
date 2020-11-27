from page_objects.base_page import BasePage
from .locators import MenuLocators
from utils.exceptions import Custom


class Menu(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = MenuLocators()

    def secuencial_click_menu(self, menues):
        if len(menues) > 3:
            raise Custom("No existen 4 submenus")
        for i in range(0, len(menues)):
            if i == 0 or i == len(menues)-1:
                _locator = self.__locators.MENU_TEMP.formatear_locator({"menu": menues[i].strip()})
                self.find_element(_locator).click()
            else:
                _locator = self.__locators.SUBMENU_TEMP.formatear_locator({"submenu": menues[i].strip()})
                self.move_to_element(_locator)


    def cierro_sesion(self, nombre, apellido):
        nombre_apellido = f'{nombre} {apellido}'
        _locator = self.__locators.CIERRE_SESION_NOMB_BTN.formatear_locator({"nombre_apellido": nombre_apellido})
        self.find_element(_locator).click()
        self.find_element(self.__locators.CIERRE_SESION_BTN).click()
        self.switch_to_alert_and_accept_it()
        self.find_element(self.__locators.LOGOUT_LBL).click()
