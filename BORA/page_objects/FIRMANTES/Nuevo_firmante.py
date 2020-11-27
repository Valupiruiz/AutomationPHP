from page_objects.base_page import BasePage
from page_objects.FIRMANTES.properties.locators import LocatorsFirmantes
import time
from generated_data.data_manager import DataManager


class NuevoFirmante(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def nuevo_firmante(self):
        time.sleep(2)
        self.find_element(LocatorsFirmantes.nuevo_BTN).click()
        self.find_element(LocatorsFirmantes.nombre_INP).send_keys(DataManager.get_firmante())
        self.find_element(LocatorsFirmantes.codigo_INP).send_keys(DataManager.get_firmante())
        self.find_element(LocatorsFirmantes.guardar_BTN).click()

    def correcta_creacion_firmante(self):
        return self.find_element(LocatorsFirmantes.mensaje_MSJ).text
