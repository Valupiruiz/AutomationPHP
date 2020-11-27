from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException, \
    ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains as _ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebElement
from typing import List, Tuple

# region Constantes
_DEFAULT_TIMEOUT = 20
_IGNORED_EXCEPTIONS = (StaleElementReferenceException, ElementNotInteractableException, ElementNotVisibleException)


# endregion
# noinspection Py
# region BasePage


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = _DEFAULT_TIMEOUT
        self.wait = WebDriverWait(self.driver, self.timeout, ignored_exceptions=_IGNORED_EXCEPTIONS)

    def get_wait(self, timeout: int) -> WebDriverWait:
        """
        Cuando hay que utilizar un timeout distinto al default, utiliza un wait diferente al del constructor

        Args:
            timeout (int): cantidad de segundos a esperar

        Returns:
            WebDriverWait: objeto de webdriver que sirve para implementar esperas.
        """
        if timeout == _DEFAULT_TIMEOUT:
            return self.wait
        return WebDriverWait(self.driver, timeout, ignored_exceptions=_IGNORED_EXCEPTIONS)

    def find_element(self, locator: "Locator", timeout: int = _DEFAULT_TIMEOUT) -> WebElement:
        """
        Encuentra el elemento definido por locator y ademas lo espera

        Args:
            locator (Locator): objeto que abstrae el elemento a encontrar
            timeout (int): cantidad máxima de tiempo a esperar antes de lanzar una excepción

        Returns:
            WebElement: elemento de webdriver que representa un objeto de la pantalla y sus atributos
        """
        self.__wait_for_element(locator, timeout)
        return self.driver.find_element(*locator.ret_locator)

    def find_elements(self, locator: "Locator", timeout: int = _DEFAULT_TIMEOUT) -> List[WebElement]:
        """
        Encuentra los elementos definidos por locator y ademas los espera

        Args:
            locator (Locator): objeto que abstrae los elementos a encontrar
            timeout (int): cantidad máxima de tiempo a esperar antes de lanzar una excepción

        Returns:
            List[WebElement]: una lista de elementos de webdriver que representan objetos de la pantalla y sus
                atributos
        """
        self.__wait_for_elements(locator, timeout)
        return self.driver.find_elements(*locator.ret_locator)

    def find_select(self, locator: "Locator") -> Select:
        """
        Encuentra un elemento de tipo select definido por locator

        Args:
            locator (Locator): objeto que abstrae el elemento select a encontrar

        Returns:
            Select: un objeto de webdriver que permite seleccionar y deseleccionar valores de un select
        """
        return Select(self.__wait_for_element(locator))

    def __wait_for_element(self, locator: "Locator", timeout: int = _DEFAULT_TIMEOUT) -> WebElement:
        """
        Espera que el elemento este presente e interactuable

        Args:
            locator: objeto que abstrae el elemento a esperar
            timeout: cantidad máxima de tiempo a esperar antes de lanzar una excepción

        Returns:
            WebElement: elemento de webdriver que representa un objeto de la pantalla y sus atributos
        """
        self.wait_until_element_interactable(locator, timeout)
        return self.get_wait(timeout).until(ec.presence_of_element_located(locator.ret_locator),
                                            message=f"No se encontro el elemento {locator.ret_locator}")

    def __wait_for_elements(self, locator: "Locator", timeout: int = _DEFAULT_TIMEOUT) -> List[WebElement]:
        """
        Espera que los elementos esten presentes e interactuables

        Args:
            locator (Locator): objeto que abstrae los elementos a esperar
            timeout (int): cantidad máxima de tiempo a esperar antes de lanzar una excepción

        Returns:
            List[WebElement]: una lista de elementos de webdriver que representan objetos de la pantalla y sus
                atributos
        """
        self.wait_until_elements_interactable(locator, timeout)
        return self.get_wait(timeout).until(ec.presence_of_all_elements_located(locator.ret_locator),
                                            message=f"No se encontro ningun elemento en {locator.ret_locator}")

    def wait_until_element_interactable(self, locator: "Locator", timeout: int = _DEFAULT_TIMEOUT) -> None:
        """
        Espera que un elemento sea interactuable. Es decir, que esté visible y habilitado

        Args:
            locator (Locator): objeto que abstrae el elemento a esperar
            timeout: cantidad máxima de tiempo a esperar antes de lanzar una excepción

        Returns:
            None
        """
        self.get_wait(timeout).until(ec.element_to_be_clickable(locator.ret_locator),
                                     message=f"No se encontro el elemento {locator.ret_locator}")

    def wait_until_elements_interactable(self, locator, timeout=_DEFAULT_TIMEOUT):
        """
        Espera que los elementos sean interactuables. Es decir, que estén visibles y habilitados

        Args:
            locator (Locator): objeto que abstrae los elementos a esperar
            timeout: cantidad máxima de tiempo a esperar antes de lanzar una excepción

        Returns:
            (None)
        """
        self.get_wait(timeout).until(ec.visibility_of_all_elements_located(locator.ret_locator),
                                     message=f"No se encontraron los elementos {locator.ret_locator}")

    def wait_for_check_status(self, locator: "Locator", checked: bool = True, timeout: int = _DEFAULT_TIMEOUT) -> None:
        """
        Espera que un elemento esté tildado (checkeado)

        Args:
            locator (Locator): objeto que abstrae el elemento a esperar
            checked (bool): valor esperado del check
            timeout (int): cantidad máxima de tiempo a esperar antes de lanzar una excepción

        Returns:
            None
        """
        wait = self.get_wait(timeout)
        if checked:
            wait.until(ec.element_located_to_be_selected(locator.ret_locator))
        else:
            wait.until_not(ec.element_located_to_be_selected(locator.ret_locator))

    def wait_for_element_invisibility(self, locator: "Locator", timeout: int = _DEFAULT_TIMEOUT) -> None:
        """
        Espera que el elemento definido por locator este invisible

        Args:
            locator (Locator): objeto que abstrae el elemento a esperar
            timeout (int): cantidad máxima de tiempo a esperar antes de lanzar una excepción

        Returns:
            None
        """
        self.get_wait(timeout).until(ec.invisibility_of_element_located(locator.ret_locator))

    def wait_for_url(self, url: str, timeout: int = _DEFAULT_TIMEOUT) -> None:
        """
        Espera que la URL actual del driver contenga a la url enviada por parámetro

        Args:
            url (str): la URL que esperamos que esté contenida en la del driver
            timeout (int): cantidad máxima de tiempo a esperar antes de lanzar una excepción

        Returns:
            None
        """
        self.get_wait(timeout).until(ec.url_contains(url),
                                     message=f"Esperaba la URL {url} y obtuve {self.driver.current_url}")

    def wait_until_not_url(self, url: str, timeout: int = _DEFAULT_TIMEOUT) -> None:
        """
        Espera que la URL actual del driver no contenga a la url enviada por parámetro

        Args:
            url (str): la URL que esperamos que esté no contenida en la del driver
            timeout (int): cantidad máxima de tiempo a esperar antes de lanzar una excepción

        Returns:
            None
        """
        self.get_wait(timeout).until_not(ec.url_contains(url))

    def wait_for_text_in_element_value(self, locator: "Locator", text: str, timeout: int = _DEFAULT_TIMEOUT) -> None:
        """
        Espera que el elemento definido por locator tenga un texto en el atributo value. Es decir, si tengo
        <EtiquetaHTML value="un_valor">ASDASD</EtiquetaHTML> este método va a esperar que "un_valor" esté contenido en
        value

        :param locator: objeto que abstrae el elemento a esperar
        :param text: texto que esperamos que tenga el elemento en atributo value
        :param timeout: cantidad máxima de tiempo a esperar antes de lanzar una excepción (opcional)
        :return: None
        """
        self.get_wait(timeout).until(ec.text_to_be_present_in_element_value(locator, text),
                                     message=f"Esperaba que el elemento tuviera el texto {text} en el atributo value,"
                                             f"pero no lo tenía")

    def wait_for_title(self, title: str) -> None:
        """
        Espera que el título de la página sea igual al enviado por parámetro

        Args:
            title (str): título que esperamos que sea igual a la del driver

        Returns:
            None
        """
        self.wait.until(ec.title_is(title))

    def wait_for_stale_element(self, element: "WebElement", timeout: int = _DEFAULT_TIMEOUT) -> None:
        """
        Espera a que un elemento desaparezca del DOM

        Args:
            element (WebElement): un WebElement de webdriver que representa el elemento. NO es un Locator
            timeout: cantidad máxima de tiempo a esperar antes de lanzar una excepción

        Returns:
            None
        """
        self.get_wait(timeout).until(ec.staleness_of(element),
                                     message="Esperaba que el elemento desapareciera del DODM pero no lo hizo")

    def switch_to_alert_and_accept_it(self) -> None:
        """
        Espera que se presente un alert y luego lo acepta, bajo la opcion considerada como aceptar

        Returns:
            None
        """
        self.wait.until(ec.alert_is_present()).accept()

    def switch_to_alert_and_dismiss_it(self) -> None:
        """
        Espera que se presente un alert y luego lo rechaza, bajo la opción considerada como cancelar

        Returns:
            None
        """
        self.wait.until(ec.alert_is_present()).dismiss()

    def switch_to_default_content(self) -> None:
        """
        Cambia el contexto al por defecto

        Returns:
             None
        """
        return self.driver.switch_to.default_content()

    def switch_to_default_window(self) -> None:
        """
        Cambia el foco a la primer pestaña

        Returns:
            None
        """
        self.driver.switch_to.window(self.driver.window_handles[0])

    def wait_and_switch_to_new_window(self, current_handles) -> None:
        """
        Cambia el contexto a la última pestaña abierta

        Args:
            current_handles: cantidad de ventanas actuales

        Returns:
            None
        """
        self.wait.until(ec.new_window_is_opened(current_handles))
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def clear_elements_text(self, *locators) -> None:
        """
        Deja vacío el campo value de los locators indicados

        Args:
            *locators (*List[Locator]): objetos de tipo Locator separados por coma, que son a los que se les va a
                borrar el valor en el atributo 'value'

        Returns:
            None
        """
        ac = ActionChains(self.driver)
        [ac.clear(e) for e in [self.find_element(l) for l in locators]]
        ac.perform()
        [self.element_text_equals(l, '') for l in locators]

    def element_has_text(self, locator: "Locator", text: str, timeout: int = _DEFAULT_TIMEOUT) -> None:
        """
        Espera que el elemento contenga el texto proporcionado. Se refiere al texto encerrado entre las etiquetas
        HTML. Es decir <TagHTML>Este valor</TagHTML>

        Args:
            locator (Locator): objeto que abstrae el elemento a esperar
            text (str): valor esperado del texto
            timeout (int): cantidad máxima de tiempo a esperar antes de lanzar una excepción

        Returns:
            None
        """
        self.__wait_for_element(locator)
        self.get_wait(timeout).until(element_has_text(self.driver, locator.ret_locator, text),
                                     message=f"{locator.ret_locator} no contiene el texto especificado")

    def element_text_equals(self, locator: "Locator", text: str) -> None:
        """
        Espera que el texto del elemento sea igual al proporcionado. Se refiere al texto encerrado entre las etiquetas
        HTML. Es decir <TagHTML>Este valor</TagHTML>

        Args:
            locator (Locator): objeto que abstrae el elemento a esperar
            text (str): valor esperado del texto

        Returns:
            None
        """
        self.__wait_for_element(locator)
        self.wait.until(element_text_to_be_equal(self.driver, locator.ret_locator, text),
                        message=f"{locator.ret_locator} no contiene el texto especificado")

    def child_element_text_equals(self, parent, locator, text):
        self.wait.until(element_has_text(parent, locator.ret_locator, text),
                        message=f"{locator.ret_locator} no contiene el texto especificado")

    def child_element_text_has_text(self, parent, locator, text):
        self.wait.until(element_has_text(parent, locator, text),
                        message=f"{locator.ret_locator} no contiene el texto especificado")


# endregion

# region Locator
class Locator:
    """
    Abstraigo un localizador como una clase.
    """

    def __init__(self, by, name):
        self._by = by
        self._name = name

    @property
    def ret_locator(self):
        """
        Accesor que permite devolver los valores de una instancia de clase Locator

        Returns:
            Tuple[str, str]: retorna los atributos de la instancia como una tupla con la estrategia y el valor
        """
        return self._by, self._name

    @property
    def ret_name(self):
        return self._name

    def formatear_locator(self, value):
        """
        Dado un locator, retorna otro formateado según los valores en un mapeador.

        Args:
            value: diccionario que mapea valores clave-valor
            
        Returns:
            Locator: con los parámetros reemplazados.
        """
        return Locator(self._by, self._name.format(**value))

    def __iter__(self):
        return iter(self.ret_locator)


# endregion

# region ECs

class element_text_to_be_equal(object):
    """ An expectation for checking if the given text is equal to the
    specified element child.
    locator, text
    """

    def __init__(self, parent, locator, text):
        self.parent = parent
        self.locator = locator
        self.text = text

    def __call__(self, ignored):
        element = self.parent.find_element(*self.locator)
        text = element.text or element.get_attribute("value")
        print(f'\n"{text}" == "{self.text}" (O == E)')
        return self.text == text


class element_has_text(object):
    """ An expectation for checking if the given text is present in the
    specified element child.
    locator, text
    """

    def __init__(self, parent, locator, text):
        self.parent = parent
        self.locator = locator
        self.text = text

    def __call__(self, ignored):
        element = self.parent.find_element(*self.locator)
        text = element.text or element.get_attribute("value")
        print(f'\n"{text}" in "{self.text}" (E in O)')
        try:
            return self.text in text
        except TypeError:
            pass  # puede que aun no se haya cargado el texto y este devolviendo none


# endregion


class ActionChains(_ActionChains):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def clear(self, elem):
        txt = elem.text or elem.get_attribute('value')
        if txt:
            self.click(elem)
            self.send_keys(Keys.END)
            for i in txt:
                self.send_keys(Keys.BACKSPACE)
        return self
