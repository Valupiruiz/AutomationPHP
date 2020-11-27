from src.web.page_objects.base_page import BasePage
from src.web.page_objects.login.locators import LoginLocators


class ExamplePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = LoginLocators()




