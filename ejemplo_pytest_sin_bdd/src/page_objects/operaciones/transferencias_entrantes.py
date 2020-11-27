from selenium.common.exceptions import TimeoutException

from src.page_objects.operaciones.properties.locators import TransferenciasEntrantesLocators
from src.page_objects.operaciones.properties.messages import TransferenciasMessages
from src.page_objects.page_elements.detalle_operacion import DetalleOperacionPageElement
from src.page_objects.page_elements.nav_bar import NavBarPageElement
from src.page_objects.page_elements.paginado import PaginadoPageElement
from src.utils.others import today


# fixme and TransferenciasSalientes
class TransferenciasEntrantesPage(NavBarPageElement):

    def __init__(self, driver, validar_paginas):
        self._validar_pagina = validar_paginas
        self._locators = TransferenciasEntrantesLocators
        self._messages = TransferenciasMessages
        super().__init__(driver, validar_paginas)
        self.wait_for_url("/operaciones/transferencias-entrantes")
        self._detalle_operaciones = DetalleOperacionPageElement(self)
        self._paginado = PaginadoPageElement(self)

    # region Transferencias

    def recepcionar_deposito(self, codigo_operacion):
        with self.stale_element(e=self._get_row_grilla(codigo_operacion)) as e:
            e.find_element(*self._locators.BTN_RECEPCIONAR_DEPOSITO).click()

    def nueva_confirmacion(self, codigo):
        self._get_row_grilla(codigo).find_element(*self._locators.BTN_CONFIRMAR_DEPOSITO).click()
        self.find_element(self._locators.FADE_OUT)

    def confirmar_deposito(self, montos, password):
        self.find_element(self._locators.FADE_OUT)
        for moneda, monto in montos.items():
            self.find_element(self._locators.TXT_MONEDA.format_locator(moneda.codigo)).send_keys(monto)
        self.find_element(self._locators.TXT_PASSWORD).send_keys(password)
        self.find_element(self._locators.BTN_CONFIRMAR_DEPOSITO_MODAL).click()

    def nuevo_reporte_problema(self, codigo):
        self._get_row_grilla(codigo).find_element(*self._locators.BTN_HUBO_UN_PROBLEMA).click()
        self.find_element(self._locators.FADE_OUT)
        self.find_element(self._locators.LBL_TITULO_MODAL)
        self.element_text_equals(self._locators.LBL_TITULO_MODAL,
                                 f"Reporte de problema\n{codigo} - {today()}")
        self.element_text_equals(self._locators.LBL_INFO_P,
                                 "Por favor indique el problema por el cuál no puede confirmar el depósito")

    def confirmar_reporte_problema(self, observacion, password):
        self.find_element(self._locators.TXT_OBSERVACIONES).send_keys(observacion)
        self.find_element(self._locators.TXT_PASSWORD).send_keys(password)
        self.find_element(self._locators.BTN_REPORTAR_PROBLEMA).click()

    def tabla_transferencia_entrante(self, codigo_operacion):
        row = self._get_row_grilla(codigo_operacion)
        obtenido = {
            "Origen": self.get_child_text(row, self._locators.LBL_ORIGEN),
            "Medio": self.get_child_text(row, self._locators.LBL_MEDIO),
            "Fecha": self.get_child_text(row, self._locators.LBL_FECHA),
            "Estado": self.get_child_text(row, self._locators.LBL_ESTADO_TRANSFERENCIA)
        }
        if 'boveda' in self.driver.current_url:
            obtenido["Montos"] = self._montos_row(row)
        return obtenido

    def detalle_transferencia_entrante(self, codigo):
        return self._get_detalle(codigo, "Transferencia")

    def transferencia_stale(self, codigo, refresh):
        if refresh:
            with self.stale_element(self._locators.CONTAINER):
                self.driver.refresh()

        if 'caja' in self.driver.current_url:
            self.pill_depositos_en_curso()
        try:
            self._get_row_grilla(codigo, 10)
        except TimeoutException:
            pass
        else:
            raise TimeoutException(
                "Esperaba que la transferencia desapareciera de la lista de transferencias en curso")

    def pill_depositos_en_curso(self):
        self.find_element(self._locators.PILL_DEPOSITOS).click()

    # endregion

    # region Solicitud Fondos

    def monedas_modal_entrante(self):
        return [moneda.get_attribute('id')[-3:] for moneda in self.find_elements(self._locators.TXTS_MONEDA)]

    def tabla_solicitud_fondos(self, codigo):
        row = self._get_row_grilla(codigo)
        return {
            "Fecha": self.get_child_text(row, self._locators.LBL_FECHA),
            "Montos": self._montos_row(row),
            "Estado": self.get_child_text(row, self._locators.LBL_ESTADO_SOLICITUD)
        }

    def detalle_solicitud_fondos(self, codigo):
        return self._get_detalle(codigo, "Solicitud")

    def solicitud_stale(self, codigo, refresh):
        if refresh:
            with self.stale_element(self._locators.CONTAINER):
                self.driver.refresh()
        self.pill_solicitud_fondos()
        try:
            self._get_row_grilla(codigo, 10)
        except TimeoutException:
            pass
        else:
            raise TimeoutException(
                "Esperaba que la solicitud desapareciera de la lista de solicitudes en curso")

    def generar_solicitud(self, montos, observacion, password):
        for moneda, monto in montos.items():
            locator = self._locators.TXT_MONEDA.format_locator(moneda.codigo)
            self.find_element(locator).send_keys(str(monto))
            self.element_has_text(locator, str(monto))
        if observacion:
            self.find_element(self._locators.TXT_OBSERVACIONES).send_keys(str(observacion))
        self.find_element(self._locators.TXT_PASSWORD).send_keys(password)
        self.find_element(self._locators.BTN_CONFIRMAR_SOLICITUD).click()

    def pill_solicitud_fondos(self):
        self.find_element(self._locators.PILL_SOLICITUD_FONDOS).click()

    def nueva_solicitud(self):
        self.find_element(self._locators.BTN_NUEVA_SOLICITUD).click()
        self.find_element(self._locators.FADE_OUT)
        self.element_text_equals(self._locators.LBL_TITULO_MODAL, "Nueva solicitud de depósito")
        self.element_text_equals(self._locators.LBL_INFO_TEXT, "Ingrese los montos de su solicitud.")

    def nueva_cancelacion_solicitud(self, codigo):
        self._get_row_grilla(codigo).find_element(*self._locators.BTN_CANCELAR_SOLICITUD).click()
        self.find_element(self._locators.FADE_OUT)
        self.element_text_equals(self._locators.LBL_TITULO_MODAL,
                                 f"Cancelar solicitud\n{codigo} - {today()}")
        self.element_text_equals(self._locators.LBL_INFO_P, "¿Está seguro que desea cancelar esta solicitud?:")

    def detalle_cancelacion_solicitud(self):
        return {
            "Montos": self._detalle_operaciones.montos_moneda(),
            "Observacion": self.get_element_text(self._locators.LBL_OBSERVACION)
        }

    def confirmar_cancelacion_solicitud_fondos(self, password):
        self.find_element(self._locators.LBL_TITULO_MODAL)
        self.find_element(self._locators.TXT_PASSWORD).send_keys(password)
        self.find_element(self._locators.BTN_CANCELAR_SOLICITUD_MODAL).click()

    # endregion

    # region Common

    def cerrar_modal(self):
        with self.stale_element(self._locators.FADE_OUT):
            self.find_element(self._locators.BTN_CERRAR_MODAL).click()

    def _get_row_grilla(self, codigo_operacion, timeout=5):
        cant_resultados = self._cant_resultados_grilla()
        if cant_resultados == 10:
            return self._paginado.search(
                lambda: self.find_element(self._locators.ROW_CODIGO.format_locator(codigo_operacion), timeout))
        return self.find_element(self._locators.ROW_CODIGO.format_locator(codigo_operacion), timeout)

    # fixme
    def _cant_resultados_grilla(self):
        try:
            return len(self.wait_for_elements(self._locators.RESULTADOS_GRILLA, 10))
        except TimeoutException:
            return 0

    def _get_detalle(self, codigo, tipo_detalle):
        detalle = {
            "Solicitud": self._detalle_operaciones.get_solicitud,
            "Transferencia": self._detalle_operaciones.get_transferencia_entrante
        }[tipo_detalle]
        self._get_row_grilla(codigo).find_element(*self._locators.BTN_VER_DETALLE).click()
        self.find_element(self._locators.FADE_OUT)
        self.element_has_text(self._locators.LBL_TITULO_MODAL, codigo)
        with self.stale_element(self._locators.FADE_OUT):
            detalle = detalle()
            self.cerrar_modal()
        return detalle

    def _montos_row(self, row):
        montos = {}  # codigo: monto
        txts = self.get_childs_text(row, self._locators.BADGES_MONTO)
        for txt in txts:
            monto, moneda = txt.split(" ")
            montos[moneda] = monto
        return montos

    def validar_modales(self, codigo_operacion):
        if not self._validar_pagina:
            return
        row_transferencia = self._get_row_grilla(codigo_operacion)
        row_transferencia.find_element(*self._locators.BTN_CONFIRMAR_DEPOSITO).click()
        with self.stale_element(self._locators.FADE_OUT):
            self.find_element(self._locators.BTN_CONFIRMAR_DEPOSITO_MODAL).click()
            self.element_text_equals(self._locators.LBL_ERROR_MONEDAS, self._messages.ERROR_MONEDA_OBLIGATORIA)
            self.element_text_equals(self._locators.LBL_ERROR_PASSWORD, self._messages.ERROR_PASSWORD_OBLIGATORIO)
            [elem.send_keys(1) for elem in self.find_elements(self._locators.TXTS_MONEDA)]
            self.find_element(self._locators.TXT_PASSWORD).send_keys("jdfhjdfjh")
            self.find_element(self._locators.BTN_CONFIRMAR_DEPOSITO_MODAL).click()
            self.get_toast()
            self.dismiss_toast()
            self.find_element(self._locators.BTN_CERRAR_MODAL).click()

        # row_transferencia.find_element(*self._locators.BTN_HUBO_UN_PROBLEMA).click()
        # with self.stale_element(self._locators.FADE_OUT):
        #     self.find_element(self._locators.BTN_REPORTAR_PROBLEMA).click()
        #     self.element_has_text(self._locators.LBL_TITULO_MODAL, "Reporte de problema")
        #     self.element_text_equals(self._locators.LBL_ERROR_OBSERVACION, self._messages.ERROR_CAMPO_OBLITATORIO)
        #     self.element_text_equals(self._locators.LBL_ERROR_PASSWORD, self._messages.ERROR_CAMPO_OBLITATORIO)
        #     self.find_element(self._locators.TXT_OBSERVACIONES).send_keys("Test")
        #     self.find_element(self._locators.TXT_PASSWORD).send_keys("jdfhj")
        #     self.find_element(self._locators.BTN_REPORTAR_PROBLEMA).click()
        #     self.validar_toast(self._messages.ERROR_PASSWORD_INCORRECTO)
        #     self.find_element(self._locators.BTN_CERRAR_MODAL).click()

    # endregion

    # def _validar_modal_solicitud(self):
    #     if not self._validar_pantalla:
    #         return
    #     self.nueva_solicitud()
    #     self.find_element(self._locators.BTN_CONFIRMAR_SOLICITUD).click()
    #     self.element_text_equals(self._locators.LBL_ERROR_PASSWORD, self._messages.ERROR_PASSWORD_OBLIGATORIO)
    #     self.element_text_equals(self._locators.LBL_ERROR_MONEDAS, self._messages.ERROR_MONEDA_OBLIGATORIA)
    #     [e.send_keys(1) for e in self.find_elements(self._locators.TXTS_MONEDA)]
    #     self.find_element(self._locators.TXT_PASSWORD).send_keys("jgdgj")
    #     self.find_element(self._locators.BTN_CONFIRMAR_SOLICITUD).click()
    #     self.validar_toast(self._messages.ERROR_PASSWORD_INCORRECTO)
    #     with self.stale_element(self._locators.FADE_OUT):
    #         self.find_element(self._locators.BTN_CERRAR_MODAL).click()
    #     self.nueva_solicitud()

    def _validar_pantalla(self):
        pass
