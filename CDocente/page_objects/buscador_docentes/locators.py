from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class BuscadorDocentesLocators:
    NOMBRE_INP = Locator(By.ID, "docente_filters_nombre")
    APELLIDO_INP = Locator(By.ID, "docente_filters_apellido")
    T_DOC_SEL = Locator(By.ID, "docente_filters_tipo_documento_id")
    NRO_DOC_INP = Locator(By.ID, "docente_filters_numero_documento")
    EMAIL_INP = Locator(By.ID, "docente_filters_email")
    BUSCAR_BTN = Locator(By.XPATH, "//input[@class='btn btn-gcba'][@value='Buscar']")
    VALIDAR_TEMP_BTN = Locator(By.XPATH, "//td[contains(text(),'{mail}')]/parent::tr//a[@title='Validar']")


