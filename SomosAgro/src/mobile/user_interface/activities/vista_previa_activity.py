from src.mobile.user_interface.mother_screen import MotherScreen
from src.mobile.user_interface.locators.vista_previa_locators import VistaPreviaLocators


class VistaPreviaActivity(MotherScreen):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = VistaPreviaLocators()

    def get_vp_titulo(self):
        return self.find_element(self.__locators.TITULO_TXTVW).text

    def get_vp_usuario(self):
        return self.find_element(self.__locators.USUARIO_TXTVW).text

    def get_vp_etiqueta(self):
        return self.find_element(self.__locators.ETIQUETA_TXTVW).text

    def get_vp_zona(self):
        return self.find_element(self.__locators.ZONA_TXTVW).text

    def get_vp_sintesis(self):
        return self.find_element(self.__locators.SINTESIS_TXTVW).text

    def get_vp_descripcion(self):
        return self.find_element(self.__locators.DESCRIPCION_TXTVW, 1)

    def publicar(self, modo):
        _locator = self.__locators.PAGAR_BTN_TEMP.format_locator({"modo": modo})
        self.t_single_tap(_locator)
