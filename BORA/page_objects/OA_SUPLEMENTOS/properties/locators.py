from selenium.webdriver.common.by import By
from page_objects.base_page import Locator
import time


class OA_Suplementos_locators:
    fecha_publicacion_INP = Locator(By.ID, "OrdenSearchType_fechaPub")
    crear_oa_BTN = Locator(By.XPATH, "//button[@class='btn btn-info btn-sm pull-right botonnuevo']")
    titulo_LBL = Locator(By.XPATH, "//h3")
    nro_edicion_INP = Locator(By.ID, "numeroBoletinSuplementoOA")
    guardar_BTN = Locator(By.ID, "guardarBtn")
    alert_LBL = Locator(By.XPATH, "//div[@class='alerts']//div[@class='alert alert-success']")
    ver_pdf_BTN = Locator(By.ID, "pdfBtn")
    visualizar_oa_TEMP = Locator(By.XPATH, "//td[contains(text(),'{fecha}')]//following-sibling::td[contains(text(),'{nombre}')]//following-sibling::td//i[@class='fa fa-search']")