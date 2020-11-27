from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class LoginLocators:
    INGRESAR_BTN = Locator(By.XPATH, "//span[@class='btn btn-primary']")
    INGRESAR_FIGARO_LBL = Locator(By.XPATH, "//h4[contains(text(),'Ingresar a Figaro')]")
    INSTITUCION_SEL = Locator(By.ID, "selectorInstitucion")
    USUARIO_INP = Locator(By.ID, "signin_username")
    PASS_INP = Locator(By.ID, "signin_password")
    INGRESAR_SUBMIT_BTN = Locator(By.ID, "signin_submit")
    MANZANA_LOADER_IMG = Locator(By.XPATH, "//div[@id='opcionesLogin']//div//img")
