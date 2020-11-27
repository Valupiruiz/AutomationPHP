from page_objects.base_page import BasePage
from .locators import BuscadorDocentesLocators


class BuscadorDocente(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = BuscadorDocentesLocators()

    def buscar_por_mail(self, mail):
        self.find_element(self.__locators.EMAIL_INP).send_keys(mail)
        self.find_element(self.__locators.BUSCAR_BTN).click()
        _locator = self.__locators.VALIDAR_TEMP_BTN.formatear_locator({"mail": mail})
        self.find_element(_locator).click()

