from selenium.webdriver.common.by import By
from page_objects.base_page import Locator

class MenuLocators:
    avisos_BTN = Locator(By.XPATH, "//a[@class='puntero'][contains(text(),'Avisos')]")
    ingreso_manual_BTN = Locator(By.ID, "ingreso_manual_li")
    verificacion_BTN = Locator(By.XPATH, "//a[contains(text(),'Verificación')]")
    bandeja_tramites_BTN = Locator(By.XPATH, "//a[contains(text(),'Bandeja de trámites')]")
    cierre_edicion_BTN = Locator(By.XPATH, "//a[contains(text(),'Cierre de edición')]")
    orden_armado_BTN = Locator(By.XPATH, "//li[@id='orden_armado_li']//a[@class='nav-pill-link'][contains(text(),'Orden de armado')]")
    facturacion_y_cobros_BTN =Locator(By.XPATH, "//a[contains(text(),'Facturación y cobros')]")
    facturas_BTN = Locator(By.XPATH, "//li[@id='facturacion_li']//a[@class='nav-pill-link']")
    facturas_hist_BTN = Locator(By.XPATH, "//li[@id='facturacion_historica_li']//a[@class='nav-pill-link']")
    nota_credito_BTN = Locator(By.XPATH, "//li[@id='nota_credito_li']//a[@class='nav-pill-link']")
    recibos_BTN = Locator(By.XPATH, "//li[@id='recibo_li']//a[@class='nav-pill-link']")
    administracion_BTN = Locator(By.XPATH, "//a[contains(text(),'Administración')]")
    organismos_BTN = Locator(By.XPATH, "//a[contains(text(),'Organismos - VIEJO')]")
    organismos_new_BTN = Locator(By.XPATH, "//li[@id='organismos_li']//a[@class='nav-pill-link'][contains(text(),'Organismos')]")
    firmantes_BTN = Locator(By.XPATH,"//a[contains(text(),'Firmantes acto Adm.')]")
    cuarta_BTN = Locator(By.XPATH, "//a[contains(text(),'Administrar Cuarta Sección')]")
    cuarta_aviso_BTN = Locator(By.XPATH, "//a[contains(text(),'Cargar avisos')]")
    organismo_judicial_BTN = Locator(By.XPATH, "//a[contains(text(),'Organismos judiciales')]")
    oa_suplementos_BTN = Locator(By.XPATH, "//a[contains(text(),'Orden de armado suplementos')]")
