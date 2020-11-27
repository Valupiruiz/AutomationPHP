from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class ver_documentacion:
    ACCORDION_BTN = Locator(By.XPATH, "//a[@class='accordion-toggle'][contains(text(),'{Listado}')]")
    NUEVO_TITULO_BTN = Locator(By.XPATH, "//div[@id='collapse1']//a[@class='btn btn-success']")
    NUEVO_CURSO_BTN = Locator(By.XPATH, "//div[@id='collapse2']//a[@class='btn btn-success']")
    NUEVO_ANTECEDENTES_BTN = Locator(By.XPATH, "//div[@id='collapse3']//a[@class='btn btn-success']")
    NUEVO_OTROS_ANTECEDENTES_BTN = Locator(By.XPATH, "//div[@id='collapse4']//a[@class='btn btn-success']")
    NUEVO_CERTIFICADOR_BTN = Locator(By.XPATH, "//div[@id='collapse5']//a[@class='btn btn-success']")






