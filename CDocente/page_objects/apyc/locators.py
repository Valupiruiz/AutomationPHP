from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class ApycLocators:
    CATEGORITA_SEL = Locator(By.ID, "tipo_antecenteId")
    TIPO_ANTECEDENTE_SEL = Locator(By.ID, "categoria")
    RANGO_SEL = Locator(By.ID, "antecedente_cultural_beca_decreto678_filters_rango_mes_id")
    AUSPICIO_SEL = Locator(By.ID, "antecedente_cultural_beca_decreto678_filters_tipo_institucion_id")
    DESCRIPCION_INP = Locator(By.ID, "documentacion_docente_antecedente_descripcion")
    AGREGAR_IMG_BTN = Locator(By.XPATH, "//button[@class='btn btn-primary btn-subir']")
    AGREGAR_BTN = Locator(By.XPATH, "//div[@id='formulario']//div[7]//input[1]")
    ALERT_LBL = Locator(By.XPATH, "//div[@class='notice alert alert-success span10']")
