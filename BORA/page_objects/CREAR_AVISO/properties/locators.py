from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class NuevoAvisoLocators:
    avisos_BTN = Locator(By.XPATH, "//a[@class='puntero'][contains(text(),'Avisos')]")
    ingreso_manual_BTN = Locator(By.ID, "ingreso_manual_li")
    seccion_SEL = Locator(By.ID, "_seccion")
    opcion_default_OPT = Locator(By.XPATH, "//select[@id='_rubro']//option[contains(text(), '--Seleccionar--')]")
    rubro_SEL = Locator(By.ID, "_rubro")
    tipo_aviso_SEL = Locator(By.ID, "_tipoDeAviso")
    modalidad_pago_SEL =Locator(By.ID, "AvisoType_modalidadPago")
    fecha_publicacion_INP =Locator(By.ID, "AvisoType_fechaPublicacion")
    cant_dias_INP =Locator(By.ID, "AvisoType_cantDiasAviso")
    texto_CLICK = Locator(By.XPATH, "//div[@class='note-editable panel-body']")
    texto_TEXT=Locator(By.CSS_SELECTOR, "//div[@class='note-editable panel-body']//p")
    documento_ADJ = Locator(By.XPATH, "//input[@id='AvisoType_documentoAviso']")
    fecha_admin_INP = Locator(By.ID, "AvisoType_fechaFirmaActoAdministrativo")
    organismo_CONTAINER = Locator(By.ID, "organismo")
    origen_SEL = Locator(By.ID, "AvisoType_sistemaOrigen")
    organismo_SEL = Locator(By.ID, "AvisoType_organismo")
    dependencia_SEL = Locator(By.ID, "AvisoType_dependencia")
    subdependencia_SEL =Locator(By.ID, "AvisoType_subDependenciaBora")
    titulo_INP = Locator(By.ID, "AvisoType_titulo")
    guardar_BTN = Locator(By.ID, "guardar")
    mensaje_MSJ =Locator(By.XPATH, "//div[@class='flash-notice']")
    opcion_default_orga_OPT = Locator(By.XPATH, "//select[@id='AvisoType_organismo']//option[contains(text(),'--Seleccionar--')]")

    def verificacion_aviso(self,idAviso):
        return Locator(By.ID, "//td[contains(text(),'"+idAviso+"')] / parent::tr // a")


