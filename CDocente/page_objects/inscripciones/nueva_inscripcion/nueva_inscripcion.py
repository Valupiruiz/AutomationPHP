from page_objects.base_page import BasePage
from .locators import NuevaInscripcionLocators


class NuevaInscripcion(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = NuevaInscripcionLocators()

    def nueva_inscripcion(self):
        self.find_element(self.__locators.AGREGAR_BTN).click()

    def buscar_inscripcion(self, area, cargo, asignatura, especialidad):
        self.find_select(self.__locators.AREA_SEL).select_by_visible_text(area)
        self.find_select(self.__locators.CARGO_SEL).select_by_visible_text(cargo)
        self.find_select(self.__locators.ASIGNATURA_SEL).select_by_visible_text(asignatura)
        self.find_select(self.__locators.ESPECIALIDAD_SEL).select_by_visible_text(especialidad)
        self.find_element(self.__locators.AGREGAR_BTN).click()
        self.find_element(self.__locators.AGREGAR_MODAL_BTN).click()

    def inscripcion_correcta(self):
        self.wait_for_element_invisibility(self.__locators.MODAL_CIERRE)
        return self.find_element(self.__locators.MENSAJE_SPAN).text



