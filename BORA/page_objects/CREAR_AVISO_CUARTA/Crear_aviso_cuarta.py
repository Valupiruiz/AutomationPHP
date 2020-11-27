from page_objects.CREAR_AVISO_CUARTA.properties.locators import CuartaLocators
from page_objects.base_page import BasePage
from config.data.utils import Utils
import time

utils = Utils()


class NuevoAvisoCuarta(BasePage):
    def crear_aviso_cuarta(self):
        for i in range(1, 1700):
            self.find_element(CuartaLocators.id_dominio_INP).send_keys(1584871 + i)
            self.find_element(CuartaLocators.dominio_INP).send_keys(1584871 + i)
            self.find_element(CuartaLocators.nro_doc_INP).send_keys("12345678")
            self.find_select(CuartaLocators.tipo_documento_SEL).select_by_value("DNI")
            self.find_select(CuartaLocators.rubro_SEL).select_by_value("6")
            self.find_select(CuartaLocators.tipo_op_SEL).select_by_value("6")
            self.find_element(CuartaLocators.titular_INP).send_keys("TESTcomar")
            self.find_element(CuartaLocators.qr_INP).send_keys("Test1.com.ar")
            self.find_element(CuartaLocators.guardar_BTN).click()
            time.sleep(1)
