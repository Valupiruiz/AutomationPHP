from src.factory.page.listado_paginas import Paginas
from src.page_objects.default.default import DefaultPage
from src.page_objects.page_elements.modales.abm_caja import ModalABMCajaPageElement
from src.page_objects.sucursales.properties.locators import EditarSucursalLocators


class EditarSucursalPage(DefaultPage, ModalABMCajaPageElement):

    def __init__(self, driver, validar_pantalla):
        self._locators = EditarSucursalLocators
        super().__init__(driver, validar_pantalla)
        self.wait_for_url("/branches/edit/")

    # region get

    def nombre_sucursal(self):
        return self.get_element_text(self._locators.Nombre)

    def provincia_sucursal(self):
        return self.get_element_text(self._locators.PROVINCIA_SELECCIONADA)

    def codigo_sucursal(self):
        return self.get_element_text(self._locators.Codigo)

    def ciudad_sucursal(self):
        return self.get_element_text(self._locators.ciudad)

    def direccion_sucursal(self):
        return self.get_element_text(self._locators.Direccion)

    def codigo_postal_sucursal(self):
        return self.get_element_text(self._locators.CodigoPostal)

    def codigo_area_sucursal(self):
        return self.get_element_text(self._locators.CodigoArea)

    def telefono_sucursal(self):
        return self.get_element_text(self._locators.Telefono)

    def email_sucursal(self):
        return self.get_element_text(self._locators.Email)

    def cajas_sucursal(self):
        cajas_sucursal = {}  # codigo: estado
        rows = self.find_elements(self._locators.ROWS_CAJA_SUCURSAL)
        for row in rows:
            codigo_caja = self.get_child_text(row, self._locators.LBL_CODIGO_CAJA)
            estado_caja = self.get_child_text(row, self._locators.LBL_ESTADO_CAJA)
            cajas_sucursal[codigo_caja] = estado_caja
        return cajas_sucursal

    def redireccionar_usuario(self):
        self.next_page = Paginas.Sucursal

    @property
    def _estados(self):
        return {
            "Activo": True,
            "Inactivo": False
        }

    # endregion

    def estado_caja(self, codigo_caja):
        rows = self.find_element(self._locators.ROWS_CAJA_SUCURSAL)
        row = rows.find_element(*self._locators.ROW_CAJA.format_locator(codigo_caja))
        return self._estados[self.get_child_text(row, self._locators.LBL_ESTADO_CAJA)]

    def guardar_sucursal(self):
        self.find_element(self._locators.Guardar).click()

    def _validar_pantalla(self):
        pass
