from abc import ABCMeta, abstractmethod
from page_objects.base_page import BasePage
from page_objects.materias.locators import MateriasLocators
from dominio.ciclo_lectivo import Curso
import sys
from page_objects.materias.evaluaciones import Evaluaciones


class IMaterias(metaclass=ABCMeta):
    @abstractmethod
    def seleccionar_materia(self, *args):
        pass


class MateriaSecundario(IMaterias, BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = MateriasLocators()

    def seleccionar_materia(self, curso: Curso):
        seleccionable = f"{curso.materias[0].nombre} - {curso.materias[0].opcion}"
        seleccionable = seleccionable + f" ({curso.nombre})" if curso.nombre != "" else seleccionable
        self.find_select(self.__locators.MATERIAS_SEL).select_by_visible_text(seleccionable)

    def dirigirse_solapa(self, solapa):
        locator = self.__locators.SOLAPA_BTN.formatear_locator({"solapa": solapa})
        self.find_element(locator).click()
        return solapa_mapper[solapa](self.driver)


class MateriaStrategy:
    @staticmethod
    def inicializar(strategy, driver):
        class_name = "Materia" + strategy.capitalize()
        return getattr(sys.modules[__name__], class_name)(driver)


solapa_mapper = {
    "Evaluaciones": Evaluaciones
}
