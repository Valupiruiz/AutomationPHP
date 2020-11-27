from src.page_objects.base.base_page import BasePage
from src.page_objects.page_elements.properties.locators import DetalleOperacionLocators


class DetalleOperacionPageElement:

    def __init__(self, parent):
        self.__locators = DetalleOperacionLocators
        self.parent: BasePage = parent

    def get_transferencia_entrante(self):
        return {
            "Titulo": self.parent.get_element_text(self.__locators.LBL_TITULO),
            "Medio": self.parent.get_element_text(self.__locators.LBL_MEDIO),
            "Origen": self.parent.get_element_text(self.__locators.LBL_ORIGEN),
            "Observacion": self.parent.get_element_text(self.__locators.LBL_OBSERVACION)
        }

    def get_transferencia_saliente(self):
        return {
            "Titulo": self.parent.get_element_text(self.__locators.LBL_TITULO),
            "Medio": self.parent.get_element_text(self.__locators.LBL_MEDIO),
            "Destino": self.parent.get_element_text(self.__locators.LBL_DESTINO),
            "Montos": self.montos_moneda(),
            "Observacion": self.parent.get_element_text(self.__locators.LBL_OBSERVACION)
        }

    def get_cancelacion(self):
        return {
            "Titulo": self.parent.get_element_text(self.__locators.LBL_TITULO),
            "Info Text": self.parent.get_element_text(self.__locators.LBL_INFO_P),
            "Destino": self.parent.get_element_text(self.__locators.LBL_DESTINO),
            "Medio": self.parent.get_element_text(self.__locators.LBL_MEDIO),
            "Montos": self.montos_moneda(),
            "Observacion": self.parent.get_element_text(self.__locators.LBL_OBSERVACION)
        }

    def get_solicitud(self):
        return {
            "Titulo": self.parent.get_element_text(self.__locators.LBL_TITULO),
            # "Info Text": self.parent.get_element_text(self.__locators.LBL_INFO_P),
            "Montos": self.montos_moneda(),
            "Observacion": self.parent.get_element_text(self.__locators.LBL_OBSERVACION)
        }

    def montos_moneda(self):
        monedas = self.parent.get_elements_text(self.__locators.LBL_MONEDAS)
        montos = {}  # codigo: monto
        for moneda in monedas:
            montos[moneda] = self.parent.get_element_text(self.__locators.LBL_MONTO.format_locator(moneda))
        return montos
