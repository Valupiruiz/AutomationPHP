from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class NuevaInscripcionLocators:
    AREA_SEL = Locator(By.ID, "area")
    CARGO_SEL = Locator(By.ID, "cargo")
    ASIGNATURA_SEL = Locator(By.ID, "asignatura")
    ESPECIALIDAD_SEL = Locator(By.ID, "especialidad")
    AGREGAR_BTN = Locator(By.ID, "btn_agregar")
    MENSAJE_SPAN = Locator(By.XPATH, "//div[@class='notice alert alert-success span10']")
    MODAL_CIERRE = Locator(By.XPATH, "//div[contains(@class, 'modal-backdrop')]")
    AGREGAR_MODAL_BTN = Locator(By.XPATH, "//div[@id='dialogo_confirmacion_inscripcion']//input[@id='pop_aceptarConfirmacion']")