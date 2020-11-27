from page_objects.base_page import BasePage
from .locators import DatosPersonalesLocators
from page_objects.menu.menu import Menu
from utils.file_utils import FileUtils


class DatosPersonales(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = DatosPersonalesLocators()
        self._menu = Menu(driver)

    def guardar(self):
        self.find_element(self.__locators.GUARDAR_BTN).click()
        self.find_element(self.__locators.TERM_CHECK).click()
        self.find_element(self.__locators.ACEPTO_BTN).click()
        self.switch_to_alert_and_accept_it()

    def se_guardo_correctamente(self):
        return self.find_element(self.__locators.ALERT_SPAN).text

    def me_dirijo(self, menues):
        self._menu.secuencial_click_menu(menues)

    def cargar_info_faltante(self, docente):
        self.find_element(self.__locators.AGREGAR_IMAGEN_DNI_BTN).click()
        FileUtils.seleccionar_img_gui(docente.imagenes_dni[0])
        self.find_element(self.__locators.RECIBE_JUB_FALSE).click()
        self.find_element(self.__locators.CELULAR_INP).send_keys(docente.celular)
