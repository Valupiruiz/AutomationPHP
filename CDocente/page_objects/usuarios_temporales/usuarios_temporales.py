from page_objects.base_page import BasePage
from .locators import UsuariosTemporalesLocator


class UsuariosTemporales(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = UsuariosTemporalesLocator()

    def cambiar_mail(self, mail_temporario, mail_definitivo):
        self.find_element(self.__locators.MAIL_FILTRO_INP).send_keys(mail_temporario)
        self.find_element(self.__locators.BUSCAR_BTN).click()
        _locator = self.__locators.EDITAR_USU_TEMP.formatear_locator({"mail": mail_temporario})
        self.find_element(_locator).click()
        self.find_element(self.__locators.MAIL_INP).send_keys(mail_definitivo)
        self.find_element(self.__locators.MAIL_REPEAT_INP).send_keys(mail_definitivo)
        self.find_element(self.__locators.GUARDAR_BTN).click()


    def habilitar_usuario(self, mail_definitivo):
        self.find_element(self.__locators.MAIL_FILTRO_INP).send_keys(mail_definitivo)
        self.find_element(self.__locators.BUSCAR_BTN).click()
        _locator = self.__locators.HABILITAR_USU_TEMP.formatear_locator({"mail": mail_definitivo})
        self.find_element(_locator).click()
        self.find_element(self.__locators.ACEPTAR_BTN).click()

    def cambio_correcto(self):
        return self.find_element(self.__locators.ALERT_LBL).text


