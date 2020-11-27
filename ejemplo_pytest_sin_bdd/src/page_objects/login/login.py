import allure
from selenium.common.exceptions import TimeoutException

from src.dominio.usuario import TiposUsuario
from src.factory.page.listado_paginas import Paginas
from src.page_objects.base.base_page import BasePage
from src.page_objects.login.properties.locators import LoginLocators
from src.page_objects.login.properties.messages import LoginMessages


class Login(BasePage):

    def __init__(self, driver, validar_pantalla):
        self._locators = LoginLocators
        self._messages = LoginMessages
        super().__init__(driver, validar_pantalla)
        self.wait_for_url("/login")

    def validar_correo_login(self, dni, email, contra):
        self._completar_credenciales_login(dni, email, contra)
        self.click_login()

    def iniciar_sesion(self, usuario):
        self._completar_credenciales_login(usuario.dni, usuario.mail, usuario.password)
        self.click_login()

    def validar_usuario_sin_sesion(self):
        self.find_element(self._locators.Dni)
        self.find_element(self._locators.Mail)
        self.find_element(self._locators.Pass)

    def redirigir(self, pagina_indicada):
        # Se me hace que estoy complicandome al hacer un diccionario en vez de directamente pasarle la pagina
        # pero tambien se me hace que la accion solo deberia indicar el contexto de la redireccion
        # en lugar de decirle a que pagina redireccionar,
        # lo que genera cierto "control" sobre a que pagina se puede redireccionar
        pagina = {
            "Apertura Caja": Paginas.AperturaCaja,
            "Apertura Boveda": Paginas.AperturaBoveda,
            "Dashboard": Paginas.Dashboard,
            "Caja no asociada": Paginas.CajaNoAsociada,
            "Boveda no asociada": Paginas.BovedaNoAsociada,
            "Gestion de caja": Paginas.GestionDeCaja
        }.get(pagina_indicada, None)
        if pagina is None:
            raise Exception("No se encontro la pagina indicada", pagina_indicada)

        try:
            self.next_page = pagina
        except TimeoutException as e:
            raise Exception("No se pudo redirigir a la pagina indicada", pagina_indicada, e)

    def _completar_credenciales_login(self, dni, email, contra):
        self.find_element(self._locators.Dni).send_keys(dni)
        self.find_element(self._locators.Mail).send_keys(email)
        self.find_element(self._locators.Pass).send_keys(contra)
        self.element_text_equals(self._locators.Pass, contra)

    def click_login(self):
        # self._check_captcha()
        self.find_element(self._locators.Enviar).click()

    def validar_campos_obligatorios(self):
        self.element_text_equals(self._locators.MensajeDNIObligatorio, self._messages.DNIObligatorio)
        self.element_text_equals(self._locators.MensajeMailObligatorio, self._messages.MailObligatorio)
        self.element_text_equals(self._locators.MensajePassObligatorio, self._messages.PassObligatorio)

    def validar_correo_olvido(self, email):
        self.find_element(self._locators.Link).click()
        self.find_element(self._locators.Correo).send_keys(email)
        self.find_element(self._locators.BotonEnviar).click()

    def _check_captcha(self):
        f = self.find_element(self._locators.FRAME)
        self.driver.switch_to.frame(f)
        self.find_element(self._locators.CheckCaptcha).click()
        self.wait_for_element(self._locators.TildeCaptcha)
        self.driver.switch_to.default_content()

    def _validar_pantalla(self):
        pass
