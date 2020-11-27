from page_objects.base_page import BasePage
from .locators import PrincipalBackendLocators
from page_objects.menu.menu import Menu


class PrincipalBackend(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = PrincipalBackendLocators()
        self._menu = Menu(driver)

    def me_dirijo(self, menues):
        self._menu.secuencial_click_menu(menues)

    def me_encuentro_en_pag_backend(self):
        self.element_has_text(self.__locators.SIST_LBL, "Sistema de Clasificación Docente", 2)