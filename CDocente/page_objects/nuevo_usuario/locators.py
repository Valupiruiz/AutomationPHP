from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class NuevoUsuarioLocators:
    #DATOS PERSONALES
    NOMBRE_INP = Locator(By.ID, "docente_nombre")
    APELLIDO_INP = Locator(By.ID, "docente_apellido")
    FECHA_NACIMIENTO_INP = Locator(By.ID, "docente_fecha_nacimiento")
    SEXO_SEL = Locator(By.ID, "docente_sexo_id")
    T_DOCUMENTO_SEL = Locator(By.ID, "docente_tipo_documento_id")
    NRO_DOCUMENTO_INP = Locator(By.ID, "docente_numero_documento")
    NRO_DOCUMENTO_AGAIN_INP = Locator(By.ID, "docente_numero_documento_again")
    IMAGEN_DOCUMENTO_BTN = Locator(By.XPATH, "//div[@class='controls dni']//button[@class='btn btn-subir'][contains(text(),'Agregar')]")
    CUIL_INP = Locator(By.ID, "docente_cuil")
    IMAGEN_CUIL_BTN = Locator(By.XPATH, "//div[@class='controls cuil']//button[@class='btn btn-subir'][contains(text(),'Agregar')]")

    #DIRECCION
    PROVINCIA_SEL = Locator(By.ID, "docente_provincia_id")
    LOCALIDAD_SEL = Locator(By.ID, "docente_localidad_id")
    CALLE_NRO_INP = Locator(By.ID, "docente_domicilio")
    PISO_INP = Locator(By.ID, "docente_piso")
    DEPARTAMENTO_INP = Locator(By.ID, "docente_departamento")
    COD_POSTAL_INP = Locator(By.ID, "docente_codigo_postal")

    #EMAIL Y CONTRASEÑA
    MAIL_INP = Locator(By.ID, "usuario_email")
    MAIL_AGAIN_INP = Locator(By.ID, "usuario_email_again")
    PASS_INP = Locator(By.ID, "usuario_password")
    PASS_AGAIN_INP = Locator(By.ID, "usuario_password_again")
    TERM_CONDIC_CHECK = Locator(By.ID, "docente_politicas")

    GUARDAR_BTN = Locator(By.XPATH, "//input[@value='Guardar']")
    REGISTRARSE_BTN = Locator(By.XPATH, "//input[@value='Registrarse']")

    ALERT_SPAN = Locator(By.XPATH, "//div[@class='notice alert alert-success span10']")




