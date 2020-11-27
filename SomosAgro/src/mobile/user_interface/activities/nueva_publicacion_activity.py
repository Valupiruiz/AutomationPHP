from src.mobile.user_interface.mother_screen import MotherScreen
from src.mobile.user_interface.locators.nueva_publicacion_locators import NuevaPublicacionLocators
from src.mobile.user_interface.activities.caracteristicas_publicacion_activity import CaracteristicasPublicacionActivity


class NuevaPublicacionActivity(MotherScreen):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = NuevaPublicacionLocators()

    def seleccionar_tipo_publicacion(self, tipo):
        _locator = self.__locators.SELECCIONAR_TIPO_TEMP.format_locator({"texto": tipo})
        self.t_single_tap(_locator)
        return CaracteristicasPublicacionActivity(self.driver)
