from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class TitulosLocators:
    #Buscador de titulos
    BUSCADOR_BTN = Locator(By.XPATH, "//input[@value='Abrir buscador de títulos']")
    NIVEL_SEL = Locator(By.ID, "nivel_titulo")
    TITULO_INP = Locator(By.ID, "resolucion_titulo_filters_titulo_filters_descripcion")
    PROCEDENCIA_INP = Locator(By.ID, "resolucion_titulo_filters_titulo_filters_procedencia_id")
    RESOLUCION_INP = Locator(By.ID, "resolucion_titulo_filters_descripcion")
    AGREGAR_TEMP_BTN = Locator(By.XPATH, "//div[@id='DivBuscador']/table/tbody/tr[td[1][normalize-space(text())='{titulo}']]/td[4]/a")
    BUSCAR_BTN = Locator(By.XPATH, "//input[@value='Buscar']")
    ALERT_SPAN = Locator(By.XPATH, "//div[@class='notice alert alert-success span10']")
    SIN_SECUNDARIO_CHK = Locator(By.ID, "no_requiere_secundario")
    ACEPTAR_SIN_SEC_BTN = Locator(By.ID, "btn_agregarNivel")