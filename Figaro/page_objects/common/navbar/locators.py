from page_objects.base_page import Locator
from selenium.webdriver.common.by import By


class NavbarLocators:
    NOMBRE_LBL = Locator(By.CLASS_NAME, 'nombre')
    NIVEL_LBL = Locator(By.CLASS_NAME, 'nivel')
    CICLO_SEL = Locator(By.ID, "ciclo_id")
    USUARIO_ANC = Locator(By.CSS_SELECTOR, "a.dropdown-toggle.sesion.pull-right")
    SUB_COLEGIO_USR_SEL = Locator(By.ID, "selectPerfilBloqueUsuario")
    SUB_COLEGIO_USR_LBL = Locator(By.ID, "select2-selectPerfilBloqueUsuario-container")
    CERRAR_SESION_LNK = Locator(By.XPATH, "//a[@class='text-danger pull-right']")
