from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class LoginBackendLocators:
    INGRESAR_BUE = Locator(By.XPATH, "//a[contains(text(), 'Ingresar con @bue')]")
