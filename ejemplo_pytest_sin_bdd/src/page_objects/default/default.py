from src.factory.page.listado_paginas import Paginas
from src.page_objects.base.base_page import BasePage
from src.page_objects.default.properties.locators import DefaultLocators
from src.page_objects.page_elements.menu_roles import MenuRolesPageElement


class DefaultPage(BasePage):

    def __init__(self, driver, validar_pagina, *args):
        super().__init__(driver, validar_pagina)
        self.__locators = DefaultLocators
        self._menu_roles = MenuRolesPageElement(self)

    def menu_roles(self):
        self._menu_roles.abrir_menu()

    def rol_actual(self):
        return self._menu_roles.rol_actual()

    def roles(self):
        return self._menu_roles.roles()

    def cerrar_sesion(self):
        self._menu_roles.cerrar_sesion()
        self.next_page = Paginas.Login

    def codigo_operable(self):
        return self.get_element_text(self.__locators.LBL_CAJA)

    def configuracion(self):
        self.find_element(self.__locators.BTN_CONFIGURACION).click()
        self.next_page = Paginas.Configuracion

    def _validar_pantalla(self):
        raise NotImplementedError
