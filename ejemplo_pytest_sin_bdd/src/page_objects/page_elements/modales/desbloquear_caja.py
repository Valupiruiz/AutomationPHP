from src.page_objects.base.base_page import BasePage
from src.page_objects.page_elements.modales.properties.locators import ModalDesbloquearCajaLocators


class ModalDesbloquearCajaPageElement:

    def __init__(self, parent):
        self.parent: BasePage = parent
        self._locators = ModalDesbloquearCajaLocators

    def abrir_modal(self, codigo_caja, nombre_oficina):
        self.parent.element_text_equals(self._locators.LBL_TITULO,
                                        f"Desbloquear caja\nCaja {codigo_caja} - {nombre_oficina}")

    def detalle_bloqueo(self):
        return {
            "Usuario": self.parent.get_element_text(self._locators.LBL_USUARIO),
            "Fecha": self.parent.get_element_text(self._locators.LBL_FECHA),
            "Situacion": self.parent.get_element_text(self._locators.LBL_SITUACION)
        }

    def diferencias_montos(self):
        template = {
            "Logicos": self._locators.LBLS_LOGICO,
            "Reales": self._locators.LBLS_REALES,
            "Diferencias": self._locators.LBLS_DIFERENCIA
        }
        diferencias = {
            "Logicos": {},
            "Reales": {},
            "Diferencias": {},
        }
        for tipo, locator in template.items():
            diffs = [txt.split(" ") for txt in self.parent.get_elements_text(locator)]
            for monto, moneda in diffs:
                if "+" in monto:
                    monto.replace("+", "")
                diferencias[tipo][moneda] = monto
        return diferencias

    def set_observacion(self, observacion):
        self.parent.find_element(self._locators.TXT_OBSERVACION).send_keys(observacion)

    def desbloquear_caja(self):
        self.parent.find_element(self._locators.BTN_DESBLOQUEAR_CAJA).click()
