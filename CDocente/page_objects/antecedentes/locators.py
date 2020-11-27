from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class AntecedentesLocators:
    CATEGORIA_SEL = Locator(By.ID, "tipo_antecenteId")
    TIPO_ANTECEDENTE_SEL = Locator(By.ID, "categoria")
    LIBRO_RANGO_SEL = Locator(By.ID, "antecedente_pedagogico_libro_decreto678_filters_rango_ejemplar_id")
    LIBRO_CANT_AUT_INP = Locator(By.ID, "documentacion_docente_antecedente_cantidad_autores")
    AGREGAR_BTN = Locator(By.XPATH, "//input[@class='btn btn-gcba'][@value='Agregar']")
    ALERTA_LBL = Locator(By.XPATH, "//div[@class='notice alert alert-success span10']")