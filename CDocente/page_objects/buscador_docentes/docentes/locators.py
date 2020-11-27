from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class DatosDocentesLocators:
    PUNTOS_APROBAR_DOC_BTN = Locator(By.XPATH, "//div[@class='controls']//i[@class='fa fa-ellipsis-h']")
    APROBAR_DOC_BTN = Locator(By.XPATH, "//div[@id='accionesDocumento']//a[contains(text(),'Aprobar')]")
    SOLAPA_TEMP_BTN = Locator(By.XPATH, "//a[contains(text(),'{solapa}')]")
    FLECHA_VALID_TITULO_BTN = Locator(By.XPATH, "//td[contains(text(),'{titulo}')]/parent::tr//i[@class=' icon-chevron-down icon-white']")
    FLECHA_VALID_APYC_BTN = Locator(By.XPATH, "//td[contains(text(),'{categoria}')]//following-sibling::td[contains(text(),'Rango {rango} | Auspicio {tipo_institucion}')]/parent::tr//i[@class=' icon-chevron-down icon-white']")
    APROBAR_TITULO_BTN = Locator(By.XPATH, "//div[@id='collapse1']//div[@class='accordion-inner']//div//a[contains(text(),'Aprobar')]")
    APROBAR_APYC_BTN = Locator(By.XPATH, "//div[@id='collapse3']//div[@class='accordion-inner']//div//a[contains(text(),'Aprobar')]")
    ACCORDION_BTN = Locator(By.XPATH, "//a[@class='accordion-toggle'][contains(text(),'{Listado}')]")
    ACEPTAR_TITULO_BTN = Locator(By.ID, "btn_aprovarTitulo")
    ESTADO_TITULO_TEMP = Locator(By.XPATH, "//td[contains(text(),'{titulo}')]//following::td[5]")
    TITULO_TRAMITE_FALSE = Locator(By.ID, "noTituloEnTramite")
    CARGA_ESTADO_LBL = Locator(By.XPATH, "//th[contains(text(),'Estado')]")
    MODAL_APROBACION_TITULO_ = Locator(By.ID, "dialogoAprobarTitulo")
