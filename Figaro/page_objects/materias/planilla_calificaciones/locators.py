from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class PlanillaLocators:
    CALIFICACION_TEMP = Locator(
        By.XPATH, '//td[contains(@title, "Alumno: {alumno}") and contains(@title, "Evaluación: {evaluacion}")]'
    )
    PROMEDIO_TEMP = Locator(
        By.XPATH, '//td[contains(@title, "Alumno: {alumno}") and contains(@title, "{tipo}") and contains(@title, "{periodo}")]'
    )
    TITULO_MODAL_LB = Locator(By.XPATH, "//h2[@id='myModalLabel']")
    NOTA_INP = Locator(By.ID, "nota")
    TITULO_PLANILLA_LB = Locator(By.XPATH, "//div[@class='dato']")
    AUSENTE_CHK = Locator(By.XPATH, "//input[@type='checkbox']")
    CERRAR_BTN = Locator(By.XPATH, "//a[contains(text(),'Cerrar')]")
