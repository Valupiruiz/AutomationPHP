from selenium.webdriver.common.by import By
from src.web.page_objects.base_page import Locator


class MenuLocators:
    MENU_TEMP = Locator(By.XPATH, "//a[contains(text(),'{menu}')]")
    CERRAR_SESION_BTN = Locator(By.XPATH, "//ul[@class='navbar-nav ml-auto']//a[@class='nav-link']")

