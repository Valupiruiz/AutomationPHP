from src.mobile.user_interface.mother_screen import MotherScreen
from src.mobile.user_interface.locators.caracteristicas_publicacion_locators import CaracteristicasPublicacionLocators
from src.mobile.user_interface.activities.descripcion_activity import DescripcionActivity


class CaracteristicasPublicacionActivity(MotherScreen):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = CaracteristicasPublicacionLocators()

    def seleccionar_dias(self, dias):
        _locator = self.__locators.CANTIDAD_DIAS_TEMP.format_locator({"cant_dias": str(dias)})
        self.t_single_tap(_locator)

    def get_precio(self):
        return int(self.find_element(self.__locators.PRECIO_PUBLICACION_VW).text.replace("$", ""))

    def continuar(self):
        super().continuar()
        return DescripcionActivity(self.driver)
