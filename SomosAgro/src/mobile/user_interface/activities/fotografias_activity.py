from src.mobile.user_interface.mother_screen import MotherScreen
from src.mobile.user_interface.locators.fotografias_locators import FotografiasLocators
from src.mobile.user_interface.activities.intereses_activity import InteresesActivity


class FotografiasActivity(MotherScreen):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = FotografiasLocators()

    def seleccionar_foto(self):
        self.t_single_tap(self.__locators.IMAGEN_TEST_IMVW)
        self.t_single_tap(self.__locators.CROP_EDITAR_TXVW)

    def continuar(self):
        super().continuar()
        return InteresesActivity(self.driver)
