from page_objects.base_page import BasePage
from .properties.locators import LoginLocators
from page_objects.COMMON.Menu.Menu import Menu


class Login(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def iniciar_sesion(self, user, password):
        self.find_element(LoginLocators.usuario_INP).send_keys(user)
        self.find_element(LoginLocators.password_INP).send_keys(password)
        self.find_element(LoginLocators.ingreso_manual_BTN).click()
        return Menu(self.driver)
