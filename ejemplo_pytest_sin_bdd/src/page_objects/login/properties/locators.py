from selenium.webdriver.common.by import By

from src.page_objects.base.base_page import Locator


class MensajesLocators:
    MensajeDNIObligatorio = Locator(By.XPATH, "//input[@name='idNumber']//parent::div//parent::div//p")
    MensajeMailObligatorio = Locator(By.ID, "inputMail-helper-text")
    MensajePassObligatorio = Locator(By.ID, "inputPassword-helper-text")
    MensajeCorreoInvalido = Locator(By.XPATH, "//p[@id='txtMailRecover-helper-text']")
    MensajeCorreoRecuperar = Locator(By.XPATH, "//p[@id='txtMailRecover-helper-text']")
    MensajeCorreoInvalidoLogin = Locator(By.ID, "inputMail-helper-text")
    MensajeCredencialesInvalidas = Locator(By.CSS_SELECTOR, "div.alert-danger")
    MensajeEnvioCorreo = Locator(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]")


class OlvidoContrasena:
    Link = Locator(By.ID, "linkForgot")
    Correo = Locator(By.XPATH, "//input[@id='txtMailRecover']")
    BotonEnviar = Locator(By.CSS_SELECTOR, "#btnConfirmarRecuperarPassword")


class LoginLocators(MensajesLocators, OlvidoContrasena):
    Dni = Locator(By.ID, "inputDni")
    Mail = Locator(By.ID, "inputMail")
    Pass = Locator(By.ID, "inputPassword")
    CheckCaptcha = Locator(By.ID, "recaptcha-anchor")
    TildeCaptcha = Locator(By.CSS_SELECTOR, ".recaptcha-checkbox-checked")
    FRAME = Locator(By.TAG_NAME, "iframe")
    Enviar = Locator(By.ID, "btnIniciarSesion")
