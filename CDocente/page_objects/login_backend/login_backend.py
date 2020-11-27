from page_objects.base_page import BasePage
from .locators import LoginBackendLocators
from page_objects.login_google.login_google import LoginGoogle


class LoginBackend(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = LoginBackendLocators()

    def ingresar(self):
        self.find_element(self.__locators.INGRESAR_BUE).click()
        return LoginGoogle(self.driver)