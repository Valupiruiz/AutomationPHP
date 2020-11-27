from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class CursosLocators:
    #BUSCADOR DE CURSOS
    ABRIR_BUSCADOR_BTN = Locator(By.XPATH, "//div[@id='DivListado']//input[1]")
    CURSO_INP = Locator(By.ID, "resolucion_curso_filters_descripcion")
    INSTITUCION_INP = Locator(By.ID, "resolucion_curso_filters_curso_filters_institucion_id")
    RESOLUCION_INP = Locator(By.ID, "resolucion_curso_filters_curso_filters_descripcion")
    BUSCAR_BTN = Locator(By.XPATH, "//input[@value='Buscar']")

    AGREGAR_CURSO_TEMP_BTN = Locator(By.XPATH, "//td[contains(text(),'{curso}')]/parent::tr//a")
    ALERT_LBL = Locator(By.XPATH, "//div[@class='notice alert alert-success span10']")

