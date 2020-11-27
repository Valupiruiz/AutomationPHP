from selenium.webdriver.common.by import By
from page_objects.base_page import Locator

class LocatorsFirmantes:
    nombre_INP = Locator(By.ID, "SelectFirmanteActoAdministrativoType_nombre")
    codigo_INP = Locator(By.ID, "SelectFirmanteActoAdministrativoType_codigo")
    guardar_BTN = Locator(By.ID, "guardar")
    nuevo_BTN = Locator(By.XPATH, "//a[@class='btn btn-info btn-sm pull-right botonnuevo']")
    mensaje_MSJ = Locator(By.XPATH, "//div[@class='flash-notice']")