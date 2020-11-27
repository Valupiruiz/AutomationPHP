from src.mobile.user_interface.mother_screen import MotherScreen
from src.mobile.user_interface.locators.login_locators import LoginStrategies


class LoginActivity(MotherScreen):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = LoginStrategies()

    def ingresar_con_facebook(self):
        self.find_element(self.__locators.FACEBOOK_LOGIN_TEXTVIEW).click()

    def ingresar_con_google(self):
        self.find_element(self.__locators.GOOGLE_LOGIN_TEXTVIEW).click()
