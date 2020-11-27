from selenium.webdriver.common.by import By
from src.web.page_objects.base_page import Locator


class PublicacionesLocators:
    #LISTADO
    CREAR_PUBLICACION_BTN = Locator(By.XPATH, "//button[@class='btn btn-success float-right']")

    #CREAR PUBLICACION
    TIPO_SEL = Locator(By.XPATH, "//select[@id='AdvertisingType_typeAdvertising']")
    DIAS_SEL = Locator(By.XPATH, "//select[@id='AdvertisingType_numberDays']")
    USUARIO_SEL = Locator(By.XPATH, "//select[@id='AdvertisingType_userApp']")
    TITULO_INP = Locator(By.XPATH, "//input[@id='AdvertisingType_title']")
    LINK_INP = Locator(By.XPATH, "//input[@id='AdvertisingType_link']")
    SINTESIS_INP = Locator(By.XPATH, "//input[@id='AdvertisingType_shortDescription']")
    DESCRIPCION_INP = Locator(By.XPATH, "//textarea[@id='AdvertisingType_description']")
    INTERESES_SEL = Locator(By.XPATH, "//select[@id='AdvertisingType_interests']")
    OPCION_INTERESES_SPN = Locator(By.XPATH, "//span[contains(text(),'{interes}')]")
    ZONAS_SEL = Locator(By.XPATH, "//select[@id='AdvertisingType_zones']")
    GUARDAR_BTN = Locator(By.XPATH, "//button[@class='btn btn-primary']")
    FLASH_LBL = Locator(By.XPATH, "//div[@class='flash-success']")
    PUBLICAR_TEMP = Locator(By.XPATH, "//td[contains(text(),'{titulo}')]//following-sibling::td[contains(text(),'{usuario}')]//following-sibling::td//a[@class='btn btn-link d-inline-block cursor-pointer']")
