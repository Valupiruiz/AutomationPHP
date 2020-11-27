from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class UsuarioBueLocators:
    #DATOS PERSONALES
    NUM_DOC_INP = Locator(By.ID, "docente_filters_numero_documento")
    BUSCAR_BTN = Locator(By.XPATH, "//input[@value='Buscar']")
    DESHABILITAR_USU_TEMP = Locator(By.XPATH, "//td[contains(text(),'{dni}')]/parent::tr//a[@title='Deshabilitar']")
    HABILITAR_USU_TEMP = Locator(By.XPATH, "//td[contains(text(),'{dni}')]/parent::tr//a[@title='Habilitar']")
    ACEPTAR_BTN = Locator(By.ID, "btn_aceptar_confirm")
    ALERT_LBL = Locator(By.XPATH, "//div[@class='notice alert alert-success span10']")
    BUSC_MAIL_INP = Locator(By.ID, "usuario_filters_email")
    EDITAR_USU_TEMP = Locator(By.XPATH, "//td[contains(text(),'{mail}')]/parent::tr//a[@title='Editar']")
    MAIL_EDU_INP = Locator(By.ID, "usuario_email")
    DNI_INP = Locator(By.ID, "docente_numero_documento")
    GUARDAR_BTN = Locator(By.XPATH, "//input[@value='Guardar']")

