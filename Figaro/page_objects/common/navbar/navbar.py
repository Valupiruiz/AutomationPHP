from page_objects.base_page import BasePage
from page_objects.common.navbar.locators import NavbarLocators
from selenium.common.exceptions import TimeoutException
from dominio.ciclo_lectivo import CicloLectivo
from collections import namedtuple


InstitucionInfo = namedtuple("InstitucionInfo", ['institucion', 'nivel'])


class Navbar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = NavbarLocators()

    def verificar_sub_colegio(self, usuario):
        """
        Verifica que este en el sub-colegio que corresponde. Si ya esta en el que corresponde, no hago nada, y sino, lo
        cambio

        Args:
            usuario (Usuario): usuario de test actual

        Returns:
            (None)
        """
        self.find_element(self.__locators.USUARIO_ANC).click()
        if self.find_element(self.__locators.SUB_COLEGIO_USR_LBL).get_attribute("title") == usuario.get_sub_colegio_select():
            return
        self.find_select(self.__locators.SUB_COLEGIO_USR_SEL).select_by_visible_text(usuario.get_sub_colegio_select())

    def verificar_ciclo(self, ciclo: CicloLectivo):
        """
        Verifico que este en el ciclo lectivo que corresponde. Se hace el try porque puede pasar que ni siquiera haya
        select, entonces en ese caso catcheo el timeout y sigo, puesto que se asume que el unico ciclo lectivo es el
        correcto.

        Args:
            ciclo (str): texto que contiene el ciclo lectivo a seleccionar

        Returns:
            None
        """
        try:
            self.find_element(self.__locators.CICLO_SEL, 4)
            self.find_select(self.__locators.CICLO_SEL).select_by_visible_text(ciclo.nombre)
        except TimeoutException:
            pass

    def get_institucion_actual(self):
        """
        Devuelve la informacion del titulo del colegio que se visualiza en el navbar.

        Returns:
            (InstitucionInfo['institucion', 'nivel']) namedtuple
        """
        try:
            colegio = self.find_element(self.__locators.NOMBRE_LBL, 2).text.strip()
        except TimeoutException:
            colegio = ""
        return InstitucionInfo(colegio, self.find_element(self.__locators.NIVEL_LBL).text.strip())

    def desloguearse(self):
        self.find_element(self.__locators.USUARIO_ANC).click()
        self.find_element(self.__locators.CERRAR_SESION_LNK).click()
