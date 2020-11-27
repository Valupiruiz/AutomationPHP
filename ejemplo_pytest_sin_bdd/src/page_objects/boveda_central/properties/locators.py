from selenium.webdriver.common.by import By

from src.page_objects.base.base_page import Locator


class BovedaNoAsociadaLocators:
    LBL_MENSAJE = Locator(By.CSS_SELECTOR, "h3 > b")
