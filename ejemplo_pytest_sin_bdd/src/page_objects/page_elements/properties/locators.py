from selenium.webdriver.common.by import By

from src.page_objects.base.base_page import Locator


class DetalleOperacionLocators:
    LBL_TITULO = Locator(By.CSS_SELECTOR, "h5.modal-title")
    LBL_SUB_TITULO = Locator(By.CSS_SELECTOR, "h5.modal-title small")
    LBL_MEDIO = Locator(By.ID, "DetalleDatoMedio")
    LBL_DESTINO = Locator(By.ID, "DetalleDatoDestino")
    LBL_ORIGEN = Locator(By.ID, "DetalleDatoOrigen")
    LBL_OBSERVACION = Locator(By.ID, "textObservaciones")
    LBL_MONEDAS = Locator(By.CSS_SELECTOR, "[id*='textSymbolMontoMoneda']")
    LBL_MONEDA = Locator(By.ID, "textSymbolMontoMoneda{0}")
    LBL_MONTO = Locator(By.ID, "textValueMontoMoneda{0}")
    LBL_INFO_P = Locator(By.CSS_SELECTOR, "p.text-center")


class IngresarMontosLocators:
    LBL_TITULO = Locator(By.CSS_SELECTOR, ".text-center")
    LBL_DESCRIPCION = Locator(By.CSS_SELECTOR, "small.text-muted")
    DIV_MONTOS = Locator(By.CSS_SELECTOR, ".col-md-4")
    TXT_MONTOS = Locator(By.CSS_SELECTOR, "input[id*='inputMonedaApertura']")
    TXT_MONTO = Locator(By.ID, "inputMonedaApertura{0}")

    BTN_APERTURAR = Locator(By.ID, "btnAperturarCaja")
    BTN_CERRAR_PARCIALMENTE = Locator(By.ID, "btnCerrarParcial")
    BTN_CERRAR_TOTALMENTE = Locator(By.ID, "btnCerrarTotal")

    ERROR_MONTO = Locator(By.CSS_SELECTOR, "[id$='helper-text']")


class NavBarLocators:
    BTN_CIERRES = Locator(By.ID, "btnCierreOperable")
    BTN_MENU = Locator(By.ID, "btnMenuUsuario")
    LISTA = Locator(By.ID, "menu-list-grow")
    BTN_HOME = Locator(By.ID, "linkHome")
    NAV_BAR = Locator(By.CSS_SELECTOR, "div > nav.navbar")
    BTN_TRANSFERENCIAS_ENTRANTES = Locator(By.LINK_TEXT, "Transferencias entrantes")
    BTN_TRANSFERENCIAS_SALIENTES = Locator(By.LINK_TEXT, "Transferencias salientes")

    BTN_CIERRE_PARCIAL = Locator(By.ID, "linkCierreParcial")
    BTN_CIERRE_TOTAL = Locator(By.ID, "linkCierreTotal")


class PaginadoLocators:
    PAGINA = Locator(By.CSS_SELECTOR, "li[data-test='goto-page-{0}'] > a")
    ACTUAL = Locator(By.CSS_SELECTOR, ".page-item.active")
    PAGINAS = Locator(By.CSS_SELECTOR, "li.page-item > a")


class MenuRolesLocators:
    LISTA = Locator(By.ID, "menu-list-grow")
    BTN_MENU = Locator(By.ID, "btnMenuUsuario")
    BTN_CERRAR = Locator(By.ID, "btnCerrarSesion")
    LBL_TRABAJANDO_CON = Locator(By.CSS_SELECTOR, "#menu-list-grow small")
    LBL_ROL_ACTUAL = Locator(By.CSS_SELECTOR, "div > p.text-primary")
    LBL_SUBTITULO_ROL = Locator(By.CSS_SELECTOR, "div > p.text-muted")

    LBLS_ROL = Locator(By.CSS_SELECTOR, "ul > a[id*='id']")
