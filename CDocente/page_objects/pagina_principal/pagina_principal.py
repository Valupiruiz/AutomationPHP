from page_objects.base_page import BasePage
from page_objects.pagina_principal.locators import PaginaPrincipalLocators
from page_objects.login_google.login_google import LoginGoogle


class PaginaPrincipal(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = PaginaPrincipalLocators()

    def loguearse_con_cuentabue(self):
        self.find_element(self.__locators.CUENTAS_BUE_BTN).click()
        return LoginGoogle(self.driver)

    def nuevo_usuario(self):
        self.find_element(self.__locators.NUEVO_USURIO_BTN).click()
