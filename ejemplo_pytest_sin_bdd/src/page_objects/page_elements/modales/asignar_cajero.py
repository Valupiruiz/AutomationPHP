from src.page_objects.base.base_page import BasePage
from src.page_objects.page_elements.modales.properties.locators import ModalAsignarCajeroLocators


class ModalAsignarCajeroPageElement:

    def __init__(self, parent):
        self.parent: BasePage = parent
        self._locators = ModalAsignarCajeroLocators

    def abrir_modal(self):
        self.parent.element_text_equals(self._locators.LBL_TITULO_MODAL, "Asignación de usuario")
        self.parent.element_text_equals(self._locators.LBL_INFO,
                                        "Solo podrá asignar cajeros que no estén asignados a otra caja")

    def desasignar_cajero(self):
        self.parent.find_element(self._locators.BTN_DESASIGNAR_USUARIO).click()
        self.parent.element_text_equals(self._locators.LBL_USUARIO_ASIGNADO, "Sin asignacion")

    def asignar_cajero(self, cajero):
        option_cajero = f"{cajero.nombre} {cajero.apellido} - {cajero.dni}"
        self.parent.select_option(self._locators.SELECT_USUARIO, option_cajero, gracias_fede=True)
        self.parent.element_text_equals(self._locators.LBL_USUARIO_ASIGNADO, option_cajero)

    def detalle(self):
        return {
            "Codigo": self.parent.get_element_text(self._locators.LBL_CODIGO_CAJA),
            "Oficina": self.parent.get_element_text(self._locators.LBL_OFICINA),
            "Usuario": self.parent.get_element_text(self._locators.LBL_USUARIO_ASIGNADO)
        }

    def guardar(self):
        self.parent.find_element(self._locators.BTN_GUARDAR_ASIGNACION).click()
