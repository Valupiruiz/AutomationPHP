from selenium.webdriver.common.by import By

from src.page_objects.base.base_page import Locator


class ModalDesbloquearCajaLocators:
    LBL_TITULO = Locator(By.CSS_SELECTOR, ".modal-title")
    BTN_CERRAR_MODAL = Locator(By.CSS_SELECTOR, "button.close")

    LBL_USUARIO = Locator(By.ID, "DetalleDatoUsuario")
    # wtf
    LBL_FECHA = Locator(By.ID, "DetalleDatoFecha de bloqueo")
    LBL_SITUACION = Locator(By.ID, "DetalleDatoSituación de bloqueo")

    TABLA = Locator(By.ID, "tableDebloquearCajaMontos")

    LBLS_LOGICO = Locator(By.CSS_SELECTOR, "[id*='logica'] > span")
    LBLS_REALES = Locator(By.CSS_SELECTOR, "[id*='reales'] > span")
    LBLS_DIFERENCIA = Locator(By.CSS_SELECTOR, "[id*='diferencia'] > span")

    TXT_OBSERVACION = Locator(By.ID, "inputObservaciones")

    BTN_DESBLOQUEAR_CAJA = Locator(By.ID, "btnDesbloquearCaja")


class ModalABMCajaLocators:
    ERROR_CODIGO_CAJA = Locator(By.ID, "inputCheckoutCode-helper-text")

    LBL_TITULO = Locator(By.CSS_SELECTOR, ".modal-title")

    FADE_OUT = Locator(By.CSS_SELECTOR, ".modal.fade.show")
    MODAL = Locator(By.CSS_SELECTOR, ".modal-content")
    TXT_CODIGO_CAJA = Locator(By.ID, "inputCheckoutCode")

    CHK_ENVIA_GIROS = Locator(By.ID, "checkCanSendRemittance")
    CHK_ENVIA_GIROS_MONEDA = Locator(By.ID, "checkOutcomingRemittanceCurrencies{0}")
    MONEDAS_DISPONIBLES_ENVIO = Locator(By.CSS_SELECTOR, "[id*='checkOutcomingRemittanceCurrencies']")

    MONEDAS_DISPONIBLES_RECIBO = Locator(By.CSS_SELECTOR, "[id*='checkIncomingRemittanceCurrencies']")
    CHK_RECIBE_GIROS_MONEDA = Locator(By.ID, "checkIncomingRemittanceCurrencies{0}")
    CHK_RECIBE_GIROS = Locator(By.ID, "checkCanRecieveRemittance")

    BTN_NUEVA_CAJA = Locator(By.ID, "btnAddCashbox")
    BTN_GUARDAR = Locator(By.ID, "btnConfirmModal")
    BTN_CERRAR = Locator(By.ID, "btnCloseCheckoutModal")
    BTN_EDITAR_CAJA = Locator(By.XPATH, "//tr[td[text()='{0}']]/td/button")
    ESTADO_CAJA = Locator(By.ID, "switchCheckoutState")
    CHK_ESTADO_CAJA = Locator(By.CSS_SELECTOR, ".modal .react-switch-bg")


class ModalConfirmarMontosLocators:
    TOAST = Locator(By.CSS_SELECTOR, ".Toastify__toast-body")
    FADE_OUT = Locator(By.CSS_SELECTOR, ".modal.fade.show")
    TXT_OBSERVACIONES = Locator(By.ID, "inputObservaciones")
    TXT_PASSWORD = Locator(By.ID, "inputPasswordConfirmApertura")

    LBL_CODIGO_MONTO = Locator(By.ID, "textSymbolMontoMoneda{0}")
    LBL_MONTO = Locator(By.ID, "textValueMontoMoneda{0}")
    LBL_TITULO_MODAL = Locator(By.CSS_SELECTOR, ".modal-title")
    LBL_DESCRIPCION = Locator(By.CSS_SELECTOR, "p.text-center")

    BTN_CONFIRMAR_CIERRE_PARCIAL = Locator(By.ID, "btnConfirmCerrarParcial")
    BTN_CONFIRMAR_APERTURA = Locator(By.ID, "btnConfirmApertura")
    BTN_CONFIRMAR_CIERRE_TOTAL = Locator(By.ID, "btnConfirmCerrarTotal")

    ERROR_PASSWORD = Locator(By.ID, "inputPasswordConfirmApertura-helper-text")
    BTN_CERRAR_MODAL = Locator(By.CSS_SELECTOR, "[id*='btnCloseConfirm']")


class ModalAsignarCajeroLocators:
    LBL_TITULO_MODAL = Locator(By.CSS_SELECTOR, ".modal-title")
    LBL_INFO = Locator(By.CSS_SELECTOR, "small.text-muted")

    LBL_CODIGO_CAJA = Locator(By.ID, "DetalleDatoId de caja")
    LBL_OFICINA = Locator(By.ID, "DetalleDatoOficina")
    SELECT_USUARIO = Locator(By.ID, "selectUsuario")
    LBL_USUARIO_ASIGNADO = Locator(By.CSS_SELECTOR, "div.col > p")
    BTN_GUARDAR_ASIGNACION = Locator(By.ID, "btnGuardarAsignacionUsuario")
    BTN_DESASIGNAR_USUARIO = Locator(By.CSS_SELECTOR, "[id*='btnDesasignarUsuario']")
