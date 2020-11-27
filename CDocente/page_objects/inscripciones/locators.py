from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class InscripcionesLocators:
    NUEVA_INSC_BTN = Locator(By.XPATH, "//a[@class='btn btn-success']")