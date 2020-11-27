from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class CertificadoLocator:
    LEGAJO_SI_INP = Locator(By.ID, "siObra")
    LEGAJO_NO_INP = Locator(By.ID, "noObra")
    ANIO_SEL = Locator(By.ID, "anio_presentacion")
    FECHA_CERTIF_INP = Locator(By.ID, "fecha_certificado")
    FECHA_CERTIF_TITTLE = Locator(By.XPATH, "//label[contains(text(),'Fecha de emisión del certificado')]")
    AGREGAR_IMG_BTN = Locator(
        By.XPATH, "//form[@id='form_AgregarAntecente']//button[@class='btn btn-primary btn-subir']"
                  "[contains(text(),'Agregar')]"
    )
    TERMIN_CONDIC_INP = Locator(By.ID, "readConfirm")
    ACEPTAR_BTN = Locator(By.ID, "btn_aceptar")
    ACEPTAR_ADV_BTN = Locator(By.ID, "pop_aceptarConfirmacion")
    ALERT_SPAN = Locator(By.XPATH, "//div[@class='notice alert alert-success span10']")

