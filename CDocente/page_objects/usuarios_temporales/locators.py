from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class UsuariosTemporalesLocator:
    #DATOS PERSONALES
    NUM_DOC_INP = Locator(By.ID, "docente_filters_numero_documento")
    BUSCAR_BTN = Locator(By.XPATH, "//input[@value='Buscar']")
    HABILITAR_USU_TEMP = Locator(By.XPATH, "//td[contains(text(),'{mail}')]/parent::tr//a[@title='Habilitar']")
    EDITAR_USU_TEMP = Locator(By.XPATH, "//td[contains(text(),'{mail}')]/parent::tr//a[@title='Editar']")
    ACEPTAR_BTN = Locator(By.ID, "btn_aceptar_confirm")
    ALERT_LBL = Locator(By.XPATH, "//div[@class='notice alert alert-success span10']")
    MAIL_FILTRO_INP = Locator(By.ID, "usuario_filters_email")
    MAIL_INP = Locator(By.ID, "usuario_email")
    MAIL_REPEAT_INP = Locator(By.ID, "usuario_email_again")
    GUARDAR_BTN = Locator(By.XPATH, "//input[@value='Guardar']")
