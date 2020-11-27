from selenium.webdriver.common.by import By
from page_objects.base_page import Locator
import time


class OrganismosJudicialesLocators:
    nuevo_orga_BTN = Locator(By.XPATH, "//a[@class='btn btn-info btn-sm pull-right botonnuevo']")
    nombre_orga_INP = Locator(By.ID, "OrganismoJudicialType_nombre")
    cuit_orga_INP = Locator(By.ID, "OrganismoJudicialType_cuit")
    calle_orga_INP = Locator(By.ID, "OrganismoJudicialType_calle")
    provincia_orga_SPAN = Locator(By.XPATH,"//span[contains(text(),'--Provincia--')]")
    partido_orga_INP = Locator(By.ID, "OrganismoJudicialType_partido")
    localidad_orga_INP = Locator(By.ID, "OrganismoJudicialType_localidad")
    num_orga_INP = Locator(By.ID, "OrganismoJudicialType_numero")
    secretaria_BTN = Locator(By.XPATH, "//a[@class='collapsed'][contains(text(),'Nueva secretaria')]")
    cod_postal_orga_INP = Locator(By.ID, "OrganismoJudicialType_codigoPostal")
    nombre_SEC_INP = Locator(By.ID, "OrganismoJudicialType_secretarias_0_nombre")
    cuit_SEC_INP = Locator(By.ID, "OrganismoJudicialType_secretarias_0_cuit")
    activo_SEC_CHK = Locator(By.ID, "OrganismoJudicialType_secretarias_0_activo")
    calle_SEC_INP = Locator(By.ID, "OrganismoJudicialType_secretarias_0_calle")
    numero_SEC_INP = Locator(By.ID, "OrganismoJudicialType_secretarias_0_numero")
    cod_postal_SEC_INP = Locator(By.ID, "OrganismoJudicialType_secretarias_0_codigoPostal")
    partido_SEC_INP = Locator(By.ID, "OrganismoJudicialType_secretarias_0_partido")
    localidad_SEC_INP = Locator(By.ID, "OrganismoJudicialType_secretarias_0_localidad")
    nombre_REP_INP = Locator(By.ID, "OrganismoJudicialType_secretarias_0_representantes_0_nombre")
    apellido_REP_INP = Locator(By.ID, "OrganismoJudicialType_secretarias_0_representantes_0_apellido")
    cuil_REP_INP = Locator(By.ID, "OrganismoJudicialType_secretarias_0_representantes_0_cuil")
    telefono_REP_INP = Locator(By.ID, "OrganismoJudicialType_secretarias_0_representantes_0_telefono")
    mail_REP_INP = Locator(By.ID, "OrganismoJudicialType_secretarias_0_representantes_0_mail")
    cargo_REP_INP = Locator(By.ID, "OrganismoJudicialType_secretarias_0_representantes_0_cargo")
    usuario_REP_INP = Locator(By.ID, "OrganismoJudicialType_secretarias_0_representantes_0_username")
    activo_REP_CHK = Locator(By.ID, "OrganismoJudicialType_secretarias_0_representantes_0_activo")
    op_1_PROV_ORGA = Locator(By.XPATH, "//div[@id='modalneweditorg']//li[2]//label[1]")
    provincia_SEC_SEL = Locator(By.ID, "OrganismoJudicialType_secretarias_0_provincia")
    nuevo_repres_BTN = Locator(By.XPATH, "//a[contains(text(),'Nuevo representante')]")
    guardar_BTN = Locator(By.XPATH,"//button[@id='guardar']")
    mensaje_MSJ = Locator(By.XPATH, "//div[@class='alert alert-success']")



