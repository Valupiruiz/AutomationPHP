from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class LoginLocators:
    usuario_INP = Locator(By.ID, "username")
    password_INP = Locator(By.ID, "password")
    ingreso_manual_BTN = Locator(By.CSS_SELECTOR, "button.btn.btn-primary")
