from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class CuartaLocators:
    id_dominio_INP = Locator(By.ID, "AvisosCuartaGeneralType_avisosCuarta_0_idDominio")
    dominio_INP = Locator(By.ID, "AvisosCuartaGeneralType_avisosCuarta_0_dominio")
    titular_INP = Locator(By.ID, "AvisosCuartaGeneralType_avisosCuarta_0_titular")
    tipo_operacion_SEL = Locator(By.ID, "AvisosCuartaGeneralType_avisosCuarta_0_tipoDoc")
    nro_doc_INP = Locator(By.ID, "AvisosCuartaGeneralType_avisosCuarta_0_nroDocumento")
    qr_INP = Locator(By.ID, "AvisosCuartaGeneralType_avisosCuarta_0_linkQr")
    tipo_op_SEL = Locator(By.ID, "AvisosCuartaGeneralType_avisosCuarta_0_tipoOperacion")
    rubro_SEL = Locator(By.ID, "AvisosCuartaGeneralType_avisosCuarta_0_rubroCuarta")
    agregar_BTN = Locator(By.XPATH, "//i[@class='fa fa-plus']")
    tipo_documento_SEL = Locator(By.ID, "AvisosCuartaGeneralType_avisosCuarta_0_tipoDoc")
    guardar_BTN = Locator(By.XPATH, " //button[@id='guardar']")

