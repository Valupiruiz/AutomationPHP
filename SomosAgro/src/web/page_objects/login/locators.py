from selenium.webdriver.common.by import By
from src.web.page_objects.base_page import Locator


class LoginLocators:
    USUARIO_INP = Locator(By.ID, "username")
    PASSWORD_INP = Locator(By.ID, "password")
    INGRESAR_INP = Locator(By.XPATH, "//button[@class='btn btn-md btn-primary']")
