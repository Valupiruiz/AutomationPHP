import datetime
from page_objects.base_page import BasePage
import calendar


class DateUtils:
    def __init__(self, dia=None, mes=None, anio=None):
        """
        Constructor para la clase. Por defecto se carga la fecha de hoy, si es que no, se le pasan parametros,
        sino crea un objeto de tipo datetime
        Args:
            dia: dia
            mes: mes
            anio: año
        """
        if all(i is not None for i in [dia, mes, anio]):
            self.fecha = datetime.datetime(int(anio), int(mes), int(dia))
        elif any(i is not None for i in [dia, mes, anio]):
            print("No completaste todos los campos (dia, mes y anio)")
        else:
            self.fecha = datetime.datetime.now()

    @staticmethod
    def set_date(dia, mes, anio) -> datetime:
        return DateUtils(dia, mes, anio)


class DatePicker(BasePage):
    import locale
    locale.setlocale(locale.LC_TIME, 'es-AR')

    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = DatePickerLocators()

    def seleccionar_fecha(self, date: datetime.datetime):
        day_texto_switcher = self.find_element(self.__locators.SWITCHER_TEMPLATE).text
        if day_texto_switcher == f"{calendar.month_name[date.month].capitalize()} {str(date.year)}":
            self.__seleccionar_dia(date.day)
            return
        self.find_element(self.__locators.SWITCHER_TEMPLATE).click()
        month_texto_switcher = self.find_element(self.__locators.SWITCHER_TEMPLATE).text
        if month_texto_switcher == str(date.year):
            self.__seleccionar_mes(date.month)
            self.__seleccionar_dia(date.day)
            return
        # TODO: años y decadas
        # self.find_element(self.__locators.SWITCHER_TEMPLATE).click()
        # year = self.find_element(self.__locators.SWITCHER_TEMPLATE).text

    def __seleccionar_dia(self, dia):
        dia_formateado = self.__locators.DAY_TEMPLATE.formatear_locator({"dia": str(dia)})
        self.find_element(dia_formateado).click()

    def __seleccionar_mes(self, mes: int):
        mes_for_select = calendar.month_abbr[mes].capitalize().replace('.', '')
        mes_formateado = self.__locators.MONTH_TEMPLATE.formatear_locator({"mes": str(mes_for_select)})
        self.find_element(mes_formateado).click()

    def __seleccionar_anio(self, anio):
        # TODO: algun dia...hacerlo
        pass


class DatePickerLocators:
    from selenium.webdriver.common.by import By
    from page_objects.base_page import Locator
    SWITCHER_TEMPLATE = Locator(By.XPATH, '//div[contains(@class,"datepicker")]//div[@style="display: block;" or @style=""]//th[@class="datepicker-switch"]')
    ANTERIOR_TH = Locator(By.XPATH, '//div[contains(@class,"datepicker")]//div[@style="display: block;"]//th[@class="prev"]')
    DAY_TEMPLATE = Locator(By.XPATH, '//tr//td[@class="day" and text()="{dia}"]')
    MONTH_TEMPLATE = Locator(By.XPATH, '//tr//td//span[@class="month" and text()="{mes}"]')
    ANIO_ACTIVO = Locator(By.XPATH, "//span[@class='year active']")
    ANIO_TEMPLATE = Locator(By.XPATH, '//tr//td//span[@class="year"] and text()="{anio}"')



