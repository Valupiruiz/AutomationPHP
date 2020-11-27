from selenium.common.exceptions import TimeoutException

from src.dominio.operaciones import TiposOperacion
from src.page_objects.base.base_page import BasePage
from src.page_objects.page_elements.modales.properties.locators import ModalConfirmarMontosLocators
from src.page_objects.page_elements.properties.messages import CajaMessages
from src.utils.others import format_number


# todo: con el nuevo diseño, puede que tenga mas responsabilidades de las que deberia
class ModalConfirmarMontosPageElement:

    def __init__(self, parent, tipo_operacion, tipo_operable):
        self.parent: BasePage = parent
        self._tipo_operacion = tipo_operacion
        self._tipo_operable = tipo_operable
        self._locators = ModalConfirmarMontosLocators

    def confirmar_accion(self, caja, montos):
        self.__validar_accion(caja.codigo)
        # todo: pasar esto al dominio algun dia
        self.parent.find_element(self._locators.TXT_OBSERVACIONES).send_keys("Observaciones de prueba")
        self.parent.find_element(self._locators.TXT_PASSWORD).send_keys(caja.password)
        self.parent.element_text_equals(self._locators.TXT_PASSWORD, caja.password)
        self.__validar_montos(montos)
        l_boton = self.__botones_por_accion()
        self.parent.element_text_equals(l_boton, self.__leyenda_boton_por_accion())
        self.parent.find_element(l_boton).click()
        try:
            self.parent.find_element(self._locators.TOAST, 5)
            txt = self.parent.get_element_text(self._locators.TOAST)
            print("Hubo un error al confirmar la accion", txt)
        except TimeoutException:
            pass

    def cerrar(self):
        with self.parent.stale_element(self._locators.FADE_OUT):
            self.parent.find_element(self._locators.BTN_CERRAR_MODAL).click()

    def __validar_montos(self, montos):
        for moneda, monto in montos.items():
            self.parent.element_text_equals(self._locators.LBL_CODIGO_MONTO.format_locator(moneda.codigo),
                                            moneda.codigo)
            self.parent.element_text_equals(self._locators.LBL_MONTO.format_locator(moneda.codigo),
                                            str(format_number(monto, ".2f")))

    def __validar_accion(self, codigo_caja):
        titulo = self.__titulos_por_accion() + f"\n{self._tipo_operable} {codigo_caja}"
        self.parent.element_text_equals(self._locators.LBL_TITULO_MODAL, titulo)
        self.parent.element_text_equals(self._locators.LBL_DESCRIPCION, self.__descripciones_por_accion())

    def __botones_por_accion(self):
        return {
            TiposOperacion.CierreTotal: self._locators.BTN_CONFIRMAR_CIERRE_TOTAL,
            TiposOperacion.CierreParcial: self._locators.BTN_CONFIRMAR_CIERRE_PARCIAL,
            TiposOperacion.Apertura: self._locators.BTN_CONFIRMAR_APERTURA
        }[self._tipo_operacion]

    def __titulos_por_accion(self):
        return {
            TiposOperacion.CierreTotal: f"Cierre total de {self._tipo_operable.lower()}",
            TiposOperacion.CierreParcial: f"Cierre parcial de {self._tipo_operable.lower()}",
            TiposOperacion.Apertura: "Confirmación de apertura"
        }[self._tipo_operacion]

    def __leyenda_boton_por_accion(self):
        return {
            TiposOperacion.CierreTotal: "Cierre total",
            TiposOperacion.CierreParcial: "Cierre parcial",
            TiposOperacion.Apertura: "Aperturar"
        }[self._tipo_operacion]

    def __descripciones_por_accion(self):
        return {
            TiposOperacion.Apertura: f"¿Está seguro que desea aperturar la {self._tipo_operable.lower()} "
            f"con los siguientes montos?",
            TiposOperacion.CierreParcial: f"¿Está seguro que desea hacer el cierre parcial de "
            f"la {self._tipo_operable.lower()} con los siguientes montos?",
            TiposOperacion.CierreTotal: f"¿Está seguro que desea hacer el cierre total de "
            f"la {self._tipo_operable.lower()} con los siguientes montos?"
        }[self._tipo_operacion]

    def validar_pantalla(self):
        self.parent.find_element(self._locators.FADE_OUT)
        self.parent.find_element(self._locators.BTN_CONFIRMAR_APERTURA).click()
        self.parent.element_text_equals(self._locators.ERROR_PASSWORD, CajaMessages.CAMPO_OBLIGATORIO)
        self.parent.find_element(self._locators.TXT_PASSWORD).send_keys('PassPrueba')
        self.parent.element_text_equals(self._locators.TXT_PASSWORD, "PassPrueba")
        self.parent.find_element(self._locators.BTN_CONFIRMAR_APERTURA).click()
        self.parent.get_toast()
        self.parent.dismiss_toast()
        self.parent.find_element(self._locators.BTN_CERRAR_MODAL).click()
