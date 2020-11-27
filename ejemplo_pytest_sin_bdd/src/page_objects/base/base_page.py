import warnings
from contextlib import contextmanager

from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException, \
    ElementNotVisibleException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains as _ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

# region globals
_DEFAULT_TIMEOUT = 30
_IGNORED_EXCEPTIONS = (StaleElementReferenceException, ElementNotInteractableException, ElementNotVisibleException)


# endregion

# region BasePage

class BasePage:

    def __init__(self, driver, validar_pagina):
        self.driver = driver
        self.timeout = _DEFAULT_TIMEOUT
        self.wait = WebDriverWait(self.driver, self.timeout, ignored_exceptions=_IGNORED_EXCEPTIONS)
        self._next_page = None
        self.__observer = None
        if validar_pagina:
            self._validar_pantalla()

    def get_wait(self, timeout):
        """Cuando hay que utilizar un timeout distinto al default,
        utiliza un wait diferente al del constructor"""
        if timeout == _DEFAULT_TIMEOUT:
            return self.wait
        return WebDriverWait(self.driver, timeout, ignored_exceptions=_IGNORED_EXCEPTIONS)

    def find_element(self, locator, timeout=_DEFAULT_TIMEOUT):
        """
        Encuentra el elemento definido por locator y ademas lo espera
        :param locator: el locator del elemento a encontrar
        :param timeout
        :return: un tipo WebElement
        """
        self.wait_until_element_interactable(locator, timeout)

        return self.driver.find_element(*locator.ret_locator)

    def get_element_text(self, locator, timeout=_DEFAULT_TIMEOUT):
        return self.get_wait(timeout).until(element_return_text(self.driver, locator),
                                            message="No se pudo obtener el texto del elemento")

    def get_elements_text(self, locator, timeout=_DEFAULT_TIMEOUT):
        return self.get_wait(timeout).until(elements_return_text(self.driver, locator),
                                            message="No se pudo obtener el texto de los elementos")

    def get_child_text(self, parent, locator, timeout=_DEFAULT_TIMEOUT):
        return self.get_wait(timeout).until(element_return_text(parent, locator),
                                            message="No se pudo obtener el texto del hijo")

    def get_childs_text(self, parent, locator, timeout=_DEFAULT_TIMEOUT):
        return self.get_wait(timeout).until(elements_return_text(parent, locator),
                                            message="No se pudo obtener el texto de los hijos")

    def find_elements(self, locator, timeout=_DEFAULT_TIMEOUT):
        """
        Encuentra los elementos definidos por locator
        :param locator: el locator de los elementos a encontrar
        :param timeout: Timeout
        :return: una lista con WebElements encontrados
        """
        self.wait_until_elements_interactable(locator, timeout)
        return self.driver.find_elements(*locator.ret_locator)

    def find_select(self, locator):
        """
        Encuentra el select definido por locator
        :param locator: el locator del select a encontrar
        :return: un elemento de tipo Select
        """

        return Select(self.wait_for_element(locator))

    def wait_for_element(self, locator, timeout=_DEFAULT_TIMEOUT):
        """
        Espera que el elemento este visible
        :param locator: el locator del elemento a esperar
        :param timeout, si es distinto del default, lo utiliza
        :return: un WebDriverWait del elemento
        """

        return self.get_wait(timeout).until(ec.presence_of_element_located(locator.ret_locator),
                                            message=f"No se encontro el elemento {locator.ret_locator}")

    def wait_for_elements(self, locator, timeout=_DEFAULT_TIMEOUT):
        """
        Espera que los elementos esten visibles y habilitados
        :param locator: el locator de los elementos a esperar
        :param timeout, si es distinto del default, lo utiliza
        """

        return self.get_wait(timeout).until(ec.presence_of_all_elements_located(locator.ret_locator),
                                            message=f"No se encontro ningun elemento en {locator.ret_locator}")

    def wait_until_element_interactable(self, locator, timeout=_DEFAULT_TIMEOUT):
        """
        Waits until an element is interactable. This means its visible and is enabled

        :param locator: locator for the element to wait for.
        :param timeout: max seconds to wait for the element to be clickable.
        """

        self.get_wait(timeout).until(ec.element_to_be_clickable(locator.ret_locator),
                                     message=f"No se encontro el elemento {locator.ret_locator}")

    def wait_until_elements_interactable(self, locator, timeout=_DEFAULT_TIMEOUT):
        self.get_wait(timeout).until(ec.visibility_of_all_elements_located(locator.ret_locator),
                                     message=f"No se encontraron los elementos {locator.ret_locator}")

    def wait_for_check_status(self, locator, checked=True, timeout=_DEFAULT_TIMEOUT):
        """
        Waits until an element is checked

        :param locator: locator for the element to wait for.
        :param timeout: max seconds to wait for the element to be clickable.
        :param checked: expected check status
        :return: Element
        :raises: TimeoutException
        """

        wait = self.get_wait(timeout)

        if checked:
            wait.until(ec.element_located_to_be_selected(locator.ret_locator))
        else:
            wait.until_not(ec.element_located_to_be_selected(locator.ret_locator))

    def wait_for_element_invisibility(self, locator, timeout=_DEFAULT_TIMEOUT):
        """
        Espera que el elemento definido por locator este invisible
        :param locator: el locator del elemento a esperar que no sea visible
        :param timeout
        :return: un WebDriverWait del elemento
        """
        self.get_wait(timeout).until(ec.invisibility_of_element_located(locator.ret_locator))

    def wait_for_url(self, url, timeout=_DEFAULT_TIMEOUT):
        self.get_wait(timeout).until(ec.url_contains(url),
                                     message=f"Esperaba la URL {url} y obtuve {self.driver.current_url}")

    def wait_until_not_url(self, url, timeout=_DEFAULT_TIMEOUT):
        self.get_wait(timeout).until_not(ec.url_contains(url))

    def wait_for_title(self, title):
        self.wait.until(ec.title_is(title))

    def wait_for_stale_element(self, element, timeout=_DEFAULT_TIMEOUT):
        """
        Espera a que el elemento desaparezca del DOM
        """

        self.get_wait(timeout).until(ec.staleness_of(element), message="Esperaba que el elemento se volviera stale")

    def switch_to_alert_and_accept_it(self):
        """
        Espera que se presente un alert y luego lo acepta, bajo la opcion considerada como aceptar
        :return: un handler para el accept
        """
        return self.wait.until(ec.alert_is_present()).accept()

    def switch_to_alert_and_dismiss_it(self):
        """
        Espera que se presente un alert y luego lo rechaza
        :return: un handler para el accept
        """
        return self.wait.until(ec.alert_is_present()).dismiss()

    def switch_to_default_content(self):
        """
        Cambia el contexto al por defecto
        :return: handler del contexto
        """
        return self.driver.switch_to.default_content()

    def switch_to_default_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def wait_and_switch_to_new_window(self, current_handles):
        self.wait.until(ec.new_window_is_opened(current_handles))
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def clear_elements_text(self, *locators):
        ac = ActionChains(self.driver)
        [ac.clear(e) for e in [self.find_element(l) for l in locators]]
        ac.perform()
        [self.element_text_equals(l, '') for l in locators]

    def element_has_text(self, locator, text, timeout=_DEFAULT_TIMEOUT):
        """
        Espera que el elemento contenga el texto proporcionado(text in element.text)
        """
        self.wait_for_element(locator)
        self.get_wait(timeout).until(element_has_text(self.driver, locator.ret_locator, text),
                                     message=f"{locator.ret_locator} no contiene el texto especificado")

    def element_text_equals(self, locator, text):
        """
        Espera que el texto del elemento sea igual al proporcionado(text == element.text)
        """
        self.wait_for_element(locator)
        self.wait.until(element_text_to_be_equal(self.driver, locator.ret_locator, text),
                        message=f"{locator.ret_locator} no contiene el texto especificado")

    def child_element_text_equals(self, parent, locator, text):
        self.wait.until(element_has_text(parent, locator.ret_locator, text),
                        message=f"{locator.ret_locator} no contiene el texto especificado")

    def child_element_text_has_text(self, parent, locator, text):
        self.wait.until(element_has_text(parent, locator, text),
                        message=f"{locator.ret_locator} no contiene el texto especificado")

    @contextmanager
    def stale_element(self, locator=None, e=None):
        if not locator and not e:
            raise Exception()

        if locator:
            e = self.find_element(locator)
        yield e
        self.wait_for_stale_element(e)

    def get_toast(self):
        locator_toast = Locator("css selector", ".Toastify__toast-body")
        return self.get_wait(_DEFAULT_TIMEOUT).until(lambda x: self.find_element(locator_toast).text, message="F toast")

    def dismiss_toast(self):
        try:
            locator_toast = Locator("css selector", ".Toastify__toast-body")
            with self.stale_element(locator_toast) as e:
                self.driver.execute_script("arguments[0].click()", e)
        except TimeoutException as e:
            print("pincho el dismiss", e)

    def _validar_pantalla(self):
        raise NotImplementedError()

    @property
    def next_page(self):
        return self._next_page

    @next_page.setter
    def next_page(self, val):
        self._next_page = val
        self.__observer.notify()

    @property
    def observer(self):
        return self.__observer

    @observer.setter
    def observer(self, new_observer):
        self.__observer = new_observer


# endregion

# region Locator
class Locator:
    def __init__(self, by, name):
        self._by = by
        self._name = name

    @property
    def ret_locator(self):
        return self._by, self._name

    @property
    def ret_name(self):
        return self._name

    def format_locator(self, *formatos):
        # Retorna un nuevo Locator con el formato aplicado
        # si es una tupla utilizo * para aplicar todos los formatos
        return Locator(self._by, self._name.format(*formatos))

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


class element_return_text(object):

    # en ocasiones, .text devuelve '' a pesar de que tenga texto ¯\_(ツ)_/¯
    def __init__(self, parent, locator):
        self.parent = parent
        self.locator = locator

    def __call__(self, ignored):
        element = self.parent.find_element(*self.locator)
        return element.text or element.get_attribute("value")


class elements_return_text(object):

    # en ocasiones, .text devuelve '' a pesar de que tenga texto ¯\_(ツ)_/¯
    def __init__(self, parent, locator):
        self.parent = parent
        self.locator = locator

    def __call__(self, ignored):
        elements = self.parent.find_elements(*self.locator)
        oks = 0
        txts = []
        for element in elements:
            txt = element.text or element.get_attribute("value")
            if txt:
                oks += 1
                txts.append(txt)
        if oks == len(elements):
            return txts
        return False


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


# region Mockers
class BaseMock:

    def __getattr__(self, item):
        print(self, item)
        if item in ['observer', 'next_page']:
            return getattr(self, item)
        return Mock


class __ActionChains(BaseMock):

    def __init__(self, *args):
        pass

    def __getattr__(self, item):
        print(self, item)
        if item in ['observer', 'next_page']:
            return getattr(self, item)
        return Mock


class _BasePage(BaseMock):

    def __init__(self, *args):
        self.__observer = None
        self._next_page = None

    @property
    def next_page(self):
        return self._next_page

    @next_page.setter
    def next_page(self, val):
        self._next_page = val
        self.__observer.notify()

    @property
    def observer(self):
        return self.__observer

    @observer.setter
    def observer(self, new_observer):
        self.__observer = new_observer


class Mock:

    def __init__(self, *args):
        pass

    def __call__(self, *args, **kwargs):
        return self._mock

    def __getattr__(self, item):
        return self._mock

    def __len__(self):
        return 1

    def __repr__(self):
        return "True"

    def __add__(self, other):
        return 1

    def __sub__(self, other):
        return 1

    def __eq__(self, other):
        return True

    @staticmethod
    def _mock(*args):
        print(__name__, *args)
        return Mock()

    @staticmethod
    def refresh():
        pass

# endregion
