from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class MenuLocators:
    MENU_TEMP = Locator(By.XPATH, "//a[contains(normalize-space(text()), '{menu}')]")
    SUBMENU_TEMP = Locator(By.XPATH, "//a[contains(normalize-space(text()), '{submenu}')][@href='#']")
    CIERRE_SESION_NOMB_BTN = Locator(By.XPATH, "//p[contains(text(),'{nombre_apellido}')]")
    CIERRE_SESION_BTN = Locator(By.XPATH, "// a[contains(text(), 'Cerrar Sesión')]")
    LOGOUT_LBL = Locator(By.XPATH, "//a[contains(text(),'logout')]")