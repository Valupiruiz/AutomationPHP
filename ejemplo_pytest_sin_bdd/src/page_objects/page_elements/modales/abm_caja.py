from src.page_objects.base.base_page import BasePage
from src.page_objects.page_elements.modales.properties.locators import ModalABMCajaLocators
from src.page_objects.page_elements.properties.messages import ModalABMCajaMessages


class ModalABMCajaPageElement(BasePage):

    def __init__(self, driver, validar_pantalla):
        self.__locators = ModalABMCajaLocators
        super().__init__(driver, validar_pantalla)

    def nueva_caja(self):
        self.find_element(self.__locators.BTN_NUEVA_CAJA).click()
        self.find_element(self.__locators.FADE_OUT)
        self.element_text_equals(self.__locators.LBL_TITULO, "Nueva caja")

    def crear_nueva_caja(self, codigo):
        self.nueva_caja()
        self.find_element(self.__locators.TXT_CODIGO_CAJA).send_keys(codigo)
        self.guardar_caja()

    def guardar_caja(self):
        self.find_element(self.__locators.BTN_GUARDAR).click()

    def cerrar_modal(self):
        with self.stale_element(self.__locators.FADE_OUT):
            self.find_element(self.__locators.BTN_CERRAR).click()

    def abrir_edicion_caja(self, caja):
        self.find_element(self.__locators.BTN_EDITAR_CAJA.format_locator(caja.codigo)).click()
        self.find_element(self.__locators.FADE_OUT)
        self.find_element(self.__locators.MODAL)
        self.element_text_equals(self.__locators.LBL_TITULO, "Editar caja")

    def estado_giros(self):
        return {
            "Envia": self.wait_for_element(self.__locators.CHK_ENVIA_GIROS).is_selected(),
            "Recibe": self.wait_for_element(self.__locators.CHK_RECIBE_GIROS).is_selected()
        }

    def estado_monedas_giros(self):
        # todo: sacar el [-3:] y hacer algo mas lindo,
        #  deberia solo levantar el estado del badge y buscar el codigo de la moneda en el span o similar
        monedas_disponibles_envio = self.wait_for_elements(self.__locators.MONEDAS_DISPONIBLES_ENVIO)
        monedas_disponibles_recibo = self.wait_for_elements(self.__locators.MONEDAS_DISPONIBLES_RECIBO)

        return {  # codigo: estado
            "Envia": {moneda.get_attribute("id")[-3:]: moneda.is_selected() for moneda in monedas_disponibles_envio},
            "Recibe": {moneda.get_attribute("id")[-3:]: moneda.is_selected() for moneda in monedas_disponibles_recibo}
        }

    def estado_toggle_caja(self):
        return self.find_element(self.__locators.ESTADO_CAJA).is_selected()

    def modificar_estado_caja(self, estado_esperado: bool):
        self.wait.until(lambda _: self.find_element(self.__locators.ESTADO_CAJA).is_selected() == (not estado_esperado))
        self.find_element(self.__locators.CHK_ESTADO_CAJA).click()
        self.wait.until(lambda _: self.find_element(self.__locators.ESTADO_CAJA).is_selected() == estado_esperado)

    def modificar_estado_giro(self, tipo_giro, estado_esperado):
        locators = {
            "Envia": self.__locators.CHK_ENVIA_GIROS,
            "Recibe": self.__locators.CHK_RECIBE_GIROS
        }
        locator = locators[tipo_giro]
        self.wait_for_element(locator).click()
        self.wait_for_check_status(locator, checked=estado_esperado)

    def modificar_moneda_giro(self, tipo_giro, codigo_moneda, estado_esperado):
        locators = {
            "Envia": self.__locators.CHK_ENVIA_GIROS_MONEDA,
            "Recibe": self.__locators.CHK_RECIBE_GIROS_MONEDA
        }

        locator = locators[tipo_giro].format_locator(codigo_moneda)

        self.wait_for_check_status(locator, checked=not estado_esperado)
        self.wait_for_element(locator).click()
        # cuando haces clic en el badge, hay un tooltip que no se oculta :shrug:
        self.find_element(self.__locators.LBL_TITULO).click()
        self.wait_for_check_status(locator, checked=estado_esperado)

    def _validar_pantalla(self):
        self.nueva_caja()
        with self.stale_element(self.__locators.FADE_OUT):
            self.find_element(self.__locators.BTN_GUARDAR).click()
            self.element_text_equals(self.__locators.ERROR_CODIGO_CAJA, ModalABMCajaMessages.CODIGO_CAJA_OBLIGATORIO)
            self.find_element(self.__locators.TXT_CODIGO_CAJA).send_keys('jklsdgjklsjkldg')
            self.find_element(self.__locators.BTN_GUARDAR).click()
            self.element_text_equals(self.__locators.ERROR_CODIGO_CAJA, ModalABMCajaMessages.CODIGO_CAJA_INVALIDO)
            self.find_element(self.__locators.BTN_CERRAR).click()
