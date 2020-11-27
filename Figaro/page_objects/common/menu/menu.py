from page_objects.base_page import BasePage
from page_objects.common.menu.locators import MenuLocators
from page_objects.materias.imaterias import MateriaStrategy
from typing import Any


class Menu(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = MenuLocators()

    def dirigirse_a_solapa(self, nombre_tab: str) -> Any:
        locator = self.__locators.SOLAPA_MENU_LBL.formatear_locator({"solapa": nombre_tab})
        self.find_element(locator).click()
        return next_[nombre_tab]


next_ = {
    "Materias": MateriaStrategy
    # "Home": MenuLocators.HOME_LBL
}
