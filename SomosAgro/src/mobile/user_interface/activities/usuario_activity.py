from src.mobile.user_interface.mother_screen import MotherScreen
from src.mobile.user_interface.locators.usuario_locators import UsuarioLocators
from src.mobile.user_interface.activities.descripcion_activity import DescripcionActivity


class UsuarioActivity(MotherScreen):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = UsuarioLocators()

    def desloguearse(self):
        self.t_single_tap(self.__locators.ENGRANAJE_BTN)
        locator_configuracion = self.__locators.OPCION_CONFIGURACION.format_locator({"opc": "Cerrar sesión"})
        self.t_single_tap(locator_configuracion)

    def ir_publicaciones_vigentes(self):
        self.t_single_tap(self.__locators.PUBLICACIONES_VIGENTES)

    def seleccionar_publicacion(self):
        # TODO: queda la firma, por un futuro
        raise NotImplementedError("Pendiente de desarrollo")

    def seleccionar_opciones_publicacion(self):
        self.t_single_tap(self.__locators.OPCIONES_PUBLICACION_BURGER)

    def seleccionar_opcion(self, opcion):
        _locator = self.__locators.OPCION_CONFIGURACION.format_locator({"opc": opcion.capitalize()})
        self.t_single_tap(_locator)
        if opcion=='editar':
            return DescripcionActivity(self.driver)
        if opcion=='eliminar':
            return self

    def eliminar(self):
        self.t_single_tap(self.__locators.ELIMINAR_BTN)

