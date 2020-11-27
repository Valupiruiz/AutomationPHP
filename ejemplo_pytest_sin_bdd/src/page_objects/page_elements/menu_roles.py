from selenium.common.exceptions import TimeoutException

from src.page_objects.base.base_page import BasePage
from src.page_objects.page_elements.properties.locators import MenuRolesLocators


# esto deberia hacer mas cosas pero por el momento esta bien asi

class MenuRolesPageElement:

    def __init__(self, parent):
        self.parent: BasePage = parent
        self.__locators = MenuRolesLocators

    def abrir_menu(self):
        self.parent.find_element(self.__locators.BTN_MENU).click()
        self.parent.element_text_equals(self.__locators.LBL_TRABAJANDO_CON, "Trabajando con")

    def rol_actual(self):
        return self.parent.get_element_text(self.__locators.LBL_ROL_ACTUAL)

    def roles(self):
        try:
            return self.parent.get_elements_text(self.__locators.LBLS_ROL)
        except TimeoutException:  # Si no aparece la lista de roles, solo tiene el actual
            return self.rol_actual()

    def cerrar_sesion(self):
        self.parent.find_element(self.__locators.LISTA)
        self.parent.element_text_equals(self.__locators.BTN_CERRAR, "Cerrar sesión")
        self.parent.find_element(self.__locators.BTN_CERRAR).click()