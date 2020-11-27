from src.mobile.user_interface.mother_screen import MotherScreen
from src.mobile.user_interface.locators.registro_info_locators import RegistroInfoLocators
from src.domain.usuario import Usuario
from src.mobile.user_interface.activities.intereses_activity import InteresesActivity


class RegistroInfoActivity(MotherScreen):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = RegistroInfoLocators()

    def __completar_usuario(self, username):
        self.find_element(self.__locators.USUARIO_EDITTEXT).send_keys(username)

    def __completar_nombre_empresa(self, nombre):
        self.find_element(self.__locators.NOMBRE_EMPRESA_EDITTEXT).send_keys(nombre)

    def __completar_email(self, mail):
        self.find_element(self.__locators.EMAIL_EDITTEXT).send_keys(mail)

    def __completar_telefono(self, telefono):
        self.find_element(self.__locators.TELEFONO_EDITTEXT).send_keys(telefono)

    def completar_datos_registro_y_continuar(self, usuario: Usuario):
        self.__completar_usuario(usuario.usuario)
        self.__completar_nombre_empresa(usuario.nombre_empresa)
        self.__completar_email(usuario.email)
        self.__completar_telefono(usuario.telefono)
        super().continuar()
        return InteresesActivity(self.driver)
