from selenium.webdriver.common.by import By

from src.page_objects.base.base_page import Locator


class ConfiguracionLocators:
    ConfigSucursal = Locator(By.ID, "linkConfiguracionSucursales")
