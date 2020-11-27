from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class DistritoLocators:
    #DATOS PERSONALES
    AREA_SEL = Locator(By.ID, "area")
    APELLIDO_INP = Locator(By.ID, "docente_apellido")
    AREA_TEMP = Locator(By.XPATH, "//td[contains(text(),'{area}')]//following::td[6]//a")
    DISTRITO_TEMP = Locator(By.ID, "d{distrito}")
    GUARDAR_BTN = Locator(By.ID, "guardarSeleccionDistrito")
    ALERT_LBL = Locator(By.XPATH, "//div[@class='notice alert alert-success span10']")