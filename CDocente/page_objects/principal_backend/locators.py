from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class PrincipalBackendLocators:
    MENU_TEMP_BTN = Locator(By.XPATH, "//a[contains(text(),'{menu}')]")
    MENU_DOC_BUSCADOR_BTN = Locator(By.XPATH, "//li[@id='buscar_docentes']//a[contains(text(),'Buscador')]")
    SIST_LBL = Locator(By.XPATH, "//h3[contains(text(),'Sistema de Clasificación Docente')]")
    