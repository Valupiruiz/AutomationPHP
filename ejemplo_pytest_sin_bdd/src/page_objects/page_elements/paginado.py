from selenium.common.exceptions import TimeoutException

from src.page_objects.base.base_page import BasePage
from src.page_objects.page_elements.properties.locators import PaginadoLocators


class PaginadoPageElement:

    def __init__(self, parent):
        self.__locators = PaginadoLocators
        self.parent: BasePage = parent

    def go_to(self, number):
        self.parent.find_element(self.__locators.PAGINA.format_locator(number)).click()

    def current(self):
        return self.parent.get_element_text(self.__locators.ACTUAL)

    def total(self):
        return len(self.parent.find_elements(self.__locators.PAGINAS, 5))

    def search(self, func):
        val = None

        for page in range(1, self.total() + 1):
            self.go_to(page)
            try:
                val = func()
                break
            except TimeoutException:
                continue
        if val is not None:
            return val
        raise Exception("No se encontro el resultado")

