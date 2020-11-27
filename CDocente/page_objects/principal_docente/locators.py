from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class PrincipalDocenteLocators:
    MENU_TEMP_BTN = Locator(By.XPATH, "//a[contains(text(),'{menu}')]")
    PERIODO_INSCR_BTN = Locator(By.XPATH, "//a[@class='btn btn-link']")


