from page_objects.base_page import BasePage
from .locators import UsuarioBueLocators
from utils.string_utils import StringUtils
import time

utils = StringUtils()


class UsuariosBue(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = UsuarioBueLocators()

    def cambio_correcto(self):
        return self.find_element(self.__locators.ALERT_LBL).text

    def cambio_mail_definitivo(self, mail_definitivo):
        self.find_element(self.__locators.BUSC_MAIL_INP).send_keys(mail_definitivo)
        self.find_element(self.__locators.BUSCAR_BTN).click()
        _locator = self.__locators.EDITAR_USU_TEMP.formatear_locator({"mail": mail_definitivo})
        self.find_element(_locator).click()
        self.find_element(self.__locators.MAIL_EDU_INP).clear()
        self.find_element(self.__locators.MAIL_EDU_INP).send_keys(str(utils.generate_word())+'@bue.edu.ar')
        self.find_element(self.__locators.DNI_INP).clear()
        self.find_element(self.__locators.DNI_INP).send_keys(str(utils.generate_num(8)))
        self.driver.execute_script(f'$("#{self.__locators.DNI_INP.ret_name}").blur()')

    def guardar(self):
        self.find_element(self.__locators.GUARDAR_BTN).click()
