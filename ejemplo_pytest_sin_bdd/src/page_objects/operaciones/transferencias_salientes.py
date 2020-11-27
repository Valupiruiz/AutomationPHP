from selenium.common.exceptions import TimeoutException

from src.page_objects.base.base_page import ActionChains
from src.page_objects.operaciones.properties.locators import TransferenciasSalientesLocators
from src.page_objects.operaciones.properties.messages import TransferenciasMessages
from src.page_objects.page_elements.detalle_operacion import DetalleOperacionPageElement
from src.page_objects.page_elements.nav_bar import NavBarPageElement
from src.page_objects.page_elements.paginado import PaginadoPageElement
from src.utils.others import today


class TransferenciasSalientesPage(NavBarPageElement):

    def __init__(self, driver, validar_paginas):
        self._locators = TransferenciasSalientesLocators
        self._messages = TransferenciasMessages
        super().__init__(driver, validar_paginas)
        self.wait_for_url("/operaciones/transferencias-salientes")
        self._detalle_operaciones = DetalleOperacionPageElement(self)
        self._paginado = PaginadoPageElement(self)

    # region Solicitud

    def nueva_autorizacion_solicitud(self, codigo):
        self._get_row_grilla(codigo).find_element(*self._locators.BTN_AUTORIZAR_SOLICITUD).click()
        self.find_element(self._locators.FADE_OUT)
        self.element_text_equals(self._locators.LBL_TITULO_MODAL,
                                 f"Autorización de solicitud de depósito\n{codigo} - {today()}")
        self.element_text_equals(self._locators.LBL_SMALL, "Ingrese los montos a autorizar.")
        self.element_text_equals(self._locators.TXT_OBSERVACIONES, '')

    def modificar_montos_autorizacion_solicitud(self, montos):
        locators = [self._locators.TXT_MONEDA.format_locator(codigo) for codigo in self._monedas_modal()]
        self.clear_elements_text(*locators)
        self._completar_montos(montos)

    def autorizar_solicitud(self, observacion, password):
        self.find_element(self._locators.TXT_OBSERVACIONES).send_keys(observacion)
        self.find_element(self._locators.TXT_PASSWORD).send_keys(password)
        self.find_element(self._locators.BTN_AUTORIZAR_SOLICITUD_MODAL).click()

    def nuevo_rechazo(self, codigo):
        self._get_row_grilla(codigo).find_element(*self._locators.BTN_RECHAZAR_SOLICITUD).click()
        self.find_element(self._locators.FADE_OUT)
        self.element_text_equals(self._locators.LBL_TITULO_MODAL,
                                 f"Rechazo de solicitud de depósito\n{codigo} - {today()}")
        self.element_text_equals(self._locators.TXT_OBSERVACIONES, '')

    def rechazar_solicitud(self, observacion, password):
        self.find_element(self._locators.TXT_OBSERVACIONES).send_keys(observacion)
        self.find_element(self._locators.TXT_PASSWORD).send_keys(password)
        self.find_element(self._locators.BTN_RECHAZAR_SOLICITUD_MODAL).click()

    def tabla_solicitud_entrante(self, codigo):
        row = self._get_row_grilla(codigo)
        return {
            "Estado": self.get_child_text(row, self._locators.LBL_ESTADO_SOLICITUD),
            "Montos": self._montos_row(row),
            "Fecha": self.get_child_text(row, self._locators.LBL_FECHA),
            "Origen": self.get_child_text(row, self._locators.LBL_ORIGEN_SOLICITUD),
        }

    def detalle_solicitud_fondos(self, codigo):
        return self._get_detalle(codigo, "Solicitud")

    def solicitud_stale(self, codigo, refresh):
        if refresh:
            with self.stale_element(self._locators.CONTAINER):
                self.driver.refresh()
        self.pill_solicitud_fondos()
        self._row_stale(codigo, "solicitud")

    def pill_solicitud_fondos(self):
        self.find_element(self._locators.PILL_SOLICITUD_FONDOS).click()

    def montos_autorizacion_solicitud(self):
        montos = {}  # codigo: monto
        for moneda in self._monedas_modal():
            monto = self.get_element_text(self._locators.TXT_MONEDA.format_locator(moneda))
            if not monto:  # si esta vacio, el monto es 0
                monto = 0
            montos[moneda] = monto
        return montos

    def nueva_cancelacion_transferencia(self, codigo):
        e = self._get_row_grilla(codigo)
        e.find_element(*self._locators.BTN_CANCELAR_EXTRACCION).click()
        self.find_element(self._locators.FADE_OUT)

    def detalle_cancelacion_transferencia(self):
        return self._detalle_operaciones.get_cancelacion()

    def cancelar_transferencia(self, password):
        self.find_element(self._locators.TXT_PASSWORD).send_keys(password)
        self.find_element(self._locators.BTN_CANCELAR_EXTRACCION_MODAL).click()

    # endregion

    # region Transferencia

    def destino_seleccionado(self):
        return self.get_element_text(self._locators.DESTINO_SELECCIONADO)

    def nueva_extraccion(self):
        self.find_element(self._locators.BTN_NUEVA_EXTRACCION).click()
        self.find_element(self._locators.FADE_OUT)
        self.element_text_equals(self._locators.LBL_TITULO_MODAL, "Generar una extracción")


    def seleccionar_destinatario(self, destinatario):
        self._completar_select(destinatario)

    def monedas_disponibles_deposito(self):
        return self._monedas_modal()

    def mensaje_extraccion_sin_monedas(self):
        self.element_text_equals(self._locators.LBL_ALERTA, self._messages.ALERTA_NO_HAY_MONEDAS)

    def generar_extraccion(self, montos, observacion, password):
        self._completar_modal_transferencia(montos, observacion)
        self.find_element(self._locators.TXT_PASSWORD).send_keys(password)
        self.find_element(self._locators.BTN_CONFIRMAR_EXTRACCION).click()

    def _completar_modal_transferencia(self, montos, observacion):
        self._completar_montos(montos)
        self.find_element(self._locators.TXT_OBSERVACIONES).send_keys(observacion)
        self.element_text_equals(self._locators.TXT_OBSERVACIONES, observacion)

    def tabla_transferencia_saliente(self, codigo_transferencia):
        row = self._get_row_grilla(codigo_transferencia)

        return {
            "Estado": self.get_child_text(row, self._locators.LBL_ESTADO_TRANSFERENCIA),
            "Montos": self._montos_row(row),
            "Fecha": self.get_child_text(row, self._locators.LBL_FECHA),
            "Destino": self.get_child_text(row, self._locators.LBL_DESTINO),
            "Medio": self.get_child_text(row, self._locators.LBL_MEDIO)
        }

    def detalle_transferencia_saliente(self, codigo):
        return self._get_detalle(codigo, "Transferencia")

    def pill_extracciones_en_curso(self):
        self.find_element(self._locators.PILL_EXTRACCIOINES_EN_CURSO).click()

    # endregion

    # region Common

    def _monedas_modal(self):
        return [moneda.get_attribute('id')[-3:] for moneda in self.find_elements(self._locators.TXTS_MONEDA)]

    def _completar_montos(self, montos):
        for moneda, monto in montos.items():
            locator = self._locators.TXT_MONEDA.format_locator(moneda.codigo)
            self.find_element(locator).send_keys(monto)
            self.element_has_text(locator, str(monto))

    def _completar_select(self, option):
        self.find_element(self._locators.SELECT).click()
        ac = ActionChains(self.driver)
        ac.send_keys(option[:-1])
        ac.pause(1).send_keys(option[-1])
        ac.perform()
        self.find_element(self._locators.OPTION.format_locator(option)).click()
        self.element_has_text(self._locators.DESTINO_SELECCIONADO, option)

    def _montos_row(self, row):
        montos = {}  # codigo: monto
        txts = self.get_childs_text(row, self._locators.BADGES_MONTO)
        for txt in txts:
            monto, moneda = txt.split(" ")
            montos[moneda] = monto
        return montos

    def _get_detalle(self, codigo, tipo_detalle):
        detalle = {
            "Solicitud": self._detalle_operaciones.get_solicitud,
            "Transferencia": self._detalle_operaciones.get_transferencia_saliente
        }[tipo_detalle]
        self._get_row_grilla(codigo).find_element(*self._locators.BTN_VER_DETALLE).click()
        self.find_element(self._locators.FADE_OUT)
        self.element_has_text(self._locators.LBL_TITULO_MODAL, codigo)
        with self.stale_element(self._locators.FADE_OUT):
            detalle = detalle()
            self.cerrar_modal()
        return detalle

    def transferencia_stale(self, codigo, refresh):
        # Estos ifs quizas deberia hacerlos en el action :thinking:
        if refresh:
            with self.stale_element(self._locators.CONTAINER):
                self.driver.refresh()

        if "boveda" in self.driver.current_url:
            self.pill_extracciones_en_curso()
        self._row_stale(codigo, "transferencia")

    def _row_stale(self, codigo, tipo_row):
        try:
            self._get_row_grilla(codigo, 5)
        except TimeoutException:
            pass
        else:
            raise TimeoutException(
                f"Esperaba que la {tipo_row} desapareciera de la lista")

    # todo: abstraer grilla para reciclar codigo, se repiten muchos metodos entre transf salientes y entrantes
    def _get_row_grilla(self, codigo_operacion, timeout=5):
        cant_resultados = self._cant_resultados_grilla()
        if cant_resultados > 10:  # Si hay mas de 10 resultados, se deberia activar el paginado
            return self._paginado.search(
                lambda: self.find_element(self._locators.ROW.format_locator(codigo_operacion), timeout))
        return self.find_element(self._locators.ROW.format_locator(codigo_operacion), timeout)

    # fixme
    def _cant_resultados_grilla(self):
        try:
            return len(self.wait_for_elements(self._locators.RESULTADOS_GRILLA, 5))
        except TimeoutException:
            return 0

    def cerrar_modal(self):
        with self.stale_element(self._locators.FADE_OUT):
            self.find_element(self._locators.BTN_CERRAR_MODAL).click()

    # endregion

    def _validar_pantalla(self):
        self.nueva_extraccion()
        self.find_element(self._locators.BTN_CONFIRMAR_EXTRACCION).click()
        self.element_text_equals(self._locators.LBL_ERROR_DESTINO, self._messages.ERROR_DESTINO_OBLIGATORIO)
        self.element_text_equals(self._locators.LBL_ERROR_PASSWORD, self._messages.ERROR_PASSWORD_OBLIGATORIO)
        self.find_element(self._locators.SELECT).click()
        self.find_element(self._locators.RANDOM_OPTION).click()
        try:
            self.element_text_equals(self._locators.LBL_ERROR_MONEDAS, self._messages.ERROR_MONEDA_OBLIGATORIA)
            for e in self.find_elements(self._locators.TXTS_MONEDA):
                e.send_keys(1)
        except TimeoutException:  # si no encuentra el error de monedas, no hay monedas en comun
            self.mensaje_extraccion_sin_monedas()
        else:
            self.find_element(self._locators.TXT_PASSWORD).send_keys("jgdgj")
            self.find_element(self._locators.BTN_CONFIRMAR_EXTRACCION).click()
            self.get_toast()
            self.dismiss_toast()
            elems = self.find_elements(self._locators.TXTS_MONEDA)
            self.find_element(self._locators.ELIMINAR_OPTION).click()
            [self.wait_for_stale_element(e) for e in elems]
        self.find_element(self._locators.BTN_CERRAR_MODAL).click()
