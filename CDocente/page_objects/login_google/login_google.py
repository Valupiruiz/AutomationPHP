from page_objects.base_page import BasePage
from page_objects.login_google.locators import LoginGoogleLocators
from page_objects.pagina_principal import pagina_principal
from selenium.common.exceptions import TimeoutException
import time



class LoginGoogle(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = LoginGoogleLocators()

    def loguearse(self, usuario):
        try:
            self.find_element(self.__locators.EMAIL_INP).send_keys(usuario.mail)
        except TimeoutException:
            self.find_element(self.__locators.USAR_OTRA_CUENTA_DIV).click()
            self.find_element(self.__locators.EMAIL_INP).send_keys(usuario.mail)
        self.move_to_element(self.__locators.SIGUIENTE_BTN)
        self.find_element(self.__locators.SIGUIENTE_BTN, 40).click()
        self.find_element(self.__locators.PASS_INP).send_keys(usuario.contrasenia)
        self.find_element(self.__locators.SIGUIENTE_BTN).click()

    def ir_a_pag_anterior(self):
        self.find_element(self.__locators.PAGINA_ANTERIOR_LNK).click()

    def realizar_proceso_de_logueo(self, usuario):
        self.loguearse(usuario)
        try:
            self.element_has_text(self.__locators.SIST_LBL, "Sistema de Clasificación Docente", 2)
        except TimeoutException:
            self.ir_a_pag_anterior()
        return pagina_principal.PaginaPrincipal(self.driver)

    def elegir_cuenta(self, usuario):
        _locator = self.__locators.CUENTA_DIV.formatear_locator({"mail": usuario.mail})
        self.find_element(_locator).click()
        self.find_element(self.__locators.PASS_INP).send_keys(usuario.contrasenia)
        self.find_element(self.__locators.SIGUIENTE_BTN).click()
        return
