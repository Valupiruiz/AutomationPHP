from page_objects.base_page import BasePage
from page_objects.common.login.locators import LoginLocators
from dominio.usuario import Usuario


class Login(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = LoginLocators()

    def loguearse(self, usuario: Usuario):
        self.find_element(self.__locators.INGRESAR_BTN).click()
        self.find_select(self.__locators.INSTITUCION_SEL).select_by_visible_text(usuario.institucion.nombre)
        self.find_element(self.__locators.USUARIO_INP).send_keys(usuario.username)
        self.find_element(self.__locators.PASS_INP).send_keys(usuario.password)
        self.find_element(self.__locators.INGRESAR_SUBMIT_BTN).click()
