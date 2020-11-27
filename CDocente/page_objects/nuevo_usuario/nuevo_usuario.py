from page_objects.base_page import BasePage
from .locators import NuevoUsuarioLocators
import time


class NuevoUsuario(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = NuevoUsuarioLocators()

    def completar_datos_personales(self, docente):
        self.find_element(self.__locators.NOMBRE_INP).send_keys(docente.nombre)
        self.find_element(self.__locators.APELLIDO_INP).send_keys(docente.apellido)
        self.driver.execute_script(
            '$("#docente_fecha_nacimiento").val("' + docente.fecha_nacimiento + '")')
        self.find_select(self.__locators.SEXO_SEL).select_by_visible_text(docente.sexo)
        self.find_select(self.__locators.T_DOCUMENTO_SEL).select_by_visible_text(docente.tipo_dni)
        self.find_element(self.__locators.NRO_DOCUMENTO_INP).send_keys(docente.nro_dni)
        self.find_element(self.__locators.NRO_DOCUMENTO_AGAIN_INP).send_keys(docente.nro_dni)
        self.find_element(self.__locators.CUIL_INP).send_keys(docente.cuil)

    def completar_direccion_personal(self, docente):
        self.find_select(self.__locators.PROVINCIA_SEL).select_by_visible_text(docente.provincia)
        self.wait_until_element_interactable(self.__locators.LOCALIDAD_SEL)
        self.find_select(self.__locators.LOCALIDAD_SEL).select_by_visible_text(docente.localidad)
        self.find_element(self.__locators.CALLE_NRO_INP).send_keys(docente.calle)
        self.wait_for_text_in_element_value(self.__locators.CALLE_NRO_INP, docente.calle)
        self.find_element(self.__locators.COD_POSTAL_INP).send_keys(docente.cod_postal)

    def completar_email_contra(self, docente):
        self.find_element(self.__locators.MAIL_INP).send_keys(docente.mail_temportal)
        self.wait_for_text_in_element_value(self.__locators.MAIL_INP, docente.mail_temportal)
        self.find_element(self.__locators.MAIL_AGAIN_INP).send_keys(docente.mail_temportal)
        self.wait_for_text_in_element_value(self.__locators.MAIL_AGAIN_INP, docente.mail_temportal)
        self.find_element(self.__locators.PASS_INP).send_keys(docente.contrasenia_temporal)
        self.find_element(self.__locators.PASS_AGAIN_INP).send_keys(docente.contrasenia_temporal)

    def guardar(self):
        self.find_element(self.__locators.TERM_CONDIC_CHECK).click()
        self.find_element(self.__locators.REGISTRARSE_BTN).click()

    def creacion_correcta(self):
        return self.find_element(self.__locators.ALERT_SPAN).text