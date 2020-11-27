from page_objects.base_page import BasePage
from .properties.locators import JudicialesLocators
from config.parameters import Parameters
from selenium.webdriver.common.keys import Keys
import time


class OrganismoJudicial(BasePage):
    def pagar_aviso(self):
        self.find_element(JudicialesLocators.juzgado_BTN).click()
        self.find_element(JudicialesLocators.jugzado_INP).send_keys(Parameters.get_organismo_judicial()['nombre_orga'])
        self.find_element(JudicialesLocators.jugzado_INP).send_keys(Keys.ENTER)
        self.find_element(JudicialesLocators.buscar_BTN).click()
        time.sleep(10)
        self.find_element(JudicialesLocators.pagar_BTN).click()
        self.find_element(JudicialesLocators.pagar_modal_BTN).click()
        time.sleep(5)

    def login(self):
        self.find_element(JudicialesLocators.usuario_INP).send_keys("jwadmin")
        self.find_element(JudicialesLocators.pass_INP).send_keys("1234")
        self.find_element(JudicialesLocators.ingresar_BTN).click()

    def pago_exitoso(self):
        return self.find_element(JudicialesLocators.mensaje_LBL).text
