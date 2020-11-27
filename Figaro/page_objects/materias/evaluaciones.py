from page_objects.base_page import BasePage
from page_objects.materias.locators import EvaluacionLocators
from dominio.evaluacion import Evaluacion, Ponderacion
from typing import List
from utils.date_utils import DatePicker, DateUtils
from utils.string_utils import StringUtils
from page_objects.materias.planilla_calificaciones.secundario import Calificaciones
from utils.math_utils import calcular_promedio_exacto


class Evaluaciones(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = EvaluacionLocators()
        self.wait_for_element_invisibility(self.__locators.MANZANA_CARGANDO)
        self._calificaciones = Calificaciones(self.driver)

    def nueva_evaluacion(self):
        self.find_element(self.__locators.NUEVA_EV_BTN).click()

    def nueva_evaluacion_aks(self,tipo):
        self.find_element(self.__locators.NUEVA_EV_BTN).click()
        self.find_select(self.__locators.TIPO_EVALUACION_SEL).select_by_visible_text(tipo)

    def crear_todas_las_evaluaciones(self, evaluaciones: List[Evaluacion], apodo):
        for evaluacion in evaluaciones:
            func = "nueva_evaluacion_" + apodo
            try:
                metodo = getattr(self, func)
                metodo(evaluacion.tipo)
            except AttributeError:
                self.nueva_evaluacion()
            self.find_element(self.__locators.MODAL_EVALUACION)
            fecha_descompuesta = StringUtils.descomponer_fecha_en_atomos(evaluacion.fecha)
            dtp = DatePicker(self.driver)
            self.find_element(self.__locators.FECHA_EV_INP).click()
            dtp.seleccionar_fecha(DateUtils.set_date(*fecha_descompuesta).fecha)
            self.find_element(self.__locators.NOMBRE_EV_INP).send_keys(evaluacion.nombre)
            if evaluacion.ponderacion == Ponderacion.MANUAL:
                self.find_element(self.__locators.PONDERACION_AUTO_BTN).click()
                self.find_element(self.__locators.VALORACION_PONDERACION_TXT).clear()
                self.find_element(self.__locators.VALORACION_PONDERACION_TXT).send_keys(evaluacion.porcentaje)
            self.find_element(self.__locators.GUARDAR_EV_BTN).click()
            self.wait_for_element_invisibility(self.__locators.MODAL_EVALUACION, 60)
            self.wait_for_element_invisibility(self.__locators.CARGANDO_LISTADO_EVALUACIONES)

    def planilla_evaluaciones(self):
        self.find_element(self.__locators.PLANILLA_EVALUACIONES_BTN).click()
        self.find_element(self.__locators.PANTALLA_EVALUACIONES).click()
        return self

    def calificar_evaluaciones(self, calificaciones):
        self._calificaciones.calificar_evaluaciones(calificaciones)

    def calificar_evaluacion(self, calificacion):
        self._calificaciones.calificar_evaluacion(calificacion)

    def obtengo_promedio_exacto(self, calificaciones, periodo):
        return self._calificaciones.obtengo_promedio_exacto(calificaciones, periodo)

    def obtener_nota_boletin_periodo(self, calificaciones, periodo):
        return self._calificaciones.obtener_nota_boletin_periodo(calificaciones, periodo)

    def manejar_ausencia(self, calificacion):
        self._calificaciones.manejar_ausencia(calificacion)

    def cerrar_modal_planilla(self):
        self.find_element(self.__locators.CERRAR_VENTANA_PLANILLA_BTN).click()




