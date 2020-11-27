from selenium.webdriver.common.by import By
from src.web.page_objects.base_page import Locator


class SponsorsLocator:
    #LISTADO
    CREAR_BTN = Locator(By.XPATH, "//button[@class='btn btn-success float-right']")

    #CREAR SPONSOR
    TIPO_SEL = Locator(By.XPATH, "//select[@id='AdvertisingSponsorType_typeAdvertisingSponsor']")
    FECHA_DESDE_INP = Locator(By.XPATH, "//input[@id='AdvertisingSponsorType_sinceDate']")
    FECHA_HASTA_INP = Locator(By.XPATH, "//input[@id='AdvertisingSponsorType_toDate']")
    NOMBRE_INP = Locator(By.XPATH, "//input[@id='AdvertisingSponsorType_title']")
    LINK_INP = Locator(By.XPATH, "//input[@id='AdvertisingSponsorType_link']")
    INTERESES_SEL = Locator(By.XPATH, "//select[@id='AdvertisingSponsorType_interests']")
    ZONAS_SEL = Locator(By.XPATH, "//select[@id='AdvertisingSponsorType_zones']")
    GUARDAR_BTN = Locator(By.XPATH, "//button[@class='btn btn-primary']")
