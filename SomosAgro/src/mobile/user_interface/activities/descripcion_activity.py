from src.mobile.user_interface.mother_screen import MotherScreen
from src.mobile.user_interface.locators.descripcion_locators import DescripcionLocators
from src.mobile.user_interface.activities.fotografias_activity import FotografiasActivity
from src.mobile.user_interface.activities.intereses_activity import InteresesActivity
from src.domain.publicacion import TipoPublicacion


class DescripcionActivity(MotherScreen):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = DescripcionLocators()

    def completar_campos(self, publicacion):
        self.find_element(self.__locators.TITULO_ETXT).send_keys(publicacion.cabecera.titulo)
        self.find_element(self.__locators.SINTESIS_ETXT).send_keys(publicacion.cabecera.sintesis)
        if publicacion.tipo == TipoPublicacion.PREMIUM:
            self.find_element(self.__locators.DESCRIPCION_ETXT).send_keys(publicacion.cabecera.descripcion)

    def editar_campos(self, publicacion):
        self.find_element(self.__locators.TITULO_ETXT).clear()
        self.find_element(self.__locators.SINTESIS_ETXT).clear()
        if publicacion.tipo == TipoPublicacion.PREMIUM:
            self.find_element(self.__locators.DESCRIPCION_ETXT).clear()
        self.completar_campos(publicacion)

    def continuar_editar(self):
        """
        Este continuar se usa para cuando se está editando la publicación
        """
        super().continuar()
        return InteresesActivity(self.driver)

    def continuar(self):
        """
        Este continuar se usa para cuando se está creando una publicación
        """
        super().continuar()
        return FotografiasActivity(self.driver)
