from src.mobile.user_interface.mother_screen import MotherScreen
from src.mobile.user_interface.locators.main_locators import MainLocators
from src.mobile.user_interface.activities.usuario_activity import UsuarioActivity
from src.mobile.user_interface.activities.nueva_publicacion_activity import NuevaPublicacionActivity
from collections import namedtuple


_Tab = namedtuple('_Tab', ['locator', 'screen'])


class MainActivity(MotherScreen):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = MainLocators()

    def empezar_bienvenida(self):
        self.t_single_tap(self.__locators.EMPEZAR)
        return self

    def ir_a_tab(self, nombre_tab):
        self.t_single_tap(_tab_matcher[nombre_tab].locator)
        return _tab_matcher[nombre_tab].screen(self.driver)


_tab_matcher = {
    "feed": _Tab(MainLocators.FEED_TAB, None),
    "busqueda": _Tab(MainLocators.BUSQUEDA_TAB, None),
    "nuevo_feed": _Tab(MainLocators.CREAR_FEED_TAB, NuevaPublicacionActivity),
    "usuario": _Tab(MainLocators.USUARIO_TAB, UsuarioActivity)
}
