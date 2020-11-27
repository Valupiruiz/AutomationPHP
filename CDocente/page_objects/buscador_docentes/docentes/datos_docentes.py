from page_objects.base_page import BasePage
from .locators import DatosDocentesLocators


class DatosDocentes(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = DatosDocentesLocators()

    def ir_a_solapa(self, solapa):
        _locator = self.__locators.SOLAPA_TEMP_BTN.formatear_locator({"solapa": solapa})
        self.find_element(_locator).click()

    def aprobar_titulo(self, titulo):
        _locator = self.__locators.ACCORDION_BTN.formatear_locator({"Listado": 'Títulos'})
        self.find_element(_locator).click()
        _locator = self.__locators.FLECHA_VALID_TITULO_BTN.formatear_locator({"titulo": titulo})
        self.find_element(_locator).click()
        self.find_element(self.__locators.APROBAR_TITULO_BTN).click()
        self.find_element(self.__locators.TITULO_TRAMITE_FALSE).click()
        self.find_element(self.__locators.ACEPTAR_TITULO_BTN).click()
        self.wait_for_element_invisibility(self.__locators.MODAL_APROBACION_TITULO_)

    def estado_titulo(self, titulo):
        self.find_element(self.__locators.CARGA_ESTADO_LBL)
        _locator = self.__locators.ESTADO_TITULO_TEMP.formatear_locator({"titulo": titulo})
        return self.find_element(_locator).text



