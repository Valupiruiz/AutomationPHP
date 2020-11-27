from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, \
    StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from appium.webdriver.common.mobileby import MobileBy
from typing import List
from src.mobile.app_utils.app_constants import TeclaAndroid, OrientacionDispositivo, SwipeTo, ScrollTo
from src.mobile.app_utils.exceptions import *
import time

_DEFAULT_TIMEOUT = 10


class BaseScreen:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = _DEFAULT_TIMEOUT
        self.wait = WebDriverWait(self.driver, _DEFAULT_TIMEOUT)

    def get_wait(self, timeout):
        if timeout == _DEFAULT_TIMEOUT:
            return self.wait
        return WebDriverWait(self.driver, timeout)

    def find_element(self, ui_locator: "UiLocator", timeout: int = _DEFAULT_TIMEOUT) -> WebElement:
        """
        Espera y encuentra el elemento definido por ui_locator
        Args:
            timeout: cantidad máxima de tiempo a esperar antes de lanzar una excepción
            ui_locator (UiLocator): define una estrategia y un valor para encontrar un elemento
        Returns:
            (WebElement): WebElement que representa al elemento encontrado
        """
        self.__wait_for_element(ui_locator, timeout)
        return self.driver.find_element(*ui_locator.get)

    def find_elements(self, ui_locator: "UiLocator", timeout: int = _DEFAULT_TIMEOUT) -> List[WebElement]:
        """
        Espera y encuentra los elementos definidos por ui_locator
        Args:
            timeout: cantidad máxima de tiempo a esperar antes de lanzar una excepción
            ui_locator (UiLocator): define una estrategia y un valor para encontrar un elemento
        Returns:
            (List[WebElement]): lista de WebElements que representan a los elementos encontrados
        """
        self.__wait_for_elements(ui_locator, timeout)
        return self.driver.find_elements(*ui_locator.get)

    def wait_for_element_invisibility(self, ui_locator: "UiLocator", timeout: int = _DEFAULT_TIMEOUT) -> None:
        """
        Espera que un elemento no sea visible ni se encuentre en el source
        Args:
            timeout: cantidad máxima de tiempo a esperar antes de lanzar una excepción
            ui_locator (UiLocator): define una estrategia y un valor para encontrar un elemento
        Returns:
            (NoneType)
        """
        self.get_wait(timeout).until(ec.invisibility_of_element(ui_locator.get))

    def __wait_for_element(self, ui_locator: "UiLocator", timeout) -> WebElement:
        """
        Método privado que espera la existencia y presencia de un elemento, hasta el timeout.
        Args:
            ui_locator (UiLocator): define una estrategia y un valor para encontrar un elemento
        Returns:
            (WebElement): WebElement que representa al elemento esperado
        """
        self.get_wait(timeout).until(ec.presence_of_element_located(ui_locator.get))
        return self.wait.until(ec.element_to_be_clickable(ui_locator.get))

    def __wait_for_elements(self, ui_locator: "UiLocator", timeout: int = _DEFAULT_TIMEOUT) -> List[WebElement]:
        """
        Método privado que espera la existencia y presencia de un conjunto de elementos, hasta el timeout
        Args:
            ui_locator: define una estrategia y un valor para encontrar un elemento
        Returns:
            (List[WebElement]): lista de WebElements que representan a los elementos esperados
        """
        self.get_wait(timeout).until(ec.presence_of_all_elements_located(ui_locator.get))
        return self.get_wait(timeout).until(ec.visibility_of_all_elements_located(ui_locator.get))

    def get_source(self) -> str:
        """
        Obtiene el cuerpo de la pantalla que estemos visualizando, es decir un HTML, XMl U otra.
        Returns:
            (str): source de la pantalla
        """
        return self.driver.page_source

    def get_geolocation(self) -> dict:
        """
        Obtiene la localización global del dispositivo.
        Returns:
            (dict): conteniendo pares clave-valor, con claves "x", "y", "z"
        """
        return self.driver.location

    def get_current_activity(self) -> str:
        """
        Obtiene el nombre del activity que esté actualmente desplegado.
        Returns:
            (str): contiene el nombre el activity
        """
        return self.driver.current_activity

    def switch_to_webview(self) -> None:
        """
        Obtiene los contextos y switchea al último. Esto permite cambiar entre webview y app nativa
        Returns:
            (NoneType)
        """
        webview = self.driver.contexts[-1]
        self.driver.switch_to.context(webview)

    def switch_to_default(self) -> None:
        """
        Obtiene los contextos y switchea a la app nativa
        Returns:
            (NoneType)
        """
        self.driver.switch_to.context(self.driver.contexts[0])

    def toggle_wifi(self) -> None:
        """
        Prende o apaga el wifi en el dispositivo.
        Returns:
            (NoneType)
        """
        self.driver.toggle_wifi()

    @property
    def orientation(self) -> str:
        """
        Obtiene la orientación actual del dispositivo
        Returns:
            (str): con el nombre de la orientación. Uno de ['LANDSCAPE', 'PORTRAIT']
        """
        return self.driver.orientation

    @orientation.setter
    def orientation(self, valor: OrientacionDispositivo) -> None:
        """
        Cambia la orientación actual del dispositivo
        Args:
            valor (OrientacionDispositivo): es el valor de la orientación. Uno de ['LANDSCAPE', 'PORTRAIT']
        Returns:
            (NoneType)
        """
        self.driver.orientation = valor

    def lock_device(self) -> None:
        """
        Bloquea el dispositivo
        Returns:
            (NoneType)
        """
        self.driver.lock()

    def unlock_device(self) -> None:
        """
        Desbloquea el dispositivo
        Returns:
            (NoneType)
        """
        self.driver.unlock()

    @property
    def is_locked(self) -> bool:
        """
        Determina si el dispositivo está bloqueado o no lo está
        Returns:
            (bool): True si está bloqueado, False si no lo está
        """
        return self.driver.is_locked()

    def press_android_key(self, codigo: TeclaAndroid) -> None:
        """
        Presiona una tecla Android
        Args:
            codigo (TeclaAndroid): valor entero que representa a la tecla.
        Returns:
            (NoneType)
        """
        self.driver.press_keycode(codigo)

    def press_and_hold_android_key(self, codigo: TeclaAndroid) -> None:
        """
        Presiona y mantiene presionada una tecla Android
        Args:
            codigo (TeclaAndroid): valor entero que representa a la tecla.
        Returns:
            (NoneType)
        """
        self.driver.long_press_keycode(codigo)

    def hide_keyboard(self) -> None:
        """
        Oculta el teclado si es que está actualmente visible.
        Returns:
            (NoneType)
        """
        self.driver.hide_keyboard()

    def is_keyboard_shown(self) -> bool:
        """
        Determina si el teclado está actualmente desplegado.
        Returns:
            (bool): True si está visible, False si no lo está.
        """
        return self.driver.is_keyboard_shown()

    def t_single_tap(self, locator: "UiLocator") -> TouchAction:
        """
        Performa un toque sobre un elemento.
        Args:
            locator (UiLocator): define una estrategia y un valor para encontrar un elemento
        Returns:
            (TouchAction): handler con una acción para seguir encadenando gestos.
        """
        action = TouchAction(self.driver)
        return action.tap(self.find_element(locator)).perform()

    def t_double_tap(self, locator: "UiLocator") -> TouchAction:
        """
        Performa dos toques seguidos sobre un elemento.
        Args:
            locator (UiLocator): define una estrategia y un valor para encontrar un elemento
        Returns:
            (TouchAction): handler con una acción para seguir encadenando gestos.
        """
        action = TouchAction(self.driver)
        return action.tap(self.find_element(locator), count=2).perform()

    def __hold_and_slide(self, first_locator, second_locator):
        """
        WORK IN PROGRESS
        Args:
            first_locator:
            second_locator:

        Returns:

        """
        # TBD
        # actions = TouchAction(self.driver)
        # source_element = self.find_element(first_locator)
        # actions.long_press(source_element, 1750).perform()
        # destiny_element = self.find_element(second_locator)
        # actions.wait(2000).move_to(destiny_element).wait(2000).release().perform()
        raise Exception("metodo aun no implementado")

    def t_pinch_open(self, locator: "UiLocator") -> MultiAction:
        """
        Performa el gesto de apertura de dedos (equivalente al gesto de zoom) sobre un elemento.
        Args:
            locator (UiLocator): define una estrategia y un valor para encontrar un elemento
        Returns:
            (MultiAction): handler de multi-acción para seguir encadenando gestos.
        """
        try:
            element = self.find_element(locator)
        except ElementNotVisibleException as e:
            raise ElementoNoVisible(
                "el elemento requerido no se encuentra actualmente visible!",
                self.get_current_activity(), e.stacktrace
            ) from e
        except (NoSuchElementException, StaleElementReferenceException) as e:
            raise ElementoNoEncontrado(
                "el elemento requerido no pudo ser localizado. Intentá eliminar la referencia que ya tenés o bien, "
                "intentá esperar a que esté presente. De última...sale time sleep bro ;)",
                self.get_current_activity(), e.stacktrace, locator
            )
        x = element.location["x"] + element.size["width"]/2
        y = element.location["y"] + element.size["height"]/2
        actions = MultiAction(self.driver)
        first_finger = TouchAction(self.driver)
        second_finger = TouchAction(self.driver)
        first_finger.press(x=x-200, y=y+200) \
            .wait(500) \
            .move_to(x=x-500, y=y+500) \
            .wait(750) \
            .release()
        second_finger.press(x=x+200, y=y-200) \
            .move_to(x=x+500, y=y-500) \
            .release()
        actions.add(first_finger)
        actions.add(second_finger)
        actions.perform()
        return actions

    def t_swipe(self, locator, orientacion: SwipeTo) -> TouchAction:
        """
        Performa un desplazamiento lateral sobre el elemento
        Args:
            locator (UiLocator): define una estrategia y un valor para encontrar un elemento
            orientacion (SwipeTo): define hacia donde se realiza el gesto. Left = Muevo el DEDO hacia la izquierda.
        Returns:
            (TouchAction): handler para seguir encadenando gestos.
        """
        touch = TouchAction(self.driver)
        element = self.find_element(locator)
        partial = touch.press(element).wait(2000)
        if not orientacion:
            partial = partial.move_to(element, x=element.size["width"]/2 - 500, y=element.size["height"]/2)
        else:
            partial = partial.move_to(element, x=element.size["width"]/2 + 500, y=element.size["height"]/2)
        partial.release().perform()
        return partial

    def t_scroll_screen(self, orientacion: ScrollTo) -> TouchAction:
        touch = TouchAction(self.driver)
        screen = UiLocator(MobileBy.CLASS_NAME, "android.widget.FrameLayout")
        element = self.find_element(screen)
        partial = touch.press(element).wait(2000)
        if not orientacion:
            partial = partial.move_to(x=element.size["width"]/2, y=10)
        else:
            partial = partial.move_to(x=element.size["width"]/2, y=element.size["height"]-10)
        partial.release().perform()
        return partial

    def t_scroll_element(self, locator, orientacion: ScrollTo):
        """
        Performa deslizamiento vertical desde el centro de un elemento hacia arriba o hacia abajo
        :param locator: instancia de tipo UiLocator con la strategy para encontrar un elemento
        :param orientacion: orientacion arriba o abajo (definida por ScrollTo)
        :return: None
        """
        touch = TouchAction(self.driver)
        element = self.find_element(locator)
        partial = touch.press(element).wait(2000)
        if not orientacion:
            partial = partial.move_to(element, x=element.size["width"]/2, y=element.size["height"] - 500)
        else:
            partial = partial.move_to(element, x=element.size["width"]/2, y=element.size["height"] + 500)
        partial.release().perform()

    def scroll_until_element_appears(self, locator: "UiLocator", timeout=10) -> WebElement:
        timeout_exit = time.time() + timeout
        while timeout_exit > time.time():
            self.t_scroll_screen(ScrollTo.UP)
            a = self.driver.find_element(*locator.get)
            if a:
                return a
            else:
                continue
        raise ElementoNoEncontrado(
            "A pesar de scrollear, no se encontró el elemento. Intente con un timeout más elevado y verifique que el"
            "localizador sea correcto",
            self.get_current_activity()
        )

    # region iOS
    def install_app(self, path):
        self.driver.install_app(path)

    # endregion

    # region Emuladores

    def set_power_percent(self, percent):
        self.driver.set_power_capacity(percent)

    def set_power_connection(self, bool_power):
        self.driver.set_power_ac(bool_power)

    # endregion


class UiLocator(object):
    def __init__(self, mobile_by, attribute):
        self._mobile_by = mobile_by
        self._property = attribute

    @property
    def get(self):
        return self._mobile_by, self._property

    def format_locator(self, template_options):
        return UiLocator(self._mobile_by, self._property.format(**template_options))
