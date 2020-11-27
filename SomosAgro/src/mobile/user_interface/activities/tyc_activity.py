from src.mobile.user_interface.locators.tyc_locators import TerminosCondicionesLocators
from src.mobile.user_interface.mother_screen import MotherScreen
from src.mobile.user_interface.activities import main_activity


class TerminosCondicionesActivity(MotherScreen):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = TerminosCondicionesLocators()

    def aceptar(self):
        self.aceptar_y_continuar()
        return main_activity.MainActivity(self.driver)
