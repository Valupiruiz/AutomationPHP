from page_objects.CREAR_AVISO.properties.locators import NuevoAvisoLocators
from page_objects.base_page import BasePage
from config.parameters import Parameters
from config.data.utils import Utils
import time
import pyperclip
import pyautogui

utils = Utils()


class NuevoAviso(BasePage):
    def __init__(self, driver, parametros):
        super().__init__(driver)
        self.__parametros = parametros

    def crear_aviso_acta(self):
        self.find_select(NuevoAvisoLocators.seccion_SEL).select_by_value(self.__parametros['seccion'])
        self.find_element(NuevoAvisoLocators.opcion_default_OPT)
        self.find_select(NuevoAvisoLocators.rubro_SEL).select_by_visible_text(self.__parametros['rubro'])
        self.find_element(NuevoAvisoLocators.tipo_aviso_SEL).send_keys(self.__parametros['tipoAviso'])
        self.find_element(NuevoAvisoLocators.modalidad_pago_SEL).send_keys(self.__parametros['formaPago'])
        self.find_element(NuevoAvisoLocators.cant_dias_INP).clear()
        self.find_element(NuevoAvisoLocators.cant_dias_INP).send_keys(self.__parametros['diasPublicar'])
        self.find_element(NuevoAvisoLocators.fecha_publicacion_INP).send_keys(self.__parametros['dia'])
        self.find_element(NuevoAvisoLocators.texto_CLICK).click()
        self.find_element(NuevoAvisoLocators.texto_CLICK).send_keys(utils.generate_paragraph())
        self.find_select(NuevoAvisoLocators.origen_SEL).select_by_visible_text(self.__parametros['origen'])
        self.find_element(NuevoAvisoLocators.opcion_default_orga_OPT)
        self.wait_for_css_class_to_disappear(NuevoAvisoLocators.organismo_CONTAINER, 'state-loading')
        self.find_select(NuevoAvisoLocators.organismo_SEL).select_by_visible_text(self.__parametros['orga'])
        self.find_element(NuevoAvisoLocators.fecha_admin_INP)
        self.find_element(NuevoAvisoLocators.fecha_admin_INP).send_keys(self.__parametros["fechaFirma"])

    def archivo(self):
        javascript = "document.getElementById('AvisoType_documentoAviso').click();"
        self.driver.execute_script(javascript)
        data = self.__parametros["archivo"]
        time.sleep(1)
        pyperclip.copy(data)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

    def correcto(self):
        self.find_element(NuevoAvisoLocators.guardar_BTN).click()
        return self.find_element(NuevoAvisoLocators.mensaje_MSJ).text
