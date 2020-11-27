from selenium.webdriver.common.by import By
from page_objects.base_page import Locator
import time
from config.parameters import Parameters

class JudicialesLocators:
    menu_avisos_BTN = Locator(By.XPATH, "//a[contains(text(),'Avisos')]")
    juzgado_BTN = Locator(By.XPATH, "//div[@id='TramitesAdminSearchType_organismoJudicial_chosen']//span[contains(text(),'Seleccione...')]")
    jugzado_INP = Locator(By.XPATH, "//div[@id='TramitesAdminSearchType_organismoJudicial_chosen']//input[@class='chosen-search-input']")
    buscar_BTN = Locator(By.XPATH, "//button[@class='btn btn-sm btn-primary']")
    usuario_INP = Locator(By.ID, "username")
    pass_INP = Locator(By.ID, "password")
    ingresar_BTN = Locator(By.XPATH, "//button[@class='btn btn-primary']")
    pagar_BTN = Locator(By.XPATH, "//i[contains(@class,'fas fa-dollar-sign')]")
    mensaje_LBL = Locator(By.XPATH, "//div[@class='flash-success']")
    pagar_modal_BTN = Locator(By.XPATH, "//button[contains(@class,'btn btn-success btn-sm')]")



