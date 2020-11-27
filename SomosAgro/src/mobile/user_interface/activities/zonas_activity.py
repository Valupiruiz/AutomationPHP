from src.mobile.user_interface.mother_screen import MotherScreen
from src.mobile.user_interface.locators.zonas_locators import ZonasLocators
from src.mobile.user_interface.activities.tyc_activity import TerminosCondicionesActivity
from src.mobile.user_interface.activities.vista_previa_activity import VistaPreviaActivity


class ZonasActivity(MotherScreen):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = ZonasLocators()

    def tocar_zona(self, nombre_zona):
        locator = self.__locators.ZONA_VIEW_TEMP.format_locator({"texto": nombre_zona})
        self.find_element(locator).click()

    def tocar_zonas(self, zonas):
        for zona in zonas:
            self.tocar_zona(zona)

    def continuar_zonas(self):
        """
        Este continuar es para la pantalla de zonas cuando se crea o edita una publicación
        """
        super().continuar()
        return VistaPreviaActivity(self.driver)

    def continuar_zonas_login(self):
        """
        Este continuar se usa para cuando se seleccionan las zonas desde el login
        """
        self.continuar_zonas()
        return TerminosCondicionesActivity(self.driver)
