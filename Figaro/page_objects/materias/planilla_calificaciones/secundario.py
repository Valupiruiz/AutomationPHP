from page_objects.base_page import BasePage
from .locators import PlanillaLocators
from dominio.calificacion import Calificacion
from typing import List


class Calificaciones(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = PlanillaLocators()

    def buscar_evaluacion_alumno(self, calificacion):
        str_alumno = f"{calificacion.alumno.apellido}, {calificacion.alumno.nombre}"
        locator = self.__locators.CALIFICACION_TEMP.formatear_locator(
            {
                "alumno": str_alumno,
                "evaluacion": calificacion.evaluacion.nombre
            }
        )
        self.find_element(locator).click()
        self.find_element(self.__locators.TITULO_MODAL_LB)  # esto es para esperar que aparezca

    def calificar_evaluacion(self, calificacion: Calificacion):
        self.buscar_evaluacion_alumno(calificacion)
        self.find_element(self.__locators.NOTA_INP).clear()
        self.find_element(self.__locators.NOTA_INP).send_keys(str(calificacion.nota))
        self.find_element(self.__locators.TITULO_MODAL_LB).click()
        self.find_element(self.__locators.CERRAR_BTN).click()

    def calificar_evaluaciones(self, calificaciones: List[Calificacion]):
        for calificacion in calificaciones:
            self.calificar_evaluacion(calificacion)

    def obtengo_promedio_exacto(self, calificaciones: List[Calificacion], periodo: str):
        alumno = f"{calificaciones[0].alumno.apellido}, {calificaciones[0].alumno.nombre}"
        locator = self.__locators.PROMEDIO_TEMP.formatear_locator({"tipo": "Promedio Exacto",
                                                                           "alumno": alumno,
                                                                           "periodo": periodo})
        return self.find_element(locator).text

    def obtener_nota_boletin_periodo(self, calificaciones: List[Calificacion], periodo: str):
        alumno = f"{calificaciones[0].alumno.apellido}, {calificaciones[0].alumno.nombre}"
        locator = self.__locators.PROMEDIO_TEMP.formatear_locator({"tipo": "Nota Boletín Periodo",
                                                                           "alumno": alumno,
                                                                           "periodo": periodo})
        return self.find_element(locator).text

    def manejar_ausencia(self, calificacion):
        self.buscar_evaluacion_alumno(calificacion)
        if calificacion.ausente and not self.find_element(self.__locators.AUSENTE_CHK).is_selected():
            self.find_element(self.__locators.AUSENTE_CHK).click()
        elif not calificacion.ausente and self.find_element(self.__locators.AUSENTE_CHK).is_selected():
            self.find_element(self.__locators.AUSENTE_CHK).click()
            self.find_element(self.__locators.NOTA_INP).send_keys(str(calificacion.nota))
        self.find_element(self.__locators.CERRAR_BTN).click()
