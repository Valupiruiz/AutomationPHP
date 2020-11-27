from selenium.webdriver.common.by import By

from src.page_objects.base.base_page import Locator


class SucursalLocators:
    Sucursal = Locator(By.ID, "linkConfiguracionSucursales")
    Agregar = Locator(By.CSS_SELECTOR, ".MuiFab-label")
    FilaSucursal = Locator(By.XPATH, "//tr[./td/b[text()='{0}']]")
    CodigoSucursal = Locator(By.ID, "inputCode")
    NombreSucursal = Locator(By.ID, "inputName")
    EditarSucursal = Locator(By.CSS_SELECTOR, "a > button > .MuiIconButton-label")
    CambiarEstadoSucursal = Locator(By.CSS_SELECTOR, "td > button > .MuiIconButton-label")
    CAJAS_ACTIVAS_SUCURSAL = Locator(By.CSS_SELECTOR, "td:nth-of-type(2)")
    caja_activa = Locator(By.CSS_SELECTOR, "td:nth-of-type(1):not(.text-black-50)")
    caja_inactiva = Locator(By.CSS_SELECTOR, "td:nth-of-type(1).text-black-50")

    FADE_OUT = Locator(By.CSS_SELECTOR, ".modal.fade.show")
    LBL_MENSAJE_CAMBIAR_ESTADO_SUCURSAL = Locator(By.CSS_SELECTOR, ".mb-0.text-center")
    BTN_ACEPTAR_CAMBIO_ESTADO = Locator(By.CSS_SELECTOR, ".modal-content button:nth-of-type(2)")
    BTN_CERRAR_MODAL = Locator(By.CSS_SELECTOR, ".modal-header > button")


class AgregarSucursalLocators:
    Nombre = Locator(By.ID, "inputName")
    Codigo = Locator(By.ID, "inputCode")
    CodigoArea = Locator(By.ID, "inputAreaCode")
    Telefono = Locator(By.ID, "inputPhone")
    Email = Locator(By.ID, "inputMail")
    select_provincia = Locator(By.ID, "selectProvince")
    OPTION = Locator(By.XPATH, "//div[contains(@id, 'react-select')][text()='{0}']")
    PROVINCIA_SELECCIONADA = Locator(By.CSS_SELECTOR, "#selectProvince [class*='singleValue']")
    ciudad = Locator(By.ID, "inputCity")
    Direccion = Locator(By.ID, "inputAdress")
    CodigoPostal = Locator(By.NAME, "address.zipCode")
    Guardar = Locator(By.ID, "btnSaveCashbox")

    ROWS_CAJA_SUCURSAL = Locator(By.CSS_SELECTOR, "tbody tr.MuiTableRow-root")
    ROW_CAJA = Locator(By.XPATH, "//tr[td[text()='{0}']]")
    LBL_CODIGO_CAJA = Locator(By.CSS_SELECTOR, "td:nth-of-type(1)")
    LBL_ESTADO_CAJA = Locator(By.CSS_SELECTOR, "td:nth-of-type(2)")

    TOAST = Locator(By.XPATH, "//div[@class='Toastify__toast-body']")

    ERROR_NOMBRE = Locator(By.ID, "inputName-helper-text")
    ERROR_CODIGO = Locator(By.ID, "inputCode-helper-text")
    ERROR_PROVINCIA = Locator(By.CSS_SELECTOR, "#selectProvince p")
    ERROR_CIUDAD = Locator(By.ID, "inputCity-helper-text")
    ERROR_DIRECCION = Locator(By.ID, "inputAdress-helper-text")
    ERROR_CODIGO_POSTAL = Locator(By.ID, "inputZipCode-helper-text")
    ERROR_CODIGO_AREA = Locator(By.ID, "inputAreaCode-helper-text")
    ERROR_TELEFONO = Locator(By.ID, "inputPhone-helper-text")
    ERROR_MAIL = Locator(By.ID, "inputMail-helper-text")


class EditarSucursalLocators(AgregarSucursalLocators):
    ERROR_CODIGO_CAJA = Locator(By.ID, "inputCheckoutCode-helper-text")
    Codigo = Locator(By.CSS_SELECTOR, "#inputCode:disabled")  # al editar, el codigo esta deshabilitado
    PROVINCIA_SELECCIONADA = Locator(By.CSS_SELECTOR, "#selectProvince [class*='singleValue']")
    AddCaja = Locator(By.ID, "btnAddCashbox")
    CodigoCaja = Locator(By.ID, "inputCheckoutCode")
    GuardarModal = Locator(By.ID, "btnConfirmModal")

    GuardarSucursal = Locator(By.ID, "btnSaveCashbox")
    editar = Locator(By.XPATH, "//tr[td[text()='{0}']]/td/button")
    operacion = Locator(By.CSS_SELECTOR, "div.row:nth-of-type(3) > .col > span:nth-of-type(1)")
    moneda = Locator(By.ID, "checkOutcomingRemittanceCurrenciesARS")
    enviaGirosUSD = Locator(By.ID, "checkOutcomingRemittanceCurrenciesUSD")
    recibeGirosUSD = Locator(By.ID, "checkIncomingRemittanceCurrenciesUSD")
    Deshabilitarcaja = Locator(By.CSS_SELECTOR, "div.modal-content div.react-switch-bg")
    fadeOutModal = Locator(By.CSS_SELECTOR, ".modal.fade.show")
    cantidad_cajas = Locator(By.CSS_SELECTOR, "tbody > tr.MuiTableRow-root")
    cantidad_cajas_activas = Locator(By.CSS_SELECTOR, "tbody > tr.MuiTableRow-root > td.text-success")
    cantidad_cajas_inactivas = Locator(By.CSS_SELECTOR, "tbody > tr.MuiTableRow-root > td.text-secondary")
