from selenium.webdriver.common.by import By
from page_objects.base_page import Locator
import time


class BandejaTramitesLocators:
    MODAL_AVISO_DIV = Locator(By.ID, "content-detalleAviso")
    motivo_rechazo_TXT = Locator(By.XPATH, "//textarea[@id='AvisoVerificacionType_observaciones']")
    mensaje_MSJ = Locator(By.XPATH, "//div[@class='alert alert-success']//div[@class='flash-notice']")
    motivo_rechazo_INP = Locator(By.ID,"RechazarAvisoType_motivoRechazo")
    reprocesar_BTN = Locator(By.XPATH, "//button[contains(text(),'Reprocesar')]")
    cierre_ventana_BTN = Locator(By.XPATH,"//div[@class='modal-dialog modal-lg']//span[contains(text(),'×')]")
    firmante1_TXT = Locator(By.ID, "select2-AvisoVerificacionType_firmantesAvisoActoAdministrativo_0_firmanteActoAdministrativo-container")
    firmante2_TXT = Locator(By.ID, "select2-AvisoVerificacionType_firmantesAvisoActoAdministrativo_1_firmanteActoAdministrativo-container")
    firmante3_TXT = Locator(By.ID, "select2-AvisoVerificacionType_firmantesAvisoActoAdministrativo_2_firmanteActoAdministrativo-container")
    descargar_texto_BTN = Locator(By.XPATH, "//h6[@class='panel-title']//i[@class='fa fa-download text-success']")
    decargar_doc_BTN = Locator(By.XPATH, "//h5[@class='panel-title']//i[@class='fa fa-download text-success']")
    doc_no_existe_LBL = Locator(By.XPATH, "//i[@class='fa fa-exclamation-triangle fa-4x text-danger']")
    dias_INP = Locator(By.ID, "AvisoVerificacionType_cantDiasAviso")
    texto_dias_LBL = Locator(By.XPATH, "//li[contains(text(),'Dias a publicar incorrecto')]")
    texto_fecha_LBL = Locator(By.XPATH, "//li[contains(text(),'Fecha de publicacion requerida')]")
    texto_firma_LBL = Locator(By.XPATH, "//li[contains(text(),'Valor requerido')]")
    guardar_Pend_PUB_BTN = Locator(By.XPATH, "//button[@id='guardarFechaPub']")
    fecha_publicar_INP = Locator(By.ID, "AvisoVerificacionType_fechaPublicacion")
    fecha_firma_INP = Locator(By.ID, "AvisoVerificacionType_fechaFirmaActoAdministrativo")
    apruebo_BTN = Locator(By.XPATH, "//button[@id='aprobarFechaPub']")
    documento_aviso_LBL = Locator(By.XPATH, "//a[@class='documento_title']")
    anio_exp_jub_LBL = Locator(By.XPATH, "//li[contains(text(),'Año expediente judicial requerido')]")
    nro_exp_jud_LBL = Locator(By.XPATH, "//li[contains(text(),'Nro expediente judicial requerido')]")
    ESTADO_AVISO_TEMP = Locator(By.XPATH, "//td[contains(text(),'{id_aviso}')]//following::td[3]")
    REPROCESAR_AVISO_TEMP = Locator(By.XPATH, "//td[contains(text(),'{id_aviso}')]/parent::tr//a")
    titulo_bandeja_LBL = Locator(By.XPATH, "//h3[contains(text(),'Bandeja de trámites')]")
    AVISO_LBL = Locator(By.XPATH, "//h4[@id='myModalLabel']")
    suplemento_SEL = Locator(By.ID, "AvisoVerificacionType_ordenArmadoSuplemento")



    def locator_estado(idAviso):
        return Locator(By.XPATH, "//td[contains(text(),'" + str(idAviso) + "')]//following::td[3]")


    def locator_reprocesar(idAviso):
        return Locator(By.XPATH,"//td[contains(text(),'" + str(idAviso) + "')]/parent::tr//a")




