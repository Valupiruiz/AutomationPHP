from appium.webdriver.common.mobileby import MobileBy
from src.mobile.user_interface.base_screen import UiLocator


class MainLocators:
    EMPEZAR = UiLocator(
        MobileBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.ViewGroup").childSelector('
        'new UiSelector().className("android.widget.TextView").text("Empezar")'
        ')'
    )
    FEED_TAB = UiLocator(MobileBy.ACCESSIBILITY_ID, "Feed, tab, 1 of 4")
    BUSQUEDA_TAB = UiLocator(MobileBy.ACCESSIBILITY_ID, "Busqueda, tab, 2 of 4")
    CREAR_FEED_TAB = UiLocator(MobileBy.ACCESSIBILITY_ID, "Crear feed, tab, 3 of 4")
    USUARIO_TAB = UiLocator(MobileBy.ACCESSIBILITY_ID, "Usuario, tab, 4 of 4")

