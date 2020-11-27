from selenium.common.exceptions import TimeoutException

from src.page_objects.base.base_page import ActionChains
from src.page_objects.caja.properties.locators import GestionDeCajaLocators
from src.page_objects.default.default import DefaultPage
from src.page_objects.page_elements.modales.asignar_cajero import ModalAsignarCajeroPageElement
from src.page_objects.page_elements.modales.desbloquear_caja import ModalDesbloquearCajaPageElement


class GestionDeCajaPage(DefaultPage):

    def __init__(self, driver, validar_pagina):
        self._locators = GestionDeCajaLocators
        super().__init__(driver, validar_pagina)
        self._modal_desbloquear_caja = ModalDesbloquearCajaPageElement(self)
        self._modal_asignar_cajero = ModalAsignarCajeroPageElement(self)
        self.wait_for_url("/cajas/gestion-de-cajas")
        self.find_element(self._locators.TABLA)

    # region modal desbloquear caja
    def nuevo_desbloqueo(self, codigo_caja, nombre_oficina):
        self._get_row(codigo_caja).find_element(*self._locators.BTN_DESBLOQUEAR_CAJA).click()
        self._modal_desbloquear_caja.abrir_modal(codigo_caja, nombre_oficina)

    def detalle_bloqueo(self):
        return self._modal_desbloquear_caja.detalle_bloqueo()

    def diferencias_monto_bloqueo(self):
        return self._modal_desbloquear_caja.diferencias_montos()

    def desbloquear_caja(self, resolucion):
        self._modal_desbloquear_caja.set_observacion(resolucion)
        self._modal_desbloquear_caja.desbloquear_caja()
    # endregion

    # region modal asignar usuario
    def nueva_asignacion(self, codigo):
        self._get_row(codigo).find_element(*self._locators.BTN_ASIGNAR_USUARIO).click()
        self._modal_asignar_cajero.abrir_modal()

    def confirmar_desasignacion(self):
        self._modal_asignar_cajero.desasignar_cajero()
        self._modal_asignar_cajero.guardar()

    def confirmar_asignacion(self, cajero):
        self._modal_asignar_cajero.asignar_cajero(cajero)
        self._modal_asignar_cajero.guardar()

    def detalle_asignar_usuario(self):
        return self._modal_asignar_cajero.detalle()
    # endregion

    def buscar_caja(self, filtros):
        if codigo := filtros.get('Codigo', None):
            self.find_element(self._locators.TXT_CODIGO_CAJA).send_keys(codigo)
        if usuario := filtros.get('Usuario', None):
            self.find_element(self._locators.TXT_USUARIO).send_keys(usuario)
        if oficina := filtros.get('Oficina', None):
            self.select_option(self._locators.SELECT_OFICINA, oficina)

    def tabla_caja(self, codigo):
        row = self._get_row(codigo)
        return {
            "Codigo": self.get_child_text(row, self._locators.COLUMNA_CODIGO_CAJA),
            "Usuario": self.get_child_text(row, self._locators.COLUMNA_CAJERO_ASIGNADO),
            "Oficina": self.get_child_text(row, self._locators.COLUMNA_OFICINA),
            "Estado": self.get_child_text(row, self._locators.COLUMNA_ESTADO)
        }

    def _get_row(self, codigo):
        return self.find_element(self._locators.ROW.format_locator(codigo))

    def select_option(self, select, valor, gracias_fede=False):
        self.find_element(select).click()
        # e = self.find_element(self._locators.SELECT_LOADING)
        # self.wait_for_stale_element(e)
        if gracias_fede:
            ActionChains(self.driver).send_keys(valor.split(' ')[0]).perform()
        else:
            ActionChains(self.driver).send_keys(valor).perform()
        self.wait_for_element(self._locators.OPTION.format_locator(valor)).click()

        self.element_text_equals(self._locators.OPCION_SELECCIONADA.format_locator(select.ret_name), valor)

    def cerrar_modal(self):
        with self.stale_element(self._locators.FADE_OUT):
            self.find_element(self._locators.BTN_CERRAR_MODAL).click()

    def _validar_pantalla(self):
        pass
