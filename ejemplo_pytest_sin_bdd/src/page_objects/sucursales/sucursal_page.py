from src.factory.page.listado_paginas import Paginas
from src.page_objects.base.base_page import ActionChains
from src.page_objects.default.default import DefaultPage
from src.page_objects.sucursales.properties.locators import SucursalLocators


class SucursalPage(DefaultPage):

    def __init__(self, driver, validar_pantalla):
        self._locators = SucursalLocators
        super().__init__(driver, validar_pantalla)
        self.wait_for_url("/branches")

    def nueva_sucursal(self):
        self.find_element(self._locators.Agregar).click()
        self.next_page = Paginas.AgregarSucursal

    def _buscar(self, val, locator):
        # Hay un bug medio falopa que si escribis muy rapido no muestra los resultados
        # como claramente es imposible reproducirlo a mano no se va a corregir asique
        # escribo hasta la ultima letra, hago un pause y escribo la ultima letra
        ac = ActionChains(self.driver)
        ac.send_keys_to_element(self.find_element(locator), val[:-1])
        ac.pause(1).send_keys(val[-1])
        ac.perform()
        self.element_text_equals(locator, val)

    def clear_filters(self):
        self.clear_elements_text(self._locators.NombreSucursal, self._locators.CodigoSucursal)

    def buscar_sucursal_por_nombre(self, nombre_sucursal):
        self._buscar(nombre_sucursal, self._locators.NombreSucursal)

    def buscar_sucursal_por_codigo(self, codigo_sucursal):
        self._buscar(codigo_sucursal, self._locators.CodigoSucursal)

    def ir_edicion_sucursal(self, nombre_compuesto):
        elem = self._get_row_sucursal(nombre_compuesto)
        elem.find_element(*self._locators.EditarSucursal).click()
        self.next_page = Paginas.EditarSucursal
    #fixme
    def validar_cajas_activas_sucursal(self, sucursal):
        elem = self._get_row_sucursal(sucursal.nombre_compuesto())
        # esto es FEO
        self.child_element_text_equals(elem, self._locators.CAJAS_ACTIVAS_SUCURSAL,
                                       f"Caja{len(sucursal.cajas_activas())} Cajas")

    def cambiar_estado_sucursal(self, sucursal):
        elem = self._get_row_sucursal(sucursal.nombre_compuesto())
        elem.find_element(*self._locators.CambiarEstadoSucursal).click()
        if not sucursal.activa:
            self.element_text_equals(self._locators.LBL_MENSAJE_CAMBIAR_ESTADO_SUCURSAL,
                                     f"¿Desea desactivar la sucursal {sucursal.nombre}?")
        else:
            self.element_text_equals(self._locators.LBL_MENSAJE_CAMBIAR_ESTADO_SUCURSAL,
                                     f"¿Desea activar la sucursal {sucursal.nombre}?")
        self.find_element(self._locators.BTN_ACEPTAR_CAMBIO_ESTADO).click()

    def validar_estado_sucursal(self, nombre_compuesto, estado):
        elem = self._get_row_sucursal(nombre_compuesto)
        if estado:
            elem.find_element(*self._locators.caja_activa)
        else:
            elem.find_element(*self._locators.caja_inactiva)

    def cerrar_modal(self):
        with self.stale_element(self._locators.FADE_OUT):
            self.find_element(self._locators.BTN_CERRAR_MODAL).click()

    def _get_row_sucursal(self, nombre_compuesto):
        """
        Retorna la fila (tr) de de la sucursal indicada
        :param nombre_compuesto: Nombre compuesto de la sucursal (#codigo - nombre)
        :rtype: WebElement
        """
        return self.find_element(self._locators.FilaSucursal.format_locator(nombre_compuesto))

    def _validar_pantalla(self):
        pass
