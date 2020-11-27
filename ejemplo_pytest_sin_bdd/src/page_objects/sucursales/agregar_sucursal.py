from src.factory.page.listado_paginas import Paginas
from src.page_objects.base.base_page import ActionChains
from src.page_objects.default.default import DefaultPage
from src.page_objects.sucursales.properties.locators import AgregarSucursalLocators
from src.page_objects.sucursales.properties.messages import AgregarSucursalMessages


class AgregarSucursal(DefaultPage):

    def __init__(self, driver, validar_pantalla):
        self._locators = AgregarSucursalLocators
        super().__init__(driver, validar_pantalla)
        self.wait_for_url("/branches/new")

    # region get

    def nombre_sucursal(self):
        return self.get_element_text(self._locators.Nombre)

    def codigo_sucursal(self):
        return self.get_element_text(self._locators.Codigo)

    def provincia_sucursal(self):
        return self.get_element_text(self._locators.PROVINCIA_SELECCIONADA)

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

    # endregion

    def agregar_sucursal(self, sucursal):
        self.find_element(self._locators.Nombre).send_keys(sucursal.nombre)
        self.find_element(self._locators.Codigo).send_keys(sucursal.codigo)
        self._completar_select_provincia(sucursal.provincia.nombre)
        self.find_element(self._locators.ciudad).send_keys(sucursal.ciudad)
        self.find_element(self._locators.Direccion).send_keys(sucursal.direccion)
        self.find_element(self._locators.CodigoPostal).send_keys(sucursal.codigo_postal)
        self.find_element(self._locators.CodigoArea).send_keys(sucursal.codigo_area)
        self.find_element(self._locators.Telefono).send_keys(sucursal.telefono)
        self.find_element(self._locators.Email).send_keys(sucursal.mail)

    def _completar_select_provincia(self, provincia):
        self.find_element(self._locators.select_provincia).click()
        ac = ActionChains(self.driver)
        ac.send_keys(provincia[:-1])
        ac.pause(1).send_keys(provincia[-1])
        ac.perform()
        self.find_element(self._locators.OPTION.format_locator(provincia)).click()
        self.element_has_text(self._locators.PROVINCIA_SELECCIONADA, provincia)

    def modificar_nombre_sucursal(self, nuevo_nombre):
        self.clear_elements_text(self._locators.Nombre)
        self.find_element(self._locators.Nombre).send_keys(nuevo_nombre)

    def guardar_sucursal(self):
        self.find_element(self._locators.Guardar).click()

    def cajas_sucursal(self):  # en esta instancia, la sucursal no puede tener cajas
        return {}

    def redireccionar_usuario(self):
        self.next_page = Paginas.Sucursal

    def _validar_pantalla(self):
        self.find_element(self._locators.Nombre)
        self.find_element(self._locators.Guardar).click()
        self.element_text_equals(self._locators.ERROR_NOMBRE, AgregarSucursalMessages.NOMBRE_OBLIGATORIO)
        self.element_text_equals(self._locators.ERROR_CODIGO, AgregarSucursalMessages.CODIGO_OBLIGATORIO)
        self.element_text_equals(self._locators.ERROR_PROVINCIA, AgregarSucursalMessages.PROVINCIA_OBLIGATORIA)
        self.element_text_equals(self._locators.ERROR_CIUDAD, AgregarSucursalMessages.CIUDAD_OBLIGATORIA)
        self.element_text_equals(self._locators.ERROR_DIRECCION, AgregarSucursalMessages.DIRECCION_OBLIGATORIA)
        self.element_text_equals(self._locators.ERROR_CODIGO_POSTAL, AgregarSucursalMessages.CODIGO_POSTAL_OBLIGATORIO)
        self.element_text_equals(self._locators.ERROR_CODIGO_AREA, AgregarSucursalMessages.CODIGO_AREA_OBLIGATORIO)
        self.element_text_equals(self._locators.ERROR_TELEFONO, AgregarSucursalMessages.TELEFONO_OBLIGATORIO)
        self.element_text_equals(self._locators.ERROR_MAIL, AgregarSucursalMessages.MAIL_OBLIGATORIO)
        self.find_element(self._locators.Codigo).send_keys("ola")
        self.find_element(self._locators.Email).send_keys("ola")
        self.find_element(self._locators.Guardar).click()
        self.element_text_equals(self._locators.ERROR_CODIGO, AgregarSucursalMessages.CODIGO_INVALIDO)

        self.element_text_equals(self._locators.ERROR_MAIL, AgregarSucursalMessages.MAIL_INVALIDO)
        self.driver.execute_script('window.scrollTo(0,0)')
        self.clear_elements_text(self._locators.Codigo, self._locators.Email)
