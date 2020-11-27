from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class PaginaPrincipalLocators:
    CUENTAS_BUE_BTN = Locator(By.XPATH, "//div[@class='row-fluid']//a[@class='btn btn-gcba'][contains(text(),'Cuenta @bue.edu.ar')]")
    USUARIO_TEMPORAL_BTN = Locator(By.XPATH, "//div[@class='row-fluid']//input[@type='button'][@value='Usuario temporal']")
    NUEVO_USURIO_BTN = Locator(By.XPATH, "//div[@class='row-fluid']//a//i[@class='icon-white icon-plus']")
