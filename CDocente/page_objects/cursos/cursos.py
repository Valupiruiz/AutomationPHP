from page_objects.base_page import BasePage
from .locators import CursosLocators
from utils.file_utils import FileUtils


class Curso(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = CursosLocators()

    def abrir_buscador(self):
        self.find_element(self.__locators.ABRIR_BUSCADOR_BTN).click()

    def buscar(self, curso):
        self.find_element(self.__locators.CURSO_INP).send_keys(curso)
        self.find_element(self.__locators.BUSCAR_BTN).click()

    def agregar_curso(self, curso):
        _locator = self.__locators.AGREGAR_CURSO_TEMP_BTN.formatear_locator({"curso": curso})
        self.find_element(_locator).click()

    def curso_agregado_correctamente(self):
        return self.find_element(self.__locators.ALERT_LBL).text


