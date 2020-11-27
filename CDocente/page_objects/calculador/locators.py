from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class CalculadorLocators:
    NUEVO_PROCESO_BTN = Locator(By.ID, "btn_cp")
    PERIODO_SEL = Locator(By.ID, "control_calculador_periodo_id")
    CALCULADOR_ARCHIVO_BTN = Locator(By.ID, "control_calculador_archivo")
    CORRER_PROCESO_BTN = Locator(By.ID, "ejecutarProcesoCalculo")
    ALERT_LBL = Locator(By.XPATH, "//div[@class='notice alert alert-success span10']")
