from src.dominio.operaciones import TiposOperacion
from src.page_objects.base.base_page import BasePage
from src.page_objects.page_elements.properties.locators import IngresarMontosLocators
from src.page_objects.page_elements.properties.messages import CajaMessages

class IngresarMontosPageElement:

    def __init__(self, parent, tipo_operacion, tipo_operable):
        self.parent: BasePage = parent
        self._locators = IngresarMontosLocators
        self._tipo_operacion = tipo_operacion
        self._tipo_operable = tipo_operable

    def completar_montos_accion(self, codigo_caja, montos):
        self.__validar_accion(codigo_caja)
        for moneda, monto in montos.items():
            self.parent.find_element(self._locators.TXT_MONTO.format_locator(moneda.codigo)).send_keys(str(monto))
            self.parent.element_text_equals(self._locators.TXT_MONTO.format_locator(moneda.codigo),
                                            str(monto).replace(".", ","))
        self.parent.find_element(self._confirmaciones_por_accion()).click()

    def monedas_operables(self):
        monedas = self.parent.find_elements(self._locators.TXT_MONTOS)
        return [moneda.get_attribute('id')[-3:] for moneda in monedas]

    def __validar_accion(self, codigo_caja):
        self.parent.element_text_equals(self._locators.LBL_TITULO,
                                        self._titulos_por_accion().format(codigo_caja))
        self.parent.element_text_equals(self._locators.LBL_DESCRIPCION,
                                        self._descripciones_por_accion().format(codigo_caja))

    def _confirmaciones_por_accion(self):
        return {
            TiposOperacion.Apertura: self._locators.BTN_APERTURAR,
            TiposOperacion.CierreParcial: self._locators.BTN_CERRAR_PARCIALMENTE,
            TiposOperacion.CierreTotal: self._locators.BTN_CERRAR_TOTALMENTE
        }[self._tipo_operacion]

    def _titulos_por_accion(self):
        return {
            TiposOperacion.Apertura: f"Apertura de {self._tipo_operable.lower()} {{0}}",
            TiposOperacion.CierreParcial: f"Cierre parcial de {self._tipo_operable.lower()}",
            TiposOperacion.CierreTotal: f"Cierre total de {self._tipo_operable.lower()}"
        }[self._tipo_operacion]

    def _descripciones_por_accion(self):
        return {
            TiposOperacion.Apertura: f"Ingrese los montos con los que apertura esta {self._tipo_operable.lower()}.",
            TiposOperacion.CierreParcial: f"Ingrese los montos con los que cierra parcialmente "
            f"esta {self._tipo_operable.lower()}.",
            TiposOperacion.CierreTotal: f"Ingrese los montos con los que cierra totalmente "
            f"esta {self._tipo_operable.lower()}."
        }[self._tipo_operacion]

    def validar_pantalla(self):
        self.parent.find_element(self._locators.BTN_APERTURAR).click()
        montos = self.parent.find_elements(self._locators.DIV_MONTOS)
        for monto in montos:
            self.parent.child_element_text_equals(monto, self._locators.ERROR_MONTO, CajaMessages.MONTO_INVALIDO)
