from selenium.webdriver.common.by import By

from src.page_objects.base.base_page import Locator
from src.page_objects.page_elements.modales.properties.locators import ModalConfirmarMontosLocators
from src.page_objects.page_elements.properties.locators import IngresarMontosLocators


class CajaLocators:
    DIV_MONTO = Locator(By.CSS_SELECTOR, ".col-md-4")

    MontoPesos = Locator(By.ID, "inputMonedaAperturaARS")
    MontoPen = Locator(By.ID, "inputMonedaAperturaPEN")
    observaciones = Locator(By.ID, "inputObservacionesConfirm")
    Clave = Locator(By.ID, "inputPasswordConfirmApertura")

    Montos = Locator(By.CSS_SELECTOR, ".text-primary.m-0")

    MensajeHeader = Locator(By.CSS_SELECTOR, ".text-center.text-black-50.mb-4")
    MensajeCajaBloqueada = Locator(By.CSS_SELECTOR, ".text-center.text-danger > b")
    subMensajesCajaBloqueada = Locator(By.CSS_SELECTOR, ".text-black-50")

    btnIrCierreParcial = Locator(By.ID, "linkCierreParcial")
    btnIrCierreTotal = Locator(By.ID, "linkCierreTotal")

    btnAbrirModalApertura = Locator(By.ID, "btnAperturarCaja")
    btnAbrirModalCierreParcial = Locator(By.ID, "btnCerrarParcial")
    btnAbrirModalCierreTotal = Locator(By.ID, "btnCerrarTotal")
    btnCloseConfirmApertura = Locator(By.ID, "btnCloseConfirmApertura")

    btnConfirmarCierreParcial = Locator(By.ID, "btnConfirmCerrarParcial")
    btnConfirmarCierreTotal = Locator(By.ID, "btnConfirmCerrarTotal")
    btnConfirmarApertura = Locator(By.ID, "btnConfirmApertura")

    Modal = Locator(By.CSS_SELECTOR, ".modal.fade.show")

    # region DDJJ
    TituloDDJJ = Locator(By.CSS_SELECTOR, "h3.text-secondary")
    IdCaja = Locator(By.CSS_SELECTOR, "div.mt-3:nth-of-type(2) div.row > div.col-sm-6:nth-of-type(1) h5")
    Provincia = Locator(By.CSS_SELECTOR, "div.mt-3:nth-of-type(2) div.row > div.col-sm-6:nth-of-type(2) h5")
    Ciudad = Locator(By.CSS_SELECTOR, "div.mt-3:nth-of-type(2) div.row > div.col-sm-6:nth-of-type(3) h5")
    Sucursal = Locator(By.CSS_SELECTOR, "div.mt-3:nth-of-type(2) div.row > div.col-sm-6:nth-of-type(4) h5")
    btnIrAHome = Locator(By.ID, "linkSalirDDJJ")
    # endregion


class CajaBloqueadaLocators:
    LBL_TITULO = Locator(By.CSS_SELECTOR, "h1.text-danger")
    LBL_SUBTITULO = Locator(By.CSS_SELECTOR, ".text-center p:nth-of-type(1)")


class CajaNoAsociadaLocators:
    LBL_MENSAJE = Locator(By.CSS_SELECTOR, "h3 > b")


class OperacionesLocators:
    pass


class AperturaCajaLocators(IngresarMontosLocators, ModalConfirmarMontosLocators):
    LBL_ALERTA_SIN_OPERACIONES = Locator(By.CSS_SELECTOR, "h3.text-center.text-danger > b")
    LBL_MENSAJE_SIN_OPERACIONES = Locator(By.CSS_SELECTOR, "h5.text-center")
    LBL_COMUNIQUESE_CON_EL_AREA = Locator(By.CSS_SELECTOR, "p.text-center")


class DeclaracionJuradaLocators:
    BTN_HOME = Locator(By.ID, "linkSalirDDJJ")
    BTN_DESCARGAR = Locator(By.ID, "btnSaveCashbox")

class GestionDeCajaLocators:

    LOADING = Locator(By.CSS_SELECTOR, ".w-100 > img")
    SELECT_LOADING = Locator(By.CSS_SELECTOR, "[class*='loadingIndicator']")
    BTN_CERRAR_MODAL = Locator(By.CSS_SELECTOR, "button.close")

    # region Modal
    FADE_OUT = Locator(By.CSS_SELECTOR, ".modal.fade.show")
    # endregion

    # region Modal Asignar usuario
    SELECT_USUARIO = Locator(By.ID, "selectUsuario")
    # endregion

    # region grilla
    TABLA = Locator(By.ID, "tableGestionDeCajas")
    ROW = Locator(By.ID, "rowCaja{0}")
    COLUMNA_CODIGO_CAJA = Locator(By.CSS_SELECTOR, "[id*='codigo']")
    COLUMNA_CAJERO_ASIGNADO = Locator(By.CSS_SELECTOR, "[id*='nombreUsuario']")
    COLUMNA_OFICINA = Locator(By.CSS_SELECTOR, "[id*='oficina']")
    COLUMNA_ESTADO = Locator(By.CSS_SELECTOR, "[id*='estado']")
    BTN_ASIGNAR_USUARIO = Locator(By.CSS_SELECTOR, "[id*='btnAsignarUsuario']")
    BTN_DESBLOQUEAR_CAJA = Locator(By.CSS_SELECTOR, "[id*='btnDesbloquearCaja']")
    # endregion

    # region buscador
    TXT_CODIGO_CAJA = Locator(By.ID, "inputCode")
    TXT_USUARIO = Locator(By.ID, "inputName")
    SELECT_OFICINA = Locator(By.ID, "selectOficina")
    CHK_OPERATIVAS = Locator(By.CSS_SELECTOR, "#checkOperativas input")
    CHK_SIN_ASIGNAR = Locator(By.CSS_SELECTOR, "#checkSinAsignar input")
    CHK_BLOQUEADAS = Locator(By.CSS_SELECTOR, "#checkBloqueadas input")
    # endregion

    # region selects
    PANEL = Locator(By.CSS_SELECTOR, "#{0} [class*='MenuList']")
    OPTION = Locator(By.XPATH, "//div[contains(@id, 'react-select')][text()='{0}']")
    OPCION_SELECCIONADA = Locator(By.CSS_SELECTOR, "#{0} div[class$='-singleValue']")
    # endregion