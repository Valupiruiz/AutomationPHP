from selenium.webdriver.common.by import By

from src.page_objects.base.base_page import Locator


class TransferenciasSalientesLocators:
    # region globals modales
    LBL_ERROR_MONEDAS = Locator(By.CSS_SELECTOR, ".mb-4.col")
    LBL_ERROR_PASSWORD = Locator(By.ID, "inputPasswordConfirmApertura-helper-text")
    TXT_MONEDA = Locator(By.ID, "inputMontoMoneda{0}")
    TXTS_MONEDA = Locator(By.CSS_SELECTOR, "input[id*='inputMontoMoneda']")
    LBL_TITULO_MODAL = Locator(By.CSS_SELECTOR, ".modal-title")
    LBL_SMALL = Locator(By.CSS_SELECTOR, "small.text-muted")
    LBL_DETALLE_TITULO = Locator(By.CSS_SELECTOR, ".modal-title p > small")
    FADE_OUT = Locator(By.CSS_SELECTOR, ".modal.fade.show")
    BTN_CERRAR_MODAL = Locator(By.CSS_SELECTOR, "button.close")
    LBL_MEDIO_DETALLE = Locator(By.ID, "textMedioTransferencia")
    LBL_DESTINO_DETALLE = Locator(By.ID, "textDestinoTransferencia")
    LBL_MONTO_DETALLE = Locator(By.ID, "textValueMontoMoneda{0}")
    TXT_PASSWORD = Locator(By.ID, "inputPasswordConfirmApertura")
    # endregion

    # region Modal generar Extraccion
    BTN_NUEVA_EXTRACCION = Locator(By.ID, "btnNuevaExtraccion")
    SELECT = Locator(By.CSS_SELECTOR, "#selectDestinoTransferencia .MuiInputBase-input")
    OPTION = Locator(By.XPATH, "//div[contains(@id, 'react-select')][text()='{0}']")
    RANDOM_OPTION = Locator(By.CSS_SELECTOR, "[id*='react-select']")
    ELIMINAR_OPTION = Locator(By.CSS_SELECTOR, "#selectDestinoTransferencia .MuiOutlinedInput-input "
                                               "div[class*='Container']:nth-of-type(1)")
    DESTINO_SELECCIONADO = Locator(By.CSS_SELECTOR, "#selectDestinoTransferencia [class$='singleValue']")
    TXT_OBSERVACIONES = Locator(By.ID, "inputObservaciones")

    LBL_ALERTA = Locator(By.CSS_SELECTOR, ".modal .alert-primary")

    BTN_CONFIRMAR_EXTRACCION = Locator(By.ID, "btnConfirmarExtraccion")

    LBL_ERROR_DESTINO = Locator(By.CSS_SELECTOR, "#selectDestinoTransferencia p")

    # endregion

    # region global grilla
    RESULTADOS_GRILLA = Locator(By.CSS_SELECTOR, "[id*='row']")
    LBL_SIN_RESULTADO = Locator(By.CSS_SELECTOR, ".card-body .alert.text-center")
    CONTAINER = Locator(By.CSS_SELECTOR, "h1.text-center")
    # endregion

    # region Grilla extracciones en curso
    PILL_EXTRACCIOINES_EN_CURSO = Locator(By.CSS_SELECTOR, ".nav-item:nth-of-type(2) a.nav-link")
    ROW = Locator(By.XPATH, '//tr[td[1][text()="{0}"]]')

    BTN_VER_DETALLE = Locator(By.CSS_SELECTOR, "[id*='btnVerDetalle']")
    BTN_CANCELAR_EXTRACCION = Locator(By.CSS_SELECTOR, "[id*='btnCancelarExtraccion']")
    LBL_ID_TRANSF = Locator(By.CSS_SELECTOR, "td:nth-of-type(1)")
    LBL_MONTO_EXTRAIDO = Locator(By.XPATH, "//span[text()='{0}'][text()='{1}']")
    LBL_FECHA = Locator(By.CSS_SELECTOR, "td:nth-of-type(2)")
    LBL_MEDIO = Locator(By.CSS_SELECTOR, "td:nth-of-type(4)")
    LBL_ESTADO_TRANSFERENCIA = Locator(By.CSS_SELECTOR, "td:nth-of-type(6)")
    LBL_DESTINO = Locator(By.CSS_SELECTOR, "td:nth-of-type(3)")
    BADGES_MONTO = Locator(By.CSS_SELECTOR, "td .badge")
    # endregion

    # region Grilla solicitudes de fondo
    PILL_SOLICITUD_FONDOS = Locator(By.CSS_SELECTOR, ".nav-item:nth-of-type(1) a.nav-link")
    LBL_ESTADO_SOLICITUD = Locator(By.CSS_SELECTOR, "td:nth-of-type(5)")
    LBL_ORIGEN_SOLICITUD = Locator(By.CSS_SELECTOR, "td:nth-of-type(3)")
    BTN_AUTORIZAR_SOLICITUD = Locator(By.CSS_SELECTOR, "[id*='btnAutorizarsolicitud']")
    BTN_RECHAZAR_SOLICITUD = Locator(By.CSS_SELECTOR, "[id*='btnCancelarExtraccion']")
    # endregion

    # region Modal Detalle extraccion
    LBL_OBSERVACION_DETALLE = Locator(By.ID, "textObservaciones")
    # endregion

    # region Modal solicitud fondos
    BTN_AUTORIZAR_SOLICITUD_MODAL = Locator(By.ID, "btnAutorizarSolicitud")
    BTN_RECHAZAR_SOLICITUD_MODAL = Locator(By.ID, "btnRechazarSolicitud")
    # endregion

    # region Modal cancelar extraccion
    LBL_INFO_TEXT = Locator(By.CSS_SELECTOR, ".modal p.text-center")
    LBL_OBSERVACION_CANCELAR = Locator(By.ID, "textObservacionesDetalleTransferencia")
    BTN_CANCELAR_EXTRACCION_MODAL = Locator(By.CSS_SELECTOR, "#btnCancelarExtraccion.btn-danger")
    # endregion


class TransferenciasEntrantesLocators:
    # region Grilla Solicitudes de fondos
    PILL_SOLICITUD_FONDOS = Locator(By.CSS_SELECTOR, ".nav-item:nth-of-type(1) a.nav-link")
    BTN_NUEVA_SOLICITUD = Locator(By.ID, "btnNuevaSolicitud")
    # endregion

    # region Modal solicitar fondos
    BTN_CONFIRMAR_SOLICITUD = Locator(By.ID, "btnConfirmarSolicitud")
    LBL_INFO_TEXT = Locator(By.CSS_SELECTOR, "p > small.text-muted")
    # endregion

    # region Modal cancelar solicitud fondos
    LBL_INFO_P = Locator(By.CSS_SELECTOR, "p.text-center")
    LBLS_MONEDA = Locator(By.CSS_SELECTOR, "[id*='textSymbolMontoMoneda']")
    LBLS_MONTO = Locator(By.CSS_SELECTOR, "[id*='textValueMontoMoneda']")
    LBL_OBSERVACION = Locator(By.CSS_SELECTOR, "textObservaciones")
    BTN_CANCELAR_SOLICITUD_MODAL = Locator(By.ID, "btnConfirmarCancelaciónSolicitudDeposito")
    # endregion

    # region globals modales
    LBL_TITULO_MODAL = Locator(By.CSS_SELECTOR, ".modal-title")
    FADE_OUT = Locator(By.CSS_SELECTOR, ".modal.fade.show")
    BTN_CERRAR_MODAL = Locator(By.CSS_SELECTOR, "button.close")
    # endregion

    # region global grilla
    RESULTADOS_GRILLA = Locator(By.CSS_SELECTOR, "[id*='row']")
    LBL_SIN_RESULTADO = Locator(By.CSS_SELECTOR, ".card-body .alert.text-center")
    CONTAINER = Locator(By.CSS_SELECTOR, "h1.text-center")
    # endregion

    # region grilla transferencias en curso
    PILL_DEPOSITOS = Locator(By.CSS_SELECTOR, ".nav-item:nth-of-type(2) a.nav-link")
    ROW_CODIGO = Locator(By.XPATH, '//tr[td[1][text()="{0}"]]')
    BTN_VER_DETALLE = Locator(By.CSS_SELECTOR, "[id*='btnVerDetalle']")
    BTN_CONFIRMAR_DEPOSITO = Locator(By.CSS_SELECTOR, "[id*='btnConfirmarRecepcionDeposito']")
    BTN_RECEPCIONAR_DEPOSITO = Locator(By.CSS_SELECTOR, "[id*='btnConfirmarDepositoEnOficina']")
    BTN_HUBO_UN_PROBLEMA = Locator(By.CSS_SELECTOR, "[id*='btnConfirmarNoRecepcionDeposito']")
    LBL_MONTO_EXTRAIDO = Locator(By.XPATH, "//span[text()='{0}'][text()='{1}']")
    BADGES_MONTO = Locator(By.CSS_SELECTOR, "td .badge")
    LBL_ORIGEN = Locator(By.CSS_SELECTOR, "td:nth-of-type(3)")
    LBL_FECHA = Locator(By.CSS_SELECTOR, "td:nth-of-type(2)")
    LBL_MEDIO = Locator(By.CSS_SELECTOR, "td:nth-of-type(4)")
    LBL_ESTADO_TRANSFERENCIA = Locator(By.CSS_SELECTOR, "td:nth-of-type(5)")
    # endregion

    # region grilla solicitudes
    LBL_ESTADO_SOLICITUD = Locator(By.CSS_SELECTOR, "td:nth-of-type(4)")
    BTN_VER_DETALLE_SOLICITUD = Locator(By.CSS_SELECTOR, "[id*='btnVerDetalleSolicitudDeposito']")
    LBL_CODIGO_SOLICITUD = Locator(By.CSS_SELECTOR, "td:nth-of-type(1)")
    BTN_CANCELAR_SOLICITUD = Locator(By.CSS_SELECTOR, "[id*='btnConfirmarCancelacionSolicitudDeposito']")
    # endregion

    # region modal confirmar deposito
    LBL_ESTADO_CONFIRMADO = Locator(By.CSS_SELECTOR, ".text-success.text-center")
    TXT_MONEDA = Locator(By.ID, "inputMontoMoneda{0}")
    TXTS_MONEDA = Locator(By.CSS_SELECTOR, "input[id*='inputMontoMoneda']")
    TXT_OBSERVACIONES = Locator(By.ID, "inputObservaciones")
    TXT_PASSWORD = Locator(By.ID, "inputPasswordConfirmApertura")

    BTN_CONFIRMAR_DEPOSITO_MODAL = Locator(By.ID, "btnConfirmOperacion")

    LBL_ERROR_MONEDAS = Locator(By.CSS_SELECTOR, ".mb-4.col")
    LBL_ERROR_PASSWORD = Locator(By.ID, "inputPasswordConfirmApertura-helper-text")
    # endregion

    # region modal hubo un problema
    BTN_REPORTAR_PROBLEMA = Locator(By.ID, "btnConfirmarNoRecepcionDeposito")
    LBL_ERROR_OBSERVACION = Locator(By.ID, "inputObservaciones-helper-text")
    # endregion
