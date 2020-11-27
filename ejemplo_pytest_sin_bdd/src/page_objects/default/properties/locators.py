from selenium.webdriver.common.by import By

from src.page_objects.base.base_page import Locator


class DefaultLocators:
    LBL_CAJA = Locator(By.CSS_SELECTOR, ".text-black-50")
    BTN_CONFIGURACION = Locator(By.ID, "linkConfiguracion")
