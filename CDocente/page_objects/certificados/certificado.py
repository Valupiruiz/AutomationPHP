from page_objects.base_page import BasePage
from .locators import CertificadoLocator
from utils.file_utils import FileUtils
import time
from selenium.common.exceptions import TimeoutException



class Certificado(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = CertificadoLocator()

    def completar_info_basica(self, img, fecha):
        time.sleep(5)
        self.driver.execute_script(
            '$("#fecha_certificado").val("'+fecha+'")')
        time.sleep(5)
        self.find_element(self.__locators.AGREGAR_IMG_BTN).click()
        FileUtils.seleccionar_img_gui(img)
        self.find_element(self.__locators.TERMIN_CONDIC_INP).click()
        self.find_element(self.__locators.ACEPTAR_BTN).click()
        try:
            self.find_element(self.__locators.ACEPTAR_ADV_BTN).click()
        except TimeoutException:
            pass

