from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class LoginGoogleLocators:
    EMAIL_INP = Locator(By.ID, "identifierId")
    SIGUIENTE_BTN = Locator(By.XPATH, "//span[contains(text(),'Siguiente')]/parent::button")
    PASS_INP = Locator(By.XPATH, "//input[@type='password']")
    PAGINA_ANTERIOR_LNK = Locator(By.LINK_TEXT, "http://cdocentep1.cysonline.com.ar:10001/index.php/login")
    CUENTA_DIV = Locator(By.XPATH, "//div[@data-identifier='{mail}']")
    INICIO_BTN = Locator(By.XPATH, "//li[@id='inicio']")
    USAR_OTRA_CUENTA_DIV = Locator(By.XPATH, "//div[contains(text(),'Usar otra cuenta')]")
    SIST_LBL = Locator(By.XPATH, "//h3[contains(text(),'Sistema de Clasificación Docente')]")

